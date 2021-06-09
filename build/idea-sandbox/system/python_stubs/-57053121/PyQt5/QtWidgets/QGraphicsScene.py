# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QGraphicsScene(__PyQt5_QtCore.QObject):
    """
    QGraphicsScene(parent: QObject = None)
    QGraphicsScene(QRectF, parent: QObject = None)
    QGraphicsScene(float, float, float, float, parent: QObject = None)
    """
    def activePanel(self): # real signature unknown; restored from __doc__
        """ activePanel(self) -> QGraphicsItem """
        return QGraphicsItem

    def activeWindow(self): # real signature unknown; restored from __doc__
        """ activeWindow(self) -> QGraphicsWidget """
        return QGraphicsWidget

    def addEllipse(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addEllipse(self, QRectF, pen: Union[QPen, QColor, Qt.GlobalColor, QGradient] = QPen(), brush: Union[QBrush, QColor, Qt.GlobalColor, QGradient] = QBrush()) -> QGraphicsEllipseItem
        addEllipse(self, float, float, float, float, pen: Union[QPen, QColor, Qt.GlobalColor, QGradient] = QPen(), brush: Union[QBrush, QColor, Qt.GlobalColor, QGradient] = QBrush()) -> QGraphicsEllipseItem
        """
        pass

    def addItem(self, QGraphicsItem): # real signature unknown; restored from __doc__
        """ addItem(self, QGraphicsItem) """
        pass

    def addLine(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addLine(self, QLineF, pen: Union[QPen, QColor, Qt.GlobalColor, QGradient] = QPen()) -> QGraphicsLineItem
        addLine(self, float, float, float, float, pen: Union[QPen, QColor, Qt.GlobalColor, QGradient] = QPen()) -> QGraphicsLineItem
        """
        pass

    def addPath(self, QPainterPath, pen, QPen=None, QColor=None, Qt_GlobalColor=None, QGradient=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ addPath(self, QPainterPath, pen: Union[QPen, QColor, Qt.GlobalColor, QGradient] = QPen(), brush: Union[QBrush, QColor, Qt.GlobalColor, QGradient] = QBrush()) -> QGraphicsPathItem """
        pass

    def addPixmap(self, QPixmap): # real signature unknown; restored from __doc__
        """ addPixmap(self, QPixmap) -> QGraphicsPixmapItem """
        return QGraphicsPixmapItem

    def addPolygon(self, QPolygonF, pen, QPen=None, QColor=None, Qt_GlobalColor=None, QGradient=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ addPolygon(self, QPolygonF, pen: Union[QPen, QColor, Qt.GlobalColor, QGradient] = QPen(), brush: Union[QBrush, QColor, Qt.GlobalColor, QGradient] = QBrush()) -> QGraphicsPolygonItem """
        pass

    def addRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addRect(self, QRectF, pen: Union[QPen, QColor, Qt.GlobalColor, QGradient] = QPen(), brush: Union[QBrush, QColor, Qt.GlobalColor, QGradient] = QBrush()) -> QGraphicsRectItem
        addRect(self, float, float, float, float, pen: Union[QPen, QColor, Qt.GlobalColor, QGradient] = QPen(), brush: Union[QBrush, QColor, Qt.GlobalColor, QGradient] = QBrush()) -> QGraphicsRectItem
        """
        pass

    def addSimpleText(self, p_str, font=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ addSimpleText(self, str, font: QFont = QFont()) -> QGraphicsSimpleTextItem """
        pass

    def addText(self, p_str, font=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ addText(self, str, font: QFont = QFont()) -> QGraphicsTextItem """
        pass

    def addWidget(self, QWidget, flags, Qt_WindowFlags=None, Qt_WindowType=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ addWidget(self, QWidget, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()) -> QGraphicsProxyWidget """
        pass

    def advance(self): # real signature unknown; restored from __doc__
        """ advance(self) """
        pass

    def backgroundBrush(self): # real signature unknown; restored from __doc__
        """ backgroundBrush(self) -> QBrush """
        pass

    def bspTreeDepth(self): # real signature unknown; restored from __doc__
        """ bspTreeDepth(self) -> int """
        return 0

    def changed(self, Iterable, QRectF=None): # real signature unknown; restored from __doc__
        """ changed(self, Iterable[QRectF]) [signal] """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def clearFocus(self): # real signature unknown; restored from __doc__
        """ clearFocus(self) """
        pass

    def clearSelection(self): # real signature unknown; restored from __doc__
        """ clearSelection(self) """
        pass

    def collidingItems(self, QGraphicsItem, mode=None): # real signature unknown; restored from __doc__
        """ collidingItems(self, QGraphicsItem, mode: Qt.ItemSelectionMode = Qt.IntersectsItemShape) -> List[QGraphicsItem] """
        return []

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, QGraphicsSceneContextMenuEvent): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, QGraphicsSceneContextMenuEvent) """
        pass

    def createItemGroup(self, Iterable, QGraphicsItem=None): # real signature unknown; restored from __doc__
        """ createItemGroup(self, Iterable[QGraphicsItem]) -> QGraphicsItemGroup """
        return QGraphicsItemGroup

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def destroyItemGroup(self, QGraphicsItemGroup): # real signature unknown; restored from __doc__
        """ destroyItemGroup(self, QGraphicsItemGroup) """
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

    def drawBackground(self, QPainter, QRectF): # real signature unknown; restored from __doc__
        """ drawBackground(self, QPainter, QRectF) """
        pass

    def drawForeground(self, QPainter, QRectF): # real signature unknown; restored from __doc__
        """ drawForeground(self, QPainter, QRectF) """
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

    def focusItem(self): # real signature unknown; restored from __doc__
        """ focusItem(self) -> QGraphicsItem """
        return QGraphicsItem

    def focusItemChanged(self, QGraphicsItem, QGraphicsItem_1, Qt_FocusReason): # real signature unknown; restored from __doc__
        """ focusItemChanged(self, QGraphicsItem, QGraphicsItem, Qt.FocusReason) [signal] """
        pass

    def focusNextPrevChild(self, bool): # real signature unknown; restored from __doc__
        """ focusNextPrevChild(self, bool) -> bool """
        return False

    def focusOnTouch(self): # real signature unknown; restored from __doc__
        """ focusOnTouch(self) -> bool """
        return False

    def focusOutEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, QFocusEvent) """
        pass

    def font(self): # real signature unknown; restored from __doc__
        """ font(self) -> QFont """
        pass

    def foregroundBrush(self): # real signature unknown; restored from __doc__
        """ foregroundBrush(self) -> QBrush """
        pass

    def hasFocus(self): # real signature unknown; restored from __doc__
        """ hasFocus(self) -> bool """
        return False

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> float """
        return 0.0

    def helpEvent(self, QGraphicsSceneHelpEvent): # real signature unknown; restored from __doc__
        """ helpEvent(self, QGraphicsSceneHelpEvent) """
        pass

    def inputMethodEvent(self, QInputMethodEvent): # real signature unknown; restored from __doc__
        """ inputMethodEvent(self, QInputMethodEvent) """
        pass

    def inputMethodQuery(self, Qt_InputMethodQuery): # real signature unknown; restored from __doc__
        """ inputMethodQuery(self, Qt.InputMethodQuery) -> Any """
        pass

    def invalidate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        invalidate(self, rect: QRectF = QRectF(), layers: Union[QGraphicsScene.SceneLayers, QGraphicsScene.SceneLayer] = QGraphicsScene.AllLayers)
        invalidate(self, float, float, float, float, layers: Union[QGraphicsScene.SceneLayers, QGraphicsScene.SceneLayer] = QGraphicsScene.AllLayers)
        """
        pass

    def isActive(self): # real signature unknown; restored from __doc__
        """ isActive(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def itemAt(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        itemAt(self, Union[QPointF, QPoint], QTransform) -> QGraphicsItem
        itemAt(self, float, float, QTransform) -> QGraphicsItem
        """
        return QGraphicsItem

    def itemIndexMethod(self): # real signature unknown; restored from __doc__
        """ itemIndexMethod(self) -> QGraphicsScene.ItemIndexMethod """
        pass

    def items(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        items(self, order: Qt.SortOrder = Qt.DescendingOrder) -> List[QGraphicsItem]
        items(self, Union[QPointF, QPoint], mode: Qt.ItemSelectionMode = Qt.IntersectsItemShape, order: Qt.SortOrder = Qt.DescendingOrder, deviceTransform: QTransform = QTransform()) -> List[QGraphicsItem]
        items(self, QRectF, mode: Qt.ItemSelectionMode = Qt.IntersectsItemShape, order: Qt.SortOrder = Qt.DescendingOrder, deviceTransform: QTransform = QTransform()) -> List[QGraphicsItem]
        items(self, QPolygonF, mode: Qt.ItemSelectionMode = Qt.IntersectsItemShape, order: Qt.SortOrder = Qt.DescendingOrder, deviceTransform: QTransform = QTransform()) -> List[QGraphicsItem]
        items(self, QPainterPath, mode: Qt.ItemSelectionMode = Qt.IntersectsItemShape, order: Qt.SortOrder = Qt.DescendingOrder, deviceTransform: QTransform = QTransform()) -> List[QGraphicsItem]
        items(self, float, float, float, float, Qt.ItemSelectionMode, Qt.SortOrder, deviceTransform: QTransform = QTransform()) -> List[QGraphicsItem]
        """
        return []

    def itemsBoundingRect(self): # real signature unknown; restored from __doc__
        """ itemsBoundingRect(self) -> QRectF """
        pass

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, QKeyEvent) """
        pass

    def keyReleaseEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, QKeyEvent) """
        pass

    def minimumRenderSize(self): # real signature unknown; restored from __doc__
        """ minimumRenderSize(self) -> float """
        return 0.0

    def mouseDoubleClickEvent(self, QGraphicsSceneMouseEvent): # real signature unknown; restored from __doc__
        """ mouseDoubleClickEvent(self, QGraphicsSceneMouseEvent) """
        pass

    def mouseGrabberItem(self): # real signature unknown; restored from __doc__
        """ mouseGrabberItem(self) -> QGraphicsItem """
        return QGraphicsItem

    def mouseMoveEvent(self, QGraphicsSceneMouseEvent): # real signature unknown; restored from __doc__
        """ mouseMoveEvent(self, QGraphicsSceneMouseEvent) """
        pass

    def mousePressEvent(self, QGraphicsSceneMouseEvent): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, QGraphicsSceneMouseEvent) """
        pass

    def mouseReleaseEvent(self, QGraphicsSceneMouseEvent): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, QGraphicsSceneMouseEvent) """
        pass

    def palette(self): # real signature unknown; restored from __doc__
        """ palette(self) -> QPalette """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeItem(self, QGraphicsItem): # real signature unknown; restored from __doc__
        """ removeItem(self, QGraphicsItem) """
        pass

    def render(self, QPainter, target=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ render(self, QPainter, target: QRectF = QRectF(), source: QRectF = QRectF(), mode: Qt.AspectRatioMode = Qt.KeepAspectRatio) """
        pass

    def sceneRect(self): # real signature unknown; restored from __doc__
        """ sceneRect(self) -> QRectF """
        pass

    def sceneRectChanged(self, QRectF): # real signature unknown; restored from __doc__
        """ sceneRectChanged(self, QRectF) [signal] """
        pass

    def selectedItems(self): # real signature unknown; restored from __doc__
        """ selectedItems(self) -> List[QGraphicsItem] """
        return []

    def selectionArea(self): # real signature unknown; restored from __doc__
        """ selectionArea(self) -> QPainterPath """
        pass

    def selectionChanged(self): # real signature unknown; restored from __doc__
        """ selectionChanged(self) [signal] """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def sendEvent(self, QGraphicsItem, QEvent): # real signature unknown; restored from __doc__
        """ sendEvent(self, QGraphicsItem, QEvent) -> bool """
        return False

    def setActivePanel(self, QGraphicsItem): # real signature unknown; restored from __doc__
        """ setActivePanel(self, QGraphicsItem) """
        pass

    def setActiveWindow(self, QGraphicsWidget): # real signature unknown; restored from __doc__
        """ setActiveWindow(self, QGraphicsWidget) """
        pass

    def setBackgroundBrush(self, Union, QBrush=None, QColor=None, Qt_GlobalColor=None, QGradient=None): # real signature unknown; restored from __doc__
        """ setBackgroundBrush(self, Union[QBrush, QColor, Qt.GlobalColor, QGradient]) """
        pass

    def setBspTreeDepth(self, p_int): # real signature unknown; restored from __doc__
        """ setBspTreeDepth(self, int) """
        pass

    def setFocus(self, focusReason=None): # real signature unknown; restored from __doc__
        """ setFocus(self, focusReason: Qt.FocusReason = Qt.OtherFocusReason) """
        pass

    def setFocusItem(self, QGraphicsItem, focusReason=None): # real signature unknown; restored from __doc__
        """ setFocusItem(self, QGraphicsItem, focusReason: Qt.FocusReason = Qt.OtherFocusReason) """
        pass

    def setFocusOnTouch(self, bool): # real signature unknown; restored from __doc__
        """ setFocusOnTouch(self, bool) """
        pass

    def setFont(self, QFont): # real signature unknown; restored from __doc__
        """ setFont(self, QFont) """
        pass

    def setForegroundBrush(self, Union, QBrush=None, QColor=None, Qt_GlobalColor=None, QGradient=None): # real signature unknown; restored from __doc__
        """ setForegroundBrush(self, Union[QBrush, QColor, Qt.GlobalColor, QGradient]) """
        pass

    def setItemIndexMethod(self, QGraphicsScene_ItemIndexMethod): # real signature unknown; restored from __doc__
        """ setItemIndexMethod(self, QGraphicsScene.ItemIndexMethod) """
        pass

    def setMinimumRenderSize(self, p_float): # real signature unknown; restored from __doc__
        """ setMinimumRenderSize(self, float) """
        pass

    def setPalette(self, QPalette): # real signature unknown; restored from __doc__
        """ setPalette(self, QPalette) """
        pass

    def setSceneRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setSceneRect(self, QRectF)
        setSceneRect(self, float, float, float, float)
        """
        pass

    def setSelectionArea(self, QPainterPath, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setSelectionArea(self, QPainterPath, QTransform)
        setSelectionArea(self, QPainterPath, mode: Qt.ItemSelectionMode = Qt.IntersectsItemShape, deviceTransform: QTransform = QTransform())
        setSelectionArea(self, QPainterPath, Qt.ItemSelectionOperation, mode: Qt.ItemSelectionMode = Qt.IntersectsItemShape, deviceTransform: QTransform = QTransform())
        """
        pass

    def setStickyFocus(self, bool): # real signature unknown; restored from __doc__
        """ setStickyFocus(self, bool) """
        pass

    def setStyle(self, QStyle): # real signature unknown; restored from __doc__
        """ setStyle(self, QStyle) """
        pass

    def stickyFocus(self): # real signature unknown; restored from __doc__
        """ stickyFocus(self) -> bool """
        return False

    def style(self): # real signature unknown; restored from __doc__
        """ style(self) -> QStyle """
        return QStyle

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def update(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        update(self, rect: QRectF = QRectF())
        update(self, float, float, float, float)
        """
        pass

    def views(self): # real signature unknown; restored from __doc__
        """ views(self) -> List[QGraphicsView] """
        return []

    def wheelEvent(self, QGraphicsSceneWheelEvent): # real signature unknown; restored from __doc__
        """ wheelEvent(self, QGraphicsSceneWheelEvent) """
        pass

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> float """
        return 0.0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AllLayers = 65535
    BackgroundLayer = 2
    BspTreeIndex = 0
    ForegroundLayer = 4
    ItemLayer = 1
    NoIndex = -1


