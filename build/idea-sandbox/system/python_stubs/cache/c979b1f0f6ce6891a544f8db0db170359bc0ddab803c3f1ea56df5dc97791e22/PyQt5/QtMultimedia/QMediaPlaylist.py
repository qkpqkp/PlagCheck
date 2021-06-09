# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QMediaBindableInterface import QMediaBindableInterface

class QMediaPlaylist(__PyQt5_QtCore.QObject, QMediaBindableInterface):
    """ QMediaPlaylist(parent: QObject = None) """
    def addMedia(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addMedia(self, QMediaContent) -> bool
        addMedia(self, Iterable[QMediaContent]) -> bool
        """
        return False

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> bool """
        return False

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def currentIndex(self): # real signature unknown; restored from __doc__
        """ currentIndex(self) -> int """
        return 0

    def currentIndexChanged(self, p_int): # real signature unknown; restored from __doc__
        """ currentIndexChanged(self, int) [signal] """
        pass

    def currentMedia(self): # real signature unknown; restored from __doc__
        """ currentMedia(self) -> QMediaContent """
        return QMediaContent

    def currentMediaChanged(self, QMediaContent): # real signature unknown; restored from __doc__
        """ currentMediaChanged(self, QMediaContent) [signal] """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> QMediaPlaylist.Error """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def insertMedia(self, p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        insertMedia(self, int, QMediaContent) -> bool
        insertMedia(self, int, Iterable[QMediaContent]) -> bool
        """
        return False

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isReadOnly(self): # real signature unknown; restored from __doc__
        """ isReadOnly(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def load(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        load(self, QNetworkRequest, format: str = None)
        load(self, QUrl, format: str = None)
        load(self, QIODevice, format: str = None)
        """
        pass

    def loaded(self): # real signature unknown; restored from __doc__
        """ loaded(self) [signal] """
        pass

    def loadFailed(self): # real signature unknown; restored from __doc__
        """ loadFailed(self) [signal] """
        pass

    def media(self, p_int): # real signature unknown; restored from __doc__
        """ media(self, int) -> QMediaContent """
        return QMediaContent

    def mediaAboutToBeInserted(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ mediaAboutToBeInserted(self, int, int) [signal] """
        pass

    def mediaAboutToBeRemoved(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ mediaAboutToBeRemoved(self, int, int) [signal] """
        pass

    def mediaChanged(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ mediaChanged(self, int, int) [signal] """
        pass

    def mediaCount(self): # real signature unknown; restored from __doc__
        """ mediaCount(self) -> int """
        return 0

    def mediaInserted(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ mediaInserted(self, int, int) [signal] """
        pass

    def mediaObject(self): # real signature unknown; restored from __doc__
        """ mediaObject(self) -> QMediaObject """
        return QMediaObject

    def mediaRemoved(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ mediaRemoved(self, int, int) [signal] """
        pass

    def moveMedia(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ moveMedia(self, int, int) -> bool """
        return False

    def next(self): # real signature unknown; restored from __doc__
        """ next(self) """
        pass

    def nextIndex(self, steps=1): # real signature unknown; restored from __doc__
        """ nextIndex(self, steps: int = 1) -> int """
        return 0

    def playbackMode(self): # real signature unknown; restored from __doc__
        """ playbackMode(self) -> QMediaPlaylist.PlaybackMode """
        pass

    def playbackModeChanged(self, QMediaPlaylist_PlaybackMode): # real signature unknown; restored from __doc__
        """ playbackModeChanged(self, QMediaPlaylist.PlaybackMode) [signal] """
        pass

    def previous(self): # real signature unknown; restored from __doc__
        """ previous(self) """
        pass

    def previousIndex(self, steps=1): # real signature unknown; restored from __doc__
        """ previousIndex(self, steps: int = 1) -> int """
        return 0

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeMedia(self, p_int, p_int_1=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        removeMedia(self, int) -> bool
        removeMedia(self, int, int) -> bool
        """
        return False

    def save(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        save(self, QUrl, format: str = None) -> bool
        save(self, QIODevice, str) -> bool
        """
        return False

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCurrentIndex(self, p_int): # real signature unknown; restored from __doc__
        """ setCurrentIndex(self, int) """
        pass

    def setMediaObject(self, QMediaObject): # real signature unknown; restored from __doc__
        """ setMediaObject(self, QMediaObject) -> bool """
        return False

    def setPlaybackMode(self, QMediaPlaylist_PlaybackMode): # real signature unknown; restored from __doc__
        """ setPlaybackMode(self, QMediaPlaylist.PlaybackMode) """
        pass

    def shuffle(self): # real signature unknown; restored from __doc__
        """ shuffle(self) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    AccessDeniedError = 4
    CurrentItemInLoop = 1
    CurrentItemOnce = 0
    FormatError = 1
    FormatNotSupportedError = 2
    Loop = 3
    NetworkError = 3
    NoError = 0
    Random = 4
    Sequential = 2


