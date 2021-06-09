# encoding: utf-8
# module PyQt5.QtLocation
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtLocation.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QGeoCodingManagerEngine(__PyQt5_QtCore.QObject):
    """ QGeoCodingManagerEngine(Dict[str, Any], parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, QGeoCodeReply, QGeoCodeReply_Error, errorString=''): # real signature unknown; restored from __doc__
        """ error(self, QGeoCodeReply, QGeoCodeReply.Error, errorString: str = '') [signal] """
        pass

    def finished(self, QGeoCodeReply): # real signature unknown; restored from __doc__
        """ finished(self, QGeoCodeReply) [signal] """
        pass

    def geocode(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        geocode(self, QGeoAddress, QGeoShape) -> QGeoCodeReply
        geocode(self, str, int, int, QGeoShape) -> QGeoCodeReply
        """
        return QGeoCodeReply

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def locale(self): # real signature unknown; restored from __doc__
        """ locale(self) -> QLocale """
        pass

    def managerName(self): # real signature unknown; restored from __doc__
        """ managerName(self) -> str """
        return ""

    def managerVersion(self): # real signature unknown; restored from __doc__
        """ managerVersion(self) -> int """
        return 0

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def reverseGeocode(self, QGeoCoordinate, QGeoShape): # real signature unknown; restored from __doc__
        """ reverseGeocode(self, QGeoCoordinate, QGeoShape) -> QGeoCodeReply """
        return QGeoCodeReply

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setLocale(self, QLocale): # real signature unknown; restored from __doc__
        """ setLocale(self, QLocale) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, Dict, p_str=None, Any=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


