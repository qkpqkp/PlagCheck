# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QMediaBindableInterface import QMediaBindableInterface

class QMediaRecorder(__PyQt5_QtCore.QObject, QMediaBindableInterface):
    """ QMediaRecorder(QMediaObject, parent: QObject = None) """
    def actualLocation(self): # real signature unknown; restored from __doc__
        """ actualLocation(self) -> QUrl """
        pass

    def actualLocationChanged(self, QUrl): # real signature unknown; restored from __doc__
        """ actualLocationChanged(self, QUrl) [signal] """
        pass

    def audioCodecDescription(self, p_str): # real signature unknown; restored from __doc__
        """ audioCodecDescription(self, str) -> str """
        return ""

    def audioSettings(self): # real signature unknown; restored from __doc__
        """ audioSettings(self) -> QAudioEncoderSettings """
        return QAudioEncoderSettings

    def availability(self): # real signature unknown; restored from __doc__
        """ availability(self) -> QMultimedia.AvailabilityStatus """
        pass

    def availabilityChanged(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        availabilityChanged(self, QMultimedia.AvailabilityStatus) [signal]
        availabilityChanged(self, bool) [signal]
        """
        pass

    def availableMetaData(self): # real signature unknown; restored from __doc__
        """ availableMetaData(self) -> List[str] """
        return []

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def containerDescription(self, p_str): # real signature unknown; restored from __doc__
        """ containerDescription(self, str) -> str """
        return ""

    def containerFormat(self): # real signature unknown; restored from __doc__
        """ containerFormat(self) -> str """
        return ""

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def duration(self): # real signature unknown; restored from __doc__
        """ duration(self) -> int """
        return 0

    def durationChanged(self, p_int): # real signature unknown; restored from __doc__
        """ durationChanged(self, int) [signal] """
        pass

    def error(self, QMediaRecorder_Error=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        error(self) -> QMediaRecorder.Error
        error(self, QMediaRecorder.Error) [signal]
        """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def isAvailable(self): # real signature unknown; restored from __doc__
        """ isAvailable(self) -> bool """
        return False

    def isMetaDataAvailable(self): # real signature unknown; restored from __doc__
        """ isMetaDataAvailable(self) -> bool """
        return False

    def isMetaDataWritable(self): # real signature unknown; restored from __doc__
        """ isMetaDataWritable(self) -> bool """
        return False

    def isMuted(self): # real signature unknown; restored from __doc__
        """ isMuted(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def mediaObject(self): # real signature unknown; restored from __doc__
        """ mediaObject(self) -> QMediaObject """
        return QMediaObject

    def metaData(self, p_str): # real signature unknown; restored from __doc__
        """ metaData(self, str) -> Any """
        pass

    def metaDataAvailableChanged(self, bool): # real signature unknown; restored from __doc__
        """ metaDataAvailableChanged(self, bool) [signal] """
        pass

    def metaDataChanged(self, p_str=None, Any=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        metaDataChanged(self, str, Any) [signal]
        metaDataChanged(self) [signal]
        """
        pass

    def metaDataWritableChanged(self, bool): # real signature unknown; restored from __doc__
        """ metaDataWritableChanged(self, bool) [signal] """
        pass

    def mutedChanged(self, bool): # real signature unknown; restored from __doc__
        """ mutedChanged(self, bool) [signal] """
        pass

    def outputLocation(self): # real signature unknown; restored from __doc__
        """ outputLocation(self) -> QUrl """
        pass

    def pause(self): # real signature unknown; restored from __doc__
        """ pause(self) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def record(self): # real signature unknown; restored from __doc__
        """ record(self) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAudioSettings(self, QAudioEncoderSettings): # real signature unknown; restored from __doc__
        """ setAudioSettings(self, QAudioEncoderSettings) """
        pass

    def setContainerFormat(self, p_str): # real signature unknown; restored from __doc__
        """ setContainerFormat(self, str) """
        pass

    def setEncodingSettings(self, QAudioEncoderSettings, video=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setEncodingSettings(self, QAudioEncoderSettings, video: QVideoEncoderSettings = QVideoEncoderSettings(), container: str = '') """
        pass

    def setMediaObject(self, QMediaObject): # real signature unknown; restored from __doc__
        """ setMediaObject(self, QMediaObject) -> bool """
        return False

    def setMetaData(self, p_str, Any): # real signature unknown; restored from __doc__
        """ setMetaData(self, str, Any) """
        pass

    def setMuted(self, bool): # real signature unknown; restored from __doc__
        """ setMuted(self, bool) """
        pass

    def setOutputLocation(self, QUrl): # real signature unknown; restored from __doc__
        """ setOutputLocation(self, QUrl) -> bool """
        return False

    def setVideoSettings(self, QVideoEncoderSettings): # real signature unknown; restored from __doc__
        """ setVideoSettings(self, QVideoEncoderSettings) """
        pass

    def setVolume(self, p_float): # real signature unknown; restored from __doc__
        """ setVolume(self, float) """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QMediaRecorder.State """
        pass

    def stateChanged(self, QMediaRecorder_State): # real signature unknown; restored from __doc__
        """ stateChanged(self, QMediaRecorder.State) [signal] """
        pass

    def status(self): # real signature unknown; restored from __doc__
        """ status(self) -> QMediaRecorder.Status """
        pass

    def statusChanged(self, QMediaRecorder_Status): # real signature unknown; restored from __doc__
        """ statusChanged(self, QMediaRecorder.Status) [signal] """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) """
        pass

    def supportedAudioCodecs(self): # real signature unknown; restored from __doc__
        """ supportedAudioCodecs(self) -> List[str] """
        return []

    def supportedAudioSampleRates(self, settings=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ supportedAudioSampleRates(self, settings: QAudioEncoderSettings = QAudioEncoderSettings()) -> Tuple[List[int], bool] """
        pass

    def supportedContainers(self): # real signature unknown; restored from __doc__
        """ supportedContainers(self) -> List[str] """
        return []

    def supportedFrameRates(self, settings=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ supportedFrameRates(self, settings: QVideoEncoderSettings = QVideoEncoderSettings()) -> Tuple[List[float], bool] """
        pass

    def supportedResolutions(self, settings=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ supportedResolutions(self, settings: QVideoEncoderSettings = QVideoEncoderSettings()) -> Tuple[List[QSize], bool] """
        pass

    def supportedVideoCodecs(self): # real signature unknown; restored from __doc__
        """ supportedVideoCodecs(self) -> List[str] """
        return []

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def videoCodecDescription(self, p_str): # real signature unknown; restored from __doc__
        """ videoCodecDescription(self, str) -> str """
        return ""

    def videoSettings(self): # real signature unknown; restored from __doc__
        """ videoSettings(self) -> QVideoEncoderSettings """
        return QVideoEncoderSettings

    def volume(self): # real signature unknown; restored from __doc__
        """ volume(self) -> float """
        return 0.0

    def volumeChanged(self, p_float): # real signature unknown; restored from __doc__
        """ volumeChanged(self, float) [signal] """
        pass

    def __init__(self, QMediaObject, parent=None): # real signature unknown; restored from __doc__
        pass

    FinalizingStatus = 7
    FormatError = 2
    LoadedStatus = 3
    LoadingStatus = 2
    NoError = 0
    OutOfSpaceError = 3
    PausedState = 2
    PausedStatus = 6
    RecordingState = 1
    RecordingStatus = 5
    ResourceError = 1
    StartingStatus = 4
    StoppedState = 0
    UnavailableStatus = 0
    UnloadedStatus = 1


