# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QVector3D(__sip.simplewrapper):
    """
    QVector3D()
    QVector3D(float, float, float)
    QVector3D(QPoint)
    QVector3D(Union[QPointF, QPoint])
    QVector3D(QVector2D)
    QVector3D(QVector2D, float)
    QVector3D(QVector4D)
    QVector3D(QVector3D)
    """
    def crossProduct(self, QVector3D, QVector3D_1): # real signature unknown; restored from __doc__
        """ crossProduct(QVector3D, QVector3D) -> QVector3D """
        return QVector3D

    def distanceToLine(self, QVector3D, QVector3D_1): # real signature unknown; restored from __doc__
        """ distanceToLine(self, QVector3D, QVector3D) -> float """
        return 0.0

    def distanceToPlane(self, QVector3D, QVector3D_1, QVector3D_2=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        distanceToPlane(self, QVector3D, QVector3D) -> float
        distanceToPlane(self, QVector3D, QVector3D, QVector3D) -> float
        """
        return 0.0

    def distanceToPoint(self, QVector3D): # real signature unknown; restored from __doc__
        """ distanceToPoint(self, QVector3D) -> float """
        return 0.0

    def dotProduct(self, QVector3D, QVector3D_1): # real signature unknown; restored from __doc__
        """ dotProduct(QVector3D, QVector3D) -> float """
        return 0.0

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def length(self): # real signature unknown; restored from __doc__
        """ length(self) -> float """
        return 0.0

    def lengthSquared(self): # real signature unknown; restored from __doc__
        """ lengthSquared(self) -> float """
        return 0.0

    def normal(self, QVector3D, QVector3D_1, QVector3D_2=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        normal(QVector3D, QVector3D) -> QVector3D
        normal(QVector3D, QVector3D, QVector3D) -> QVector3D
        """
        return QVector3D

    def normalize(self): # real signature unknown; restored from __doc__
        """ normalize(self) """
        pass

    def normalized(self): # real signature unknown; restored from __doc__
        """ normalized(self) -> QVector3D """
        return QVector3D

    def project(self, QMatrix4x4, QMatrix4x4_1, QRect): # real signature unknown; restored from __doc__
        """ project(self, QMatrix4x4, QMatrix4x4, QRect) -> QVector3D """
        return QVector3D

    def setX(self, p_float): # real signature unknown; restored from __doc__
        """ setX(self, float) """
        pass

    def setY(self, p_float): # real signature unknown; restored from __doc__
        """ setY(self, float) """
        pass

    def setZ(self, p_float): # real signature unknown; restored from __doc__
        """ setZ(self, float) """
        pass

    def toPoint(self): # real signature unknown; restored from __doc__
        """ toPoint(self) -> QPoint """
        pass

    def toPointF(self): # real signature unknown; restored from __doc__
        """ toPointF(self) -> QPointF """
        pass

    def toVector2D(self): # real signature unknown; restored from __doc__
        """ toVector2D(self) -> QVector2D """
        return QVector2D

    def toVector4D(self): # real signature unknown; restored from __doc__
        """ toVector4D(self) -> QVector4D """
        return QVector4D

    def unproject(self, QMatrix4x4, QMatrix4x4_1, QRect): # real signature unknown; restored from __doc__
        """ unproject(self, QMatrix4x4, QMatrix4x4, QRect) -> QVector3D """
        return QVector3D

    def x(self): # real signature unknown; restored from __doc__
        """ x(self) -> float """
        return 0.0

    def y(self): # real signature unknown; restored from __doc__
        """ y(self) -> float """
        return 0.0

    def z(self): # real signature unknown; restored from __doc__
        """ z(self) -> float """
        return 0.0

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
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


    __hash__ = None


