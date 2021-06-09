# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QOpenGLContext(__PyQt5_QtCore.QObject):
    """ QOpenGLContext(parent: QObject = None) """
    def aboutToBeDestroyed(self): # real signature unknown; restored from __doc__
        """ aboutToBeDestroyed(self) [signal] """
        pass

    def areSharing(self, QOpenGLContext, QOpenGLContext_1): # real signature unknown; restored from __doc__
        """ areSharing(QOpenGLContext, QOpenGLContext) -> bool """
        return False

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def create(self): # real signature unknown; restored from __doc__
        """ create(self) -> bool """
        return False

    def currentContext(self): # real signature unknown; restored from __doc__
        """ currentContext() -> QOpenGLContext """
        return QOpenGLContext

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultFramebufferObject(self): # real signature unknown; restored from __doc__
        """ defaultFramebufferObject(self) -> int """
        return 0

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def doneCurrent(self): # real signature unknown; restored from __doc__
        """ doneCurrent(self) """
        pass

    def extensions(self): # real signature unknown; restored from __doc__
        """ extensions(self) -> Set[QByteArray] """
        pass

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> QSurfaceFormat """
        return QSurfaceFormat

    def getProcAddress(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ getProcAddress(self, Union[QByteArray, bytes, bytearray]) -> sip.voidptr """
        pass

    def globalShareContext(self): # real signature unknown; restored from __doc__
        """ globalShareContext() -> QOpenGLContext """
        return QOpenGLContext

    def hasExtension(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ hasExtension(self, Union[QByteArray, bytes, bytearray]) -> bool """
        return False

    def isOpenGLES(self): # real signature unknown; restored from __doc__
        """ isOpenGLES(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def makeCurrent(self, QSurface): # real signature unknown; restored from __doc__
        """ makeCurrent(self, QSurface) -> bool """
        return False

    def nativeHandle(self): # real signature unknown; restored from __doc__
        """ nativeHandle(self) -> Any """
        pass

    def openGLModuleHandle(self): # real signature unknown; restored from __doc__
        """ openGLModuleHandle() -> sip.voidptr """
        pass

    def openGLModuleType(self): # real signature unknown; restored from __doc__
        """ openGLModuleType() -> QOpenGLContext.OpenGLModuleType """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def screen(self): # real signature unknown; restored from __doc__
        """ screen(self) -> QScreen """
        return QScreen

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setFormat(self, QSurfaceFormat): # real signature unknown; restored from __doc__
        """ setFormat(self, QSurfaceFormat) """
        pass

    def setNativeHandle(self, Any): # real signature unknown; restored from __doc__
        """ setNativeHandle(self, Any) """
        pass

    def setScreen(self, QScreen): # real signature unknown; restored from __doc__
        """ setScreen(self, QScreen) """
        pass

    def setShareContext(self, QOpenGLContext): # real signature unknown; restored from __doc__
        """ setShareContext(self, QOpenGLContext) """
        pass

    def shareContext(self): # real signature unknown; restored from __doc__
        """ shareContext(self) -> QOpenGLContext """
        return QOpenGLContext

    def shareGroup(self): # real signature unknown; restored from __doc__
        """ shareGroup(self) -> QOpenGLContextGroup """
        return QOpenGLContextGroup

    def supportsThreadedOpenGL(self): # real signature unknown; restored from __doc__
        """ supportsThreadedOpenGL() -> bool """
        return False

    def surface(self): # real signature unknown; restored from __doc__
        """ surface(self) -> QSurface """
        return QSurface

    def swapBuffers(self, QSurface): # real signature unknown; restored from __doc__
        """ swapBuffers(self, QSurface) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def versionFunctions(self, versionProfile=None): # real signature unknown; restored from __doc__
        """ versionFunctions(self, versionProfile: QOpenGLVersionProfile = None) -> object """
        return object()

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    LibGL = 0
    LibGLES = 1


