# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QAbstractScrollArea import QAbstractScrollArea

class QGraphicsView(QAbstractScrollArea):
    """
    QGraphicsView(parent: QWidget = None)
    QGraphicsView(QGraphicsScene, parent: QWidget = None)
    """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def alignment(self): # real signature unknown; restored from __doc__
        """ alignment(self) -> Qt.Alignment """
        pass

    def backgroundBrush(self): # real signature unknown; restored from __doc__
        """ backgroundBrush(self) -> QBrush """
        pass

    def cacheMode(self): # real signature unknown; restored from __doc__
        """ cacheMode(self) -> QGraphicsView.CacheMode """
        pass

    def centerOn(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        centerOn(self, Union[QPointF, QPoint])
        centerOn(self, QGraphicsItem)
        centerOn(self, float, float)
        """
        pass

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, QContextMenuEvent): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, QContextMenuEvent) """
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dragEnterEvent(self, QDragEnterEvent): # real signature unknown; restored from __doc__
        """ dragEnterEvent(self, QDragEnterEvent) """
        pass

    def dragLeaveEvent(self, QDragLeaveEvent): # real signature unknown; restored from __doc__
        """ dragLeaveEvent(self, QDragLeaveEvent) """
        pass

    def dragMode(self): # real signature unknown; restored from __doc__
        """ dragMode(self) -> QGraphicsView.DragMode """
        pass

    def dragMoveEvent(self, QDragMoveEvent): # real signature unknown; restored from __doc__
        """ dragMoveEvent(self, QDragMoveEvent) """
        pass

    def drawBackground(self, QPainter, QRectF): # real signature unknown; restored from __doc__
        """ drawBackground(self, QPainter, QRectF) """
        pass

    def drawForeground(self, QPainter, QRectF): # real signature unknown; restored from __doc__
        """ drawForeground(self, QPainter, QRectF) """
        pass

    def drawFrame(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, QDropEvent): # real signature unknown; restored from __doc__
        """ dropEvent(self, QDropEvent) """
        pass

    def ensureVisible(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        ensureVisible(self, QRectF, xMargin: int = 50, yMargin: int = 50)
        ensureVisible(self, QGraphicsItem, xMargin: int = 50, yMargin: int = 50)
        ensureVisible(self, float, float, float, float, xMargin: int = 50, yMargin: int = 50)
        """
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def eventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def fitInView(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        fitInView(self, QRectF, mode: Qt.AspectRatioMode = Qt.IgnoreAspectRatio)
        fitInView(self, QGraphicsItem, mode: Qt.AspectRatioMode = Qt.IgnoreAspectRatio)
        fitInView(self, float, float, float, float, mode: Qt.AspectRatioMode = Qt.IgnoreAspectRatio)
        """
        pass

    def focusInEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ focusInEvent(self, QFocusEvent) """
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, bool): # real signature unknown; restored from __doc__
        """ focusNextPrevChild(self, bool) -> bool """
        return False

    def focusOutEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, QFocusEvent) """
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def foregroundBrush(self): # real signature unknown; restored from __doc__
        """ foregroundBrush(self) -> QBrush """
        pass

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def initStyleOption(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, QInputMethodEvent): # real signature unknown; restored from __doc__
        """ inputMethodEvent(self, QInputMethodEvent) """
        pass

    def inputMethodQuery(self, Qt_InputMethodQuery): # real signature unknown; restored from __doc__
        """ inputMethodQuery(self, Qt.InputMethodQuery) -> Any """
        pass

    def invalidateScene(self, rect=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ invalidateScene(self, rect: QRectF = QRectF(), layers: Union[QGraphicsScene.SceneLayers, QGraphicsScene.SceneLayer] = QGraphicsScene.AllLayers) """
        pass

    def isInteractive(self): # real signature unknown; restored from __doc__
        """ isInteractive(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isTransformed(self): # real signature unknown; restored from __doc__
        """ isTransformed(self) -> bool """
        return False

    def itemAt(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        itemAt(self, QPoint) -> QGraphicsItem
        itemAt(self, int, int) -> QGraphicsItem
        """
        return QGraphicsItem

    def items(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        items(self) -> List[QGraphicsItem]
        items(self, QPoint) -> List[QGraphicsItem]
        items(self, int, int) -> List[QGraphicsItem]
        items(self, int, int, int, int, mode: Qt.ItemSelectionMode = Qt.IntersectsItemShape) -> List[QGraphicsItem]
        items(self, QRect, mode: Qt.ItemSelectionMode = Qt.IntersectsItemShape) -> List[QGraphicsItem]
        items(self, QPolygon, mode: Qt.ItemSelectionMode = Qt.IntersectsItemShape) -> List[QGraphicsItem]
        items(self, QPainterPath, mode: Qt.ItemSelectionMode = Qt.IntersectsItemShape) -> List[QGraphicsItem]
        """
        return []

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, QKeyEvent) """
        pass

    def keyReleaseEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, QKeyEvent) """
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mapFromScene(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mapFromScene(self, Union[QPointF, QPoint]) -> QPoint
        mapFromScene(self, QRectF) -> QPolygon
        mapFromScene(self, QPolygonF) -> QPolygon
        mapFromScene(self, QPainterPath) -> QPainterPath
        mapFromScene(self, float, float) -> QPoint
        mapFromScene(self, float, float, float, float) -> QPolygon
        """
        pass

    def mapToScene(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mapToScene(self, QPoint) -> QPointF
        mapToScene(self, QRect) -> QPolygonF
        mapToScene(self, QPolygon) -> QPolygonF
        mapToScene(self, QPainterPath) -> QPainterPath
        mapToScene(self, int, int) -> QPointF
        mapToScene(self, int, int, int, int) -> QPolygonF
        """
        pass

    def metric(self, *args, **kwargs): # real signature unknown
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

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def optimizationFlags(self): # real signature unknown; restored from __doc__
        """ optimizationFlags(self) -> QGraphicsView.OptimizationFlags """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ paintEvent(self, QPaintEvent) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def render(self, QPainter, target=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ render(self, QPainter, target: QRectF = QRectF(), source: QRect = QRect(), mode: Qt.AspectRatioMode = Qt.KeepAspectRatio) """
        pass

    def renderHints(self): # real signature unknown; restored from __doc__
        """ renderHints(self) -> QPainter.RenderHints """
        pass

    def resetCachedContent(self): # real signature unknown; restored from __doc__
        """ resetCachedContent(self) """
        pass

    def resetTransform(self): # real signature unknown; restored from __doc__
        """ resetTransform(self) """
        pass

    def resizeAnchor(self): # real signature unknown; restored from __doc__
        """ resizeAnchor(self) -> QGraphicsView.ViewportAnchor """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ resizeEvent(self, QResizeEvent) """
        pass

    def rotate(self, p_float): # real signature unknown; restored from __doc__
        """ rotate(self, float) """
        pass

    def rubberBandChanged(self, QRect, Union, QPointF=None, QPoint=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ rubberBandChanged(self, QRect, Union[QPointF, QPoint], Union[QPointF, QPoint]) [signal] """
        pass

    def rubberBandRect(self): # real signature unknown; restored from __doc__
        """ rubberBandRect(self) -> QRect """
        pass

    def rubberBandSelectionMode(self): # real signature unknown; restored from __doc__
        """ rubberBandSelectionMode(self) -> Qt.ItemSelectionMode """
        pass

    def scale(self, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ scale(self, float, float) """
        pass

    def scene(self): # real signature unknown; restored from __doc__
        """ scene(self) -> QGraphicsScene """
        return QGraphicsScene

    def sceneRect(self): # real signature unknown; restored from __doc__
        """ sceneRect(self) -> QRectF """
        pass

    def scrollContentsBy(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ scrollContentsBy(self, int, int) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAlignment(self, Union, Qt_Alignment=None, Qt_AlignmentFlag=None): # real signature unknown; restored from __doc__
        """ setAlignment(self, Union[Qt.Alignment, Qt.AlignmentFlag]) """
        pass

    def setBackgroundBrush(self, Union, QBrush=None, QColor=None, Qt_GlobalColor=None, QGradient=None): # real signature unknown; restored from __doc__
        """ setBackgroundBrush(self, Union[QBrush, QColor, Qt.GlobalColor, QGradient]) """
        pass

    def setCacheMode(self, Union, QGraphicsView_CacheMode=None, QGraphicsView_CacheModeFlag=None): # real signature unknown; restored from __doc__
        """ setCacheMode(self, Union[QGraphicsView.CacheMode, QGraphicsView.CacheModeFlag]) """
        pass

    def setDragMode(self, QGraphicsView_DragMode): # real signature unknown; restored from __doc__
        """ setDragMode(self, QGraphicsView.DragMode) """
        pass

    def setForegroundBrush(self, Union, QBrush=None, QColor=None, Qt_GlobalColor=None, QGradient=None): # real signature unknown; restored from __doc__
        """ setForegroundBrush(self, Union[QBrush, QColor, Qt.GlobalColor, QGradient]) """
        pass

    def setInteractive(self, bool): # real signature unknown; restored from __doc__
        """ setInteractive(self, bool) """
        pass

    def setOptimizationFlag(self, QGraphicsView_OptimizationFlag, enabled=True): # real signature unknown; restored from __doc__
        """ setOptimizationFlag(self, QGraphicsView.OptimizationFlag, enabled: bool = True) """
        pass

    def setOptimizationFlags(self, Union, QGraphicsView_OptimizationFlags=None, QGraphicsView_OptimizationFlag=None): # real signature unknown; restored from __doc__
        """ setOptimizationFlags(self, Union[QGraphicsView.OptimizationFlags, QGraphicsView.OptimizationFlag]) """
        pass

    def setRenderHint(self, QPainter_RenderHint, on=True): # real signature unknown; restored from __doc__
        """ setRenderHint(self, QPainter.RenderHint, on: bool = True) """
        pass

    def setRenderHints(self, Union, QPainter_RenderHints=None, QPainter_RenderHint=None): # real signature unknown; restored from __doc__
        """ setRenderHints(self, Union[QPainter.RenderHints, QPainter.RenderHint]) """
        pass

    def setResizeAnchor(self, QGraphicsView_ViewportAnchor): # real signature unknown; restored from __doc__
        """ setResizeAnchor(self, QGraphicsView.ViewportAnchor) """
        pass

    def setRubberBandSelectionMode(self, Qt_ItemSelectionMode): # real signature unknown; restored from __doc__
        """ setRubberBandSelectionMode(self, Qt.ItemSelectionMode) """
        pass

    def setScene(self, QGraphicsScene): # real signature unknown; restored from __doc__
        """ setScene(self, QGraphicsScene) """
        pass

    def setSceneRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setSceneRect(self, QRectF)
        setSceneRect(self, float, float, float, float)
        """
        pass

    def setTransform(self, QTransform, combine=False): # real signature unknown; restored from __doc__
        """ setTransform(self, QTransform, combine: bool = False) """
        pass

    def setTransformationAnchor(self, QGraphicsView_ViewportAnchor): # real signature unknown; restored from __doc__
        """ setTransformationAnchor(self, QGraphicsView.ViewportAnchor) """
        pass

    def setupViewport(self, QWidget): # real signature unknown; restored from __doc__
        """ setupViewport(self, QWidget) """
        pass

    def setViewportMargins(self, *args, **kwargs): # real signature unknown
        pass

    def setViewportUpdateMode(self, QGraphicsView_ViewportUpdateMode): # real signature unknown; restored from __doc__
        """ setViewportUpdateMode(self, QGraphicsView.ViewportUpdateMode) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def shear(self, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ shear(self, float, float) """
        pass

    def showEvent(self, QShowEvent): # real signature unknown; restored from __doc__
        """ showEvent(self, QShowEvent) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def transform(self): # real signature unknown; restored from __doc__
        """ transform(self) -> QTransform """
        pass

    def transformationAnchor(self): # real signature unknown; restored from __doc__
        """ transformationAnchor(self) -> QGraphicsView.ViewportAnchor """
        pass

    def translate(self, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ translate(self, float, float) """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def updateScene(self, Iterable, QRectF=None): # real signature unknown; restored from __doc__
        """ updateScene(self, Iterable[QRectF]) """
        pass

    def updateSceneRect(self, QRectF): # real signature unknown; restored from __doc__
        """ updateSceneRect(self, QRectF) """
        pass

    def viewportEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ viewportEvent(self, QEvent) -> bool """
        return False

    def viewportMargins(self, *args, **kwargs): # real signature unknown
        pass

    def viewportSizeHint(self, *args, **kwargs): # real signature unknown
        pass

    def viewportTransform(self): # real signature unknown; restored from __doc__
        """ viewportTransform(self) -> QTransform """
        pass

    def viewportUpdateMode(self): # real signature unknown; restored from __doc__
        """ viewportUpdateMode(self) -> QGraphicsView.ViewportUpdateMode """
        pass

    def wheelEvent(self, QWheelEvent): # real signature unknown; restored from __doc__
        """ wheelEvent(self, QWheelEvent) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AnchorUnderMouse = 2
    AnchorViewCenter = 1
    BoundingRectViewportUpdate = 4
    CacheBackground = 1
    CacheNone = 0
    DontAdjustForAntialiasing = 4
    DontClipPainter = 1
    DontSavePainterState = 2
    FullViewportUpdate = 0
    MinimalViewportUpdate = 1
    NoAnchor = 0
    NoDrag = 0
    NoViewportUpdate = 3
    RubberBandDrag = 2
    ScrollHandDrag = 1
    SmartViewportUpdate = 2


