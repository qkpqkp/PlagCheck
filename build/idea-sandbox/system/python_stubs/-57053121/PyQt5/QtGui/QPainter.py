# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QPainter(__sip.simplewrapper):
    """
    QPainter()
    QPainter(QPaintDevice)
    """
    def background(self): # real signature unknown; restored from __doc__
        """ background(self) -> QBrush """
        return QBrush

    def backgroundMode(self): # real signature unknown; restored from __doc__
        """ backgroundMode(self) -> Qt.BGMode """
        pass

    def begin(self, QPaintDevice): # real signature unknown; restored from __doc__
        """ begin(self, QPaintDevice) -> bool """
        return False

    def beginNativePainting(self): # real signature unknown; restored from __doc__
        """ beginNativePainting(self) """
        pass

    def boundingRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        boundingRect(self, QRectF, int, str) -> QRectF
        boundingRect(self, QRect, int, str) -> QRect
        boundingRect(self, QRectF, str, option: QTextOption = QTextOption()) -> QRectF
        boundingRect(self, int, int, int, int, int, str) -> QRect
        """
        pass

    def brush(self): # real signature unknown; restored from __doc__
        """ brush(self) -> QBrush """
        return QBrush

    def brushOrigin(self): # real signature unknown; restored from __doc__
        """ brushOrigin(self) -> QPoint """
        pass

    def clipBoundingRect(self): # real signature unknown; restored from __doc__
        """ clipBoundingRect(self) -> QRectF """
        pass

    def clipPath(self): # real signature unknown; restored from __doc__
        """ clipPath(self) -> QPainterPath """
        return QPainterPath

    def clipRegion(self): # real signature unknown; restored from __doc__
        """ clipRegion(self) -> QRegion """
        return QRegion

    def combinedTransform(self): # real signature unknown; restored from __doc__
        """ combinedTransform(self) -> QTransform """
        return QTransform

    def compositionMode(self): # real signature unknown; restored from __doc__
        """ compositionMode(self) -> QPainter.CompositionMode """
        pass

    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> QPaintDevice """
        return QPaintDevice

    def deviceTransform(self): # real signature unknown; restored from __doc__
        """ deviceTransform(self) -> QTransform """
        return QTransform

    def drawArc(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawArc(self, QRectF, int, int)
        drawArc(self, QRect, int, int)
        drawArc(self, int, int, int, int, int, int)
        """
        pass

    def drawChord(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawChord(self, QRectF, int, int)
        drawChord(self, QRect, int, int)
        drawChord(self, int, int, int, int, int, int)
        """
        pass

    def drawConvexPolygon(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawConvexPolygon(self, Union[QPointF, QPoint], *)
        drawConvexPolygon(self, QPolygonF)
        drawConvexPolygon(self, QPoint, *)
        drawConvexPolygon(self, QPolygon)
        """
        pass

    def drawEllipse(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawEllipse(self, QRectF)
        drawEllipse(self, QRect)
        drawEllipse(self, int, int, int, int)
        drawEllipse(self, Union[QPointF, QPoint], float, float)
        drawEllipse(self, QPoint, int, int)
        """
        pass

    def drawGlyphRun(self, Union, QPointF=None, QPoint=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ drawGlyphRun(self, Union[QPointF, QPoint], QGlyphRun) """
        pass

    def drawImage(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawImage(self, QRectF, QImage, QRectF, flags: Union[Qt.ImageConversionFlags, Qt.ImageConversionFlag] = Qt.AutoColor)
        drawImage(self, QRect, QImage, QRect, flags: Union[Qt.ImageConversionFlags, Qt.ImageConversionFlag] = Qt.AutoColor)
        drawImage(self, Union[QPointF, QPoint], QImage, QRectF, flags: Union[Qt.ImageConversionFlags, Qt.ImageConversionFlag] = Qt.AutoColor)
        drawImage(self, QPoint, QImage, QRect, flags: Union[Qt.ImageConversionFlags, Qt.ImageConversionFlag] = Qt.AutoColor)
        drawImage(self, QRectF, QImage)
        drawImage(self, QRect, QImage)
        drawImage(self, Union[QPointF, QPoint], QImage)
        drawImage(self, QPoint, QImage)
        drawImage(self, int, int, QImage, sx: int = 0, sy: int = 0, sw: int = -1, sh: int = -1, flags: Union[Qt.ImageConversionFlags, Qt.ImageConversionFlag] = Qt.AutoColor)
        """
        pass

    def drawLine(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawLine(self, QLineF)
        drawLine(self, QLine)
        drawLine(self, int, int, int, int)
        drawLine(self, QPoint, QPoint)
        drawLine(self, Union[QPointF, QPoint], Union[QPointF, QPoint])
        """
        pass

    def drawLines(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawLines(self, QLineF, *)
        drawLines(self, Iterable[QLineF])
        drawLines(self, Union[QPointF, QPoint], *)
        drawLines(self, Iterable[Union[QPointF, QPoint]])
        drawLines(self, QLine, *)
        drawLines(self, Iterable[QLine])
        drawLines(self, QPoint, *)
        drawLines(self, Iterable[QPoint])
        """
        pass

    def drawPath(self, QPainterPath): # real signature unknown; restored from __doc__
        """ drawPath(self, QPainterPath) """
        pass

    def drawPicture(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawPicture(self, Union[QPointF, QPoint], QPicture)
        drawPicture(self, int, int, QPicture)
        drawPicture(self, QPoint, QPicture)
        """
        pass

    def drawPie(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawPie(self, QRectF, int, int)
        drawPie(self, QRect, int, int)
        drawPie(self, int, int, int, int, int, int)
        """
        pass

    def drawPixmap(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawPixmap(self, QRectF, QPixmap, QRectF)
        drawPixmap(self, QRect, QPixmap, QRect)
        drawPixmap(self, Union[QPointF, QPoint], QPixmap)
        drawPixmap(self, QPoint, QPixmap)
        drawPixmap(self, QRect, QPixmap)
        drawPixmap(self, int, int, QPixmap)
        drawPixmap(self, int, int, int, int, QPixmap)
        drawPixmap(self, int, int, int, int, QPixmap, int, int, int, int)
        drawPixmap(self, int, int, QPixmap, int, int, int, int)
        drawPixmap(self, Union[QPointF, QPoint], QPixmap, QRectF)
        drawPixmap(self, QPoint, QPixmap, QRect)
        """
        pass

    def drawPixmapFragments(self, List, QPainter_PixmapFragment=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ drawPixmapFragments(self, List[QPainter.PixmapFragment], QPixmap, hints: QPainter.PixmapFragmentHints = 0) """
        pass

    def drawPoint(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawPoint(self, Union[QPointF, QPoint])
        drawPoint(self, int, int)
        drawPoint(self, QPoint)
        """
        pass

    def drawPoints(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawPoints(self, Union[QPointF, QPoint], *)
        drawPoints(self, QPolygonF)
        drawPoints(self, QPoint, *)
        drawPoints(self, QPolygon)
        """
        pass

    def drawPolygon(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawPolygon(self, Union[QPointF, QPoint], *)
        drawPolygon(self, QPolygonF, fillRule: Qt.FillRule = Qt.OddEvenFill)
        drawPolygon(self, QPoint, *)
        drawPolygon(self, QPolygon, fillRule: Qt.FillRule = Qt.OddEvenFill)
        """
        pass

    def drawPolyline(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawPolyline(self, Union[QPointF, QPoint], *)
        drawPolyline(self, QPolygonF)
        drawPolyline(self, QPoint, *)
        drawPolyline(self, QPolygon)
        """
        pass

    def drawRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawRect(self, QRectF)
        drawRect(self, int, int, int, int)
        drawRect(self, QRect)
        """
        pass

    def drawRects(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawRects(self, QRectF, *)
        drawRects(self, Iterable[QRectF])
        drawRects(self, QRect, *)
        drawRects(self, Iterable[QRect])
        """
        pass

    def drawRoundedRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawRoundedRect(self, QRectF, float, float, mode: Qt.SizeMode = Qt.AbsoluteSize)
        drawRoundedRect(self, int, int, int, int, float, float, mode: Qt.SizeMode = Qt.AbsoluteSize)
        drawRoundedRect(self, QRect, float, float, mode: Qt.SizeMode = Qt.AbsoluteSize)
        """
        pass

    def drawStaticText(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawStaticText(self, Union[QPointF, QPoint], QStaticText)
        drawStaticText(self, QPoint, QStaticText)
        drawStaticText(self, int, int, QStaticText)
        """
        pass

    def drawText(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawText(self, Union[QPointF, QPoint], str)
        drawText(self, QRectF, int, str) -> QRectF
        drawText(self, QRect, int, str) -> QRect
        drawText(self, QRectF, str, option: QTextOption = QTextOption())
        drawText(self, QPoint, str)
        drawText(self, int, int, int, int, int, str) -> QRect
        drawText(self, int, int, str)
        """
        pass

    def drawTiledPixmap(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawTiledPixmap(self, QRectF, QPixmap, pos: Union[QPointF, QPoint] = QPointF())
        drawTiledPixmap(self, QRect, QPixmap, pos: QPoint = QPoint())
        drawTiledPixmap(self, int, int, int, int, QPixmap, sx: int = 0, sy: int = 0)
        """
        pass

    def end(self): # real signature unknown; restored from __doc__
        """ end(self) -> bool """
        return False

    def endNativePainting(self): # real signature unknown; restored from __doc__
        """ endNativePainting(self) """
        pass

    def eraseRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        eraseRect(self, QRectF)
        eraseRect(self, QRect)
        eraseRect(self, int, int, int, int)
        """
        pass

    def fillPath(self, QPainterPath, Union, QBrush=None, QColor=None, Qt_GlobalColor=None, QGradient=None): # real signature unknown; restored from __doc__
        """ fillPath(self, QPainterPath, Union[QBrush, QColor, Qt.GlobalColor, QGradient]) """
        pass

    def fillRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        fillRect(self, QRectF, Union[QBrush, QColor, Qt.GlobalColor, QGradient])
        fillRect(self, QRect, Union[QBrush, QColor, Qt.GlobalColor, QGradient])
        fillRect(self, int, int, int, int, Union[QBrush, QColor, Qt.GlobalColor, QGradient])
        fillRect(self, QRectF, Union[QColor, Qt.GlobalColor, QGradient])
        fillRect(self, QRect, Union[QColor, Qt.GlobalColor, QGradient])
        fillRect(self, int, int, int, int, Union[QColor, Qt.GlobalColor, QGradient])
        fillRect(self, int, int, int, int, Qt.GlobalColor)
        fillRect(self, QRect, Qt.GlobalColor)
        fillRect(self, QRectF, Qt.GlobalColor)
        fillRect(self, int, int, int, int, Qt.BrushStyle)
        fillRect(self, QRect, Qt.BrushStyle)
        fillRect(self, QRectF, Qt.BrushStyle)
        fillRect(self, int, int, int, int, QGradient.Preset)
        fillRect(self, QRect, QGradient.Preset)
        fillRect(self, QRectF, QGradient.Preset)
        """
        pass

    def font(self): # real signature unknown; restored from __doc__
        """ font(self) -> QFont """
        return QFont

    def fontInfo(self): # real signature unknown; restored from __doc__
        """ fontInfo(self) -> QFontInfo """
        return QFontInfo

    def fontMetrics(self): # real signature unknown; restored from __doc__
        """ fontMetrics(self) -> QFontMetrics """
        return QFontMetrics

    def hasClipping(self): # real signature unknown; restored from __doc__
        """ hasClipping(self) -> bool """
        return False

    def isActive(self): # real signature unknown; restored from __doc__
        """ isActive(self) -> bool """
        return False

    def layoutDirection(self): # real signature unknown; restored from __doc__
        """ layoutDirection(self) -> Qt.LayoutDirection """
        pass

    def opacity(self): # real signature unknown; restored from __doc__
        """ opacity(self) -> float """
        return 0.0

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ paintEngine(self) -> QPaintEngine """
        return QPaintEngine

    def pen(self): # real signature unknown; restored from __doc__
        """ pen(self) -> QPen """
        return QPen

    def renderHints(self): # real signature unknown; restored from __doc__
        """ renderHints(self) -> QPainter.RenderHints """
        pass

    def resetTransform(self): # real signature unknown; restored from __doc__
        """ resetTransform(self) """
        pass

    def restore(self): # real signature unknown; restored from __doc__
        """ restore(self) """
        pass

    def rotate(self, p_float): # real signature unknown; restored from __doc__
        """ rotate(self, float) """
        pass

    def save(self): # real signature unknown; restored from __doc__
        """ save(self) """
        pass

    def scale(self, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ scale(self, float, float) """
        pass

    def setBackground(self, Union, QBrush=None, QColor=None, Qt_GlobalColor=None, QGradient=None): # real signature unknown; restored from __doc__
        """ setBackground(self, Union[QBrush, QColor, Qt.GlobalColor, QGradient]) """
        pass

    def setBackgroundMode(self, Qt_BGMode): # real signature unknown; restored from __doc__
        """ setBackgroundMode(self, Qt.BGMode) """
        pass

    def setBrush(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setBrush(self, Union[QBrush, QColor, Qt.GlobalColor, QGradient])
        setBrush(self, Qt.BrushStyle)
        """
        pass

    def setBrushOrigin(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setBrushOrigin(self, Union[QPointF, QPoint])
        setBrushOrigin(self, int, int)
        setBrushOrigin(self, QPoint)
        """
        pass

    def setClipPath(self, QPainterPath, operation=None): # real signature unknown; restored from __doc__
        """ setClipPath(self, QPainterPath, operation: Qt.ClipOperation = Qt.ReplaceClip) """
        pass

    def setClipping(self, bool): # real signature unknown; restored from __doc__
        """ setClipping(self, bool) """
        pass

    def setClipRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setClipRect(self, QRectF, operation: Qt.ClipOperation = Qt.ReplaceClip)
        setClipRect(self, int, int, int, int, operation: Qt.ClipOperation = Qt.ReplaceClip)
        setClipRect(self, QRect, operation: Qt.ClipOperation = Qt.ReplaceClip)
        """
        pass

    def setClipRegion(self, QRegion, operation=None): # real signature unknown; restored from __doc__
        """ setClipRegion(self, QRegion, operation: Qt.ClipOperation = Qt.ReplaceClip) """
        pass

    def setCompositionMode(self, QPainter_CompositionMode): # real signature unknown; restored from __doc__
        """ setCompositionMode(self, QPainter.CompositionMode) """
        pass

    def setFont(self, QFont): # real signature unknown; restored from __doc__
        """ setFont(self, QFont) """
        pass

    def setLayoutDirection(self, Qt_LayoutDirection): # real signature unknown; restored from __doc__
        """ setLayoutDirection(self, Qt.LayoutDirection) """
        pass

    def setOpacity(self, p_float): # real signature unknown; restored from __doc__
        """ setOpacity(self, float) """
        pass

    def setPen(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setPen(self, Union[QColor, Qt.GlobalColor, QGradient])
        setPen(self, Union[QPen, QColor, Qt.GlobalColor, QGradient])
        setPen(self, Qt.PenStyle)
        """
        pass

    def setRenderHint(self, QPainter_RenderHint, on=True): # real signature unknown; restored from __doc__
        """ setRenderHint(self, QPainter.RenderHint, on: bool = True) """
        pass

    def setRenderHints(self, Union, QPainter_RenderHints=None, QPainter_RenderHint=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setRenderHints(self, Union[QPainter.RenderHints, QPainter.RenderHint], on: bool = True) """
        pass

    def setTransform(self, QTransform, combine=False): # real signature unknown; restored from __doc__
        """ setTransform(self, QTransform, combine: bool = False) """
        pass

    def setViewport(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setViewport(self, QRect)
        setViewport(self, int, int, int, int)
        """
        pass

    def setViewTransformEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setViewTransformEnabled(self, bool) """
        pass

    def setWindow(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setWindow(self, QRect)
        setWindow(self, int, int, int, int)
        """
        pass

    def setWorldMatrixEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setWorldMatrixEnabled(self, bool) """
        pass

    def setWorldTransform(self, QTransform, combine=False): # real signature unknown; restored from __doc__
        """ setWorldTransform(self, QTransform, combine: bool = False) """
        pass

    def shear(self, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ shear(self, float, float) """
        pass

    def strokePath(self, QPainterPath, Union, QPen=None, QColor=None, Qt_GlobalColor=None, QGradient=None): # real signature unknown; restored from __doc__
        """ strokePath(self, QPainterPath, Union[QPen, QColor, Qt.GlobalColor, QGradient]) """
        pass

    def testRenderHint(self, QPainter_RenderHint): # real signature unknown; restored from __doc__
        """ testRenderHint(self, QPainter.RenderHint) -> bool """
        return False

    def transform(self): # real signature unknown; restored from __doc__
        """ transform(self) -> QTransform """
        return QTransform

    def translate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        translate(self, Union[QPointF, QPoint])
        translate(self, float, float)
        translate(self, QPoint)
        """
        pass

    def viewport(self): # real signature unknown; restored from __doc__
        """ viewport(self) -> QRect """
        pass

    def viewTransformEnabled(self): # real signature unknown; restored from __doc__
        """ viewTransformEnabled(self) -> bool """
        return False

    def window(self): # real signature unknown; restored from __doc__
        """ window(self) -> QRect """
        pass

    def worldMatrixEnabled(self): # real signature unknown; restored from __doc__
        """ worldMatrixEnabled(self) -> bool """
        return False

    def worldTransform(self): # real signature unknown; restored from __doc__
        """ worldTransform(self) -> QTransform """
        return QTransform

    def __enter__(self): # real signature unknown; restored from __doc__
        """ __enter__(self) -> object """
        return object()

    def __exit__(self, p_object, p_object_1, p_object_2): # real signature unknown; restored from __doc__
        """ __exit__(self, object, object, object) """
        pass

    def __init__(self, QPaintDevice=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Antialiasing = 1
    CompositionMode_Clear = 2
    CompositionMode_ColorBurn = 19
    CompositionMode_ColorDodge = 18
    CompositionMode_Darken = 16
    CompositionMode_Destination = 4
    CompositionMode_DestinationAtop = 10
    CompositionMode_DestinationIn = 6
    CompositionMode_DestinationOut = 8
    CompositionMode_DestinationOver = 1
    CompositionMode_Difference = 22
    CompositionMode_Exclusion = 23
    CompositionMode_HardLight = 20
    CompositionMode_Lighten = 17
    CompositionMode_Multiply = 13
    CompositionMode_Overlay = 15
    CompositionMode_Plus = 12
    CompositionMode_Screen = 14
    CompositionMode_SoftLight = 21
    CompositionMode_Source = 3
    CompositionMode_SourceAtop = 9
    CompositionMode_SourceIn = 5
    CompositionMode_SourceOut = 7
    CompositionMode_SourceOver = 0
    CompositionMode_Xor = 11
    HighQualityAntialiasing = 8
    NonCosmeticDefaultPen = 16
    OpaqueHint = 1
    Qt4CompatiblePainting = 32
    RasterOp_ClearDestination = 35
    RasterOp_NotDestination = 37
    RasterOp_NotSource = 30
    RasterOp_NotSourceAndDestination = 31
    RasterOp_NotSourceAndNotDestination = 27
    RasterOp_NotSourceOrDestination = 33
    RasterOp_NotSourceOrNotDestination = 28
    RasterOp_NotSourceXorDestination = 29
    RasterOp_SetDestination = 36
    RasterOp_SourceAndDestination = 25
    RasterOp_SourceAndNotDestination = 32
    RasterOp_SourceOrDestination = 24
    RasterOp_SourceOrNotDestination = 34
    RasterOp_SourceXorDestination = 26
    SmoothPixmapTransform = 4
    TextAntialiasing = 2


