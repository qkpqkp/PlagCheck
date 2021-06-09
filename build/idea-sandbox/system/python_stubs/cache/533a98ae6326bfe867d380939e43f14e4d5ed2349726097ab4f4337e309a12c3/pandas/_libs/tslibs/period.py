# encoding: utf-8
# module pandas._libs.tslibs.period
# from C:\Users\Doly\Anaconda3\lib\site-packages\pandas\_libs\tslibs\period.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py
from pandas._libs.tslibs.offsets import _Tick

from pandas._libs.tslibs.parsing import parse_time_string

from pandas._libs.tslibs.resolution import Resolution

from pandas._libs.tslibs.timedeltas import Timedelta

from pandas._libs.tslibs.timestamps import Timestamp

import datetime as __datetime


# Variables with simple values

DIFFERENT_FREQ = 'Input has different freq={other_freq} from {cls}(freq={own_freq})'

# functions

def dt64arr_to_periodarr(*args, **kwargs): # real signature unknown
    """
    Convert array of datetime64 values (passed in as 'i8' dtype) to a set of
        periods corresponding to desired frequency, per period convention.
    """
    pass

def extract_freq(*args, **kwargs): # real signature unknown
    pass

def extract_ordinals(*args, **kwargs): # real signature unknown
    pass

def get_period_field_arr(*args, **kwargs): # real signature unknown
    pass

def periodarr_to_dt64arr(*args, **kwargs): # real signature unknown
    """
    Convert array to datetime64 values from a set of ordinals corresponding to
        periods per period convention.
    """
    pass

def period_asfreq(*args, **kwargs): # real signature unknown
    """
    Convert period ordinal from one frequency to another, and if upsampling,
        choose to use start ('S') or end ('E') of period.
    """
    pass

def period_asfreq_arr(*args, **kwargs): # real signature unknown
    """
    Convert int64-array of period ordinals from one frequency to another, and
        if upsampling, choose to use start ('S') or end ('E') of period.
    """
    pass

def period_ordinal(*args, **kwargs): # real signature unknown
    """
    Find the ordinal representation of the given datetime components at the
        frequency `freq`.
    
        Parameters
        ----------
        y : int
        m : int
        d : int
        h : int
        min : int
        s : int
        us : int
        ps : int
    
        Returns
        -------
        ordinal : int64_t
    """
    pass

def quarter_to_myear(*args, **kwargs): # real signature unknown
    """
    A quarterly frequency defines a "year" which may not coincide with
        the calendar-year.  Find the calendar-year and calendar-month associated
        with the given year and quarter under the `freq`-derived calendar.
    
        Parameters
        ----------
        year : int
        quarter : int
        freq : DateOffset
    
        Returns
        -------
        year : int
        month : int
    
        See Also
        --------
        Period.qyear
    """
    pass

