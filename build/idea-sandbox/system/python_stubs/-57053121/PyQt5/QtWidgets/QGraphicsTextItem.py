# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QGraphicsObject import QGraphicsObject

class QGraphicsTextItem(QGraphicsObject):
    """
    QGraphicsTextItem(parent: QGraphicsItem = None)
    QGraphicsTextItem(str, parent: QGraphicsItem = None)
    """
    def adjustSize(self): # real signature unknown; restored from __doc__
        """ adjustSize(self) """
        pass

    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> QRectF """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contains(self, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ contains(self, Union[QPointF, QPoint]) -> bool """
        return False

    def contextMenuEvent(self, QGraphicsSceneContextMenuEvent): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, QGraphicsSceneContextMenuEvent) """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultTextColor(self): # real signature unknown; restored from __doc__
        """ defaultTextColor(self) -> QColor """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def document(self): # real signature unknown; restored from __doc__
        """ document(self) -> QTextDocument """
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

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def focusInEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ focusInEvent(self, QFocusEvent) """
        pass

    def focusOutEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, QFocusEvent) """
        pass

    def font(self): # real signature unknown; restored from __doc__
        """ font(self) -> QFont """
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

    def inputMethodEvent(self, QInputMethodEvent): # real signature unknown; restored from __doc__
        """ inputMethodEvent(self, QInputMethodEvent) """
        pass

    def inputMethodQuery(self, Qt_InputMethodQuery): # real signature unknown; restored from __doc__
        """ inputMethodQuery(self, Qt.InputMethodQuery) -> Any """
        pass

    def isObscuredBy(self, QGraphicsItem): # real signature unknown; restored from __doc__
        """ isObscuredBy(self, QGraphicsItem) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def itemChange(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, QKeyEvent) """
        pass

    def keyReleaseEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, QKeyEvent) """
        pass

    def linkActivated(self, p_str): # real signature unknown; restored from __doc__
        """ linkActivated(self, str) [signal] """
        pass

    def linkHovered(self, p_str): # real signature unknown; restored from __doc__
        """ linkHovered(self, str) [signal] """
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

    def opaqueArea(self): # real signature unknown; restored from __doc__
        """ opaqueArea(self) -> QPainterPath """
        pass

    def openExternalLinks(self): # real signature unknown; restored from __doc__
        """ openExternalLinks(self) -> bool """
        return False

    def paint(self, QPainter, QStyleOptionGraphicsItem, QWidget): # real signature unknown; restored from __doc__
        """ paint(self, QPainter, QStyleOptionGraphicsItem, QWidget) """
        pass

    def prepareGeometryChange(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sceneEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ sceneEvent(self, QEvent) -> bool """
        return False

    def sceneEventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setDefaultTextColor(self, Union, QColor=None, Qt_GlobalColor=None, QGradient=None): # real signature unknown; restored from __doc__
        """ setDefaultTextColor(self, Union[QColor, Qt.GlobalColor, QGradient]) """
        pass

    def setDocument(self, QTextDocument): # real signature unknown; restored from __doc__
        """ setDocument(self, QTextDocument) """
        pass

    def setFont(self, QFont): # real signature unknown; restored from __doc__
        """ setFont(self, QFont) """
        pass

    def setHtml(self, p_str): # real signature unknown; restored from __doc__
        """ setHtml(self, str) """
        pass

    def setOpenExternalLinks(self, bool): # real signature unknown; restored from __doc__
        """ setOpenExternalLinks(self, bool) """
        pass

    def setPlainText(self, p_str): # real signature unknown; restored from __doc__
        """ setPlainText(self, str) """
        pass

    def setTabChangesFocus(self, bool): # real signature unknown; restored from __doc__
        """ setTabChangesFocus(self, bool) """
        pass

    def setTextCursor(self, QTextCursor): # real signature unknown; restored from __doc__
        """ setTextCursor(self, QTextCursor) """
        pass

    def setTextInteractionFlags(self, Union, Qt_TextInteractionFlags=None, Qt_TextInteractionFlag=None): # real signature unknown; restored from __doc__
        """ setTextInteractionFlags(self, Union[Qt.TextInteractionFlags, Qt.TextInteractionFlag]) """
        pass

    def setTextWidth(self, p_float): # real signature unknown; restored from __doc__
        """ setTextWidth(self, float) """
        pass

    def shape(self): # real signature unknown; restored from __doc__
        """ shape(self) -> QPainterPath """
        pass

    def tabChangesFocus(self): # real signature unknown; restored from __doc__
        """ tabChangesFocus(self) -> bool """
        return False

    def textCursor(self): # real signature unknown; restored from __doc__
        """ textCursor(self) -> QTextCursor """
        pass

    def textInteractionFlags(self): # real signature unknown; restored from __doc__
        """ textInteractionFlags(self) -> Qt.TextInteractionFlags """
        pass

    def textWidth(self): # real signature unknown; restored from __doc__
        """ textWidth(self) -> float """
        return 0.0

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def toHtml(self): # real signature unknown; restored from __doc__
        """ toHtml(self) -> str """
        return ""

    def toPlainText(self): # real signature unknown; restored from __doc__
        """ toPlainText(self) -> str """
        return ""

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> int """
        return 0

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


