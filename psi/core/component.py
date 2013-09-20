# =============================================================================
# Federal University of Rio Grande do Sul (UFRGS)
# Connectionist Artificial Intelligence Laboratory (LIAC)
# Renato de Pontes Pereira - rppereira@inf.ufrgs.br
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

import psi
from .properties import *
# from psi.tools.property_handler import *

__all__ = ['Component']

class Component(object):
    __id = 0
    id = None
    name = None
    roles = []
    fields = None

    def __init__(self):
        Component.__id+=1
        self.id = Component.__id
        self.on_init()

    def __getstate__(self):
        if self.fields is not None:
            if 'name' not in self.fields:
                self.fields.append('name')

            if 'id' not in self.fields:
                self.fields.append('id')

            return {f:getattr(self, f) for f in self.fields}
        else:
            return self.__dict__

    def __setstate__(self, state):
        self.__dict__.update(state)
        self.on_init()

    def on_init(self): pass
    def on_update(self, tick): pass
    def on_draw(self, tick): pass
    def on_run(self): pass
    def on_pause(self): pass
    def on_resume(self): pass
    def on_stop(self): pass
    def on_key_down(self): pass
    def on_key_up(self): pass
    def on_mouse_motion(self, pos): pass
    def on_mouse_down(self, button, pos): pass
    def on_mouse_up(self, button, pos): pass
    def on_mouse_wheel(self, delta, pos): pass

    def ui_options(self, mgr):
        mgr.add_row('ID', Text(self, 'id', INTEGER, enabled=False))
        mgr.add_row('Name', Text(self, 'name', UNICODE, update_list=True))

    def to_string(self):
        return u'%s (#%d)'%(self.name, self.id)

    def __repr__(self):
        return '<Component %s>'%self.name