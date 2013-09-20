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
from wx.lib.sized_controls import SizedPanel
from wx.lib.scrolledpanel import ScrolledPanel 

import psi
from psi.tools.property_handler import *
from .filechooser_widget import FileChooserWidget
from .robotchooser_widget import RobotChooserWidget

__all__ = ['ComponentPropertyWidget']

class PropertyManager(object):
    def __init__(self, parent):
        self.parent = parent
        self.rows = []

    def clear(self):
        self.rows = []

    def add_row(self, label, ctrl):
        _label = wx.StaticText(self.parent, -1, label)
        _label.SetMinSize((-1, 15))
        ctrl.show(self.parent)
        self.rows.extend([_label, (ctrl, 1, wx.EXPAND)])


class ComponentPropertyWidget(ScrolledPanel):
    def __init__(self, parent, *args, **kwargs):
        styles = wx.TAB_TRAVERSAL|wx.BORDER_NONE|wx.VSCROLL
        super(ComponentPropertyWidget, self).__init__(parent, style=styles)#, style=wx.VSCROLL)
        self._panel = wx.Panel(self)

        self.SetAutoLayout(1)
        self.SetupScrolling()

        self._manager = PropertyManager(self._panel)
        # self.Bind(wx.EVT_SIZE, self.on_resize)

        hbox = wx.BoxSizer(wx.HORIZONTAL)

        self.grid = wx.FlexGridSizer(0, 2, 5, 5)
        self.grid.AddGrowableCol(1, 1)

        hbox.Add(self.grid, proportion=1, flag=wx.ALL|wx.EXPAND, border=10)
        self._panel.SetSizer(hbox)

        bag = wx.BoxSizer()
        bag.Add(self._panel, wx.EXPAND)
        self.SetSizer(bag)

    def show(self, component):
        component.ui_options(self._manager)
        self.grid.AddMany(self._manager.rows)
        self.Layout()

    def hide(self):
        self._manager.clear()
        self.grid.Clear()
        for c in self._panel.GetChildren():
            c.Destroy()
        self.Layout()

    # def on_resize(self, event):
    #     size = event.GetSize()
    #     sizer = self._panel.GetSizer()
    #     if sizer:
    #         w, h = size.Get()
    #         for (ctrl, _, _1) in self._manager.rows[1::2]:
    #             sizer = ctrl.GetSizer()
    #             x, y = sizer.GetPosition().Get()
    #             sizer.SetDimension(x, y, w, h)
    #         self._panel.SetSize(size)
