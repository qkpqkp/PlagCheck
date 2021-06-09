# encoding: utf-8
# module PyQt5.QtWebChannel
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWebChannel.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


# no functions
# classes

class QWebChannel(__PyQt5_QtCore.QObject):
    """ QWebChannel(parent: QObject = None) """
    def blockUpdates(self): # real signature unknown; restored from __doc__
        """ blockUpdates(self) -> bool """
        return False

    def blockUpdatesChanged(self, bool): # real signature unknown; restored from __doc__
        """ blockUpdatesChanged(self, bool) [signal] """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def connectTo(self, QWebChannelAbstractTransport): # real signature unknown; restored from __doc__
        """ connectTo(self, QWebChannelAbstractTransport) """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def deregisterObject(self, QObject): # real signature unknown; restored from __doc__
        """ deregisterObject(self, QObject) """
        pass

    def disconnectFrom(self, QWebChannelAbstractTransport): # real signature unknown; restored from __doc__
        """ disconnectFrom(self, QWebChannelAbstractTransport) """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def registeredObjects(self): # real signature unknown; restored from __doc__
        """ registeredObjects(self) -> Dict[str, QObject] """
        return {}

    def registerObject(self, p_str, QObject): # real signature unknown; restored from __doc__
        """ registerObject(self, str, QObject) """
        pass

    def registerObjects(self, Dict, p_str=None, QObject=None): # real signature unknown; restored from __doc__
        """ registerObjects(self, Dict[str, QObject]) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setBlockUpdates(self, bool): # real signature unknown; restored from __doc__
        """ setBlockUpdates(self, bool) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


class QWebChannelAbstractTransport(__PyQt5_QtCore.QObject):
    """ QWebChannelAbstractTransport(parent: QObject = None) """
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

    def messageReceived(self, Dict, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ messageReceived(self, Dict[str, Union[QJsonValue, QJsonValue.Type, Iterable[QJsonValue], bool, int, float, str]], QWebChannelAbstractTransport) [signal] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def sendMessage(self, Dict, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ sendMessage(self, Dict[str, Union[QJsonValue, QJsonValue.Type, Iterable[QJsonValue], bool, int, float, str]]) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


# variables with complex values



