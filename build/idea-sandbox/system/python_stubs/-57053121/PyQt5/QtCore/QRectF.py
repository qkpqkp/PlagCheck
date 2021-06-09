# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QRectF(__sip.simplewrapper):
    """
    QRectF()
    QRectF(Union[QPointF, QPoint], QSizeF)
    QRectF(Union[QPointF, QPoint], Union[QPointF, QPoint])
    QRectF(float, float, float, float)
    QRectF(QRect)
    QRectF(QRectF)
    """
    def adjust(self, p_float, p_float_1, p_float_2, p_float_3): # real signature unknown; restored from __doc__
        """ adjust(self, float, float, float, float) """
        pass

    def adjusted(self, p_float, p_float_1, p_float_2, p_float_3): # real signature unknown; restored from __doc__
        """ adjusted(self, float, float, float, float) -> QRectF """
        return QRectF

    def bottom(self): # real signature unknown; restored from __doc__
        """ bottom(self) -> float """
        return 0.0

    def bottomLeft(self): # real signature unknown; restored from __doc__
        """ bottomLeft(self) -> QPointF """
        return QPointF

    def bottomRight(self): # real signature unknown; restored from __doc__
        """ bottomRight(self) -> QPointF """
        return QPointF

    def center(self): # real signature unknown; restored from __doc__
        """ center(self) -> QPointF """
        return QPointF

    def contains(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        contains(self, Union[QPointF, QPoint]) -> bool
        contains(self, QRectF) -> bool
        contains(self, float, float) -> bool
        """
        return False

    def getCoords(self): # real signature unknown; restored from __doc__
        """ getCoords(self) -> Tuple[float, float, float, float] """
        pass

    def getRect(self): # real signature unknown; restored from __doc__
        """ getRect(self) -> Tuple[float, float, float, float] """
        pass

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> float """
        return 0.0

    def intersected(self, QRectF): # real signature unknown; restored from __doc__
        """ intersected(self, QRectF) -> QRectF """
        return QRectF

    def intersects(self, QRectF): # real signature unknown; restored from __doc__
        """ intersects(self, QRectF) -> bool """
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
        """ left(self) -> float """
        return 0.0

    def marginsAdded(self, QMarginsF): # real signature unknown; restored from __doc__
        """ marginsAdded(self, QMarginsF) -> QRectF """
        return QRectF

    def marginsRemoved(self, QMarginsF): # real signature unknown; restored from __doc__
        """ marginsRemoved(self, QMarginsF) -> QRectF """
        return QRectF

    def moveBottom(self, p_float): # real signature unknown; restored from __doc__
        """ moveBottom(self, float) """
        pass

    def moveBottomLeft(self, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ moveBottomLeft(self, Union[QPointF, QPoint]) """
        pass

    def moveBottomRight(self, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ moveBottomRight(self, Union[QPointF, QPoint]) """
        pass

    def moveCenter(self, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ moveCenter(self, Union[QPointF, QPoint]) """
        pass

    def moveLeft(self, p_float): # real signature unknown; restored from __doc__
        """ moveLeft(self, float) """
        pass

    def moveRight(self, p_float): # real signature unknown; restored from __doc__
        """ moveRight(self, float) """
        pass

    def moveTo(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        moveTo(self, float, float)
        moveTo(self, Union[QPointF, QPoint])
        """
        pass

    def moveTop(self, p_float): # real signature unknown; restored from __doc__
        """ moveTop(self, float) """
        pass

    def moveTopLeft(self, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ moveTopLeft(self, Union[QPointF, QPoint]) """
        pass

    def moveTopRight(self, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ moveTopRight(self, Union[QPointF, QPoint]) """
        pass

    def normalized(self): # real signature unknown; restored from __doc__
        """ normalized(self) -> QRectF """
        return QRectF

    def right(self): # real signature unknown; restored from __doc__
        """ right(self) -> float """
        return 0.0

    def setBottom(self, p_float): # real signature unknown; restored from __doc__
        """ setBottom(self, float) """
        pass

    def setBottomLeft(self, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ setBottomLeft(self, Union[QPointF, QPoint]) """
        pass

    def setBottomRight(self, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ setBottomRight(self, Union[QPointF, QPoint]) """
        pass

    def setCoords(self, p_float, p_float_1, p_float_2, p_float_3): # real signature unknown; restored from __doc__
        """ setCoords(self, float, float, float, float) """
        pass

    def setHeight(self, p_float): # real signature unknown; restored from __doc__
        """ setHeight(self, float) """
        pass

    def setLeft(self, p_float): # real signature unknown; restored from __doc__
        """ setLeft(self, float) """
        pass

    def setRect(self, p_float, p_float_1, p_float_2, p_float_3): # real signature unknown; restored from __doc__
        """ setRect(self, float, float, float, float) """
        pass

    def setRight(self, p_float): # real signature unknown; restored from __doc__
        """ setRight(self, float) """
        pass

    def setSize(self, QSizeF): # real signature unknown; restored from __doc__
        """ setSize(self, QSizeF) """
        pass

    def setTop(self, p_float): # real signature unknown; restored from __doc__
        """ setTop(self, float) """
        pass

    def setTopLeft(self, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ setTopLeft(self, Union[QPointF, QPoint]) """
        pass

    def setTopRight(self, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ setTopRight(self, Union[QPointF, QPoint]) """
        pass

    def setWidth(self, p_float): # real signature unknown; restored from __doc__
        """ setWidth(self, float) """
        pass

    def setX(self, p_float): # real signature unknown; restored from __doc__
        """ setX(self, float) """
        pass

    def setY(self, p_float): # real signature unknown; restored from __doc__
        """ setY(self, float) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> QSizeF """
        return QSizeF

    def toAlignedRect(self): # real signature unknown; restored from __doc__
        """ toAlignedRect(self) -> QRect """
        return QRect

    def top(self): # real signature unknown; restored from __doc__
        """ top(self) -> float """
        return 0.0

    def topLeft(self): # real signature unknown; restored from __doc__
        """ topLeft(self) -> QPointF """
        return QPointF

    def topRight(self): # real signature unknown; restored from __doc__
        """ topRight(self) -> QPointF """
        return QPointF

    def toRect(self): # real signature unknown; restored from __doc__
        """ toRect(self) -> QRect """
        return QRect

    def translate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        translate(self, float, float)
        translate(self, Union[QPointF, QPoint])
        """
        pass

    def translated(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        translated(self, float, float) -> QRectF
        translated(self, Union[QPointF, QPoint]) -> QRectF
        """
        return QRectF

    def transposed(self): # real signature unknown; restored from __doc__
        """ transposed(self) -> QRectF """
        return QRectF

    def united(self, QRectF): # real signature unknown; restored from __doc__
        """ united(self, QRectF) -> QRectF """
        return QRectF

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> float """
        return 0.0

    def x(self): # real signature unknown; restored from __doc__
        """ x(self) -> float """
        return 0.0

    def y(self): # real signature unknown; restored from __doc__
        """ y(self) -> float """
        return 0.0

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


