# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QObject import QObject

class QSignalMapper(QObject):
    """ QSignalMapper(parent: QObject = None) """
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

    def map(self, QObject=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        map(self)
        map(self, QObject)
        """
        pass

    def mapped(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mapped(self, int) [signal]
        mapped(self, str) [signal]
        mapped(self, QObject) [signal]
        """
        pass

    def mapping(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mapping(self, int) -> QObject
        mapping(self, str) -> QObject
        mapping(self, QWidget) -> QObject
        mapping(self, QObject) -> QObject
        """
        return QObject

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeMappings(self, QObject): # real signature unknown; restored from __doc__
        """ removeMappings(self, QObject) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setMapping(self, QObject, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setMapping(self, QObject, int)
        setMapping(self, QObject, str)
        setMapping(self, QObject, QWidget)
        setMapping(self, QObject, QObject)
        """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


