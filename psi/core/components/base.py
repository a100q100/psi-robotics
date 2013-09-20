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
from ..component import Component
from ..map_grid import MapGrid
from psi.euclid import Vector2

__all__ = ['BaseRobot', 'BaseGridMapper']

class BaseRobot(Component):
    def __init__(self):
        super(BaseRobot, self).__init__()
        self.pos = Vector2(0, 0)
        self.th = 0.0
        self.size = Vector2(45, 38) # robot size by cm

    def get_obstacles(self):
        pass

    def act(self, *kwargs):
        pass

    def on_draw(self, tick):
        scale = psi.config.TILE_SCALE
        w, h = self.size*scale
        hw, hh = w//2, h//2
        hhh = hh//2
        x, y = self.pos
        
        color = (1., 0., 0., 1.)
        psi.graphics.draw_box(x-hw, y-hh, w, h, color, rotation=self.th, center=(x, y))

        color = (1., 1., 0., 1.)
        psi.graphics.draw_box(x, y-hhh, hw, hh, color, rotation=self.th, center=(x, y))
       

class BaseGridMapper(Component):
    def __init__(self):
        super(BaseGridMapper, self).__init__()

