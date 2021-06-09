# encoding: utf-8
# module pandas._libs.tslibs.c_timestamp
# from C:\Users\Doly\Anaconda3\lib\site-packages\pandas\_libs\tslibs\c_timestamp.cp37-win_amd64.pyd
# by generator 1.147
"""
_Timestamp is a c-defined subclass of datetime.datetime

It is separate from timestamps.pyx to prevent circular cimports

This allows _Timestamp to be imported in other modules
so that isinstance(obj, _Timestamp) checks can be performed

_Timestamp is PITA. Because we inherit from datetime, which has very specific
construction requirements, we need to do object instantiation in python
(see Timestamp class below). This will serve as a C extension type that
shadows the python class, where we do any heavy lifting.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import warnings as warnings # C:\Users\Doly\Anaconda3\lib\warnings.py
import numpy as np # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py
from pandas._libs.tslibs.fields import (get_date_name_field, 
    get_start_end_field)

from pandas._libs.tslibs.np_datetime import OutOfBoundsDatetime

import datetime as __datetime


# functions

def integer_op_not_supported(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class NullFrequencyError(ValueError):
    """
    Error raised when a null `freq` attribute is used in an operation
        that needs a non-null frequency, particularly `DatetimeIndex.shift`,
        `TimedeltaIndex.shift`, `PeriodIndex.shift`.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class _Timestamp(__datetime.datetime):
    # no doc
    def timestamp(self, *args, **kwargs): # real signature unknown
        """ Return POSIX timestamp as float. """
        pass

    def to_datetime64(self, *args, **kwargs): # real signature unknown
        """ Return a numpy.datetime64 object with 'ns' precision. """
        pass

    def to_numpy(self, *args, **kwargs): # real signature unknown
        """
        Convert the Timestamp to a NumPy datetime64.
        
                .. versionadded:: 0.25.0
        
                This is an alias method for `Timestamp.to_datetime64()`. The dtype and
                copy parameters are available here only for compatibility. Their values
                will not affect the return value.
        
                Returns
                -------
                numpy.datetime64
        
                See Also
                --------
                DatetimeIndex.to_numpy : Similar method for DatetimeIndex.
        """
        pass

    def to_pydatetime(self, *args, **kwargs): # real signature unknown
        """
        Convert a Timestamp object to a native Python datetime object.
        
                If warn=True, issue a warning if nanoseconds is nonzero.
        """
        pass

    def _get_date_name_field(self, *args, **kwargs): # real signature unknown
        pass

    def _get_start_end_field(self, *args, **kwargs): # real signature unknown
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

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    asm8 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return numpy datetime64 format in nanoseconds.
        """

    freq = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nanosecond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _date_attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _date_repr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _repr_base = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _short_repr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _time_repr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __array_priority__ = 100
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001E560495930>'


# variables with complex values

UTC = None # (!) real value is '<UTC>'

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001E5604AB5F8>'

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.tslibs.c_timestamp', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001E5604AB5F8>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\pandas\\\\_libs\\\\tslibs\\\\c_timestamp.cp37-win_amd64.pyd')"

__test__ = {}

