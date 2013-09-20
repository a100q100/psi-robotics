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

import wx
import wx.glcanvas

import psi
from psi.euclid import Vector2

__all__ = ['CanvasWidget']

class CanvasWidget(wx.glcanvas.GLCanvas):
    '''The canvas widget.'''

    def __init__(self, parent):
        super(CanvasWidget, self).__init__(parent, -1)

        self.initialized = False
        self.mouse_position = None
        self.canvas_size = Vector2(0, 0)

        self.Bind(wx.EVT_PAINT, self.on_draw)
        self.Bind(wx.EVT_SIZE, self.on_resize)
        # self.Bind(wx.EVT_IDLE, self.on_idle)

        self.Bind(wx.EVT_LEFT_DOWN, self.on_mouse_down)
        self.Bind(wx.EVT_LEFT_UP, self.on_mouse_up)
        self.Bind(wx.EVT_MIDDLE_DOWN, self.on_mouse_down)
        self.Bind(wx.EVT_MIDDLE_UP, self.on_mouse_up)
        self.Bind(wx.EVT_RIGHT_DOWN, self.on_mouse_down)
        self.Bind(wx.EVT_RIGHT_UP, self.on_mouse_up)
        self.Bind(wx.EVT_MOUSEWHEEL, self.on_mouse_wheel)
        self.Bind(wx.EVT_MOTION, self.on_mouse_motion)

        if wx.Platform == '__WXMSW__' : 
            self.Bind(wx.EVT_LEFT_DCLICK,  self.on_mouse_down)
            self.Bind(wx.EVT_RIGHT_DCLICK,  self.on_mouse_down)
            self.Bind(wx.EVT_MIDDLE_DCLICK,  self.on_mouse_down)


    def swap_buffers(self):
        self.SwapBuffers()

    def on_draw(self, event):
        dc = wx.PaintDC(self)
        self.SetCurrent()
        
        if not self.initialized:
            self.initialized = True
            self.canvas_size = Vector2(*self.GetSize())
            psi.app.on_init()

    def on_resize(self, event):
        size = Vector2(*event.GetSize())
        psi.app.on_window_resize(size)

    def on_mouse_motion(self, event):
        x, y = event.GetPosition()
        pos = Vector2(x, self.canvas_size.y-y)
        self.mouse_position = pos
        psi.app.on_mouse_motion(pos)

    def on_mouse_down(self, event):
        self.SetFocus()
        self.CaptureMouse()
        button = event.GetButton()
        psi.app.on_mouse_down(button, self.mouse_position)

    def on_mouse_up(self, event):
        self.ReleaseMouse()
        button = event.GetButton()
        psi.app.on_mouse_up(button, self.mouse_position)

    def on_mouse_wheel(self, event):
        delta = event.GetWheelRotation()
        psi.app.on_mouse_wheel(delta, self.mouse_position)