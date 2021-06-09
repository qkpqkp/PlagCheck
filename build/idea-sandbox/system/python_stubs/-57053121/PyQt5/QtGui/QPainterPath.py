# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QPainterPath(__sip.simplewrapper):
    """
    QPainterPath()
    QPainterPath(Union[QPointF, QPoint])
    QPainterPath(QPainterPath)
    """
    def addEllipse(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addEllipse(self, QRectF)
        addEllipse(self, float, float, float, float)
        addEllipse(self, Union[QPointF, QPoint], float, float)
        """
        pass

    def addPath(self, QPainterPath): # real signature unknown; restored from __doc__
        """ addPath(self, QPainterPath) """
        pass

    def addPolygon(self, QPolygonF): # real signature unknown; restored from __doc__
        """ addPolygon(self, QPolygonF) """
        pass

    def addRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addRect(self, QRectF)
        addRect(self, float, float, float, float)
        """
        pass

    def addRegion(self, QRegion): # real signature unknown; restored from __doc__
        """ addRegion(self, QRegion) """
        pass

    def addRoundedRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addRoundedRect(self, QRectF, float, float, mode: Qt.SizeMode = Qt.AbsoluteSize)
        addRoundedRect(self, float, float, float, float, float, float, mode: Qt.SizeMode = Qt.AbsoluteSize)
        """
        pass

    def addText(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addText(self, Union[QPointF, QPoint], QFont, str)
        addText(self, float, float, QFont, str)
        """
        pass

    def angleAtPercent(self, p_float): # real signature unknown; restored from __doc__
        """ angleAtPercent(self, float) -> float """
        return 0.0

    def arcMoveTo(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        arcMoveTo(self, QRectF, float)
        arcMoveTo(self, float, float, float, float, float)
        """
        pass

    def arcTo(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        arcTo(self, QRectF, float, float)
        arcTo(self, float, float, float, float, float, float)
        """
        pass

    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> QRectF """
        pass

    def closeSubpath(self): # real signature unknown; restored from __doc__
        """ closeSubpath(self) """
        pass

    def connectPath(self, QPainterPath): # real signature unknown; restored from __doc__
        """ connectPath(self, QPainterPath) """
        pass

    def contains(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        contains(self, Union[QPointF, QPoint]) -> bool
        contains(self, QRectF) -> bool
        contains(self, QPainterPath) -> bool
        """
        return False

    def controlPointRect(self): # real signature unknown; restored from __doc__
        """ controlPointRect(self) -> QRectF """
        pass

    def cubicTo(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        cubicTo(self, Union[QPointF, QPoint], Union[QPointF, QPoint], Union[QPointF, QPoint])
        cubicTo(self, float, float, float, float, float, float)
        """
        pass

    def currentPosition(self): # real signature unknown; restored from __doc__
        """ currentPosition(self) -> QPointF """
        pass

    def elementAt(self, p_int): # real signature unknown; restored from __doc__
        """ elementAt(self, int) -> QPainterPath.Element """
        pass

    def elementCount(self): # real signature unknown; restored from __doc__
        """ elementCount(self) -> int """
        return 0

    def fillRule(self): # real signature unknown; restored from __doc__
        """ fillRule(self) -> Qt.FillRule """
        pass

    def intersected(self, QPainterPath): # real signature unknown; restored from __doc__
        """ intersected(self, QPainterPath) -> QPainterPath """
        return QPainterPath

    def intersects(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        intersects(self, QRectF) -> bool
        intersects(self, QPainterPath) -> bool
        """
        return False

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def length(self): # real signature unknown; restored from __doc__
        """ length(self) -> float """
        return 0.0

    def lineTo(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        lineTo(self, Union[QPointF, QPoint])
        lineTo(self, float, float)
        """
        pass

    def moveTo(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        moveTo(self, Union[QPointF, QPoint])
        moveTo(self, float, float)
        """
        pass

    def percentAtLength(self, p_float): # real signature unknown; restored from __doc__
        """ percentAtLength(self, float) -> float """
        return 0.0

    def pointAtPercent(self, p_float): # real signature unknown; restored from __doc__
        """ pointAtPercent(self, float) -> QPointF """
        pass

    def quadTo(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        quadTo(self, Union[QPointF, QPoint], Union[QPointF, QPoint])
        quadTo(self, float, float, float, float)
        """
        pass

    def setElementPositionAt(self, p_int, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ setElementPositionAt(self, int, float, float) """
        pass

    def setFillRule(self, Qt_FillRule): # real signature unknown; restored from __doc__
        """ setFillRule(self, Qt.FillRule) """
        pass

    def simplified(self): # real signature unknown; restored from __doc__
        """ simplified(self) -> QPainterPath """
        return QPainterPath

    def slopeAtPercent(self, p_float): # real signature unknown; restored from __doc__
        """ slopeAtPercent(self, float) -> float """
        return 0.0

    def subtracted(self, QPainterPath): # real signature unknown; restored from __doc__
        """ subtracted(self, QPainterPath) -> QPainterPath """
        return QPainterPath

    def swap(self, QPainterPath): # real signature unknown; restored from __doc__
        """ swap(self, QPainterPath) """
        pass

    def toFillPolygon(self, QTransform=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        toFillPolygon(self) -> QPolygonF
        toFillPolygon(self, QTransform) -> QPolygonF
        """
        return QPolygonF

    def toFillPolygons(self, QTransform=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        toFillPolygons(self) -> List[QPolygonF]
        toFillPolygons(self, QTransform) -> List[QPolygonF]
        """
        return []

    def toReversed(self): # real signature unknown; restored from __doc__
        """ toReversed(self) -> QPainterPath """
        return QPainterPath

    def toSubpathPolygons(self, QTransform=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        toSubpathPolygons(self) -> List[QPolygonF]
        toSubpathPolygons(self, QTransform) -> List[QPolygonF]
        """
        return []

    def translate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        translate(self, float, float)
        translate(self, Union[QPointF, QPoint])
        """
        pass

    def translated(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        translated(self, float, float) -> QPainterPath
        translated(self, Union[QPointF, QPoint]) -> QPainterPath
        """
        return QPainterPath

    def united(self, QPainterPath): # real signature unknown; restored from __doc__
        """ united(self, QPainterPath) -> QPainterPath """
        return QPainterPath

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
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

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    CurveToDataElement = 3
    CurveToElement = 2
    LineToElement = 1
    MoveToElement = 0
    __hash__ = None


