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
import numpy as np

import scipy
import scipy.spatial

import psi
import arff
from ..properties import *
# from psi.tools.property_handler import *
from psi.euclid import Vector2
from ..component import Component
from .base import BaseRobot

from psi.tools.timer import Timer

__all__ = ['ReplayRobot']


def bresenham(x0, y0, x1, y1, step=1):
    x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    den, num, num_add, num_pixels = (0, 0, 0, 0)

    xinc1 = step if x0 <= x1 else -step
    xinc2 = xinc1
    yinc1 = step if y0 <= y1 else -step
    yinc2 = yinc1

    if dx >= dy:
        xinc1 = 0
        yinc2 = 0
        den = dx
        num = dx/2.
        num_add = dy
        num_pixels = dx
    else:
        xinc2 = 0
        yinc1 = 0
        den = dy
        num = dy/2.
        num_add = dx
        num_pixels = dy

    x, y = x0, y0
    points = []
    for curpixel in xrange(0, num_pixels+1, step):
        p = (x, y)
        points.append(p)

        num += num_add
        if (num >= den):
            num -= den
            x += xinc1
            y += yinc1
        x += xinc2
        y += yinc2

    return points


class ReplayRobot(Component):
    name = 'Replay Robot'
    roles = [psi.ROLE_ROBOT]
    fields = ['_path']

    def __init__(self):
        super(ReplayRobot, self).__init__()
        self._path = ''
        self.on_init()

    def on_init(self):
        self._pos = Vector2(0, 0)
        self._th = 0.0
        self.size = Vector2(45, 38)
        self.aux = []

        self._data_pos = None
        self._data_th = None
        self._data_sonar = None
        self._data_index = None

    def on_run(self):
        f = open(self._path, 'rb')
        dataset = arff.load(f)
        data = np.array(dataset['data'])
        print len(data)

        self.pos = self._pos.copy()
        self.th = self._th
        self._data_pos = data[:, 1:3]/10.0
        self._data_th = data[:, 3:4]
        self._data_sonar = data[:, 6:14]/10.0
        self._data_index = 0
        f.close()

    def on_update(self, tick):
        tsize = psi.config.TILE_PIXEL_SIZE
        self._pos.x = self._data_pos[self._data_index//1][0]*psi.config.TILE_SCALE
        self._pos.y = self._data_pos[self._data_index//1][1]*psi.config.TILE_SCALE
        self._th = self._data_th[self._data_index//1][0]
        self._data_index += 1

        sonar = self._data_sonar[self._data_index//1]
        
        self.obstacles = []
        self.not_obstacles = []
        snap = psi.calc.snap_to_grid
        euc = scipy.spatial.distance.euclidean
        
        # timer = Timer()
        # timer.tic()

        self.aux = []
        self.not_obstacles = set()
        for i, angle in enumerate([-90, -50, -30, -10, 10, 30, 50, 90]):
            d = sonar[i]
            d = psi.calc.clip(d, 0, 200)
            
            opos = psi.calc.obstacle_position(d, angle, self._pos, self._th)
            if d < 200:
                self.obstacles.append(opos)
            # else:
            #     self.not_obstacles.add(opos)

            # if angle == -50:
            for a_ in xrange(-15, 15, 2):
                p = psi.calc.obstacle_position(d*0.75, a_-angle-90, [self._pos[1], self._pos[0]], -self._th)
                points = bresenham(self._pos[0], self._pos[1], p[0], p[1], tsize)
                self.not_obstacles.update(points)
                self.aux.append(p)

        # t = timer.toc()
        # print 'replay_robot.on_update: %.4f seconds'%t



        # # print self.obstacles
    def on_draw(self, tick):
        scale = psi.config.TILE_SCALE
        w, h = self.size*scale
        hw, hh = w//2, h//2
        hhh = hh//2
        x, y = self._pos
        
        color = (1., 0., 0., 1.)
        psi.graphics.draw_box(x-hw, y-hh, w, h, color, rotation=self._th, center=(x, y))

        color = (1., 1., 0., 1.)
        psi.graphics.draw_box(x, y-hhh, hw, hh, color, rotation=self._th, center=(x, y))
       
        # tsize = psi.config.TILE_PIXEL_SIZE
        # ht = tsize/2
        # for a in self.aux:
        #     ax = Vector2(a[0], a[1])
        #     psi.graphics.draw_box(ax.x, ax.y, tsize, tsize, psi.BLUE)
        #     psi.graphics.draw_line([self._pos+[ht, ht], ax+(ht, ht)])
            # psi.graphics.draw_line([self.mark+(ht, ht), ax+(ht, ht)])


    def ui_options(self, mgr):
        super(ReplayRobot, self).ui_options(mgr)

        # mgr.add_row('Position', Text(self, '_pos', VECTOR2))
        # mgr.add_row('Heading', Text(self, '_th', FLOAT))
        mgr.add_row('Path', FileChooser(self, '_path'))

