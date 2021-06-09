# encoding: utf-8
# module PyQt5.QtLocation
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtLocation.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QPlaceReply import QPlaceReply

class QPlaceIdReply(QPlaceReply):
    """ QPlaceIdReply(QPlaceIdReply.OperationType, parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def id(self): # real signature unknown; restored from __doc__
        """ id(self) -> str """
        return ""

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def operationType(self): # real signature unknown; restored from __doc__
        """ operationType(self) -> QPlaceIdReply.OperationType """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setError(self, *args, **kwargs): # real signature unknown
        pass

    def setFinished(self, *args, **kwargs): # real signature unknown
        pass

    def setId(self, p_str): # real signature unknown; restored from __doc__
        """ setId(self, str) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QPlaceReply.Type """
        pass

    def __init__(self, QPlaceIdReply_OperationType, parent=None): # real signature unknown; restored from __doc__
        pass

    RemoveCategory = 3
    RemovePlace = 2
    SaveCategory = 1
    SavePlace = 0


