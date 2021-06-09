# encoding: utf-8
# module pandas._libs.tslibs.timestamps
# from C:\Users\Doly\Anaconda3\lib\site-packages\pandas\_libs\tslibs\timestamps.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import sys as sys # <module 'sys' (built-in)>
import warnings as warnings # C:\Users\Doly\Anaconda3\lib\warnings.py
import numpy as np # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py
from pandas._libs.tslibs.conversion import normalize_i8_timestamps

from pandas._libs.tslibs.timedeltas import Timedelta

from pandas._libs.tslibs.tzconversion import (tz_convert_single, 
    tz_localize_to_utc)

import pandas._libs.tslibs.c_timestamp as __pandas__libs_tslibs_c_timestamp


# Variables with simple values

DAY_SECONDS = 86400

# functions

def round_nsint64(*args, **kwargs): # real signature unknown
    """
    Applies rounding mode at given frequency
    
        Parameters
        ----------
        values : :obj:`ndarray`
        mode : instance of `RoundTo` enumeration
        freq : str, obj
    
        Returns
        -------
        :obj:`ndarray`
    """
    pass

# classes

class datetime_time(object):
    """
    time([hour[, minute[, second[, microsecond[, tzinfo]]]]]) --> a time object
    
    All arguments are optional. tzinfo may be None, or an instance of
    a tzinfo subclass. The remaining arguments may be ints.
    """
    def dst(self): # real signature unknown; restored from __doc__
        """ Return self.tzinfo.dst(self). """
        pass

    @classmethod
    def fromisoformat(cls, *args, **kwargs): # real signature unknown
        """ string -> time from time.isoformat() output """
        pass

    def isoformat(self, *args, **kwargs): # real signature unknown
        """
        Return string in ISO 8601 format, [HH[:MM[:SS[.mmm[uuu]]]]][+HH:MM].
        
        timespec specifies what components of the time to include.
        """
        pass

    def replace(self, *args, **kwargs): # real signature unknown
        """ Return time with new specified fields. """
        pass

    def strftime(self): # real signature unknown; restored from __doc__
        """ format -> strftime() style string. """
        pass

    def tzname(self): # real signature unknown; restored from __doc__
        """ Return self.tzinfo.tzname(self). """
        pass

    def utcoffset(self): # real signature unknown; restored from __doc__
        """ Return self.tzinfo.utcoffset(self). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ Formats self with strftime. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
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

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce_ex__(self, proto): # real signature unknown; restored from __doc__
        """ __reduce_ex__(proto) -> (cls, state) """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ __reduce__() -> (cls, state) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    fold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    microsecond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    minute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    second = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tzinfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    max = datetime.time(23, 59, 59, 999999)
    min = datetime.time(0, 0)
    resolution = datetime.timedelta(microseconds=1)


class RoundTo(object):
    """
    enumeration defining the available rounding modes
    
        Attributes
        ----------
        MINUS_INFTY
            round towards -∞, or floor [2]_
        PLUS_INFTY
            round towards +∞, or ceil [3]_
        NEAREST_HALF_EVEN
            round to nearest, tie-break half to even [6]_
        NEAREST_HALF_MINUS_INFTY
            round to nearest, tie-break half to -∞ [5]_
        NEAREST_HALF_PLUS_INFTY
            round to nearest, tie-break half to +∞ [4]_
    
    
        References
        ----------
        .. [1] "Rounding - Wikipedia"
               https://en.wikipedia.org/wiki/Rounding
        .. [2] "Rounding down"
               https://en.wikipedia.org/wiki/Rounding#Rounding_down
        .. [3] "Rounding up"
               https://en.wikipedia.org/wiki/Rounding#Rounding_up
        .. [4] "Round half up"
               https://en.wikipedia.org/wiki/Rounding#Round_half_up
        .. [5] "Round half down"
               https://en.wikipedia.org/wiki/Rounding#Round_half_down
        .. [6] "Round half to even"
               https://en.wikipedia.org/wiki/Rounding#Round_half_to_even
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    MINUS_INFTY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    NEAREST_HALF_EVEN = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    NEAREST_HALF_MINUS_INFTY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    NEAREST_HALF_PLUS_INFTY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    PLUS_INFTY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pandas._libs.tslibs.timestamps\', \'__doc__\': \'\\n    enumeration defining the available rounding modes\\n\\n    Attributes\\n    ----------\\n    MINUS_INFTY\\n        round towards -?, or floor [2]_\\n    PLUS_INFTY\\n        round towards +?, or ceil [3]_\\n    NEAREST_HALF_EVEN\\n        round to nearest, tie-break half to even [6]_\\n    NEAREST_HALF_MINUS_INFTY\\n        round to nearest, tie-break half to -? [5]_\\n    NEAREST_HALF_PLUS_INFTY\\n        round to nearest, tie-break half to +? [4]_\\n\\n\\n    References\\n    ----------\\n    .. [1] "Rounding - Wikipedia"\\n           https://en.wikipedia.org/wiki/Rounding\\n    .. [2] "Rounding down"\\n           https://en.wikipedia.org/wiki/Rounding#Rounding_down\\n    .. [3] "Rounding up"\\n           https://en.wikipedia.org/wiki/Rounding#Rounding_up\\n    .. [4] "Round half up"\\n           https://en.wikipedia.org/wiki/Rounding#Round_half_up\\n    .. [5] "Round half down"\\n           https://en.wikipedia.org/wiki/Rounding#Round_half_down\\n    .. [6] "Round half to even"\\n           https://en.wikipedia.org/wiki/Rounding#Round_half_to_even\\n    \', \'MINUS_INFTY\': <property object at 0x000001B6FF6D7458>, \'PLUS_INFTY\': <property object at 0x000001B6FF6D73B8>, \'NEAREST_HALF_EVEN\': <property object at 0x000001B6FF6D7408>, \'NEAREST_HALF_PLUS_INFTY\': <property object at 0x000001B6FF6D74A8>, \'NEAREST_HALF_MINUS_INFTY\': <property object at 0x000001B6FF6D74F8>, \'__dict__\': <attribute \'__dict__\' of \'RoundTo\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'RoundTo\' objects>})'


