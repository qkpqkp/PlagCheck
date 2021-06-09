# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QRect(__sip.simplewrapper):
    """
    QRect()
    QRect(int, int, int, int)
    QRect(QPoint, QPoint)
    QRect(QPoint, QSize)
    QRect(QRect)
    """
    def adjust(self, p_int, p_int_1, p_int_2, p_int_3): # real signature unknown; restored from __doc__
        """ adjust(self, int, int, int, int) """
        pass

    def adjusted(self, p_int, p_int_1, p_int_2, p_int_3): # real signature unknown; restored from __doc__
        """ adjusted(self, int, int, int, int) -> QRect """
        return QRect

    def bottom(self): # real signature unknown; restored from __doc__
        """ bottom(self) -> int """
        return 0

    def bottomLeft(self): # real signature unknown; restored from __doc__
        """ bottomLeft(self) -> QPoint """
        return QPoint

    def bottomRight(self): # real signature unknown; restored from __doc__
        """ bottomRight(self) -> QPoint """
        return QPoint

    def center(self): # real signature unknown; restored from __doc__
        """ center(self) -> QPoint """
        return QPoint

    def contains(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        contains(self, QPoint, proper: bool = False) -> bool
        contains(self, QRect, proper: bool = False) -> bool
        contains(self, int, int, bool) -> bool
        contains(self, int, int) -> bool
        """
        return False

    def getCoords(self): # real signature unknown; restored from __doc__
        """ getCoords(self) -> Tuple[int, int, int, int] """
        pass

    def getRect(self): # real signature unknown; restored from __doc__
        """ getRect(self) -> Tuple[int, int, int, int] """
        pass

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> int """
        return 0

    def intersected(self, QRect): # real signature unknown; restored from __doc__
        """ intersected(self, QRect) -> QRect """
        return QRect

    def intersects(self, QRect): # real signature unknown; restored from __doc__
        """ intersects(self, QRect) -> bool """
        return False

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def left(self): # real signature unknown; restored from __doc__
        """ left(self) -> int """
        return 0

    def marginsAdded(self, QMargins): # real signature unknown; restored from __doc__
        """ marginsAdded(self, QMargins) -> QRect """
        return QRect

    def marginsRemoved(self, QMargins): # real signature unknown; restored from __doc__
        """ marginsRemoved(self, QMargins) -> QRect """
        return QRect

    def moveBottom(self, p_int): # real signature unknown; restored from __doc__
        """ moveBottom(self, int) """
        pass

    def moveBottomLeft(self, QPoint): # real signature unknown; restored from __doc__
        """ moveBottomLeft(self, QPoint) """
        pass

    def moveBottomRight(self, QPoint): # real signature unknown; restored from __doc__
        """ moveBottomRight(self, QPoint) """
        pass

    def moveCenter(self, QPoint): # real signature unknown; restored from __doc__
        """ moveCenter(self, QPoint) """
        pass

    def moveLeft(self, p_int): # real signature unknown; restored from __doc__
        """ moveLeft(self, int) """
        pass

    def moveRight(self, p_int): # real signature unknown; restored from __doc__
        """ moveRight(self, int) """
        pass

    def moveTo(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        moveTo(self, int, int)
        moveTo(self, QPoint)
        """
        pass

    def moveTop(self, p_int): # real signature unknown; restored from __doc__
        """ moveTop(self, int) """
        pass

    def moveTopLeft(self, QPoint): # real signature unknown; restored from __doc__
        """ moveTopLeft(self, QPoint) """
        pass

    def moveTopRight(self, QPoint): # real signature unknown; restored from __doc__
        """ moveTopRight(self, QPoint) """
        pass

    def normalized(self): # real signature unknown; restored from __doc__
        """ normalized(self) -> QRect """
        return QRect

    def right(self): # real signature unknown; restored from __doc__
        """ right(self) -> int """
        return 0

    def setBottom(self, p_int): # real signature unknown; restored from __doc__
        """ setBottom(self, int) """
        pass

    def setBottomLeft(self, QPoint): # real signature unknown; restored from __doc__
        """ setBottomLeft(self, QPoint) """
        pass

    def setBottomRight(self, QPoint): # real signature unknown; restored from __doc__
        """ setBottomRight(self, QPoint) """
        pass

    def setCoords(self, p_int, p_int_1, p_int_2, p_int_3): # real signature unknown; restored from __doc__
        """ setCoords(self, int, int, int, int) """
        pass

    def setHeight(self, p_int): # real signature unknown; restored from __doc__
        """ setHeight(self, int) """
        pass

    def setLeft(self, p_int): # real signature unknown; restored from __doc__
        """ setLeft(self, int) """
        pass

    def setRect(self, p_int, p_int_1, p_int_2, p_int_3): # real signature unknown; restored from __doc__
        """ setRect(self, int, int, int, int) """
        pass

    def setRight(self, p_int): # real signature unknown; restored from __doc__
        """ setRight(self, int) """
        pass

    def setSize(self, QSize): # real signature unknown; restored from __doc__
        """ setSize(self, QSize) """
        pass

    def setTop(self, p_int): # real signature unknown; restored from __doc__
        """ setTop(self, int) """
        pass

    def setTopLeft(self, QPoint): # real signature unknown; restored from __doc__
        """ setTopLeft(self, QPoint) """
        pass

    def setTopRight(self, QPoint): # real signature unknown; restored from __doc__
        """ setTopRight(self, QPoint) """
        pass

    def setWidth(self, p_int): # real signature unknown; restored from __doc__
        """ setWidth(self, int) """
        pass

    def setX(self, p_int): # real signature unknown; restored from __doc__
        """ setX(self, int) """
        pass

    def setY(self, p_int): # real signature unknown; restored from __doc__
        """ setY(self, int) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> QSize """
        return QSize

    def top(self): # real signature unknown; restored from __doc__
        """ top(self) -> int """
        return 0

    def topLeft(self): # real signature unknown; restored from __doc__
        """ topLeft(self) -> QPoint """
        return QPoint

    def topRight(self): # real signature unknown; restored from __doc__
        """ topRight(self) -> QPoint """
        return QPoint

    def translate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        translate(self, int, int)
        translate(self, QPoint)
        """
        pass

    def translated(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        translated(self, int, int) -> QRect
        translated(self, QPoint) -> QRect
        """
        return QRect

    def transposed(self): # real signature unknown; restored from __doc__
        """ transposed(self) -> QRect """
        return QRect

    def united(self, QRect): # real signature unknown; restored from __doc__
        """ united(self, QRect) -> QRect """
        return QRect

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> int """
        return 0

    def x(self): # real signature unknown; restored from __doc__
        """ x(self) -> int """
        return 0

    def y(self): # real signature unknown; restored from __doc__
        """ y(self) -> int """
        return 0

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

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
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

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __hash__ = None


