# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QValidator import QValidator

class QIntValidator(QValidator):
    """
    QIntValidator(parent: QObject = None)
    QIntValidator(int, int, parent: QObject = None)
    """
    def bottom(self): # real signature unknown; restored from __doc__
        """ bottom(self) -> int """
        return 0

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def fixup(self, p_str): # real signature unknown; restored from __doc__
        """ fixup(self, str) -> str """
        return ""

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setBottom(self, p_int): # real signature unknown; restored from __doc__
        """ setBottom(self, int) """
        pass

    def setRange(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ setRange(self, int, int) """
        pass

    def setTop(self, p_int): # real signature unknown; restored from __doc__
        """ setTop(self, int) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def top(self): # real signature unknown; restored from __doc__
        """ top(self) -> int """
        return 0

    def validate(self, p_str, p_int): # real signature unknown; restored from __doc__
        """ validate(self, str, int) -> Tuple[QValidator.State, str, int] """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


