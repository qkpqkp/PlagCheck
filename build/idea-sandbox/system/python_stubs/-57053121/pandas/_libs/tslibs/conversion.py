# encoding: utf-8
# module pandas._libs.tslibs.conversion
# from C:\Users\Doly\Anaconda3\lib\site-packages\pandas\_libs\tslibs\conversion.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py
import pytz as pytz # C:\Users\Doly\Anaconda3\lib\site-packages\pytz\__init__.py
from pandas._libs.tslibs.np_datetime import OutOfBoundsDatetime

from pandas._libs.tslibs.parsing import parse_datetime_string

from pandas._libs.tslibs.tzconversion import (tz_convert_single, 
    tz_localize_to_utc)


# functions

def datetime_to_datetime64(*args, **kwargs): # real signature unknown
    """
    Convert ndarray of datetime-like objects to int64 array representing
        nanosecond timestamps.
    
        Parameters
        ----------
        values : ndarray[object]
    
        Returns
        -------
        result : ndarray[int64_t]
        inferred_tz : tzinfo or None
    """
    pass

def ensure_datetime64ns(*args, **kwargs): # real signature unknown
    """
    Ensure a np.datetime64 array has dtype specifically 'datetime64[ns]'
    
        Parameters
        ----------
        arr : ndarray
        copy : boolean, default True
    
        Returns
        -------
        result : ndarray with dtype datetime64[ns]
    """
    pass

def ensure_timedelta64ns(*args, **kwargs): # real signature unknown
    """
    Ensure a np.timedelta64 array has dtype specifically 'timedelta64[ns]'
    
        Parameters
        ----------
        arr : ndarray
        copy : boolean, default True
    
        Returns
        -------
        result : ndarray with dtype timedelta64[ns]
    """
    pass

def is_date_array_normalized(*args, **kwargs): # real signature unknown
    """
    Check if all of the given (nanosecond) timestamps are normalized to
        midnight, i.e. hour == minute == second == 0.  If the optional timezone
        `tz` is not None, then this is midnight for this timezone.
    
        Parameters
        ----------
        stamps : int64 ndarray
        tz : tzinfo or None
    
        Returns
        -------
        is_normalized : bool True if all stamps are normalized
    """
    pass

def localize_pydatetime(*args, **kwargs): # real signature unknown
    """
    Take a datetime/Timestamp in UTC and localizes to timezone tz.
    
        Parameters
        ----------
        dt : datetime or Timestamp
        tz : tzinfo, "UTC", or None
    
        Returns
        -------
        localized : datetime or Timestamp
    """
    pass

def normalize_date(*args, **kwargs): # real signature unknown
    """
    Normalize datetime.datetime value to midnight. Returns datetime.date as a
        datetime.datetime at midnight
    
        Parameters
        ----------
        dt : date, datetime, or Timestamp
    
        Returns
        -------
        normalized : datetime.datetime or Timestamp
    
        Raises
        ------
        TypeError : if input is not datetime.date, datetime.datetime, or Timestamp
    """
    pass

def normalize_i8_timestamps(*args, **kwargs): # real signature unknown
    """
    Normalize each of the (nanosecond) timezone aware timestamps in the given
        array by rounding down to the beginning of the day (i.e. midnight).
        This is midnight for timezone, `tz`.
    
        Parameters
        ----------
        stamps : int64 ndarray
        tz : tzinfo or None
    
        Returns
        -------
        result : int64 ndarray of converted of normalized nanosecond timestamps
    """
    pass

def pydt_to_i8(*args, **kwargs): # real signature unknown
    """
    Convert to int64 representation compatible with numpy datetime64; converts
        to UTC
    
        Parameters
        ----------
        pydt : object
    
        Returns
        -------
        i8value : np.int64
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
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


class _TSObject(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

nat_strings = None # (!) real value is "{'NaN', 'NAT', 'nan', 'nat', 'NAN', 'NaT'}"

NS_DTYPE = None # (!) real value is "dtype('<M8[ns]')"

TD_DTYPE = None # (!) real value is "dtype('<m8[ns]')"

UTC = pytz.UTC

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000019C7FD80860>'

__pyx_capi__ = {
    'convert_datetime_to_tsobject': None, # (!) real value is '<capsule object "struct __pyx_obj_6pandas_5_libs_6tslibs_10conversion__TSObject *(PyDateTime_DateTime *, PyObject *, struct __pyx_opt_args_6pandas_5_libs_6tslibs_10conversion_convert_datetime_to_tsobject *__pyx_optional_args)" at 0x0000019C7FD75780>'
    'convert_to_tsobject': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyObject *, PyObject *, int, int, struct __pyx_opt_args_6pandas_5_libs_6tslibs_10conversion_convert_to_tsobject *__pyx_optional_args)" at 0x0000019C7FD757B0>'
    'get_datetime64_nanos': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (PyObject *)" at 0x0000019C7FD75810>'
    'localize_pydatetime': None, # (!) real value is '<capsule object "PyDateTime_DateTime *(PyDateTime_DateTime *, PyObject *, int __pyx_skip_dispatch)" at 0x0000019C7FD75870>'
    'maybe_datetimelike_to_i8': None, # (!) real value is '<capsule object "PyObject *(PyObject *)" at 0x0000019C7FD75840>'
    'pydt_to_i8': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (PyObject *, int __pyx_skip_dispatch)" at 0x0000019C7FD757E0>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.tslibs.conversion', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000019C7FD80860>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\pandas\\\\_libs\\\\tslibs\\\\conversion.cp37-win_amd64.pyd')"

__test__ = {}

