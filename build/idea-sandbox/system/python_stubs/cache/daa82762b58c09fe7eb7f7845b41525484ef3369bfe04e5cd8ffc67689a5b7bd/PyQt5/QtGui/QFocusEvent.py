# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QFocusEvent(__PyQt5_QtCore.QEvent):
    """
    QFocusEvent(QEvent.Type, reason: Qt.FocusReason = Qt.OtherFocusReason)
    QFocusEvent(QFocusEvent)
    """
    def gotFocus(self): # real signature unknown; restored from __doc__
        """ gotFocus(self) -> bool """
        return False

    def lostFocus(self): # real signature unknown; restored from __doc__
        """ lostFocus(self) -> bool """
        return False

    def reason(self): # real signature unknown; restored from __doc__
        """ reason(self) -> Qt.FocusReason """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


