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

import wx

VERSION = '1.0.0'

ROLE_ROBOT = 0
ROLE_MAPPER = 1
ROLE_CONTROLLER = 2

STATE_RUNNING = 0
STATE_PAUSED = 1
STATE_STOPPED = 2

LOG_INFO = 0
LOG_DEBUG = 1
LOG_ERROR = 2
LOG_WARNING = 3

ID_NEWPROJECT       = wx.ID_NEW
ID_SAVEPROJECT      = wx.ID_SAVE
ID_SAVEPROJECTAS    = wx.ID_SAVEAS
ID_OPENPROJECT      = wx.ID_OPEN
ID_QUIT             = wx.ID_EXIT
ID_RUN              = wx.NewId()
ID_PAUSE            = wx.NewId()
ID_RESUME           = wx.NewId()
ID_STOP             = wx.NewId()
ID_CENTER           = wx.NewId()
ID_FOLLOWROBOT      = wx.NewId()
ID_ZOOMIN           = wx.ID_ZOOM_IN
ID_ZOOMOUT          = wx.ID_ZOOM_OUT
ID_RESETZOOM        = wx.ID_ZOOM_100
ID_SHOWGRID         = wx.NewId()
ID_ADDCOMPONENT     = wx.NewId()
ID_REMOVECOMPONENT  = wx.NewId()
ID_ABOUT            = wx.ID_HELP

MOUSE_LEFT = wx.MOUSE_BTN_LEFT
MOUSE_MIDDLE = wx.MOUSE_BTN_MIDDLE
MOUSE_RIGHT = wx.MOUSE_BTN_RIGHT
MOUSE_ANY = wx.MOUSE_BTN_ANY

