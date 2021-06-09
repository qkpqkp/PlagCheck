# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QMediaObject import QMediaObject

class QCamera(QMediaObject):
    """
    QCamera(parent: QObject = None)
    QCamera(Union[QByteArray, bytes, bytearray], parent: QObject = None)
    QCamera(QCameraInfo, parent: QObject = None)
    QCamera(QCamera.Position, parent: QObject = None)
    """
    def addPropertyWatch(self, *args, **kwargs): # real signature unknown
        pass

    def availability(self): # real signature unknown; restored from __doc__
        """ availability(self) -> QMultimedia.AvailabilityStatus """
        pass

    def availableDevices(self): # real signature unknown; restored from __doc__
        """ availableDevices() -> List[QByteArray] """
        return []

    def captureMode(self): # real signature unknown; restored from __doc__
        """ captureMode(self) -> QCamera.CaptureModes """
        pass

    def captureModeChanged(self, Union, QCamera_CaptureModes=None, QCamera_CaptureMode=None): # real signature unknown; restored from __doc__
        """ captureModeChanged(self, Union[QCamera.CaptureModes, QCamera.CaptureMode]) [signal] """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def deviceDescription(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ deviceDescription(Union[QByteArray, bytes, bytearray]) -> str """
        return ""

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, QCamera_Error=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        error(self) -> QCamera.Error
        error(self, QCamera.Error) [signal]
        """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def exposure(self): # real signature unknown; restored from __doc__
        """ exposure(self) -> QCameraExposure """
        return QCameraExposure

    def focus(self): # real signature unknown; restored from __doc__
        """ focus(self) -> QCameraFocus """
        return QCameraFocus

    def imageProcessing(self): # real signature unknown; restored from __doc__
        """ imageProcessing(self) -> QCameraImageProcessing """
        return QCameraImageProcessing

    def isCaptureModeSupported(self, Union, QCamera_CaptureModes=None, QCamera_CaptureMode=None): # real signature unknown; restored from __doc__
        """ isCaptureModeSupported(self, Union[QCamera.CaptureModes, QCamera.CaptureMode]) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def load(self): # real signature unknown; restored from __doc__
        """ load(self) """
        pass

    def locked(self): # real signature unknown; restored from __doc__
        """ locked(self) [signal] """
        pass

    def lockFailed(self): # real signature unknown; restored from __doc__
        """ lockFailed(self) [signal] """
        pass

    def lockStatus(self, QCamera_LockType=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        lockStatus(self) -> QCamera.LockStatus
        lockStatus(self, QCamera.LockType) -> QCamera.LockStatus
        """
        pass

    def lockStatusChanged(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        lockStatusChanged(self, QCamera.LockStatus, QCamera.LockChangeReason) [signal]
        lockStatusChanged(self, QCamera.LockType, QCamera.LockStatus, QCamera.LockChangeReason) [signal]
        """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removePropertyWatch(self, *args, **kwargs): # real signature unknown
        pass

    def requestedLocks(self): # real signature unknown; restored from __doc__
        """ requestedLocks(self) -> QCamera.LockTypes """
        pass

    def searchAndLock(self, Union=None, QCamera_LockTypes=None, QCamera_LockType=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        searchAndLock(self)
        searchAndLock(self, Union[QCamera.LockTypes, QCamera.LockType])
        """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCaptureMode(self, Union, QCamera_CaptureModes=None, QCamera_CaptureMode=None): # real signature unknown; restored from __doc__
        """ setCaptureMode(self, Union[QCamera.CaptureModes, QCamera.CaptureMode]) """
        pass

    def setViewfinder(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setViewfinder(self, QVideoWidget)
        setViewfinder(self, QGraphicsVideoItem)
        setViewfinder(self, QAbstractVideoSurface)
        """
        pass

    def setViewfinderSettings(self, QCameraViewfinderSettings): # real signature unknown; restored from __doc__
        """ setViewfinderSettings(self, QCameraViewfinderSettings) """
        pass

    def start(self): # real signature unknown; restored from __doc__
        """ start(self) """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QCamera.State """
        pass

    def stateChanged(self, QCamera_State): # real signature unknown; restored from __doc__
        """ stateChanged(self, QCamera.State) [signal] """
        pass

    def status(self): # real signature unknown; restored from __doc__
        """ status(self) -> QCamera.Status """
        pass

    def statusChanged(self, QCamera_Status): # real signature unknown; restored from __doc__
        """ statusChanged(self, QCamera.Status) [signal] """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) """
        pass

    def supportedLocks(self): # real signature unknown; restored from __doc__
        """ supportedLocks(self) -> QCamera.LockTypes """
        pass

    def supportedViewfinderFrameRateRanges(self, settings=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ supportedViewfinderFrameRateRanges(self, settings: QCameraViewfinderSettings = QCameraViewfinderSettings()) -> List[QCamera.FrameRateRange] """
        pass

    def supportedViewfinderPixelFormats(self, settings=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ supportedViewfinderPixelFormats(self, settings: QCameraViewfinderSettings = QCameraViewfinderSettings()) -> List[QVideoFrame.PixelFormat] """
        pass

    def supportedViewfinderResolutions(self, settings=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ supportedViewfinderResolutions(self, settings: QCameraViewfinderSettings = QCameraViewfinderSettings()) -> List[QSize] """
        pass

    def supportedViewfinderSettings(self, settings=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ supportedViewfinderSettings(self, settings: QCameraViewfinderSettings = QCameraViewfinderSettings()) -> List[QCameraViewfinderSettings] """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def unload(self): # real signature unknown; restored from __doc__
        """ unload(self) """
        pass

    def unlock(self, Union=None, QCamera_LockTypes=None, QCamera_LockType=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        unlock(self)
        unlock(self, Union[QCamera.LockTypes, QCamera.LockType])
        """
        pass

    def viewfinderSettings(self): # real signature unknown; restored from __doc__
        """ viewfinderSettings(self) -> QCameraViewfinderSettings """
        return QCameraViewfinderSettings

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    ActiveState = 2
    ActiveStatus = 8
    BackFace = 1
    CameraError = 1
    CaptureStillImage = 1
    CaptureVideo = 2
    CaptureViewfinder = 0
    FrontFace = 2
    InvalidRequestError = 2
    LoadedState = 1
    LoadedStatus = 4
    LoadingStatus = 2
    LockAcquired = 1
    Locked = 2
    LockExposure = 1
    LockFailed = 2
    LockFocus = 4
    LockLost = 3
    LockTemporaryLost = 4
    LockWhiteBalance = 2
    NoError = 0
    NoLock = 0
    NotSupportedFeatureError = 4
    Searching = 1
    ServiceMissingError = 3
    StandbyStatus = 5
    StartingStatus = 6
    StoppingStatus = 7
    UnavailableStatus = 0
    UnloadedState = 0
    UnloadedStatus = 1
    UnloadingStatus = 3
    Unlocked = 0
    UnspecifiedPosition = 0
    UserRequest = 0


