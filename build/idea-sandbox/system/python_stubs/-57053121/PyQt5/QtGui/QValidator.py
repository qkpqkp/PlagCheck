# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QValidator(__PyQt5_QtCore.QObject):
    """ QValidator(parent: QObject = None) """
    def changed(self): # real signature unknown; restored from __doc__
        """ changed(self) [signal] """
        pass

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

    def locale(self): # real signature unknown; restored from __doc__
        """ locale(self) -> QLocale """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setLocale(self, QLocale): # real signature unknown; restored from __doc__
        """ setLocale(self, QLocale) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def validate(self, p_str, p_int): # real signature unknown; restored from __doc__
        """ validate(self, str, int) -> Tuple[QValidator.State, str, int] """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    Acceptable = 2
    Intermediate = 1
    Invalid = 0


