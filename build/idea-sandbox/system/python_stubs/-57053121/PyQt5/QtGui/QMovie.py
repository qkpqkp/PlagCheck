# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QMovie(__PyQt5_QtCore.QObject):
    """
    QMovie(parent: QObject = None)
    QMovie(QIODevice, format: Union[QByteArray, bytes, bytearray] = QByteArray(), parent: QObject = None)
    QMovie(str, format: Union[QByteArray, bytes, bytearray] = QByteArray(), parent: QObject = None)
    """
    def backgroundColor(self): # real signature unknown; restored from __doc__
        """ backgroundColor(self) -> QColor """
        return QColor

    def cacheMode(self): # real signature unknown; restored from __doc__
        """ cacheMode(self) -> QMovie.CacheMode """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def currentFrameNumber(self): # real signature unknown; restored from __doc__
        """ currentFrameNumber(self) -> int """
        return 0

    def currentImage(self): # real signature unknown; restored from __doc__
        """ currentImage(self) -> QImage """
        return QImage

    def currentPixmap(self): # real signature unknown; restored from __doc__
        """ currentPixmap(self) -> QPixmap """
        return QPixmap

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> QIODevice """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, QImageReader_ImageReaderError): # real signature unknown; restored from __doc__
        """ error(self, QImageReader.ImageReaderError) [signal] """
        pass

    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def finished(self): # real signature unknown; restored from __doc__
        """ finished(self) [signal] """
        pass

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> QByteArray """
        pass

    def frameChanged(self, p_int): # real signature unknown; restored from __doc__
        """ frameChanged(self, int) [signal] """
        pass

    def frameCount(self): # real signature unknown; restored from __doc__
        """ frameCount(self) -> int """
        return 0

    def frameRect(self): # real signature unknown; restored from __doc__
        """ frameRect(self) -> QRect """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def jumpToFrame(self, p_int): # real signature unknown; restored from __doc__
        """ jumpToFrame(self, int) -> bool """
        return False

    def jumpToNextFrame(self): # real signature unknown; restored from __doc__
        """ jumpToNextFrame(self) -> bool """
        return False

    def lastError(self): # real signature unknown; restored from __doc__
        """ lastError(self) -> QImageReader.ImageReaderError """
        pass

    def lastErrorString(self): # real signature unknown; restored from __doc__
        """ lastErrorString(self) -> str """
        return ""

    def loopCount(self): # real signature unknown; restored from __doc__
        """ loopCount(self) -> int """
        return 0

    def nextFrameDelay(self): # real signature unknown; restored from __doc__
        """ nextFrameDelay(self) -> int """
        return 0

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resized(self, QSize): # real signature unknown; restored from __doc__
        """ resized(self, QSize) [signal] """
        pass

    def scaledSize(self): # real signature unknown; restored from __doc__
        """ scaledSize(self) -> QSize """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setBackgroundColor(self, Union, QColor=None, Qt_GlobalColor=None, QGradient=None): # real signature unknown; restored from __doc__
        """ setBackgroundColor(self, Union[QColor, Qt.GlobalColor, QGradient]) """
        pass

    def setCacheMode(self, QMovie_CacheMode): # real signature unknown; restored from __doc__
        """ setCacheMode(self, QMovie.CacheMode) """
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

    def setPaused(self, bool): # real signature unknown; restored from __doc__
        """ setPaused(self, bool) """
        pass

    def setScaledSize(self, QSize): # real signature unknown; restored from __doc__
        """ setScaledSize(self, QSize) """
        pass

    def setSpeed(self, p_int): # real signature unknown; restored from __doc__
        """ setSpeed(self, int) """
        pass

    def speed(self): # real signature unknown; restored from __doc__
        """ speed(self) -> int """
        return 0

    def start(self): # real signature unknown; restored from __doc__
        """ start(self) """
        pass

    def started(self): # real signature unknown; restored from __doc__
        """ started(self) [signal] """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QMovie.MovieState """
        pass

    def stateChanged(self, QMovie_MovieState): # real signature unknown; restored from __doc__
        """ stateChanged(self, QMovie.MovieState) [signal] """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) """
        pass

    def supportedFormats(self): # real signature unknown; restored from __doc__
        """ supportedFormats() -> List[QByteArray] """
        return []

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updated(self, QRect): # real signature unknown; restored from __doc__
        """ updated(self, QRect) [signal] """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    CacheAll = 1
    CacheNone = 0
    NotRunning = 0
    Paused = 1
    Running = 2


