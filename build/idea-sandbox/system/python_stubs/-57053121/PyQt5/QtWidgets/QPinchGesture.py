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

class QPinchGesture(QGesture):
    """ QPinchGesture(parent: QObject = None) """
    def centerPoint(self): # real signature unknown; restored from __doc__
        """ centerPoint(self) -> QPointF """
        pass

    def changeFlags(self): # real signature unknown; restored from __doc__
        """ changeFlags(self) -> QPinchGesture.ChangeFlags """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def lastCenterPoint(self): # real signature unknown; restored from __doc__
        """ lastCenterPoint(self) -> QPointF """
        pass

    def lastRotationAngle(self): # real signature unknown; restored from __doc__
        """ lastRotationAngle(self) -> float """
        return 0.0

    def lastScaleFactor(self): # real signature unknown; restored from __doc__
        """ lastScaleFactor(self) -> float """
        return 0.0

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def rotationAngle(self): # real signature unknown; restored from __doc__
        """ rotationAngle(self) -> float """
        return 0.0

    def scaleFactor(self): # real signature unknown; restored from __doc__
        """ scaleFactor(self) -> float """
        return 0.0

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCenterPoint(self, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ setCenterPoint(self, Union[QPointF, QPoint]) """
        pass

    def setChangeFlags(self, Union, QPinchGesture_ChangeFlags=None, QPinchGesture_ChangeFlag=None): # real signature unknown; restored from __doc__
        """ setChangeFlags(self, Union[QPinchGesture.ChangeFlags, QPinchGesture.ChangeFlag]) """
        pass

    def setLastCenterPoint(self, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ setLastCenterPoint(self, Union[QPointF, QPoint]) """
        pass

    def setLastRotationAngle(self, p_float): # real signature unknown; restored from __doc__
        """ setLastRotationAngle(self, float) """
        pass

    def setLastScaleFactor(self, p_float): # real signature unknown; restored from __doc__
        """ setLastScaleFactor(self, float) """
        pass

    def setRotationAngle(self, p_float): # real signature unknown; restored from __doc__
        """ setRotationAngle(self, float) """
        pass

    def setScaleFactor(self, p_float): # real signature unknown; restored from __doc__
        """ setScaleFactor(self, float) """
        pass

    def setStartCenterPoint(self, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ setStartCenterPoint(self, Union[QPointF, QPoint]) """
        pass

    def setTotalChangeFlags(self, Union, QPinchGesture_ChangeFlags=None, QPinchGesture_ChangeFlag=None): # real signature unknown; restored from __doc__
        """ setTotalChangeFlags(self, Union[QPinchGesture.ChangeFlags, QPinchGesture.ChangeFlag]) """
        pass

    def setTotalRotationAngle(self, p_float): # real signature unknown; restored from __doc__
        """ setTotalRotationAngle(self, float) """
        pass

    def setTotalScaleFactor(self, p_float): # real signature unknown; restored from __doc__
        """ setTotalScaleFactor(self, float) """
        pass

    def startCenterPoint(self): # real signature unknown; restored from __doc__
        """ startCenterPoint(self) -> QPointF """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def totalChangeFlags(self): # real signature unknown; restored from __doc__
        """ totalChangeFlags(self) -> QPinchGesture.ChangeFlags """
        pass

    def totalRotationAngle(self): # real signature unknown; restored from __doc__
        """ totalRotationAngle(self) -> float """
        return 0.0

    def totalScaleFactor(self): # real signature unknown; restored from __doc__
        """ totalScaleFactor(self) -> float """
        return 0.0

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    CenterPointChanged = 4
    RotationAngleChanged = 2
    ScaleFactorChanged = 1


