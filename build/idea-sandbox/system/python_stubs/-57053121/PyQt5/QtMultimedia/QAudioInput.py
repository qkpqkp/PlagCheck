# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QAudioInput(__PyQt5_QtCore.QObject):
    """
    QAudioInput(format: QAudioFormat = QAudioFormat(), parent: QObject = None)
    QAudioInput(QAudioDeviceInfo, format: QAudioFormat = QAudioFormat(), parent: QObject = None)
    """
    def bufferSize(self): # real signature unknown; restored from __doc__
        """ bufferSize(self) -> int """
        return 0

    def bytesReady(self): # real signature unknown; restored from __doc__
        """ bytesReady(self) -> int """
        return 0

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def elapsedUSecs(self): # real signature unknown; restored from __doc__
        """ elapsedUSecs(self) -> int """
        return 0

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> QAudio.Error """
        pass

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> QAudioFormat """
        return QAudioFormat

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def notify(self): # real signature unknown; restored from __doc__
        """ notify(self) [signal] """
        pass

    def notifyInterval(self): # real signature unknown; restored from __doc__
        """ notifyInterval(self) -> int """
        return 0

    def periodSize(self): # real signature unknown; restored from __doc__
        """ periodSize(self) -> int """
        return 0

    def processedUSecs(self): # real signature unknown; restored from __doc__
        """ processedUSecs(self) -> int """
        return 0

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) """
        pass

    def resume(self): # real signature unknown; restored from __doc__
        """ resume(self) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setBufferSize(self, p_int): # real signature unknown; restored from __doc__
        """ setBufferSize(self, int) """
        pass

    def setNotifyInterval(self, p_int): # real signature unknown; restored from __doc__
        """ setNotifyInterval(self, int) """
        pass

    def setVolume(self, p_float): # real signature unknown; restored from __doc__
        """ setVolume(self, float) """
        pass

    def start(self, QIODevice=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        start(self, QIODevice)
        start(self) -> QIODevice
        """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QAudio.State """
        pass

    def stateChanged(self, QAudio_State): # real signature unknown; restored from __doc__
        """ stateChanged(self, QAudio.State) [signal] """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) """
        pass

    def suspend(self): # real signature unknown; restored from __doc__
        """ suspend(self) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def volume(self): # real signature unknown; restored from __doc__
        """ volume(self) -> float """
        return 0.0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


