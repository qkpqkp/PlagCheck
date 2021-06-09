# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QInputEvent import QInputEvent

class QTouchEvent(QInputEvent):
    """
    QTouchEvent(QEvent.Type, device: QTouchDevice = None, modifiers: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, touchPointStates: Union[Qt.TouchPointStates, Qt.TouchPointState] = Qt.TouchPointStates(), touchPoints: Iterable[QTouchEvent.TouchPoint] = [])
    QTouchEvent(QTouchEvent)
    """
    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> QTouchDevice """
        return QTouchDevice

    def setDevice(self, QTouchDevice): # real signature unknown; restored from __doc__
        """ setDevice(self, QTouchDevice) """
        pass

    def target(self): # real signature unknown; restored from __doc__
        """ target(self) -> QObject """
        pass

    def touchPoints(self): # real signature unknown; restored from __doc__
        """ touchPoints(self) -> List[QTouchEvent.TouchPoint] """
        return []

    def touchPointStates(self): # real signature unknown; restored from __doc__
        """ touchPointStates(self) -> Qt.TouchPointStates """
        pass

    def window(self): # real signature unknown; restored from __doc__
        """ window(self) -> QWindow """
        return QWindow

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass



