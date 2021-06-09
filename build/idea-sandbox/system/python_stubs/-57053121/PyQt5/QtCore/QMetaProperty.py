# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QMetaProperty(__sip.simplewrapper):
    """
    QMetaProperty()
    QMetaProperty(QMetaProperty)
    """
    def enumerator(self): # real signature unknown; restored from __doc__
        """ enumerator(self) -> QMetaEnum """
        return QMetaEnum

    def hasNotifySignal(self): # real signature unknown; restored from __doc__
        """ hasNotifySignal(self) -> bool """
        return False

    def hasStdCppSet(self): # real signature unknown; restored from __doc__
        """ hasStdCppSet(self) -> bool """
        return False

    def isConstant(self): # real signature unknown; restored from __doc__
        """ isConstant(self) -> bool """
        return False

    def isDesignable(self, p_object=None): # real signature unknown; restored from __doc__
        """ isDesignable(self, object: QObject = None) -> bool """
        return False

    def isEnumType(self): # real signature unknown; restored from __doc__
        """ isEnumType(self) -> bool """
        return False

    def isFinal(self): # real signature unknown; restored from __doc__
        """ isFinal(self) -> bool """
        return False

    def isFlagType(self): # real signature unknown; restored from __doc__
        """ isFlagType(self) -> bool """
        return False

    def isReadable(self): # real signature unknown; restored from __doc__
        """ isReadable(self) -> bool """
        return False

    def isResettable(self): # real signature unknown; restored from __doc__
        """ isResettable(self) -> bool """
        return False

    def isScriptable(self, p_object=None): # real signature unknown; restored from __doc__
        """ isScriptable(self, object: QObject = None) -> bool """
        return False

    def isStored(self, p_object=None): # real signature unknown; restored from __doc__
        """ isStored(self, object: QObject = None) -> bool """
        return False

    def isUser(self, p_object=None): # real signature unknown; restored from __doc__
        """ isUser(self, object: QObject = None) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def isWritable(self): # real signature unknown; restored from __doc__
        """ isWritable(self) -> bool """
        return False

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def notifySignal(self): # real signature unknown; restored from __doc__
        """ notifySignal(self) -> QMetaMethod """
        return QMetaMethod

    def notifySignalIndex(self): # real signature unknown; restored from __doc__
        """ notifySignalIndex(self) -> int """
        return 0

    def propertyIndex(self): # real signature unknown; restored from __doc__
        """ propertyIndex(self) -> int """
        return 0

    def read(self, QObject): # real signature unknown; restored from __doc__
        """ read(self, QObject) -> Any """
        pass

    def reset(self, QObject): # real signature unknown; restored from __doc__
        """ reset(self, QObject) -> bool """
        return False

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QVariant.Type """
        pass

    def typeName(self): # real signature unknown; restored from __doc__
        """ typeName(self) -> str """
        return ""

    def userType(self): # real signature unknown; restored from __doc__
        """ userType(self) -> int """
        return 0

    def write(self, QObject, Any): # real signature unknown; restored from __doc__
        """ write(self, QObject, Any) -> bool """
        return False

    def __init__(self, QMetaProperty=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



