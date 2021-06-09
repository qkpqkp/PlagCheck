# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QTime(__sip.simplewrapper):
    """
    QTime()
    QTime(int, int, second: int = 0, msec: int = 0)
    QTime(QTime)
    """
    def addMSecs(self, p_int): # real signature unknown; restored from __doc__
        """ addMSecs(self, int) -> QTime """
        return QTime

    def addSecs(self, p_int): # real signature unknown; restored from __doc__
        """ addSecs(self, int) -> QTime """
        return QTime

    def currentTime(self): # real signature unknown; restored from __doc__
        """ currentTime() -> QTime """
        return QTime

    def elapsed(self): # real signature unknown; restored from __doc__
        """ elapsed(self) -> int """
        return 0

    def fromMSecsSinceStartOfDay(self, p_int): # real signature unknown; restored from __doc__
        """ fromMSecsSinceStartOfDay(int) -> QTime """
        return QTime

    def fromString(self, p_str, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        fromString(str, format: Qt.DateFormat = Qt.TextDate) -> QTime
        fromString(str, str) -> QTime
        """
        return QTime

    def hour(self): # real signature unknown; restored from __doc__
        """ hour(self) -> int """
        return 0

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isValid(self, p_int=None, p_int_1=None, p_int_2=None, msec=0): # real signature unknown; restored from __doc__ with multiple overloads
        """
        isValid(self) -> bool
        isValid(int, int, int, msec: int = 0) -> bool
        """
        return False

    def minute(self): # real signature unknown; restored from __doc__
        """ minute(self) -> int """
        return 0

    def msec(self): # real signature unknown; restored from __doc__
        """ msec(self) -> int """
        return 0

    def msecsSinceStartOfDay(self): # real signature unknown; restored from __doc__
        """ msecsSinceStartOfDay(self) -> int """
        return 0

    def msecsTo(self, Union, QTime=None, datetime_time=None): # real signature unknown; restored from __doc__
        """ msecsTo(self, Union[QTime, datetime.time]) -> int """
        return 0

    def restart(self): # real signature unknown; restored from __doc__
        """ restart(self) -> int """
        return 0

    def second(self): # real signature unknown; restored from __doc__
        """ second(self) -> int """
        return 0

    def secsTo(self, Union, QTime=None, datetime_time=None): # real signature unknown; restored from __doc__
        """ secsTo(self, Union[QTime, datetime.time]) -> int """
        return 0

    def setHMS(self, p_int, p_int_1, p_int_2, msec=0): # real signature unknown; restored from __doc__
        """ setHMS(self, int, int, int, msec: int = 0) -> bool """
        return False

    def start(self): # real signature unknown; restored from __doc__
        """ start(self) """
        pass

    def toPyTime(self): # real signature unknown; restored from __doc__
        """ toPyTime(self) -> datetime.time """
        pass

    def toString(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        toString(self, format: Qt.DateFormat = Qt.TextDate) -> str
        toString(self, str) -> str
        """
        return ""

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
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

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
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

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



