# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QAbstractAnimation import QAbstractAnimation

class QAnimationGroup(QAbstractAnimation):
    """ QAnimationGroup(parent: QObject = None) """
    def addAnimation(self, QAbstractAnimation): # real signature unknown; restored from __doc__
        """ addAnimation(self, QAbstractAnimation) """
        pass

    def animationAt(self, p_int): # real signature unknown; restored from __doc__
        """ animationAt(self, int) -> QAbstractAnimation """
        return QAbstractAnimation

    def animationCount(self): # real signature unknown; restored from __doc__
        """ animationCount(self) -> int """
        return 0

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def indexOfAnimation(self, QAbstractAnimation): # real signature unknown; restored from __doc__
        """ indexOfAnimation(self, QAbstractAnimation) -> int """
        return 0

    def insertAnimation(self, p_int, QAbstractAnimation): # real signature unknown; restored from __doc__
        """ insertAnimation(self, int, QAbstractAnimation) """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeAnimation(self, QAbstractAnimation): # real signature unknown; restored from __doc__
        """ removeAnimation(self, QAbstractAnimation) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def takeAnimation(self, p_int): # real signature unknown; restored from __doc__
        """ takeAnimation(self, int) -> QAbstractAnimation """
        return QAbstractAnimation

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateCurrentTime(self, *args, **kwargs): # real signature unknown
        pass

    def updateDirection(self, *args, **kwargs): # real signature unknown
        pass

    def updateState(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


