# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QGestureEvent(__PyQt5_QtCore.QEvent):
    """
    QGestureEvent(Iterable[QGesture])
    QGestureEvent(QGestureEvent)
    """
    def accept(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        accept(self)
        accept(self, QGesture)
        accept(self, Qt.GestureType)
        """
        pass

    def activeGestures(self): # real signature unknown; restored from __doc__
        """ activeGestures(self) -> List[QGesture] """
        return []

    def canceledGestures(self): # real signature unknown; restored from __doc__
        """ canceledGestures(self) -> List[QGesture] """
        return []

    def gesture(self, Qt_GestureType): # real signature unknown; restored from __doc__
        """ gesture(self, Qt.GestureType) -> QGesture """
        return QGesture

    def gestures(self): # real signature unknown; restored from __doc__
        """ gestures(self) -> List[QGesture] """
        return []

    def ignore(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        ignore(self)
        ignore(self, QGesture)
        ignore(self, Qt.GestureType)
        """
        pass

    def isAccepted(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        isAccepted(self) -> bool
        isAccepted(self, QGesture) -> bool
        isAccepted(self, Qt.GestureType) -> bool
        """
        return False

    def mapToGraphicsScene(self, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ mapToGraphicsScene(self, Union[QPointF, QPoint]) -> QPointF """
        pass

    def setAccepted(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setAccepted(self, bool)
        setAccepted(self, QGesture, bool)
        setAccepted(self, Qt.GestureType, bool)
        """
        pass

    def widget(self): # real signature unknown; restored from __doc__
        """ widget(self) -> QWidget """
        return QWidget

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


