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

class QPanGesture(QGesture):
    """ QPanGesture(parent: QObject = None) """
    def acceleration(self): # real signature unknown; restored from __doc__
        """ acceleration(self) -> float """
        return 0.0

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def delta(self): # real signature unknown; restored from __doc__
        """ delta(self) -> QPointF """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def lastOffset(self): # real signature unknown; restored from __doc__
        """ lastOffset(self) -> QPointF """
        pass

    def offset(self): # real signature unknown; restored from __doc__
        """ offset(self) -> QPointF """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAcceleration(self, p_float): # real signature unknown; restored from __doc__
        """ setAcceleration(self, float) """
        pass

    def setLastOffset(self, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ setLastOffset(self, Union[QPointF, QPoint]) """
        pass

    def setOffset(self, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ setOffset(self, Union[QPointF, QPoint]) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


