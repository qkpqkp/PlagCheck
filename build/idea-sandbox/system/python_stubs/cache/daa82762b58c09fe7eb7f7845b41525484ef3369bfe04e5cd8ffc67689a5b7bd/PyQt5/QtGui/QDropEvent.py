# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QDropEvent(__PyQt5_QtCore.QEvent):
    """
    QDropEvent(Union[QPointF, QPoint], Union[Qt.DropActions, Qt.DropAction], QMimeData, Union[Qt.MouseButtons, Qt.MouseButton], Union[Qt.KeyboardModifiers, Qt.KeyboardModifier], type: QEvent.Type = QEvent.Drop)
    QDropEvent(QDropEvent)
    """
    def acceptProposedAction(self): # real signature unknown; restored from __doc__
        """ acceptProposedAction(self) """
        pass

    def dropAction(self): # real signature unknown; restored from __doc__
        """ dropAction(self) -> Qt.DropAction """
        pass

    def keyboardModifiers(self): # real signature unknown; restored from __doc__
        """ keyboardModifiers(self) -> Qt.KeyboardModifiers """
        pass

    def mimeData(self): # real signature unknown; restored from __doc__
        """ mimeData(self) -> QMimeData """
        pass

    def mouseButtons(self): # real signature unknown; restored from __doc__
        """ mouseButtons(self) -> Qt.MouseButtons """
        pass

    def pos(self): # real signature unknown; restored from __doc__
        """ pos(self) -> QPoint """
        pass

    def posF(self): # real signature unknown; restored from __doc__
        """ posF(self) -> QPointF """
        pass

    def possibleActions(self): # real signature unknown; restored from __doc__
        """ possibleActions(self) -> Qt.DropActions """
        pass

    def proposedAction(self): # real signature unknown; restored from __doc__
        """ proposedAction(self) -> Qt.DropAction """
        pass

    def setDropAction(self, Qt_DropAction): # real signature unknown; restored from __doc__
        """ setDropAction(self, Qt.DropAction) """
        pass

    def source(self): # real signature unknown; restored from __doc__
        """ source(self) -> QObject """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


