# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QGesture(__PyQt5_QtCore.QObject):
    """ QGesture(parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def gestureCancelPolicy(self): # real signature unknown; restored from __doc__
        """ gestureCancelPolicy(self) -> QGesture.GestureCancelPolicy """
        pass

    def gestureType(self): # real signature unknown; restored from __doc__
        """ gestureType(self) -> Qt.GestureType """
        pass

    def hasHotSpot(self): # real signature unknown; restored from __doc__
        """ hasHotSpot(self) -> bool """
        return False

    def hotSpot(self): # real signature unknown; restored from __doc__
        """ hotSpot(self) -> QPointF """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setGestureCancelPolicy(self, QGesture_GestureCancelPolicy): # real signature unknown; restored from __doc__
        """ setGestureCancelPolicy(self, QGesture.GestureCancelPolicy) """
        pass

    def setHotSpot(self, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ setHotSpot(self, Union[QPointF, QPoint]) """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> Qt.GestureState """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def unsetHotSpot(self): # real signature unknown; restored from __doc__
        """ unsetHotSpot(self) """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    CancelAllInContext = 1
    CancelNone = 0


