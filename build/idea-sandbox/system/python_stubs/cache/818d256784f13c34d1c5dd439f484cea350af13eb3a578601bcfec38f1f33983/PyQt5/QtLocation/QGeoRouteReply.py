# encoding: utf-8
# module PyQt5.QtLocation
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtLocation.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QGeoRouteReply(__PyQt5_QtCore.QObject):
    """
    QGeoRouteReply(QGeoRouteReply.Error, str, parent: QObject = None)
    QGeoRouteReply(QGeoRouteRequest, parent: QObject = None)
    """
    def abort(self): # real signature unknown; restored from __doc__
        """ abort(self) """
        pass

    def aborted(self): # real signature unknown; restored from __doc__
        """ aborted(self) [signal] """
        pass

    def addRoutes(self, Iterable, QGeoRoute=None): # real signature unknown; restored from __doc__
        """ addRoutes(self, Iterable[QGeoRoute]) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, QGeoRouteReply_Error=None, errorString=''): # real signature unknown; restored from __doc__ with multiple overloads
        """
        error(self) -> QGeoRouteReply.Error
        error(self, QGeoRouteReply.Error, errorString: str = '') [signal]
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

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def request(self): # real signature unknown; restored from __doc__
        """ request(self) -> QGeoRouteRequest """
        return QGeoRouteRequest

    def routes(self): # real signature unknown; restored from __doc__
        """ routes(self) -> List[QGeoRoute] """
        return []

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setError(self, QGeoRouteReply_Error, p_str): # real signature unknown; restored from __doc__
        """ setError(self, QGeoRouteReply.Error, str) """
        pass

    def setFinished(self, bool): # real signature unknown; restored from __doc__
        """ setFinished(self, bool) """
        pass

    def setRoutes(self, Iterable, QGeoRoute=None): # real signature unknown; restored from __doc__
        """ setRoutes(self, Iterable[QGeoRoute]) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    CommunicationError = 2
    EngineNotSetError = 1
    NoError = 0
    ParseError = 3
    UnknownError = 5
    UnsupportedOptionError = 4


