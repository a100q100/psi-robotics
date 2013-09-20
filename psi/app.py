# =============================================================================
# Federal University of Rio Grande do Sul (UFRGS)
# Connectionist Artificial Intelligence Laboratory (LIAC)
# Renato de Pontes Pereira - renato.ppontes@gmail.com
# =============================================================================
# Copyright (c) 2011 Renato de Pontes Pereira, renato.ppontes at gmail dot com
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights 
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in 
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# =============================================================================

import numpy as np

import os
import sys
import wx
import psi
import time
import threading

from tools import project_handler
from psi.tools.timer import Timer as psiTimer

__all__ = ['App']

class Timer(wx.Timer):
    def __init__(self, callback):
        super(Timer, self).__init__()
        self.callback  = callback

    def Notify(self):
        tick = self.GetInterval()/1000.0
        self.callback(tick)

class SimulationThread(threading.Thread):
    def __init__(self):
        super(SimulationThread, self).__init__()

    def run(self):
        try:
            t = 1./psi.config.UPDATE_TIME
            while True:
                if psi.app.state == psi.STATE_RUNNING:
                    # timer = psiTimer()
                    # timer.tic()
                    psi.app.on_update(t)
                    # t = timer.toc()
                    # print 'thread.run: %.4f seconds'%t


                if psi.app.state == psi.STATE_STOPPED: 
                    break

                time.sleep(t)
            print 'leaving thread'
        except Exception as e:
            type_ = str(e.__class__.__name__)
            psi.log.error('%s: %s'%(type_, e.message))

