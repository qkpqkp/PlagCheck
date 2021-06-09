# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QDeadlineTimer(__sip.simplewrapper):
    """
    QDeadlineTimer(type: Qt.TimerType = Qt.CoarseTimer)
    QDeadlineTimer(QDeadlineTimer.ForeverConstant, type: Qt.TimerType = Qt.CoarseTimer)
    QDeadlineTimer(int, type: Qt.TimerType = Qt.CoarseTimer)
    QDeadlineTimer(QDeadlineTimer)
    """
    def addNSecs(self, QDeadlineTimer, p_int): # real signature unknown; restored from __doc__
        """ addNSecs(QDeadlineTimer, int) -> QDeadlineTimer """
        return QDeadlineTimer

    def current(self, type=None): # real signature unknown; restored from __doc__
        """ current(type: Qt.TimerType = Qt.CoarseTimer) -> QDeadlineTimer """
        return QDeadlineTimer

    def deadline(self): # real signature unknown; restored from __doc__
        """ deadline(self) -> int """
        return 0

    def deadlineNSecs(self): # real signature unknown; restored from __doc__
        """ deadlineNSecs(self) -> int """
        return 0

    def hasExpired(self): # real signature unknown; restored from __doc__
        """ hasExpired(self) -> bool """
        return False

    def isForever(self): # real signature unknown; restored from __doc__
        """ isForever(self) -> bool """
        return False

    def remainingTime(self): # real signature unknown; restored from __doc__
        """ remainingTime(self) -> int """
        return 0

    def remainingTimeNSecs(self): # real signature unknown; restored from __doc__
        """ remainingTimeNSecs(self) -> int """
        return 0

    def setDeadline(self, p_int, type=None): # real signature unknown; restored from __doc__
        """ setDeadline(self, int, type: Qt.TimerType = Qt.CoarseTimer) """
        pass

    def setPreciseDeadline(self, p_int, nsecs=0, type=None): # real signature unknown; restored from __doc__
        """ setPreciseDeadline(self, int, nsecs: int = 0, type: Qt.TimerType = Qt.CoarseTimer) """
        pass

    def setPreciseRemainingTime(self, p_int, nsecs=0, type=None): # real signature unknown; restored from __doc__
        """ setPreciseRemainingTime(self, int, nsecs: int = 0, type: Qt.TimerType = Qt.CoarseTimer) """
        pass

    def setRemainingTime(self, p_int, type=None): # real signature unknown; restored from __doc__
        """ setRemainingTime(self, int, type: Qt.TimerType = Qt.CoarseTimer) """
        pass

    def setTimerType(self, Qt_TimerType): # real signature unknown; restored from __doc__
        """ setTimerType(self, Qt.TimerType) """
        pass

    def swap(self, QDeadlineTimer): # real signature unknown; restored from __doc__
        """ swap(self, QDeadlineTimer) """
        pass

    def timerType(self): # real signature unknown; restored from __doc__
        """ timerType(self) -> Qt.TimerType """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __iadd__(self, *args, **kwargs): # real signature unknown
        """ Return self+=value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __isub__(self, *args, **kwargs): # real signature unknown
        """ Return self-=value. """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Forever = 0
    __hash__ = None


