# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QObject import QObject

class QThread(QObject):
    """ QThread(parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def currentThread(self): # real signature unknown; restored from __doc__
        """ currentThread() -> QThread """
        return QThread

    def currentThreadId(self): # real signature unknown; restored from __doc__
        """ currentThreadId() -> sip.voidptr """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def eventDispatcher(self): # real signature unknown; restored from __doc__
        """ eventDispatcher(self) -> QAbstractEventDispatcher """
        return QAbstractEventDispatcher

    def exec(self): # real signature unknown; restored from __doc__
        """ exec(self) -> int """
        return 0

    def exec_(self): # real signature unknown; restored from __doc__
        """ exec_(self) -> int """
        return 0

    def exit(self, returnCode=0): # real signature unknown; restored from __doc__
        """ exit(self, returnCode: int = 0) """
        pass

    def finished(self): # real signature unknown; restored from __doc__
        """ finished(self) [signal] """
        pass

    def idealThreadCount(self): # real signature unknown; restored from __doc__
        """ idealThreadCount() -> int """
        return 0

    def isFinished(self): # real signature unknown; restored from __doc__
        """ isFinished(self) -> bool """
        return False

    def isInterruptionRequested(self): # real signature unknown; restored from __doc__
        """ isInterruptionRequested(self) -> bool """
        return False

    def isRunning(self): # real signature unknown; restored from __doc__
        """ isRunning(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def loopLevel(self): # real signature unknown; restored from __doc__
        """ loopLevel(self) -> int """
        return 0

    def msleep(self, p_int): # real signature unknown; restored from __doc__
        """ msleep(int) """
        pass

    def priority(self): # real signature unknown; restored from __doc__
        """ priority(self) -> QThread.Priority """
        pass

    def quit(self): # real signature unknown; restored from __doc__
        """ quit(self) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def requestInterruption(self): # real signature unknown; restored from __doc__
        """ requestInterruption(self) """
        pass

    def run(self): # real signature unknown; restored from __doc__
        """ run(self) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setEventDispatcher(self, QAbstractEventDispatcher): # real signature unknown; restored from __doc__
        """ setEventDispatcher(self, QAbstractEventDispatcher) """
        pass

    def setPriority(self, QThread_Priority): # real signature unknown; restored from __doc__
        """ setPriority(self, QThread.Priority) """
        pass

    def setStackSize(self, p_int): # real signature unknown; restored from __doc__
        """ setStackSize(self, int) """
        pass

    def setTerminationEnabled(self, enabled=True): # real signature unknown; restored from __doc__
        """ setTerminationEnabled(enabled: bool = True) """
        pass

    def sleep(self, p_int): # real signature unknown; restored from __doc__
        """ sleep(int) """
        pass

    def stackSize(self): # real signature unknown; restored from __doc__
        """ stackSize(self) -> int """
        return 0

    def start(self, priority=None): # real signature unknown; restored from __doc__
        """ start(self, priority: QThread.Priority = QThread.InheritPriority) """
        pass

    def started(self): # real signature unknown; restored from __doc__
        """ started(self) [signal] """
        pass

    def terminate(self): # real signature unknown; restored from __doc__
        """ terminate(self) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def usleep(self, p_int): # real signature unknown; restored from __doc__
        """ usleep(int) """
        pass

    def wait(self, msecs=None): # real signature unknown; restored from __doc__
        """ wait(self, msecs: int = ULONG_MAX) -> bool """
        return False

    def yieldCurrentThread(self): # real signature unknown; restored from __doc__
        """ yieldCurrentThread() """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    HighestPriority = 5
    HighPriority = 4
    IdlePriority = 0
    InheritPriority = 7
    LowestPriority = 1
    LowPriority = 2
    NormalPriority = 3
    TimeCriticalPriority = 6


