# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QObject import QObject

class QThreadPool(QObject):
    """ QThreadPool(parent: QObject = None) """
    def activeThreadCount(self): # real signature unknown; restored from __doc__
        """ activeThreadCount(self) -> int """
        return 0

    def cancel(self, QRunnable): # real signature unknown; restored from __doc__
        """ cancel(self, QRunnable) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def expiryTimeout(self): # real signature unknown; restored from __doc__
        """ expiryTimeout(self) -> int """
        return 0

    def globalInstance(self): # real signature unknown; restored from __doc__
        """ globalInstance() -> QThreadPool """
        return QThreadPool

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def maxThreadCount(self): # real signature unknown; restored from __doc__
        """ maxThreadCount(self) -> int """
        return 0

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def releaseThread(self): # real signature unknown; restored from __doc__
        """ releaseThread(self) """
        pass

    def reserveThread(self): # real signature unknown; restored from __doc__
        """ reserveThread(self) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setExpiryTimeout(self, p_int): # real signature unknown; restored from __doc__
        """ setExpiryTimeout(self, int) """
        pass

    def setMaxThreadCount(self, p_int): # real signature unknown; restored from __doc__
        """ setMaxThreadCount(self, int) """
        pass

    def setStackSize(self, p_int): # real signature unknown; restored from __doc__
        """ setStackSize(self, int) """
        pass

    def stackSize(self): # real signature unknown; restored from __doc__
        """ stackSize(self) -> int """
        return 0

    def start(self, QRunnable, priority=0): # real signature unknown; restored from __doc__
        """ start(self, QRunnable, priority: int = 0) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def tryStart(self, QRunnable): # real signature unknown; restored from __doc__
        """ tryStart(self, QRunnable) -> bool """
        return False

    def tryTake(self, QRunnable): # real signature unknown; restored from __doc__
        """ tryTake(self, QRunnable) -> bool """
        return False

    def waitForDone(self, msecs=-1): # real signature unknown; restored from __doc__
        """ waitForDone(self, msecs: int = -1) -> bool """
        return False

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


