# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QVideoFrame(__sip.simplewrapper):
    """
    QVideoFrame()
    QVideoFrame(QAbstractVideoBuffer, QSize, QVideoFrame.PixelFormat)
    QVideoFrame(int, QSize, int, QVideoFrame.PixelFormat)
    QVideoFrame(QImage)
    QVideoFrame(QVideoFrame)
    """
    def availableMetaData(self): # real signature unknown; restored from __doc__
        """ availableMetaData(self) -> Dict[str, Any] """
        return {}

    def bits(self, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        bits(self) -> sip.voidptr
        bits(self, int) -> sip.voidptr
        """
        pass

    def bytesPerLine(self, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        bytesPerLine(self) -> int
        bytesPerLine(self, int) -> int
        """
        return 0

    def endTime(self): # real signature unknown; restored from __doc__
        """ endTime(self) -> int """
        return 0

    def fieldType(self): # real signature unknown; restored from __doc__
        """ fieldType(self) -> QVideoFrame.FieldType """
        pass

    def handle(self): # real signature unknown; restored from __doc__
        """ handle(self) -> Any """
        pass

    def handleType(self): # real signature unknown; restored from __doc__
        """ handleType(self) -> QAbstractVideoBuffer.HandleType """
        pass

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> int """
        return 0

    def imageFormatFromPixelFormat(self, QVideoFrame_PixelFormat): # real signature unknown; restored from __doc__
        """ imageFormatFromPixelFormat(QVideoFrame.PixelFormat) -> QImage.Format """
        pass

    def isMapped(self): # real signature unknown; restored from __doc__
        """ isMapped(self) -> bool """
        return False

    def isReadable(self): # real signature unknown; restored from __doc__
        """ isReadable(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def isWritable(self): # real signature unknown; restored from __doc__
        """ isWritable(self) -> bool """
        return False

    def map(self, QAbstractVideoBuffer_MapMode): # real signature unknown; restored from __doc__
        """ map(self, QAbstractVideoBuffer.MapMode) -> bool """
        return False

    def mapMode(self): # real signature unknown; restored from __doc__
        """ mapMode(self) -> QAbstractVideoBuffer.MapMode """
        pass

    def mappedBytes(self): # real signature unknown; restored from __doc__
        """ mappedBytes(self) -> int """
        return 0

    def metaData(self, p_str): # real signature unknown; restored from __doc__
        """ metaData(self, str) -> Any """
        pass

    def pixelFormat(self): # real signature unknown; restored from __doc__
        """ pixelFormat(self) -> QVideoFrame.PixelFormat """
        pass

    def pixelFormatFromImageFormat(self, QImage_Format): # real signature unknown; restored from __doc__
        """ pixelFormatFromImageFormat(QImage.Format) -> QVideoFrame.PixelFormat """
        pass

    def planeCount(self): # real signature unknown; restored from __doc__
        """ planeCount(self) -> int """
        return 0

    def setEndTime(self, p_int): # real signature unknown; restored from __doc__
        """ setEndTime(self, int) """
        pass

    def setFieldType(self, QVideoFrame_FieldType): # real signature unknown; restored from __doc__
        """ setFieldType(self, QVideoFrame.FieldType) """
        pass

    def setMetaData(self, p_str, Any): # real signature unknown; restored from __doc__
        """ setMetaData(self, str, Any) """
        pass

    def setStartTime(self, p_int): # real signature unknown; restored from __doc__
        """ setStartTime(self, int) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> QSize """
        pass

    def startTime(self): # real signature unknown; restored from __doc__
        """ startTime(self) -> int """
        return 0

    def unmap(self): # real signature unknown; restored from __doc__
        """ unmap(self) """
        pass

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

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    BottomField = 2
    Format_AdobeDng = 32
    Format_ARGB32 = 1
    Format_ARGB32_Premultiplied = 2
    Format_ARGB8565_Premultiplied = 7
    Format_AYUV444 = 15
    Format_AYUV444_Premultiplied = 16
    Format_BGR24 = 11
    Format_BGR32 = 10
    Format_BGR555 = 13
    Format_BGR565 = 12
    Format_BGRA32 = 8
    Format_BGRA32_Premultiplied = 9
    Format_BGRA5658_Premultiplied = 14
    Format_CameraRaw = 31
    Format_IMC1 = 24
    Format_IMC2 = 25
    Format_IMC3 = 26
    Format_IMC4 = 27
    Format_Invalid = 0
    Format_Jpeg = 30
    Format_NV12 = 22
    Format_NV21 = 23
    Format_RGB24 = 4
    Format_RGB32 = 3
    Format_RGB555 = 6
    Format_RGB565 = 5
    Format_User = 1000
    Format_UYVY = 20
    Format_Y16 = 29
    Format_Y8 = 28
    Format_YUV420P = 18
    Format_YUV444 = 17
    Format_YUYV = 21
    Format_YV12 = 19
    InterlacedFrame = 3
    ProgressiveFrame = 0
    TopField = 1
    __hash__ = None


