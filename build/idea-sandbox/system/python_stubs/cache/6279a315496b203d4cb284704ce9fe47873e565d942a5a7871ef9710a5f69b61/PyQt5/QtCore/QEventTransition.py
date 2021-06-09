# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QAbstractTransition import QAbstractTransition

class QEventTransition(QAbstractTransition):
    """
    QEventTransition(sourceState: QState = None)
    QEventTransition(QObject, QEvent.Type, sourceState: QState = None)
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

    def eventSource(self): # real signature unknown; restored from __doc__
        """ eventSource(self) -> QObject """
        return QObject

    def eventTest(self, QEvent): # real signature unknown; restored from __doc__
        """ eventTest(self, QEvent) -> bool """
        return False

    def eventType(self): # real signature unknown; restored from __doc__
        """ eventType(self) -> QEvent.Type """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def onTransition(self, QEvent): # real signature unknown; restored from __doc__
        """ onTransition(self, QEvent) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setEventSource(self, QObject): # real signature unknown; restored from __doc__
        """ setEventSource(self, QObject) """
        pass

    def setEventType(self, QEvent_Type): # real signature unknown; restored from __doc__
        """ setEventType(self, QEvent.Type) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


