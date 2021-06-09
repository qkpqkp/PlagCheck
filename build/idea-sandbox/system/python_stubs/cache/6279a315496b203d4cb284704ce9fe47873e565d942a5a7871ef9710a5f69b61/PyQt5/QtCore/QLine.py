# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QLine(__sip.simplewrapper):
    """
    QLine()
    QLine(QPoint, QPoint)
    QLine(int, int, int, int)
    QLine(QLine)
    """
    def center(self): # real signature unknown; restored from __doc__
        """ center(self) -> QPoint """
        return QPoint

    def dx(self): # real signature unknown; restored from __doc__
        """ dx(self) -> int """
        return 0

    def dy(self): # real signature unknown; restored from __doc__
        """ dy(self) -> int """
        return 0

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def p1(self): # real signature unknown; restored from __doc__
        """ p1(self) -> QPoint """
        return QPoint

    def p2(self): # real signature unknown; restored from __doc__
        """ p2(self) -> QPoint """
        return QPoint

    def setLine(self, p_int, p_int_1, p_int_2, p_int_3): # real signature unknown; restored from __doc__
        """ setLine(self, int, int, int, int) """
        pass

    def setP1(self, QPoint): # real signature unknown; restored from __doc__
        """ setP1(self, QPoint) """
        pass

    def setP2(self, QPoint): # real signature unknown; restored from __doc__
        """ setP2(self, QPoint) """
        pass

    def setPoints(self, QPoint, QPoint_1): # real signature unknown; restored from __doc__
        """ setPoints(self, QPoint, QPoint) """
        pass

    def translate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        translate(self, QPoint)
        translate(self, int, int)
        """
        pass

    def translated(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        translated(self, QPoint) -> QLine
        translated(self, int, int) -> QLine
        """
        return QLine

    def x1(self): # real signature unknown; restored from __doc__
        """ x1(self) -> int """
        return 0

    def x2(self): # real signature unknown; restored from __doc__
        """ x2(self) -> int """
        return 0

    def y1(self): # real signature unknown; restored from __doc__
        """ y1(self) -> int """
        return 0

    def y2(self): # real signature unknown; restored from __doc__
        """ y2(self) -> int """
        return 0

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

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

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __hash__ = None


