# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QShortcut(__PyQt5_QtCore.QObject):
    """
    QShortcut(QWidget)
    QShortcut(Union[QKeySequence, QKeySequence.StandardKey, str, int], QWidget, member: PYQT_SLOT = 0, ambiguousMember: PYQT_SLOT = 0, context: Qt.ShortcutContext = Qt.WindowShortcut)
    """
    def activated(self): # real signature unknown; restored from __doc__
        """ activated(self) [signal] """
        pass

    def activatedAmbiguously(self): # real signature unknown; restored from __doc__
        """ activatedAmbiguously(self) [signal] """
        pass

    def autoRepeat(self): # real signature unknown; restored from __doc__
        """ autoRepeat(self) -> bool """
        return False

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def context(self): # real signature unknown; restored from __doc__
        """ context(self) -> Qt.ShortcutContext """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def id(self): # real signature unknown; restored from __doc__
        """ id(self) -> int """
        return 0

    def isEnabled(self): # real signature unknown; restored from __doc__
        """ isEnabled(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def key(self): # real signature unknown; restored from __doc__
        """ key(self) -> QKeySequence """
        pass

    def parentWidget(self): # real signature unknown; restored from __doc__
        """ parentWidget(self) -> QWidget """
        return QWidget

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAutoRepeat(self, bool): # real signature unknown; restored from __doc__
        """ setAutoRepeat(self, bool) """
        pass

    def setContext(self, Qt_ShortcutContext): # real signature unknown; restored from __doc__
        """ setContext(self, Qt.ShortcutContext) """
        pass

    def setEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setEnabled(self, bool) """
        pass

    def setKey(self, Union, QKeySequence=None, QKeySequence_StandardKey=None, p_str=None, p_int=None): # real signature unknown; restored from __doc__
        """ setKey(self, Union[QKeySequence, QKeySequence.StandardKey, str, int]) """
        pass

    def setWhatsThis(self, p_str): # real signature unknown; restored from __doc__
        """ setWhatsThis(self, str) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def whatsThis(self): # real signature unknown; restored from __doc__
        """ whatsThis(self) -> str """
        return ""

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


