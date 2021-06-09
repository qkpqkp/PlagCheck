# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QGestureRecognizer(__sip.wrapper):
    """
    QGestureRecognizer()
    QGestureRecognizer(QGestureRecognizer)
    """
    def create(self, QObject): # real signature unknown; restored from __doc__
        """ create(self, QObject) -> QGesture """
        return QGesture

    def recognize(self, QGesture, QObject, QEvent): # real signature unknown; restored from __doc__
        """ recognize(self, QGesture, QObject, QEvent) -> QGestureRecognizer.Result """
        pass

    def registerRecognizer(self, QGestureRecognizer): # real signature unknown; restored from __doc__
        """ registerRecognizer(QGestureRecognizer) -> Qt.GestureType """
        pass

    def reset(self, QGesture): # real signature unknown; restored from __doc__
        """ reset(self, QGesture) """
        pass

    def unregisterRecognizer(self, Qt_GestureType): # real signature unknown; restored from __doc__
        """ unregisterRecognizer(Qt.GestureType) """
        pass

    def __init__(self, QGestureRecognizer=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    CancelGesture = 16
    ConsumeEventHint = 256
    FinishGesture = 8
    Ignore = 1
    MayBeGesture = 2
    TriggerGesture = 4


