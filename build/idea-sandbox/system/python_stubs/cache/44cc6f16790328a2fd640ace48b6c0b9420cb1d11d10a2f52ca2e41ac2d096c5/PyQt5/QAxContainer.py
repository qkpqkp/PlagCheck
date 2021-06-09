# encoding: utf-8
# module PyQt5.QAxContainer
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QAxContainer.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtWidgets as __PyQt5_QtWidgets
import sip as __sip


# no functions
# classes

class QAxBase(__sip.simplewrapper):
    # no doc
    def asVariant(self): # real signature unknown; restored from __doc__
        """ asVariant(self) -> Any """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def control(self): # real signature unknown; restored from __doc__
        """ control(self) -> str """
        return ""

    def disableClassInfo(self): # real signature unknown; restored from __doc__
        """ disableClassInfo(self) """
        pass

    def disableEventSink(self): # real signature unknown; restored from __doc__
        """ disableEventSink(self) """
        pass

    def disableMetaObject(self): # real signature unknown; restored from __doc__
        """ disableMetaObject(self) """
        pass

    def dynamicCall(self, p_str, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        dynamicCall(self, str, Iterable[Any]) -> Any
        dynamicCall(self, str, value1: Any = None, value2: Any = None, value3: Any = None, value4: Any = None, value5: Any = None, value6: Any = None, value7: Any = None, value8: Any = None) -> Any
        """
        pass

    def generateDocumentation(self): # real signature unknown; restored from __doc__
        """ generateDocumentation(self) -> str """
        return ""

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def propertyBag(self): # real signature unknown; restored from __doc__
        """ propertyBag(self) -> Dict[str, Any] """
        return {}

    def propertyWritable(self, p_str): # real signature unknown; restored from __doc__
        """ propertyWritable(self, str) -> bool """
        return False

    def querySubObject(self, p_str, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        querySubObject(self, str, Iterable[Any]) -> QAxObject
        querySubObject(self, str, value1: Any = None, value2: Any = None, value3: Any = None, value4: Any = None, value5: Any = None, value6: Any = None, value7: Any = None, value8: Any = None) -> QAxObject
        """
        return QAxObject

    def setControl(self, p_str): # real signature unknown; restored from __doc__
        """ setControl(self, str) -> bool """
        return False

    def setPropertyBag(self, Dict, p_str=None, Any=None): # real signature unknown; restored from __doc__
        """ setPropertyBag(self, Dict[str, Any]) """
        pass

    def setPropertyWritable(self, p_str, bool): # real signature unknown; restored from __doc__
        """ setPropertyWritable(self, str, bool) """
        pass

    def verbs(self): # real signature unknown; restored from __doc__
        """ verbs(self) -> List[str] """
        return []

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QAxObject(__PyQt5_QtCore.QObject, QAxBase):
    """
    QAxObject(parent: QObject = None)
    QAxObject(str, parent: QObject = None)
    """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, QMetaMethod): # real signature unknown; restored from __doc__
        """ connectNotify(self, QMetaMethod) """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def doVerb(self, p_str): # real signature unknown; restored from __doc__
        """ doVerb(self, str) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


class QAxWidget(__PyQt5_QtWidgets.QWidget, QAxBase):
    """
    QAxWidget(parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = 0)
    QAxWidget(str, parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = 0)
    """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ changeEvent(self, QEvent) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, QMetaMethod): # real signature unknown; restored from __doc__
        """ connectNotify(self, QMetaMethod) """
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def createHostWindow(self, bool): # real signature unknown; restored from __doc__
        """ createHostWindow(self, bool) -> bool """
        return False

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def doVerb(self, p_str): # real signature unknown; restored from __doc__
        """ doVerb(self, str) -> bool """
        return False

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def focusInEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> QSize """
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ resizeEvent(self, QResizeEvent) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def translateKeyEvent(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ translateKeyEvent(self, int, int) -> bool """
        return False

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


# variables with complex values



