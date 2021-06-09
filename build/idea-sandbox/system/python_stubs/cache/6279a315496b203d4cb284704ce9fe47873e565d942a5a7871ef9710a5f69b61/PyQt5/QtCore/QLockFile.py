# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QLockFile(__sip.simplewrapper):
    """ QLockFile(str) """
    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> QLockFile.LockError """
        pass

    def getLockInfo(self): # real signature unknown; restored from __doc__
        """ getLockInfo(self) -> Tuple[bool, int, str, str] """
        pass

    def isLocked(self): # real signature unknown; restored from __doc__
        """ isLocked(self) -> bool """
        return False

    def lock(self): # real signature unknown; restored from __doc__
        """ lock(self) -> bool """
        return False

    def removeStaleLockFile(self): # real signature unknown; restored from __doc__
        """ removeStaleLockFile(self) -> bool """
        return False

    def setStaleLockTime(self, p_int): # real signature unknown; restored from __doc__
        """ setStaleLockTime(self, int) """
        pass

    def staleLockTime(self): # real signature unknown; restored from __doc__
        """ staleLockTime(self) -> int """
        return 0

    def tryLock(self, timeout=0): # real signature unknown; restored from __doc__
        """ tryLock(self, timeout: int = 0) -> bool """
        return False

    def unlock(self): # real signature unknown; restored from __doc__
        """ unlock(self) """
        pass

    def __init__(self, p_str): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    LockFailedError = 1
    NoError = 0
    PermissionError = 2
    UnknownError = 3


