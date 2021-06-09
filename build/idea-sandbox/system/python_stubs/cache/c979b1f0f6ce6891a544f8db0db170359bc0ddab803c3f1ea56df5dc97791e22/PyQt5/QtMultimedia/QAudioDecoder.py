# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QMediaObject import QMediaObject

class QAudioDecoder(QMediaObject):
    """ QAudioDecoder(parent: QObject = None) """
    def addPropertyWatch(self, *args, **kwargs): # real signature unknown
        pass

    def audioFormat(self): # real signature unknown; restored from __doc__
        """ audioFormat(self) -> QAudioFormat """
        return QAudioFormat

    def bind(self, QObject): # real signature unknown; restored from __doc__
        """ bind(self, QObject) -> bool """
        return False

    def bufferAvailable(self): # real signature unknown; restored from __doc__
        """ bufferAvailable(self) -> bool """
        return False

    def bufferAvailableChanged(self, bool): # real signature unknown; restored from __doc__
        """ bufferAvailableChanged(self, bool) [signal] """
        pass

    def bufferReady(self): # real signature unknown; restored from __doc__
        """ bufferReady(self) [signal] """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

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

    def error(self, QAudioDecoder_Error=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        error(self) -> QAudioDecoder.Error
        error(self, QAudioDecoder.Error) [signal]
        """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def finished(self): # real signature unknown; restored from __doc__
        """ finished(self) [signal] """
        pass

    def formatChanged(self, QAudioFormat): # real signature unknown; restored from __doc__
        """ formatChanged(self, QAudioFormat) [signal] """
        pass

    def hasSupport(self, p_str, codecs, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ hasSupport(str, codecs: Iterable[str] = []) -> QMultimedia.SupportEstimate """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def position(self): # real signature unknown; restored from __doc__
        """ position(self) -> int """
        return 0

    def positionChanged(self, p_int): # real signature unknown; restored from __doc__
        """ positionChanged(self, int) [signal] """
        pass

    def read(self): # real signature unknown; restored from __doc__
        """ read(self) -> QAudioBuffer """
        return QAudioBuffer

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removePropertyWatch(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAudioFormat(self, QAudioFormat): # real signature unknown; restored from __doc__
        """ setAudioFormat(self, QAudioFormat) """
        pass

    def setSourceDevice(self, QIODevice): # real signature unknown; restored from __doc__
        """ setSourceDevice(self, QIODevice) """
        pass

    def setSourceFilename(self, p_str): # real signature unknown; restored from __doc__
        """ setSourceFilename(self, str) """
        pass

    def sourceChanged(self): # real signature unknown; restored from __doc__
        """ sourceChanged(self) [signal] """
        pass

    def sourceDevice(self): # real signature unknown; restored from __doc__
        """ sourceDevice(self) -> QIODevice """
        pass

    def sourceFilename(self): # real signature unknown; restored from __doc__
        """ sourceFilename(self) -> str """
        return ""

    def start(self): # real signature unknown; restored from __doc__
        """ start(self) """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QAudioDecoder.State """
        pass

    def stateChanged(self, QAudioDecoder_State): # real signature unknown; restored from __doc__
        """ stateChanged(self, QAudioDecoder.State) [signal] """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def unbind(self, QObject): # real signature unknown; restored from __doc__
        """ unbind(self, QObject) """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    AccessDeniedError = 3
    DecodingState = 1
    FormatError = 2
    NoError = 0
    ResourceError = 1
    ServiceMissingError = 4
    StoppedState = 0


