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
import logging

class Log(object):
    def __init__(self, buffer_size=100):
        self.buffer_size = 100
        self.count = 0
        self.buffer = []

    def __keep_size(self):
        if self.count > self.buffer_size:
            self.pop(0)

    def debug(self, msg):
        # self.buffer.append((psi.LOG_DEBUG, msg))
        # self.__keep_size()
        print 'DEBUG:', msg

    def info(self, msg):
        self.buffer.append((psi.LOG_INFO, msg))
        self.__keep_size()

        print 'INFO:', msg
        psi.window.set_status_info(msg, psi.LOG_INFO)

    def error(self, msg):
        self.buffer.append((psi.LOG_ERROR, msg))
        self.__keep_size()

        print 'ERROR:', msg
        psi.window.set_status_info(msg, psi.LOG_ERROR)
        
    def warning(self, msg):
        self.buffer.append((psi.LOG_WARNING, msg))
        self.__keep_size()
        
        print 'WARNING:', msg
        psi.window.set_status_info(msg, psi.LOG_WARNING)