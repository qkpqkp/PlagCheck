# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QImageWriter(__sip.simplewrapper):
    """
    QImageWriter()
    QImageWriter(QIODevice, Union[QByteArray, bytes, bytearray])
    QImageWriter(str, format: Union[QByteArray, bytes, bytearray] = QByteArray())
    """
    def canWrite(self): # real signature unknown; restored from __doc__
        """ canWrite(self) -> bool """
        return False

    def compression(self): # real signature unknown; restored from __doc__
        """ compression(self) -> int """
        return 0

    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> QIODevice """
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> QImageWriter.ImageWriterError """
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

    def imageFormatsForMimeType(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ imageFormatsForMimeType(Union[QByteArray, bytes, bytearray]) -> List[QByteArray] """
        return []

    def optimizedWrite(self): # real signature unknown; restored from __doc__
        """ optimizedWrite(self) -> bool """
        return False

    def progressiveScanWrite(self): # real signature unknown; restored from __doc__
        """ progressiveScanWrite(self) -> bool """
        return False

    def quality(self): # real signature unknown; restored from __doc__
        """ quality(self) -> int """
        return 0

    def setCompression(self, p_int): # real signature unknown; restored from __doc__
        """ setCompression(self, int) """
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

    def setOptimizedWrite(self, bool): # real signature unknown; restored from __doc__
        """ setOptimizedWrite(self, bool) """
        pass

    def setProgressiveScanWrite(self, bool): # real signature unknown; restored from __doc__
        """ setProgressiveScanWrite(self, bool) """
        pass

    def setQuality(self, p_int): # real signature unknown; restored from __doc__
        """ setQuality(self, int) """
        pass

    def setSubType(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setSubType(self, Union[QByteArray, bytes, bytearray]) """
        pass

    def setText(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ setText(self, str, str) """
        pass

    def setTransformation(self, Union, QImageIOHandler_Transformations=None, QImageIOHandler_Transformation=None): # real signature unknown; restored from __doc__
        """ setTransformation(self, Union[QImageIOHandler.Transformations, QImageIOHandler.Transformation]) """
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

    def supportsOption(self, QImageIOHandler_ImageOption): # real signature unknown; restored from __doc__
        """ supportsOption(self, QImageIOHandler.ImageOption) -> bool """
        return False

    def transformation(self): # real signature unknown; restored from __doc__
        """ transformation(self) -> QImageIOHandler.Transformations """
        pass

    def write(self, QImage): # real signature unknown; restored from __doc__
        """ write(self, QImage) -> bool """
        return False

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    DeviceError = 1
    InvalidImageError = 3
    UnknownError = 0
    UnsupportedFormatError = 2


