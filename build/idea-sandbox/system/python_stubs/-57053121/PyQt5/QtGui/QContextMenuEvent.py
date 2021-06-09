# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QInputEvent import QInputEvent

class QContextMenuEvent(QInputEvent):
    """
    QContextMenuEvent(QContextMenuEvent.Reason, QPoint, QPoint, Union[Qt.KeyboardModifiers, Qt.KeyboardModifier])
    QContextMenuEvent(QContextMenuEvent.Reason, QPoint, QPoint)
    QContextMenuEvent(QContextMenuEvent.Reason, QPoint)
    QContextMenuEvent(QContextMenuEvent)
    """
    def globalPos(self): # real signature unknown; restored from __doc__
        """ globalPos(self) -> QPoint """
        pass

    def globalX(self): # real signature unknown; restored from __doc__
        """ globalX(self) -> int """
        return 0

    def globalY(self): # real signature unknown; restored from __doc__
        """ globalY(self) -> int """
        return 0

    def pos(self): # real signature unknown; restored from __doc__
        """ pos(self) -> QPoint """
        pass

    def reason(self): # real signature unknown; restored from __doc__
        """ reason(self) -> QContextMenuEvent.Reason """
        pass

    def x(self): # real signature unknown; restored from __doc__
        """ x(self) -> int """
        return 0

    def y(self): # real signature unknown; restored from __doc__
        """ y(self) -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    Keyboard = 1
    Mouse = 0
    Other = 2


