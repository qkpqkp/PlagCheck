# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QAbstractAnimation import QAbstractAnimation

class QVariantAnimation(QAbstractAnimation):
    """ QVariantAnimation(parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def currentValue(self): # real signature unknown; restored from __doc__
        """ currentValue(self) -> Any """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def duration(self): # real signature unknown; restored from __doc__
        """ duration(self) -> int """
        return 0

    def easingCurve(self): # real signature unknown; restored from __doc__
        """ easingCurve(self) -> QEasingCurve """
        return QEasingCurve

    def endValue(self): # real signature unknown; restored from __doc__
        """ endValue(self) -> Any """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def interpolated(self, Any, Any_1, p_float): # real signature unknown; restored from __doc__
        """ interpolated(self, Any, Any, float) -> Any """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyValueAt(self, p_float): # real signature unknown; restored from __doc__
        """ keyValueAt(self, float) -> Any """
        pass

    def keyValues(self): # real signature unknown; restored from __doc__
        """ keyValues(self) -> List[Tuple[float, Any]] """
        return []

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setDuration(self, p_int): # real signature unknown; restored from __doc__
        """ setDuration(self, int) """
        pass

    def setEasingCurve(self, Union, QEasingCurve=None, QEasingCurve_Type=None): # real signature unknown; restored from __doc__
        """ setEasingCurve(self, Union[QEasingCurve, QEasingCurve.Type]) """
        pass

    def setEndValue(self, Any): # real signature unknown; restored from __doc__
        """ setEndValue(self, Any) """
        pass

    def setKeyValueAt(self, p_float, Any): # real signature unknown; restored from __doc__
        """ setKeyValueAt(self, float, Any) """
        pass

    def setKeyValues(self, Iterable, Tuple=None, p_float=None, Any=None): # real signature unknown; restored from __doc__
        """ setKeyValues(self, Iterable[Tuple[float, Any]]) """
        pass

    def setStartValue(self, Any): # real signature unknown; restored from __doc__
        """ setStartValue(self, Any) """
        pass

    def startValue(self): # real signature unknown; restored from __doc__
        """ startValue(self) -> Any """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateCurrentTime(self, p_int): # real signature unknown; restored from __doc__
        """ updateCurrentTime(self, int) """
        pass

    def updateCurrentValue(self, Any): # real signature unknown; restored from __doc__
        """ updateCurrentValue(self, Any) """
        pass

    def updateDirection(self, *args, **kwargs): # real signature unknown
        pass

    def updateState(self, QAbstractAnimation_State, QAbstractAnimation_State_1): # real signature unknown; restored from __doc__
        """ updateState(self, QAbstractAnimation.State, QAbstractAnimation.State) """
        pass

    def valueChanged(self, Any): # real signature unknown; restored from __doc__
        """ valueChanged(self, Any) [signal] """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