def _validate_end_alias(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class datetime(__datetime.date):
    """
    datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])
    
    The year, month and day arguments are required. tzinfo may be None, or an
    instance of a tzinfo subclass. The remaining arguments may be ints.
    """
    def astimezone(self, *args, **kwargs): # real signature unknown
        """ tz -> convert to local time in new timezone tz """
        pass

    @classmethod
    def combine(cls, *args, **kwargs): # real signature unknown
        """ date, time -> datetime with same date and time fields """
        pass

    def ctime(self): # real signature unknown; restored from __doc__
        """ Return ctime() style string. """
        pass

    def date(self, *args, **kwargs): # real signature unknown
        """ Return date object with same year, month and day. """
        pass

    def dst(self): # real signature unknown; restored from __doc__
        """ Return self.tzinfo.dst(self). """
        pass

    @classmethod
    def fromisoformat(cls, *args, **kwargs): # real signature unknown
        """ string -> datetime from datetime.isoformat() output """
        pass

    @classmethod
    def fromtimestamp(cls, *args, **kwargs): # real signature unknown
        """ timestamp[, tz] -> tz's local time from POSIX timestamp. """
        pass

    def isoformat(self, *args, **kwargs): # real signature unknown
        """
        [sep] -> string in ISO 8601 format, YYYY-MM-DDT[HH[:MM[:SS[.mmm[uuu]]]]][+HH:MM].
        sep is used to separate the year from the time, and defaults to 'T'.
        timespec specifies what components of the time to include (allowed values are 'auto', 'hours', 'minutes', 'seconds', 'milliseconds', and 'microseconds').
        """
        pass

    @classmethod
    def now(cls, *args, **kwargs): # real signature unknown
        """
        Returns new datetime object representing current time local to tz.
        
          tz
            Timezone object.
        
        If no tz is specified, uses local timezone.
        """
        pass

    def replace(self, *args, **kwargs): # real signature unknown
        """ Return datetime with new specified fields. """
        pass

    @classmethod
    def strptime(cls): # real signature unknown; restored from __doc__
        """ string, format -> new datetime parsed from a string (like time.strptime()). """
        pass

    def time(self, *args, **kwargs): # real signature unknown
        """ Return time object with same time but with tzinfo=None. """
        pass

    def timestamp(self, *args, **kwargs): # real signature unknown
        """ Return POSIX timestamp as float. """
        pass

    def timetuple(self, *args, **kwargs): # real signature unknown
        """ Return time tuple, compatible with time.localtime(). """
        pass

    def timetz(self, *args, **kwargs): # real signature unknown
        """ Return time object with same time and tzinfo. """
        pass

    def tzname(self): # real signature unknown; restored from __doc__
        """ Return self.tzinfo.tzname(self). """
        pass

    @classmethod
    def utcfromtimestamp(cls, *args, **kwargs): # real signature unknown
        """ Construct a naive UTC datetime from a POSIX timestamp. """
        pass

    @classmethod
    def utcnow(cls, *args, **kwargs): # real signature unknown
        """ Return a new datetime representing UTC day and time. """
        pass

    def utcoffset(self): # real signature unknown; restored from __doc__
        """ Return self.tzinfo.utcoffset(self). """
        pass

    def utctimetuple(self, *args, **kwargs): # real signature unknown
        """ Return UTC time tuple, compatible with time.localtime(). """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
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

    def __init__(self, year, month, day, hour=None, minute=None, second=None, microsecond=None, tzinfo=None): # real signature unknown; restored from __doc__
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

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
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

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    fold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    microsecond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    minute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    second = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tzinfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    max = datetime.datetime(9999, 12, 31, 23, 59, 59, 999999)
    min = datetime.datetime(1, 1, 1, 0, 0)
    resolution = datetime.timedelta(microseconds=1)


class IncompatibleFrequency(ValueError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class _Period(object):
    # no doc
    def asfreq(self, *args, **kwargs): # real signature unknown
        """
        Convert Period to desired frequency, at the start or end of the interval.
        
                Parameters
                ----------
                freq : str
                    The desired frequency.
                how : {'E', 'S', 'end', 'start'}, default 'end'
                    Start or end of the timespan.
        
                Returns
                -------
                resampled : Period
        """
        pass

    @classmethod
    def now(cls, *args, **kwargs): # real signature unknown
        pass

    def strftime(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Returns the string representation of the :class:`Period`, depending
                on the selected ``fmt``. ``fmt`` must be a string
                containing one or several directives.  The method recognizes the same
                directives as the :func:`time.strftime` function of the standard Python
                distribution, as well as the specific additional directives ``%f``,
                ``%F``, ``%q``. (formatting & docs originally from scikits.timeries).
        
                +-----------+--------------------------------+-------+
                | Directive | Meaning                        | Notes |
                +===========+================================+=======+
                | ``%a``    | Locale's abbreviated weekday   |       |
                |           | name.                          |       |
                +-----------+--------------------------------+-------+
                | ``%A``    | Locale's full weekday name.    |       |
                +-----------+--------------------------------+-------+
                | ``%b``    | Locale's abbreviated month     |       |
                |           | name.                          |       |
                +-----------+--------------------------------+-------+
                | ``%B``    | Locale's full month name.      |       |
                +-----------+--------------------------------+-------+
                | ``%c``    | Locale's appropriate date and  |       |
                |           | time representation.           |       |
                +-----------+--------------------------------+-------+
                | ``%d``    | Day of the month as a decimal  |       |
                |           | number [01,31].                |       |
                +-----------+--------------------------------+-------+
                | ``%f``    | 'Fiscal' year without a        | \(1)  |
                |           | century  as a decimal number   |       |
                |           | [00,99]                        |       |
                +-----------+--------------------------------+-------+
                | ``%F``    | 'Fiscal' year with a century   | \(2)  |
                |           | as a decimal number            |       |
                +-----------+--------------------------------+-------+
                | ``%H``    | Hour (24-hour clock) as a      |       |
                |           | decimal number [00,23].        |       |
                +-----------+--------------------------------+-------+
                | ``%I``    | Hour (12-hour clock) as a      |       |
                |           | decimal number [01,12].        |       |
                +-----------+--------------------------------+-------+
                | ``%j``    | Day of the year as a decimal   |       |
                |           | number [001,366].              |       |
                +-----------+--------------------------------+-------+
                | ``%m``    | Month as a decimal number      |       |
                |           | [01,12].                       |       |
                +-----------+--------------------------------+-------+
                | ``%M``    | Minute as a decimal number     |       |
                |           | [00,59].                       |       |
                +-----------+--------------------------------+-------+
                | ``%p``    | Locale's equivalent of either  | \(3)  |
                |           | AM or PM.                      |       |
                +-----------+--------------------------------+-------+
                | ``%q``    | Quarter as a decimal number    |       |
                |           | [01,04]                        |       |
                +-----------+--------------------------------+-------+
                | ``%S``    | Second as a decimal number     | \(4)  |
                |           | [00,61].                       |       |
                +-----------+--------------------------------+-------+
                | ``%U``    | Week number of the year        | \(5)  |
                |           | (Sunday as the first day of    |       |
                |           | the week) as a decimal number  |       |
                |           | [00,53].  All days in a new    |       |
                |           | year preceding the first       |       |
                |           | Sunday are considered to be in |       |
                |           | week 0.                        |       |
                +-----------+--------------------------------+-------+
                | ``%w``    | Weekday as a decimal number    |       |
                |           | [0(Sunday),6].                 |       |
                +-----------+--------------------------------+-------+
                | ``%W``    | Week number of the year        | \(5)  |
                |           | (Monday as the first day of    |       |
                |           | the week) as a decimal number  |       |
                |           | [00,53].  All days in a new    |       |
                |           | year preceding the first       |       |
                |           | Monday are considered to be in |       |
                |           | week 0.                        |       |
                +-----------+--------------------------------+-------+
                | ``%x``    | Locale's appropriate date      |       |
                |           | representation.                |       |
                +-----------+--------------------------------+-------+
                | ``%X``    | Locale's appropriate time      |       |
                |           | representation.                |       |
                +-----------+--------------------------------+-------+
                | ``%y``    | Year without century as a      |       |
                |           | decimal number [00,99].        |       |
                +-----------+--------------------------------+-------+
                | ``%Y``    | Year with century as a decimal |       |
                |           | number.                        |       |
                +-----------+--------------------------------+-------+
                | ``%Z``    | Time zone name (no characters  |       |
                |           | if no time zone exists).       |       |
                +-----------+--------------------------------+-------+
                | ``%%``    | A literal ``'%'`` character.   |       |
                +-----------+--------------------------------+-------+
        
                Notes
                -----
        
                (1)
                    The ``%f`` directive is the same as ``%y`` if the frequency is
                    not quarterly.
                    Otherwise, it corresponds to the 'fiscal' year, as defined by
                    the :attr:`qyear` attribute.
        
                (2)
                    The ``%F`` directive is the same as ``%Y`` if the frequency is
                    not quarterly.
                    Otherwise, it corresponds to the 'fiscal' year, as defined by
                    the :attr:`qyear` attribute.
        
                (3)
                    The ``%p`` directive only affects the output hour field
                    if the ``%I`` directive is used to parse the hour.
        
                (4)
                    The range really is ``0`` to ``61``; this accounts for leap
                    seconds and the (very rare) double leap seconds.
        
                (5)
                    The ``%U`` and ``%W`` directives are only used in calculations
                    when the day of the week and the year are specified.
        
                Examples
                --------
        
                >>> a = Period(freq='Q-JUL', year=2006, quarter=1)
                >>> a.strftime('%F-Q%q')
                '2006-Q1'
                >>> # Output the last month in the quarter of this date
                >>> a.strftime('%b-%Y')
                'Oct-2005'
                >>>
                >>> a = Period(freq='D', year=2001, month=1, day=1)
                >>> a.strftime('%d-%b-%Y')
                '01-Jan-2006'
                >>> a.strftime('%b. %d, %Y was a %A')
                'Jan. 01, 2001 was a Monday'
        """
        pass

    def to_timestamp(self, *args, **kwargs): # real signature unknown
        """
        Return the Timestamp representation of the Period.
        
                Uses the target frequency specified at the part of the period specified
                by `how`, which is either `Start` or `Finish`.
        
                Parameters
                ----------
                freq : str or DateOffset
                    Target frequency. Default is 'D' if self.freq is week or
                    longer and 'S' otherwise.
                how : str, default 'S' (start)
                    One of 'S', 'E'. Can be aliased as case insensitive
                    'Start', 'Finish', 'Begin', 'End'.
        
                Returns
                -------
                Timestamp
        """
        pass

    def _add_delta(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def _from_ordinal(cls, *args, **kwargs): # real signature unknown
        """ Fast creation from an ordinal and freq that are already validated! """
        pass

    @classmethod
    def _maybe_convert_freq(cls, *args, **kwargs): # real signature unknown
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

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return a string representation for a particular DataFrame """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    day = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Get day of the month that a Period falls on.

        Returns
        -------
        int

        See Also
        --------
        Period.dayofweek : Get the day of the week.
        Period.dayofyear : Get the day of the year.

        Examples
        --------
        >>> p = pd.Period("2018-03-11", freq='H')
        >>> p.day
        11
        """

    dayofweek = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Day of the week the period lies in, with Monday=0 and Sunday=6.

        If the period frequency is lower than daily (e.g. hourly), and the
        period spans over multiple days, the day at the start of the period is
        used.

        If the frequency is higher than daily (e.g. monthly), the last day
        of the period is used.

        Returns
        -------
        int
            Day of the week.

        See Also
        --------
        Period.dayofweek : Day of the week the period lies in.
        Period.weekday : Alias of Period.dayofweek.
        Period.day : Day of the month.
        Period.dayofyear : Day of the year.

        Examples
        --------
        >>> per = pd.Period('2017-12-31 22:00', 'H')
        >>> per.dayofweek
        6

        For periods that span over multiple days, the day at the beginning of
        the period is returned.

        >>> per = pd.Period('2017-12-31 22:00', '4H')
        >>> per.dayofweek
        6
        >>> per.start_time.dayofweek
        6

        For periods with a frequency higher than days, the last day of the
        period is returned.

        >>> per = pd.Period('2018-01', 'M')
        >>> per.dayofweek
        2
        >>> per.end_time.dayofweek
        2
        """

    dayofyear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the day of the year.

        This attribute returns the day of the year on which the particular
        date occurs. The return value ranges between 1 to 365 for regular
        years and 1 to 366 for leap years.

        Returns
        -------
        int
            The day of year.

        See Also
        --------
        Period.day : Return the day of the month.
        Period.dayofweek : Return the day of week.
        PeriodIndex.dayofyear : Return the day of year of all indexes.

        Examples
        --------
        >>> period = pd.Period("2015-10-23", freq='H')
        >>> period.dayofyear
        296
        >>> period = pd.Period("2012-12-31", freq='D')
        >>> period.dayofyear
        366
        >>> period = pd.Period("2013-01-01", freq='D')
        >>> period.dayofyear
        1
        """

    daysinmonth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Get the total number of days of the month that the Period falls in.

        Returns
        -------
        int

        See Also
        --------
        Period.days_in_month : Return the days of the month.
        Period.dayofyear : Return the day of the year.

        Examples
        --------
        >>> p = pd.Period("2018-03-11", freq='H')
        >>> p.daysinmonth
        31
        """

    days_in_month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Get the total number of days in the month that this period falls on.

        Returns
        -------
        int

        See Also
        --------
        Period.daysinmonth : Gets the number of days in the month.
        DatetimeIndex.daysinmonth : Gets the number of days in the month.
        calendar.monthrange : Returns a tuple containing weekday
            (0-6 ~ Mon-Sun) and number of days (28-31).

        Examples
        --------
        >>> p = pd.Period('2018-2-17')
        >>> p.days_in_month
        28

        >>> pd.Period('2018-03-01').days_in_month
        31

        Handles the leap year case as well:

        >>> p = pd.Period('2016-2-17')
        >>> p.days_in_month
        29
        """

    end_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    freq = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    freqstr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Get the hour of the day component of the Period.

        Returns
        -------
        int
            The hour as an integer, between 0 and 23.

        See Also
        --------
        Period.second : Get the second component of the Period.
        Period.minute : Get the minute component of the Period.

        Examples
        --------
        >>> p = pd.Period("2018-03-11 13:03:12.050000")
        >>> p.hour
        13

        Period longer than a day

        >>> p = pd.Period("2018-03-11", freq="M")
        >>> p.hour
        0
        """

    is_leap_year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    minute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Get minute of the hour component of the Period.

        Returns
        -------
        int
            The minute as an integer, between 0 and 59.

        See Also
        --------
        Period.hour : Get the hour component of the Period.
        Period.second : Get the second component of the Period.

        Examples
        --------
        >>> p = pd.Period("2018-03-11 13:03:12.050000")
        >>> p.minute
        3
        """

    month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ordinal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    quarter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qyear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Fiscal year the Period lies in according to its starting-quarter.

        The `year` and the `qyear` of the period will be the same if the fiscal
        and calendar years are the same. When they are not, the fiscal year
        can be different from the calendar year of the period.

        Returns
        -------
        int
            The fiscal year of the period.

        See Also
        --------
        Period.year : Return the calendar year of the period.

        Examples
        --------
        If the natural and fiscal year are the same, `qyear` and `year` will
        be the same.

        >>> per = pd.Period('2018Q1', freq='Q')
        >>> per.qyear
        2018
        >>> per.year
        2018

        If the fiscal year starts in April (`Q-MAR`), the first quarter of
        2018 will start in April 2017. `year` will then be 2018, but `qyear`
        will be the fiscal year, 2018.

        >>> per = pd.Period('2018Q1', freq='Q-MAR')
        >>> per.start_time
        Timestamp('2017-04-01 00:00:00')
        >>> per.qyear
        2018
        >>> per.year
        2017
        """

    second = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Get the second component of the Period.

        Returns
        -------
        int
            The second of the Period (ranges from 0 to 59).

        See Also
        --------
        Period.hour : Get the hour component of the Period.
        Period.minute : Get the minute component of the Period.

        Examples
        --------
        >>> p = pd.Period("2018-03-11 13:03:12.050000")
        >>> p.second
        12
        """

    start_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Get the Timestamp for the start of the period.

        Returns
        -------
        Timestamp

        See Also
        --------
        Period.end_time : Return the end Timestamp.
        Period.dayofyear : Return the day of year.
        Period.daysinmonth : Return the days in that month.
        Period.dayofweek : Return the day of the week.

        Examples
        --------
        >>> period = pd.Period('2012-1-1', freq='D')
        >>> period
        Period('2012-01-01', 'D')

        >>> period.start_time
        Timestamp('2012-01-01 00:00:00')

        >>> period.end_time
        Timestamp('2012-01-01 23:59:59.999999999')
        """

    week = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Get the week of the year on the given Period.

        Returns
        -------
        int

        See Also
        --------
        Period.dayofweek : Get the day component of the Period.
        Period.weekday : Get the day component of the Period.

        Examples
        --------
        >>> p = pd.Period("2018-03-11", "H")
        >>> p.week
        10

        >>> p = pd.Period("2018-02-01", "D")
        >>> p.week
        5

        >>> p = pd.Period("2018-01-06", "D")
        >>> p.week
        1
        """

    weekday = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Day of the week the period lies in, with Monday=0 and Sunday=6.

        If the period frequency is lower than daily (e.g. hourly), and the
        period spans over multiple days, the day at the start of the period is
        used.

        If the frequency is higher than daily (e.g. monthly), the last day
        of the period is used.

        Returns
        -------
        int
            Day of the week.

        See Also
        --------
        Period.dayofweek : Day of the week the period lies in.
        Period.weekday : Alias of Period.dayofweek.
        Period.day : Day of the month.
        Period.dayofyear : Day of the year.

        Examples
        --------
        >>> per = pd.Period('2017-12-31 22:00', 'H')
        >>> per.dayofweek
        6

        For periods that span over multiple days, the day at the beginning of
        the period is returned.

        >>> per = pd.Period('2017-12-31 22:00', '4H')
        >>> per.dayofweek
        6
        >>> per.start_time.dayofweek
        6

        For periods with a frequency higher than days, the last day of the
        period is returned.

        >>> per = pd.Period('2018-01', 'M')
        >>> per.dayofweek
        2
        >>> per.end_time.dayofweek
        2
        """

    weekofyear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    _typ = 'period'


class Period(_Period):
    """
    Represents a period of time.
    
        Parameters
        ----------
        value : Period or str, default None
            The time period represented (e.g., '4Q2005').
        freq : str, default None
            One of pandas period strings or corresponding objects.
        ordinal : int, default None
            The period offset from the gregorian proleptic epoch.
        year : int, default None
            Year value of the period.
        month : int, default 1
            Month value of the period.
        quarter : int, default None
            Quarter value of the period.
        day : int, default 1
            Day value of the period.
        hour : int, default 0
            Hour value of the period.
        minute : int, default 0
            Minute value of the period.
        second : int, default 0
            Second value of the period.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pandas._libs.tslibs.period\', \'__doc__\': "\\n    Represents a period of time.\\n\\n    Parameters\\n    ----------\\n    value : Period or str, default None\\n        The time period represented (e.g., \'4Q2005\').\\n    freq : str, default None\\n        One of pandas period strings or corresponding objects.\\n    ordinal : int, default None\\n        The period offset from the gregorian proleptic epoch.\\n    year : int, default None\\n        Year value of the period.\\n    month : int, default 1\\n        Month value of the period.\\n    quarter : int, default None\\n        Quarter value of the period.\\n    day : int, default 1\\n        Day value of the period.\\n    hour : int, default 0\\n        Hour value of the period.\\n    minute : int, default 0\\n        Minute value of the period.\\n    second : int, default 0\\n        Second value of the period.\\n    ", \'__new__\': <cyfunction Period.__new__ at 0x000001ABF8DE0B10>, \'__dict__\': <attribute \'__dict__\' of \'Period\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'Period\' objects>})'


# variables with complex values

MONTH_NUMBERS = {
    'APR': 3,
    'AUG': 7,
    'DEC': 11,
    'FEB': 1,
    'JAN': 0,
    'JUL': 6,
    'JUN': 5,
    'MAR': 2,
    'MAY': 4,
    'NOV': 10,
    'OCT': 9,
    'SEP': 8,
}

nat_strings = None # (!) real value is "{'NaN', 'NaT', 'nat', 'NAT', 'NAN', 'nan'}"

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001ABF8D41978>'

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.tslibs.period', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001ABF8D41978>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\pandas\\\\_libs\\\\tslibs\\\\period.cp37-win_amd64.pyd')"

__test__ = {
    '_Period.day.__get__ (line 1824)': '\n        Get day of the month that a Period falls on.\n\n        Returns\n        -------\n        int\n\n        See Also\n        --------\n        Period.dayofweek : Get the day of the week.\n        Period.dayofyear : Get the day of the year.\n\n        Examples\n        --------\n        >>> p = pd.Period("2018-03-11", freq=\'H\')\n        >>> p.day\n        11\n        ',
    '_Period.dayofweek.__get__ (line 1960)': "\n        Day of the week the period lies in, with Monday=0 and Sunday=6.\n\n        If the period frequency is lower than daily (e.g. hourly), and the\n        period spans over multiple days, the day at the start of the period is\n        used.\n\n        If the frequency is higher than daily (e.g. monthly), the last day\n        of the period is used.\n\n        Returns\n        -------\n        int\n            Day of the week.\n\n        See Also\n        --------\n        Period.dayofweek : Day of the week the period lies in.\n        Period.weekday : Alias of Period.dayofweek.\n        Period.day : Day of the month.\n        Period.dayofyear : Day of the year.\n\n        Examples\n        --------\n        >>> per = pd.Period('2017-12-31 22:00', 'H')\n        >>> per.dayofweek\n        6\n\n        For periods that span over multiple days, the day at the beginning of\n        the period is returned.\n\n        >>> per = pd.Period('2017-12-31 22:00', '4H')\n        >>> per.dayofweek\n        6\n        >>> per.start_time.dayofweek\n        6\n\n        For periods with a frequency higher than days, the last day of the\n        period is returned.\n\n        >>> per = pd.Period('2018-01', 'M')\n        >>> per.dayofweek\n        2\n        >>> per.end_time.dayofweek\n        2\n        ",
    '_Period.dayofyear.__get__ (line 2064)': '\n        Return the day of the year.\n\n        This attribute returns the day of the year on which the particular\n        date occurs. The return value ranges between 1 to 365 for regular\n        years and 1 to 366 for leap years.\n\n        Returns\n        -------\n        int\n            The day of year.\n\n        See Also\n        --------\n        Period.day : Return the day of the month.\n        Period.dayofweek : Return the day of week.\n        PeriodIndex.dayofyear : Return the day of year of all indexes.\n\n        Examples\n        --------\n        >>> period = pd.Period("2015-10-23", freq=\'H\')\n        >>> period.dayofyear\n        296\n        >>> period = pd.Period("2012-12-31", freq=\'D\')\n        >>> period.dayofyear\n        366\n        >>> period = pd.Period("2013-01-01", freq=\'D\')\n        >>> period.dayofyear\n        1\n        ',
    '_Period.days_in_month.__get__ (line 2148)': "\n        Get the total number of days in the month that this period falls on.\n\n        Returns\n        -------\n        int\n\n        See Also\n        --------\n        Period.daysinmonth : Gets the number of days in the month.\n        DatetimeIndex.daysinmonth : Gets the number of days in the month.\n        calendar.monthrange : Returns a tuple containing weekday\n            (0-6 ~ Mon-Sun) and number of days (28-31).\n\n        Examples\n        --------\n        >>> p = pd.Period('2018-2-17')\n        >>> p.days_in_month\n        28\n\n        >>> pd.Period('2018-03-01').days_in_month\n        31\n\n        Handles the leap year case as well:\n\n        >>> p = pd.Period('2016-2-17')\n        >>> p.days_in_month\n        29\n        ",
    '_Period.daysinmonth.__get__ (line 2182)': '\n        Get the total number of days of the month that the Period falls in.\n\n        Returns\n        -------\n        int\n\n        See Also\n        --------\n        Period.days_in_month : Return the days of the month.\n        Period.dayofyear : Return the day of the year.\n\n        Examples\n        --------\n        >>> p = pd.Period("2018-03-11", freq=\'H\')\n        >>> p.daysinmonth\n        31\n        ',
    '_Period.hour.__get__ (line 1847)': '\n        Get the hour of the day component of the Period.\n\n        Returns\n        -------\n        int\n            The hour as an integer, between 0 and 23.\n\n        See Also\n        --------\n        Period.second : Get the second component of the Period.\n        Period.minute : Get the minute component of the Period.\n\n        Examples\n        --------\n        >>> p = pd.Period("2018-03-11 13:03:12.050000")\n        >>> p.hour\n        13\n\n        Period longer than a day\n\n        >>> p = pd.Period("2018-03-11", freq="M")\n        >>> p.hour\n        0\n        ',
    '_Period.minute.__get__ (line 1877)': '\n        Get minute of the hour component of the Period.\n\n        Returns\n        -------\n        int\n            The minute as an integer, between 0 and 59.\n\n        See Also\n        --------\n        Period.hour : Get the hour component of the Period.\n        Period.second : Get the second component of the Period.\n\n        Examples\n        --------\n        >>> p = pd.Period("2018-03-11 13:03:12.050000")\n        >>> p.minute\n        3\n        ',
    '_Period.qyear.__get__ (line 2104)': "\n        Fiscal year the Period lies in according to its starting-quarter.\n\n        The `year` and the `qyear` of the period will be the same if the fiscal\n        and calendar years are the same. When they are not, the fiscal year\n        can be different from the calendar year of the period.\n\n        Returns\n        -------\n        int\n            The fiscal year of the period.\n\n        See Also\n        --------\n        Period.year : Return the calendar year of the period.\n\n        Examples\n        --------\n        If the natural and fiscal year are the same, `qyear` and `year` will\n        be the same.\n\n        >>> per = pd.Period('2018Q1', freq='Q')\n        >>> per.qyear\n        2018\n        >>> per.year\n        2018\n\n        If the fiscal year starts in April (`Q-MAR`), the first quarter of\n        2018 will start in April 2017. `year` will then be 2018, but `qyear`\n        will be the fiscal year, 2018.\n\n        >>> per = pd.Period('2018Q1', freq='Q-MAR')\n        >>> per.start_time\n        Timestamp('2017-04-01 00:00:00')\n        >>> per.qyear\n        2018\n        >>> per.year\n        2017\n        ",
    '_Period.second.__get__ (line 1901)': '\n        Get the second component of the Period.\n\n        Returns\n        -------\n        int\n            The second of the Period (ranges from 0 to 59).\n\n        See Also\n        --------\n        Period.hour : Get the hour component of the Period.\n        Period.minute : Get the minute component of the Period.\n\n        Examples\n        --------\n        >>> p = pd.Period("2018-03-11 13:03:12.050000")\n        >>> p.second\n        12\n        ',
    '_Period.start_time.__get__ (line 1738)': "\n        Get the Timestamp for the start of the period.\n\n        Returns\n        -------\n        Timestamp\n\n        See Also\n        --------\n        Period.end_time : Return the end Timestamp.\n        Period.dayofyear : Return the day of year.\n        Period.daysinmonth : Return the days in that month.\n        Period.dayofweek : Return the day of the week.\n\n        Examples\n        --------\n        >>> period = pd.Period('2012-1-1', freq='D')\n        >>> period\n        Period('2012-01-01', 'D')\n\n        >>> period.start_time\n        Timestamp('2012-01-01 00:00:00')\n\n        >>> period.end_time\n        Timestamp('2012-01-01 23:59:59.999999999')\n        ",
    '_Period.strftime (line 2237)': "\n        Returns the string representation of the :class:`Period`, depending\n        on the selected ``fmt``. ``fmt`` must be a string\n        containing one or several directives.  The method recognizes the same\n        directives as the :func:`time.strftime` function of the standard Python\n        distribution, as well as the specific additional directives ``%f``,\n        ``%F``, ``%q``. (formatting & docs originally from scikits.timeries).\n\n        +-----------+--------------------------------+-------+\n        | Directive | Meaning                        | Notes |\n        +===========+================================+=======+\n        | ``%a``    | Locale's abbreviated weekday   |       |\n        |           | name.                          |       |\n        +-----------+--------------------------------+-------+\n        | ``%A``    | Locale's full weekday name.    |       |\n        +-----------+--------------------------------+-------+\n        | ``%b``    | Locale's abbreviated month     |       |\n        |           | name.                          |       |\n        +-----------+--------------------------------+-------+\n        | ``%B``    | Locale's full month name.      |       |\n        +-----------+--------------------------------+-------+\n        | ``%c``    | Locale's appropriate date and  |       |\n        |           | time representation.           |       |\n        +-----------+--------------------------------+-------+\n        | ``%d``    | Day of the month as a decimal  |       |\n        |           | number [01,31].                |       |\n        +-----------+--------------------------------+-------+\n        | ``%f``    | 'Fiscal' year without a        | \\(1)  |\n        |           | century  as a decimal number   |       |\n        |           | [00,99]                        |       |\n        +-----------+--------------------------------+-------+\n        | ``%F``    | 'Fiscal' year with a century   | \\(2)  |\n        |           | as a decimal number            |       |\n        +-----------+--------------------------------+-------+\n        | ``%H``    | Hour (24-hour clock) as a      |       |\n        |           | decimal number [00,23].        |       |\n        +-----------+--------------------------------+-------+\n        | ``%I``    | Hour (12-hour clock) as a      |       |\n        |           | decimal number [01,12].        |       |\n        +-----------+--------------------------------+-------+\n        | ``%j``    | Day of the year as a decimal   |       |\n        |           | number [001,366].              |       |\n        +-----------+--------------------------------+-------+\n        | ``%m``    | Month as a decimal number      |       |\n        |           | [01,12].                       |       |\n        +-----------+--------------------------------+-------+\n        | ``%M``    | Minute as a decimal number     |       |\n        |           | [00,59].                       |       |\n        +-----------+--------------------------------+-------+\n        | ``%p``    | Locale's equivalent of either  | \\(3)  |\n        |           | AM or PM.                      |       |\n        +-----------+--------------------------------+-------+\n        | ``%q``    | Quarter as a decimal number    |       |\n        |           | [01,04]                        |       |\n        +-----------+--------------------------------+-------+\n        | ``%S``    | Second as a decimal number     | \\(4)  |\n        |           | [00,61].                       |       |\n        +-----------+--------------------------------+-------+\n        | ``%U``    | Week number of the year        | \\(5)  |\n        |           | (Sunday as the first day of    |       |\n        |           | the week) as a decimal number  |       |\n        |           | [00,53].  All days in a new    |       |\n        |           | year preceding the first       |       |\n        |           | Sunday are considered to be in |       |\n        |           | week 0.                        |       |\n        +-----------+--------------------------------+-------+\n        | ``%w``    | Weekday as a decimal number    |       |\n        |           | [0(Sunday),6].                 |       |\n        +-----------+--------------------------------+-------+\n        | ``%W``    | Week number of the year        | \\(5)  |\n        |           | (Monday as the first day of    |       |\n        |           | the week) as a decimal number  |       |\n        |           | [00,53].  All days in a new    |       |\n        |           | year preceding the first       |       |\n        |           | Monday are considered to be in |       |\n        |           | week 0.                        |       |\n        +-----------+--------------------------------+-------+\n        | ``%x``    | Locale's appropriate date      |       |\n        |           | representation.                |       |\n        +-----------+--------------------------------+-------+\n        | ``%X``    | Locale's appropriate time      |       |\n        |           | representation.                |       |\n        +-----------+--------------------------------+-------+\n        | ``%y``    | Year without century as a      |       |\n        |           | decimal number [00,99].        |       |\n        +-----------+--------------------------------+-------+\n        | ``%Y``    | Year with century as a decimal |       |\n        |           | number.                        |       |\n        +-----------+--------------------------------+-------+\n        | ``%Z``    | Time zone name (no characters  |       |\n        |           | if no time zone exists).       |       |\n        +-----------+--------------------------------+-------+\n        | ``%%``    | A literal ``'%'`` character.   |       |\n        +-----------+--------------------------------+-------+\n\n        Notes\n        -----\n\n        (1)\n            The ``%f`` directive is the same as ``%y`` if the frequency is\n            not quarterly.\n            Otherwise, it corresponds to the 'fiscal' year, as defined by\n            the :attr:`qyear` attribute.\n\n        (2)\n            The ``%F`` directive is the same as ``%Y`` if the frequency is\n            not quarterly.\n            Otherwise, it corresponds to the 'fiscal' year, as defined by\n            the :attr:`qyear` attribute.\n\n        (3)\n            The ``%p`` directive only affects the output hour field\n            if the ``%I`` directive is used to parse the hour.\n\n        (4)\n            The range really is ``0`` to ``61``; this accounts for leap\n            seconds and the (very rare) double leap seconds.\n\n        (5)\n            The ``%U`` and ``%W`` directives are only used in calculations\n            when the day of the week and the year are specified.\n\n        Examples\n        --------\n\n        >>> a = Period(freq='Q-JUL', year=2006, quarter=1)\n        >>> a.strftime('%F-Q%q')\n        '2006-Q1'\n        >>> # Output the last month in the quarter of this date\n        >>> a.strftime('%b-%Y')\n        'Oct-2005'\n        >>>\n        >>> a = Period(freq='D', year=2001, month=1, day=1)\n        >>> a.strftime('%d-%b-%Y')\n        '01-Jan-2006'\n        >>> a.strftime('%b. %d, %Y was a %A')\n        'Jan. 01, 2001 was a Monday'\n        ",
    '_Period.week.__get__ (line 1930)': '\n        Get the week of the year on the given Period.\n\n        Returns\n        -------\n        int\n\n        See Also\n        --------\n        Period.dayofweek : Get the day component of the Period.\n        Period.weekday : Get the day component of the Period.\n\n        Examples\n        --------\n        >>> p = pd.Period("2018-03-11", "H")\n        >>> p.week\n        10\n\n        >>> p = pd.Period("2018-02-01", "D")\n        >>> p.week\n        5\n\n        >>> p = pd.Period("2018-01-06", "D")\n        >>> p.week\n        1\n        ',
    '_Period.weekday.__get__ (line 2011)': "\n        Day of the week the period lies in, with Monday=0 and Sunday=6.\n\n        If the period frequency is lower than daily (e.g. hourly), and the\n        period spans over multiple days, the day at the start of the period is\n        used.\n\n        If the frequency is higher than daily (e.g. monthly), the last day\n        of the period is used.\n\n        Returns\n        -------\n        int\n            Day of the week.\n\n        See Also\n        --------\n        Period.dayofweek : Day of the week the period lies in.\n        Period.weekday : Alias of Period.dayofweek.\n        Period.day : Day of the month.\n        Period.dayofyear : Day of the year.\n\n        Examples\n        --------\n        >>> per = pd.Period('2017-12-31 22:00', 'H')\n        >>> per.dayofweek\n        6\n\n        For periods that span over multiple days, the day at the beginning of\n        the period is returned.\n\n        >>> per = pd.Period('2017-12-31 22:00', '4H')\n        >>> per.dayofweek\n        6\n        >>> per.start_time.dayofweek\n        6\n\n        For periods with a frequency higher than days, the last day of the\n        period is returned.\n\n        >>> per = pd.Period('2018-01', 'M')\n        >>> per.dayofweek\n        2\n        >>> per.end_time.dayofweek\n        2\n        ",
}

