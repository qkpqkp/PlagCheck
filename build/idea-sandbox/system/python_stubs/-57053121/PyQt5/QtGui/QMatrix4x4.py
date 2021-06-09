# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QMatrix4x4(__sip.simplewrapper):
    """
    QMatrix4x4()
    QMatrix4x4(Sequence[float])
    QMatrix4x4(float, float, float, float, float, float, float, float, float, float, float, float, float, float, float, float)
    QMatrix4x4(QTransform)
    QMatrix4x4(QMatrix4x4)
    """
    def column(self, p_int): # real signature unknown; restored from __doc__
        """ column(self, int) -> QVector4D """
        return QVector4D

    def copyDataTo(self): # real signature unknown; restored from __doc__
        """ copyDataTo(self) -> List[float] """
        return []

    def data(self): # real signature unknown; restored from __doc__
        """ data(self) -> List[float] """
        return []

    def determinant(self): # real signature unknown; restored from __doc__
        """ determinant(self) -> float """
        return 0.0

    def fill(self, p_float): # real signature unknown; restored from __doc__
        """ fill(self, float) """
        pass

    def frustum(self, p_float, p_float_1, p_float_2, p_float_3, p_float_4, p_float_5): # real signature unknown; restored from __doc__
        """ frustum(self, float, float, float, float, float, float) """
        pass

    def inverted(self): # real signature unknown; restored from __doc__
        """ inverted(self) -> Tuple[QMatrix4x4, bool] """
        pass

    def isAffine(self): # real signature unknown; restored from __doc__
        """ isAffine(self) -> bool """
        return False

    def isIdentity(self): # real signature unknown; restored from __doc__
        """ isIdentity(self) -> bool """
        return False

    def lookAt(self, QVector3D, QVector3D_1, QVector3D_2): # real signature unknown; restored from __doc__
        """ lookAt(self, QVector3D, QVector3D, QVector3D) """
        pass

    def map(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        map(self, QPoint) -> QPoint
        map(self, Union[QPointF, QPoint]) -> QPointF
        map(self, QVector3D) -> QVector3D
        map(self, QVector4D) -> QVector4D
        """
        return QVector3D or QVector4D

    def mapRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mapRect(self, QRect) -> QRect
        mapRect(self, QRectF) -> QRectF
        """
        pass

    def mapVector(self, QVector3D): # real signature unknown; restored from __doc__
        """ mapVector(self, QVector3D) -> QVector3D """
        return QVector3D

    def normalMatrix(self): # real signature unknown; restored from __doc__
        """ normalMatrix(self) -> QMatrix3x3 """
        return QMatrix3x3

    def optimize(self): # real signature unknown; restored from __doc__
        """ optimize(self) """
        pass

    def ortho(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        ortho(self, QRect)
        ortho(self, QRectF)
        ortho(self, float, float, float, float, float, float)
        """
        pass

    def perspective(self, p_float, p_float_1, p_float_2, p_float_3): # real signature unknown; restored from __doc__
        """ perspective(self, float, float, float, float) """
        pass

    def rotate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        rotate(self, float, QVector3D)
        rotate(self, float, float, float, z: float = 0)
        rotate(self, QQuaternion)
        """
        pass

    def row(self, p_int): # real signature unknown; restored from __doc__
        """ row(self, int) -> QVector4D """
        return QVector4D

    def scale(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        scale(self, QVector3D)
        scale(self, float, float)
        scale(self, float, float, float)
        scale(self, float)
        """
        pass

    def setColumn(self, p_int, QVector4D): # real signature unknown; restored from __doc__
        """ setColumn(self, int, QVector4D) """
        pass

    def setRow(self, p_int, QVector4D): # real signature unknown; restored from __doc__
        """ setRow(self, int, QVector4D) """
        pass

    def setToIdentity(self): # real signature unknown; restored from __doc__
        """ setToIdentity(self) """
        pass

    def toTransform(self, p_float=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        toTransform(self) -> QTransform
        toTransform(self, float) -> QTransform
        """
        return QTransform

    def translate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        translate(self, QVector3D)
        translate(self, float, float)
        translate(self, float, float, float)
        """
        pass

    def transposed(self): # real signature unknown; restored from __doc__
        """ transposed(self) -> QMatrix4x4 """
        return QMatrix4x4

    def viewport(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        viewport(self, float, float, float, float, nearPlane: float = 0, farPlane: float = 1)
        viewport(self, QRectF)
        """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
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

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
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

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __hash__ = None


