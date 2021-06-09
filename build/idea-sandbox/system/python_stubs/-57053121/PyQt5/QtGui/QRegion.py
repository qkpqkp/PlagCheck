# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QRegion(__sip.simplewrapper):
    """
    QRegion()
    QRegion(int, int, int, int, type: QRegion.RegionType = QRegion.Rectangle)
    QRegion(QRect, type: QRegion.RegionType = QRegion.Rectangle)
    QRegion(QPolygon, fillRule: Qt.FillRule = Qt.OddEvenFill)
    QRegion(QBitmap)
    QRegion(QRegion)
    QRegion(Any)
    """
    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> QRect """
        pass

    def contains(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        contains(self, QPoint) -> bool
        contains(self, QRect) -> bool
        """
        return False

    def intersected(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        intersected(self, QRegion) -> QRegion
        intersected(self, QRect) -> QRegion
        """
        return QRegion

    def intersects(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        intersects(self, QRegion) -> bool
        intersects(self, QRect) -> bool
        """
        return False

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def rectCount(self): # real signature unknown; restored from __doc__
        """ rectCount(self) -> int """
        return 0

    def rects(self): # real signature unknown; restored from __doc__
        """ rects(self) -> List[QRect] """
        return []

    def setRects(self, Iterable, QRect=None): # real signature unknown; restored from __doc__
        """ setRects(self, Iterable[QRect]) """
        pass

    def subtracted(self, QRegion): # real signature unknown; restored from __doc__
        """ subtracted(self, QRegion) -> QRegion """
        return QRegion

    def swap(self, QRegion): # real signature unknown; restored from __doc__
        """ swap(self, QRegion) """
        pass

    def translate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        translate(self, int, int)
        translate(self, QPoint)
        """
        pass

    def translated(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        translated(self, int, int) -> QRegion
        translated(self, QPoint) -> QRegion
        """
        return QRegion

    def united(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        united(self, QRegion) -> QRegion
        united(self, QRect) -> QRegion
        """
        return QRegion

    def xored(self, QRegion): # real signature unknown; restored from __doc__
        """ xored(self, QRegion) -> QRegion """
        return QRegion

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
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

    def __iadd__(self, *args, **kwargs): # real signature unknown
        """ Return self+=value. """
        pass

    def __iand__(self, *args, **kwargs): # real signature unknown
        """ Return self&=value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __ior__(self, *args, **kwargs): # real signature unknown
        """ Return self|=value. """
        pass

    def __isub__(self, *args, **kwargs): # real signature unknown
        """ Return self-=value. """
        pass

    def __ixor__(self, *args, **kwargs): # real signature unknown
        """ Return self^=value. """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
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

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Ellipse = 1
    Rectangle = 0
    __hash__ = None


