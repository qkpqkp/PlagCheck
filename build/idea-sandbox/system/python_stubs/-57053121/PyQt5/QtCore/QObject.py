# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QObject(__sip.wrapper):
    """ QObject(parent: QObject = None) """
    def blockSignals(self, bool): # real signature unknown; restored from __doc__
        """ blockSignals(self, bool) -> bool """
        return False

    def childEvent(self, QChildEvent): # real signature unknown; restored from __doc__
        """ childEvent(self, QChildEvent) """
        pass

    def children(self): # real signature unknown; restored from __doc__
        """ children(self) -> List[QObject] """
        return []

    def connectNotify(self, QMetaMethod): # real signature unknown; restored from __doc__
        """ connectNotify(self, QMetaMethod) """
        pass

    def customEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ customEvent(self, QEvent) """
        pass

    def deleteLater(self): # real signature unknown; restored from __doc__
        """ deleteLater(self) """
        pass

    def destroyed(self, p_object=None): # real signature unknown; restored from __doc__
        """ destroyed(self, object: QObject = None) [signal] """
        pass

    def disconnect(self): # real signature unknown; restored from __doc__
        """ disconnect(self) """
        pass

    def disconnectNotify(self, QMetaMethod): # real signature unknown; restored from __doc__
        """ disconnectNotify(self, QMetaMethod) """
        pass

    def dumpObjectInfo(self): # real signature unknown; restored from __doc__
        """ dumpObjectInfo(self) """
        pass

    def dumpObjectTree(self): # real signature unknown; restored from __doc__
        """ dumpObjectTree(self) """
        pass

    def dynamicPropertyNames(self): # real signature unknown; restored from __doc__
        """ dynamicPropertyNames(self) -> List[QByteArray] """
        return []

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def eventFilter(self, QObject, QEvent): # real signature unknown; restored from __doc__
        """ eventFilter(self, QObject, QEvent) -> bool """
        return False

    def findChild(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject
        findChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject
        """
        pass

    def findChildren(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]
        findChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]
        findChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]
        findChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]
        findChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]
        findChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]
        """
        pass

    def inherits(self, p_str): # real signature unknown; restored from __doc__
        """ inherits(self, str) -> bool """
        return False

    def installEventFilter(self, QObject): # real signature unknown; restored from __doc__
        """ installEventFilter(self, QObject) """
        pass

    def isSignalConnected(self, QMetaMethod): # real signature unknown; restored from __doc__
        """ isSignalConnected(self, QMetaMethod) -> bool """
        return False

    def isWidgetType(self): # real signature unknown; restored from __doc__
        """ isWidgetType(self) -> bool """
        return False

    def isWindowType(self): # real signature unknown; restored from __doc__
        """ isWindowType(self) -> bool """
        return False

    def killTimer(self, p_int): # real signature unknown; restored from __doc__
        """ killTimer(self, int) """
        pass

    def metaObject(self): # real signature unknown; restored from __doc__
        """ metaObject(self) -> QMetaObject """
        return QMetaObject

    def moveToThread(self, QThread): # real signature unknown; restored from __doc__
        """ moveToThread(self, QThread) """
        pass

    def objectName(self): # real signature unknown; restored from __doc__
        """ objectName(self) -> str """
        return ""

    def objectNameChanged(self, p_str): # real signature unknown; restored from __doc__
        """ objectNameChanged(self, str) [signal] """
        pass

    def parent(self): # real signature unknown; restored from __doc__
        """ parent(self) -> QObject """
        return QObject

    def property(self, p_str): # real signature unknown; restored from __doc__
        """ property(self, str) -> Any """
        pass

    def pyqtConfigure(self, *more): # real signature unknown; restored from __doc__
        """
        QObject.pyqtConfigure(...)
        
        Each keyword argument is either the name of a Qt property or a Qt signal.
        For properties the property is set to the given value which should be of an
        appropriate type.
        For signals the signal is connected to the given value which should be a
        callable.
        """
        pass

    def receivers(self, PYQT_SIGNAL): # real signature unknown; restored from __doc__
        """ receivers(self, PYQT_SIGNAL) -> int """
        return 0

    def removeEventFilter(self, QObject): # real signature unknown; restored from __doc__
        """ removeEventFilter(self, QObject) """
        pass

    def sender(self): # real signature unknown; restored from __doc__
        """ sender(self) -> QObject """
        return QObject

    def senderSignalIndex(self): # real signature unknown; restored from __doc__
        """ senderSignalIndex(self) -> int """
        return 0

    def setObjectName(self, p_str): # real signature unknown; restored from __doc__
        """ setObjectName(self, str) """
        pass

    def setParent(self, QObject): # real signature unknown; restored from __doc__
        """ setParent(self, QObject) """
        pass

    def setProperty(self, p_str, Any): # real signature unknown; restored from __doc__
        """ setProperty(self, str, Any) -> bool """
        return False

    def signalsBlocked(self): # real signature unknown; restored from __doc__
        """ signalsBlocked(self) -> bool """
        return False

    def startTimer(self, p_int, timerType=None): # real signature unknown; restored from __doc__
        """ startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int """
        return 0

    def thread(self): # real signature unknown; restored from __doc__
        """ thread(self) -> QThread """
        return QThread

    def timerEvent(self, QTimerEvent): # real signature unknown; restored from __doc__
        """ timerEvent(self, QTimerEvent) """
        pass

    def tr(self, p_str, disambiguation=None, n=-1): # real signature unknown; restored from __doc__
        """ tr(self, str, disambiguation: str = None, n: int = -1) -> str """
        return ""

    def __getattr__(self, p_str): # real signature unknown; restored from __doc__
        """ __getattr__(self, str) -> object """
        return object()

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""




