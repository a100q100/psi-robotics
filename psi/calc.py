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

import math
import numpy as np
import psi

def clip(value, min_value, max_value):
    return max(min_value, min(max_value, value))

def rotation_matrix(rotation):
    angle = np.deg2rad(rotation)
    c, s = np.cos(angle), np.sin(angle)
    return np.array([[c, -s], [s, c]])

def obstacle_position(sonar_distance, sonar_angle, robot_position, robot_angle):
    angle = np.deg2rad(-(sonar_angle - robot_angle))
    x = np.cos(angle)*sonar_distance
    y = np.sin(angle)*sonar_distance
    return (y+robot_position[1], x+robot_position[0]) #invert axis

def point_in_polygon(point, polygon):
    n = len(polygon)
    x, y = point
    inside =False

    p1x, p1y = polygon[0]
    for i in range(n+1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y

    return inside

def snap_to_grid(pos):
    tsize = psi.config.TILE_PIXEL_SIZE
    return pos-(pos.x%tsize, pos.y%tsize)

def virtual_coord(pos):
    v_pos = pos - psi.window.get_canvas_size()//2 
    return v_pos + psi.graphics.get_camera_pos()

# print obstacle_position(100, 90, (0, 0), 0)