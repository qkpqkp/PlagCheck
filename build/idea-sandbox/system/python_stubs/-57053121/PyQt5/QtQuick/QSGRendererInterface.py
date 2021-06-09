# encoding: utf-8
# module PyQt5.QtQuick
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtQuick.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import PyQt5.QtQml as __PyQt5_QtQml
import sip as __sip


class QSGRendererInterface(__sip.simplewrapper):
    # no doc
    def getResource(self, QQuickWindow, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        getResource(self, QQuickWindow, QSGRendererInterface.Resource) -> sip.voidptr
        getResource(self, QQuickWindow, str) -> sip.voidptr
        """
        pass

    def graphicsApi(self): # real signature unknown; restored from __doc__
        """ graphicsApi(self) -> QSGRendererInterface.GraphicsApi """
        pass

    def shaderCompilationType(self): # real signature unknown; restored from __doc__
        """ shaderCompilationType(self) -> QSGRendererInterface.ShaderCompilationTypes """
        pass

    def shaderSourceType(self): # real signature unknown; restored from __doc__
        """ shaderSourceType(self) -> QSGRendererInterface.ShaderSourceTypes """
        pass

    def shaderType(self): # real signature unknown; restored from __doc__
        """ shaderType(self) -> QSGRendererInterface.ShaderType """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    CommandListResource = 2
    CommandQueueResource = 1
    DeviceResource = 0
    Direct3D12 = 3
    GLSL = 1
    HLSL = 2
    OfflineCompilation = 2
    OpenGL = 2
    OpenVG = 4
    PainterResource = 3
    RuntimeCompilation = 1
    ShaderByteCode = 4
    ShaderSourceFile = 2
    ShaderSourceString = 1
    Software = 1
    Unknown = 0
    UnknownShadingLanguage = 0


