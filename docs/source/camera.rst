======
Camera
======


The Camera object is responsible to control the scene view in PSI. The camera position defines the translation of all object in the scene and which objects will be visible to the user. A camera view is defined by a rect where the camera position is the central point and the dimensions is the size of the canvas. i.e.:

::

                            +------------------------+
                            |                        |
                            |                        |
                            |           x            | canvas height
                            |     camera position    |
                            |                        |
                            +------------------------+
                                   canvas width

By default, the camera starts on the position (0, 0), where it is also the center of the map. The coordinate system of PSI follows the usual way of orienting axes, with the positive x-axis pointing right and the positive y-axis pointing up. Remember that in OpenGL y-axis is inversed.

::

                            +------------------------+
                            |           ^ y          |
                            |           |      x     |
                            |           x------>     | 
                            |                        |
                            |                        |
                            +------------------------+

