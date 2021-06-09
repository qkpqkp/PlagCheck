# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QPolygonF(__sip.simplewrapper):
    """
    QPolygonF()
    QPolygonF(QPolygonF)
    QPolygonF(Iterable[Union[QPointF, QPoint]])
    QPolygonF(QRectF)
    QPolygonF(QPolygon)
    QPolygonF(int)
    """
    def append(self, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ append(self, Union[QPointF, QPoint]) """
        pass

    def at(self, p_int): # real signature unknown; restored from __doc__
        """ at(self, int) -> QPointF """
        pass

    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> QRectF """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def contains(self, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ contains(self, Union[QPointF, QPoint]) -> bool """
        return False

    def containsPoint(self, Union, QPointF=None, QPoint=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ containsPoint(self, Union[QPointF, QPoint], Qt.FillRule) -> bool """
        pass

    def count(self, Union=None, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        count(self, Union[QPointF, QPoint]) -> int
        count(self) -> int
        """
        return 0

    def data(self): # real signature unknown; restored from __doc__
        """ data(self) -> sip.voidptr """
        pass

    def fill(self, Union, QPointF=None, QPoint=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ fill(self, Union[QPointF, QPoint], size: int = -1) """
        pass

    def first(self): # real signature unknown; restored from __doc__
        """ first(self) -> QPointF """
        pass

    def indexOf(self, Union, QPointF=None, QPoint=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ indexOf(self, Union[QPointF, QPoint], from_: int = 0) -> int """
        pass

    def insert(self, p_int, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ insert(self, int, Union[QPointF, QPoint]) """
        pass

    def intersected(self, QPolygonF): # real signature unknown; restored from __doc__
        """ intersected(self, QPolygonF) -> QPolygonF """
        return QPolygonF

    def intersects(self, QPolygonF): # real signature unknown; restored from __doc__
        """ intersects(self, QPolygonF) -> bool """
        return False

    def isClosed(self): # real signature unknown; restored from __doc__
        """ isClosed(self) -> bool """
        return False

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def last(self): # real signature unknown; restored from __doc__
        """ last(self) -> QPointF """
        pass

    def lastIndexOf(self, Union, QPointF=None, QPoint=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ lastIndexOf(self, Union[QPointF, QPoint], from_: int = -1) -> int """
        pass

    def mid(self, p_int, length=-1): # real signature unknown; restored from __doc__
        """ mid(self, int, length: int = -1) -> QPolygonF """
        return QPolygonF

    def prepend(self, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ prepend(self, Union[QPointF, QPoint]) """
        pass

    def remove(self, p_int, p_int_1=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        remove(self, int)
        remove(self, int, int)
        """
        pass

    def replace(self, p_int, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ replace(self, int, Union[QPointF, QPoint]) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def subtracted(self, QPolygonF): # real signature unknown; restored from __doc__
        """ subtracted(self, QPolygonF) -> QPolygonF """
        return QPolygonF

    def swap(self, QPolygonF): # real signature unknown; restored from __doc__
        """ swap(self, QPolygonF) """
        pass

    def toPolygon(self): # real signature unknown; restored from __doc__
        """ toPolygon(self) -> QPolygon """
        return QPolygon

    def translate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        translate(self, Union[QPointF, QPoint])
        translate(self, float, float)
        """
        pass

    def translated(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        translated(self, Union[QPointF, QPoint]) -> QPolygonF
        translated(self, float, float) -> QPolygonF
        """
        return QPolygonF

    def united(self, QPolygonF): # real signature unknown; restored from __doc__
        """ united(self, QPolygonF) -> QPolygonF """
        return QPolygonF

    def value(self, p_int, Union=None, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        value(self, int) -> QPointF
        value(self, int, Union[QPointF, QPoint]) -> QPointF
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


