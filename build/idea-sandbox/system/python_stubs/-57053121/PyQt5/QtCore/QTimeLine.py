# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QObject import QObject

class QTimeLine(QObject):
    """ QTimeLine(duration: int = 1000, parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def currentFrame(self): # real signature unknown; restored from __doc__
        """ currentFrame(self) -> int """
        return 0

    def currentTime(self): # real signature unknown; restored from __doc__
        """ currentTime(self) -> int """
        return 0

    def currentValue(self): # real signature unknown; restored from __doc__
        """ currentValue(self) -> float """
        return 0.0

    def curveShape(self): # real signature unknown; restored from __doc__
        """ curveShape(self) -> QTimeLine.CurveShape """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def direction(self): # real signature unknown; restored from __doc__
        """ direction(self) -> QTimeLine.Direction """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def duration(self): # real signature unknown; restored from __doc__
        """ duration(self) -> int """
        return 0

    def easingCurve(self): # real signature unknown; restored from __doc__
        """ easingCurve(self) -> QEasingCurve """
        return QEasingCurve

    def endFrame(self): # real signature unknown; restored from __doc__
        """ endFrame(self) -> int """
        return 0

    def finished(self): # real signature unknown; restored from __doc__
        """ finished(self) [signal] """
        pass

    def frameChanged(self, p_int): # real signature unknown; restored from __doc__
        """ frameChanged(self, int) [signal] """
        pass

    def frameForTime(self, p_int): # real signature unknown; restored from __doc__
        """ frameForTime(self, int) -> int """
        return 0

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def loopCount(self): # real signature unknown; restored from __doc__
        """ loopCount(self) -> int """
        return 0

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resume(self): # real signature unknown; restored from __doc__
        """ resume(self) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCurrentTime(self, p_int): # real signature unknown; restored from __doc__
        """ setCurrentTime(self, int) """
        pass

    def setCurveShape(self, QTimeLine_CurveShape): # real signature unknown; restored from __doc__
        """ setCurveShape(self, QTimeLine.CurveShape) """
        pass

    def setDirection(self, QTimeLine_Direction): # real signature unknown; restored from __doc__
        """ setDirection(self, QTimeLine.Direction) """
        pass

    def setDuration(self, p_int): # real signature unknown; restored from __doc__
        """ setDuration(self, int) """
        pass

    def setEasingCurve(self, Union, QEasingCurve=None, QEasingCurve_Type=None): # real signature unknown; restored from __doc__
        """ setEasingCurve(self, Union[QEasingCurve, QEasingCurve.Type]) """
        pass

    def setEndFrame(self, p_int): # real signature unknown; restored from __doc__
        """ setEndFrame(self, int) """
        pass

    def setFrameRange(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ setFrameRange(self, int, int) """
        pass

    def setLoopCount(self, p_int): # real signature unknown; restored from __doc__
        """ setLoopCount(self, int) """
        pass

    def setPaused(self, bool): # real signature unknown; restored from __doc__
        """ setPaused(self, bool) """
        pass

    def setStartFrame(self, p_int): # real signature unknown; restored from __doc__
        """ setStartFrame(self, int) """
        pass

    def setUpdateInterval(self, p_int): # real signature unknown; restored from __doc__
        """ setUpdateInterval(self, int) """
        pass

    def start(self): # real signature unknown; restored from __doc__
        """ start(self) """
        pass

    def startFrame(self): # real signature unknown; restored from __doc__
        """ startFrame(self) -> int """
        return 0

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QTimeLine.State """
        pass

    def stateChanged(self, QTimeLine_State): # real signature unknown; restored from __doc__
        """ stateChanged(self, QTimeLine.State) [signal] """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) """
        pass

    def timerEvent(self, QTimerEvent): # real signature unknown; restored from __doc__
        """ timerEvent(self, QTimerEvent) """
        pass

    def toggleDirection(self): # real signature unknown; restored from __doc__
        """ toggleDirection(self) """
        pass

    def updateInterval(self): # real signature unknown; restored from __doc__
        """ updateInterval(self) -> int """
        return 0

    def valueChanged(self, p_float): # real signature unknown; restored from __doc__
        """ valueChanged(self, float) [signal] """
        pass

    def valueForTime(self, p_int): # real signature unknown; restored from __doc__
        """ valueForTime(self, int) -> float """
        return 0.0

    def __init__(self, duration=1000, parent=None): # real signature unknown; restored from __doc__
        pass

    Backward = 1
    CosineCurve = 5
    EaseInCurve = 0
    EaseInOutCurve = 2
    EaseOutCurve = 1
    Forward = 0
    LinearCurve = 3
    NotRunning = 0
    Paused = 1
    Running = 2
    SineCurve = 4


