# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QTextItem(__sip.simplewrapper):
    """
    QTextItem()
    QTextItem(QTextItem)
    """
    def ascent(self): # real signature unknown; restored from __doc__
        """ ascent(self) -> float """
        return 0.0

    def descent(self): # real signature unknown; restored from __doc__
        """ descent(self) -> float """
        return 0.0

    def font(self): # real signature unknown; restored from __doc__
        """ font(self) -> QFont """
        return QFont

    def renderFlags(self): # real signature unknown; restored from __doc__
        """ renderFlags(self) -> QTextItem.RenderFlags """
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> float """
        return 0.0

    def __init__(self, QTextItem=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Overline = 16
    RightToLeft = 1
    StrikeOut = 64
    Underline = 32


