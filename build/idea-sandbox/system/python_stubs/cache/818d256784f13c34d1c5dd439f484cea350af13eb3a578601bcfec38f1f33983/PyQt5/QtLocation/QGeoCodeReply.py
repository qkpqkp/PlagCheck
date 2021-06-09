# encoding: utf-8
# module PyQt5.QtLocation
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtLocation.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QGeoCodeReply(__PyQt5_QtCore.QObject):
    """
    QGeoCodeReply(QGeoCodeReply.Error, str, parent: QObject = None)
    QGeoCodeReply(parent: QObject = None)
    """
    def abort(self): # real signature unknown; restored from __doc__
        """ abort(self) """
        pass

    def aborted(self): # real signature unknown; restored from __doc__
        """ aborted(self) [signal] """
        pass

    def addLocation(self, QGeoLocation): # real signature unknown; restored from __doc__
        """ addLocation(self, QGeoLocation) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, QGeoCodeReply_Error=None, errorString=''): # real signature unknown; restored from __doc__ with multiple overloads
        """
        error(self) -> QGeoCodeReply.Error
        error(self, QGeoCodeReply.Error, errorString: str = '') [signal]
        """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def finished(self): # real signature unknown; restored from __doc__
        """ finished(self) [signal] """
        pass

    def isFinished(self): # real signature unknown; restored from __doc__
        """ isFinished(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def limit(self): # real signature unknown; restored from __doc__
        """ limit(self) -> int """
        return 0

    def locations(self): # real signature unknown; restored from __doc__
        """ locations(self) -> List[QGeoLocation] """
        return []

    def offset(self): # real signature unknown; restored from __doc__
        """ offset(self) -> int """
        return 0

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setError(self, QGeoCodeReply_Error, p_str): # real signature unknown; restored from __doc__
        """ setError(self, QGeoCodeReply.Error, str) """
        pass

    def setFinished(self, bool): # real signature unknown; restored from __doc__
        """ setFinished(self, bool) """
        pass

    def setLimit(self, p_int): # real signature unknown; restored from __doc__
        """ setLimit(self, int) """
        pass

    def setLocations(self, Iterable, QGeoLocation=None): # real signature unknown; restored from __doc__
        """ setLocations(self, Iterable[QGeoLocation]) """
        pass

    def setOffset(self, p_int): # real signature unknown; restored from __doc__
        """ setOffset(self, int) """
        pass

    def setViewport(self, QGeoShape): # real signature unknown; restored from __doc__
        """ setViewport(self, QGeoShape) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def viewport(self): # real signature unknown; restored from __doc__
        """ viewport(self) -> QGeoShape """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    CombinationError = 5
    CommunicationError = 2
    EngineNotSetError = 1
    NoError = 0
    ParseError = 3
    UnknownError = 6
    UnsupportedOptionError = 4


