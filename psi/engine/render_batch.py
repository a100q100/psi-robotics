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

import psi
import numpy as np

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.arrays.vbo import VBO

__all__ = ['RenderBatch', 'RenderBatchOpt']


class RenderBatch(object):
    def __init__(self, draw_type=GL_QUADS):
        self.count = 0
        self.color_data = []
        self.position_data = []
        self.color_buffer = VBO(np.array([]))
        self.position_buffer = VBO(np.array([]))

        self.draw_type = draw_type


    def draw2d(self, points, color=(0, 0, 0, 1), rotation=0, center=(0, 0)):
        n = len(points)
        self.count += n

        if not isinstance(color[0], (tuple, list)):
            color = [color]*n

        if rotation:
            transform = psi.calc.rotation_matrix(rotation)

            temp = np.array(points) - center
            temp = transform.dot(temp.T).T + center
            points = temp.tolist()

        self.color_data.extend(color)
        self.position_data.extend(points)

    def clear(self):
        self.position_data = []
        self.color_data = []
        self.count = 0

    def render(self):
        self.color_buffer.set_array(np.array(self.color_data, dtype='float32'))
        self.position_buffer.set_array(np.array(self.position_data, dtype='float32'))

        self.color_buffer.bind()
        glColorPointer(4, GL_FLOAT, 0, self.color_buffer)

        self.position_buffer.bind()
        glVertexPointer(2, GL_FLOAT, 0, self.position_buffer)

        glEnableClientState(GL_VERTEX_ARRAY)
        glEnableClientState(GL_COLOR_ARRAY)
        glDrawArrays(self.draw_type, 0, self.count)
        glDisableClientState(GL_COLOR_ARRAY)
        glDisableClientState(GL_VERTEX_ARRAY)


class RenderBatchOpt(object):
    def __init__(self, draw_type=GL_QUADS):
        self.count = 0
        self.color_buffer = VBO(np.array([]))
        self.vertex_buffer = VBO(np.array([]))
        self.draw_type = draw_type


    def draw2d(self, points, color=(0, 0, 0, 1), rotation=0, center=(0, 0)):
        n = points.shape[0]
        self.count += n

        if rotation:
            transform = psi.calc.rotation_matrix(rotation)

            temp = points - center
            temp = transform.dot(temp.T).T + center
            points = temp.tolist()

        self.color_buffer.set_array(color)
        self.vertex_buffer.set_array(points)

    def clear(self):
        self.color_buffer.set_array(np.array([]))
        self.vertex_buffer.set_array(np.array([]))
        self.count = 0

    def render(self):
        self.color_buffer.bind()
        glColorPointer(4, GL_FLOAT, 0, self.color_buffer)

        self.vertex_buffer.bind()
        glVertexPointer(2, GL_FLOAT, 0, self.vertex_buffer)

        glEnableClientState(GL_VERTEX_ARRAY)
        glEnableClientState(GL_COLOR_ARRAY)
        glDrawArrays(self.draw_type, 0, self.count)
        glDisableClientState(GL_COLOR_ARRAY)
        glDisableClientState(GL_VERTEX_ARRAY)