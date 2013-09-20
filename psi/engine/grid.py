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

# import random
import numpy as np

import psi
from psi.calc import clip
from psi.euclid import Vector2
from .render_batch import RenderBatchOpt

__all__ = ['Grid']

class Grid(object):
    def __init__(self, size):
        self._render = RenderBatchOpt(GL_LINES)
        self._renders = [RenderBatchOpt(GL_LINES) for i in xrange(3)]
        # self._render.call_before = self.before
        self._grid_size = size
        self.create_grid()

    def create_grid(self):
        self._render.clear()
        vertexes = []
        colors = []
        gs = self._grid_size
        tsize = psi.config.TILE_PIXEL_SIZE
        ntile = psi.config.MAX_TILE

        n = tsize*ntile
        hn = n/2

        offset_x = (hn%tsize)
        offset_y = (hn%tsize)
        COLOR = (.75, .75, .75, .5)
        c = 0

        for i, (render, scale) in enumerate(zip(self._renders, [1, 5, 10])):
            c = 0
            vertexes = []
            colors = []
            for x in xrange(-hn-offset_x, hn+1, tsize*scale):
                c += 2
                vertexes.extend([[x, -hn], [x, hn]])
                colors.extend([COLOR, COLOR])
            for y in xrange(-hn-offset_x, hn+1, tsize*scale):
                c += 2
                vertexes.extend([[-hn, y], [hn, y]])
                colors.extend([COLOR, COLOR])
            render.count = c
            render.vertex_buffer.set_array(np.array(vertexes, dtype='float32'))
            render.color_buffer.set_array(np.array(colors, dtype='float32'))

    def on_window_resize(self, size):
        self._grid_size = size
        self.create_grid()

    def on_draw(self, tick):
        zoom = psi.graphics.camera.zoom
        width = 1
        if zoom < 1.5: 
            glLineWidth(width); width+=1;
            self._renders[0].render()
        if zoom < 5.5: 
            glLineWidth(width); width+=1;
            self._renders[1].render()
        if zoom < 11.5: 
            glLineWidth(width); width+=1;
            self._renders[2].render()
        
        glLineWidth(1);
