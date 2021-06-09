# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QPaintDeviceWindow import QPaintDeviceWindow

class QOpenGLWindow(QPaintDeviceWindow):
    """
    QOpenGLWindow(updateBehavior: QOpenGLWindow.UpdateBehavior = QOpenGLWindow.NoPartialUpdate, parent: QWindow = None)
    QOpenGLWindow(QOpenGLContext, updateBehavior: QOpenGLWindow.UpdateBehavior = QOpenGLWindow.NoPartialUpdate, parent: QWindow = None)
    """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def context(self): # real signature unknown; restored from __doc__
        """ context(self) -> QOpenGLContext """
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

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def exposeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusInEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, *args, **kwargs): # real signature unknown
        pass

    def frameSwapped(self): # real signature unknown; restored from __doc__
        """ frameSwapped(self) [signal] """
        pass

    def grabFramebuffer(self): # real signature unknown; restored from __doc__
        """ grabFramebuffer(self) -> QImage """
        return QImage

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def initializeGL(self): # real signature unknown; restored from __doc__
        """ initializeGL(self) """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def makeCurrent(self): # real signature unknown; restored from __doc__
        """ makeCurrent(self) """
        pass

    def metric(self, QPaintDevice_PaintDeviceMetric): # real signature unknown; restored from __doc__
        """ metric(self, QPaintDevice.PaintDeviceMetric) -> int """
        return 0

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ paintEvent(self, QPaintEvent) """
        pass

    def paintGL(self): # real signature unknown; restored from __doc__
        """ paintGL(self) """
        pass

    def paintOverGL(self): # real signature unknown; restored from __doc__
        """ paintOverGL(self) """
        pass

    def paintUnderGL(self): # real signature unknown; restored from __doc__
        """ paintUnderGL(self) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ resizeEvent(self, QResizeEvent) """
        pass

    def resizeGL(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ resizeGL(self, int, int) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def shareContext(self): # real signature unknown; restored from __doc__
        """ shareContext(self) -> QOpenGLContext """
        return QOpenGLContext

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def touchEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateBehavior(self): # real signature unknown; restored from __doc__
        """ updateBehavior(self) -> QOpenGLWindow.UpdateBehavior """
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    NoPartialUpdate = 0
    PartialUpdateBlend = 2
    PartialUpdateBlit = 1


