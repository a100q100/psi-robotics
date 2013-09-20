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

import re
import psi

class FLOAT(object):
    @classmethod
    def to_string(cls, val): return unicode(val)

    @classmethod
    def to_type(cls, val): return float(val)

class INTEGER(object):
    @classmethod
    def to_string(cls, val): return unicode(val)

    @classmethod
    def to_type(cls, val): return int(val)

class UNICODE(object):
    @classmethod
    def to_string(cls, val): return unicode(val)

    @classmethod
    def to_type(cls, val): return unicode(val)

class VECTOR2(object):
    @classmethod
    def to_string(cls, val): return u'%.1f, %.1f'%(val.x, val.y)

    @classmethod
    def to_type(cls, val): 
        x, y = [float(v.strip()) for v in val.split(',')]
        return psi.euclid.Vector2(x, y)

class COMPONENT(object):
    @classmethod
    def to_string(cls, val):
        if val is None:
            return ''
        else:
            return val.to_string()

    @classmethod
    def to_type(cls, val): 
        if val != '':
            id_ = re.findall('\(#(\d+)\)', val)
            id_ = int(id_)
            component = psi.manager.get_component_by_id(id_)
            return component

        return None
