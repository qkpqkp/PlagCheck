# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QSoundEffect(__PyQt5_QtCore.QObject):
    """ QSoundEffect(parent: QObject = None) """
    def category(self): # real signature unknown; restored from __doc__
        """ category(self) -> str """
        return ""

    def categoryChanged(self): # real signature unknown; restored from __doc__
        """ categoryChanged(self) [signal] """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isLoaded(self): # real signature unknown; restored from __doc__
        """ isLoaded(self) -> bool """
        return False

    def isMuted(self): # real signature unknown; restored from __doc__
        """ isMuted(self) -> bool """
        return False

    def isPlaying(self): # real signature unknown; restored from __doc__
        """ isPlaying(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def loadedChanged(self): # real signature unknown; restored from __doc__
        """ loadedChanged(self) [signal] """
        pass

    def loopCount(self): # real signature unknown; restored from __doc__
        """ loopCount(self) -> int """
        return 0

    def loopCountChanged(self): # real signature unknown; restored from __doc__
        """ loopCountChanged(self) [signal] """
        pass

    def loopsRemaining(self): # real signature unknown; restored from __doc__
        """ loopsRemaining(self) -> int """
        return 0

    def loopsRemainingChanged(self): # real signature unknown; restored from __doc__
        """ loopsRemainingChanged(self) [signal] """
        pass

    def mutedChanged(self): # real signature unknown; restored from __doc__
        """ mutedChanged(self) [signal] """
        pass

    def play(self): # real signature unknown; restored from __doc__
        """ play(self) """
        pass

    def playingChanged(self): # real signature unknown; restored from __doc__
        """ playingChanged(self) [signal] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCategory(self, p_str): # real signature unknown; restored from __doc__
        """ setCategory(self, str) """
        pass

    def setLoopCount(self, p_int): # real signature unknown; restored from __doc__
        """ setLoopCount(self, int) """
        pass

    def setMuted(self, bool): # real signature unknown; restored from __doc__
        """ setMuted(self, bool) """
        pass

    def setSource(self, QUrl): # real signature unknown; restored from __doc__
        """ setSource(self, QUrl) """
        pass

    def setVolume(self, p_float): # real signature unknown; restored from __doc__
        """ setVolume(self, float) """
        pass

    def source(self): # real signature unknown; restored from __doc__
        """ source(self) -> QUrl """
        pass

    def sourceChanged(self): # real signature unknown; restored from __doc__
        """ sourceChanged(self) [signal] """
        pass

    def status(self): # real signature unknown; restored from __doc__
        """ status(self) -> QSoundEffect.Status """
        pass

    def statusChanged(self): # real signature unknown; restored from __doc__
        """ statusChanged(self) [signal] """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) """
        pass

    def supportedMimeTypes(self): # real signature unknown; restored from __doc__
        """ supportedMimeTypes() -> List[str] """
        return []

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def volume(self): # real signature unknown; restored from __doc__
        """ volume(self) -> float """
        return 0.0

    def volumeChanged(self): # real signature unknown; restored from __doc__
        """ volumeChanged(self) [signal] """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    Error = 3
    Infinite = -2
    Loading = 1
    Null = 0
    Ready = 2


