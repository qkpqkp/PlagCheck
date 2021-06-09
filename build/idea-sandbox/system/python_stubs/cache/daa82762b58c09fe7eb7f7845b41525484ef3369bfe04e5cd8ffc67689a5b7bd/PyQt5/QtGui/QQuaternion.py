# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QQuaternion(__sip.simplewrapper):
    """
    QQuaternion()
    QQuaternion(float, float, float, float)
    QQuaternion(float, QVector3D)
    QQuaternion(QVector4D)
    QQuaternion(QQuaternion)
    """
    def conjugate(self): # real signature unknown; restored from __doc__
        """ conjugate(self) -> QQuaternion """
        return QQuaternion

    def conjugated(self): # real signature unknown; restored from __doc__
        """ conjugated(self) -> QQuaternion """
        return QQuaternion

    def dotProduct(self, QQuaternion, QQuaternion_1): # real signature unknown; restored from __doc__
        """ dotProduct(QQuaternion, QQuaternion) -> float """
        return 0.0

    def fromAxes(self, QVector3D, QVector3D_1, QVector3D_2): # real signature unknown; restored from __doc__
        """ fromAxes(QVector3D, QVector3D, QVector3D) -> QQuaternion """
        return QQuaternion

    def fromAxisAndAngle(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        fromAxisAndAngle(QVector3D, float) -> QQuaternion
        fromAxisAndAngle(float, float, float, float) -> QQuaternion
        """
        return QQuaternion

    def fromDirection(self, QVector3D, QVector3D_1): # real signature unknown; restored from __doc__
        """ fromDirection(QVector3D, QVector3D) -> QQuaternion """
        return QQuaternion

    def fromEulerAngles(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        fromEulerAngles(float, float, float) -> QQuaternion
        fromEulerAngles(QVector3D) -> QQuaternion
        """
        return QQuaternion

    def fromRotationMatrix(self, QMatrix3x3): # real signature unknown; restored from __doc__
        """ fromRotationMatrix(QMatrix3x3) -> QQuaternion """
        return QQuaternion

    def getAxes(self): # real signature unknown; restored from __doc__
        """ getAxes(self) -> Tuple[QVector3D, QVector3D, QVector3D] """
        pass

    def getAxisAndAngle(self): # real signature unknown; restored from __doc__
        """ getAxisAndAngle(self) -> Tuple[QVector3D, float] """
        pass

    def getEulerAngles(self): # real signature unknown; restored from __doc__
        """ getEulerAngles(self) -> Tuple[float, float, float] """
        pass

    def inverted(self): # real signature unknown; restored from __doc__
        """ inverted(self) -> QQuaternion """
        return QQuaternion

    def isIdentity(self): # real signature unknown; restored from __doc__
        """ isIdentity(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def length(self): # real signature unknown; restored from __doc__
        """ length(self) -> float """
        return 0.0

    def lengthSquared(self): # real signature unknown; restored from __doc__
        """ lengthSquared(self) -> float """
        return 0.0

    def nlerp(self, QQuaternion, QQuaternion_1, p_float): # real signature unknown; restored from __doc__
        """ nlerp(QQuaternion, QQuaternion, float) -> QQuaternion """
        return QQuaternion

    def normalize(self): # real signature unknown; restored from __doc__
        """ normalize(self) """
        pass

    def normalized(self): # real signature unknown; restored from __doc__
        """ normalized(self) -> QQuaternion """
        return QQuaternion

    def rotatedVector(self, QVector3D): # real signature unknown; restored from __doc__
        """ rotatedVector(self, QVector3D) -> QVector3D """
        return QVector3D

    def rotationTo(self, QVector3D, QVector3D_1): # real signature unknown; restored from __doc__
        """ rotationTo(QVector3D, QVector3D) -> QQuaternion """
        return QQuaternion

    def scalar(self): # real signature unknown; restored from __doc__
        """ scalar(self) -> float """
        return 0.0

    def setScalar(self, p_float): # real signature unknown; restored from __doc__
        """ setScalar(self, float) """
        pass

    def setVector(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setVector(self, QVector3D)
        setVector(self, float, float, float)
        """
        pass

    def setX(self, p_float): # real signature unknown; restored from __doc__
        """ setX(self, float) """
        pass

    def setY(self, p_float): # real signature unknown; restored from __doc__
        """ setY(self, float) """
        pass

    def setZ(self, p_float): # real signature unknown; restored from __doc__
        """ setZ(self, float) """
        pass

    def slerp(self, QQuaternion, QQuaternion_1, p_float): # real signature unknown; restored from __doc__
        """ slerp(QQuaternion, QQuaternion, float) -> QQuaternion """
        return QQuaternion

    def toEulerAngles(self): # real signature unknown; restored from __doc__
        """ toEulerAngles(self) -> QVector3D """
        return QVector3D

    def toRotationMatrix(self): # real signature unknown; restored from __doc__
        """ toRotationMatrix(self) -> QMatrix3x3 """
        return QMatrix3x3

    def toVector4D(self): # real signature unknown; restored from __doc__
        """ toVector4D(self) -> QVector4D """
        return QVector4D

    def vector(self): # real signature unknown; restored from __doc__
        """ vector(self) -> QVector3D """
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


