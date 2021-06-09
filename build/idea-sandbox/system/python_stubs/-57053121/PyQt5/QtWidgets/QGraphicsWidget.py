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

from .QGraphicsLayoutItem import QGraphicsLayoutItem

class QGraphicsWidget(QGraphicsObject, QGraphicsLayoutItem):
    """ QGraphicsWidget(parent: QGraphicsItem = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()) """
    def actions(self): # real signature unknown; restored from __doc__
        """ actions(self) -> List[QAction] """
        return []

    def addAction(self, QAction): # real signature unknown; restored from __doc__
        """ addAction(self, QAction) """
        pass

    def addActions(self, Iterable, QAction=None): # real signature unknown; restored from __doc__
        """ addActions(self, Iterable[QAction]) """
        pass

    def adjustSize(self): # real signature unknown; restored from __doc__
        """ adjustSize(self) """
        pass

    def autoFillBackground(self): # real signature unknown; restored from __doc__
        """ autoFillBackground(self) -> bool """
        return False

    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> QRectF """
        pass

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ changeEvent(self, QEvent) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) -> bool """
        return False

    def closeEvent(self, QCloseEvent): # real signature unknown; restored from __doc__
        """ closeEvent(self, QCloseEvent) """
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

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
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

    def focusPolicy(self): # real signature unknown; restored from __doc__
        """ focusPolicy(self) -> Qt.FocusPolicy """
        pass

    def focusWidget(self): # real signature unknown; restored from __doc__
        """ focusWidget(self) -> QGraphicsWidget """
        return QGraphicsWidget

    def font(self): # real signature unknown; restored from __doc__
        """ font(self) -> QFont """
        pass

    def geometryChanged(self): # real signature unknown; restored from __doc__
        """ geometryChanged(self) [signal] """
        pass

    def getContentsMargins(self): # real signature unknown; restored from __doc__
        """ getContentsMargins(self) -> Tuple[float, float, float, float] """
        pass

    def getWindowFrameMargins(self): # real signature unknown; restored from __doc__
        """ getWindowFrameMargins(self) -> Tuple[float, float, float, float] """
        pass

    def grabKeyboardEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ grabKeyboardEvent(self, QEvent) """
        pass

    def grabMouseEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ grabMouseEvent(self, QEvent) """
        pass

    def grabShortcut(self, Union, QKeySequence=None, QKeySequence_StandardKey=None, p_str=None, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ grabShortcut(self, Union[QKeySequence, QKeySequence.StandardKey, str, int], context: Qt.ShortcutContext = Qt.WindowShortcut) -> int """
        pass

    def hideEvent(self, QHideEvent): # real signature unknown; restored from __doc__
        """ hideEvent(self, QHideEvent) """
        pass

    def hoverEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def hoverLeaveEvent(self, QGraphicsSceneHoverEvent): # real signature unknown; restored from __doc__
        """ hoverLeaveEvent(self, QGraphicsSceneHoverEvent) """
        pass

    def hoverMoveEvent(self, QGraphicsSceneHoverEvent): # real signature unknown; restored from __doc__
        """ hoverMoveEvent(self, QGraphicsSceneHoverEvent) """
        pass

    def initStyleOption(self, QStyleOption): # real signature unknown; restored from __doc__
        """ initStyleOption(self, QStyleOption) """
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodQuery(self, *args, **kwargs): # real signature unknown
        pass

    def insertAction(self, QAction, QAction_1): # real signature unknown; restored from __doc__
        """ insertAction(self, QAction, QAction) """
        pass

    def insertActions(self, QAction, Iterable, QAction=None): # real signature unknown; restored from __doc__
        """ insertActions(self, QAction, Iterable[QAction]) """
        pass

    def isActiveWindow(self): # real signature unknown; restored from __doc__
        """ isActiveWindow(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def itemChange(self, QGraphicsItem_GraphicsItemChange, Any): # real signature unknown; restored from __doc__
        """ itemChange(self, QGraphicsItem.GraphicsItemChange, Any) -> Any """
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def layout(self): # real signature unknown; restored from __doc__
        """ layout(self) -> QGraphicsLayout """
        return QGraphicsLayout

    def layoutDirection(self): # real signature unknown; restored from __doc__
        """ layoutDirection(self) -> Qt.LayoutDirection """
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def moveEvent(self, QGraphicsSceneMoveEvent): # real signature unknown; restored from __doc__
        """ moveEvent(self, QGraphicsSceneMoveEvent) """
        pass

    def paint(self, QPainter, QStyleOptionGraphicsItem, widget=None): # real signature unknown; restored from __doc__
        """ paint(self, QPainter, QStyleOptionGraphicsItem, widget: QWidget = None) """
        pass

    def paintWindowFrame(self, QPainter, QStyleOptionGraphicsItem, widget=None): # real signature unknown; restored from __doc__
        """ paintWindowFrame(self, QPainter, QStyleOptionGraphicsItem, widget: QWidget = None) """
        pass

    def palette(self): # real signature unknown; restored from __doc__
        """ palette(self) -> QPalette """
        pass

    def polishEvent(self): # real signature unknown; restored from __doc__
        """ polishEvent(self) """
        pass

    def prepareGeometryChange(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def rect(self): # real signature unknown; restored from __doc__
        """ rect(self) -> QRectF """
        pass

    def releaseShortcut(self, p_int): # real signature unknown; restored from __doc__
        """ releaseShortcut(self, int) """
        pass

    def removeAction(self, QAction): # real signature unknown; restored from __doc__
        """ removeAction(self, QAction) """
        pass

    def resize(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        resize(self, QSizeF)
        resize(self, float, float)
        """
        pass

    def resizeEvent(self, QGraphicsSceneResizeEvent): # real signature unknown; restored from __doc__
        """ resizeEvent(self, QGraphicsSceneResizeEvent) """
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

    def setAttribute(self, Qt_WidgetAttribute, on=True): # real signature unknown; restored from __doc__
        """ setAttribute(self, Qt.WidgetAttribute, on: bool = True) """
        pass

    def setAutoFillBackground(self, bool): # real signature unknown; restored from __doc__
        """ setAutoFillBackground(self, bool) """
        pass

    def setContentsMargins(self, p_float, p_float_1, p_float_2, p_float_3): # real signature unknown; restored from __doc__
        """ setContentsMargins(self, float, float, float, float) """
        pass

    def setFocusPolicy(self, Qt_FocusPolicy): # real signature unknown; restored from __doc__
        """ setFocusPolicy(self, Qt.FocusPolicy) """
        pass

    def setFont(self, QFont): # real signature unknown; restored from __doc__
        """ setFont(self, QFont) """
        pass

    def setGeometry(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setGeometry(self, QRectF)
        setGeometry(self, float, float, float, float)
        """
        pass

    def setGraphicsItem(self, *args, **kwargs): # real signature unknown
        pass

    def setLayout(self, QGraphicsLayout): # real signature unknown; restored from __doc__
        """ setLayout(self, QGraphicsLayout) """
        pass

    def setLayoutDirection(self, Qt_LayoutDirection): # real signature unknown; restored from __doc__
        """ setLayoutDirection(self, Qt.LayoutDirection) """
        pass

    def setOwnedByLayout(self, *args, **kwargs): # real signature unknown
        pass

    def setPalette(self, QPalette): # real signature unknown; restored from __doc__
        """ setPalette(self, QPalette) """
        pass

    def setShortcutAutoRepeat(self, p_int, enabled=True): # real signature unknown; restored from __doc__
        """ setShortcutAutoRepeat(self, int, enabled: bool = True) """
        pass

    def setShortcutEnabled(self, p_int, enabled=True): # real signature unknown; restored from __doc__
        """ setShortcutEnabled(self, int, enabled: bool = True) """
        pass

    def setStyle(self, QStyle): # real signature unknown; restored from __doc__
        """ setStyle(self, QStyle) """
        pass

    def setTabOrder(self, QGraphicsWidget, QGraphicsWidget_1): # real signature unknown; restored from __doc__
        """ setTabOrder(QGraphicsWidget, QGraphicsWidget) """
        pass

    def setWindowFlags(self, Union, Qt_WindowFlags=None, Qt_WindowType=None): # real signature unknown; restored from __doc__
        """ setWindowFlags(self, Union[Qt.WindowFlags, Qt.WindowType]) """
        pass

    def setWindowFrameMargins(self, p_float, p_float_1, p_float_2, p_float_3): # real signature unknown; restored from __doc__
        """ setWindowFrameMargins(self, float, float, float, float) """
        pass

    def setWindowTitle(self, p_str): # real signature unknown; restored from __doc__
        """ setWindowTitle(self, str) """
        pass

    def shape(self): # real signature unknown; restored from __doc__
        """ shape(self) -> QPainterPath """
        pass

    def showEvent(self, QShowEvent): # real signature unknown; restored from __doc__
        """ showEvent(self, QShowEvent) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> QSizeF """
        pass

    def sizeHint(self, Qt_SizeHint, constraint=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ sizeHint(self, Qt.SizeHint, constraint: QSizeF = QSizeF()) -> QSizeF """
        pass

    def style(self): # real signature unknown; restored from __doc__
        """ style(self) -> QStyle """
        return QStyle

    def testAttribute(self, Qt_WidgetAttribute): # real signature unknown; restored from __doc__
        """ testAttribute(self, Qt.WidgetAttribute) -> bool """
        return False

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> int """
        return 0

    def ungrabKeyboardEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ ungrabKeyboardEvent(self, QEvent) """
        pass

    def ungrabMouseEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ ungrabMouseEvent(self, QEvent) """
        pass

    def unsetLayoutDirection(self): # real signature unknown; restored from __doc__
        """ unsetLayoutDirection(self) """
        pass

    def unsetWindowFrameMargins(self): # real signature unknown; restored from __doc__
        """ unsetWindowFrameMargins(self) """
        pass

    def updateGeometry(self): # real signature unknown; restored from __doc__
        """ updateGeometry(self) """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def windowFlags(self): # real signature unknown; restored from __doc__
        """ windowFlags(self) -> Qt.WindowFlags """
        pass

    def windowFrameEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ windowFrameEvent(self, QEvent) -> bool """
        return False

    def windowFrameGeometry(self): # real signature unknown; restored from __doc__
        """ windowFrameGeometry(self) -> QRectF """
        pass

    def windowFrameRect(self): # real signature unknown; restored from __doc__
        """ windowFrameRect(self) -> QRectF """
        pass

    def windowFrameSectionAt(self, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ windowFrameSectionAt(self, Union[QPointF, QPoint]) -> Qt.WindowFrameSection """
        pass

    def windowTitle(self): # real signature unknown; restored from __doc__
        """ windowTitle(self) -> str """
        return ""

    def windowType(self): # real signature unknown; restored from __doc__
        """ windowType(self) -> Qt.WindowType """
        pass

    def __init__(self, parent=None, flags, Qt_WindowFlags=None, Qt_WindowType=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


