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

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import psi
from psi.calc import clip
from psi.euclid import Vector2

__all__ = ['Camera']

class Camera(object):
    def __init__(self, pos=Vector2(0, 0)):
        self.pos = pos
        self.half_size = Vector2(300, 300)
        self.zoom = 1.0
        self._zoom_step = 0.5
        self._scale_rate = 1/self.zoom

    def adjust(self, old_scale, new_scale):
        pass

    def zoom_out(self):
        self.zoom = clip(self.zoom+self._zoom_step, self._zoom_step, 10.5)
        old = self._scale_rate
        self._scale_rate = 1/self.zoom
        self.adjust(old, self._scale_rate)

    def zoom_in(self):
        self.zoom = clip(self.zoom-self._zoom_step, self._zoom_step, 10.5)
        old = self._scale_rate
        self._scale_rate = 1/self.zoom
        self.adjust(old, self._scale_rate)

    def reset_zoom(self):
        self.zoom = 1.
        self._scale_rate = 1/self.zoom

    def pan(self, delta):
        self.pos += delta

    def locate(self):
        glTranslatef(-self.pos.x+self.half_size.x, -self.pos.y+self.half_size.y, 0)
        glScalef(self._scale_rate, self._scale_rate, 0)


    def on_window_resize(self, size):
        half_size = size/2.
        diff = self.half_size - half_size
        # print self.half_size, '=>', half_size, '=', diff
        self.half_size = half_size

        # self.pan(-diff/4.)