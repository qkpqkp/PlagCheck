# encoding: utf-8
# module PyQt5.QtLocation
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtLocation.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QPlaceReply import QPlaceReply

class QPlaceSearchReply(QPlaceReply):
    """ QPlaceSearchReply(parent: QObject = None) """
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

    def nextPageRequest(self): # real signature unknown; restored from __doc__
        """ nextPageRequest(self) -> QPlaceSearchRequest """
        return QPlaceSearchRequest

    def previousPageRequest(self): # real signature unknown; restored from __doc__
        """ previousPageRequest(self) -> QPlaceSearchRequest """
        return QPlaceSearchRequest

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def request(self): # real signature unknown; restored from __doc__
        """ request(self) -> QPlaceSearchRequest """
        return QPlaceSearchRequest

    def results(self): # real signature unknown; restored from __doc__
        """ results(self) -> List[QPlaceSearchResult] """
        return []

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setError(self, *args, **kwargs): # real signature unknown
        pass

    def setFinished(self, *args, **kwargs): # real signature unknown
        pass

    def setNextPageRequest(self, QPlaceSearchRequest): # real signature unknown; restored from __doc__
        """ setNextPageRequest(self, QPlaceSearchRequest) """
        pass

    def setPreviousPageRequest(self, QPlaceSearchRequest): # real signature unknown; restored from __doc__
        """ setPreviousPageRequest(self, QPlaceSearchRequest) """
        pass

    def setRequest(self, QPlaceSearchRequest): # real signature unknown; restored from __doc__
        """ setRequest(self, QPlaceSearchRequest) """
        pass

    def setResults(self, Iterable, QPlaceSearchResult=None): # real signature unknown; restored from __doc__
        """ setResults(self, Iterable[QPlaceSearchResult]) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QPlaceReply.Type """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


