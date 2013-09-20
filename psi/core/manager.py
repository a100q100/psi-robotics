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

__all__ = ['Manager']


class Manager(object):
    def __init__(self):
        self._components = [[], [], []]
        self._allcomponents = []
        self._registry = []
        self._count = 0

    def add(self, component):
        if psi.ROLE_ROBOT in component.roles:
            self._components[psi.ROLE_ROBOT].append(component)

        elif psi.ROLE_MAPPER in component.roles:
            self._components[psi.ROLE_MAPPER].append(component)

        elif psi.ROLE_CONTROLLER in component.roles:
            self._components[psi.ROLE_CONTROLLER].append(component)
        
        else:
            raise Exception('Unknown component role')

        self._count += 1
        self._allcomponents.append(component)

    def get_robots(self):
        return self._components[psi.ROLE_ROBOT]
        
    def get_mappers(self):
        return self._components[psi.ROLE_MAPPER]

    def get_controllers(self):
        return self._components[psi.ROLE_CONTROLLER]

    def get_components(self):
        return self._allcomponents

    def get_component_count(self):
        return self._count

    def get_component_by_id(self, id_):
        for c in self.get_components():
            if c.id == id_:
                return c

    def remove(self, component):
        if psi.ROLE_ROBOT in component.roles:
            self._components[psi.ROLE_ROBOT].remove(component)

        elif psi.ROLE_MAPPER in component.roles:
            self._components[psi.ROLE_MAPPER].remove(component)

        elif psi.ROLE_CONTROLLER in component.roles:
            self._components[psi.ROLE_CONTROLLER].remove(component)
        
        else:
            raise Exception('Unknown component role')

        self._count -= 0
        self._allcomponents.remove(component)

    def clear(self):
        self._components = [[], [], []]
        self._allcomponents = []
        self._count = 0

    def __iter__(self):
        for component in self._components[psi.ROLE_ROBOT]:
            yield component

        for component in self._components[psi.ROLE_MAPPER]:
            yield component

        for component in self._components[psi.ROLE_CONTROLLER]:
            yield component

    def reversed(self):
        for component in self._components[psi.ROLE_MAPPER]:
            yield component

        for component in self._components[psi.ROLE_CONTROLLER]:
            yield component
            
        for component in self._components[psi.ROLE_ROBOT]:
            yield component

    def on_update(self, tick):
        for component in self:
            component.on_update(tick)

    def on_draw(self, tick):
        for component in self.reversed():
            component.on_draw(tick)

    def on_run(self):
        for component in self:
            component.on_run()

    def on_pause(self):
        for component in self:
            component.on_pause()

    def on_resume(self):
        for component in self:
            component.on_resume()

    def on_unpause(self):
        for component in self:
            component.on_unpause()

    def on_stop(self):
        for component in self:
            component.on_stop()

    def on_key_down(self):
        for component in self:
            component.on_key_down()

    def on_key_up(self):
        for component in self:
            component.on_key_up()

    def on_mouse_motion(self, pos):
        for component in self:
            component.on_mouse_motion(pos)

    def on_mouse_down(self, button, pos):
        for component in self:
            component.on_mouse_down(button, pos)

    def on_mouse_up(self, button, pos):
        for component in self:
            component.on_mouse_up(button, pos)

    def on_mouse_wheel(self, delta, pos):
        for component in self:
            component.on_mouse_wheel(delta, pos)