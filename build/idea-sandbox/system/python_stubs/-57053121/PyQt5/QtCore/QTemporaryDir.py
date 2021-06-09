# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QTemporaryDir(__sip.simplewrapper):
    """
    QTemporaryDir()
    QTemporaryDir(str)
    """
    def autoRemove(self): # real signature unknown; restored from __doc__
        """ autoRemove(self) -> bool """
        return False

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def filePath(self, p_str): # real signature unknown; restored from __doc__
        """ filePath(self, str) -> str """
        return ""

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def path(self): # real signature unknown; restored from __doc__
        """ path(self) -> str """
        return ""

    def remove(self): # real signature unknown; restored from __doc__
        """ remove(self) -> bool """
        return False

    def setAutoRemove(self, bool): # real signature unknown; restored from __doc__
        """ setAutoRemove(self, bool) """
        pass

    def __init__(self, p_str=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



