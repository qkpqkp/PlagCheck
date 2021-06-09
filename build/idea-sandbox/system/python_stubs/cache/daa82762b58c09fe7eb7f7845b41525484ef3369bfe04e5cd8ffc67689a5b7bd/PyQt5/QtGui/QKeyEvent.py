# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QInputEvent import QInputEvent

class QKeyEvent(QInputEvent):
    """
    QKeyEvent(QEvent.Type, int, Union[Qt.KeyboardModifiers, Qt.KeyboardModifier], int, int, int, text: str = '', autorep: bool = False, count: int = 1)
    QKeyEvent(QEvent.Type, int, Union[Qt.KeyboardModifiers, Qt.KeyboardModifier], text: str = '', autorep: bool = False, count: int = 1)
    QKeyEvent(QKeyEvent)
    """
    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def isAutoRepeat(self): # real signature unknown; restored from __doc__
        """ isAutoRepeat(self) -> bool """
        return False

    def key(self): # real signature unknown; restored from __doc__
        """ key(self) -> int """
        return 0

    def matches(self, QKeySequence_StandardKey): # real signature unknown; restored from __doc__
        """ matches(self, QKeySequence.StandardKey) -> bool """
        return False

    def modifiers(self): # real signature unknown; restored from __doc__
        """ modifiers(self) -> Qt.KeyboardModifiers """
        pass

    def nativeModifiers(self): # real signature unknown; restored from __doc__
        """ nativeModifiers(self) -> int """
        return 0

    def nativeScanCode(self): # real signature unknown; restored from __doc__
        """ nativeScanCode(self) -> int """
        return 0

    def nativeVirtualKey(self): # real signature unknown; restored from __doc__
        """ nativeVirtualKey(self) -> int """
        return 0

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __hash__ = None


