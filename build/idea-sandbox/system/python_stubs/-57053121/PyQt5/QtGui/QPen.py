# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QPen(__sip.simplewrapper):
    """
    QPen()
    QPen(Qt.PenStyle)
    QPen(Union[QBrush, QColor, Qt.GlobalColor, QGradient], float, style: Qt.PenStyle = Qt.SolidLine, cap: Qt.PenCapStyle = Qt.SquareCap, join: Qt.PenJoinStyle = Qt.BevelJoin)
    QPen(Union[QPen, QColor, Qt.GlobalColor, QGradient])
    QPen(Any)
    """
    def brush(self): # real signature unknown; restored from __doc__
        """ brush(self) -> QBrush """
        return QBrush

    def capStyle(self): # real signature unknown; restored from __doc__
        """ capStyle(self) -> Qt.PenCapStyle """
        pass

    def color(self): # real signature unknown; restored from __doc__
        """ color(self) -> QColor """
        return QColor

    def dashOffset(self): # real signature unknown; restored from __doc__
        """ dashOffset(self) -> float """
        return 0.0

    def dashPattern(self): # real signature unknown; restored from __doc__
        """ dashPattern(self) -> List[float] """
        return []

    def isCosmetic(self): # real signature unknown; restored from __doc__
        """ isCosmetic(self) -> bool """
        return False

    def isSolid(self): # real signature unknown; restored from __doc__
        """ isSolid(self) -> bool """
        return False

    def joinStyle(self): # real signature unknown; restored from __doc__
        """ joinStyle(self) -> Qt.PenJoinStyle """
        pass

    def miterLimit(self): # real signature unknown; restored from __doc__
        """ miterLimit(self) -> float """
        return 0.0

    def setBrush(self, Union, QBrush=None, QColor=None, Qt_GlobalColor=None, QGradient=None): # real signature unknown; restored from __doc__
        """ setBrush(self, Union[QBrush, QColor, Qt.GlobalColor, QGradient]) """
        pass

    def setCapStyle(self, Qt_PenCapStyle): # real signature unknown; restored from __doc__
        """ setCapStyle(self, Qt.PenCapStyle) """
        pass

    def setColor(self, Union, QColor=None, Qt_GlobalColor=None, QGradient=None): # real signature unknown; restored from __doc__
        """ setColor(self, Union[QColor, Qt.GlobalColor, QGradient]) """
        pass

    def setCosmetic(self, bool): # real signature unknown; restored from __doc__
        """ setCosmetic(self, bool) """
        pass

    def setDashOffset(self, p_float): # real signature unknown; restored from __doc__
        """ setDashOffset(self, float) """
        pass

    def setDashPattern(self, Iterable, p_float=None): # real signature unknown; restored from __doc__
        """ setDashPattern(self, Iterable[float]) """
        pass

    def setJoinStyle(self, Qt_PenJoinStyle): # real signature unknown; restored from __doc__
        """ setJoinStyle(self, Qt.PenJoinStyle) """
        pass

    def setMiterLimit(self, p_float): # real signature unknown; restored from __doc__
        """ setMiterLimit(self, float) """
        pass

    def setStyle(self, Qt_PenStyle): # real signature unknown; restored from __doc__
        """ setStyle(self, Qt.PenStyle) """
        pass

    def setWidth(self, p_int): # real signature unknown; restored from __doc__
        """ setWidth(self, int) """
        pass

    def setWidthF(self, p_float): # real signature unknown; restored from __doc__
        """ setWidthF(self, float) """
        pass

    def style(self): # real signature unknown; restored from __doc__
        """ style(self) -> Qt.PenStyle """
        pass

    def swap(self, QPen): # real signature unknown; restored from __doc__
        """ swap(self, QPen) """
        pass

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> int """
        return 0

    def widthF(self): # real signature unknown; restored from __doc__
        """ widthF(self) -> float """
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


    __hash__ = None


