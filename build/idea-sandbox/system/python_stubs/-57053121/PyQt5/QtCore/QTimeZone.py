# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QTimeZone(__sip.simplewrapper):
    """
    QTimeZone()
    QTimeZone(Union[QByteArray, bytes, bytearray])
    QTimeZone(int)
    QTimeZone(Union[QByteArray, bytes, bytearray], int, str, str, country: QLocale.Country = QLocale.AnyCountry, comment: str = '')
    QTimeZone(QTimeZone)
    """
    def abbreviation(self, Union, QDateTime=None, datetime_datetime=None): # real signature unknown; restored from __doc__
        """ abbreviation(self, Union[QDateTime, datetime.datetime]) -> str """
        return ""

    def availableTimeZoneIds(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        availableTimeZoneIds() -> List[QByteArray]
        availableTimeZoneIds(QLocale.Country) -> List[QByteArray]
        availableTimeZoneIds(int) -> List[QByteArray]
        """
        return []

    def comment(self): # real signature unknown; restored from __doc__
        """ comment(self) -> str """
        return ""

    def country(self): # real signature unknown; restored from __doc__
        """ country(self) -> QLocale.Country """
        pass

    def daylightTimeOffset(self, Union, QDateTime=None, datetime_datetime=None): # real signature unknown; restored from __doc__
        """ daylightTimeOffset(self, Union[QDateTime, datetime.datetime]) -> int """
        return 0

    def displayName(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        displayName(self, Union[QDateTime, datetime.datetime], nameType: QTimeZone.NameType = QTimeZone.DefaultName, locale: QLocale = QLocale()) -> str
        displayName(self, QTimeZone.TimeType, nameType: QTimeZone.NameType = QTimeZone.DefaultName, locale: QLocale = QLocale()) -> str
        """
        pass

    def hasDaylightTime(self): # real signature unknown; restored from __doc__
        """ hasDaylightTime(self) -> bool """
        return False

    def hasTransitions(self): # real signature unknown; restored from __doc__
        """ hasTransitions(self) -> bool """
        return False

    def ianaIdToWindowsId(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ ianaIdToWindowsId(Union[QByteArray, bytes, bytearray]) -> QByteArray """
        return QByteArray

    def id(self): # real signature unknown; restored from __doc__
        """ id(self) -> QByteArray """
        return QByteArray

    def isDaylightTime(self, Union, QDateTime=None, datetime_datetime=None): # real signature unknown; restored from __doc__
        """ isDaylightTime(self, Union[QDateTime, datetime.datetime]) -> bool """
        return False

    def isTimeZoneIdAvailable(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ isTimeZoneIdAvailable(Union[QByteArray, bytes, bytearray]) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def nextTransition(self, Union, QDateTime=None, datetime_datetime=None): # real signature unknown; restored from __doc__
        """ nextTransition(self, Union[QDateTime, datetime.datetime]) -> QTimeZone.OffsetData """
        pass

    def offsetData(self, Union, QDateTime=None, datetime_datetime=None): # real signature unknown; restored from __doc__
        """ offsetData(self, Union[QDateTime, datetime.datetime]) -> QTimeZone.OffsetData """
        pass

    def offsetFromUtc(self, Union, QDateTime=None, datetime_datetime=None): # real signature unknown; restored from __doc__
        """ offsetFromUtc(self, Union[QDateTime, datetime.datetime]) -> int """
        return 0

    def previousTransition(self, Union, QDateTime=None, datetime_datetime=None): # real signature unknown; restored from __doc__
        """ previousTransition(self, Union[QDateTime, datetime.datetime]) -> QTimeZone.OffsetData """
        pass

    def standardTimeOffset(self, Union, QDateTime=None, datetime_datetime=None): # real signature unknown; restored from __doc__
        """ standardTimeOffset(self, Union[QDateTime, datetime.datetime]) -> int """
        return 0

    def swap(self, QTimeZone): # real signature unknown; restored from __doc__
        """ swap(self, QTimeZone) """
        pass

    def systemTimeZone(self): # real signature unknown; restored from __doc__
        """ systemTimeZone() -> QTimeZone """
        return QTimeZone

    def systemTimeZoneId(self): # real signature unknown; restored from __doc__
        """ systemTimeZoneId() -> QByteArray """
        return QByteArray

    def transitions(self, Union, QDateTime=None, datetime_datetime=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ transitions(self, Union[QDateTime, datetime.datetime], Union[QDateTime, datetime.datetime]) -> List[QTimeZone.OffsetData] """
        pass

    def utc(self): # real signature unknown; restored from __doc__
        """ utc() -> QTimeZone """
        return QTimeZone

    def windowsIdToDefaultIanaId(self, Union, QByteArray=None, bytes=None, bytearray=None, *args=None, **kwargs=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        windowsIdToDefaultIanaId(Union[QByteArray, bytes, bytearray]) -> QByteArray
        windowsIdToDefaultIanaId(Union[QByteArray, bytes, bytearray], QLocale.Country) -> QByteArray
        """
        return QByteArray

    def windowsIdToIanaIds(self, Union, QByteArray=None, bytes=None, bytearray=None, *args=None, **kwargs=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        windowsIdToIanaIds(Union[QByteArray, bytes, bytearray]) -> List[QByteArray]
        windowsIdToIanaIds(Union[QByteArray, bytes, bytearray], QLocale.Country) -> List[QByteArray]
        """
        return []

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
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

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    DaylightTime = 1
    DefaultName = 0
    GenericTime = 2
    LongName = 1
    OffsetName = 3
    ShortName = 2
    StandardTime = 0
    __hash__ = None


