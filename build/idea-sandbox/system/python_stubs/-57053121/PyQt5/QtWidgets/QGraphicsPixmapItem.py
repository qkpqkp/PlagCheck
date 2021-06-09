# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QGraphicsItem import QGraphicsItem

class QGraphicsPixmapItem(QGraphicsItem):
    """
    QGraphicsPixmapItem(parent: QGraphicsItem = None)
    QGraphicsPixmapItem(QPixmap, parent: QGraphicsItem = None)
    """
    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> QRectF """
        pass

    def contains(self, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ contains(self, Union[QPointF, QPoint]) -> bool """
        return False

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
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

    def isObscuredBy(self, QGraphicsItem): # real signature unknown; restored from __doc__
        """ isObscuredBy(self, QGraphicsItem) -> bool """
        return False

    def itemChange(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def offset(self): # real signature unknown; restored from __doc__
        """ offset(self) -> QPointF """
        pass

    def opaqueArea(self): # real signature unknown; restored from __doc__
        """ opaqueArea(self) -> QPainterPath """
        pass

    def paint(self, QPainter, QStyleOptionGraphicsItem, QWidget): # real signature unknown; restored from __doc__
        """ paint(self, QPainter, QStyleOptionGraphicsItem, QWidget) """
        pass

    def pixmap(self): # real signature unknown; restored from __doc__
        """ pixmap(self) -> QPixmap """
        pass

    def prepareGeometryChange(self, *args, **kwargs): # real signature unknown
        pass

    def sceneEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sceneEventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def setOffset(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setOffset(self, Union[QPointF, QPoint])
        setOffset(self, float, float)
        """
        pass

    def setPixmap(self, QPixmap): # real signature unknown; restored from __doc__
        """ setPixmap(self, QPixmap) """
        pass

    def setShapeMode(self, QGraphicsPixmapItem_ShapeMode): # real signature unknown; restored from __doc__
        """ setShapeMode(self, QGraphicsPixmapItem.ShapeMode) """
        pass

    def setTransformationMode(self, Qt_TransformationMode): # real signature unknown; restored from __doc__
        """ setTransformationMode(self, Qt.TransformationMode) """
        pass

    def shape(self): # real signature unknown; restored from __doc__
        """ shape(self) -> QPainterPath """
        pass

    def shapeMode(self): # real signature unknown; restored from __doc__
        """ shapeMode(self) -> QGraphicsPixmapItem.ShapeMode """
        pass

    def transformationMode(self): # real signature unknown; restored from __doc__
        """ transformationMode(self) -> Qt.TransformationMode """
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

    BoundingRectShape = 1
    HeuristicMaskShape = 2
    MaskShape = 0


