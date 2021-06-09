# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QDropEvent import QDropEvent

class QDragMoveEvent(QDropEvent):
    """
    QDragMoveEvent(QPoint, Union[Qt.DropActions, Qt.DropAction], QMimeData, Union[Qt.MouseButtons, Qt.MouseButton], Union[Qt.KeyboardModifiers, Qt.KeyboardModifier], type: QEvent.Type = QEvent.DragMove)
    QDragMoveEvent(QDragMoveEvent)
    """
    def accept(self, QRect=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        accept(self)
        accept(self, QRect)
        """
        pass

    def answerRect(self): # real signature unknown; restored from __doc__
        """ answerRect(self) -> QRect """
        pass

    def ignore(self, QRect=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        ignore(self)
        ignore(self, QRect)
        """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


