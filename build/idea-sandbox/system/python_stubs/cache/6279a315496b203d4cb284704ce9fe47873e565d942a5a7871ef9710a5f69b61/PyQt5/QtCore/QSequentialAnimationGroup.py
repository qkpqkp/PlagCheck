# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QAnimationGroup import QAnimationGroup

class QSequentialAnimationGroup(QAnimationGroup):
    """ QSequentialAnimationGroup(parent: QObject = None) """
    def addPause(self, p_int): # real signature unknown; restored from __doc__
        """ addPause(self, int) -> QPauseAnimation """
        return QPauseAnimation

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def currentAnimation(self): # real signature unknown; restored from __doc__
        """ currentAnimation(self) -> QAbstractAnimation """
        return QAbstractAnimation

    def currentAnimationChanged(self, QAbstractAnimation): # real signature unknown; restored from __doc__
        """ currentAnimationChanged(self, QAbstractAnimation) [signal] """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def duration(self): # real signature unknown; restored from __doc__
        """ duration(self) -> int """
        return 0

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def insertPause(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ insertPause(self, int, int) -> QPauseAnimation """
        return QPauseAnimation

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

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


