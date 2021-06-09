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


class QQuickItem(__PyQt5_QtCore.QObject, __PyQt5_QtQml.QQmlParserStatus):
    """ QQuickItem(parent: QQuickItem = None) """
    def acceptedMouseButtons(self): # real signature unknown; restored from __doc__
        """ acceptedMouseButtons(self) -> Qt.MouseButtons """
        pass

    def acceptHoverEvents(self): # real signature unknown; restored from __doc__
        """ acceptHoverEvents(self) -> bool """
        return False

    def acceptTouchEvents(self): # real signature unknown; restored from __doc__
        """ acceptTouchEvents(self) -> bool """
        return False

    def activeFocusOnTab(self): # real signature unknown; restored from __doc__
        """ activeFocusOnTab(self) -> bool """
        return False

    def antialiasing(self): # real signature unknown; restored from __doc__
        """ antialiasing(self) -> bool """
        return False

    def baselineOffset(self): # real signature unknown; restored from __doc__
        """ baselineOffset(self) -> float """
        return 0.0

    def childAt(self, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ childAt(self, float, float) -> QQuickItem """
        return QQuickItem

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childItems(self): # real signature unknown; restored from __doc__
        """ childItems(self) -> List[QQuickItem] """
        return []

    def childMouseEventFilter(self, QQuickItem, QEvent): # real signature unknown; restored from __doc__
        """ childMouseEventFilter(self, QQuickItem, QEvent) -> bool """
        return False

    def childrenRect(self): # real signature unknown; restored from __doc__
        """ childrenRect(self) -> QRectF """
        pass

    def classBegin(self): # real signature unknown; restored from __doc__
        """ classBegin(self) """
        pass

    def clip(self): # real signature unknown; restored from __doc__
        """ clip(self) -> bool """
        return False

    def componentComplete(self): # real signature unknown; restored from __doc__
        """ componentComplete(self) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def containmentMask(self): # real signature unknown; restored from __doc__
        """ containmentMask(self) -> QObject """
        pass

    def containmentMaskChanged(self): # real signature unknown; restored from __doc__
        """ containmentMaskChanged(self) [signal] """
        pass

    def contains(self, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ contains(self, Union[QPointF, QPoint]) -> bool """
        return False

    def cursor(self): # real signature unknown; restored from __doc__
        """ cursor(self) -> QCursor """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dragEnterEvent(self, QDragEnterEvent): # real signature unknown; restored from __doc__
        """ dragEnterEvent(self, QDragEnterEvent) """
        pass

    def dragLeaveEvent(self, QDragLeaveEvent): # real signature unknown; restored from __doc__
        """ dragLeaveEvent(self, QDragLeaveEvent) """
        pass

    def dragMoveEvent(self, QDragMoveEvent): # real signature unknown; restored from __doc__
        """ dragMoveEvent(self, QDragMoveEvent) """
        pass

    def dropEvent(self, QDropEvent): # real signature unknown; restored from __doc__
        """ dropEvent(self, QDropEvent) """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def filtersChildMouseEvents(self): # real signature unknown; restored from __doc__
        """ filtersChildMouseEvents(self) -> bool """
        return False

    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> QQuickItem.Flags """
        pass

    def focusInEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ focusInEvent(self, QFocusEvent) """
        pass

    def focusOutEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, QFocusEvent) """
        pass

    def forceActiveFocus(self, Qt_FocusReason=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        forceActiveFocus(self)
        forceActiveFocus(self, Qt.FocusReason)
        """
        pass

    def geometryChanged(self, QRectF, QRectF_1): # real signature unknown; restored from __doc__
        """ geometryChanged(self, QRectF, QRectF) """
        pass

    def grabMouse(self): # real signature unknown; restored from __doc__
        """ grabMouse(self) """
        pass

    def grabToImage(self, targetSize=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ grabToImage(self, targetSize: QSize = QSize()) -> QQuickItemGrabResult """
        pass

    def grabTouchPoints(self, Iterable, p_int=None): # real signature unknown; restored from __doc__
        """ grabTouchPoints(self, Iterable[int]) """
        pass

    def hasActiveFocus(self): # real signature unknown; restored from __doc__
        """ hasActiveFocus(self) -> bool """
        return False

    def hasFocus(self): # real signature unknown; restored from __doc__
        """ hasFocus(self) -> bool """
        return False

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> float """
        return 0.0

    def heightValid(self): # real signature unknown; restored from __doc__
        """ heightValid(self) -> bool """
        return False

    def hoverEnterEvent(self, QHoverEvent): # real signature unknown; restored from __doc__
        """ hoverEnterEvent(self, QHoverEvent) """
        pass

    def hoverLeaveEvent(self, QHoverEvent): # real signature unknown; restored from __doc__
        """ hoverLeaveEvent(self, QHoverEvent) """
        pass

    def hoverMoveEvent(self, QHoverEvent): # real signature unknown; restored from __doc__
        """ hoverMoveEvent(self, QHoverEvent) """
        pass

    def implicitHeight(self): # real signature unknown; restored from __doc__
        """ implicitHeight(self) -> float """
        return 0.0

    def implicitWidth(self): # real signature unknown; restored from __doc__
        """ implicitWidth(self) -> float """
        return 0.0

    def inputMethodEvent(self, QInputMethodEvent): # real signature unknown; restored from __doc__
        """ inputMethodEvent(self, QInputMethodEvent) """
        pass

    def inputMethodQuery(self, Qt_InputMethodQuery): # real signature unknown; restored from __doc__
        """ inputMethodQuery(self, Qt.InputMethodQuery) -> Any """
        pass

    def isAncestorOf(self, QQuickItem): # real signature unknown; restored from __doc__
        """ isAncestorOf(self, QQuickItem) -> bool """
        return False

    def isComponentComplete(self): # real signature unknown; restored from __doc__
        """ isComponentComplete(self) -> bool """
        return False

    def isEnabled(self): # real signature unknown; restored from __doc__
        """ isEnabled(self) -> bool """
        return False

    def isFocusScope(self): # real signature unknown; restored from __doc__
        """ isFocusScope(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isTextureProvider(self): # real signature unknown; restored from __doc__
        """ isTextureProvider(self) -> bool """
        return False

    def isVisible(self): # real signature unknown; restored from __doc__
        """ isVisible(self) -> bool """
        return False

    def itemChange(self, QQuickItem_ItemChange, QQuickItem_ItemChangeData): # real signature unknown; restored from __doc__
        """ itemChange(self, QQuickItem.ItemChange, QQuickItem.ItemChangeData) """
        pass

    def keepMouseGrab(self): # real signature unknown; restored from __doc__
        """ keepMouseGrab(self) -> bool """
        return False

    def keepTouchGrab(self): # real signature unknown; restored from __doc__
        """ keepTouchGrab(self) -> bool """
        return False

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, QKeyEvent) """
        pass

    def keyReleaseEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, QKeyEvent) """
        pass

    def mapFromGlobal(self, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ mapFromGlobal(self, Union[QPointF, QPoint]) -> QPointF """
        pass

    def mapFromItem(self, QQuickItem, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ mapFromItem(self, QQuickItem, Union[QPointF, QPoint]) -> QPointF """
        pass

    def mapFromScene(self, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ mapFromScene(self, Union[QPointF, QPoint]) -> QPointF """
        pass

    def mapRectFromItem(self, QQuickItem, QRectF): # real signature unknown; restored from __doc__
        """ mapRectFromItem(self, QQuickItem, QRectF) -> QRectF """
        pass

    def mapRectFromScene(self, QRectF): # real signature unknown; restored from __doc__
        """ mapRectFromScene(self, QRectF) -> QRectF """
        pass

    def mapRectToItem(self, QQuickItem, QRectF): # real signature unknown; restored from __doc__
        """ mapRectToItem(self, QQuickItem, QRectF) -> QRectF """
        pass

    def mapRectToScene(self, QRectF): # real signature unknown; restored from __doc__
        """ mapRectToScene(self, QRectF) -> QRectF """
        pass

    def mapToGlobal(self, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ mapToGlobal(self, Union[QPointF, QPoint]) -> QPointF """
        pass

    def mapToItem(self, QQuickItem, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ mapToItem(self, QQuickItem, Union[QPointF, QPoint]) -> QPointF """
        pass

    def mapToScene(self, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ mapToScene(self, Union[QPointF, QPoint]) -> QPointF """
        pass

    def mouseDoubleClickEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mouseDoubleClickEvent(self, QMouseEvent) """
        pass

    def mouseMoveEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mouseMoveEvent(self, QMouseEvent) """
        pass

    def mousePressEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, QMouseEvent) """
        pass

    def mouseReleaseEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, QMouseEvent) """
        pass

    def mouseUngrabEvent(self): # real signature unknown; restored from __doc__
        """ mouseUngrabEvent(self) """
        pass

    def nextItemInFocusChain(self, forward=True): # real signature unknown; restored from __doc__
        """ nextItemInFocusChain(self, forward: bool = True) -> QQuickItem """
        return QQuickItem

    def opacity(self): # real signature unknown; restored from __doc__
        """ opacity(self) -> float """
        return 0.0

    def parentItem(self): # real signature unknown; restored from __doc__
        """ parentItem(self) -> QQuickItem """
        return QQuickItem

    def polish(self): # real signature unknown; restored from __doc__
        """ polish(self) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def releaseResources(self): # real signature unknown; restored from __doc__
        """ releaseResources(self) """
        pass

    def resetAntialiasing(self): # real signature unknown; restored from __doc__
        """ resetAntialiasing(self) """
        pass

    def resetHeight(self): # real signature unknown; restored from __doc__
        """ resetHeight(self) """
        pass

    def resetWidth(self): # real signature unknown; restored from __doc__
        """ resetWidth(self) """
        pass

    def rotation(self): # real signature unknown; restored from __doc__
        """ rotation(self) -> float """
        return 0.0

    def scale(self): # real signature unknown; restored from __doc__
        """ scale(self) -> float """
        return 0.0

    def scopedFocusItem(self): # real signature unknown; restored from __doc__
        """ scopedFocusItem(self) -> QQuickItem """
        return QQuickItem

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
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

    def setActiveFocusOnTab(self, bool): # real signature unknown; restored from __doc__
        """ setActiveFocusOnTab(self, bool) """
        pass

    def setAntialiasing(self, bool): # real signature unknown; restored from __doc__
        """ setAntialiasing(self, bool) """
        pass

    def setBaselineOffset(self, p_float): # real signature unknown; restored from __doc__
        """ setBaselineOffset(self, float) """
        pass

    def setClip(self, bool): # real signature unknown; restored from __doc__
        """ setClip(self, bool) """
        pass

    def setContainmentMask(self, QObject): # real signature unknown; restored from __doc__
        """ setContainmentMask(self, QObject) """
        pass

    def setCursor(self, Union, QCursor=None, Qt_CursorShape=None): # real signature unknown; restored from __doc__
        """ setCursor(self, Union[QCursor, Qt.CursorShape]) """
        pass

    def setEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setEnabled(self, bool) """
        pass

    def setFiltersChildMouseEvents(self, bool): # real signature unknown; restored from __doc__
        """ setFiltersChildMouseEvents(self, bool) """
        pass

    def setFlag(self, QQuickItem_Flag, enabled=True): # real signature unknown; restored from __doc__
        """ setFlag(self, QQuickItem.Flag, enabled: bool = True) """
        pass

    def setFlags(self, Union, QQuickItem_Flags=None, QQuickItem_Flag=None): # real signature unknown; restored from __doc__
        """ setFlags(self, Union[QQuickItem.Flags, QQuickItem.Flag]) """
        pass

    def setFocus(self, bool, Qt_FocusReason=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setFocus(self, bool)
        setFocus(self, bool, Qt.FocusReason)
        """
        pass

    def setHeight(self, p_float): # real signature unknown; restored from __doc__
        """ setHeight(self, float) """
        pass

    def setImplicitHeight(self, p_float): # real signature unknown; restored from __doc__
        """ setImplicitHeight(self, float) """
        pass

    def setImplicitWidth(self, p_float): # real signature unknown; restored from __doc__
        """ setImplicitWidth(self, float) """
        pass

    def setKeepMouseGrab(self, bool): # real signature unknown; restored from __doc__
        """ setKeepMouseGrab(self, bool) """
        pass

    def setKeepTouchGrab(self, bool): # real signature unknown; restored from __doc__
        """ setKeepTouchGrab(self, bool) """
        pass

    def setOpacity(self, p_float): # real signature unknown; restored from __doc__
        """ setOpacity(self, float) """
        pass

    def setParentItem(self, QQuickItem): # real signature unknown; restored from __doc__
        """ setParentItem(self, QQuickItem) """
        pass

    def setRotation(self, p_float): # real signature unknown; restored from __doc__
        """ setRotation(self, float) """
        pass

    def setScale(self, p_float): # real signature unknown; restored from __doc__
        """ setScale(self, float) """
        pass

    def setSmooth(self, bool): # real signature unknown; restored from __doc__
        """ setSmooth(self, bool) """
        pass

    def setState(self, p_str): # real signature unknown; restored from __doc__
        """ setState(self, str) """
        pass

    def setTransformOrigin(self, QQuickItem_TransformOrigin): # real signature unknown; restored from __doc__
        """ setTransformOrigin(self, QQuickItem.TransformOrigin) """
        pass

    def setVisible(self, bool): # real signature unknown; restored from __doc__
        """ setVisible(self, bool) """
        pass

    def setWidth(self, p_float): # real signature unknown; restored from __doc__
        """ setWidth(self, float) """
        pass

    def setX(self, p_float): # real signature unknown; restored from __doc__
        """ setX(self, float) """
        pass

    def setY(self, p_float): # real signature unknown; restored from __doc__
        """ setY(self, float) """
        pass

    def setZ(self, p_float): # real signature unknown; restored from __doc__
        """ setZ(self, float) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> QSizeF """
        pass

    def smooth(self): # real signature unknown; restored from __doc__
        """ smooth(self) -> bool """
        return False

    def stackAfter(self, QQuickItem): # real signature unknown; restored from __doc__
        """ stackAfter(self, QQuickItem) """
        pass

    def stackBefore(self, QQuickItem): # real signature unknown; restored from __doc__
        """ stackBefore(self, QQuickItem) """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> str """
        return ""

    def textureProvider(self): # real signature unknown; restored from __doc__
        """ textureProvider(self) -> QSGTextureProvider """
        return QSGTextureProvider

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def touchEvent(self, QTouchEvent): # real signature unknown; restored from __doc__
        """ touchEvent(self, QTouchEvent) """
        pass

    def touchUngrabEvent(self): # real signature unknown; restored from __doc__
        """ touchUngrabEvent(self) """
        pass

    def transformOrigin(self): # real signature unknown; restored from __doc__
        """ transformOrigin(self) -> QQuickItem.TransformOrigin """
        pass

    def ungrabMouse(self): # real signature unknown; restored from __doc__
        """ ungrabMouse(self) """
        pass

    def ungrabTouchPoints(self): # real signature unknown; restored from __doc__
        """ ungrabTouchPoints(self) """
        pass

    def unsetCursor(self): # real signature unknown; restored from __doc__
        """ unsetCursor(self) """
        pass

    def update(self): # real signature unknown; restored from __doc__
        """ update(self) """
        pass

    def updateInputMethod(self, queries, Qt_InputMethodQueries=None, Qt_InputMethodQuery=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ updateInputMethod(self, queries: Union[Qt.InputMethodQueries, Qt.InputMethodQuery] = Qt.ImQueryInput) """
        pass

    def updatePaintNode(self, QSGNode, QQuickItem_UpdatePaintNodeData): # real signature unknown; restored from __doc__
        """ updatePaintNode(self, QSGNode, QQuickItem.UpdatePaintNodeData) -> QSGNode """
        return QSGNode

    def updatePolish(self): # real signature unknown; restored from __doc__
        """ updatePolish(self) """
        pass

    def wheelEvent(self, QWheelEvent): # real signature unknown; restored from __doc__
        """ wheelEvent(self, QWheelEvent) """
        pass

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> float """
        return 0.0

    def widthValid(self): # real signature unknown; restored from __doc__
        """ widthValid(self) -> bool """
        return False

    def window(self): # real signature unknown; restored from __doc__
        """ window(self) -> QQuickWindow """
        return QQuickWindow

    def windowChanged(self, QQuickWindow): # real signature unknown; restored from __doc__
        """ windowChanged(self, QQuickWindow) [signal] """
        pass

    def x(self): # real signature unknown; restored from __doc__
        """ x(self) -> float """
        return 0.0

    def y(self): # real signature unknown; restored from __doc__
        """ y(self) -> float """
        return 0.0

    def z(self): # real signature unknown; restored from __doc__
        """ z(self) -> float """
        return 0.0

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    Bottom = 7
    BottomLeft = 6
    BottomRight = 8
    Center = 4
    ItemAcceptsDrops = 16
    ItemAcceptsInputMethod = 2
    ItemActiveFocusHasChanged = 6
    ItemAntialiasingHasChanged = 8
    ItemChildAddedChange = 0
    ItemChildRemovedChange = 1
    ItemClipsChildrenToShape = 1
    ItemDevicePixelRatioHasChanged = 9
    ItemEnabledHasChanged = 10
    ItemHasContents = 8
    ItemIsFocusScope = 4
    ItemOpacityHasChanged = 5
    ItemParentHasChanged = 4
    ItemRotationHasChanged = 7
    ItemSceneChange = 2
    ItemVisibleHasChanged = 3
    Left = 3
    Right = 5
    Top = 1
    TopLeft = 0
    TopRight = 2


