# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QAbstractTransition import QAbstractTransition

class QSignalTransition(QAbstractTransition):
    """
    QSignalTransition(sourceState: QState = None)
    QSignalTransition(pyqtBoundSignal, sourceState: QState = None)
    """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def eventTest(self, QEvent): # real signature unknown; restored from __doc__
        """ eventTest(self, QEvent) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def onTransition(self, QEvent): # real signature unknown; restored from __doc__
        """ onTransition(self, QEvent) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderObject(self): # real signature unknown; restored from __doc__
        """ senderObject(self) -> QObject """
        return QObject

    def senderObjectChanged(self): # real signature unknown; restored from __doc__
        """ senderObjectChanged(self) [signal] """
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setSenderObject(self, QObject): # real signature unknown; restored from __doc__
        """ setSenderObject(self, QObject) """
        pass

    def setSignal(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setSignal(self, Union[QByteArray, bytes, bytearray]) """
        pass

    def signal(self): # real signature unknown; restored from __doc__
        """ signal(self) -> QByteArray """
        return QByteArray

    def signalChanged(self): # real signature unknown; restored from __doc__
        """ signalChanged(self) [signal] """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


