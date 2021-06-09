# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QReadLocker(__sip.simplewrapper):
    """ QReadLocker(QReadWriteLock) """
    def readWriteLock(self): # real signature unknown; restored from __doc__
        """ readWriteLock(self) -> QReadWriteLock """
        return QReadWriteLock

    def relock(self): # real signature unknown; restored from __doc__
        """ relock(self) """
        pass

    def unlock(self): # real signature unknown; restored from __doc__
        """ unlock(self) """
        pass

    def __enter__(self): # real signature unknown; restored from __doc__
        """ __enter__(self) -> object """
        return object()

    def __exit__(self, p_object, p_object_1, p_object_2): # real signature unknown; restored from __doc__
        """ __exit__(self, object, object, object) """
        pass

    def __init__(self, QReadWriteLock): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



