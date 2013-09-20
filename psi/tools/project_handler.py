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

import os
import json
import time
import cPickle as pickle
import zipfile
import StringIO

import psi


def save_as(path): 
    raw_components = psi.manager._allcomponents

    info = json.dumps({'version':psi.VERSION})
    components = pickle.dumps(raw_components)

    psi_file = zipfile.ZipFile(path, 'w')
    psi_file.writestr('INFO', info)
    psi_file.writestr('components.pickle', components)

    psi_file.close()

def open(path):
    psi_file = zipfile.ZipFile(path, 'r')
    assert len(psi_file.namelist()) == 2, 'Invalid PSI file'

    info = json.load(psi_file.open('INFO'))
    components = pickle.load(psi_file.open('components.pickle'))

    for c in components:
        psi.app.add_component(c)
