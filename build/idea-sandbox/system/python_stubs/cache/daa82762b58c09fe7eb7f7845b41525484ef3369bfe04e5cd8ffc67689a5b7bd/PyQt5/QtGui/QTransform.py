# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QTransform(__sip.simplewrapper):
    """
    QTransform()
    QTransform(float, float, float, float, float, float, float, float, m33: float = 1)
    QTransform(float, float, float, float, float, float)
    QTransform(QTransform)
    """
    def adjoint(self): # real signature unknown; restored from __doc__
        """ adjoint(self) -> QTransform """
        return QTransform

    def determinant(self): # real signature unknown; restored from __doc__
        """ determinant(self) -> float """
        return 0.0

    def dx(self): # real signature unknown; restored from __doc__
        """ dx(self) -> float """
        return 0.0

    def dy(self): # real signature unknown; restored from __doc__
        """ dy(self) -> float """
        return 0.0

    def fromScale(self, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ fromScale(float, float) -> QTransform """
        return QTransform

    def fromTranslate(self, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ fromTranslate(float, float) -> QTransform """
        return QTransform

    def inverted(self): # real signature unknown; restored from __doc__
        """ inverted(self) -> Tuple[QTransform, bool] """
        pass

    def isAffine(self): # real signature unknown; restored from __doc__
        """ isAffine(self) -> bool """
        return False

    def isIdentity(self): # real signature unknown; restored from __doc__
        """ isIdentity(self) -> bool """
        return False

    def isInvertible(self): # real signature unknown; restored from __doc__
        """ isInvertible(self) -> bool """
        return False

    def isRotating(self): # real signature unknown; restored from __doc__
        """ isRotating(self) -> bool """
        return False

    def isScaling(self): # real signature unknown; restored from __doc__
        """ isScaling(self) -> bool """
        return False

    def isTranslating(self): # real signature unknown; restored from __doc__
        """ isTranslating(self) -> bool """
        return False

    def m11(self): # real signature unknown; restored from __doc__
        """ m11(self) -> float """
        return 0.0

    def m12(self): # real signature unknown; restored from __doc__
        """ m12(self) -> float """
        return 0.0

    def m13(self): # real signature unknown; restored from __doc__
        """ m13(self) -> float """
        return 0.0

    def m21(self): # real signature unknown; restored from __doc__
        """ m21(self) -> float """
        return 0.0

    def m22(self): # real signature unknown; restored from __doc__
        """ m22(self) -> float """
        return 0.0

    def m23(self): # real signature unknown; restored from __doc__
        """ m23(self) -> float """
        return 0.0

    def m31(self): # real signature unknown; restored from __doc__
        """ m31(self) -> float """
        return 0.0

    def m32(self): # real signature unknown; restored from __doc__
        """ m32(self) -> float """
        return 0.0

    def m33(self): # real signature unknown; restored from __doc__
        """ m33(self) -> float """
        return 0.0

    def map(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        map(self, int, int) -> Tuple[int, int]
        map(self, float, float) -> Tuple[float, float]
        map(self, QPoint) -> QPoint
        map(self, Union[QPointF, QPoint]) -> QPointF
        map(self, QLine) -> QLine
        map(self, QLineF) -> QLineF
        map(self, QPolygonF) -> QPolygonF
        map(self, QPolygon) -> QPolygon
        map(self, QRegion) -> QRegion
        map(self, QPainterPath) -> QPainterPath
        """
        return QPolygonF or QPolygon or QRegion or QPainterPath

    def mapRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mapRect(self, QRect) -> QRect
        mapRect(self, QRectF) -> QRectF
        """
        pass

    def mapToPolygon(self, QRect): # real signature unknown; restored from __doc__
        """ mapToPolygon(self, QRect) -> QPolygon """
        return QPolygon

    def quadToQuad(self, QPolygonF, QPolygonF_1, QTransform): # real signature unknown; restored from __doc__
        """ quadToQuad(QPolygonF, QPolygonF, QTransform) -> bool """
        return False

    def quadToSquare(self, QPolygonF, QTransform): # real signature unknown; restored from __doc__
        """ quadToSquare(QPolygonF, QTransform) -> bool """
        return False

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) """
        pass

    def rotate(self, p_float, axis=None): # real signature unknown; restored from __doc__
        """ rotate(self, float, axis: Qt.Axis = Qt.ZAxis) -> QTransform """
        return QTransform

    def rotateRadians(self, p_float, axis=None): # real signature unknown; restored from __doc__
        """ rotateRadians(self, float, axis: Qt.Axis = Qt.ZAxis) -> QTransform """
        return QTransform

    def scale(self, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ scale(self, float, float) -> QTransform """
        return QTransform

    def setMatrix(self, p_float, p_float_1, p_float_2, p_float_3, p_float_4, p_float_5, p_float_6, p_float_7, p_float_8): # real signature unknown; restored from __doc__
        """ setMatrix(self, float, float, float, float, float, float, float, float, float) """
        pass

    def shear(self, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ shear(self, float, float) -> QTransform """
        return QTransform

    def squareToQuad(self, QPolygonF, QTransform): # real signature unknown; restored from __doc__
        """ squareToQuad(QPolygonF, QTransform) -> bool """
        return False

    def translate(self, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ translate(self, float, float) -> QTransform """
        return QTransform

    def transposed(self): # real signature unknown; restored from __doc__
        """ transposed(self) -> QTransform """
        return QTransform

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QTransform.TransformationType """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
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

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __iadd__(self, *args, **kwargs): # real signature unknown
        """ Return self+=value. """
        pass

    def __imatmul__(self, *args, **kwargs): # real signature unknown
        """ Return self@=value. """
        pass

    def __imul__(self, *args, **kwargs): # real signature unknown
        """ Return self*=value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __isub__(self, *args, **kwargs): # real signature unknown
        """ Return self-=value. """
        pass

    def __itruediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/=value. """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __matmul__(self, *args, **kwargs): # real signature unknown
        """ Return self@value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __rmatmul__(self, *args, **kwargs): # real signature unknown
        """ Return value@self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    TxNone = 0
    TxProject = 16
    TxRotate = 4
    TxScale = 2
    TxShear = 8
    TxTranslate = 1


