# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QWidget import QWidget

class QOpenGLWidget(QWidget):
    """ QOpenGLWidget(parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()) """
    def aboutToCompose(self): # real signature unknown; restored from __doc__
        """ aboutToCompose(self) [signal] """
        pass

    def aboutToResize(self): # real signature unknown; restored from __doc__
        """ aboutToResize(self) [signal] """
        pass

    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def context(self): # real signature unknown; restored from __doc__
        """ context(self) -> QOpenGLContext """
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultFramebufferObject(self): # real signature unknown; restored from __doc__
        """ defaultFramebufferObject(self) -> int """
        return 0

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def doneCurrent(self): # real signature unknown; restored from __doc__
        """ doneCurrent(self) """
        pass

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def focusInEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> QSurfaceFormat """
        pass

    def frameSwapped(self): # real signature unknown; restored from __doc__
        """ frameSwapped(self) [signal] """
        pass

    def grabFramebuffer(self): # real signature unknown; restored from __doc__
        """ grabFramebuffer(self) -> QImage """
        pass

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def initializeGL(self): # real signature unknown; restored from __doc__
        """ initializeGL(self) """
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
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

    def leaveEvent(self, *args, **kwargs): # real signature unknown
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

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ paintEngine(self) -> QPaintEngine """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ paintEvent(self, QPaintEvent) """
        pass

    def paintGL(self): # real signature unknown; restored from __doc__
        """ paintGL(self) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resized(self): # real signature unknown; restored from __doc__
        """ resized(self) [signal] """
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

    def setFormat(self, QSurfaceFormat): # real signature unknown; restored from __doc__
        """ setFormat(self, QSurfaceFormat) """
        pass

    def setTextureFormat(self, p_int): # real signature unknown; restored from __doc__
        """ setTextureFormat(self, int) """
        pass

    def setUpdateBehavior(self, QOpenGLWidget_UpdateBehavior): # real signature unknown; restored from __doc__
        """ setUpdateBehavior(self, QOpenGLWidget.UpdateBehavior) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def textureFormat(self): # real signature unknown; restored from __doc__
        """ textureFormat(self) -> int """
        return 0

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateBehavior(self): # real signature unknown; restored from __doc__
        """ updateBehavior(self) -> QOpenGLWidget.UpdateBehavior """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None, flags, Qt_WindowFlags=None, Qt_WindowType=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    NoPartialUpdate = 0
    PartialUpdate = 1


