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

app = psi.App()

psi.manager._registry.extend([
    # psi.core.components.StubRobot,
    psi.core.components.StubMapper,
    psi.core.components.TesteBoy,
    psi.core.components.ReplayRobot,
    psi.core.components.HimmMapper,
])

print 'adding components...'
t = psi.core.components.TesteBoy()
psi.app.add_component(t)
robot = psi.core.components.ReplayRobot()
# t.component = robot
robot._path = 'C:\\Users\\Renato\\Dropbox\\Renato\\Dev\\python\\psi\\examples\\arffs\\irregular.arff'
# robot._path = 'D:\\Dropbox\\Renato\\Dev\\python\\psi\\examples\\arffs\\irregular.arff'
# robot._path = 'D:\\Dropbox\\Renato\\Dev\\python\\psi\\examples\\arffs\\maze.arff'
# robot._path = 'D:\\Dropbox\\Renato\\Dev\\python\\psi\\examples\\arffs\\linaker1v.arff'
# robot._path = '/home/renatopp/Dropbox/Renato/Dev/python/psi/examples/arffs/maze.arff'
psi.app.add_component(robot)
mapper = psi.core.components.HimmMapper()
mapper.robot = robot
psi.app.add_component(mapper)

app.main_loop()