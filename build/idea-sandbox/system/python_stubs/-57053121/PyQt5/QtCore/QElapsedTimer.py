# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QElapsedTimer(__sip.simplewrapper):
    """
    QElapsedTimer()
    QElapsedTimer(QElapsedTimer)
    """
    def clockType(self): # real signature unknown; restored from __doc__
        """ clockType() -> QElapsedTimer.ClockType """
        pass

    def elapsed(self): # real signature unknown; restored from __doc__
        """ elapsed(self) -> int """
        return 0

    def hasExpired(self, p_int): # real signature unknown; restored from __doc__
        """ hasExpired(self, int) -> bool """
        return False

    def invalidate(self): # real signature unknown; restored from __doc__
        """ invalidate(self) """
        pass

    def isMonotonic(self): # real signature unknown; restored from __doc__
        """ isMonotonic() -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def msecsSinceReference(self): # real signature unknown; restored from __doc__
        """ msecsSinceReference(self) -> int """
        return 0

    def msecsTo(self, QElapsedTimer): # real signature unknown; restored from __doc__
        """ msecsTo(self, QElapsedTimer) -> int """
        return 0

    def nsecsElapsed(self): # real signature unknown; restored from __doc__
        """ nsecsElapsed(self) -> int """
        return 0

    def restart(self): # real signature unknown; restored from __doc__
        """ restart(self) -> int """
        return 0

    def secsTo(self, QElapsedTimer): # real signature unknown; restored from __doc__
        """ secsTo(self, QElapsedTimer) -> int """
        return 0

    def start(self): # real signature unknown; restored from __doc__
        """ start(self) """
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

    def __init__(self, QElapsedTimer=None): # real signature unknown; restored from __doc__ with multiple overloads
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

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    MachAbsoluteTime = 3
    MonotonicClock = 1
    PerformanceCounter = 4
    SystemTime = 0
    TickCounter = 2
    __hash__ = None


