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
from wx.lib.stattext import GenStaticText
import psi

__all__ = ['StatusbarWidget']

class StatusbarWidget(wx.StatusBar):
    def __init__(self, parent):
        super(StatusbarWidget, self).__init__(parent, style=wx.SB_FLAT)
        self.SetFieldsCount(3)
        self.SetStatusWidths([-6, -1, -1])
        self.size_changed = False

        self._label_info = GenStaticText(self, -1, '')
        self._label_coord = GenStaticText(self, -1, '')
        self._label_simulation = GenStaticText(self, -1, '')

        self.Bind(wx.EVT_SIZE, self.on_size)
        self.Bind(wx.EVT_IDLE, self.on_idle)

    def set_log_text(self, msg, mode=psi.LOG_INFO):
        self._label_info.SetLabel(msg)

        font = self._label_info.GetFont()

        if mode == psi.LOG_ERROR:
            self._label_info.SetForegroundColour((193,43,1))
            font.SetWeight(wx.BOLD)
        
        else:
            self._label_info.SetForegroundColour((0,0,0))
            font.SetWeight(wx.NORMAL)
        
        self._label_info.SetFont(font)

    def set_coord_text(self, msg):
        self._label_coord.SetLabel(msg)

    def set_simulation_text(self, msg):
        self._label_simulation.SetLabel(msg)
        # self.SetStatusText(msg, 1) 

    def on_size(self, event):
        self.reposition()
        self.size_changed = True

    def on_idle(self, event):
        if self.size_changed:
            self.reposition()

    def reposition(self):
        rect = self.GetFieldRect(0)
        self._label_info.SetPosition((rect.x+3, rect.y+4))
        self._label_info.SetSize((rect.width-4, rect.height-4))

        rect = self.GetFieldRect(1)
        self._label_coord.SetPosition((rect.x+3, rect.y+4))
        self._label_coord.SetSize((rect.width-4, rect.height-4))

        rect = self.GetFieldRect(2)
        self._label_simulation.SetPosition((rect.x+3, rect.y+4))
        self._label_simulation.SetSize((rect.width-4, rect.height-4))

        self.size_changed = False

    def SetStatusText(self, *args, **kwargs):
        'ignoring'
        pass