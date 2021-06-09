# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QMediaObject(__PyQt5_QtCore.QObject):
    """ QMediaObject(QObject, QMediaService) """
    def addPropertyWatch(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ addPropertyWatch(self, Union[QByteArray, bytes, bytearray]) """
        pass

    def availability(self): # real signature unknown; restored from __doc__
        """ availability(self) -> QMultimedia.AvailabilityStatus """
        pass

    def availabilityChanged(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        availabilityChanged(self, QMultimedia.AvailabilityStatus) [signal]
        availabilityChanged(self, bool) [signal]
        """
        pass

    def availableMetaData(self): # real signature unknown; restored from __doc__
        """ availableMetaData(self) -> List[str] """
        return []

    def bind(self, QObject): # real signature unknown; restored from __doc__
        """ bind(self, QObject) -> bool """
        return False

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isAvailable(self): # real signature unknown; restored from __doc__
        """ isAvailable(self) -> bool """
        return False

    def isMetaDataAvailable(self): # real signature unknown; restored from __doc__
        """ isMetaDataAvailable(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def metaData(self, p_str): # real signature unknown; restored from __doc__
        """ metaData(self, str) -> Any """
        pass

    def metaDataAvailableChanged(self, bool): # real signature unknown; restored from __doc__
        """ metaDataAvailableChanged(self, bool) [signal] """
        pass

    def metaDataChanged(self, p_str=None, Any=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        metaDataChanged(self) [signal]
        metaDataChanged(self, str, Any) [signal]
        """
        pass

    def notifyInterval(self): # real signature unknown; restored from __doc__
        """ notifyInterval(self) -> int """
        return 0

    def notifyIntervalChanged(self, p_int): # real signature unknown; restored from __doc__
        """ notifyIntervalChanged(self, int) [signal] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removePropertyWatch(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ removePropertyWatch(self, Union[QByteArray, bytes, bytearray]) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def service(self): # real signature unknown; restored from __doc__
        """ service(self) -> QMediaService """
        return QMediaService

    def setNotifyInterval(self, p_int): # real signature unknown; restored from __doc__
        """ setNotifyInterval(self, int) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def unbind(self, QObject): # real signature unknown; restored from __doc__
        """ unbind(self, QObject) """
        pass

    def __init__(self, QObject, QMediaService): # real signature unknown; restored from __doc__
        pass


