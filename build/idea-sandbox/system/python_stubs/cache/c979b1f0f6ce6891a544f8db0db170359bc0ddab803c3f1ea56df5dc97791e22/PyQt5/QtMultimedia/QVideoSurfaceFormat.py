# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QVideoSurfaceFormat(__sip.simplewrapper):
    """
    QVideoSurfaceFormat()
    QVideoSurfaceFormat(QSize, QVideoFrame.PixelFormat, type: QAbstractVideoBuffer.HandleType = QAbstractVideoBuffer.NoHandle)
    QVideoSurfaceFormat(QVideoSurfaceFormat)
    """
    def frameHeight(self): # real signature unknown; restored from __doc__
        """ frameHeight(self) -> int """
        return 0

    def frameRate(self): # real signature unknown; restored from __doc__
        """ frameRate(self) -> float """
        return 0.0

    def frameSize(self): # real signature unknown; restored from __doc__
        """ frameSize(self) -> QSize """
        pass

    def frameWidth(self): # real signature unknown; restored from __doc__
        """ frameWidth(self) -> int """
        return 0

    def handleType(self): # real signature unknown; restored from __doc__
        """ handleType(self) -> QAbstractVideoBuffer.HandleType """
        pass

    def isMirrored(self): # real signature unknown; restored from __doc__
        """ isMirrored(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def pixelAspectRatio(self): # real signature unknown; restored from __doc__
        """ pixelAspectRatio(self) -> QSize """
        pass

    def pixelFormat(self): # real signature unknown; restored from __doc__
        """ pixelFormat(self) -> QVideoFrame.PixelFormat """
        pass

    def property(self, p_str): # real signature unknown; restored from __doc__
        """ property(self, str) -> Any """
        pass

    def propertyNames(self): # real signature unknown; restored from __doc__
        """ propertyNames(self) -> List[QByteArray] """
        return []

    def scanLineDirection(self): # real signature unknown; restored from __doc__
        """ scanLineDirection(self) -> QVideoSurfaceFormat.Direction """
        pass

    def setFrameRate(self, p_float): # real signature unknown; restored from __doc__
        """ setFrameRate(self, float) """
        pass

    def setFrameSize(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setFrameSize(self, QSize)
        setFrameSize(self, int, int)
        """
        pass

    def setMirrored(self, bool): # real signature unknown; restored from __doc__
        """ setMirrored(self, bool) """
        pass

    def setPixelAspectRatio(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setPixelAspectRatio(self, QSize)
        setPixelAspectRatio(self, int, int)
        """
        pass

    def setProperty(self, p_str, Any): # real signature unknown; restored from __doc__
        """ setProperty(self, str, Any) """
        pass

    def setScanLineDirection(self, QVideoSurfaceFormat_Direction): # real signature unknown; restored from __doc__
        """ setScanLineDirection(self, QVideoSurfaceFormat.Direction) """
        pass

    def setViewport(self, QRect): # real signature unknown; restored from __doc__
        """ setViewport(self, QRect) """
        pass

    def setYCbCrColorSpace(self, QVideoSurfaceFormat_YCbCrColorSpace): # real signature unknown; restored from __doc__
        """ setYCbCrColorSpace(self, QVideoSurfaceFormat.YCbCrColorSpace) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def viewport(self): # real signature unknown; restored from __doc__
        """ viewport(self) -> QRect """
        pass

    def yCbCrColorSpace(self): # real signature unknown; restored from __doc__
        """ yCbCrColorSpace(self) -> QVideoSurfaceFormat.YCbCrColorSpace """
        pass

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


    BottomToTop = 1
    TopToBottom = 0
    YCbCr_BT601 = 1
    YCbCr_BT709 = 2
    YCbCr_JPEG = 5
    YCbCr_Undefined = 0
    YCbCr_xvYCC601 = 3
    YCbCr_xvYCC709 = 4
    __hash__ = None


