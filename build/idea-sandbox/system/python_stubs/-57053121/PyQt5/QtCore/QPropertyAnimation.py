# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QVariantAnimation import QVariantAnimation

class QPropertyAnimation(QVariantAnimation):
    """
    QPropertyAnimation(parent: QObject = None)
    QPropertyAnimation(QObject, Union[QByteArray, bytes, bytearray], parent: QObject = None)
    """
    def childEvent(self, *args, **kwargs): # real signature unknown
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

    def interpolated(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def propertyName(self): # real signature unknown; restored from __doc__
        """ propertyName(self) -> QByteArray """
        return QByteArray

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setPropertyName(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setPropertyName(self, Union[QByteArray, bytes, bytearray]) """
        pass

    def setTargetObject(self, QObject): # real signature unknown; restored from __doc__
        """ setTargetObject(self, QObject) """
        pass

    def targetObject(self): # real signature unknown; restored from __doc__
        """ targetObject(self) -> QObject """
        return QObject

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateCurrentTime(self, *args, **kwargs): # real signature unknown
        pass

    def updateCurrentValue(self, Any): # real signature unknown; restored from __doc__
        """ updateCurrentValue(self, Any) """
        pass

    def updateDirection(self, *args, **kwargs): # real signature unknown
        pass

    def updateState(self, QAbstractAnimation_State, QAbstractAnimation_State_1): # real signature unknown; restored from __doc__
        """ updateState(self, QAbstractAnimation.State, QAbstractAnimation.State) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


