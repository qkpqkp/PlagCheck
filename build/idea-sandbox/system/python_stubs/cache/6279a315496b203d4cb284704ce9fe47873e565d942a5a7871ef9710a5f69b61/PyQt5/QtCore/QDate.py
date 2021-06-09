# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QDate(__sip.simplewrapper):
    """
    QDate()
    QDate(int, int, int)
    QDate(QDate)
    """
    def addDays(self, p_int): # real signature unknown; restored from __doc__
        """ addDays(self, int) -> QDate """
        return QDate

    def addMonths(self, p_int): # real signature unknown; restored from __doc__
        """ addMonths(self, int) -> QDate """
        return QDate

    def addYears(self, p_int): # real signature unknown; restored from __doc__
        """ addYears(self, int) -> QDate """
        return QDate

    def currentDate(self): # real signature unknown; restored from __doc__
        """ currentDate() -> QDate """
        return QDate

    def day(self): # real signature unknown; restored from __doc__
        """ day(self) -> int """
        return 0

    def dayOfWeek(self): # real signature unknown; restored from __doc__
        """ dayOfWeek(self) -> int """
        return 0

    def dayOfYear(self): # real signature unknown; restored from __doc__
        """ dayOfYear(self) -> int """
        return 0

    def daysInMonth(self): # real signature unknown; restored from __doc__
        """ daysInMonth(self) -> int """
        return 0

    def daysInYear(self): # real signature unknown; restored from __doc__
        """ daysInYear(self) -> int """
        return 0

    def daysTo(self, Union, QDate=None, datetime_date=None): # real signature unknown; restored from __doc__
        """ daysTo(self, Union[QDate, datetime.date]) -> int """
        return 0

    def fromJulianDay(self, p_int): # real signature unknown; restored from __doc__
        """ fromJulianDay(int) -> QDate """
        return QDate

    def fromString(self, p_str, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        fromString(str, format: Qt.DateFormat = Qt.TextDate) -> QDate
        fromString(str, str) -> QDate
        """
        return QDate

    def getDate(self): # real signature unknown; restored from __doc__
        """ getDate(self) -> Tuple[int, int, int] """
        pass

    def isLeapYear(self, p_int): # real signature unknown; restored from __doc__
        """ isLeapYear(int) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isValid(self, p_int=None, p_int_1=None, p_int_2=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        isValid(self) -> bool
        isValid(int, int, int) -> bool
        """
        return False

    def longDayName(self, p_int, type=None): # real signature unknown; restored from __doc__
        """ longDayName(int, type: QDate.MonthNameType = QDate.DateFormat) -> str """
        return ""

    def longMonthName(self, p_int, type=None): # real signature unknown; restored from __doc__
        """ longMonthName(int, type: QDate.MonthNameType = QDate.DateFormat) -> str """
        return ""

    def month(self): # real signature unknown; restored from __doc__
        """ month(self) -> int """
        return 0

    def setDate(self, p_int, p_int_1, p_int_2): # real signature unknown; restored from __doc__
        """ setDate(self, int, int, int) -> bool """
        return False

    def shortDayName(self, p_int, type=None): # real signature unknown; restored from __doc__
        """ shortDayName(int, type: QDate.MonthNameType = QDate.DateFormat) -> str """
        return ""

    def shortMonthName(self, p_int, type=None): # real signature unknown; restored from __doc__
        """ shortMonthName(int, type: QDate.MonthNameType = QDate.DateFormat) -> str """
        return ""

    def toJulianDay(self): # real signature unknown; restored from __doc__
        """ toJulianDay(self) -> int """
        return 0

    def toPyDate(self): # real signature unknown; restored from __doc__
        """ toPyDate(self) -> datetime.date """
        pass

    def toString(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        toString(self, format: Qt.DateFormat = Qt.TextDate) -> str
        toString(self, str) -> str
        """
        return ""

    def weekNumber(self): # real signature unknown; restored from __doc__
        """ weekNumber(self) -> Tuple[int, int] """
        pass

    def year(self): # real signature unknown; restored from __doc__
        """ year(self) -> int """
        return 0

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


    DateFormat = 0
    StandaloneFormat = 1


