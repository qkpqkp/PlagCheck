# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QGesture import QGesture

class QSwipeGesture(QGesture):
    """ QSwipeGesture(parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def horizontalDirection(self): # real signature unknown; restored from __doc__
        """ horizontalDirection(self) -> QSwipeGesture.SwipeDirection """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setSwipeAngle(self, p_float): # real signature unknown; restored from __doc__
        """ setSwipeAngle(self, float) """
        pass

    def swipeAngle(self): # real signature unknown; restored from __doc__
        """ swipeAngle(self) -> float """
        return 0.0

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def verticalDirection(self): # real signature unknown; restored from __doc__
        """ verticalDirection(self) -> QSwipeGesture.SwipeDirection """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    Down = 4
    Left = 1
    NoDirection = 0
    Right = 2
    Up = 3


