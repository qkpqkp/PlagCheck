# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QLoggingCategory(__sip.simplewrapper):
    """
    QLoggingCategory(str)
    QLoggingCategory(str, QtMsgType)
    """
    def categoryName(self): # real signature unknown; restored from __doc__
        """ categoryName(self) -> str """
        return ""

    def defaultCategory(self): # real signature unknown; restored from __doc__
        """ defaultCategory() -> QLoggingCategory """
        return QLoggingCategory

    def isCriticalEnabled(self): # real signature unknown; restored from __doc__
        """ isCriticalEnabled(self) -> bool """
        return False

    def isDebugEnabled(self): # real signature unknown; restored from __doc__
        """ isDebugEnabled(self) -> bool """
        return False

    def isEnabled(self, QtMsgType): # real signature unknown; restored from __doc__
        """ isEnabled(self, QtMsgType) -> bool """
        return False

    def isInfoEnabled(self): # real signature unknown; restored from __doc__
        """ isInfoEnabled(self) -> bool """
        return False

    def isWarningEnabled(self): # real signature unknown; restored from __doc__
        """ isWarningEnabled(self) -> bool """
        return False

    def setEnabled(self, QtMsgType, bool): # real signature unknown; restored from __doc__
        """ setEnabled(self, QtMsgType, bool) """
        pass

    def setFilterRules(self, p_str): # real signature unknown; restored from __doc__
        """ setFilterRules(str) """
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __init__(self, p_str, QtMsgType=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



