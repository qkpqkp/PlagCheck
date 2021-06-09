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


from .QQuickItem import QQuickItem

class QQuickPaintedItem(QQuickItem):
    """ QQuickPaintedItem(parent: QQuickItem = None) """
    def antialiasing(self): # real signature unknown; restored from __doc__
        """ antialiasing(self) -> bool """
        return False

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childMouseEventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def classBegin(self, *args, **kwargs): # real signature unknown
        pass

    def componentComplete(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contentsBoundingRect(self): # real signature unknown; restored from __doc__
        """ contentsBoundingRect(self) -> QRectF """
        pass

    def contentsScale(self): # real signature unknown; restored from __doc__
        """ contentsScale(self) -> float """
        return 0.0

    def contentsScaleChanged(self): # real signature unknown; restored from __doc__
        """ contentsScaleChanged(self) [signal] """
        pass

    def contentsSize(self): # real signature unknown; restored from __doc__
        """ contentsSize(self) -> QSize """
        pass

    def contentsSizeChanged(self): # real signature unknown; restored from __doc__
        """ contentsSizeChanged(self) [signal] """
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

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def fillColor(self): # real signature unknown; restored from __doc__
        """ fillColor(self) -> QColor """
        pass

    def fillColorChanged(self): # real signature unknown; restored from __doc__
        """ fillColorChanged(self) [signal] """
        pass

    def focusInEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, *args, **kwargs): # real signature unknown
        pass

    def geometryChanged(self, *args, **kwargs): # real signature unknown
        pass

    def heightValid(self, *args, **kwargs): # real signature unknown
        pass

    def hoverEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def hoverLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def hoverMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isComponentComplete(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isTextureProvider(self): # real signature unknown; restored from __doc__
        """ isTextureProvider(self) -> bool """
        return False

    def itemChange(self, QQuickItem_ItemChange, QQuickItem_ItemChangeData): # real signature unknown; restored from __doc__
        """ itemChange(self, QQuickItem.ItemChange, QQuickItem.ItemChangeData) """
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mipmap(self): # real signature unknown; restored from __doc__
        """ mipmap(self) -> bool """
        return False

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseUngrabEvent(self, *args, **kwargs): # real signature unknown
        pass

    def opaquePainting(self): # real signature unknown; restored from __doc__
        """ opaquePainting(self) -> bool """
        return False

    def paint(self, QPainter): # real signature unknown; restored from __doc__
        """ paint(self, QPainter) """
        pass

    def performanceHints(self): # real signature unknown; restored from __doc__
        """ performanceHints(self) -> QQuickPaintedItem.PerformanceHints """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def releaseResources(self): # real signature unknown; restored from __doc__
        """ releaseResources(self) """
        pass

    def renderTarget(self): # real signature unknown; restored from __doc__
        """ renderTarget(self) -> QQuickPaintedItem.RenderTarget """
        pass

    def renderTargetChanged(self): # real signature unknown; restored from __doc__
        """ renderTargetChanged(self) [signal] """
        pass

    def resetContentsSize(self): # real signature unknown; restored from __doc__
        """ resetContentsSize(self) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAntialiasing(self, bool): # real signature unknown; restored from __doc__
        """ setAntialiasing(self, bool) """
        pass

    def setContentsScale(self, p_float): # real signature unknown; restored from __doc__
        """ setContentsScale(self, float) """
        pass

    def setContentsSize(self, QSize): # real signature unknown; restored from __doc__
        """ setContentsSize(self, QSize) """
        pass

    def setFillColor(self, Union, QColor=None, Qt_GlobalColor=None): # real signature unknown; restored from __doc__
        """ setFillColor(self, Union[QColor, Qt.GlobalColor]) """
        pass

    def setMipmap(self, bool): # real signature unknown; restored from __doc__
        """ setMipmap(self, bool) """
        pass

    def setOpaquePainting(self, bool): # real signature unknown; restored from __doc__
        """ setOpaquePainting(self, bool) """
        pass

    def setPerformanceHint(self, QQuickPaintedItem_PerformanceHint, enabled=True): # real signature unknown; restored from __doc__
        """ setPerformanceHint(self, QQuickPaintedItem.PerformanceHint, enabled: bool = True) """
        pass

    def setPerformanceHints(self, Union, QQuickPaintedItem_PerformanceHints=None, QQuickPaintedItem_PerformanceHint=None): # real signature unknown; restored from __doc__
        """ setPerformanceHints(self, Union[QQuickPaintedItem.PerformanceHints, QQuickPaintedItem.PerformanceHint]) """
        pass

    def setRenderTarget(self, QQuickPaintedItem_RenderTarget): # real signature unknown; restored from __doc__
        """ setRenderTarget(self, QQuickPaintedItem.RenderTarget) """
        pass

    def setTextureSize(self, QSize): # real signature unknown; restored from __doc__
        """ setTextureSize(self, QSize) """
        pass

    def textureProvider(self): # real signature unknown; restored from __doc__
        """ textureProvider(self) -> QSGTextureProvider """
        return QSGTextureProvider

    def textureSize(self): # real signature unknown; restored from __doc__
        """ textureSize(self) -> QSize """
        pass

    def textureSizeChanged(self): # real signature unknown; restored from __doc__
        """ textureSizeChanged(self) [signal] """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def touchEvent(self, *args, **kwargs): # real signature unknown
        pass

    def touchUngrabEvent(self, *args, **kwargs): # real signature unknown
        pass

    def update(self, rect=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ update(self, rect: QRect = QRect()) """
        pass

    def updateInputMethod(self, *args, **kwargs): # real signature unknown
        pass

    def updatePaintNode(self, QSGNode, QQuickItem_UpdatePaintNodeData): # real signature unknown; restored from __doc__
        """ updatePaintNode(self, QSGNode, QQuickItem.UpdatePaintNodeData) -> QSGNode """
        return QSGNode

    def updatePolish(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def widthValid(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    FastFBOResizing = 1
    FramebufferObject = 1
    Image = 0
    InvertedYFramebufferObject = 2


