# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QDateTime(__sip.simplewrapper):
    """
    QDateTime()
    QDateTime(Union[QDateTime, datetime.datetime])
    QDateTime(Union[QDate, datetime.date])
    QDateTime(Union[QDate, datetime.date], Union[QTime, datetime.time], timeSpec: Qt.TimeSpec = Qt.LocalTime)
    QDateTime(int, int, int, int, int, second: int = 0, msec: int = 0, timeSpec: int = 0)
    QDateTime(Union[QDate, datetime.date], Union[QTime, datetime.time], Qt.TimeSpec, int)
    QDateTime(Union[QDate, datetime.date], Union[QTime, datetime.time], QTimeZone)
    """
    def addDays(self, p_int): # real signature unknown; restored from __doc__
        """ addDays(self, int) -> QDateTime """
        return QDateTime

    def addMonths(self, p_int): # real signature unknown; restored from __doc__
        """ addMonths(self, int) -> QDateTime """
        return QDateTime

    def addMSecs(self, p_int): # real signature unknown; restored from __doc__
        """ addMSecs(self, int) -> QDateTime """
        return QDateTime

    def addSecs(self, p_int): # real signature unknown; restored from __doc__
        """ addSecs(self, int) -> QDateTime """
        return QDateTime

    def addYears(self, p_int): # real signature unknown; restored from __doc__
        """ addYears(self, int) -> QDateTime """
        return QDateTime

    def currentDateTime(self): # real signature unknown; restored from __doc__
        """ currentDateTime() -> QDateTime """
        return QDateTime

    def currentDateTimeUtc(self): # real signature unknown; restored from __doc__
        """ currentDateTimeUtc() -> QDateTime """
        return QDateTime

    def currentMSecsSinceEpoch(self): # real signature unknown; restored from __doc__
        """ currentMSecsSinceEpoch() -> int """
        return 0

    def currentSecsSinceEpoch(self): # real signature unknown; restored from __doc__
        """ currentSecsSinceEpoch() -> int """
        return 0

    def date(self): # real signature unknown; restored from __doc__
        """ date(self) -> QDate """
        return QDate

    def daysTo(self, Union, QDateTime=None, datetime_datetime=None): # real signature unknown; restored from __doc__
        """ daysTo(self, Union[QDateTime, datetime.datetime]) -> int """
        return 0

    def fromMSecsSinceEpoch(self, p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        fromMSecsSinceEpoch(int) -> QDateTime
        fromMSecsSinceEpoch(int, Qt.TimeSpec, offsetSeconds: int = 0) -> QDateTime
        fromMSecsSinceEpoch(int, QTimeZone) -> QDateTime
        """
        return QDateTime

    def fromSecsSinceEpoch(self, p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        fromSecsSinceEpoch(int, spec: Qt.TimeSpec = Qt.LocalTime, offsetSeconds: int = 0) -> QDateTime
        fromSecsSinceEpoch(int, QTimeZone) -> QDateTime
        """
        return QDateTime

    def fromString(self, p_str, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        fromString(str, format: Qt.DateFormat = Qt.TextDate) -> QDateTime
        fromString(str, str) -> QDateTime
        """
        return QDateTime

    def fromTime_t(self, p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        fromTime_t(int) -> QDateTime
        fromTime_t(int, Qt.TimeSpec, offsetSeconds: int = 0) -> QDateTime
        fromTime_t(int, QTimeZone) -> QDateTime
        """
        return QDateTime

    def isDaylightTime(self): # real signature unknown; restored from __doc__
        """ isDaylightTime(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def msecsTo(self, Union, QDateTime=None, datetime_datetime=None): # real signature unknown; restored from __doc__
        """ msecsTo(self, Union[QDateTime, datetime.datetime]) -> int """
        return 0

    def offsetFromUtc(self): # real signature unknown; restored from __doc__
        """ offsetFromUtc(self) -> int """
        return 0

    def secsTo(self, Union, QDateTime=None, datetime_datetime=None): # real signature unknown; restored from __doc__
        """ secsTo(self, Union[QDateTime, datetime.datetime]) -> int """
        return 0

    def setDate(self, Union, QDate=None, datetime_date=None): # real signature unknown; restored from __doc__
        """ setDate(self, Union[QDate, datetime.date]) """
        pass

    def setMSecsSinceEpoch(self, p_int): # real signature unknown; restored from __doc__
        """ setMSecsSinceEpoch(self, int) """
        pass

    def setOffsetFromUtc(self, p_int): # real signature unknown; restored from __doc__
        """ setOffsetFromUtc(self, int) """
        pass

    def setSecsSinceEpoch(self, p_int): # real signature unknown; restored from __doc__
        """ setSecsSinceEpoch(self, int) """
        pass

    def setTime(self, Union, QTime=None, datetime_time=None): # real signature unknown; restored from __doc__
        """ setTime(self, Union[QTime, datetime.time]) """
        pass

    def setTimeSpec(self, Qt_TimeSpec): # real signature unknown; restored from __doc__
        """ setTimeSpec(self, Qt.TimeSpec) """
        pass

    def setTimeZone(self, QTimeZone): # real signature unknown; restored from __doc__
        """ setTimeZone(self, QTimeZone) """
        pass

    def setTime_t(self, p_int): # real signature unknown; restored from __doc__
        """ setTime_t(self, int) """
        pass

    def swap(self, QDateTime): # real signature unknown; restored from __doc__
        """ swap(self, QDateTime) """
        pass

    def time(self): # real signature unknown; restored from __doc__
        """ time(self) -> QTime """
        return QTime

    def timeSpec(self): # real signature unknown; restored from __doc__
        """ timeSpec(self) -> Qt.TimeSpec """
        pass

    def timeZone(self): # real signature unknown; restored from __doc__
        """ timeZone(self) -> QTimeZone """
        return QTimeZone

    def timeZoneAbbreviation(self): # real signature unknown; restored from __doc__
        """ timeZoneAbbreviation(self) -> str """
        return ""

    def toLocalTime(self): # real signature unknown; restored from __doc__
        """ toLocalTime(self) -> QDateTime """
        return QDateTime

    def toMSecsSinceEpoch(self): # real signature unknown; restored from __doc__
        """ toMSecsSinceEpoch(self) -> int """
        return 0

    def toOffsetFromUtc(self, p_int): # real signature unknown; restored from __doc__
        """ toOffsetFromUtc(self, int) -> QDateTime """
        return QDateTime

    def toPyDateTime(self): # real signature unknown; restored from __doc__
        """ toPyDateTime(self) -> datetime.datetime """
        pass

    def toSecsSinceEpoch(self): # real signature unknown; restored from __doc__
        """ toSecsSinceEpoch(self) -> int """
        return 0

    def toString(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        toString(self, format: Qt.DateFormat = Qt.TextDate) -> str
        toString(self, str) -> str
        """
        return ""

    def toTimeSpec(self, Qt_TimeSpec): # real signature unknown; restored from __doc__
        """ toTimeSpec(self, Qt.TimeSpec) -> QDateTime """
        return QDateTime

    def toTimeZone(self, QTimeZone): # real signature unknown; restored from __doc__
        """ toTimeZone(self, QTimeZone) -> QDateTime """
        return QDateTime

    def toTime_t(self): # real signature unknown; restored from __doc__
        """ toTime_t(self) -> int """
        return 0

    def toUTC(self): # real signature unknown; restored from __doc__
        """ toUTC(self) -> QDateTime """
        return QDateTime

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



