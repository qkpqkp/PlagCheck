# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QPaintEngine(__sip.simplewrapper):
    """ QPaintEngine(features: Union[QPaintEngine.PaintEngineFeatures, QPaintEngine.PaintEngineFeature] = QPaintEngine.PaintEngineFeatures()) """
    def begin(self, QPaintDevice): # real signature unknown; restored from __doc__
        """ begin(self, QPaintDevice) -> bool """
        return False

    def drawEllipse(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawEllipse(self, QRectF)
        drawEllipse(self, QRect)
        """
        pass

    def drawImage(self, QRectF, QImage, QRectF_1, flags, Qt_ImageConversionFlags=None, Qt_ImageConversionFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ drawImage(self, QRectF, QImage, QRectF, flags: Union[Qt.ImageConversionFlags, Qt.ImageConversionFlag] = Qt.AutoColor) """
        pass

    def drawLines(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawLines(self, QLine)
        drawLines(self, QLineF)
        """
        pass

    def drawPath(self, QPainterPath): # real signature unknown; restored from __doc__
        """ drawPath(self, QPainterPath) """
        pass

    def drawPixmap(self, QRectF, QPixmap, QRectF_1): # real signature unknown; restored from __doc__
        """ drawPixmap(self, QRectF, QPixmap, QRectF) """
        pass

    def drawPoints(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawPoints(self, Union[QPointF, QPoint])
        drawPoints(self, QPoint)
        """
        pass

    def drawPolygon(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawPolygon(self, Union[QPointF, QPoint], QPaintEngine.PolygonDrawMode)
        drawPolygon(self, QPoint, QPaintEngine.PolygonDrawMode)
        """
        pass

    def drawRects(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawRects(self, QRect)
        drawRects(self, QRectF)
        """
        pass

    def drawTextItem(self, Union, QPointF=None, QPoint=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ drawTextItem(self, Union[QPointF, QPoint], QTextItem) """
        pass

    def drawTiledPixmap(self, QRectF, QPixmap, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ drawTiledPixmap(self, QRectF, QPixmap, Union[QPointF, QPoint]) """
        pass

    def end(self): # real signature unknown; restored from __doc__
        """ end(self) -> bool """
        return False

    def hasFeature(self, Union, QPaintEngine_PaintEngineFeatures=None, QPaintEngine_PaintEngineFeature=None): # real signature unknown; restored from __doc__
        """ hasFeature(self, Union[QPaintEngine.PaintEngineFeatures, QPaintEngine.PaintEngineFeature]) -> bool """
        return False

    def isActive(self): # real signature unknown; restored from __doc__
        """ isActive(self) -> bool """
        return False

    def paintDevice(self): # real signature unknown; restored from __doc__
        """ paintDevice(self) -> QPaintDevice """
        return QPaintDevice

    def painter(self): # real signature unknown; restored from __doc__
        """ painter(self) -> QPainter """
        return QPainter

    def setActive(self, bool): # real signature unknown; restored from __doc__
        """ setActive(self, bool) """
        pass

    def setPaintDevice(self, QPaintDevice): # real signature unknown; restored from __doc__
        """ setPaintDevice(self, QPaintDevice) """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QPaintEngine.Type """
        pass

    def updateState(self, QPaintEngineState): # real signature unknown; restored from __doc__
        """ updateState(self, QPaintEngineState) """
        pass

    def __init__(self, features, QPaintEngine_PaintEngineFeatures=None, QPaintEngine_PaintEngineFeature=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AllDirty = 65535
    AllFeatures = -1
    AlphaBlend = 128
    Antialiasing = 1024
    BlendModes = 32768
    Blitter = 16
    BrushStroke = 2048
    ConicalGradientFill = 64
    ConstantOpacity = 4096
    ConvexMode = 2
    CoreGraphics = 3
    Direct2D = 17
    Direct3D = 11
    DirtyBackground = 16
    DirtyBackgroundMode = 32
    DirtyBrush = 2
    DirtyBrushOrigin = 4
    DirtyClipEnabled = 2048
    DirtyClipPath = 256
    DirtyClipRegion = 128
    DirtyCompositionMode = 1024
    DirtyFont = 8
    DirtyHints = 512
    DirtyOpacity = 4096
    DirtyPen = 1
    DirtyTransform = 64
    LinearGradientFill = 16
    MacPrinter = 4
    MaskedBrush = 8192
    MaxUser = 100
    ObjectBoundingModeGradients = 65536
    OddEvenMode = 0
    OpenGL = 7
    OpenGL2 = 14
    OpenVG = 13
    PaintBuffer = 15
    PainterPaths = 512
    PaintOutsidePaintEvent = 536870912
    PatternBrush = 8
    PatternTransform = 2
    Pdf = 12
    PerspectiveTransform = 16384
    Picture = 8
    PixmapTransform = 4
    PolylineMode = 3
    PorterDuff = 256
    PostScript = 6
    PrimitiveTransform = 1
    QuickDraw = 2
    QWindowSystem = 5
    RadialGradientFill = 32
    Raster = 10
    RasterOpModes = 131072
    SVG = 9
    User = 50
    WindingMode = 1
    Windows = 1
    X11 = 0


