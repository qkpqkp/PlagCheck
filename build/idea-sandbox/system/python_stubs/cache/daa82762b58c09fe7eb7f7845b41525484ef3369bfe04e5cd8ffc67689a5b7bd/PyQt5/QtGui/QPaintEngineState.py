# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QPaintEngineState(__sip.simplewrapper):
    """
    QPaintEngineState()
    QPaintEngineState(QPaintEngineState)
    """
    def backgroundBrush(self): # real signature unknown; restored from __doc__
        """ backgroundBrush(self) -> QBrush """
        return QBrush

    def backgroundMode(self): # real signature unknown; restored from __doc__
        """ backgroundMode(self) -> Qt.BGMode """
        pass

    def brush(self): # real signature unknown; restored from __doc__
        """ brush(self) -> QBrush """
        return QBrush

    def brushNeedsResolving(self): # real signature unknown; restored from __doc__
        """ brushNeedsResolving(self) -> bool """
        return False

    def brushOrigin(self): # real signature unknown; restored from __doc__
        """ brushOrigin(self) -> QPointF """
        pass

    def clipOperation(self): # real signature unknown; restored from __doc__
        """ clipOperation(self) -> Qt.ClipOperation """
        pass

    def clipPath(self): # real signature unknown; restored from __doc__
        """ clipPath(self) -> QPainterPath """
        return QPainterPath

    def clipRegion(self): # real signature unknown; restored from __doc__
        """ clipRegion(self) -> QRegion """
        return QRegion

    def compositionMode(self): # real signature unknown; restored from __doc__
        """ compositionMode(self) -> QPainter.CompositionMode """
        pass

    def font(self): # real signature unknown; restored from __doc__
        """ font(self) -> QFont """
        return QFont

    def isClipEnabled(self): # real signature unknown; restored from __doc__
        """ isClipEnabled(self) -> bool """
        return False

    def opacity(self): # real signature unknown; restored from __doc__
        """ opacity(self) -> float """
        return 0.0

    def painter(self): # real signature unknown; restored from __doc__
        """ painter(self) -> QPainter """
        return QPainter

    def pen(self): # real signature unknown; restored from __doc__
        """ pen(self) -> QPen """
        return QPen

    def penNeedsResolving(self): # real signature unknown; restored from __doc__
        """ penNeedsResolving(self) -> bool """
        return False

    def renderHints(self): # real signature unknown; restored from __doc__
        """ renderHints(self) -> QPainter.RenderHints """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QPaintEngine.DirtyFlags """
        pass

    def transform(self): # real signature unknown; restored from __doc__
        """ transform(self) -> QTransform """
        return QTransform

    def __init__(self, QPaintEngineState=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



