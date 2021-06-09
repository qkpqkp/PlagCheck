# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QMetaObject(__sip.simplewrapper):
    """
    QMetaObject()
    QMetaObject(QMetaObject)
    """
    def checkConnectArgs(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        checkConnectArgs(str, str) -> bool
        checkConnectArgs(QMetaMethod, QMetaMethod) -> bool
        """
        return False

    def classInfo(self, p_int): # real signature unknown; restored from __doc__
        """ classInfo(self, int) -> QMetaClassInfo """
        return QMetaClassInfo

    def classInfoCount(self): # real signature unknown; restored from __doc__
        """ classInfoCount(self) -> int """
        return 0

    def classInfoOffset(self): # real signature unknown; restored from __doc__
        """ classInfoOffset(self) -> int """
        return 0

    def className(self): # real signature unknown; restored from __doc__
        """ className(self) -> str """
        return ""

    def connectSlotsByName(self, QObject): # real signature unknown; restored from __doc__
        """ connectSlotsByName(QObject) """
        pass

    def constructor(self, p_int): # real signature unknown; restored from __doc__
        """ constructor(self, int) -> QMetaMethod """
        return QMetaMethod

    def constructorCount(self): # real signature unknown; restored from __doc__
        """ constructorCount(self) -> int """
        return 0

    def enumerator(self, p_int): # real signature unknown; restored from __doc__
        """ enumerator(self, int) -> QMetaEnum """
        return QMetaEnum

    def enumeratorCount(self): # real signature unknown; restored from __doc__
        """ enumeratorCount(self) -> int """
        return 0

    def enumeratorOffset(self): # real signature unknown; restored from __doc__
        """ enumeratorOffset(self) -> int """
        return 0

    def indexOfClassInfo(self, p_str): # real signature unknown; restored from __doc__
        """ indexOfClassInfo(self, str) -> int """
        return 0

    def indexOfConstructor(self, p_str): # real signature unknown; restored from __doc__
        """ indexOfConstructor(self, str) -> int """
        return 0

    def indexOfEnumerator(self, p_str): # real signature unknown; restored from __doc__
        """ indexOfEnumerator(self, str) -> int """
        return 0

    def indexOfMethod(self, p_str): # real signature unknown; restored from __doc__
        """ indexOfMethod(self, str) -> int """
        return 0

    def indexOfProperty(self, p_str): # real signature unknown; restored from __doc__
        """ indexOfProperty(self, str) -> int """
        return 0

    def indexOfSignal(self, p_str): # real signature unknown; restored from __doc__
        """ indexOfSignal(self, str) -> int """
        return 0

    def indexOfSlot(self, p_str): # real signature unknown; restored from __doc__
        """ indexOfSlot(self, str) -> int """
        return 0

    def inherits(self, QMetaObject): # real signature unknown; restored from __doc__
        """ inherits(self, QMetaObject) -> bool """
        return False

    def invokeMethod(self, QObject, p_str, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        invokeMethod(QObject, str, Qt.ConnectionType, QGenericReturnArgument, value0: QGenericArgument = QGenericArgument(0,0), value1: QGenericArgument = QGenericArgument(0,0), value2: QGenericArgument = QGenericArgument(0,0), value3: QGenericArgument = QGenericArgument(0,0), value4: QGenericArgument = QGenericArgument(0,0), value5: QGenericArgument = QGenericArgument(0,0), value6: QGenericArgument = QGenericArgument(0,0), value7: QGenericArgument = QGenericArgument(0,0), value8: QGenericArgument = QGenericArgument(0,0), value9: QGenericArgument = QGenericArgument(0,0)) -> object
        invokeMethod(QObject, str, QGenericReturnArgument, value0: QGenericArgument = QGenericArgument(0,0), value1: QGenericArgument = QGenericArgument(0,0), value2: QGenericArgument = QGenericArgument(0,0), value3: QGenericArgument = QGenericArgument(0,0), value4: QGenericArgument = QGenericArgument(0,0), value5: QGenericArgument = QGenericArgument(0,0), value6: QGenericArgument = QGenericArgument(0,0), value7: QGenericArgument = QGenericArgument(0,0), value8: QGenericArgument = QGenericArgument(0,0), value9: QGenericArgument = QGenericArgument(0,0)) -> object
        invokeMethod(QObject, str, Qt.ConnectionType, value0: QGenericArgument = QGenericArgument(0,0), value1: QGenericArgument = QGenericArgument(0,0), value2: QGenericArgument = QGenericArgument(0,0), value3: QGenericArgument = QGenericArgument(0,0), value4: QGenericArgument = QGenericArgument(0,0), value5: QGenericArgument = QGenericArgument(0,0), value6: QGenericArgument = QGenericArgument(0,0), value7: QGenericArgument = QGenericArgument(0,0), value8: QGenericArgument = QGenericArgument(0,0), value9: QGenericArgument = QGenericArgument(0,0)) -> object
        invokeMethod(QObject, str, value0: QGenericArgument = QGenericArgument(0,0), value1: QGenericArgument = QGenericArgument(0,0), value2: QGenericArgument = QGenericArgument(0,0), value3: QGenericArgument = QGenericArgument(0,0), value4: QGenericArgument = QGenericArgument(0,0), value5: QGenericArgument = QGenericArgument(0,0), value6: QGenericArgument = QGenericArgument(0,0), value7: QGenericArgument = QGenericArgument(0,0), value8: QGenericArgument = QGenericArgument(0,0), value9: QGenericArgument = QGenericArgument(0,0)) -> object
        """
        pass

    def method(self, p_int): # real signature unknown; restored from __doc__
        """ method(self, int) -> QMetaMethod """
        return QMetaMethod

    def methodCount(self): # real signature unknown; restored from __doc__
        """ methodCount(self) -> int """
        return 0

    def methodOffset(self): # real signature unknown; restored from __doc__
        """ methodOffset(self) -> int """
        return 0

    def normalizedSignature(self, p_str): # real signature unknown; restored from __doc__
        """ normalizedSignature(str) -> QByteArray """
        return QByteArray

    def normalizedType(self, p_str): # real signature unknown; restored from __doc__
        """ normalizedType(str) -> QByteArray """
        return QByteArray

    def property(self, p_int): # real signature unknown; restored from __doc__
        """ property(self, int) -> QMetaProperty """
        return QMetaProperty

    def propertyCount(self): # real signature unknown; restored from __doc__
        """ propertyCount(self) -> int """
        return 0

    def propertyOffset(self): # real signature unknown; restored from __doc__
        """ propertyOffset(self) -> int """
        return 0

    def superClass(self): # real signature unknown; restored from __doc__
        """ superClass(self) -> QMetaObject """
        return QMetaObject

    def userProperty(self): # real signature unknown; restored from __doc__
        """ userProperty(self) -> QMetaProperty """
        return QMetaProperty

    def __init__(self, QMetaObject=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""




