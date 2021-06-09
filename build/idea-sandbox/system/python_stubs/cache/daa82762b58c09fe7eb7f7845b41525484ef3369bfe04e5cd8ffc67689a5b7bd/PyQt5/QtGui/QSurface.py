# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QSurface(__sip.simplewrapper):
    # no doc
    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> QSurfaceFormat """
        return QSurfaceFormat

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> QSize """
        pass

    def supportsOpenGL(self): # real signature unknown; restored from __doc__
        """ supportsOpenGL(self) -> bool """
        return False

    def surfaceClass(self): # real signature unknown; restored from __doc__
        """ surfaceClass(self) -> QSurface.SurfaceClass """
        pass

    def surfaceType(self): # real signature unknown; restored from __doc__
        """ surfaceType(self) -> QSurface.SurfaceType """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    MetalSurface = 5
    Offscreen = 1
    OpenGLSurface = 1
    OpenVGSurface = 3
    RasterGLSurface = 2
    RasterSurface = 0
    VulkanSurface = 4
    Window = 0