class App(object):
    '''The psi application.

    This is the main class of psi framework, performing the role of dispatching 
    system events and initializing the global variables of the framework.
    '''

    def __init__(self):
        self._wx_app = wx.App(redirect=False)
        self._draw_timer = Timer(self.on_draw) #wx.Timer(self._wx_app)
        # self._update_timer = Timer(self.on_update)
        # self._queue = Queue.Queue()
        self._simulation = None

        self.state = psi.STATE_STOPPED
        self.project_path = None
        self.project_name = 'Untitled'
        self.project_modified = False
        # self._wx_app.Bind(wx.EVT_TIMER, self._on_timer

        psi.splash = psi.gui.SplashScreen(psi.window)
        psi.splash.Show()

        # Initializes the global variables
        psi.log = psi._log.Log(100)
        psi.app = self
        psi.window = psi.gui.MainWindow()
        psi.graphics = psi.engine.Graphics()
        psi.manager = psi.core.Manager()

        psi.log.info('Ready')
        psi.window.set_status_simulation(self.state)
        psi.window.set_window_title(self.project_name)
        self.on_pre_load()

    def main_loop(self):
        psi.window.Show()
        psi.splash.Close()
        # import time
        
        # event_loop = wx.EventLoop()
        # wx.EventLoop.SetActive(event_loop)

        # while True:
        #     while event_loop.Pending():
        #         event_loop.Dispatch()
        #         self._wx_app.ProcessPendingEvents()
        #         # while self._wx_app.Pending():
        #         #     self._wx_app.Dispatch()
        # # time.sleep(0.1)
        # self._wx_app.ProcessIdle()

        self._wx_app.MainLoop()

    # =========================================================================
    # MAIN FUNCTIONS
    # =========================================================================
    # COMPONENT CONTROL
    def add_component(self, component):
        psi.window.add_component(component)
        psi.manager.add(component)
        self.project_modified = True
    
    def remove_component(self, component):
        psi.window.remove_component(component)
        psi.manager.remove(component)
        self.project_modified = True

    # PROJECT CONTROL
    def new_project(self):
        self.project_path = None
        self.project_name = 'Untitled'
        self.project_modified = False

        psi.window.clear_components()
        psi.window.set_window_title(self.project_name)
        psi.manager.clear()

    def save_project(self):
        self.save_project_as(self.project_path)

    def save_project_as(self, path):
        project_handler.save_as(path)

        self.project_path = path
        self.project_name = os.path.basename(path)[:-4]
        self.project_modified = False
        psi.log.info('Project saved as "%s.psi".'%self.project_name)
        psi.window.set_window_title(self.project_name)

    def open_project(self, path):
        psi.window.clear_components()
        psi.manager.clear()
        
        project_handler.open(path)
        self.project_path = path
        self.project_name = os.path.basename(path)[:-4]
        psi.log.info('Project opened from "%s.psi".'%self.project_name)
        psi.window.set_window_title(self.project_name)

    def is_project_opened(self):
        return self.project_path is not None

    # SIMULATION CONTROL
    def run_simulation(self):
        psi.window.deselect_component()

        self.state = psi.STATE_RUNNING
        psi.window.set_status_simulation(psi.STATE_RUNNING)
        psi.window.disable_menu_item(psi.ID_RUN)
        psi.window.disable_menu_item(psi.ID_RESUME)
        psi.window.enable_menu_item(psi.ID_PAUSE)
        psi.window.enable_menu_item(psi.ID_STOP)

        self.on_run()

    def pause_simulation(self):
        self.state = psi.STATE_PAUSED
        psi.window.set_status_simulation(psi.STATE_PAUSED)
        psi.window.disable_menu_item(psi.ID_RUN)
        psi.window.disable_menu_item(psi.ID_PAUSE)
        psi.window.enable_menu_item(psi.ID_RESUME)
        psi.window.enable_menu_item(psi.ID_STOP)

        self.on_pause()

    def resume_simulation(self):
        self.state = psi.STATE_RUNNING
        psi.window.set_status_simulation(psi.STATE_RUNNING)
        psi.window.disable_menu_item(psi.ID_RUN)
        psi.window.enable_menu_item(psi.ID_PAUSE)
        psi.window.disable_menu_item(psi.ID_RESUME)
        psi.window.enable_menu_item(psi.ID_STOP)

        self.on_resume()

    def stop_simulation(self):
        self.state = psi.STATE_STOPPED
        psi.window.set_status_simulation(psi.STATE_STOPPED)
        psi.window.enable_menu_item(psi.ID_RUN)
        psi.window.disable_menu_item(psi.ID_PAUSE)
        psi.window.disable_menu_item(psi.ID_RESUME)
        psi.window.disable_menu_item(psi.ID_STOP)

        self.on_stop()

    # CAMERA CONTROL
    def center_camera(self):
        size = psi.window.canvas.canvas_size
        psi.graphics.camera.pos = psi.euclid.Vector2(0, 0)
        psi.graphics.camera.pan(-size/2.)

    def follow_robot_camera(self):
        pass

    def zoom_in(self):
        psi.graphics.camera.zoom_in()

    def zoom_out(self):
        psi.graphics.camera.zoom_out()

    def reset_zoom(self):
        psi.graphics.camera.reset_zoom()

    def toogle_grid(self):
        pass

    # =========================================================================

    # =========================================================================
    # EVENTS
    # =========================================================================
    def on_pre_load(self):
        psi.graphics.on_pre_load()

    def on_init(self):
        print 'at psi.app.on_init.'
        psi.graphics.on_init()
        self._draw_timer.Start(1000/psi.config.DRAW_TIME)
        # self._update_timer.Start(1000/psi.config.UPDATE_TIME)

    def on_quit(self):
        print 'at psi.app.on_quit.'
        psi.graphics.on_quit()
        # psi.manager.on_quit()
        if self.state != psi.STATE_STOPPED:
            self.stop_simulation()
        sys.exit()


    def on_draw(self, tick):
        # print 'on-drw', tick
        # pass#print 'at psi.app.on_draw.'
        # timer = psiTimer()
        # timer.tic()
        psi.manager.on_draw(tick)
        psi.graphics.on_draw(tick)
        psi.window.canvas.swap_buffers()
        # t = timer.toc()
        # print 'app.on_draw: %.4f seconds'%t

    def on_run(self):
        psi.log.info('Initializing components...')
        psi.manager.on_run()
        psi.log.info('Starting simulation...')
        psi.log.info('Simulation started')
        self._simulation = SimulationThread()
        self._simulation.start()

    def on_update(self, tick): 
        # print 'on-updt', tick
        # pass#print 'at psi.app.on_update.'
        psi.manager.on_update(tick)

    def on_pause(self):
        # self._update_timer.Stop()
        psi.log.info('Pausing components...')
        psi.manager.on_pause()
        psi.log.info('Simulation paused')

    def on_resume(self):
        # self._update_timer.Start(1000/psi.config.UPDATE_TIME)
        psi.log.info('Resuming components...')
        psi.manager.on_resume()
        psi.log.info('Simulation resumed')

    def on_stop(self):
        # self._update_timer.Stop()
        psi.log.info('Stopping components...')
        psi.manager.on_stop()
        psi.log.info('Simulation stopped')
        self._simulation.join()

    def on_window_resize(self, size):
        print 'at psi.app.on_window_resize,', size
        if psi.graphics is not None:
            psi.graphics.on_window_resize(size)

    def on_key_down(self):
        print 'at psi.app.on_key_down.'
        psi.graphics.on_key_down()
        psi.manager.on_key_down()

    def on_key_up(self):
        print 'at psi.app.on_key_up.'
        psi.graphics.on_key_up()
        psi.manager.on_key_up()

    def on_mouse_motion(self, pos):
        # print 'at psi.app.on_mouse_motion,', pos
        psi.window.set_coord_info(psi.calc.virtual_coord(pos))
        psi.graphics.on_mouse_motion(pos)
        psi.manager.on_mouse_motion(pos)

    def on_mouse_down(self, button, pos):
        print 'at psi.app.on_mouse_down,', button, pos
        psi.graphics.on_mouse_down(button, pos)
        psi.manager.on_mouse_down(button, pos)

    def on_mouse_up(self, button, pos):
        print 'at psi.app.on_mouse_up,', button, pos
        psi.graphics.on_mouse_up(button, pos)
        psi.manager.on_mouse_up(button, pos)

    def on_mouse_wheel(self, delta, pos):
        print 'at psi.app.on_mouse_wheel,', delta, pos
        psi.graphics.on_mouse_wheel(delta, pos)
        psi.manager.on_mouse_wheel(delta, pos)
    # =========================================================================