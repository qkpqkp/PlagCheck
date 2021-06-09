# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QTextLength(__sip.simplewrapper):
    """
    QTextLength()
    QTextLength(QTextLength.Type, float)
    QTextLength(Any)
    QTextLength(QTextLength)
    """
    def rawValue(self): # real signature unknown; restored from __doc__
        """ rawValue(self) -> float """
        return 0.0

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QTextLength.Type """
        pass

    def value(self, p_float): # real signature unknown; restored from __doc__
        """ value(self, float) -> float """
        return 0.0

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

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    FixedLength = 1
    PercentageLength = 2
    VariableLength = 0
    __hash__ = None


