# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QPolygon(__sip.simplewrapper):
    """
    QPolygon()
    QPolygon(QPolygon)
    QPolygon(List[int])
    QPolygon(Iterable[QPoint])
    QPolygon(QRect, closed: bool = False)
    QPolygon(int)
    QPolygon(Any)
    """
    def append(self, QPoint): # real signature unknown; restored from __doc__
        """ append(self, QPoint) """
        pass

    def at(self, p_int): # real signature unknown; restored from __doc__
        """ at(self, int) -> QPoint """
        pass

    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> QRect """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def contains(self, QPoint): # real signature unknown; restored from __doc__
        """ contains(self, QPoint) -> bool """
        return False

    def containsPoint(self, QPoint, Qt_FillRule): # real signature unknown; restored from __doc__
        """ containsPoint(self, QPoint, Qt.FillRule) -> bool """
        return False

    def count(self, QPoint=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        count(self, QPoint) -> int
        count(self) -> int
        """
        return 0

    def data(self): # real signature unknown; restored from __doc__
        """ data(self) -> sip.voidptr """
        pass

    def fill(self, QPoint, size=-1): # real signature unknown; restored from __doc__
        """ fill(self, QPoint, size: int = -1) """
        pass

    def first(self): # real signature unknown; restored from __doc__
        """ first(self) -> QPoint """
        pass

    def indexOf(self, QPoint, from_=0): # real signature unknown; restored from __doc__
        """ indexOf(self, QPoint, from_: int = 0) -> int """
        return 0

    def insert(self, p_int, QPoint): # real signature unknown; restored from __doc__
        """ insert(self, int, QPoint) """
        pass

    def intersected(self, QPolygon): # real signature unknown; restored from __doc__
        """ intersected(self, QPolygon) -> QPolygon """
        return QPolygon

    def intersects(self, QPolygon): # real signature unknown; restored from __doc__
        """ intersects(self, QPolygon) -> bool """
        return False

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def last(self): # real signature unknown; restored from __doc__
        """ last(self) -> QPoint """
        pass

    def lastIndexOf(self, QPoint, from_=-1): # real signature unknown; restored from __doc__
        """ lastIndexOf(self, QPoint, from_: int = -1) -> int """
        return 0

    def mid(self, p_int, length=-1): # real signature unknown; restored from __doc__
        """ mid(self, int, length: int = -1) -> QPolygon """
        return QPolygon

    def point(self, p_int): # real signature unknown; restored from __doc__
        """ point(self, int) -> QPoint """
        pass

    def prepend(self, QPoint): # real signature unknown; restored from __doc__
        """ prepend(self, QPoint) """
        pass

    def putPoints(self, p_int, p_int_1, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        putPoints(self, int, int, int, *)
        putPoints(self, int, int, QPolygon, from_: int = 0)
        """
        pass

    def remove(self, p_int, p_int_1=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        remove(self, int)
        remove(self, int, int)
        """
        pass

    def replace(self, p_int, QPoint): # real signature unknown; restored from __doc__
        """ replace(self, int, QPoint) """
        pass

    def setPoint(self, p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setPoint(self, int, QPoint)
        setPoint(self, int, int, int)
        """
        pass

    def setPoints(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setPoints(self, List[int])
        setPoints(self, int, int, *)
        """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def subtracted(self, QPolygon): # real signature unknown; restored from __doc__
        """ subtracted(self, QPolygon) -> QPolygon """
        return QPolygon

    def swap(self, QPolygon): # real signature unknown; restored from __doc__
        """ swap(self, QPolygon) """
        pass

    def translate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        translate(self, int, int)
        translate(self, QPoint)
        """
        pass

    def translated(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        translated(self, int, int) -> QPolygon
        translated(self, QPoint) -> QPolygon
        """
        return QPolygon

    def united(self, QPolygon): # real signature unknown; restored from __doc__
        """ united(self, QPolygon) -> QPolygon """
        return QPolygon

    def value(self, p_int, QPoint=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        value(self, int) -> QPoint
        value(self, int, QPoint) -> QPoint
        """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __iadd__(self, *args, **kwargs): # real signature unknown
        """ Implement self+=value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __hash__ = None


