# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QPaintDevice import QPaintDevice

class QPixmap(QPaintDevice):
    """
    QPixmap()
    QPixmap(int, int)
    QPixmap(QSize)
    QPixmap(str, format: str = None, flags: Union[Qt.ImageConversionFlags, Qt.ImageConversionFlag] = Qt.AutoColor)
    QPixmap(List[str])
    QPixmap(QPixmap)
    QPixmap(Any)
    """
    def cacheKey(self): # real signature unknown; restored from __doc__
        """ cacheKey(self) -> int """
        return 0

    def convertFromImage(self, QImage, flags, Qt_ImageConversionFlags=None, Qt_ImageConversionFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ convertFromImage(self, QImage, flags: Union[Qt.ImageConversionFlags, Qt.ImageConversionFlag] = Qt.AutoColor) -> bool """
        pass

    def copy(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        copy(self, rect: QRect = QRect()) -> QPixmap
        copy(self, int, int, int, int) -> QPixmap
        """
        return QPixmap

    def createHeuristicMask(self, clipTight=True): # real signature unknown; restored from __doc__
        """ createHeuristicMask(self, clipTight: bool = True) -> QBitmap """
        return QBitmap

    def createMaskFromColor(self, Union, QColor=None, Qt_GlobalColor=None, QGradient=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ createMaskFromColor(self, Union[QColor, Qt.GlobalColor, QGradient], mode: Qt.MaskMode = Qt.MaskInColor) -> QBitmap """
        pass

    def defaultDepth(self): # real signature unknown; restored from __doc__
        """ defaultDepth() -> int """
        return 0

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

    def fill(self, color, QColor=None, Qt_GlobalColor=None, QGradient=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ fill(self, color: Union[QColor, Qt.GlobalColor, QGradient] = Qt.white) """
        pass

    def fromImage(self, QImage, flags, Qt_ImageConversionFlags=None, Qt_ImageConversionFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ fromImage(QImage, flags: Union[Qt.ImageConversionFlags, Qt.ImageConversionFlag] = Qt.AutoColor) -> QPixmap """
        pass

    def fromImageReader(self, QImageReader, flags, Qt_ImageConversionFlags=None, Qt_ImageConversionFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ fromImageReader(QImageReader, flags: Union[Qt.ImageConversionFlags, Qt.ImageConversionFlag] = Qt.AutoColor) -> QPixmap """
        pass

    def hasAlpha(self): # real signature unknown; restored from __doc__
        """ hasAlpha(self) -> bool """
        return False

    def hasAlphaChannel(self): # real signature unknown; restored from __doc__
        """ hasAlphaChannel(self) -> bool """
        return False

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> int """
        return 0

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isQBitmap(self): # real signature unknown; restored from __doc__
        """ isQBitmap(self) -> bool """
        return False

    def load(self, p_str, format=None, flags, Qt_ImageConversionFlags=None, Qt_ImageConversionFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ load(self, str, format: str = None, flags: Union[Qt.ImageConversionFlags, Qt.ImageConversionFlag] = Qt.AutoColor) -> bool """
        pass

    def loadFromData(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        loadFromData(self, bytes, format: str = None, flags: Union[Qt.ImageConversionFlags, Qt.ImageConversionFlag] = Qt.AutoColor) -> bool
        loadFromData(self, Union[QByteArray, bytes, bytearray], format: str = None, flags: Union[Qt.ImageConversionFlags, Qt.ImageConversionFlag] = Qt.AutoColor) -> bool
        """
        pass

    def mask(self): # real signature unknown; restored from __doc__
        """ mask(self) -> QBitmap """
        return QBitmap

    def metric(self, QPaintDevice_PaintDeviceMetric): # real signature unknown; restored from __doc__
        """ metric(self, QPaintDevice.PaintDeviceMetric) -> int """
        return 0

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ paintEngine(self) -> QPaintEngine """
        return QPaintEngine

    def rect(self): # real signature unknown; restored from __doc__
        """ rect(self) -> QRect """
        pass

    def save(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        save(self, str, format: str = None, quality: int = -1) -> bool
        save(self, QIODevice, format: str = None, quality: int = -1) -> bool
        """
        return False

    def scaled(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        scaled(self, int, int, aspectRatioMode: Qt.AspectRatioMode = Qt.IgnoreAspectRatio, transformMode: Qt.TransformationMode = Qt.FastTransformation) -> QPixmap
        scaled(self, QSize, aspectRatioMode: Qt.AspectRatioMode = Qt.IgnoreAspectRatio, transformMode: Qt.TransformationMode = Qt.FastTransformation) -> QPixmap
        """
        return QPixmap

    def scaledToHeight(self, p_int, mode=None): # real signature unknown; restored from __doc__
        """ scaledToHeight(self, int, mode: Qt.TransformationMode = Qt.FastTransformation) -> QPixmap """
        return QPixmap

    def scaledToWidth(self, p_int, mode=None): # real signature unknown; restored from __doc__
        """ scaledToWidth(self, int, mode: Qt.TransformationMode = Qt.FastTransformation) -> QPixmap """
        return QPixmap

    def scroll(self, p_int, p_int_1, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        scroll(self, int, int, QRect) -> QRegion
        scroll(self, int, int, int, int, int, int) -> QRegion
        """
        return QRegion

    def setDevicePixelRatio(self, p_float): # real signature unknown; restored from __doc__
        """ setDevicePixelRatio(self, float) """
        pass

    def setMask(self, QBitmap): # real signature unknown; restored from __doc__
        """ setMask(self, QBitmap) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> QSize """
        pass

    def swap(self, QPixmap): # real signature unknown; restored from __doc__
        """ swap(self, QPixmap) """
        pass

    def toImage(self): # real signature unknown; restored from __doc__
        """ toImage(self) -> QImage """
        return QImage

    def transformed(self, QTransform, mode=None): # real signature unknown; restored from __doc__
        """ transformed(self, QTransform, mode: Qt.TransformationMode = Qt.FastTransformation) -> QPixmap """
        return QPixmap

    def trueMatrix(self, QTransform, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ trueMatrix(QTransform, int, int) -> QTransform """
        return QTransform

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


