# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QEasingCurve(__sip.simplewrapper):
    """
    QEasingCurve(type: QEasingCurve.Type = QEasingCurve.Linear)
    QEasingCurve(Union[QEasingCurve, QEasingCurve.Type])
    """
    def addCubicBezierSegment(self, Union, QPointF=None, QPoint=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ addCubicBezierSegment(self, Union[QPointF, QPoint], Union[QPointF, QPoint], Union[QPointF, QPoint]) """
        pass

    def addTCBSegment(self, Union, QPointF=None, QPoint=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ addTCBSegment(self, Union[QPointF, QPoint], float, float, float) """
        pass

    def amplitude(self): # real signature unknown; restored from __doc__
        """ amplitude(self) -> float """
        return 0.0

    def customType(self): # real signature unknown; restored from __doc__
        """ customType(self) -> Callable[[float], float] """
        pass

    def overshoot(self): # real signature unknown; restored from __doc__
        """ overshoot(self) -> float """
        return 0.0

    def period(self): # real signature unknown; restored from __doc__
        """ period(self) -> float """
        return 0.0

    def setAmplitude(self, p_float): # real signature unknown; restored from __doc__
        """ setAmplitude(self, float) """
        pass

    def setCustomType(self, Callable, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setCustomType(self, Callable[[float], float]) """
        pass

    def setOvershoot(self, p_float): # real signature unknown; restored from __doc__
        """ setOvershoot(self, float) """
        pass

    def setPeriod(self, p_float): # real signature unknown; restored from __doc__
        """ setPeriod(self, float) """
        pass

    def setType(self, QEasingCurve_Type): # real signature unknown; restored from __doc__
        """ setType(self, QEasingCurve.Type) """
        pass

    def swap(self, QEasingCurve): # real signature unknown; restored from __doc__
        """ swap(self, QEasingCurve) """
        pass

    def toCubicSpline(self): # real signature unknown; restored from __doc__
        """ toCubicSpline(self) -> List[QPointF] """
        return []

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QEasingCurve.Type """
        pass

    def valueForProgress(self, p_float): # real signature unknown; restored from __doc__
        """ valueForProgress(self, float) -> float """
        return 0.0

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

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    BezierSpline = 45
    CosineCurve = 44
    Custom = 47
    InBack = 33
    InBounce = 37
    InCirc = 25
    InCubic = 5
    InCurve = 41
    InElastic = 29
    InExpo = 21
    InOutBack = 35
    InOutBounce = 39
    InOutCirc = 27
    InOutCubic = 7
    InOutElastic = 31
    InOutExpo = 23
    InOutQuad = 3
    InOutQuart = 11
    InOutQuint = 15
    InOutSine = 19
    InQuad = 1
    InQuart = 9
    InQuint = 13
    InSine = 17
    Linear = 0
    OutBack = 34
    OutBounce = 38
    OutCirc = 26
    OutCubic = 6
    OutCurve = 42
    OutElastic = 30
    OutExpo = 22
    OutInBack = 36
    OutInBounce = 40
    OutInCirc = 28
    OutInCubic = 8
    OutInElastic = 32
    OutInExpo = 24
    OutInQuad = 4
    OutInQuart = 12
    OutInQuint = 16
    OutInSine = 20
    OutQuad = 2
    OutQuart = 10
    OutQuint = 14
    OutSine = 18
    SineCurve = 43
    TCBSpline = 46
    __hash__ = None


