# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QAbstractState import QAbstractState

class QHistoryState(QAbstractState):
    """
    QHistoryState(parent: QState = None)
    QHistoryState(QHistoryState.HistoryType, parent: QState = None)
    """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultState(self): # real signature unknown; restored from __doc__
        """ defaultState(self) -> QAbstractState """
        return QAbstractState

    def defaultStateChanged(self): # real signature unknown; restored from __doc__
        """ defaultStateChanged(self) [signal] """
        pass

    def defaultTransition(self): # real signature unknown; restored from __doc__
        """ defaultTransition(self) -> QAbstractTransition """
        return QAbstractTransition

    def defaultTransitionChanged(self): # real signature unknown; restored from __doc__
        """ defaultTransitionChanged(self) [signal] """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def historyType(self): # real signature unknown; restored from __doc__
        """ historyType(self) -> QHistoryState.HistoryType """
        pass

    def historyTypeChanged(self): # real signature unknown; restored from __doc__
        """ historyTypeChanged(self) [signal] """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def onEntry(self, QEvent): # real signature unknown; restored from __doc__
        """ onEntry(self, QEvent) """
        pass

    def onExit(self, QEvent): # real signature unknown; restored from __doc__
        """ onExit(self, QEvent) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setDefaultState(self, QAbstractState): # real signature unknown; restored from __doc__
        """ setDefaultState(self, QAbstractState) """
        pass

    def setDefaultTransition(self, QAbstractTransition): # real signature unknown; restored from __doc__
        """ setDefaultTransition(self, QAbstractTransition) """
        pass

    def setHistoryType(self, QHistoryState_HistoryType): # real signature unknown; restored from __doc__
        """ setHistoryType(self, QHistoryState.HistoryType) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    DeepHistory = 1
    ShallowHistory = 0


