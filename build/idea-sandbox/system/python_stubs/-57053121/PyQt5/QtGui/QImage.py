# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QPaintDevice import QPaintDevice

class QImage(QPaintDevice):
    """
    QImage()
    QImage(QSize, QImage.Format)
    QImage(int, int, QImage.Format)
    QImage(bytes, int, int, QImage.Format)
    QImage(sip.voidptr, int, int, QImage.Format)
    QImage(bytes, int, int, int, QImage.Format)
    QImage(sip.voidptr, int, int, int, QImage.Format)
    QImage(List[str])
    QImage(str, format: str = None)
    QImage(QImage)
    QImage(Any)
    """
    def allGray(self): # real signature unknown; restored from __doc__
        """ allGray(self) -> bool """
        return False

    def bitPlaneCount(self): # real signature unknown; restored from __doc__
        """ bitPlaneCount(self) -> int """
        return 0

    def bits(self): # real signature unknown; restored from __doc__
        """ bits(self) -> sip.voidptr """
        pass

    def byteCount(self): # real signature unknown; restored from __doc__
        """ byteCount(self) -> int """
        return 0

    def bytesPerLine(self): # real signature unknown; restored from __doc__
        """ bytesPerLine(self) -> int """
        return 0

    def cacheKey(self): # real signature unknown; restored from __doc__
        """ cacheKey(self) -> int """
        return 0

    def color(self, p_int): # real signature unknown; restored from __doc__
        """ color(self, int) -> int """
        return 0

    def colorCount(self): # real signature unknown; restored from __doc__
        """ colorCount(self) -> int """
        return 0

    def colorTable(self): # real signature unknown; restored from __doc__
        """ colorTable(self) -> List[int] """
        return []

    def constBits(self): # real signature unknown; restored from __doc__
        """ constBits(self) -> sip.voidptr """
        pass

    def constScanLine(self, p_int): # real signature unknown; restored from __doc__
        """ constScanLine(self, int) -> sip.voidptr """
        pass

    def convertToFormat(self, QImage_Format, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        convertToFormat(self, QImage.Format, flags: Union[Qt.ImageConversionFlags, Qt.ImageConversionFlag] = Qt.AutoColor) -> QImage
        convertToFormat(self, QImage.Format, Iterable[int], flags: Union[Qt.ImageConversionFlags, Qt.ImageConversionFlag] = Qt.AutoColor) -> QImage
        """
        pass

    def copy(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        copy(self, rect: QRect = QRect()) -> QImage
        copy(self, int, int, int, int) -> QImage
        """
        return QImage

    def createAlphaMask(self, flags, Qt_ImageConversionFlags=None, Qt_ImageConversionFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ createAlphaMask(self, flags: Union[Qt.ImageConversionFlags, Qt.ImageConversionFlag] = Qt.AutoColor) -> QImage """
        pass

    def createHeuristicMask(self, clipTight=True): # real signature unknown; restored from __doc__
        """ createHeuristicMask(self, clipTight: bool = True) -> QImage """
        return QImage

    def createMaskFromColor(self, p_int, mode=None): # real signature unknown; restored from __doc__
        """ createMaskFromColor(self, int, mode: Qt.MaskMode = Qt.MaskInColor) -> QImage """
        return QImage

    def depth(self): # real signature unknown; restored from __doc__
        """ depth(self) -> int """
        return 0

    def detach(self): # real signature unknown; restored from __doc__
        """ detach(self) """
        pass

    def devicePixelRatio(self): # real signature unknown; restored from __doc__
        """ devicePixelRatio(self) -> float """
        return 0.0

    def devType(self): # real signature unknown; restored from __doc__
        """ devType(self) -> int """
        return 0

    def dotsPerMeterX(self): # real signature unknown; restored from __doc__
        """ dotsPerMeterX(self) -> int """
        return 0

    def dotsPerMeterY(self): # real signature unknown; restored from __doc__
        """ dotsPerMeterY(self) -> int """
        return 0

    def fill(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        fill(self, Qt.GlobalColor)
        fill(self, Union[QColor, Qt.GlobalColor, QGradient])
        fill(self, int)
        """
        pass

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> QImage.Format """
        pass

    def fromData(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        fromData(bytes, format: str = None) -> QImage
        fromData(Union[QByteArray, bytes, bytearray], format: str = None) -> QImage
        """
        return QImage

    def hasAlphaChannel(self): # real signature unknown; restored from __doc__
        """ hasAlphaChannel(self) -> bool """
        return False

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> int """
        return 0

    def invertPixels(self, mode=None): # real signature unknown; restored from __doc__
        """ invertPixels(self, mode: QImage.InvertMode = QImage.InvertRgb) """
        pass

    def isDetached(self): # real signature unknown; restored from __doc__
        """ isDetached(self) -> bool """
        return False

    def isGrayscale(self): # real signature unknown; restored from __doc__
        """ isGrayscale(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def load(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        load(self, QIODevice, str) -> bool
        load(self, str, format: str = None) -> bool
        """
        return False

    def loadFromData(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        loadFromData(self, bytes, format: str = None) -> bool
        loadFromData(self, Union[QByteArray, bytes, bytearray], format: str = None) -> bool
        """
        return False

    def metric(self, QPaintDevice_PaintDeviceMetric): # real signature unknown; restored from __doc__
        """ metric(self, QPaintDevice.PaintDeviceMetric) -> int """
        return 0

    def mirrored(self, horizontal=False, vertical=True): # real signature unknown; restored from __doc__
        """ mirrored(self, horizontal: bool = False, vertical: bool = True) -> QImage """
        return QImage

    def offset(self): # real signature unknown; restored from __doc__
        """ offset(self) -> QPoint """
        pass

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ paintEngine(self) -> QPaintEngine """
        return QPaintEngine

    def pixel(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        pixel(self, QPoint) -> int
        pixel(self, int, int) -> int
        """
        return 0

    def pixelColor(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        pixelColor(self, int, int) -> QColor
        pixelColor(self, QPoint) -> QColor
        """
        return QColor

    def pixelFormat(self): # real signature unknown; restored from __doc__
        """ pixelFormat(self) -> QPixelFormat """
        return QPixelFormat

    def pixelIndex(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        pixelIndex(self, QPoint) -> int
        pixelIndex(self, int, int) -> int
        """
        return 0

    def rect(self): # real signature unknown; restored from __doc__
        """ rect(self) -> QRect """
        pass

    def reinterpretAsFormat(self, QImage_Format): # real signature unknown; restored from __doc__
        """ reinterpretAsFormat(self, QImage.Format) -> bool """
        return False

    def rgbSwapped(self): # real signature unknown; restored from __doc__
        """ rgbSwapped(self) -> QImage """
        return QImage

    def save(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        save(self, str, format: str = None, quality: int = -1) -> bool
        save(self, QIODevice, format: str = None, quality: int = -1) -> bool
        """
        return False

    def scaled(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        scaled(self, int, int, aspectRatioMode: Qt.AspectRatioMode = Qt.IgnoreAspectRatio, transformMode: Qt.TransformationMode = Qt.FastTransformation) -> QImage
        scaled(self, QSize, aspectRatioMode: Qt.AspectRatioMode = Qt.IgnoreAspectRatio, transformMode: Qt.TransformationMode = Qt.FastTransformation) -> QImage
        """
        return QImage

    def scaledToHeight(self, p_int, mode=None): # real signature unknown; restored from __doc__
        """ scaledToHeight(self, int, mode: Qt.TransformationMode = Qt.FastTransformation) -> QImage """
        return QImage

    def scaledToWidth(self, p_int, mode=None): # real signature unknown; restored from __doc__
        """ scaledToWidth(self, int, mode: Qt.TransformationMode = Qt.FastTransformation) -> QImage """
        return QImage

    def scanLine(self, p_int): # real signature unknown; restored from __doc__
        """ scanLine(self, int) -> sip.voidptr """
        pass

    def setColor(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ setColor(self, int, int) """
        pass

    def setColorCount(self, p_int): # real signature unknown; restored from __doc__
        """ setColorCount(self, int) """
        pass

    def setColorTable(self, Iterable, p_int=None): # real signature unknown; restored from __doc__
        """ setColorTable(self, Iterable[int]) """
        pass

    def setDevicePixelRatio(self, p_float): # real signature unknown; restored from __doc__
        """ setDevicePixelRatio(self, float) """
        pass

    def setDotsPerMeterX(self, p_int): # real signature unknown; restored from __doc__
        """ setDotsPerMeterX(self, int) """
        pass

    def setDotsPerMeterY(self, p_int): # real signature unknown; restored from __doc__
        """ setDotsPerMeterY(self, int) """
        pass

    def setOffset(self, QPoint): # real signature unknown; restored from __doc__
        """ setOffset(self, QPoint) """
        pass

    def setPixel(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setPixel(self, QPoint, int)
        setPixel(self, int, int, int)
        """
        pass

    def setPixelColor(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setPixelColor(self, int, int, Union[QColor, Qt.GlobalColor, QGradient])
        setPixelColor(self, QPoint, Union[QColor, Qt.GlobalColor, QGradient])
        """
        pass

    def setText(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ setText(self, str, str) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> QSize """
        pass

    def sizeInBytes(self): # real signature unknown; restored from __doc__
        """ sizeInBytes(self) -> int """
        return 0

    def smoothScaled(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ smoothScaled(self, int, int) -> QImage """
        return QImage

    def swap(self, QImage): # real signature unknown; restored from __doc__
        """ swap(self, QImage) """
        pass

    def text(self, key=''): # real signature unknown; restored from __doc__
        """ text(self, key: str = '') -> str """
        return ""

    def textKeys(self): # real signature unknown; restored from __doc__
        """ textKeys(self) -> List[str] """
        return []

    def toImageFormat(self, QPixelFormat): # real signature unknown; restored from __doc__
        """ toImageFormat(QPixelFormat) -> QImage.Format """
        pass

    def toPixelFormat(self, QImage_Format): # real signature unknown; restored from __doc__
        """ toPixelFormat(QImage.Format) -> QPixelFormat """
        return QPixelFormat

    def transformed(self, QTransform, mode=None): # real signature unknown; restored from __doc__
        """ transformed(self, QTransform, mode: Qt.TransformationMode = Qt.FastTransformation) -> QImage """
        return QImage

    def trueMatrix(self, QTransform, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ trueMatrix(QTransform, int, int) -> QTransform """
        return QTransform

    def valid(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        valid(self, QPoint) -> bool
        valid(self, int, int) -> bool
        """
        return False

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> int """
        return 0

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    Format_A2BGR30_Premultiplied = 20
    Format_A2RGB30_Premultiplied = 22
    Format_Alpha8 = 23
    Format_ARGB32 = 5
    Format_ARGB32_Premultiplied = 6
    Format_ARGB4444_Premultiplied = 15
    Format_ARGB6666_Premultiplied = 10
    Format_ARGB8555_Premultiplied = 12
    Format_ARGB8565_Premultiplied = 8
    Format_BGR30 = 19
    Format_Grayscale8 = 24
    Format_Indexed8 = 3
    Format_Invalid = 0
    Format_Mono = 1
    Format_MonoLSB = 2
    Format_RGB16 = 7
    Format_RGB30 = 21
    Format_RGB32 = 4
    Format_RGB444 = 14
    Format_RGB555 = 11
    Format_RGB666 = 9
    Format_RGB888 = 13
    Format_RGBA64 = 26
    Format_RGBA64_Premultiplied = 27
    Format_RGBA8888 = 17
    Format_RGBA8888_Premultiplied = 18
    Format_RGBX64 = 25
    Format_RGBX8888 = 16
    InvertRgb = 0
    InvertRgba = 1
    __hash__ = None


