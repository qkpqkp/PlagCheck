# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QAudioFormat(__sip.simplewrapper):
    """
    QAudioFormat()
    QAudioFormat(QAudioFormat)
    """
    def byteOrder(self): # real signature unknown; restored from __doc__
        """ byteOrder(self) -> QAudioFormat.Endian """
        pass

    def bytesForDuration(self, p_int): # real signature unknown; restored from __doc__
        """ bytesForDuration(self, int) -> int """
        return 0

    def bytesForFrames(self, p_int): # real signature unknown; restored from __doc__
        """ bytesForFrames(self, int) -> int """
        return 0

    def bytesPerFrame(self): # real signature unknown; restored from __doc__
        """ bytesPerFrame(self) -> int """
        return 0

    def channelCount(self): # real signature unknown; restored from __doc__
        """ channelCount(self) -> int """
        return 0

    def codec(self): # real signature unknown; restored from __doc__
        """ codec(self) -> str """
        return ""

    def durationForBytes(self, p_int): # real signature unknown; restored from __doc__
        """ durationForBytes(self, int) -> int """
        return 0

    def durationForFrames(self, p_int): # real signature unknown; restored from __doc__
        """ durationForFrames(self, int) -> int """
        return 0

    def framesForBytes(self, p_int): # real signature unknown; restored from __doc__
        """ framesForBytes(self, int) -> int """
        return 0

    def framesForDuration(self, p_int): # real signature unknown; restored from __doc__
        """ framesForDuration(self, int) -> int """
        return 0

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def sampleRate(self): # real signature unknown; restored from __doc__
        """ sampleRate(self) -> int """
        return 0

    def sampleSize(self): # real signature unknown; restored from __doc__
        """ sampleSize(self) -> int """
        return 0

    def sampleType(self): # real signature unknown; restored from __doc__
        """ sampleType(self) -> QAudioFormat.SampleType """
        pass

    def setByteOrder(self, QAudioFormat_Endian): # real signature unknown; restored from __doc__
        """ setByteOrder(self, QAudioFormat.Endian) """
        pass

    def setChannelCount(self, p_int): # real signature unknown; restored from __doc__
        """ setChannelCount(self, int) """
        pass

    def setCodec(self, p_str): # real signature unknown; restored from __doc__
        """ setCodec(self, str) """
        pass

    def setSampleRate(self, p_int): # real signature unknown; restored from __doc__
        """ setSampleRate(self, int) """
        pass

    def setSampleSize(self, p_int): # real signature unknown; restored from __doc__
        """ setSampleSize(self, int) """
        pass

    def setSampleType(self, QAudioFormat_SampleType): # real signature unknown; restored from __doc__
        """ setSampleType(self, QAudioFormat.SampleType) """
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

    def __init__(self, QAudioFormat=None): # real signature unknown; restored from __doc__ with multiple overloads
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


    BigEndian = 0
    Float = 3
    LittleEndian = 1
    SignedInt = 1
    Unknown = 0
    UnSignedInt = 2
    __hash__ = None


