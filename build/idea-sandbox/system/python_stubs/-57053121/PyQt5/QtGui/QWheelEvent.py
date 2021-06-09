# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QInputEvent import QInputEvent

class QWheelEvent(QInputEvent):
    """
    QWheelEvent(Union[QPointF, QPoint], Union[QPointF, QPoint], QPoint, QPoint, int, Qt.Orientation, Union[Qt.MouseButtons, Qt.MouseButton], Union[Qt.KeyboardModifiers, Qt.KeyboardModifier])
    QWheelEvent(Union[QPointF, QPoint], Union[QPointF, QPoint], QPoint, QPoint, int, Qt.Orientation, Union[Qt.MouseButtons, Qt.MouseButton], Union[Qt.KeyboardModifiers, Qt.KeyboardModifier], Qt.ScrollPhase)
    QWheelEvent(Union[QPointF, QPoint], Union[QPointF, QPoint], QPoint, QPoint, int, Qt.Orientation, Union[Qt.MouseButtons, Qt.MouseButton], Union[Qt.KeyboardModifiers, Qt.KeyboardModifier], Qt.ScrollPhase, Qt.MouseEventSource)
    QWheelEvent(Union[QPointF, QPoint], Union[QPointF, QPoint], QPoint, QPoint, int, Qt.Orientation, Union[Qt.MouseButtons, Qt.MouseButton], Union[Qt.KeyboardModifiers, Qt.KeyboardModifier], Qt.ScrollPhase, Qt.MouseEventSource, bool)
    QWheelEvent(Union[QPointF, QPoint], Union[QPointF, QPoint], QPoint, QPoint, Union[Qt.MouseButtons, Qt.MouseButton], Union[Qt.KeyboardModifiers, Qt.KeyboardModifier], Qt.ScrollPhase, bool, source: Qt.MouseEventSource = Qt.MouseEventNotSynthesized)
    QWheelEvent(QWheelEvent)
    """
    def angleDelta(self): # real signature unknown; restored from __doc__
        """ angleDelta(self) -> QPoint """
        pass

    def buttons(self): # real signature unknown; restored from __doc__
        """ buttons(self) -> Qt.MouseButtons """
        pass

    def globalPos(self): # real signature unknown; restored from __doc__
        """ globalPos(self) -> QPoint """
        pass

    def globalPosF(self): # real signature unknown; restored from __doc__
        """ globalPosF(self) -> QPointF """
        pass

    def globalX(self): # real signature unknown; restored from __doc__
        """ globalX(self) -> int """
        return 0

    def globalY(self): # real signature unknown; restored from __doc__
        """ globalY(self) -> int """
        return 0

    def inverted(self): # real signature unknown; restored from __doc__
        """ inverted(self) -> bool """
        return False

    def phase(self): # real signature unknown; restored from __doc__
        """ phase(self) -> Qt.ScrollPhase """
        pass

    def pixelDelta(self): # real signature unknown; restored from __doc__
        """ pixelDelta(self) -> QPoint """
        pass

    def pos(self): # real signature unknown; restored from __doc__
        """ pos(self) -> QPoint """
        pass

    def posF(self): # real signature unknown; restored from __doc__
        """ posF(self) -> QPointF """
        pass

    def source(self): # real signature unknown; restored from __doc__
        """ source(self) -> Qt.MouseEventSource """
        pass

    def x(self): # real signature unknown; restored from __doc__
        """ x(self) -> int """
        return 0

    def y(self): # real signature unknown; restored from __doc__
        """ y(self) -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


