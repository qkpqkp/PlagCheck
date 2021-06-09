# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QMutex(__sip.simplewrapper):
    """ QMutex(mode: QMutex.RecursionMode = QMutex.NonRecursive) """
    def isRecursive(self): # real signature unknown; restored from __doc__
        """ isRecursive(self) -> bool """
        return False

    def lock(self): # real signature unknown; restored from __doc__
        """ lock(self) """
        pass

    def tryLock(self, timeout=0): # real signature unknown; restored from __doc__
        """ tryLock(self, timeout: int = 0) -> bool """
        return False

    def unlock(self): # real signature unknown; restored from __doc__
        """ unlock(self) """
        pass

    def __init__(self, mode=None): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    NonRecursive = 0
    Recursive = 1


