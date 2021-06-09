# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QAudioDeviceInfo(__sip.simplewrapper):
    """
    QAudioDeviceInfo()
    QAudioDeviceInfo(QAudioDeviceInfo)
    """
    def availableDevices(self, QAudio_Mode): # real signature unknown; restored from __doc__
        """ availableDevices(QAudio.Mode) -> List[QAudioDeviceInfo] """
        return []

    def defaultInputDevice(self): # real signature unknown; restored from __doc__
        """ defaultInputDevice() -> QAudioDeviceInfo """
        return QAudioDeviceInfo

    def defaultOutputDevice(self): # real signature unknown; restored from __doc__
        """ defaultOutputDevice() -> QAudioDeviceInfo """
        return QAudioDeviceInfo

    def deviceName(self): # real signature unknown; restored from __doc__
        """ deviceName(self) -> str """
        return ""

    def isFormatSupported(self, QAudioFormat): # real signature unknown; restored from __doc__
        """ isFormatSupported(self, QAudioFormat) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def nearestFormat(self, QAudioFormat): # real signature unknown; restored from __doc__
        """ nearestFormat(self, QAudioFormat) -> QAudioFormat """
        return QAudioFormat

    def preferredFormat(self): # real signature unknown; restored from __doc__
        """ preferredFormat(self) -> QAudioFormat """
        return QAudioFormat

    def supportedByteOrders(self): # real signature unknown; restored from __doc__
        """ supportedByteOrders(self) -> List[QAudioFormat.Endian] """
        return []

    def supportedChannelCounts(self): # real signature unknown; restored from __doc__
        """ supportedChannelCounts(self) -> List[int] """
        return []

    def supportedCodecs(self): # real signature unknown; restored from __doc__
        """ supportedCodecs(self) -> List[str] """
        return []

    def supportedSampleRates(self): # real signature unknown; restored from __doc__
        """ supportedSampleRates(self) -> List[int] """
        return []

    def supportedSampleSizes(self): # real signature unknown; restored from __doc__
        """ supportedSampleSizes(self) -> List[int] """
        return []

    def supportedSampleTypes(self): # real signature unknown; restored from __doc__
        """ supportedSampleTypes(self) -> List[QAudioFormat.SampleType] """
        return []

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, QAudioDeviceInfo=None): # real signature unknown; restored from __doc__ with multiple overloads
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


    __hash__ = None


