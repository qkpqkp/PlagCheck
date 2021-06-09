# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QInputEvent import QInputEvent

class QTabletEvent(QInputEvent):
    """
    QTabletEvent(QEvent.Type, Union[QPointF, QPoint], Union[QPointF, QPoint], int, int, float, int, int, float, float, int, Union[Qt.KeyboardModifiers, Qt.KeyboardModifier], int, Qt.MouseButton, Union[Qt.MouseButtons, Qt.MouseButton])
    QTabletEvent(QEvent.Type, Union[QPointF, QPoint], Union[QPointF, QPoint], int, int, float, int, int, float, float, int, Union[Qt.KeyboardModifiers, Qt.KeyboardModifier], int)
    QTabletEvent(QTabletEvent)
    """
    def button(self): # real signature unknown; restored from __doc__
        """ button(self) -> Qt.MouseButton """
        pass

    def buttons(self): # real signature unknown; restored from __doc__
        """ buttons(self) -> Qt.MouseButtons """
        pass

    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> QTabletEvent.TabletDevice """
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

    def hiResGlobalX(self): # real signature unknown; restored from __doc__
        """ hiResGlobalX(self) -> float """
        return 0.0

    def hiResGlobalY(self): # real signature unknown; restored from __doc__
        """ hiResGlobalY(self) -> float """
        return 0.0

    def pointerType(self): # real signature unknown; restored from __doc__
        """ pointerType(self) -> QTabletEvent.PointerType """
        pass

    def pos(self): # real signature unknown; restored from __doc__
        """ pos(self) -> QPoint """
        pass

    def posF(self): # real signature unknown; restored from __doc__
        """ posF(self) -> QPointF """
        pass

    def pressure(self): # real signature unknown; restored from __doc__
        """ pressure(self) -> float """
        return 0.0

    def rotation(self): # real signature unknown; restored from __doc__
        """ rotation(self) -> float """
        return 0.0

    def tangentialPressure(self): # real signature unknown; restored from __doc__
        """ tangentialPressure(self) -> float """
        return 0.0

    def uniqueId(self): # real signature unknown; restored from __doc__
        """ uniqueId(self) -> int """
        return 0

    def x(self): # real signature unknown; restored from __doc__
        """ x(self) -> int """
        return 0

    def xTilt(self): # real signature unknown; restored from __doc__
        """ xTilt(self) -> int """
        return 0

    def y(self): # real signature unknown; restored from __doc__
        """ y(self) -> int """
        return 0

    def yTilt(self): # real signature unknown; restored from __doc__
        """ yTilt(self) -> int """
        return 0

    def z(self): # real signature unknown; restored from __doc__
        """ z(self) -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    Airbrush = 3
    Cursor = 2
    Eraser = 3
    FourDMouse = 4
    NoDevice = 0
    Pen = 1
    Puck = 1
    RotationStylus = 6
    Stylus = 2
    UnknownPointer = 0
    XFreeEraser = 5


