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

import random

import wx
import psi

import numpy as np

from psi.tools.timer import Timer
from ..component import Component
from ..map_grid import MapGrid
from ..properties import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

__all__ = ['HimmMapper']

class HimmMapper(Component):
    name = 'HIMM Mapper'
    roles = [psi.ROLE_MAPPER]
    fields = ['robot']
    robot = None

    def on_init(self):
        self.map = MapGrid(psi.config.MAX_TILE, -1)

        self._render = psi.engine.render_batch.RenderBatchOpt(GL_QUADS)
        self._render.count = self.map._size**2*4
        self._render.vertex_buffer = psi.graphics._mapgrid_vertexbuffer
        self._render.color_buffer.set_array(np.array(psi.graphics._mapgrid_colors, dtype='float32'))

    def __set(self, row, col, val):
        x = (row+self.map._center[0])
        y = (col+self.map._center[1])
        index = x*self.map._size*4 + y*4
        
        self._render.color_buffer[index:index+4] = np.array([val, val, val, 1.])
        # print 'setting:', index, index+4, val


    def __sum(self, row, col, c):
        v = self.map[row, col] + c
        self.map[row, col] = psi.calc.clip(v, 0, 1)
        val = 1-self.map[row, col]
        self.__set(row, col, val)

    def __sub(self, row, col, c):
        v = self.map[row, col] - c
        old = self.map[row, col]
        self.map[row, col] = psi.calc.clip(v, 0, 1)
        if old != self.map[row, col]:
            val = 1-self.map[row, col]
            self.__set(row, col, val)        

    def on_update(self, tick):
        size = psi.config.TILE_PIXEL_SIZE

        # timer = Timer()
        # timer.tic()
        for obs in self.robot.not_obstacles:
            row, col = int(obs[1])//size, int(obs[0])//size
            # self.__sub(row, col, 0.05)
            v = self.map[row, col] - 0.05
            old = self.map[row, col]
            self.map[row, col] = psi.calc.clip(v, 0, 1)
            if old != self.map[row, col]:
                val = 1-self.map[row, col]
                        
                x = (row+self.map._center[0])
                y = (col+self.map._center[1])
                index = x*self.map._size*4 + y*4
                
                self._render.color_buffer[index:index+4] = np.array([val, val, val, 1.])

        # for obs in self.robot.not_obstacles:
        #     row, col = int(obs[1])//size, int(obs[0])//size
        #     self.__sub(row, col, 0.05)

        for obs in self.robot.obstacles:
            row, col = int(obs[0])//size, int(obs[1])//size

            self.__sum(row, col, 0.66)
            self.__sum(row-1, col-1, 0.33)
            self.__sum(row-1, col,   0.33)
            self.__sum(row-1, col+1, 0.33)
            self.__sum(row+1, col-1, 0.33)
            self.__sum(row+1, col,   0.33)
            self.__sum(row+1, col+1, 0.33)
            self.__sum(row,   col-1, 0.33)
            self.__sum(row,   col+1, 0.33)


        
            # self.__sub(row-1, col-1, 0.1)
            # self.__sub(row-1, col,   0.1)
            # self.__sub(row-1, col+1, 0.1)
            # self.__sub(row+1, col-1, 0.1)
            # self.__sub(row+1, col,   0.1)
            # self.__sub(row+1, col+1, 0.1)
            # self.__sub(row,   col-1, 0.1)
            # self.__sub(row,   col+1, 0.1)
        # t = timer.toc()
        # print 'himm_mapper.on_update: %.4f seconds, with %d itens'%(t, len(self.robot.not_obstacles))

    def on_draw(self, tick):
        psi.graphics.draw_batch(self._render)


    def ui_options(self, mgr):
        super(HimmMapper, self).ui_options(mgr)
        mgr.add_row('Robot', ComponentChooser(self, 'robot', roles=[psi.ROLE_ROBOT]))

