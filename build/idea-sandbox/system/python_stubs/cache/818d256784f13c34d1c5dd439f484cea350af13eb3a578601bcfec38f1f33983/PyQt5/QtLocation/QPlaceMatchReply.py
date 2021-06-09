# encoding: utf-8
# module PyQt5.QtLocation
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtLocation.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QPlaceReply import QPlaceReply

class QPlaceMatchReply(QPlaceReply):
    """ QPlaceMatchReply(parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def places(self): # real signature unknown; restored from __doc__
        """ places(self) -> List[QPlace] """
        return []

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def request(self): # real signature unknown; restored from __doc__
        """ request(self) -> QPlaceMatchRequest """
        return QPlaceMatchRequest

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setError(self, *args, **kwargs): # real signature unknown
        pass

    def setFinished(self, *args, **kwargs): # real signature unknown
        pass

    def setPlaces(self, Iterable, QPlace=None): # real signature unknown; restored from __doc__
        """ setPlaces(self, Iterable[QPlace]) """
        pass

    def setRequest(self, QPlaceMatchRequest): # real signature unknown; restored from __doc__
        """ setRequest(self, QPlaceMatchRequest) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QPlaceReply.Type """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


