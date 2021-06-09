# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QReadWriteLock(__sip.simplewrapper):
    """ QReadWriteLock(recursionMode: QReadWriteLock.RecursionMode = QReadWriteLock.NonRecursive) """
    def lockForRead(self): # real signature unknown; restored from __doc__
        """ lockForRead(self) """
        pass

    def lockForWrite(self): # real signature unknown; restored from __doc__
        """ lockForWrite(self) """
        pass

    def tryLockForRead(self, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        tryLockForRead(self) -> bool
        tryLockForRead(self, int) -> bool
        """
        return False

    def tryLockForWrite(self, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        tryLockForWrite(self) -> bool
        tryLockForWrite(self, int) -> bool
        """
        return False

    def unlock(self): # real signature unknown; restored from __doc__
        """ unlock(self) """
        pass

    def __init__(self, recursionMode=None): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    NonRecursive = 0
    Recursive = 1