ALICE_BLUE                  = (0.9412, 0.9725, 1.0000, 1.0000)
ANTIQUE_WHITE               = (0.9804, 0.9216, 0.8431, 1.0000)
AQUA                        = (0.0000, 1.0000, 1.0000, 1.0000)
AQUAMARINE                  = (0.4980, 1.0000, 0.8314, 1.0000)
AZURE                       = (0.9412, 1.0000, 1.0000, 1.0000)
BEIGE                       = (0.9608, 0.9608, 0.8627, 1.0000)
BISQUE                      = (1.0000, 0.8941, 0.7686, 1.0000)
BLACK                       = (0.0000, 0.0000, 0.0000, 1.0000)
BLANCHED_ALMOND             = (1.0000, 0.9216, 0.8039, 1.0000)
BLUE                        = (0.0000, 0.0000, 1.0000, 1.0000)
BLUE_VIOLET                 = (0.5412, 0.1686, 0.8863, 1.0000)
BROWN                       = (0.6471, 0.1647, 0.1647, 1.0000)
BURLY_WOOD                  = (0.8706, 0.7216, 0.5294, 1.0000)
CADET_BLUE                  = (0.3725, 0.6196, 0.6275, 1.0000)
CHARTREUSE                  = (0.4980, 1.0000, 0.0000, 1.0000)
CHOCOLATE                   = (0.8235, 0.4118, 0.1176, 1.0000)
CORNFLOWER_BLUE             = (0.3922, 0.5843, 0.9294, 1.0000)
CORNSILK                    = (1.0000, 0.9725, 0.8627, 1.0000)
CRIMSOM                     = (0.8627, 0.0784, 0.2353, 1.0000)
CYAN                        = (0.0000, 1.0000, 1.0000, 1.0000)
DARK_BLUE                   = (0.0000, 0.0000, 0.5451, 1.0000)
DARK_CYAN                   = (0.0000, 0.5451, 0.5451, 1.0000)
DARK_GOLDENROD              = (0.7216, 0.5255, 0.0431, 1.0000)
DARK_GRAY                   = (0.2510, 0.2510, 0.2510, 1.0000)
DARK_GREEN                  = (0.0000, 0.3922, 0.0000, 1.0000)
DARK_KHAKI                  = (0.7412, 0.7176, 0.4196, 1.0000)
DARK_MAGENTA                = (0.5451, 0.0000, 0.5451, 1.0000)
DARK_OLIVE_GREEN            = (0.3333, 0.4196, 0.1843, 1.0000)
DARK_ORANGE                 = (1.0000, 0.5490, 0.0000, 1.0000)
DARK_ORCHID                 = (0.6000, 0.1961, 0.8000, 1.0000)
DARK_RED                    = (0.5451, 0.0000, 0.0000, 1.0000)
DARK_SALMAN                 = (0.9137, 0.5882, 0.4784, 1.0000)
DARK_SEA_GREEN              = (0.5608, 0.7373, 0.5451, 1.0000)
DARK_SLATE_BLUE             = (0.2824, 0.2392, 0.5451, 1.0000)
DARK_SLATE_GRAY             = (0.1843, 0.3098, 0.3098, 1.0000)
DARK_TURQUOISE              = (0.0000, 0.8078, 0.8196, 1.0000)
DARK_VIOLET                 = (0.5804, 0.0000, 0.8275, 1.0000)
DEEP_PINK                   = (1.0000, 0.0784, 0.5765, 1.0000)
DEEP_SKY_BLUE               = (0.0000, 0.7490, 1.0000, 1.0000)
DIM_GRAY                    = (0.4118, 0.4118, 0.4118, 1.0000)
DODGER_BLUE                 = (0.1176, 0.5647, 1.0000, 1.0000)
FIRE_BRICK                  = (0.6980, 0.1333, 0.1333, 1.0000)
FLORAL_WHITE                = (1.0000, 0.9804, 0.9412, 1.0000)
FOREST_GREEN                = (0.1333, 0.5451, 0.1333, 1.0000)
FUCHSIA                     = (1.0000, 0.0000, 1.0000, 1.0000)
GAINSBORO                   = (0.8627, 0.8627, 0.8627, 1.0000)
GHOST_WHITE                 = (0.9725, 0.9725, 1.0000, 1.0000)
GOLD                        = (1.0000, 0.8431, 0.0000, 1.0000)
GOLDNROD                    = (0.8549, 0.6471, 0.1255, 1.0000)
GRAY                        = (0.5020, 0.5020, 0.5020, 1.0000)
GREEN                       = (0.0000, 1.0000, 0.0000, 1.0000)
GREEN_YELLOW                = (0.6784, 1.0000, 0.1843, 1.0000)
HONEYDEW                    = (0.9412, 1.0000, 0.9412, 1.0000)
HOT_PINK                    = (1.0000, 0.4118, 0.7059, 1.0000)
INDIAN_RED                  = (0.8039, 0.3608, 0.3608, 1.0000)
INDIGO                      = (0.2941, 0.0000, 0.5098, 1.0000)
IVORY                       = (1.0000, 1.0000, 0.9412, 1.0000)
KHAKI                       = (0.9412, 0.9020, 0.5490, 1.0000)
LAVENDER                    = (0.9020, 0.9020, 0.9804, 1.0000)
LAVENDER_BLUE               = (0.8000, 0.8000, 1.0000, 1.0000)
LAVENDER_BLUSH              = (1.0000, 0.9412, 0.9608, 1.0000)
LAWN_GREEN                  = (0.4863, 0.9882, 0.0000, 1.0000)
LEMON_CHIFFON               = (1.0000, 0.9804, 0.8039, 1.0000)
LIGHT_BLUE                  = (0.6784, 0.8471, 0.9020, 1.0000)
LIGHT_CORAL                 = (0.9412, 0.5020, 0.5020, 1.0000)
LIGHT_CYAN                  = (0.8784, 1.0000, 1.0000, 1.0000)
LIGHT_FRENCH_LAVANDER       = (0.6588, 0.6000, 0.9020, 1.0000)
LIGHT_GOLDENROD_YELLOW      = (0.9804, 0.9804, 0.8235, 1.0000)
LIGHT_GRAY                  = (0.8275, 0.8275, 0.8275, 1.0000)
LIGHT_GREEN                 = (0.5647, 0.9333, 0.5647, 1.0000)
LIGHT_PINK                  = (1.0000, 0.7137, 0.7569, 1.0000)
LIGHT_SALMON                = (1.0000, 0.6275, 0.4784, 1.0000)
LIGHT_SEA_GREEN             = (0.1255, 0.6980, 0.6667, 1.0000)
LIGHT_SKY_BLUE              = (0.5294, 0.8078, 0.9804, 1.0000)
LIGHT_SLATE_GRAY            = (0.4667, 0.5333, 0.6000, 1.0000)
LIGHT_STEEL_BLUE            = (0.6902, 0.7686, 0.8706, 1.0000)
LIGHT_YELLOW                = (1.0000, 1.0000, 0.8784, 1.0000)
LIME                        = (0.0000, 1.0000, 0.0000, 1.0000)
LIME_GREEN                  = (0.1961, 0.8039, 0.1961, 1.0000)
LINEN                       = (0.9804, 0.9412, 0.9020, 1.0000)
MAGENTA                     = (1.0000, 0.0000, 1.0000, 1.0000)
MAROON                      = (0.5020, 0.0000, 0.0000, 1.0000)
MEDIUM_AQUAMARINE           = (0.4000, 0.8039, 0.6667, 1.0000)
MEDIUM_BLUE                 = (0.0000, 0.0000, 0.8039, 1.0000)
MEDIUM_ORCHID               = (0.7294, 0.3333, 0.8275, 1.0000)
MEDIUM_PURPLE               = (0.5765, 0.4392, 0.8588, 1.0000)
MEDIUM_SEA_GREEN            = (0.2353, 0.7020, 0.4431, 1.0000)
MEDIUM_SLATE_BLUE           = (0.4824, 0.4078, 0.9333, 1.0000)
MEDIUM_SPRING_GREEN         = (0.0000, 0.9804, 0.6039, 1.0000)
MEDIUM_TURQUOISE            = (0.2824, 0.8196, 0.8000, 1.0000)
MEDIUM_VIOLETRED            = (0.7804, 0.0824, 0.5216, 1.0000)
MIDNIGHT_BLUE               = (0.0980, 0.0980, 0.4392, 1.0000)
MINT_CREAM                  = (0.9608, 1.0000, 0.9804, 1.0000)
MISTY_ROSE                  = (1.0000, 0.8941, 0.8824, 1.0000)
MOCCASIN                    = (1.0000, 0.8941, 0.7098, 1.0000)
NAVAJO_WHITE                = (1.0000, 0.8706, 0.6784, 1.0000)
NAVY                        = (0.0000, 0.0000, 0.5020, 1.0000)
OLD_LACE                    = (0.9922, 0.9608, 0.9020, 1.0000)
OLIVE                       = (0.5020, 0.5020, 0.0000, 1.0000)
OLIVE_DRAB                  = (0.4196, 0.5569, 0.1373, 1.0000)
ORANGE                      = (1.0000, 0.6471, 0.0000, 1.0000)
ORANGE_RED                  = (1.0000, 0.2706, 0.0000, 1.0000)
ORCHID                      = (0.8549, 0.4392, 0.8392, 1.0000)
PALE_GOLDENROD              = (0.9333, 0.9098, 0.6667, 1.0000)
PALE_GREEN                  = (0.5961, 0.9843, 0.5961, 1.0000)
PALE_TURQUOISE              = (0.6863, 0.9333, 0.9333, 1.0000)
PALE_VIOLET_RED             = (0.8588, 0.4392, 0.5765, 1.0000)
PAPAYA_WHIP                 = (1.0000, 0.9373, 0.8353, 1.0000)
PEACH_PUFF                  = (1.0000, 0.8549, 0.7255, 1.0000)
PERIWINKLE                  = (0.8000, 0.8000, 1.0000, 1.0000)
PERU                        = (0.8039, 0.5216, 0.2471, 1.0000)
PINK                        = (1.0000, 0.7529, 0.7961, 1.0000)
PLUM                        = (0.8667, 0.6275, 0.8667, 1.0000)
POWDER_BLUE                 = (0.6902, 0.8784, 0.9020, 1.0000)
PURPLE                      = (0.5020, 0.0000, 0.5020, 1.0000)
RED                         = (1.0000, 0.0000, 0.0000, 1.0000)
ROSY_BROWN                  = (0.7373, 0.5608, 0.5608, 1.0000)
ROYAL_BLUE                  = (0.2549, 0.4118, 0.8824, 1.0000)
SADDLE_BROWN                = (0.5451, 0.2706, 0.0745, 1.0000)
SALMON                      = (0.9804, 0.5020, 0.4471, 1.0000)
SANDY_BROWN                 = (0.9569, 0.6431, 0.3765, 1.0000)
SEA_GREEN                   = (0.1804, 0.5451, 0.3412, 1.0000)
SEA_SHELL                   = (1.0000, 0.9608, 0.9333, 1.0000)
SIENNA                      = (0.6275, 0.3216, 0.1765, 1.0000)
SILVER                      = (0.7529, 0.7529, 0.7529, 1.0000)
SKY_BLUE                    = (0.5294, 0.8078, 0.9216, 1.0000)
SLATE_BLUE                  = (0.4157, 0.3529, 0.8039, 1.0000)
SLATE_GRAY                  = (0.4392, 0.5020, 0.5647, 1.0000)
SNOW                        = (1.0000, 0.9804, 0.9804, 1.0000)
SPRING_GREEN                = (0.0000, 1.0000, 0.4980, 1.0000)
STEEL_BLUE                  = (0.2745, 0.5098, 0.7059, 1.0000)
TAN                         = (0.8235, 0.7059, 0.5490, 1.0000)
TEAL                        = (0.0000, 0.5020, 0.5020, 1.0000)
THISTLE                     = (0.8471, 0.7490, 0.8471, 1.0000)
TOMATO                      = (1.0000, 0.3882, 0.2784, 1.0000)
TRANSPARENT                 = (0.0000, 0.0000, 0.0000, 0.0000)
TURQUOISE                   = (0.2510, 0.8784, 0.8157, 1.0000)
VIOLET                      = (0.9333, 0.5098, 0.9333, 1.0000)
WHEAT                       = (0.9608, 0.8706, 0.7020, 1.0000)
WHITE                       = (1.0000, 1.0000, 1.0000, 1.0000)
WHITE_SMOKE                 = (0.9608, 0.9608, 0.9608, 1.0000)
YELLOW                      = (1.0000, 1.0000, 0.0000, 1.0000)
YELLOW_GREEN                = (0.6039, 0.8039, 0.1961, 1.0000)