# encoding: utf-8
# module PyQt5.QtSvg
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtSvg.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import PyQt5.QtWidgets as __PyQt5_QtWidgets


# no functions
# classes

class QGraphicsSvgItem(__PyQt5_QtWidgets.QGraphicsObject):
    """
    QGraphicsSvgItem(parent: QGraphicsItem = None)
    QGraphicsSvgItem(str, parent: QGraphicsItem = None)
    """
    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> QRectF """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def elementId(self): # real signature unknown; restored from __doc__
        """ elementId(self) -> str """
        return ""

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def focusInEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, *args, **kwargs): # real signature unknown
        pass

    def hoverEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def hoverLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def hoverMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodQuery(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def itemChange(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def maximumCacheSize(self): # real signature unknown; restored from __doc__
        """ maximumCacheSize(self) -> QSize """
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def paint(self, QPainter, QStyleOptionGraphicsItem, widget=None): # real signature unknown; restored from __doc__
        """ paint(self, QPainter, QStyleOptionGraphicsItem, widget: QWidget = None) """
        pass

    def prepareGeometryChange(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def renderer(self): # real signature unknown; restored from __doc__
        """ renderer(self) -> QSvgRenderer """
        return QSvgRenderer

    def sceneEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sceneEventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setElementId(self, p_str): # real signature unknown; restored from __doc__
        """ setElementId(self, str) """
        pass

    def setMaximumCacheSize(self, QSize): # real signature unknown; restored from __doc__
        """ setMaximumCacheSize(self, QSize) """
        pass

    def setSharedRenderer(self, QSvgRenderer): # real signature unknown; restored from __doc__
        """ setSharedRenderer(self, QSvgRenderer) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> int """
        return 0

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


class QSvgGenerator(__PyQt5_QtGui.QPaintDevice):
    """ QSvgGenerator() """
    def description(self): # real signature unknown; restored from __doc__
        """ description(self) -> str """
        return ""

    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def metric(self, QPaintDevice_PaintDeviceMetric): # real signature unknown; restored from __doc__
        """ metric(self, QPaintDevice.PaintDeviceMetric) -> int """
        return 0

    def outputDevice(self): # real signature unknown; restored from __doc__
        """ outputDevice(self) -> QIODevice """
        pass

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ paintEngine(self) -> QPaintEngine """
        pass

    def resolution(self): # real signature unknown; restored from __doc__
        """ resolution(self) -> int """
        return 0

    def setDescription(self, p_str): # real signature unknown; restored from __doc__
        """ setDescription(self, str) """
        pass

    def setFileName(self, p_str): # real signature unknown; restored from __doc__
        """ setFileName(self, str) """
        pass

    def setOutputDevice(self, QIODevice): # real signature unknown; restored from __doc__
        """ setOutputDevice(self, QIODevice) """
        pass

    def setResolution(self, p_int): # real signature unknown; restored from __doc__
        """ setResolution(self, int) """
        pass

    def setSize(self, QSize): # real signature unknown; restored from __doc__
        """ setSize(self, QSize) """
        pass

    def setTitle(self, p_str): # real signature unknown; restored from __doc__
        """ setTitle(self, str) """
        pass

    def setViewBox(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setViewBox(self, QRect)
        setViewBox(self, QRectF)
        """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> QSize """
        pass

    def title(self): # real signature unknown; restored from __doc__
        """ title(self) -> str """
        return ""

    def viewBox(self): # real signature unknown; restored from __doc__
        """ viewBox(self) -> QRect """
        pass

    def viewBoxF(self): # real signature unknown; restored from __doc__
        """ viewBoxF(self) -> QRectF """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass


class QSvgRenderer(__PyQt5_QtCore.QObject):
    """
    QSvgRenderer(parent: QObject = None)
    QSvgRenderer(str, parent: QObject = None)
    QSvgRenderer(Union[QByteArray, bytes, bytearray], parent: QObject = None)
    QSvgRenderer(QXmlStreamReader, parent: QObject = None)
    """
    def animated(self): # real signature unknown; restored from __doc__
        """ animated(self) -> bool """
        return False

    def animationDuration(self): # real signature unknown; restored from __doc__
        """ animationDuration(self) -> int """
        return 0

    def boundsOnElement(self, p_str): # real signature unknown; restored from __doc__
        """ boundsOnElement(self, str) -> QRectF """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def currentFrame(self): # real signature unknown; restored from __doc__
        """ currentFrame(self) -> int """
        return 0

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultSize(self): # real signature unknown; restored from __doc__
        """ defaultSize(self) -> QSize """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def elementExists(self, p_str): # real signature unknown; restored from __doc__
        """ elementExists(self, str) -> bool """
        return False

    def framesPerSecond(self): # real signature unknown; restored from __doc__
        """ framesPerSecond(self) -> int """
        return 0

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def load(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        load(self, str) -> bool
        load(self, Union[QByteArray, bytes, bytearray]) -> bool
        load(self, QXmlStreamReader) -> bool
        """
        return False

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def render(self, QPainter, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        render(self, QPainter)
        render(self, QPainter, QRectF)
        render(self, QPainter, str, bounds: QRectF = QRectF())
        """
        pass

    def repaintNeeded(self): # real signature unknown; restored from __doc__
        """ repaintNeeded(self) [signal] """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCurrentFrame(self, p_int): # real signature unknown; restored from __doc__
        """ setCurrentFrame(self, int) """
        pass

    def setFramesPerSecond(self, p_int): # real signature unknown; restored from __doc__
        """ setFramesPerSecond(self, int) """
        pass

    def setViewBox(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setViewBox(self, QRect)
        setViewBox(self, QRectF)
        """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def viewBox(self): # real signature unknown; restored from __doc__
        """ viewBox(self) -> QRect """
        pass

    def viewBoxF(self): # real signature unknown; restored from __doc__
        """ viewBoxF(self) -> QRectF """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


class QSvgWidget(__PyQt5_QtWidgets.QWidget):
    """
    QSvgWidget(parent: QWidget = None)
    QSvgWidget(str, parent: QWidget = None)
    """
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

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
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

    def event(self, *args, **kwargs): # real signature unknown
        pass

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

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def load(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        load(self, str)
        load(self, Union[QByteArray, bytes, bytearray])
        """
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

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

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ paintEvent(self, QPaintEvent) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def renderer(self): # real signature unknown; restored from __doc__
        """ renderer(self) -> QSvgRenderer """
        return QSvgRenderer

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


# variables with complex values



