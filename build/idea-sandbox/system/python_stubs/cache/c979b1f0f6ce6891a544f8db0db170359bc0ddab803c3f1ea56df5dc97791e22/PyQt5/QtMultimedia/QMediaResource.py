# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QMediaResource(__sip.simplewrapper):
    """
    QMediaResource()
    QMediaResource(QUrl, mimeType: str = '')
    QMediaResource(QNetworkRequest, mimeType: str = '')
    QMediaResource(QMediaResource)
    """
    def audioBitRate(self): # real signature unknown; restored from __doc__
        """ audioBitRate(self) -> int """
        return 0

    def audioCodec(self): # real signature unknown; restored from __doc__
        """ audioCodec(self) -> str """
        return ""

    def channelCount(self): # real signature unknown; restored from __doc__
        """ channelCount(self) -> int """
        return 0

    def dataSize(self): # real signature unknown; restored from __doc__
        """ dataSize(self) -> int """
        return 0

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def language(self): # real signature unknown; restored from __doc__
        """ language(self) -> str """
        return ""

    def mimeType(self): # real signature unknown; restored from __doc__
        """ mimeType(self) -> str """
        return ""

    def request(self): # real signature unknown; restored from __doc__
        """ request(self) -> QNetworkRequest """
        pass

    def resolution(self): # real signature unknown; restored from __doc__
        """ resolution(self) -> QSize """
        pass

    def sampleRate(self): # real signature unknown; restored from __doc__
        """ sampleRate(self) -> int """
        return 0

    def setAudioBitRate(self, p_int): # real signature unknown; restored from __doc__
        """ setAudioBitRate(self, int) """
        pass

    def setAudioCodec(self, p_str): # real signature unknown; restored from __doc__
        """ setAudioCodec(self, str) """
        pass

    def setChannelCount(self, p_int): # real signature unknown; restored from __doc__
        """ setChannelCount(self, int) """
        pass

    def setDataSize(self, p_int): # real signature unknown; restored from __doc__
        """ setDataSize(self, int) """
        pass

    def setLanguage(self, p_str): # real signature unknown; restored from __doc__
        """ setLanguage(self, str) """
        pass

    def setResolution(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setResolution(self, QSize)
        setResolution(self, int, int)
        """
        pass

    def setSampleRate(self, p_int): # real signature unknown; restored from __doc__
        """ setSampleRate(self, int) """
        pass

    def setVideoBitRate(self, p_int): # real signature unknown; restored from __doc__
        """ setVideoBitRate(self, int) """
        pass

    def setVideoCodec(self, p_str): # real signature unknown; restored from __doc__
        """ setVideoCodec(self, str) """
        pass

    def url(self): # real signature unknown; restored from __doc__
        """ url(self) -> QUrl """
        pass

    def videoBitRate(self): # real signature unknown; restored from __doc__
        """ videoBitRate(self) -> int """
        return 0

    def videoCodec(self): # real signature unknown; restored from __doc__
        """ videoCodec(self) -> str """
        return ""

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
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


