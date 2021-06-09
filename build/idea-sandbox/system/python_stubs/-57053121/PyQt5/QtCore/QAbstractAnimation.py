# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QObject import QObject

class QAbstractAnimation(QObject):
    """ QAbstractAnimation(parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def currentLoop(self): # real signature unknown; restored from __doc__
        """ currentLoop(self) -> int """
        return 0

    def currentLoopChanged(self, p_int): # real signature unknown; restored from __doc__
        """ currentLoopChanged(self, int) [signal] """
        pass

    def currentLoopTime(self): # real signature unknown; restored from __doc__
        """ currentLoopTime(self) -> int """
        return 0

    def currentTime(self): # real signature unknown; restored from __doc__
        """ currentTime(self) -> int """
        return 0

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def direction(self): # real signature unknown; restored from __doc__
        """ direction(self) -> QAbstractAnimation.Direction """
        pass

    def directionChanged(self, QAbstractAnimation_Direction): # real signature unknown; restored from __doc__
        """ directionChanged(self, QAbstractAnimation.Direction) [signal] """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def duration(self): # real signature unknown; restored from __doc__
        """ duration(self) -> int """
        return 0

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def finished(self): # real signature unknown; restored from __doc__
        """ finished(self) [signal] """
        pass

    def group(self): # real signature unknown; restored from __doc__
        """ group(self) -> QAnimationGroup """
        return QAnimationGroup

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def loopCount(self): # real signature unknown; restored from __doc__
        """ loopCount(self) -> int """
        return 0

    def pause(self): # real signature unknown; restored from __doc__
        """ pause(self) """
        pass

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

    def setDirection(self, QAbstractAnimation_Direction): # real signature unknown; restored from __doc__
        """ setDirection(self, QAbstractAnimation.Direction) """
        pass

    def setLoopCount(self, p_int): # real signature unknown; restored from __doc__
        """ setLoopCount(self, int) """
        pass

    def setPaused(self, bool): # real signature unknown; restored from __doc__
        """ setPaused(self, bool) """
        pass

    def start(self, policy=None): # real signature unknown; restored from __doc__
        """ start(self, policy: QAbstractAnimation.DeletionPolicy = QAbstractAnimation.KeepWhenStopped) """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QAbstractAnimation.State """
        pass

    def stateChanged(self, QAbstractAnimation_State, QAbstractAnimation_State_1): # real signature unknown; restored from __doc__
        """ stateChanged(self, QAbstractAnimation.State, QAbstractAnimation.State) [signal] """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def totalDuration(self): # real signature unknown; restored from __doc__
        """ totalDuration(self) -> int """
        return 0

    def updateCurrentTime(self, p_int): # real signature unknown; restored from __doc__
        """ updateCurrentTime(self, int) """
        pass

    def updateDirection(self, QAbstractAnimation_Direction): # real signature unknown; restored from __doc__
        """ updateDirection(self, QAbstractAnimation.Direction) """
        pass

    def updateState(self, QAbstractAnimation_State, QAbstractAnimation_State_1): # real signature unknown; restored from __doc__
        """ updateState(self, QAbstractAnimation.State, QAbstractAnimation.State) """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    Backward = 1
    DeleteWhenStopped = 1
    Forward = 0
    KeepWhenStopped = 0
    Paused = 1
    Running = 2
    Stopped = 0


