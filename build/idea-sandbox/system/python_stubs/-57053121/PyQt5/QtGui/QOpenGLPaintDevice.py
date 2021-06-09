# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QPaintDevice import QPaintDevice

class QOpenGLPaintDevice(QPaintDevice):
    """
    QOpenGLPaintDevice()
    QOpenGLPaintDevice(QSize)
    QOpenGLPaintDevice(int, int)
    """
    def context(self): # real signature unknown; restored from __doc__
        """ context(self) -> QOpenGLContext """
        return QOpenGLContext

    def dotsPerMeterX(self): # real signature unknown; restored from __doc__
        """ dotsPerMeterX(self) -> float """
        return 0.0

    def dotsPerMeterY(self): # real signature unknown; restored from __doc__
        """ dotsPerMeterY(self) -> float """
        return 0.0

    def ensureActiveTarget(self): # real signature unknown; restored from __doc__
        """ ensureActiveTarget(self) """
        pass

    def metric(self, QPaintDevice_PaintDeviceMetric): # real signature unknown; restored from __doc__
        """ metric(self, QPaintDevice.PaintDeviceMetric) -> int """
        return 0

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ paintEngine(self) -> QPaintEngine """
        return QPaintEngine

    def paintFlipped(self): # real signature unknown; restored from __doc__
        """ paintFlipped(self) -> bool """
        return False

    def setDevicePixelRatio(self, p_float): # real signature unknown; restored from __doc__
        """ setDevicePixelRatio(self, float) """
        pass

    def setDotsPerMeterX(self, p_float): # real signature unknown; restored from __doc__
        """ setDotsPerMeterX(self, float) """
        pass

    def setDotsPerMeterY(self, p_float): # real signature unknown; restored from __doc__
        """ setDotsPerMeterY(self, float) """
        pass

    def setPaintFlipped(self, bool): # real signature unknown; restored from __doc__
        """ setPaintFlipped(self, bool) """
        pass

    def setSize(self, QSize): # real signature unknown; restored from __doc__
        """ setSize(self, QSize) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> QSize """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