class timedelta(object):
    """
    Difference between two datetime values.
    
    timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
    
    All arguments are optional and default to 0.
    Arguments may be integers or floats, and may be positive or negative.
    """
    def total_seconds(self, *args, **kwargs): # real signature unknown
        """ Total seconds in the duration. """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
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

    def __init__(self, days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ __reduce__() -> (cls, state) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    days = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of days."""

    microseconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of microseconds (>= 0 and less than 1 second)."""

    seconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of seconds (>= 0 and less than 1 day)."""


    max = datetime.timedelta(days=999999999, seconds=86399, microseconds=999999)
    min = datetime.timedelta(days=-999999999)
    resolution = datetime.timedelta(microseconds=1)


class Timestamp(__pandas__libs_tslibs_c_timestamp._Timestamp):
    """
    Pandas replacement for python datetime.datetime object.
    
        Timestamp is the pandas equivalent of python's Datetime
        and is interchangeable with it in most cases. It's the type used
        for the entries that make up a DatetimeIndex, and other timeseries
        oriented data structures in pandas.
    
        Parameters
        ----------
        ts_input : datetime-like, str, int, float
            Value to be converted to Timestamp.
        freq : str, DateOffset
            Offset which Timestamp will have.
        tz : str, pytz.timezone, dateutil.tz.tzfile or None
            Time zone for time which Timestamp will have.
        unit : str
            Unit used for conversion if ts_input is of type int or float. The
            valid values are 'D', 'h', 'm', 's', 'ms', 'us', and 'ns'. For
            example, 's' means seconds and 'ms' means milliseconds.
        year, month, day : int
        hour, minute, second, microsecond : int, optional, default 0
        nanosecond : int, optional, default 0
            .. versionadded:: 0.23.0
        tzinfo : datetime.tzinfo, optional, default None
    
        Notes
        -----
        There are essentially three calling conventions for the constructor. The
        primary form accepts four parameters. They can be passed by position or
        keyword.
    
        The other two forms mimic the parameters from ``datetime.datetime``. They
        can be passed by either position or keyword, but not both mixed together.
    
        Examples
        --------
        Using the primary calling convention:
    
        This converts a datetime-like string
    
        >>> pd.Timestamp('2017-01-01T12')
        Timestamp('2017-01-01 12:00:00')
    
        This converts a float representing a Unix epoch in units of seconds
    
        >>> pd.Timestamp(1513393355.5, unit='s')
        Timestamp('2017-12-16 03:02:35.500000')
    
        This converts an int representing a Unix-epoch in units of seconds
        and for a particular timezone
    
        >>> pd.Timestamp(1513393355, unit='s', tz='US/Pacific')
        Timestamp('2017-12-15 19:02:35-0800', tz='US/Pacific')
    
        Using the other two forms that mimic the API for ``datetime.datetime``:
    
        >>> pd.Timestamp(2017, 1, 1, 12)
        Timestamp('2017-01-01 12:00:00')
    
        >>> pd.Timestamp(year=2017, month=1, day=1, hour=12)
        Timestamp('2017-01-01 12:00:00')
    """
    def astimezone(self, *args, **kwargs): # real signature unknown
        """
        Convert tz-aware Timestamp to another time zone.
        
                Parameters
                ----------
                tz : str, pytz.timezone, dateutil.tz.tzfile or None
                    Time zone for time which Timestamp will be converted to.
                    None will remove timezone holding UTC time.
        
                Returns
                -------
                converted : Timestamp
        
                Raises
                ------
                TypeError
                    If Timestamp is tz-naive.
        """
        pass

    def ceil(self, *args, **kwargs): # real signature unknown
        """
        return a new Timestamp ceiled to this resolution.
        
                Parameters
                ----------
                freq : str
                    Frequency string indicating the ceiling resolution.
                ambiguous : bool or {'raise', 'NaT'}, default 'raise'
                    The behavior is as follows:
        
                    * bool contains flags to determine if time is dst or not (note
                      that this flag is only applicable for ambiguous fall dst dates).
                    * 'NaT' will return NaT for an ambiguous time.
                    * 'raise' will raise an AmbiguousTimeError for an ambiguous time.
        
                    .. versionadded:: 0.24.0
                nonexistent : {'raise', 'shift_forward', 'shift_backward, 'NaT', timedelta}, default 'raise'
                    A nonexistent time does not exist in a particular timezone
                    where clocks moved forward due to DST.
        
                    * 'shift_forward' will shift the nonexistent time forward to the
                      closest existing time.
                    * 'shift_backward' will shift the nonexistent time backward to the
                      closest existing time.
                    * 'NaT' will return NaT where there are nonexistent times.
                    * timedelta objects will shift nonexistent times by the timedelta.
                    * 'raise' will raise an NonExistentTimeError if there are
                      nonexistent times.
        
                    .. versionadded:: 0.24.0
        
                Raises
                ------
                ValueError if the freq cannot be converted.
        """
        pass

    @classmethod
    def combine(cls, date, time): # real signature unknown; restored from __doc__
        """
        Timestamp.combine(date, time)
        
                date, time -> datetime with same date and time fields.
        """
        pass

    def day_name(self, *args, **kwargs): # real signature unknown
        """
        Return the day name of the Timestamp with specified locale.
        
                Parameters
                ----------
                locale : string, default None (English locale)
                    Locale determining the language in which to return the day name.
        
                Returns
                -------
                day_name : string
        
                .. versionadded:: 0.23.0
        """
        pass

    def floor(self, *args, **kwargs): # real signature unknown
        """
        return a new Timestamp floored to this resolution.
        
                Parameters
                ----------
                freq : str
                    Frequency string indicating the flooring resolution.
                ambiguous : bool or {'raise', 'NaT'}, default 'raise'
                    The behavior is as follows:
        
                    * bool contains flags to determine if time is dst or not (note
                      that this flag is only applicable for ambiguous fall dst dates).
                    * 'NaT' will return NaT for an ambiguous time.
                    * 'raise' will raise an AmbiguousTimeError for an ambiguous time.
        
                    .. versionadded:: 0.24.0
                nonexistent : {'raise', 'shift_forward', 'shift_backward, 'NaT', timedelta}, default 'raise'
                    A nonexistent time does not exist in a particular timezone
                    where clocks moved forward due to DST.
        
                    * 'shift_forward' will shift the nonexistent time forward to the
                      closest existing time.
                    * 'shift_backward' will shift the nonexistent time backward to the
                      closest existing time.
                    * 'NaT' will return NaT where there are nonexistent times.
                    * timedelta objects will shift nonexistent times by the timedelta.
                    * 'raise' will raise an NonExistentTimeError if there are
                      nonexistent times.
        
                    .. versionadded:: 0.24.0
        
                Raises
                ------
                ValueError if the freq cannot be converted.
        """
        pass

    @classmethod
    def fromordinal(cls, ordinal, freq=None, tz=None): # real signature unknown; restored from __doc__
        """
        Timestamp.fromordinal(ordinal, freq=None, tz=None)
        
                Passed an ordinal, translate and convert to a ts.
                Note: by definition there cannot be any tz info on the ordinal itself.
        
                Parameters
                ----------
                ordinal : int
                    Date corresponding to a proleptic Gregorian ordinal.
                freq : str, DateOffset
                    Offset to apply to the Timestamp.
                tz : str, pytz.timezone, dateutil.tz.tzfile or None
                    Time zone for the Timestamp.
        """
        pass

    @classmethod
    def fromtimestamp(cls, ts): # real signature unknown; restored from __doc__
        """
        Timestamp.fromtimestamp(ts)
        
                timestamp[, tz] -> tz's local time from POSIX timestamp.
        """
        pass

    def isoformat(self, *args, **kwargs): # real signature unknown
        pass

    def month_name(self, *args, **kwargs): # real signature unknown
        """
        Return the month name of the Timestamp with specified locale.
        
                Parameters
                ----------
                locale : string, default None (English locale)
                    Locale determining the language in which to return the month name.
        
                Returns
                -------
                month_name : string
        
                .. versionadded:: 0.23.0
        """
        pass

    def normalize(self, *args, **kwargs): # real signature unknown
        """
        Normalize Timestamp to midnight, preserving
                tz information.
        """
        pass

    @classmethod
    def now(cls, tz=None): # real signature unknown; restored from __doc__
        """
        Timestamp.now(tz=None)
        
                Return new Timestamp object representing current time local to
                tz.
        
                Parameters
                ----------
                tz : str or timezone object, default None
                    Timezone to localize to.
        """
        pass

    def replace(self, *args, **kwargs): # real signature unknown
        """
        implements datetime.replace, handles nanoseconds.
        
                Parameters
                ----------
                year : int, optional
                month : int, optional
                day : int, optional
                hour : int, optional
                minute : int, optional
                second : int, optional
                microsecond : int, optional
                nanosecond : int, optional
                tzinfo : tz-convertible, optional
                fold : int, optional, default is 0
        
                Returns
                -------
                Timestamp with fields replaced
        """
        pass

    def round(self, *args, **kwargs): # real signature unknown
        """
        Round the Timestamp to the specified resolution.
        
                Parameters
                ----------
                freq : str
                    Frequency string indicating the rounding resolution.
                ambiguous : bool or {'raise', 'NaT'}, default 'raise'
                    The behavior is as follows:
        
                    * bool contains flags to determine if time is dst or not (note
                      that this flag is only applicable for ambiguous fall dst dates).
                    * 'NaT' will return NaT for an ambiguous time.
                    * 'raise' will raise an AmbiguousTimeError for an ambiguous time.
        
                    .. versionadded:: 0.24.0
                nonexistent : {'raise', 'shift_forward', 'shift_backward, 'NaT', timedelta}, default 'raise'
                    A nonexistent time does not exist in a particular timezone
                    where clocks moved forward due to DST.
        
                    * 'shift_forward' will shift the nonexistent time forward to the
                      closest existing time.
                    * 'shift_backward' will shift the nonexistent time backward to the
                      closest existing time.
                    * 'NaT' will return NaT where there are nonexistent times.
                    * timedelta objects will shift nonexistent times by the timedelta.
                    * 'raise' will raise an NonExistentTimeError if there are
                      nonexistent times.
        
                    .. versionadded:: 0.24.0
        
                Returns
                -------
                a new Timestamp rounded to the given resolution of `freq`
        
                Raises
                ------
                ValueError if the freq cannot be converted
        """
        pass

    @classmethod
    def strptime(cls, string, format): # real signature unknown; restored from __doc__
        """
        Timestamp.strptime(string, format)
        
                Function is not implemented. Use pd.to_datetime().
        """
        pass

    @classmethod
    def today(cls, cls_1, tz=None): # real signature unknown; restored from __doc__
        """
        Timestamp.today(cls, tz=None)
        
                Return the current time in the local timezone.  This differs
                from datetime.today() in that it can be localized to a
                passed timezone.
        
                Parameters
                ----------
                tz : str or timezone object, default None
                    Timezone to localize to.
        """
        pass

    def to_julian_date(self, *args, **kwargs): # real signature unknown
        """
        Convert TimeStamp to a Julian Date.
                0 Julian date is noon January 1, 4713 BC.
        """
        pass

    def to_period(self, *args, **kwargs): # real signature unknown
        """ Return an period of which this timestamp is an observation. """
        pass

    def tz_convert(self, *args, **kwargs): # real signature unknown
        """
        Convert tz-aware Timestamp to another time zone.
        
                Parameters
                ----------
                tz : str, pytz.timezone, dateutil.tz.tzfile or None
                    Time zone for time which Timestamp will be converted to.
                    None will remove timezone holding UTC time.
        
                Returns
                -------
                converted : Timestamp
        
                Raises
                ------
                TypeError
                    If Timestamp is tz-naive.
        """
        pass

    def tz_localize(self, *args, **kwargs): # real signature unknown
        """
        Convert naive Timestamp to local time zone, or remove
                timezone from tz-aware Timestamp.
        
                Parameters
                ----------
                tz : str, pytz.timezone, dateutil.tz.tzfile or None
                    Time zone for time which Timestamp will be converted to.
                    None will remove timezone holding local time.
        
                ambiguous : bool, 'NaT', default 'raise'
                    When clocks moved backward due to DST, ambiguous times may arise.
                    For example in Central European Time (UTC+01), when going from
                    03:00 DST to 02:00 non-DST, 02:30:00 local time occurs both at
                    00:30:00 UTC and at 01:30:00 UTC. In such a situation, the
                    `ambiguous` parameter dictates how ambiguous times should be
                    handled.
        
                    The behavior is as follows:
        
                    * bool contains flags to determine if time is dst or not (note
                      that this flag is only applicable for ambiguous fall dst dates).
                    * 'NaT' will return NaT for an ambiguous time.
                    * 'raise' will raise an AmbiguousTimeError for an ambiguous time.
        
                nonexistent : 'shift_forward', 'shift_backward, 'NaT', timedelta, default 'raise'
                    A nonexistent time does not exist in a particular timezone
                    where clocks moved forward due to DST.
        
                    The behavior is as follows:
        
                    * 'shift_forward' will shift the nonexistent time forward to the
                      closest existing time.
                    * 'shift_backward' will shift the nonexistent time backward to the
                      closest existing time.
                    * 'NaT' will return NaT where there are nonexistent times.
                    * timedelta objects will shift nonexistent times by the timedelta.
                    * 'raise' will raise an NonExistentTimeError if there are
                      nonexistent times.
        
                    .. versionadded:: 0.24.0
        
                Returns
                -------
                localized : Timestamp
        
                Raises
                ------
                TypeError
                    If the Timestamp is tz-aware and tz is not None.
        """
        pass

    @classmethod
    def utcfromtimestamp(cls, ts): # real signature unknown; restored from __doc__
        """
        Timestamp.utcfromtimestamp(ts)
        
                Construct a naive UTC datetime from a POSIX timestamp.
        """
        pass

    @classmethod
    def utcnow(cls): # real signature unknown; restored from __doc__
        """
        Timestamp.utcnow()
        
                Return a new Timestamp representing UTC day and time.
        """
        pass

    def _has_time_component(self, *args, **kwargs): # real signature unknown
        """
        Returns if the Timestamp has a time component
                in addition to the date part
        """
        pass

    def _round(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    dayofweek = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return day of the week.
        """

    dayofyear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the day of the year.
        """

    daysinmonth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the number of days in the month.
        """

    days_in_month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the number of days in the month.
        """

    freqstr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the total number of days in the month.
        """

    is_leap_year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return True if year is a leap year.
        """

    is_month_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return True if date is last day of month.
        """

    is_month_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return True if date is first day of month.
        """

    is_quarter_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return True if date is last day of the quarter.
        """

    is_quarter_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return True if date is first day of the quarter.
        """

    is_year_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return True if date is last day of the year.
        """

    is_year_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return True if date is first day of the year.
        """

    quarter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the quarter of the year.
        """

    tz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Alias for tzinfo.
        """

    week = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the week number of the year.
        """

    weekofyear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the week number of the year.
        """

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    max = Timestamp('2262-04-11 23:47:16.854775807')
    min = Timestamp('1677-09-21 00:12:43.145225')
    resolution = Timedelta('0 days 00:00:00.000000')
    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pandas._libs.tslibs.timestamps\', \'__doc__\': "\\n    Pandas replacement for python datetime.datetime object.\\n\\n    Timestamp is the pandas equivalent of python\'s Datetime\\n    and is interchangeable with it in most cases. It\'s the type used\\n    for the entries that make up a DatetimeIndex, and other timeseries\\n    oriented data structures in pandas.\\n\\n    Parameters\\n    ----------\\n    ts_input : datetime-like, str, int, float\\n        Value to be converted to Timestamp.\\n    freq : str, DateOffset\\n        Offset which Timestamp will have.\\n    tz : str, pytz.timezone, dateutil.tz.tzfile or None\\n        Time zone for time which Timestamp will have.\\n    unit : str\\n        Unit used for conversion if ts_input is of type int or float. The\\n        valid values are \'D\', \'h\', \'m\', \'s\', \'ms\', \'us\', and \'ns\'. For\\n        example, \'s\' means seconds and \'ms\' means milliseconds.\\n    year, month, day : int\\n    hour, minute, second, microsecond : int, optional, default 0\\n    nanosecond : int, optional, default 0\\n        .. versionadded:: 0.23.0\\n    tzinfo : datetime.tzinfo, optional, default None\\n\\n    Notes\\n    -----\\n    There are essentially three calling conventions for the constructor. The\\n    primary form accepts four parameters. They can be passed by position or\\n    keyword.\\n\\n    The other two forms mimic the parameters from ``datetime.datetime``. They\\n    can be passed by either position or keyword, but not both mixed together.\\n\\n    Examples\\n    --------\\n    Using the primary calling convention:\\n\\n    This converts a datetime-like string\\n\\n    >>> pd.Timestamp(\'2017-01-01T12\')\\n    Timestamp(\'2017-01-01 12:00:00\')\\n\\n    This converts a float representing a Unix epoch in units of seconds\\n\\n    >>> pd.Timestamp(1513393355.5, unit=\'s\')\\n    Timestamp(\'2017-12-16 03:02:35.500000\')\\n\\n    This converts an int representing a Unix-epoch in units of seconds\\n    and for a particular timezone\\n\\n    >>> pd.Timestamp(1513393355, unit=\'s\', tz=\'US/Pacific\')\\n    Timestamp(\'2017-12-15 19:02:35-0800\', tz=\'US/Pacific\')\\n\\n    Using the other two forms that mimic the API for ``datetime.datetime``:\\n\\n    >>> pd.Timestamp(2017, 1, 1, 12)\\n    Timestamp(\'2017-01-01 12:00:00\')\\n\\n    >>> pd.Timestamp(year=2017, month=1, day=1, hour=12)\\n    Timestamp(\'2017-01-01 12:00:00\')\\n    ", \'fromordinal\': <classmethod object at 0x000001B6FF63D780>, \'now\': <classmethod object at 0x000001B6FF6D8780>, \'today\': <classmethod object at 0x000001B6FF6D87B8>, \'utcnow\': <classmethod object at 0x000001B6FF6D87F0>, \'utcfromtimestamp\': <classmethod object at 0x000001B6FF6D8828>, \'fromtimestamp\': <classmethod object at 0x000001B6FF6D8748>, \'strptime\': <classmethod object at 0x000001B6FF6D8860>, \'combine\': <classmethod object at 0x000001B6FF6D8898>, \'__new__\': <cyfunction Timestamp.__new__ at 0x000001B6FF6CBD38>, \'_round\': <cyfunction Timestamp._round at 0x000001B6FF6CBDF0>, \'round\': <cyfunction Timestamp.round at 0x000001B6FF6CBEA8>, \'floor\': <cyfunction Timestamp.floor at 0x000001B6FF6CBF60>, \'ceil\': <cyfunction Timestamp.ceil at 0x000001B6FF6DD048>, \'tz\': <property object at 0x000001B6FF6D7638>, \'__setstate__\': <cyfunction Timestamp.__setstate__ at 0x000001B6FF6DD270>, \'__reduce__\': <cyfunction Timestamp.__reduce__ at 0x000001B6FF6DD328>, \'to_period\': <cyfunction Timestamp.to_period at 0x000001B6FF6DD3E0>, \'dayofweek\': <property object at 0x000001B6FF6D7598>, \'day_name\': <cyfunction Timestamp.day_name at 0x000001B6FF6DD550>, \'month_name\': <cyfunction Timestamp.month_name at 0x000001B6FF6DD608>, \'dayofyear\': <property object at 0x000001B6FF6D7688>, \'week\': <property object at 0x000001B6FF6D76D8>, \'weekofyear\': <property object at 0x000001B6FF6D76D8>, \'quarter\': <property object at 0x000001B6FF6D7728>, \'days_in_month\': <property object at 0x000001B6FF6D7778>, \'daysinmonth\': <property object at 0x000001B6FF6D7778>, \'freqstr\': <property object at 0x000001B6FF6D77C8>, \'is_month_start\': <property object at 0x000001B6FF6D7818>, \'is_month_end\': <property object at 0x000001B6FF6D7868>, \'is_quarter_start\': <property object at 0x000001B6FF6D78B8>, \'is_quarter_end\': <property object at 0x000001B6FF6D7908>, \'is_year_start\': <property object at 0x000001B6FF6D7958>, \'is_year_end\': <property object at 0x000001B6FF6D79A8>, \'is_leap_year\': <property object at 0x000001B6FF6D79F8>, \'tz_localize\': <cyfunction Timestamp.tz_localize at 0x000001B6FF6DDF60>, \'tz_convert\': <cyfunction Timestamp.tz_convert at 0x000001B6FF6E0048>, \'astimezone\': <cyfunction Timestamp.tz_convert at 0x000001B6FF6E0048>, \'replace\': <cyfunction Timestamp.replace at 0x000001B6FF6E0100>, \'isoformat\': <cyfunction Timestamp.isoformat at 0x000001B6FF6E01B8>, \'_has_time_component\': <cyfunction Timestamp._has_time_component at 0x000001B6FF6E0270>, \'to_julian_date\': <cyfunction Timestamp.to_julian_date at 0x000001B6FF6E0328>, \'normalize\': <cyfunction Timestamp.normalize at 0x000001B6FF6E03E0>, \'__radd__\': <cyfunction Timestamp.__radd__ at 0x000001B6FF6E0498>, \'__dict__\': <attribute \'__dict__\' of \'Timestamp\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'Timestamp\' objects>, \'min\': Timestamp(\'1677-09-21 00:12:43.145225\'), \'max\': Timestamp(\'2262-04-11 23:47:16.854775807\'), \'resolution\': Timedelta(\'0 days 00:00:00.000000\')})'


# variables with complex values

UTC = None # (!) real value is '<UTC>'

_no_input = None # (!) real value is '<object object at 0x000001B6F862E730>'

_zero_time = None # (!) real value is 'datetime.time(0, 0)'

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001B6FF6D3B70>'

__pyx_capi__ = {
    'create_timestamp_from_ts': None, # (!) real value is '<capsule object "PyObject *(__pyx_t_5numpy_int64_t, npy_datetimestruct, PyObject *, PyObject *)" at 0x000001B6FF6D0360>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.tslibs.timestamps', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001B6FF6D3B70>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\pandas\\\\_libs\\\\tslibs\\\\timestamps.cp37-win_amd64.pyd')"

__test__ = {}

