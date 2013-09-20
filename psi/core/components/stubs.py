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
import wx

import psi
from psi.euclid import Vector2
from .base import BaseRobot
from .base import BaseGridMapper
from ..map_grid import MapGrid
from ..component import Component

import random
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from ..properties import *

__all__ = ['StubRobot', 'StubMapper', 'TesteBoy']

class StubMapper(BaseGridMapper):
    name = 'Stub Mapper'
    roles = [psi.ROLE_MAPPER]

    def on_init(self):
        self.map = MapGrid(psi.config.MAX_TILE, 0)
        self._render = psi.engine.render_batch.RenderBatchOpt(GL_QUADS)

        tile_size = psi.config.TILE_PIXEL_SIZE
        draw_box = psi.graphics.draw_box
        _map = self.map._map
        cx, cy = self.map._center

        self._render.count = self.map._size**2*4
        self._render.vertex_buffer = psi.graphics._mapgrid_vertexbuffer
        self._render.color_buffer.set_array(np.array(psi.graphics._mapgrid_colors, dtype='float32'))
        self.create()

    def __getstate__(self):
        return {}

    def __setstate__(self, state):
        self.on_init()

    def set(self, center):
        v = random.random()
        for i in xrange(-5, 6, 1):
            for j in xrange(-5, 6, 1):
                val = None
                if i == 0 and j == 0:
                    val = 1
                elif (abs(i) + abs(j)) < 6:
                    val = 1./(abs(i) + abs(j))

                if val is not None:
                    self.map[i+center[0], j+center[1]] = val

                    x = (i+self.map._center[0]+center[0])
                    y = (j+self.map._center[1]+center[1])
                    index = x*self.map._size*4 + y*4
                    self._render.color_buffer[index:index+4] = np.array([(1-val)*v, (1-val), (1-val)*(1-v), 0.6])
    
    def create(self):
        self.set([0, 0])
        import random
        for _ in xrange(10):
            i = random.randint(-40, 40)
            j = random.randint(-40, 40)
            self.set([i, j])

    def on_draw(self, tick):
        psi.graphics.draw_batch(self._render)


class StubRobot(BaseRobot):
    name = 'Stub Robot'
    roles = [psi.ROLE_ROBOT]

    def __init__(self):
        super(StubRobot, self).__init__()
        self.pos += (30, 30)
        self.th = 60

    def on_update(self, tick):
        self.th += -1

    def on_stop(self):
        self.th = 60

def pip(x, y, poly):
    n = len(poly)
    inside =False

    p1x,p1y = poly[0]
    for i in range(n+1):
        p2x,p2y = poly[i % n]
        if y > min(p1y,p2y):
            if y <= max(p1y,p2y):
                if x <= max(p1x,p2x):
                    if p1y != p2y:
                        xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x,p1y = p2x,p2y

    return inside

from psi.tools.timer import Timer
import scipy
import scipy.spatial

def bresenham(x0, y0, x1, y1, step=1):
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


class TesteBoy(Component):
    name = 'Teste boy'
    roles = [psi.ROLE_ROBOT]

    def on_init(self):
        self.mark = None
        self.aux = []
        self.inside = []
        self.outside = []
        self.center = Vector2(0, 0)
        self.var = 'lol'
        self.lll = 'lll'
        self.component = None

    def on_mouse_down(self, button, pos):
        tsize = psi.config.TILE_PIXEL_SIZE
        update = False
        if button == psi.MOUSE_RIGHT:
            self.center = psi.calc.virtual_coord(pos)
            self.center = psi.calc.snap_to_grid(self.center)
            update = True

        if button == psi.MOUSE_LEFT:
            self.mark = psi.calc.virtual_coord(pos)
            self.mark = psi.calc.snap_to_grid(self.mark)
            update = True

        if update:

            d = scipy.spatial.distance.euclidean(self.center, self.mark)
            th = np.rad2deg(np.arctan2(self.center[1]-self.mark[1], self.center[0]-self.mark[0]))

            self.inside = set()
            self.aux = []

            timer = Timer()
            timer.tic
            points = bresenham(int(self.center[0]), int(self.center[1]), int(self.mark[0]), int(self.mark[1]), tsize)
            self.inside.update(points)
            for angle in xrange(-15, 15, 2):
                # angle = a_/2.
                r = psi.calc.rotation_matrix(angle)
                p = (Vector2(*r.dot(self.mark-self.center).tolist()))+self.center

                points = bresenham(int(self.center[0]), int(self.center[1]), int(p[0]), int(p[1]), tsize)
                self.inside.update(points)
            t = timer.toc()
            print '\n::: %.4f seconds.'%t


    def on_draw(self, tick):
        tsize = psi.config.TILE_PIXEL_SIZE
        ht = tsize/2
        # for pos in self.marks:       

        psi.graphics.draw_box(200, 0, tsize, tsize, psi.CYAN)
        psi.graphics.draw_box(0, 200, tsize, tsize, psi.CYAN)
        psi.graphics.draw_box(200, 200, tsize, tsize, psi.CYAN)
        psi.graphics.draw_box(-200, 0, tsize, tsize, psi.CYAN)
        psi.graphics.draw_box(0, -200, tsize, tsize, psi.CYAN)
        psi.graphics.draw_box(-200, -200, tsize, tsize, psi.CYAN)
        psi.graphics.draw_box(-200, 200, tsize, tsize, psi.CYAN)
        psi.graphics.draw_box(200, -200, tsize, tsize, psi.CYAN)
            
        for i in self.inside:
            psi.graphics.draw_box(i[0], i[1], tsize, tsize, (.3, .3, .3, .5))

        for i in self.outside:
            psi.graphics.draw_box(i[0], i[1], tsize, tsize, (.2, .6, .2, .5))

        for a in self.aux:
            ax = Vector2(a[0], a[1])
            psi.graphics.draw_box(ax.x, ax.y, tsize, tsize, psi.BLUE)
            psi.graphics.draw_line([self.center+[ht, ht], ax+(ht, ht)])
            psi.graphics.draw_line([self.mark+(ht, ht), ax+(ht, ht)])

        if self.mark is not None:
            psi.graphics.draw_box(self.mark.x, self.mark.y, tsize, tsize, psi.GREEN)
            psi.graphics.draw_box(self.center.x, self.center.y, tsize, tsize, psi.GREEN)
            psi.graphics.draw_line([self.center+[ht, ht], self.mark+(ht, ht)])

    def ui_options(self, mgr):
        super(TesteBoy, self).ui_options(mgr)
        mgr.add_row('Position', TextArea(self, 'var', UNICODE))
        mgr.add_row('Size', FileChooser(self, 'lll', UNICODE))
        mgr.add_row('Component', ComponentChooser(self, 'component', roles=[psi.ROLE_MAPPER]))