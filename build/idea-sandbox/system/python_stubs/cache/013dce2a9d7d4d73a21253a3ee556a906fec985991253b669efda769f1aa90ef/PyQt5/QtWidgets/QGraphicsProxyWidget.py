# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QGraphicsWidget import QGraphicsWidget

class QGraphicsProxyWidget(QGraphicsWidget):
    """ QGraphicsProxyWidget(parent: QGraphicsItem = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()) """
    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, QGraphicsSceneContextMenuEvent): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, QGraphicsSceneContextMenuEvent) """
        pass

    def createProxyForChildWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ createProxyForChildWidget(self, QWidget) -> QGraphicsProxyWidget """
        return QGraphicsProxyWidget

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dragEnterEvent(self, QGraphicsSceneDragDropEvent): # real signature unknown; restored from __doc__
        """ dragEnterEvent(self, QGraphicsSceneDragDropEvent) """
        pass

    def dragLeaveEvent(self, QGraphicsSceneDragDropEvent): # real signature unknown; restored from __doc__
        """ dragLeaveEvent(self, QGraphicsSceneDragDropEvent) """
        pass

    def dragMoveEvent(self, QGraphicsSceneDragDropEvent): # real signature unknown; restored from __doc__
        """ dragMoveEvent(self, QGraphicsSceneDragDropEvent) """
        pass

    def dropEvent(self, QGraphicsSceneDragDropEvent): # real signature unknown; restored from __doc__
        """ dropEvent(self, QGraphicsSceneDragDropEvent) """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def eventFilter(self, QObject, QEvent): # real signature unknown; restored from __doc__
        """ eventFilter(self, QObject, QEvent) -> bool """
        return False

    def focusInEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ focusInEvent(self, QFocusEvent) """
        pass

    def focusNextPrevChild(self, bool): # real signature unknown; restored from __doc__
        """ focusNextPrevChild(self, bool) -> bool """
        return False

    def focusOutEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, QFocusEvent) """
        pass

    def grabKeyboardEvent(self, *args, **kwargs): # real signature unknown
        pass

    def grabMouseEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ grabMouseEvent(self, QEvent) """
        pass

    def hideEvent(self, QHideEvent): # real signature unknown; restored from __doc__
        """ hideEvent(self, QHideEvent) """
        pass

    def hoverEnterEvent(self, QGraphicsSceneHoverEvent): # real signature unknown; restored from __doc__
        """ hoverEnterEvent(self, QGraphicsSceneHoverEvent) """
        pass

    def hoverLeaveEvent(self, QGraphicsSceneHoverEvent): # real signature unknown; restored from __doc__
        """ hoverLeaveEvent(self, QGraphicsSceneHoverEvent) """
        pass

    def hoverMoveEvent(self, QGraphicsSceneHoverEvent): # real signature unknown; restored from __doc__
        """ hoverMoveEvent(self, QGraphicsSceneHoverEvent) """
        pass

    def initStyleOption(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, QInputMethodEvent): # real signature unknown; restored from __doc__
        """ inputMethodEvent(self, QInputMethodEvent) """
        pass

    def inputMethodQuery(self, Qt_InputMethodQuery): # real signature unknown; restored from __doc__
        """ inputMethodQuery(self, Qt.InputMethodQuery) -> Any """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def itemChange(self, QGraphicsItem_GraphicsItemChange, Any): # real signature unknown; restored from __doc__
        """ itemChange(self, QGraphicsItem.GraphicsItemChange, Any) -> Any """
        pass

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, QKeyEvent) """
        pass

    def keyReleaseEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, QKeyEvent) """
        pass

    def mouseDoubleClickEvent(self, QGraphicsSceneMouseEvent): # real signature unknown; restored from __doc__
        """ mouseDoubleClickEvent(self, QGraphicsSceneMouseEvent) """
        pass

    def mouseMoveEvent(self, QGraphicsSceneMouseEvent): # real signature unknown; restored from __doc__
        """ mouseMoveEvent(self, QGraphicsSceneMouseEvent) """
        pass

    def mousePressEvent(self, QGraphicsSceneMouseEvent): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, QGraphicsSceneMouseEvent) """
        pass

    def mouseReleaseEvent(self, QGraphicsSceneMouseEvent): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, QGraphicsSceneMouseEvent) """
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def newProxyWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ newProxyWidget(self, QWidget) -> QGraphicsProxyWidget """
        return QGraphicsProxyWidget

    def paint(self, QPainter, QStyleOptionGraphicsItem, QWidget): # real signature unknown; restored from __doc__
        """ paint(self, QPainter, QStyleOptionGraphicsItem, QWidget) """
        pass

    def polishEvent(self, *args, **kwargs): # real signature unknown
        pass

    def prepareGeometryChange(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, QGraphicsSceneResizeEvent): # real signature unknown; restored from __doc__
        """ resizeEvent(self, QGraphicsSceneResizeEvent) """
        pass

    def sceneEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sceneEventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setGeometry(self, QRectF): # real signature unknown; restored from __doc__
        """ setGeometry(self, QRectF) """
        pass

    def setGraphicsItem(self, *args, **kwargs): # real signature unknown
        pass

    def setOwnedByLayout(self, *args, **kwargs): # real signature unknown
        pass

    def setWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ setWidget(self, QWidget) """
        pass

    def showEvent(self, QShowEvent): # real signature unknown; restored from __doc__
        """ showEvent(self, QShowEvent) """
        pass

    def sizeHint(self, Qt_SizeHint, constraint=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ sizeHint(self, Qt.SizeHint, constraint: QSizeF = QSizeF()) -> QSizeF """
        pass

    def subWidgetRect(self, QWidget): # real signature unknown; restored from __doc__
        """ subWidgetRect(self, QWidget) -> QRectF """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> int """
        return 0

    def ungrabKeyboardEvent(self, *args, **kwargs): # real signature unknown
        pass

    def ungrabMouseEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ ungrabMouseEvent(self, QEvent) """
        pass

    def updateGeometry(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, QGraphicsSceneWheelEvent): # real signature unknown; restored from __doc__
        """ wheelEvent(self, QGraphicsSceneWheelEvent) """
        pass

    def widget(self): # real signature unknown; restored from __doc__
        """ widget(self) -> QWidget """
        return QWidget

    def windowFrameEvent(self, *args, **kwargs): # real signature unknown
        pass

    def windowFrameSectionAt(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None, flags, Qt_WindowFlags=None, Qt_WindowType=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


