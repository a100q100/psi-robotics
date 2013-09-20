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

import os

import wx
import wx.lib.agw.aui as aui
from wx.lib.wordwrap import wordwrap

import psi
import psi.gui.widgets
from . import dialogs

__all__ = ['MainWindow']

class MainWindow(wx.Frame):
    def __init__(self):
        super(MainWindow, self).__init__(None, title='PSI', size=(800, 600))

        self.canvas = None
        self.menubar = None
        self.statusbar = None
        self.component_list = None
        self.component_property = None
    
        self.__init_ui()
        self.Centre()

    def __init_ui(self):
        # INITIALIZATION ======================================================
        self.menubar = psi.gui.widgets.MenubarWidget(self)
        self.canvas = psi.gui.widgets.CanvasWidget(self)
        self.component_list = psi.gui.widgets.ComponentListWidget(self)
        self.component_property = psi.gui.widgets.ComponentPropertyWidget(self)
        # self.statusbar = self.CreateStatusBar()
        self.statusbar = psi.gui.widgets.StatusbarWidget(self)
        # =====================================================================

        # icon = wx.IconBundle()
        # icon.AddIconFromFile("psi/resources/icon.ico", wx.BITMAP_TYPE_ANY)
        icon = wx.EmptyIcon()
        icon.CopyFromBitmap(wx.Bitmap("psi/resources/icon.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)
        # self.SetIcons(icon)

        # MENU BAR ============================================================
        item = self.menubar.add_item
        separator = self.menubar.add_separator

        # PROJECT
        menu = self.menubar.add_menu('&Project')
        item(menu, psi.ID_NEWPROJECT, 'New Project', self.wx_menu_new_project)
        item(menu, psi.ID_SAVEPROJECT, 'Save Project', self.wx_menu_save_project)
        item(menu, psi.ID_SAVEPROJECTAS, 'Save Project As...', self.wx_menu_save_project_as)
        item(menu, psi.ID_OPENPROJECT, 'Open Project...', self.wx_menu_open_project)
        separator(menu)
        item(menu, psi.ID_QUIT, 'Quit', self.wx_menu_quit)

        # SIMULATION
        menu = self.menubar.add_menu('&Simulation')
        item(menu, psi.ID_RUN, 'Run', self.wx_menu_run)
        item(menu, psi.ID_PAUSE, 'Pause', self.wx_menu_pause)
        item(menu, psi.ID_RESUME, 'Resume', self.wx_menu_resume)
        item(menu, psi.ID_STOP, 'Stop', self.wx_menu_stop)

        # VIEW
        menu = self.menubar.add_menu('&View')
        item(menu, psi.ID_CENTER, 'Center', self.wx_menu_center)
        item(menu, psi.ID_FOLLOWROBOT, 'Follow Robot', self.wx_menu_follow_robot)
        separator(menu)
        item(menu, psi.ID_ZOOMIN, 'Zoom In', self.wx_menu_zoom_in)
        item(menu, psi.ID_ZOOMOUT, 'Zoom Out', self.wx_menu_zoom_out)
        item(menu, psi.ID_RESETZOOM, 'Reset Zoom', self.wx_menu_reset_zoom)
        separator(menu)
        item(menu, psi.ID_SHOWGRID, 'Show/Hide Grid', self.wx_menu_show_grid)

        # COMPONENTS
        menu = self.menubar.add_menu('&Components')
        item(menu, psi.ID_ADDCOMPONENT, 'Add Component', self.wx_menu_add_component)
        item(menu, psi.ID_REMOVECOMPONENT, 'Remove Component', self.wx_menu_remove_component)

        # HELP
        menu = self.menubar.add_menu('&Help')
        item(menu, psi.ID_ABOUT, 'About', self.wx_menu_about)


        self.SetMenuBar(self.menubar)
        self.menubar.disable_item(psi.ID_PAUSE)
        self.menubar.disable_item(psi.ID_RESUME)
        self.menubar.disable_item(psi.ID_STOP)
        self.menubar.disable_item(psi.ID_REMOVECOMPONENT)
        # =====================================================================
        
        # STATUS BAR ==========================================================
        self.SetStatusBar(self.statusbar)
        # =====================================================================

        # PANELS ==============================================================
        #
        flags = aui.AUI_MGR_ALLOW_FLOATING|aui.AUI_MGR_TRANSPARENT_HINT|\
                aui.AUI_MGR_HINT_FADE|aui.AUI_MGR_NO_VENETIAN_BLINDS_FADE
                # aui.AUI_MGR_AERO_DOCKING_GUIDES
                # aui.AUI_MGR_USE_NATIVE_MINIFRAMES
                # aui.AUI_MGR_LIVE_RESIZE|
        self._mgr = aui.AuiManager(self, agwFlags=flags)

        # CANVAS
        self._mgr.AddPane(
            self.canvas, 
            aui.AuiPaneInfo().Center().Layer(1).Caption('Canvas').
                              MinSize((400, 400)).CaptionVisible(False).
                              CloseButton(False))

        # COMPONENT LIST
        self._mgr.AddPane(
            self.component_list, 
            aui.AuiPaneInfo().Right().Layer(1).Caption('Components').
                              MinSize((200, 100)).CloseButton(False).
                              MinimizeButton(True))

        # COMPONENT PROPERTY
        self._mgr.AddPane(
            self.component_property, 
            aui.AuiPaneInfo().Right().Layer(1).Caption('Properties').
                              MinSize((200, 100)).CloseButton(False).
                              MinimizeButton(True))

        self._mgr.Update()
        # =====================================================================

        self.Bind(wx.EVT_CLOSE, self.wx_on_close)

    # =========================================================================
    # ACCESS METHODS
    # =========================================================================
    # MAIN WINDOW
    def set_window_title(self, text):
        self.SetTitle(text + ' - PSI Robotics')

    # STATUS BAR
    def set_status_info(self, text, mode=psi.LOG_INFO):
        self.statusbar.set_log_text(text, mode)

    def set_coord_info(self, coord):
        self.statusbar.set_coord_text('(%d, %d)'%(coord[0], coord[1]))

    def set_status_simulation(self, status):
        if status == psi.STATE_RUNNING:
            self.statusbar.set_simulation_text('Running') 
        elif status == psi.STATE_PAUSED:
            self.statusbar.set_simulation_text('Paused') 
        elif status == psi.STATE_STOPPED:
            self.statusbar.set_simulation_text('Not Running') 

    # CANVAS
    def get_canvas_size(self):
        return self.canvas.canvas_size

    def get_canvas_mouse_position(self):
        return self.canvas.mouse_position

    def swap_buffers(self):
        self.canvas.swap_buffers()

    # MENU CONTROL
    def disable_menu_item(self, id):
        self.menubar.disable_item(id)

    def enable_menu_item(self, id):
        self.menubar.enable_item(id)

    # COMPONENT LIST
    def add_component(self, component):
        self.component_list.add(component)

    def remove_component(self, component):
        self.component_list.remove(component)

    def clear_components(self):
        self.component_list.clear()

    def select_component(self, component):
        self.enable_menu_item(psi.ID_REMOVECOMPONENT)
        self.show_component_options(component)

    def deselect_component(self):
        self.disable_menu_item(psi.ID_REMOVECOMPONENT)
        self.hide_component_options()

    def show_component_options(self, component):
        self.component_property.show(component)

    def hide_component_options(self):
        self.component_property.hide()


    # =========================================================================
    # MENU EVENTS
    # =========================================================================
    def wx_menu_new_project(self, event): 
        psi.app.new_project()

    def wx_menu_save_project(self, event):
        if psi.app.project_path is None:
            self.wx_menu_save_project_as(event)
        else:
            psi.app.save_project()

    def wx_menu_save_project_as(self, event):
        status, path = dialogs.save_project_as(self)

        if status != wx.ID_OK: return
        psi.app.save_project_as(path)

    def wx_menu_open_project(self, event):
        status, path = dialogs.open_project(self)

        if status != wx.ID_OK: return
        psi.app.open_project(path)

    def wx_menu_run(self, event): 
        psi.app.run_simulation()

    def wx_menu_pause(self, event):
        psi.app.pause_simulation()

    def wx_menu_resume(self, event):
        psi.app.resume_simulation()

    def wx_menu_stop(self, event):
        psi.app.stop_simulation()

    def wx_menu_center(self, event): 
        psi.app.center_camera()

    def wx_menu_follow_robot(self, event): 
        psi.app.follow_robot_camera()
        
    def wx_menu_zoom_in(self, event):
        psi.app.zoom_in()

    def wx_menu_zoom_out(self, event):
        psi.app.zoom_out()

    def wx_menu_reset_zoom(self, event):
        psi.app.reset_zoom()

    def wx_menu_show_grid(self, event):
        psi.app.toogle_grid()

    def wx_menu_add_component(self, event):
        components = psi.manager._registry
        choices = [c.name for c in components]

        status, selections = dialogs.multichoice(self,
            message="Select The Components",
            caption="Add Component", 
            choices=choices
        )

        if status != wx.ID_OK: return

        for i in selections:
            c = components[i]()
            psi.app.add_component(c)

    def wx_menu_remove_component(self, event):
        component = self.component_list.get_selected()
        psi.app.remove_component(component)

    def wx_menu_quit(self, event):
        self.Close()

    def wx_on_close(self, event):
        psi.app.on_quit()        

    def wx_menu_about(self, event):
        info = wx.AboutDialogInfo()
        info.Name = "PSI Robotics"
        info.Version = "1.0.0"
        info.Copyright = "(C) 2013 Renato de Pontes Pereira"
        info.Description = wordwrap(
            '''PSI is a component-based robotic system.''',
            350, wx.ClientDC(self))
        info.WebSite = ("http://inf.ufrgs.br/~rppereira", "My page")
        info.Developers = ["Renato de Pontes Pereira"]
        # info.License = wordwrap(licenseText, 500, wx.ClientDC(self))
        wx.AboutBox(info)

    # =========================================================================