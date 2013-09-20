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


import random
import itertools

import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.arrays.vbo import VBO

import psi
from psi.euclid import Vector2
from .camera import Camera
from .render_batch import RenderBatch
from .grid import Grid
from psi.tools.timer import Timer

__all__ = ['Graphics']


class Graphics(object):
    def __init__(self):
        self._is_middle_down = False
        self._last_mouse_position = Vector2(0, 0)

        self._render_batch = RenderBatch(GL_QUADS)
        self._overlay_batch = RenderBatch(GL_LINES)
        self._grid = None
        self._mapgrid_colors = None
        self._mapgrid_vertexes = None
        self._mapgrid_vertexbuffer = None
        self._batches = []
        self.camera = Camera()

    # =========================================================================
    # INTERNAL FUNCTIONS
    # =========================================================================
    def _set_projection(self, size):
        width, height = size.x, size.y
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION);
        glLoadIdentity();
        glOrtho(0, width, 0, height, -1.0, 1.0);

        glMatrixMode(GL_MODELVIEW)

    def _set_display(self):
        glEnable(GL_TEXTURE_2D)
        glEnable(GL_COLOR_MATERIAL)

        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)        
        
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LEQUAL)
        glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
        glDisable(GL_DEPTH_TEST)
    # =========================================================================

    # =========================================================================
    # ACCESS METHODS
    # =========================================================================
    # CAMERA
    def get_camera_pos(self): 
        return self.camera.pos

    def get_camera_zoom(self):
        return self.camera.zoom

    def get_camera_scale(self):
        return self.camera._scale_rate

    def camera_zoom_in(self):
        self.camera.zoom_in()

    def camera_zoom_out(self):
        self.camera.zoom_out()

    def camera_reset_zoom(self):
        self.camera.reset_zoom()

    def camera_pan(self, delta):
        self.camera.pan(delta)

    # =========================================================================
    # DRAWING SHORTCUTS
    # =========================================================================
    def draw_batch(self, batch):
        self._batches.append(batch)

    def draw_box(self, x, y, dx, dy, color=(0, 0, 0, 1), rotation=0, center=(0, 0)):
        points = [
            (x, y),
            (x+dx, y),
            (x+dx, y+dy),
            (x, y+dy)
        ]
        self._render_batch.draw2d(points, color, rotation, center)

    def draw_quads(self, points, color=(0, 0, 0, 1), rotation=0, center=(0, 0)):
        self._render_batch.draw2d(points, color, rotation, center)

    def draw_line(self, points, color=(0, 0, 0, 1), rotation=0, center=(0, 0)):
        self._overlay_batch.draw2d(points, color, rotation, center)

    def draw_grid(self):
        zoom = psi.graphics.camera.zoom
        tsize = psi.config.TILE_PIXEL_SIZE

        w, h = psi.window.canvas.GetSize()
        w, h = int(w*zoom)//2, int(h*zoom)//2

        cx, cy = psi.graphics.camera.pos.toint()
        cx, cy = int(cx*zoom + w), int(cy*zoom + h)
        
        ox, oy = ((w-cx)%tsize), ((h-cy)%tsize) #offset

        range_x = (cx-w, cx+w)
        range_y = (cy-h, cy+h)

        for x in xrange(range_x[0]+ox, range_x[1]+ox, tsize):
            self.draw_line([(x, range_y[0]), (x, range_y[1])], color=(.1, .9, .1, .6))

        for y in xrange(range_y[0]+oy, range_y[1]+oy, tsize):
            self.draw_line([(range_x[0], y), (range_x[1], y)], color=(.1, .9, .1, .6))
    # =========================================================================

    # =========================================================================
    # EVENTS
    # =========================================================================
    def on_pre_load(self):
        print 'at psi.graphics.on_pre_load'
        timer = Timer()
        timer.tic()

        tile_size = psi.config.TILE_PIXEL_SIZE
        n_tile = psi.config.MAX_TILE
        center = n_tile//2
        
        n = n_tile*n_tile*4
        self._mapgrid_vertexes = np.zeros([n, 2], dtype='float32')
        self._mapgrid_colors = np.zeros([n, 4], dtype='float32')
        # self._mapgrid_colors = np.random.random([n, 4]).astype('float32')

        i = 0
        start = (0-center)*tile_size
        end = (n_tile-center)*tile_size

        tiles = itertools.product(
            xrange(start, end, tile_size), 
            xrange(start, end, tile_size)
        )
        v = self._mapgrid_vertexes
        for row, col in tiles:
            x1, y1 = col, row
            x2, y2 = x1+tile_size, y1+tile_size
            # if i>10: raw_input()
            # print [[x1, y1], [x2, y1], [x2, y2], [x1, y2]]
            v[i:i+4, :] = [[x1, y1], [x2, y1], [x2, y2], [x1, y2]]
            i += 4
        
        # v = self._mapgrid_vertexes
        # row_cont = 0
        # for row in xrange(start, end, tile_size):
        #     # for col in xrange(start, end, tile_size):
        #     col_cont = row_cont
        #     for col in xrange(row, end, tile_size):
        #         x1, y1 = col, row
        #         x2, y2 = x1+tile_size, y1+tile_size
                
        #         j = col_cont*(4*n_tile) + row_cont*4
        #         v[i:i+4, :] = [[x1, y1], [x2, y1], [x2, y2], [x1, y2]]
        #         v[j:j+4, :] = [[y1, x1], [y1, x2], [y2, x2], [y2, x1]]
        #         # v[(i+0)] = [x1, y1]
        #         # v[(i+1)] = [x2, y1]
        #         # v[(i+2)] = [x2, y2]
        #         # v[(i+3)] = [x1, y2]

        #         # v[(j+0)] = [y1, x1]
        #         # v[(j+1)] = [y1, x2]
        #         # v[(j+2)] = [y2, x2]
        #         # v[(j+3)] = [y2, x1]

        #         i+=4
        #         col_cont += 1

        #     row_cont += 1
        #     i += 4*row_cont

        self._mapgrid_vertexbuffer = VBO(self._mapgrid_vertexes)

        s = timer.toc()
        print 'Timer elapsed: %.4f seconds'%s

    def on_init(self): 
        print 'at psi.graphics.on_init.'
        size = psi.window.canvas.canvas_size
        
        self.camera.half_size = size/2.
        self._set_projection(size)
        self._set_display()
        self._grid = Grid(size)

    def on_quit(self): print 'at psi.graphics.on_quit.'

    def on_draw(self, tick):
        # timer = Timer()
        # timer.tic()
        glClear(GL_COLOR_BUFFER_BIT);
        glClearColor(*psi.WHITE);
        # glClearColor(0.341176, 0.46274, 0.466666, 1.);

        
        glPushMatrix()
        self.camera.locate()

        # if self.camera.zoom <= 1.5:
        #     self.draw_grid()

        for render in self._batches:
            render.render()
        
        self._grid.on_draw(tick)

        self._overlay_batch.render()
        self._render_batch.render()

        self._batches = []
        self._render_batch.clear()
        self._overlay_batch.clear()


        glPopMatrix()
        # t = timer.toc()
        # print 'graphics.on_draw: %.4f seconds'%t


    def on_run(self): print 'at psi.graphics.on_run.'

    def on_update(self, tick): pass#print 'at psi.graphics.on_update.'

    def on_pause(self): print 'at psi.graphics.on_pause.'

    def on_resume(self): print 'at psi.graphics._on_resume'

    def on_stop(self): print 'at psi.graphics.on_stop.'


    def on_window_resize(self, size):
        self._set_projection(size)
        self._set_display()
        self._grid.on_window_resize(size)
        self.camera.on_window_resize(size)

    def on_key_down(self): print 'at psi.graphics.on_key_down.'

    def on_key_up(self): print 'at psi.graphics.on_key_up.'

    def on_mouse_motion(self, pos):
        if self._is_middle_down:
            delta = self._last_mouse_position - pos
            # delta.y = -delta.y
            self.camera.pan(delta)
            self._last_mouse_position = pos

    def on_mouse_down(self, button, pos):
        if button == psi.MOUSE_MIDDLE:
            self._is_middle_down = True
            self._last_mouse_position = pos

    def on_mouse_up(self, button, pos):
        if button == psi.MOUSE_MIDDLE:
            self._is_middle_down = False

    def on_mouse_wheel(self, delta, pos):
        if delta > 0: self.camera.zoom_in()
        if delta < 0: self.camera.zoom_out()
    # =========================================================================
