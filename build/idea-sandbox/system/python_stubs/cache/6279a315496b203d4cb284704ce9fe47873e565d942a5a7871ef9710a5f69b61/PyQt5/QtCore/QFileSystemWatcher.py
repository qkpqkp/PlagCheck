# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QObject import QObject

class QFileSystemWatcher(QObject):
    """
    QFileSystemWatcher(parent: QObject = None)
    QFileSystemWatcher(Iterable[str], parent: QObject = None)
    """
    def addPath(self, p_str): # real signature unknown; restored from __doc__
        """ addPath(self, str) -> bool """
        return False

    def addPaths(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ addPaths(self, Iterable[str]) -> List[str] """
        return []

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def directories(self): # real signature unknown; restored from __doc__
        """ directories(self) -> List[str] """
        return []

    def directoryChanged(self, p_str): # real signature unknown; restored from __doc__
        """ directoryChanged(self, str) [signal] """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def fileChanged(self, p_str): # real signature unknown; restored from __doc__
        """ fileChanged(self, str) [signal] """
        pass

    def files(self): # real signature unknown; restored from __doc__
        """ files(self) -> List[str] """
        return []

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removePath(self, p_str): # real signature unknown; restored from __doc__
        """ removePath(self, str) -> bool """
        return False

    def removePaths(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ removePaths(self, Iterable[str]) -> List[str] """
        return []

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


