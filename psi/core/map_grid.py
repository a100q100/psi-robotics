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

import numpy as np

import psi
from psi.euclid import Vector2

__all__ = ['MapGrid']

class MapGrid(object):
    def __init__(self, size=None, initial_value=None):
        self._initial_value = initial_value
        self._size = size or psi.config.MAX_TILE
        self._center = Vector2(self._size//2, self._size//2)
        self._map = None

        self._min_pos_real = self._center.copy()
        self._max_pos_real = self._center.copy()
        self.min_pos = Vector2(0, 0)
        self.max_pos = Vector2(0, 0)

        self.clear()

    def clear(self):
        self._map = np.ones([self._size, self._size])*self._initial_value

    def __getstate__(self):
        return {'_initial_value': self._initial_value, '_size': self._size}

    def __setstate__(self, state):
        self._initial_value = state['_initial_value']
        self._size = state['_size']
        self._center = Vector2(self._size//2, self._size//2)
        self._map = None

        self._min_pos_real = self._center.copy()
        self._max_pos_real = self._center.copy()
        self.min_pos = Vector2(0, 0)
        self.max_pos = Vector2(0, 0)

        self.clear()

    def __setitem__(self, pos, value):
        x, y = pos + self._center

        if pos[0] < self.min_pos[0]:
            self.min_pos[0] = pos[0]
            self._min_pos_real[0] = x

        if pos[0] > self.max_pos[0]:
            self.max_pos[0] = pos[0]
            self._max_pos_real[0] = x

        if pos[1] < self.min_pos[1]:
            self.min_pos[1] = pos[1]
            self._min_pos_real[1] = y

        if pos[1] > self.max_pos[1]:
            self.max_pos[1] = pos[1]
            self._max_pos_real[1] = y

        self._map[(x, y)] = value

    def __getitem__(self, pos):
        try:
            x, y = pos+self._center
            return self._map[x, y]
        except IndexError as e:
            return self._initial_value


    
