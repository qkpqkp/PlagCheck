# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QImageReader(__sip.simplewrapper):
    """
    QImageReader()
    QImageReader(QIODevice, format: Union[QByteArray, bytes, bytearray] = QByteArray())
    QImageReader(str, format: Union[QByteArray, bytes, bytearray] = QByteArray())
    """
    def autoDetectImageFormat(self): # real signature unknown; restored from __doc__
        """ autoDetectImageFormat(self) -> bool """
        return False

    def autoTransform(self): # real signature unknown; restored from __doc__
        """ autoTransform(self) -> bool """
        return False

    def backgroundColor(self): # real signature unknown; restored from __doc__
        """ backgroundColor(self) -> QColor """
        return QColor

    def canRead(self): # real signature unknown; restored from __doc__
        """ canRead(self) -> bool """
        return False

    def clipRect(self): # real signature unknown; restored from __doc__
        """ clipRect(self) -> QRect """
        pass

    def currentImageNumber(self): # real signature unknown; restored from __doc__
        """ currentImageNumber(self) -> int """
        return 0

    def currentImageRect(self): # real signature unknown; restored from __doc__
        """ currentImageRect(self) -> QRect """
        pass

    def decideFormatFromContent(self): # real signature unknown; restored from __doc__
        """ decideFormatFromContent(self) -> bool """
        return False

    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> QIODevice """
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> QImageReader.ImageReaderError """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> QByteArray """
        pass

    def gamma(self): # real signature unknown; restored from __doc__
        """ gamma(self) -> float """
        return 0.0

    def imageCount(self): # real signature unknown; restored from __doc__
        """ imageCount(self) -> int """
        return 0

    def imageFormat(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        imageFormat(str) -> QByteArray
        imageFormat(QIODevice) -> QByteArray
        imageFormat(self) -> QImage.Format
        """
        pass

    def imageFormatsForMimeType(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ imageFormatsForMimeType(Union[QByteArray, bytes, bytearray]) -> List[QByteArray] """
        return []

    def jumpToImage(self, p_int): # real signature unknown; restored from __doc__
        """ jumpToImage(self, int) -> bool """
        return False

    def jumpToNextImage(self): # real signature unknown; restored from __doc__
        """ jumpToNextImage(self) -> bool """
        return False

    def loopCount(self): # real signature unknown; restored from __doc__
        """ loopCount(self) -> int """
        return 0

    def nextImageDelay(self): # real signature unknown; restored from __doc__
        """ nextImageDelay(self) -> int """
        return 0

    def quality(self): # real signature unknown; restored from __doc__
        """ quality(self) -> int """
        return 0

    def read(self, QImage=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        read(self) -> QImage
        read(self, QImage) -> bool
        """
        return QImage or False

    def scaledClipRect(self): # real signature unknown; restored from __doc__
        """ scaledClipRect(self) -> QRect """
        pass

    def scaledSize(self): # real signature unknown; restored from __doc__
        """ scaledSize(self) -> QSize """
        pass

    def setAutoDetectImageFormat(self, bool): # real signature unknown; restored from __doc__
        """ setAutoDetectImageFormat(self, bool) """
        pass

    def setAutoTransform(self, bool): # real signature unknown; restored from __doc__
        """ setAutoTransform(self, bool) """
        pass

    def setBackgroundColor(self, Union, QColor=None, Qt_GlobalColor=None, QGradient=None): # real signature unknown; restored from __doc__
        """ setBackgroundColor(self, Union[QColor, Qt.GlobalColor, QGradient]) """
        pass

    def setClipRect(self, QRect): # real signature unknown; restored from __doc__
        """ setClipRect(self, QRect) """
        pass

    def setDecideFormatFromContent(self, bool): # real signature unknown; restored from __doc__
        """ setDecideFormatFromContent(self, bool) """
        pass

    def setDevice(self, QIODevice): # real signature unknown; restored from __doc__
        """ setDevice(self, QIODevice) """
        pass

    def setFileName(self, p_str): # real signature unknown; restored from __doc__
        """ setFileName(self, str) """
        pass

    def setFormat(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setFormat(self, Union[QByteArray, bytes, bytearray]) """
        pass

    def setGamma(self, p_float): # real signature unknown; restored from __doc__
        """ setGamma(self, float) """
        pass

    def setQuality(self, p_int): # real signature unknown; restored from __doc__
        """ setQuality(self, int) """
        pass

    def setScaledClipRect(self, QRect): # real signature unknown; restored from __doc__
        """ setScaledClipRect(self, QRect) """
        pass

    def setScaledSize(self, QSize): # real signature unknown; restored from __doc__
        """ setScaledSize(self, QSize) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> QSize """
        pass

    def subType(self): # real signature unknown; restored from __doc__
        """ subType(self) -> QByteArray """
        pass

    def supportedImageFormats(self): # real signature unknown; restored from __doc__
        """ supportedImageFormats() -> List[QByteArray] """
        return []

    def supportedMimeTypes(self): # real signature unknown; restored from __doc__
        """ supportedMimeTypes() -> List[QByteArray] """
        return []

    def supportedSubTypes(self): # real signature unknown; restored from __doc__
        """ supportedSubTypes(self) -> List[QByteArray] """
        return []

    def supportsAnimation(self): # real signature unknown; restored from __doc__
        """ supportsAnimation(self) -> bool """
        return False

    def supportsOption(self, QImageIOHandler_ImageOption): # real signature unknown; restored from __doc__
        """ supportsOption(self, QImageIOHandler.ImageOption) -> bool """
        return False

    def text(self, p_str): # real signature unknown; restored from __doc__
        """ text(self, str) -> str """
        return ""

    def textKeys(self): # real signature unknown; restored from __doc__
        """ textKeys(self) -> List[str] """
        return []

    def transformation(self): # real signature unknown; restored from __doc__
        """ transformation(self) -> QImageIOHandler.Transformations """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    DeviceError = 2
    FileNotFoundError = 1
    InvalidDataError = 4
    UnknownError = 0
    UnsupportedFormatError = 3


