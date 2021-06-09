# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QMediaBindableInterface import QMediaBindableInterface

class QCameraImageCapture(__PyQt5_QtCore.QObject, QMediaBindableInterface):
    """ QCameraImageCapture(QMediaObject, parent: QObject = None) """
    def availability(self): # real signature unknown; restored from __doc__
        """ availability(self) -> QMultimedia.AvailabilityStatus """
        pass

    def bufferFormat(self): # real signature unknown; restored from __doc__
        """ bufferFormat(self) -> QVideoFrame.PixelFormat """
        pass

    def bufferFormatChanged(self, QVideoFrame_PixelFormat): # real signature unknown; restored from __doc__
        """ bufferFormatChanged(self, QVideoFrame.PixelFormat) [signal] """
        pass

    def cancelCapture(self): # real signature unknown; restored from __doc__
        """ cancelCapture(self) """
        pass

    def capture(self, file=''): # real signature unknown; restored from __doc__
        """ capture(self, file: str = '') -> int """
        return 0

    def captureDestination(self): # real signature unknown; restored from __doc__
        """ captureDestination(self) -> QCameraImageCapture.CaptureDestinations """
        pass

    def captureDestinationChanged(self, Union, QCameraImageCapture_CaptureDestinations=None, QCameraImageCapture_CaptureDestination=None): # real signature unknown; restored from __doc__
        """ captureDestinationChanged(self, Union[QCameraImageCapture.CaptureDestinations, QCameraImageCapture.CaptureDestination]) [signal] """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def encodingSettings(self): # real signature unknown; restored from __doc__
        """ encodingSettings(self) -> QImageEncoderSettings """
        return QImageEncoderSettings

    def error(self, p_int=None, QCameraImageCapture_Error=None, p_str=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        error(self) -> QCameraImageCapture.Error
        error(self, int, QCameraImageCapture.Error, str) [signal]
        """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def imageAvailable(self, p_int, QVideoFrame): # real signature unknown; restored from __doc__
        """ imageAvailable(self, int, QVideoFrame) [signal] """
        pass

    def imageCaptured(self, p_int, QImage): # real signature unknown; restored from __doc__
        """ imageCaptured(self, int, QImage) [signal] """
        pass

    def imageCodecDescription(self, p_str): # real signature unknown; restored from __doc__
        """ imageCodecDescription(self, str) -> str """
        return ""

    def imageExposed(self, p_int): # real signature unknown; restored from __doc__
        """ imageExposed(self, int) [signal] """
        pass

    def imageMetadataAvailable(self, p_int, p_str, Any): # real signature unknown; restored from __doc__
        """ imageMetadataAvailable(self, int, str, Any) [signal] """
        pass

    def imageSaved(self, p_int, p_str): # real signature unknown; restored from __doc__
        """ imageSaved(self, int, str) [signal] """
        pass

    def isAvailable(self): # real signature unknown; restored from __doc__
        """ isAvailable(self) -> bool """
        return False

    def isCaptureDestinationSupported(self, Union, QCameraImageCapture_CaptureDestinations=None, QCameraImageCapture_CaptureDestination=None): # real signature unknown; restored from __doc__
        """ isCaptureDestinationSupported(self, Union[QCameraImageCapture.CaptureDestinations, QCameraImageCapture.CaptureDestination]) -> bool """
        return False

    def isReadyForCapture(self): # real signature unknown; restored from __doc__
        """ isReadyForCapture(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def mediaObject(self): # real signature unknown; restored from __doc__
        """ mediaObject(self) -> QMediaObject """
        return QMediaObject

    def readyForCaptureChanged(self, bool): # real signature unknown; restored from __doc__
        """ readyForCaptureChanged(self, bool) [signal] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setBufferFormat(self, QVideoFrame_PixelFormat): # real signature unknown; restored from __doc__
        """ setBufferFormat(self, QVideoFrame.PixelFormat) """
        pass

    def setCaptureDestination(self, Union, QCameraImageCapture_CaptureDestinations=None, QCameraImageCapture_CaptureDestination=None): # real signature unknown; restored from __doc__
        """ setCaptureDestination(self, Union[QCameraImageCapture.CaptureDestinations, QCameraImageCapture.CaptureDestination]) """
        pass

    def setEncodingSettings(self, QImageEncoderSettings): # real signature unknown; restored from __doc__
        """ setEncodingSettings(self, QImageEncoderSettings) """
        pass

    def setMediaObject(self, QMediaObject): # real signature unknown; restored from __doc__
        """ setMediaObject(self, QMediaObject) -> bool """
        return False

    def supportedBufferFormats(self): # real signature unknown; restored from __doc__
        """ supportedBufferFormats(self) -> List[QVideoFrame.PixelFormat] """
        return []

    def supportedImageCodecs(self): # real signature unknown; restored from __doc__
        """ supportedImageCodecs(self) -> List[str] """
        return []

    def supportedResolutions(self, settings=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ supportedResolutions(self, settings: QImageEncoderSettings = QImageEncoderSettings()) -> Tuple[List[QSize], bool] """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, QMediaObject, parent=None): # real signature unknown; restored from __doc__
        pass

    CaptureToBuffer = 2
    CaptureToFile = 1
    FormatError = 5
    NoError = 0
    NotReadyError = 1
    NotSupportedFeatureError = 4
    OutOfSpaceError = 3
    ResourceError = 2
    SingleImageCapture = 0


