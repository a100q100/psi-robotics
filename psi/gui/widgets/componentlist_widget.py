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
import wx.lib.mixins.listctrl as listmix

import psi

__all__ = ['ComponentListWidget']

class ComponentListWidget(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        super(ComponentListWidget, self).__init__(parent)
        # wx.LC_NO_HEADER|wx.LC_EDIT_LABELS|
        list_style = wx.LC_REPORT|\
                     wx.LC_VRULES|wx.LC_SINGLE_SEL|wx.BORDER_NONE

        self._list = wx.ListCtrl(self, -1, style=list_style)
        self._component_count = 0
        self._components = []

        self.__init_ui()

    # =========================================================================
    # INTERNALS
    # =========================================================================
    def __init_ui(self):
        sizer = wx.BoxSizer()
        sizer.Add(self._list, 1, wx.EXPAND)
        self.SetSizer(sizer)

        self._list.InsertColumn(1, 'ID', wx.LIST_FORMAT_RIGHT, width=30)
        self._list.InsertColumn(2, 'Name', width=165)
        
        self._list.Bind(wx.EVT_LIST_ITEM_SELECTED, self.wx_item_select)
        self._list.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.wx_item_deselect)
        self._list.Bind(wx.EVT_LIST_DELETE_ITEM, self.wx_item_delete)
        self._list.Bind(wx.EVT_RIGHT_UP, self.wx_right_click)
        self._list.Bind(wx.EVT_COMMAND_RIGHT_CLICK, self.wx_right_click)

    def __open_menu(self):
        menu = wx.Menu()
        menu_delete = menu.Append(wx.ID_ANY, "Delete")
        self.Bind(wx.EVT_MENU, self.wx_menu_delete, menu_delete)
        self._list.PopupMenu(menu)
        menu.Destroy()

    # =========================================================================
    # COMPONENT HANDLING
    # =========================================================================
    def add(self, component):
        count = psi.manager.get_component_count()
        self._list.Append(('#%d'%component.id, component.name))
        # self._list.InsertStringItem(count, component.name)
        # self._list.InsertStringItem(count, [component.id, component.name])

    def remove(self, component):
        components = psi.manager.get_components()
        i = components.index(component)
        self._list.DeleteItem(i)

    def clear(self):
        count = psi.manager.get_component_count()
        for i in xrange(count):
            self._list.DeleteAllItems()

        psi.window.deselect_component()

    def update(self, component):
        components = psi.manager.get_components()
        i = components.index(component)
        # self._list.SetItemText(i, component.name)
        self._list.SetStringItem(i, 0, '#%d'%component.id)
        self._list.SetStringItem(i, 1, component.name)

    def get_selected(self):
        index = self._list.GetFirstSelected()
        components = psi.manager.get_components()
        return components[index]

    # =========================================================================
    # EVENTS
    # =========================================================================
    def wx_item_select(self, event):
        component = self.get_selected()
        psi.window.select_component(component)

    def wx_item_deselect(self, event):
        psi.window.deselect_component()

    def wx_right_click(self, event):
        self.__open_menu()

    def wx_menu_delete(self, event):
        component = self.get_selected()
        psi.app.remove_component(component)

    def wx_item_delete(self, event):
        psi.window.deselect_component()