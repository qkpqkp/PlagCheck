# encoding: utf-8
# module PyQt5.QtLocation
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtLocation.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QGeoCodingManager(__PyQt5_QtCore.QObject):
    # no doc
    def error(self, QGeoCodeReply, QGeoCodeReply_Error, errorString=''): # real signature unknown; restored from __doc__
        """ error(self, QGeoCodeReply, QGeoCodeReply.Error, errorString: str = '') [signal] """
        pass

    def finished(self, QGeoCodeReply): # real signature unknown; restored from __doc__
        """ finished(self, QGeoCodeReply) [signal] """
        pass

    def geocode(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        geocode(self, QGeoAddress, bounds: QGeoShape = QGeoShape()) -> QGeoCodeReply
        geocode(self, str, limit: int = -1, offset: int = 0, bounds: QGeoShape = QGeoShape()) -> QGeoCodeReply
        """
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

    def reverseGeocode(self, QGeoCoordinate, bounds=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ reverseGeocode(self, QGeoCoordinate, bounds: QGeoShape = QGeoShape()) -> QGeoCodeReply """
        pass

    def setLocale(self, QLocale): # real signature unknown; restored from __doc__
        """ setLocale(self, QLocale) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


