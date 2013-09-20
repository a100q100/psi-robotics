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

_last_path = os.getcwd()

def save_project_as(parent):
    global _last_path
    dialog = wx.FileDialog(parent, 
        message="Save Project As ...", 
        defaultDir=_last_path, 
        defaultFile="", 
        wildcard="Psi project (*.psi)|*.psi", 
        style=wx.SAVE|wx.OVERWRITE_PROMPT|wx.CHANGE_DIR
    )
    status = dialog.ShowModal()
    path = dialog.GetPath()
    dialog.Destroy()

    if path:
        _last_path = os.path.dirname(path)
        
        if not path.endswith('.psi'):
            path += '.psi'

    return status, path

def open_project(parent):
    global _last_path
    dialog = wx.FileDialog(parent,
        message="Open Project...",
        defaultDir=_last_path, 
        defaultFile="",
        wildcard="Psi project (*.psi)|*.psi",
        style=wx.OPEN|wx.CHANGE_DIR
    )
    status = dialog.ShowModal()
    path = dialog.GetPath()
    dialog.Destroy()

    _last_path = path or _last_path
    return status, path


def confirm(parent, caption, message):
    dialog = wx.MessageDialog(parent, 
        message=message, 
        caption=caption, 
        style=wx.YES_NO|wx.ICON_INFORMATION
    )
    status = dialog.ShowModal()
    dialog.Destroy()
    return status

def multichoice(parent, caption, message, choices):
    dialog = wx.MultiChoiceDialog(parent, message, caption, choices)
    status = dialog.ShowModal()
    selections = dialog.GetSelections()
    dialog.Destroy()
    return status, selections
