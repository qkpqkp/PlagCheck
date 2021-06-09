# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QState import QState

class QStateMachine(QState):
    """
    QStateMachine(parent: QObject = None)
    QStateMachine(QState.ChildMode, parent: QObject = None)
    """
    def addDefaultAnimation(self, QAbstractAnimation): # real signature unknown; restored from __doc__
        """ addDefaultAnimation(self, QAbstractAnimation) """
        pass

    def addState(self, QAbstractState): # real signature unknown; restored from __doc__
        """ addState(self, QAbstractState) """
        pass

    def cancelDelayedEvent(self, p_int): # real signature unknown; restored from __doc__
        """ cancelDelayedEvent(self, int) -> bool """
        return False

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clearError(self): # real signature unknown; restored from __doc__
        """ clearError(self) """
        pass

    def configuration(self): # real signature unknown; restored from __doc__
        """ configuration(self) -> Set[QAbstractState] """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultAnimations(self): # real signature unknown; restored from __doc__
        """ defaultAnimations(self) -> List[QAbstractAnimation] """
        return []

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> QStateMachine.Error """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def eventFilter(self, QObject, QEvent): # real signature unknown; restored from __doc__
        """ eventFilter(self, QObject, QEvent) -> bool """
        return False

    def globalRestorePolicy(self): # real signature unknown; restored from __doc__
        """ globalRestorePolicy(self) -> QState.RestorePolicy """
        pass

    def isAnimated(self): # real signature unknown; restored from __doc__
        """ isAnimated(self) -> bool """
        return False

    def isRunning(self): # real signature unknown; restored from __doc__
        """ isRunning(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def onEntry(self, QEvent): # real signature unknown; restored from __doc__
        """ onEntry(self, QEvent) """
        pass

    def onExit(self, QEvent): # real signature unknown; restored from __doc__
        """ onExit(self, QEvent) """
        pass

    def postDelayedEvent(self, QEvent, p_int): # real signature unknown; restored from __doc__
        """ postDelayedEvent(self, QEvent, int) -> int """
        return 0

    def postEvent(self, QEvent, priority=None): # real signature unknown; restored from __doc__
        """ postEvent(self, QEvent, priority: QStateMachine.EventPriority = QStateMachine.NormalPriority) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeDefaultAnimation(self, QAbstractAnimation): # real signature unknown; restored from __doc__
        """ removeDefaultAnimation(self, QAbstractAnimation) """
        pass

    def removeState(self, QAbstractState): # real signature unknown; restored from __doc__
        """ removeState(self, QAbstractState) """
        pass

    def runningChanged(self, bool): # real signature unknown; restored from __doc__
        """ runningChanged(self, bool) [signal] """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAnimated(self, bool): # real signature unknown; restored from __doc__
        """ setAnimated(self, bool) """
        pass

    def setGlobalRestorePolicy(self, QState_RestorePolicy): # real signature unknown; restored from __doc__
        """ setGlobalRestorePolicy(self, QState.RestorePolicy) """
        pass

    def setRunning(self, bool): # real signature unknown; restored from __doc__
        """ setRunning(self, bool) """
        pass

    def start(self): # real signature unknown; restored from __doc__
        """ start(self) """
        pass

    def started(self): # real signature unknown; restored from __doc__
        """ started(self) [signal] """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) """
        pass

    def stopped(self): # real signature unknown; restored from __doc__
        """ stopped(self) [signal] """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    HighPriority = 1
    NoCommonAncestorForTransitionError = 3
    NoDefaultStateInHistoryStateError = 2
    NoError = 0
    NoInitialStateError = 1
    NormalPriority = 0


