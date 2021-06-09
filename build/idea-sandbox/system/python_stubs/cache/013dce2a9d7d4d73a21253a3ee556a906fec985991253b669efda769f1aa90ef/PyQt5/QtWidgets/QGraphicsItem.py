# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QGraphicsItem(__sip.wrapper):
    """ QGraphicsItem(parent: QGraphicsItem = None) """
    def acceptDrops(self): # real signature unknown; restored from __doc__
        """ acceptDrops(self) -> bool """
        return False

    def acceptedMouseButtons(self): # real signature unknown; restored from __doc__
        """ acceptedMouseButtons(self) -> Qt.MouseButtons """
        pass

    def acceptHoverEvents(self): # real signature unknown; restored from __doc__
        """ acceptHoverEvents(self) -> bool """
        return False

    def acceptTouchEvents(self): # real signature unknown; restored from __doc__
        """ acceptTouchEvents(self) -> bool """
        return False

    def advance(self, p_int): # real signature unknown; restored from __doc__
        """ advance(self, int) """
        pass

    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> QRectF """
        pass

    def boundingRegion(self, QTransform): # real signature unknown; restored from __doc__
        """ boundingRegion(self, QTransform) -> QRegion """
        pass

    def boundingRegionGranularity(self): # real signature unknown; restored from __doc__
        """ boundingRegionGranularity(self) -> float """
        return 0.0

    def cacheMode(self): # real signature unknown; restored from __doc__
        """ cacheMode(self) -> QGraphicsItem.CacheMode """
        pass

    def childItems(self): # real signature unknown; restored from __doc__
        """ childItems(self) -> List[QGraphicsItem] """
        return []

    def childrenBoundingRect(self): # real signature unknown; restored from __doc__
        """ childrenBoundingRect(self) -> QRectF """
        pass

    def clearFocus(self): # real signature unknown; restored from __doc__
        """ clearFocus(self) """
        pass

    def clipPath(self): # real signature unknown; restored from __doc__
        """ clipPath(self) -> QPainterPath """
        pass

    def collidesWithItem(self, QGraphicsItem, mode=None): # real signature unknown; restored from __doc__
        """ collidesWithItem(self, QGraphicsItem, mode: Qt.ItemSelectionMode = Qt.IntersectsItemShape) -> bool """
        return False

    def collidesWithPath(self, QPainterPath, mode=None): # real signature unknown; restored from __doc__
        """ collidesWithPath(self, QPainterPath, mode: Qt.ItemSelectionMode = Qt.IntersectsItemShape) -> bool """
        return False

    def collidingItems(self, mode=None): # real signature unknown; restored from __doc__
        """ collidingItems(self, mode: Qt.ItemSelectionMode = Qt.IntersectsItemShape) -> List[QGraphicsItem] """
        return []

    def commonAncestorItem(self, QGraphicsItem): # real signature unknown; restored from __doc__
        """ commonAncestorItem(self, QGraphicsItem) -> QGraphicsItem """
        return QGraphicsItem

    def contains(self, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ contains(self, Union[QPointF, QPoint]) -> bool """
        return False

    def contextMenuEvent(self, QGraphicsSceneContextMenuEvent): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, QGraphicsSceneContextMenuEvent) """
        pass

    def cursor(self): # real signature unknown; restored from __doc__
        """ cursor(self) -> QCursor """
        pass

    def data(self, p_int): # real signature unknown; restored from __doc__
        """ data(self, int) -> Any """
        pass

    def deviceTransform(self, QTransform): # real signature unknown; restored from __doc__
        """ deviceTransform(self, QTransform) -> QTransform """
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

    def effectiveOpacity(self): # real signature unknown; restored from __doc__
        """ effectiveOpacity(self) -> float """
        return 0.0

    def ensureVisible(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        ensureVisible(self, rect: QRectF = QRectF(), xMargin: int = 50, yMargin: int = 50)
        ensureVisible(self, float, float, float, float, xMargin: int = 50, yMargin: int = 50)
        """
        pass

    def filtersChildEvents(self): # real signature unknown; restored from __doc__
        """ filtersChildEvents(self) -> bool """
        return False

    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> QGraphicsItem.GraphicsItemFlags """
        pass

    def focusInEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ focusInEvent(self, QFocusEvent) """
        pass

    def focusItem(self): # real signature unknown; restored from __doc__
        """ focusItem(self) -> QGraphicsItem """
        return QGraphicsItem

    def focusOutEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, QFocusEvent) """
        pass

    def focusProxy(self): # real signature unknown; restored from __doc__
        """ focusProxy(self) -> QGraphicsItem """
        return QGraphicsItem

    def grabKeyboard(self): # real signature unknown; restored from __doc__
        """ grabKeyboard(self) """
        pass

    def grabMouse(self): # real signature unknown; restored from __doc__
        """ grabMouse(self) """
        pass

    def graphicsEffect(self): # real signature unknown; restored from __doc__
        """ graphicsEffect(self) -> QGraphicsEffect """
        return QGraphicsEffect

    def group(self): # real signature unknown; restored from __doc__
        """ group(self) -> QGraphicsItemGroup """
        return QGraphicsItemGroup

    def hasCursor(self): # real signature unknown; restored from __doc__
        """ hasCursor(self) -> bool """
        return False

    def hasFocus(self): # real signature unknown; restored from __doc__
        """ hasFocus(self) -> bool """
        return False

    def hide(self): # real signature unknown; restored from __doc__
        """ hide(self) """
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

    def inputMethodHints(self): # real signature unknown; restored from __doc__
        """ inputMethodHints(self) -> Qt.InputMethodHints """
        pass

    def inputMethodQuery(self, Qt_InputMethodQuery): # real signature unknown; restored from __doc__
        """ inputMethodQuery(self, Qt.InputMethodQuery) -> Any """
        pass

    def installSceneEventFilter(self, QGraphicsItem): # real signature unknown; restored from __doc__
        """ installSceneEventFilter(self, QGraphicsItem) """
        pass

    def isActive(self): # real signature unknown; restored from __doc__
        """ isActive(self) -> bool """
        return False

    def isAncestorOf(self, QGraphicsItem): # real signature unknown; restored from __doc__
        """ isAncestorOf(self, QGraphicsItem) -> bool """
        return False

    def isBlockedByModalPanel(self): # real signature unknown; restored from __doc__
        """ isBlockedByModalPanel(self) -> Tuple[bool, QGraphicsItem] """
        pass

    def isClipped(self): # real signature unknown; restored from __doc__
        """ isClipped(self) -> bool """
        return False

    def isEnabled(self): # real signature unknown; restored from __doc__
        """ isEnabled(self) -> bool """
        return False

    def isObscured(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        isObscured(self, rect: QRectF = QRectF()) -> bool
        isObscured(self, float, float, float, float) -> bool
        """
        return False

    def isObscuredBy(self, QGraphicsItem): # real signature unknown; restored from __doc__
        """ isObscuredBy(self, QGraphicsItem) -> bool """
        return False

    def isPanel(self): # real signature unknown; restored from __doc__
        """ isPanel(self) -> bool """
        return False

    def isSelected(self): # real signature unknown; restored from __doc__
        """ isSelected(self) -> bool """
        return False

    def isUnderMouse(self): # real signature unknown; restored from __doc__
        """ isUnderMouse(self) -> bool """
        return False

    def isVisible(self): # real signature unknown; restored from __doc__
        """ isVisible(self) -> bool """
        return False

    def isVisibleTo(self, QGraphicsItem): # real signature unknown; restored from __doc__
        """ isVisibleTo(self, QGraphicsItem) -> bool """
        return False

    def isWidget(self): # real signature unknown; restored from __doc__
        """ isWidget(self) -> bool """
        return False

    def isWindow(self): # real signature unknown; restored from __doc__
        """ isWindow(self) -> bool """
        return False

    def itemChange(self, QGraphicsItem_GraphicsItemChange, Any): # real signature unknown; restored from __doc__
        """ itemChange(self, QGraphicsItem.GraphicsItemChange, Any) -> Any """
        pass

    def itemTransform(self, QGraphicsItem): # real signature unknown; restored from __doc__
        """ itemTransform(self, QGraphicsItem) -> Tuple[QTransform, bool] """
        pass

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, QKeyEvent) """
        pass

    def keyReleaseEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, QKeyEvent) """
        pass

    def mapFromItem(self, QGraphicsItem, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mapFromItem(self, QGraphicsItem, Union[QPointF, QPoint]) -> QPointF
        mapFromItem(self, QGraphicsItem, QRectF) -> QPolygonF
        mapFromItem(self, QGraphicsItem, QPolygonF) -> QPolygonF
        mapFromItem(self, QGraphicsItem, QPainterPath) -> QPainterPath
        mapFromItem(self, QGraphicsItem, float, float) -> QPointF
        mapFromItem(self, QGraphicsItem, float, float, float, float) -> QPolygonF
        """
        pass

    def mapFromParent(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mapFromParent(self, Union[QPointF, QPoint]) -> QPointF
        mapFromParent(self, QRectF) -> QPolygonF
        mapFromParent(self, QPolygonF) -> QPolygonF
        mapFromParent(self, QPainterPath) -> QPainterPath
        mapFromParent(self, float, float) -> QPointF
        mapFromParent(self, float, float, float, float) -> QPolygonF
        """
        pass

    def mapFromScene(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mapFromScene(self, Union[QPointF, QPoint]) -> QPointF
        mapFromScene(self, QRectF) -> QPolygonF
        mapFromScene(self, QPolygonF) -> QPolygonF
        mapFromScene(self, QPainterPath) -> QPainterPath
        mapFromScene(self, float, float) -> QPointF
        mapFromScene(self, float, float, float, float) -> QPolygonF
        """
        pass

    def mapRectFromItem(self, QGraphicsItem, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mapRectFromItem(self, QGraphicsItem, QRectF) -> QRectF
        mapRectFromItem(self, QGraphicsItem, float, float, float, float) -> QRectF
        """
        pass

    def mapRectFromParent(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mapRectFromParent(self, QRectF) -> QRectF
        mapRectFromParent(self, float, float, float, float) -> QRectF
        """
        pass

    def mapRectFromScene(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mapRectFromScene(self, QRectF) -> QRectF
        mapRectFromScene(self, float, float, float, float) -> QRectF
        """
        pass

    def mapRectToItem(self, QGraphicsItem, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mapRectToItem(self, QGraphicsItem, QRectF) -> QRectF
        mapRectToItem(self, QGraphicsItem, float, float, float, float) -> QRectF
        """
        pass

    def mapRectToParent(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mapRectToParent(self, QRectF) -> QRectF
        mapRectToParent(self, float, float, float, float) -> QRectF
        """
        pass

    def mapRectToScene(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mapRectToScene(self, QRectF) -> QRectF
        mapRectToScene(self, float, float, float, float) -> QRectF
        """
        pass

    def mapToItem(self, QGraphicsItem, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mapToItem(self, QGraphicsItem, Union[QPointF, QPoint]) -> QPointF
        mapToItem(self, QGraphicsItem, QRectF) -> QPolygonF
        mapToItem(self, QGraphicsItem, QPolygonF) -> QPolygonF
        mapToItem(self, QGraphicsItem, QPainterPath) -> QPainterPath
        mapToItem(self, QGraphicsItem, float, float) -> QPointF
        mapToItem(self, QGraphicsItem, float, float, float, float) -> QPolygonF
        """
        pass

    def mapToParent(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mapToParent(self, Union[QPointF, QPoint]) -> QPointF
        mapToParent(self, QRectF) -> QPolygonF
        mapToParent(self, QPolygonF) -> QPolygonF
        mapToParent(self, QPainterPath) -> QPainterPath
        mapToParent(self, float, float) -> QPointF
        mapToParent(self, float, float, float, float) -> QPolygonF
        """
        pass

    def mapToScene(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mapToScene(self, Union[QPointF, QPoint]) -> QPointF
        mapToScene(self, QRectF) -> QPolygonF
        mapToScene(self, QPolygonF) -> QPolygonF
        mapToScene(self, QPainterPath) -> QPainterPath
        mapToScene(self, float, float) -> QPointF
        mapToScene(self, float, float, float, float) -> QPolygonF
        """
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

    def moveBy(self, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ moveBy(self, float, float) """
        pass

    def opacity(self): # real signature unknown; restored from __doc__
        """ opacity(self) -> float """
        return 0.0

    def opaqueArea(self): # real signature unknown; restored from __doc__
        """ opaqueArea(self) -> QPainterPath """
        pass

    def paint(self, QPainter, QStyleOptionGraphicsItem, widget=None): # real signature unknown; restored from __doc__
        """ paint(self, QPainter, QStyleOptionGraphicsItem, widget: QWidget = None) """
        pass

    def panel(self): # real signature unknown; restored from __doc__
        """ panel(self) -> QGraphicsItem """
        return QGraphicsItem

    def panelModality(self): # real signature unknown; restored from __doc__
        """ panelModality(self) -> QGraphicsItem.PanelModality """
        pass

    def parentItem(self): # real signature unknown; restored from __doc__
        """ parentItem(self) -> QGraphicsItem """
        return QGraphicsItem

    def parentObject(self): # real signature unknown; restored from __doc__
        """ parentObject(self) -> QGraphicsObject """
        return QGraphicsObject

    def parentWidget(self): # real signature unknown; restored from __doc__
        """ parentWidget(self) -> QGraphicsWidget """
        return QGraphicsWidget

    def pos(self): # real signature unknown; restored from __doc__
        """ pos(self) -> QPointF """
        pass

    def prepareGeometryChange(self): # real signature unknown; restored from __doc__
        """ prepareGeometryChange(self) """
        pass

    def removeSceneEventFilter(self, QGraphicsItem): # real signature unknown; restored from __doc__
        """ removeSceneEventFilter(self, QGraphicsItem) """
        pass

    def resetTransform(self): # real signature unknown; restored from __doc__
        """ resetTransform(self) """
        pass

    def rotation(self): # real signature unknown; restored from __doc__
        """ rotation(self) -> float """
        return 0.0

    def scale(self): # real signature unknown; restored from __doc__
        """ scale(self) -> float """
        return 0.0

    def scene(self): # real signature unknown; restored from __doc__
        """ scene(self) -> QGraphicsScene """
        return QGraphicsScene

    def sceneBoundingRect(self): # real signature unknown; restored from __doc__
        """ sceneBoundingRect(self) -> QRectF """
        pass

    def sceneEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ sceneEvent(self, QEvent) -> bool """
        return False

    def sceneEventFilter(self, QGraphicsItem, QEvent): # real signature unknown; restored from __doc__
        """ sceneEventFilter(self, QGraphicsItem, QEvent) -> bool """
        return False

    def scenePos(self): # real signature unknown; restored from __doc__
        """ scenePos(self) -> QPointF """
        pass

    def sceneTransform(self): # real signature unknown; restored from __doc__
        """ sceneTransform(self) -> QTransform """
        pass

    def scroll(self, p_float, p_float_1, rect=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ scroll(self, float, float, rect: QRectF = QRectF()) """
        pass

    def setAcceptDrops(self, bool): # real signature unknown; restored from __doc__
        """ setAcceptDrops(self, bool) """
        pass

    def setAcceptedMouseButtons(self, Union, Qt_MouseButtons=None, Qt_MouseButton=None): # real signature unknown; restored from __doc__
        """ setAcceptedMouseButtons(self, Union[Qt.MouseButtons, Qt.MouseButton]) """
        pass

    def setAcceptHoverEvents(self, bool): # real signature unknown; restored from __doc__
        """ setAcceptHoverEvents(self, bool) """
        pass

    def setAcceptTouchEvents(self, bool): # real signature unknown; restored from __doc__
        """ setAcceptTouchEvents(self, bool) """
        pass

    def setActive(self, bool): # real signature unknown; restored from __doc__
        """ setActive(self, bool) """
        pass

    def setBoundingRegionGranularity(self, p_float): # real signature unknown; restored from __doc__
        """ setBoundingRegionGranularity(self, float) """
        pass

    def setCacheMode(self, QGraphicsItem_CacheMode, logicalCacheSize=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setCacheMode(self, QGraphicsItem.CacheMode, logicalCacheSize: QSize = QSize()) """
        pass

    def setCursor(self, Union, QCursor=None, Qt_CursorShape=None): # real signature unknown; restored from __doc__
        """ setCursor(self, Union[QCursor, Qt.CursorShape]) """
        pass

    def setData(self, p_int, Any): # real signature unknown; restored from __doc__
        """ setData(self, int, Any) """
        pass

    def setEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setEnabled(self, bool) """
        pass

    def setFiltersChildEvents(self, bool): # real signature unknown; restored from __doc__
        """ setFiltersChildEvents(self, bool) """
        pass

    def setFlag(self, QGraphicsItem_GraphicsItemFlag, enabled=True): # real signature unknown; restored from __doc__
        """ setFlag(self, QGraphicsItem.GraphicsItemFlag, enabled: bool = True) """
        pass

    def setFlags(self, Union, QGraphicsItem_GraphicsItemFlags=None, QGraphicsItem_GraphicsItemFlag=None): # real signature unknown; restored from __doc__
        """ setFlags(self, Union[QGraphicsItem.GraphicsItemFlags, QGraphicsItem.GraphicsItemFlag]) """
        pass

    def setFocus(self, focusReason=None): # real signature unknown; restored from __doc__
        """ setFocus(self, focusReason: Qt.FocusReason = Qt.OtherFocusReason) """
        pass

    def setFocusProxy(self, QGraphicsItem): # real signature unknown; restored from __doc__
        """ setFocusProxy(self, QGraphicsItem) """
        pass

    def setGraphicsEffect(self, QGraphicsEffect): # real signature unknown; restored from __doc__
        """ setGraphicsEffect(self, QGraphicsEffect) """
        pass

    def setGroup(self, QGraphicsItemGroup): # real signature unknown; restored from __doc__
        """ setGroup(self, QGraphicsItemGroup) """
        pass

    def setInputMethodHints(self, Union, Qt_InputMethodHints=None, Qt_InputMethodHint=None): # real signature unknown; restored from __doc__
        """ setInputMethodHints(self, Union[Qt.InputMethodHints, Qt.InputMethodHint]) """
        pass

    def setOpacity(self, p_float): # real signature unknown; restored from __doc__
        """ setOpacity(self, float) """
        pass

    def setPanelModality(self, QGraphicsItem_PanelModality): # real signature unknown; restored from __doc__
        """ setPanelModality(self, QGraphicsItem.PanelModality) """
        pass

    def setParentItem(self, QGraphicsItem): # real signature unknown; restored from __doc__
        """ setParentItem(self, QGraphicsItem) """
        pass

    def setPos(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setPos(self, Union[QPointF, QPoint])
        setPos(self, float, float)
        """
        pass

    def setRotation(self, p_float): # real signature unknown; restored from __doc__
        """ setRotation(self, float) """
        pass

    def setScale(self, p_float): # real signature unknown; restored from __doc__
        """ setScale(self, float) """
        pass

    def setSelected(self, bool): # real signature unknown; restored from __doc__
        """ setSelected(self, bool) """
        pass

    def setToolTip(self, p_str): # real signature unknown; restored from __doc__
        """ setToolTip(self, str) """
        pass

    def setTransform(self, QTransform, combine=False): # real signature unknown; restored from __doc__
        """ setTransform(self, QTransform, combine: bool = False) """
        pass

    def setTransformations(self, Iterable, QGraphicsTransform=None): # real signature unknown; restored from __doc__
        """ setTransformations(self, Iterable[QGraphicsTransform]) """
        pass

    def setTransformOriginPoint(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setTransformOriginPoint(self, Union[QPointF, QPoint])
        setTransformOriginPoint(self, float, float)
        """
        pass

    def setVisible(self, bool): # real signature unknown; restored from __doc__
        """ setVisible(self, bool) """
        pass

    def setX(self, p_float): # real signature unknown; restored from __doc__
        """ setX(self, float) """
        pass

    def setY(self, p_float): # real signature unknown; restored from __doc__
        """ setY(self, float) """
        pass

    def setZValue(self, p_float): # real signature unknown; restored from __doc__
        """ setZValue(self, float) """
        pass

    def shape(self): # real signature unknown; restored from __doc__
        """ shape(self) -> QPainterPath """
        pass

    def show(self): # real signature unknown; restored from __doc__
        """ show(self) """
        pass

    def stackBefore(self, QGraphicsItem): # real signature unknown; restored from __doc__
        """ stackBefore(self, QGraphicsItem) """
        pass

    def toGraphicsObject(self): # real signature unknown; restored from __doc__
        """ toGraphicsObject(self) -> QGraphicsObject """
        return QGraphicsObject

    def toolTip(self): # real signature unknown; restored from __doc__
        """ toolTip(self) -> str """
        return ""

    def topLevelItem(self): # real signature unknown; restored from __doc__
        """ topLevelItem(self) -> QGraphicsItem """
        return QGraphicsItem

    def topLevelWidget(self): # real signature unknown; restored from __doc__
        """ topLevelWidget(self) -> QGraphicsWidget """
        return QGraphicsWidget

    def transform(self): # real signature unknown; restored from __doc__
        """ transform(self) -> QTransform """
        pass

    def transformations(self): # real signature unknown; restored from __doc__
        """ transformations(self) -> List[QGraphicsTransform] """
        return []

    def transformOriginPoint(self): # real signature unknown; restored from __doc__
        """ transformOriginPoint(self) -> QPointF """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> int """
        return 0

    def ungrabKeyboard(self): # real signature unknown; restored from __doc__
        """ ungrabKeyboard(self) """
        pass

    def ungrabMouse(self): # real signature unknown; restored from __doc__
        """ ungrabMouse(self) """
        pass

    def unsetCursor(self): # real signature unknown; restored from __doc__
        """ unsetCursor(self) """
        pass

    def update(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        update(self, rect: QRectF = QRectF())
        update(self, float, float, float, float)
        """
        pass

    def updateMicroFocus(self): # real signature unknown; restored from __doc__
        """ updateMicroFocus(self) """
        pass

    def wheelEvent(self, QGraphicsSceneWheelEvent): # real signature unknown; restored from __doc__
        """ wheelEvent(self, QGraphicsSceneWheelEvent) """
        pass

    def window(self): # real signature unknown; restored from __doc__
        """ window(self) -> QGraphicsWidget """
        return QGraphicsWidget

    def x(self): # real signature unknown; restored from __doc__
        """ x(self) -> float """
        return 0.0

    def y(self): # real signature unknown; restored from __doc__
        """ y(self) -> float """
        return 0.0

    def zValue(self): # real signature unknown; restored from __doc__
        """ zValue(self) -> float """
        return 0.0

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    DeviceCoordinateCache = 2
    ItemAcceptsInputMethod = 4096
    ItemChildAddedChange = 6
    ItemChildRemovedChange = 7
    ItemClipsChildrenToShape = 16
    ItemClipsToShape = 8
    ItemContainsChildrenInShape = 524288
    ItemCoordinateCache = 1
    ItemCursorChange = 17
    ItemCursorHasChanged = 18
    ItemDoesntPropagateOpacityToChildren = 128
    ItemEnabledChange = 3
    ItemEnabledHasChanged = 13
    ItemFlagsChange = 21
    ItemFlagsHaveChanged = 22
    ItemHasNoContents = 1024
    ItemIgnoresParentOpacity = 64
    ItemIgnoresTransformations = 32
    ItemIsFocusable = 4
    ItemIsMovable = 1
    ItemIsPanel = 16384
    ItemIsSelectable = 2
    ItemMatrixChange = 1
    ItemNegativeZStacksBehindParent = 8192
    ItemOpacityChange = 25
    ItemOpacityHasChanged = 26
    ItemParentChange = 5
    ItemParentHasChanged = 15
    ItemPositionChange = 0
    ItemPositionHasChanged = 9
    ItemRotationChange = 28
    ItemRotationHasChanged = 29
    ItemScaleChange = 30
    ItemScaleHasChanged = 31
    ItemSceneChange = 11
    ItemSceneHasChanged = 16
    ItemScenePositionHasChanged = 27
    ItemSelectedChange = 4
    ItemSelectedHasChanged = 14
    ItemSendsGeometryChanges = 2048
    ItemSendsScenePositionChanges = 65536
    ItemStacksBehindParent = 256
    ItemToolTipChange = 19
    ItemToolTipHasChanged = 20
    ItemTransformChange = 8
    ItemTransformHasChanged = 10
    ItemTransformOriginPointChange = 32
    ItemTransformOriginPointHasChanged = 33
    ItemUsesExtendedStyleOption = 512
    ItemVisibleChange = 2
    ItemVisibleHasChanged = 12
    ItemZValueChange = 23
    ItemZValueHasChanged = 24
    NoCache = 0
    NonModal = 0
    PanelModal = 1
    SceneModal = 2
    Type = 1
    UserType = 65536


