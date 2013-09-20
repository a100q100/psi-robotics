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
import wx.lib.agw.advancedsplash as AS

class SplashScreen(wx.SplashScreen):
    def __init__(self, parent=None):
        bitmap = wx.Bitmap('psi/resources/splash.png', wx.BITMAP_TYPE_PNG)
        splashStyle = wx.SPLASH_CENTRE_ON_SCREEN | wx.SPLASH_NO_TIMEOUT
        super(SplashScreen, self).__init__(bitmap, splashStyle, -1, parent)

# import psi
# class SplashScreen(wx.Frame):
#     def __init__(self, parent=None):
#         bitmap = wx.Bitmap('psi/resources/splash.png', wx.BITMAP_TYPE_PNG)
#         width, height = bitmap.GetWidth(), bitmap.GetHeight()
#         super(SplashScreen, self).__init__(parent, -1, size=(width, height), style=wx.NO_BORDER|wx.FULL_REPAINT_ON_RESIZE)

#         self.Bind(wx.EVT_IDLE, self.idle)

#         panel = wx.Panel(self, -1, size=(width, height))
#         wx.StaticBitmap(panel, -1, bitmap, size=(width, height))
#         # sizer = wx.BoxSizer()
#         # sizer.Add(panel, wx.EXPAND)
#         # self.SetSizer(sizer)

#     def show(self):
#         # self.preloader = PreloaderThread(self, psi.app)
#         self.Centre()
#         self.Show()
#         # self.preloader.start()

#     def idle(self, event):
#         psi.app.on_pre_load()
#         self.Close()
#         psi.window.Show()

# import psi
# import threading

# class PreloaderThread(threading.Thread):
#     def __init__(self, parent, app):
#         threading.Thread.__init__(self)
#         self._parent = parent
#         self._app = app
#         print self._parent, self._app
#         self._is_running = True

#     def run(self):
#         print 'running me...'
#         self._app.on_pre_load()
#         self._is_running = False

# class SplashScreen(wx.Frame):
#     def __init__(self, parent=None):
#         bitmap = wx.Bitmap('psi/resources/splash.png', wx.BITMAP_TYPE_PNG)
#         width, height = bitmap.GetWidth(), bitmap.GetHeight()
#         super(SplashScreen, self).__init__(parent, -1, size=(width, height), style=wx.NO_BORDER|wx.FULL_REPAINT_ON_RESIZE)

#         self.Bind(wx.EVT_IDLE, self.verify)

#         panel = wx.Panel(self, -1, size=(width, height))
#         wx.StaticBitmap(panel, -1, bitmap, size=(width, height))
#         # sizer = wx.BoxSizer()
#         # sizer.Add(panel, wx.EXPAND)
#         # self.SetSizer(sizer)

#     def show(self):
#         # self.preloader = PreloaderThread(self, psi.app)
#         self.Centre()
#         self.Show()
#         # self.preloader.start()

#     def verify(self, event):
#         psi.app.on_pre_load()
#         self.Close()
#         psi.window.Show()
#         # if not self.preloader._is_running:
#         #     self.preloader.join()
#         #     self.Close()
#         #     psi.window.Show()

# class SplashScreen(wx.SplashScreen):
#     def __init__(self, parent=None):
#         bitmap = wx.Bitmap('psi/resources/splash.png', wx.BITMAP_TYPE_PNG)
#         splashStyle = wx.SPLASH_CENTRE_ON_SCREEN | wx.SPLASH_NO_TIMEOUT
#         super(SplashScreen, self).__init__(bitmap, splashStyle, -1, parent)























# TESTES ======================================================================
# class SplashScreen(AS.AdvancedSplash):
#     def __init__(self, parent=None):
#         bitmap = wx.Bitmap('psi/resources/splash.png', wx.BITMAP_TYPE_PNG)
#         splashStyle = AS.AS_CENTER_ON_SCREEN | AS.AS_NOTIMEOUT
#         super(SplashScreen, self).__init__(parent, -1, bitmap=bitmap, agwStyle=splashStyle)



# class SplashScreen(wx.Frame):
#     def __init__(self, parent=None):
#         bitmap = wx.Bitmap('psi/resources/splash.png', wx.BITMAP_TYPE_PNG)
#         width, height = bitmap.GetWidth(), bitmap.GetHeight()
#         super(SplashScreen, self).__init__(parent, -1, size=(width, height), style=wx.NO_BORDER|wx.FULL_REPAINT_ON_RESIZE)

#         panel = wx.Panel(self, -1, size=(width, height))
#         wx.StaticBitmap(panel, -1, bitmap, size=(width, height))
#         # sizer = wx.BoxSizer()
#         # sizer.Add(panel, wx.EXPAND)
#         # self.SetSizer(sizer)
#         self.Centre()
#         self.Show()

# class SplashScreen(wx.Frame):
#     def __init__(self, parent=None):
#         self.bitmap = wx.Bitmap('psi/resources/splash.png', wx.BITMAP_TYPE_PNG)
#         size = (self.bitmap.GetWidth(), self.bitmap.GetHeight())

#         style=wx.SIMPLE_BORDER|wx.STAY_ON_TOP
#         super(SplashScreen, self).__init__(parent, -1, title='lol', size=size, style=style)

#         # self.Bind(wx.EVT_LEFT_DOWN, self.OnMouseClick)
#         self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
#         self.Bind(wx.EVT_PAINT, self.OnPaint)
#         self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBG)

#         self.Centre()
#         self.Show(True)

#     def OnPaint(self, event):
#         dc = wx.PaintDC(self)
#         dc.DrawBitmap(self.bitmap, 0,0, False)

#     def OnEraseBG(self, event):
#         pass

#     def OnCloseWindow(self, event=None):
#         self.Show(False)
#         self.Destroy()


# class SplashScreen(wx.Frame):
#     def __init__(self, parent=None):
#         bitmap = wx.Bitmap('psi/resources/splash.png', wx.BITMAP_TYPE_PNG)
#         width, height = bitmap.GetWidth(), bitmap.GetHeight()
#         super(SplashScreen, self).__init__(parent, -1, size=(width, height), style=wx.FULL_REPAINT_ON_RESIZE|wx.DOUBLE_BORDER)

#         # panel = wx.Panel(self, -1)
#         # bitmap = wx.Bitmap('psi/resources/splash.png', wx.BITMAP_TYPE_PNG)
#         panel = wx.Panel(self, -1, size=(width, height))
#         wx.StaticBitmap(panel, -1, bitmap, size=(width, height))

#         self.Centre()
#         self.Show()


#         # splashStyle = wx.SPLASH_CENTRE_ON_SCREEN | wx.SPLASH_NO_TIMEOUT
#         # super(SplashScreen, self).__init__(bitmap, splashStyle, -1, parent)