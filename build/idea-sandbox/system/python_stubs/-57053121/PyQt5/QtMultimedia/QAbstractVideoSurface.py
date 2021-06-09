# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QAbstractVideoSurface(__PyQt5_QtCore.QObject):
    """ QAbstractVideoSurface(parent: QObject = None) """
    def activeChanged(self, bool): # real signature unknown; restored from __doc__
        """ activeChanged(self, bool) [signal] """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> QAbstractVideoSurface.Error """
        pass

    def isActive(self): # real signature unknown; restored from __doc__
        """ isActive(self) -> bool """
        return False

    def isFormatSupported(self, QVideoSurfaceFormat): # real signature unknown; restored from __doc__
        """ isFormatSupported(self, QVideoSurfaceFormat) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def nativeResolution(self): # real signature unknown; restored from __doc__
        """ nativeResolution(self) -> QSize """
        pass

    def nativeResolutionChanged(self, QSize): # real signature unknown; restored from __doc__
        """ nativeResolutionChanged(self, QSize) [signal] """
        pass

    def nearestFormat(self, QVideoSurfaceFormat): # real signature unknown; restored from __doc__
        """ nearestFormat(self, QVideoSurfaceFormat) -> QVideoSurfaceFormat """
        return QVideoSurfaceFormat

    def present(self, QVideoFrame): # real signature unknown; restored from __doc__
        """ present(self, QVideoFrame) -> bool """
        return False

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setError(self, QAbstractVideoSurface_Error): # real signature unknown; restored from __doc__
        """ setError(self, QAbstractVideoSurface.Error) """
        pass

    def setNativeResolution(self, QSize): # real signature unknown; restored from __doc__
        """ setNativeResolution(self, QSize) """
        pass

    def start(self, QVideoSurfaceFormat): # real signature unknown; restored from __doc__
        """ start(self, QVideoSurfaceFormat) -> bool """
        return False

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) """
        pass

    def supportedFormatsChanged(self): # real signature unknown; restored from __doc__
        """ supportedFormatsChanged(self) [signal] """
        pass

    def supportedPixelFormats(self, type=None): # real signature unknown; restored from __doc__
        """ supportedPixelFormats(self, type: QAbstractVideoBuffer.HandleType = QAbstractVideoBuffer.NoHandle) -> List[QVideoFrame.PixelFormat] """
        return []

    def surfaceFormat(self): # real signature unknown; restored from __doc__
        """ surfaceFormat(self) -> QVideoSurfaceFormat """
        return QVideoSurfaceFormat

    def surfaceFormatChanged(self, QVideoSurfaceFormat): # real signature unknown; restored from __doc__
        """ surfaceFormatChanged(self, QVideoSurfaceFormat) [signal] """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    IncorrectFormatError = 2
    NoError = 0
    ResourceError = 4
    StoppedError = 3
    UnsupportedFormatError = 1


