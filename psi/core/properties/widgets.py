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
import os
import psi
from . types import *

class Widget(wx.Panel):
    def __init__(self, comp, attr, type_, update_list=False):
        self._comp = comp
        self._attr = attr
        self._type = type_
        self._update_list = update_list

    def _get(self):
        return self._type.to_string(getattr(self._comp, self._attr))

    def _set(self, val):
        value = self._get()
        if value != val:
            val = setattr(self._comp, self._attr, self._type.to_type(val))

        if self._update_list:
            psi.window.component_list.update(self._comp)

class Text(Widget):
    def __init__(self, comp, attr, type_, update_list=False, enabled=True):
        super(Text, self).__init__(comp, attr, type_, update_list)
        self._enabled = enabled

    def show(self, parent):
        super(Widget, self).__init__(parent, -1)
        value = self._get()
            
        self._text = wx.TextCtrl(self, -1, value, style=wx.TE_PROCESS_ENTER)
        if not self._enabled:
            self._text.Disable()
        self._text.Bind(wx.EVT_KILL_FOCUS , self.on_save)
        self._text.Bind(wx.EVT_TEXT_ENTER , self.on_save)

        bag = wx.BoxSizer(wx.HORIZONTAL)
        bag.Add(self._text, wx.EXPAND)
        self.SetSizer(bag)

    def on_save(self, event):
        value = self._text.GetValue()
        self._set(value)

class TextArea(Widget):
    def show(self, parent):
        super(Widget, self).__init__(parent, -1)
        value = self._get()
        self._text = wx.TextCtrl(self, -1, value, style=wx.TE_MULTILINE, 
                                                  size=(100, 100))
        self._text.Bind(wx.EVT_KILL_FOCUS , self.on_save)

        bag = wx.BoxSizer(wx.HORIZONTAL)
        bag.Add(self._text, wx.EXPAND)
        self.SetSizer(bag)

    def on_save(self, event):
        value = self._text.GetValue()
        self._set(value)

class FileChooser(Widget):
    def __init__(self, comp, attr, type_=UNICODE):
        super(FileChooser, self).__init__(comp, attr, type_)

    def show(self, parent):
        super(Widget, self).__init__(parent, -1)
        value = self._get()
        self._text = wx.TextCtrl(self, -1, value, style=wx.TE_PROCESS_ENTER)
        self._button = wx.Button(self, -1, '...')
        self._text.Bind(wx.EVT_KILL_FOCUS , self.on_save)
        self._button.Bind(wx.EVT_BUTTON, self.on_button)

        bag = wx.BoxSizer(wx.HORIZONTAL)
        bag.Add(self._text, 8, wx.EXPAND)
        bag.Add(self._button, 2)
        self.SetSizer(bag)

    def on_save(self, event=None):
        value = self._text.GetValue()
        self._set(value)

    def on_button(self, event):
        path = psi.config.last_path
        if path is None:
            path = os.getcwd()

        dialog = wx.FileDialog(self, 
            message="Select an ARFF file...", 
            defaultDir=path, 
            defaultFile="", 
            wildcard="ARFF dataset (*.arff)|*.arff",
            style=wx.FD_OPEN
        )
        status = dialog.ShowModal()
        path = dialog.GetPath()
        dialog.Destroy()

        if path:
            psi.config.last_path = path
            self._text.SetValue(path)
            self._text.SetInsertionPointEnd()
            self.on_save()

class ComponentChooser(Widget):
    def __init__(self, comp, attr, roles=None):
        super(ComponentChooser, self).__init__(comp, attr, type_=COMPONENT)
        self.roles = roles

    def __get_choices(self):
        choices = []

        if self.roles is not None and not isinstance(self.roles, (list, tuple)):
            self.roles = [self.roles]

        components = psi.manager.get_components()
        for c in components:
            if c == self._comp: continue

            if self.roles is None or any([role in c.roles for role in self.roles]):
                choices.append(c)

        return choices

    def show(self, parent):
        super(Widget, self).__init__(parent, -1)
        value = self._get()

        self._compoent = None

        self._text = wx.TextCtrl(self, -1, value, style=wx.TE_PROCESS_ENTER)
        self._text.Disable()
        self._button = wx.Button(self, -1, '...')
        self._button.Bind(wx.EVT_BUTTON, self.on_button)

        bag = wx.BoxSizer(wx.HORIZONTAL)
        bag.Add(self._text, 8, wx.EXPAND)
        bag.Add(self._button, 2)
        self.SetSizer(bag)

    def on_button(self, event):
        choices = self.__get_choices()
        dialog = wx.SingleChoiceDialog(
            self,
            message="Select a component",
            caption="Component selection", 
            choices=[c.to_string() for c in choices]
        )
        status = dialog.ShowModal()
        selection = dialog.GetSelection()
        dialog.Destroy()

        if status == wx.ID_OK:
            component = choices[selection]
            self._text.SetValue(COMPONENT.to_string(component))
            setattr(self._comp, self._attr, component)