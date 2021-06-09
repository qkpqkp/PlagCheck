# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QGlyphRun(__sip.simplewrapper):
    """
    QGlyphRun()
    QGlyphRun(QGlyphRun)
    """
    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> QRectF """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> QGlyphRun.GlyphRunFlags """
        pass

    def glyphIndexes(self): # real signature unknown; restored from __doc__
        """ glyphIndexes(self) -> List[int] """
        return []

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isRightToLeft(self): # real signature unknown; restored from __doc__
        """ isRightToLeft(self) -> bool """
        return False

    def overline(self): # real signature unknown; restored from __doc__
        """ overline(self) -> bool """
        return False

    def positions(self): # real signature unknown; restored from __doc__
        """ positions(self) -> List[QPointF] """
        return []

    def rawFont(self): # real signature unknown; restored from __doc__
        """ rawFont(self) -> QRawFont """
        return QRawFont

    def setBoundingRect(self, QRectF): # real signature unknown; restored from __doc__
        """ setBoundingRect(self, QRectF) """
        pass

    def setFlag(self, QGlyphRun_GlyphRunFlag, enabled=True): # real signature unknown; restored from __doc__
        """ setFlag(self, QGlyphRun.GlyphRunFlag, enabled: bool = True) """
        pass

    def setFlags(self, Union, QGlyphRun_GlyphRunFlags=None, QGlyphRun_GlyphRunFlag=None): # real signature unknown; restored from __doc__
        """ setFlags(self, Union[QGlyphRun.GlyphRunFlags, QGlyphRun.GlyphRunFlag]) """
        pass

    def setGlyphIndexes(self, Iterable, p_int=None): # real signature unknown; restored from __doc__
        """ setGlyphIndexes(self, Iterable[int]) """
        pass

    def setOverline(self, bool): # real signature unknown; restored from __doc__
        """ setOverline(self, bool) """
        pass

    def setPositions(self, Iterable, Union=None, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ setPositions(self, Iterable[Union[QPointF, QPoint]]) """
        pass

    def setRawFont(self, QRawFont): # real signature unknown; restored from __doc__
        """ setRawFont(self, QRawFont) """
        pass

    def setRightToLeft(self, bool): # real signature unknown; restored from __doc__
        """ setRightToLeft(self, bool) """
        pass

    def setStrikeOut(self, bool): # real signature unknown; restored from __doc__
        """ setStrikeOut(self, bool) """
        pass

    def setUnderline(self, bool): # real signature unknown; restored from __doc__
        """ setUnderline(self, bool) """
        pass

    def strikeOut(self): # real signature unknown; restored from __doc__
        """ strikeOut(self) -> bool """
        return False

    def swap(self, QGlyphRun): # real signature unknown; restored from __doc__
        """ swap(self, QGlyphRun) """
        pass

    def underline(self): # real signature unknown; restored from __doc__
        """ underline(self) -> bool """
        return False

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, QGlyphRun=None): # real signature unknown; restored from __doc__ with multiple overloads
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


    Overline = 1
    RightToLeft = 8
    SplitLigature = 16
    StrikeOut = 4
    Underline = 2
    __hash__ = None


