# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QFontMetricsF(__sip.simplewrapper):
    """
    QFontMetricsF(QFont)
    QFontMetricsF(QFont, QPaintDevice)
    QFontMetricsF(QFontMetrics)
    QFontMetricsF(QFontMetricsF)
    """
    def ascent(self): # real signature unknown; restored from __doc__
        """ ascent(self) -> float """
        return 0.0

    def averageCharWidth(self): # real signature unknown; restored from __doc__
        """ averageCharWidth(self) -> float """
        return 0.0

    def boundingRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        boundingRect(self, str) -> QRectF
        boundingRect(self, QRectF, int, str, tabStops: int = 0, tabArray: Optional[List[int]] = 0) -> QRectF
        """
        pass

    def boundingRectChar(self, p_str): # real signature unknown; restored from __doc__
        """ boundingRectChar(self, str) -> QRectF """
        pass

    def capHeight(self): # real signature unknown; restored from __doc__
        """ capHeight(self) -> float """
        return 0.0

    def descent(self): # real signature unknown; restored from __doc__
        """ descent(self) -> float """
        return 0.0

    def elidedText(self, p_str, Qt_TextElideMode, p_float, flags=0): # real signature unknown; restored from __doc__
        """ elidedText(self, str, Qt.TextElideMode, float, flags: int = 0) -> str """
        return ""

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> float """
        return 0.0

    def horizontalAdvance(self, p_str, length=-1): # real signature unknown; restored from __doc__
        """ horizontalAdvance(self, str, length: int = -1) -> float """
        return 0.0

    def inFont(self, p_str): # real signature unknown; restored from __doc__
        """ inFont(self, str) -> bool """
        return False

    def inFontUcs4(self, p_int): # real signature unknown; restored from __doc__
        """ inFontUcs4(self, int) -> bool """
        return False

    def leading(self): # real signature unknown; restored from __doc__
        """ leading(self) -> float """
        return 0.0

    def leftBearing(self, p_str): # real signature unknown; restored from __doc__
        """ leftBearing(self, str) -> float """
        return 0.0

    def lineSpacing(self): # real signature unknown; restored from __doc__
        """ lineSpacing(self) -> float """
        return 0.0

    def lineWidth(self): # real signature unknown; restored from __doc__
        """ lineWidth(self) -> float """
        return 0.0

    def maxWidth(self): # real signature unknown; restored from __doc__
        """ maxWidth(self) -> float """
        return 0.0

    def minLeftBearing(self): # real signature unknown; restored from __doc__
        """ minLeftBearing(self) -> float """
        return 0.0

    def minRightBearing(self): # real signature unknown; restored from __doc__
        """ minRightBearing(self) -> float """
        return 0.0

    def overlinePos(self): # real signature unknown; restored from __doc__
        """ overlinePos(self) -> float """
        return 0.0

    def rightBearing(self, p_str): # real signature unknown; restored from __doc__
        """ rightBearing(self, str) -> float """
        return 0.0

    def size(self, p_int, p_str, tabStops=0, tabArray, List=None, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ size(self, int, str, tabStops: int = 0, tabArray: Optional[List[int]] = 0) -> QSizeF """
        pass

    def strikeOutPos(self): # real signature unknown; restored from __doc__
        """ strikeOutPos(self) -> float """
        return 0.0

    def swap(self, QFontMetricsF): # real signature unknown; restored from __doc__
        """ swap(self, QFontMetricsF) """
        pass

    def tightBoundingRect(self, p_str): # real signature unknown; restored from __doc__
        """ tightBoundingRect(self, str) -> QRectF """
        pass

    def underlinePos(self): # real signature unknown; restored from __doc__
        """ underlinePos(self) -> float """
        return 0.0

    def width(self, p_str): # real signature unknown; restored from __doc__
        """ width(self, str) -> float """
        return 0.0

    def widthChar(self, p_str): # real signature unknown; restored from __doc__
        """ widthChar(self, str) -> float """
        return 0.0

    def xHeight(self): # real signature unknown; restored from __doc__
        """ xHeight(self) -> float """
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


