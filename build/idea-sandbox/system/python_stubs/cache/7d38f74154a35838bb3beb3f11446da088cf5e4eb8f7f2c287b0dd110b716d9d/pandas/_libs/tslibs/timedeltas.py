# encoding: utf-8
# module pandas._libs.tslibs.timedeltas
# from C:\Users\Doly\Anaconda3\lib\site-packages\pandas\_libs\tslibs\timedeltas.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import collections as collections # C:\Users\Doly\Anaconda3\lib\collections\__init__.py
import textwrap as textwrap # C:\Users\Doly\Anaconda3\lib\textwrap.py
import numpy as np # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py
from pandas._libs.tslibs.offsets import Tick

import datetime as __datetime


# Variables with simple values

DAY_SECONDS = 86400

# functions

def array_to_timedelta64(*args, **kwargs): # real signature unknown
    """
    Convert an ndarray to an array of timedeltas. If errors == 'coerce',
        coerce non-convertible objects to NaT. Otherwise, raise.
    """
    pass

def delta_to_nanoseconds(*args, **kwargs): # real signature unknown
    pass

def ints_to_pytimedelta(*args, **kwargs): # real signature unknown
    """
    convert an i8 repr to an ndarray of timedelta or Timedelta (if box ==
        True)
    
        Parameters
        ----------
        arr : ndarray[int64_t]
        box : bool, default False
    
        Returns
        -------
        result : ndarray[object]
            array of Timedelta or timedeltas objects
    """
    pass

def parse_timedelta_unit(*args, **kwargs): # real signature unknown
    """
    Parameters
        ----------
        unit : an unit string
    """
    pass

def precision_from_unit(*args, **kwargs): # real signature unknown
    """
    Return a casting of the unit represented to nanoseconds + the precision
        to round the fractional part.
    """
    pass

def _binary_op_method_timedeltalike(*args, **kwargs): # real signature unknown
    pass

def _op_unary_method(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle__Timedelta(*args, **kwargs): # real signature unknown
    pass

# classes

class Components(tuple):
    """ Components(days, hours, minutes, seconds, milliseconds, microseconds, nanoseconds) """
    def _asdict(self): # reliably restored by inspect
        """ Return a new OrderedDict which maps field names to their values. """
        pass

    @classmethod
    def _make(cls, *args, **kwargs): # real signature unknown
        """ Make a new Components object from a sequence or iterable """
        pass

    def _replace(_self, **kwds): # reliably restored by inspect
        """ Return a new Components object replacing specified fields with new values """
        pass

    def __getnewargs__(self): # reliably restored by inspect
        """ Return self as a plain tuple.  Used by copy and pickle. """
        pass

    def __init__(self, days, hours, minutes, seconds, milliseconds, microseconds, nanoseconds): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(_cls, days, hours, minutes, seconds, milliseconds, microseconds, nanoseconds): # reliably restored by inspect
        """ Create new instance of Components(days, hours, minutes, seconds, milliseconds, microseconds, nanoseconds) """
        pass

    def __repr__(self): # reliably restored by inspect
        """ Return a nicely formatted representation string """
        pass

    days = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 0"""

    hours = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 1"""

    microseconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 5"""

    milliseconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 4"""

    minutes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 2"""

    nanoseconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 6"""

    seconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 3"""


    _fields = (
        'days',
        'hours',
        'minutes',
        'seconds',
        'milliseconds',
        'microseconds',
        'nanoseconds',
    )
    _fields_defaults = {}
    __slots__ = ()


class _Timedelta(__datetime.timedelta):
    # no doc
    def isoformat(self): # real signature unknown; restored from __doc__
        """
        Format Timedelta as ISO 8601 Duration like
                ``P[n]Y[n]M[n]DT[n]H[n]M[n]S``, where the ``[n]`` s are replaced by the
                values. See https://en.wikipedia.org/wiki/ISO_8601#Durations.
        
                Returns
                -------
                formatted : str
        
                See Also
                --------
                Timestamp.isoformat
        
                Notes
                -----
                The longest component is days, whose value may be larger than
                365.
                Every component is always included, even if its value is 0.
                Pandas uses nanosecond precision, so up to 9 decimal places may
                be included in the seconds component.
                Trailing 0's are removed from the seconds component after the decimal.
                We do not 0 pad components, so it's `...T5H...`, not `...T05H...`
        
                Examples
                --------
                >>> td = pd.Timedelta(days=6, minutes=50, seconds=3,
                ...                   milliseconds=10, microseconds=10, nanoseconds=12)
                >>> td.isoformat()
                'P6DT0H50M3.010010012S'
                >>> pd.Timedelta(hours=1, seconds=10).isoformat()
                'P0DT0H0M10S'
                >>> pd.Timedelta(hours=1, seconds=10).isoformat()
                'P0DT0H0M10S'
                >>> pd.Timedelta(days=500.5).isoformat()
                'P500DT12H0MS'
        """
        pass

    def total_seconds(self, *args, **kwargs): # real signature unknown
        """ Total duration of timedelta in seconds (to ns precision). """
        pass

    def to_numpy(self, *args, **kwargs): # real signature unknown
        """
        Convert the Timedelta to a NumPy timedelta64.
        
                .. versionadded:: 0.25.0
        
                This is an alias method for `Timedelta.to_timedelta64()`. The dtype and
                copy parameters are available here only for compatibility. Their values
                will not affect the return value.
        
                Returns
                -------
                numpy.timedelta64
        
                See Also
                --------
                Series.to_numpy : Similar method for Series.
        """
        pass

    def to_pytimedelta(self): # real signature unknown; restored from __doc__
        """
        Convert a pandas Timedelta object into a python timedelta object.
        
                Timedelta objects are internally saved as numpy datetime64[ns] dtype.
                Use to_pytimedelta() to convert to object dtype.
        
                Returns
                -------
                datetime.timedelta or numpy.array of datetime.timedelta
        
                See Also
                --------
                to_timedelta : Convert argument to Timedelta type.
        
                Notes
                -----
                Any nanosecond resolution will be lost.
        """
        pass

    def to_timedelta64(self, *args, **kwargs): # real signature unknown
        """ Return a numpy.timedelta64 object with 'ns' precision. """
        pass

    def view(self, *args, **kwargs): # real signature unknown
        """ Array view compatibility. """
        pass

    def _ensure_components(self, *args, **kwargs): # real signature unknown
        """ compute the components """
        pass

    def _has_ns(self, *args, **kwargs): # real signature unknown
        pass

    def _repr_base(self, *args, **kwargs): # real signature unknown
        """
        Parameters
                ----------
                format : None|all|sub_day|long
        
                Returns
                -------
                converted : string of a Timedelta
        """
        pass

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

    def __reduce_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    asm8 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return a numpy timedelta64 array scalar view.

        Provides access to the array scalar view (i.e. a combination of the
        value and the units) associated with the numpy.timedelta64().view(),
        including a 64-bit integer representation of the timedelta in
        nanoseconds (Python int compatible).

        Returns
        -------
        numpy timedelta64 array scalar view
            Array scalar view of the timedelta in nanoseconds.

        Examples
        --------
        >>> td = pd.Timedelta('1 days 2 min 3 us 42 ns')
        >>> td.asm8
        numpy.timedelta64(86520000003042,'ns')

        >>> td = pd.Timedelta('2 min 3 s')
        >>> td.asm8
        numpy.timedelta64(123000000000,'ns')

        >>> td = pd.Timedelta('3 ms 5 us')
        >>> td.asm8
        numpy.timedelta64(3005000,'ns')

        >>> td = pd.Timedelta(42, unit='ns')
        >>> td.asm8
        numpy.timedelta64(42,'ns')
        """

    components = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return a components namedtuple-like.
        """

    delta = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the timedelta in nanoseconds (ns), for internal compatibility.

        Returns
        -------
        int
            Timedelta in nanoseconds.

        Examples
        --------
        >>> td = pd.Timedelta('1 days 42 ns')
        >>> td.delta
        86400000000042

        >>> td = pd.Timedelta('3 s')
        >>> td.delta
        3000000000

        >>> td = pd.Timedelta('3 ms 5 us')
        >>> td.delta
        3005000

        >>> td = pd.Timedelta(42, unit='ns')
        >>> td.delta
        42
        """

    freq = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_populated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nanoseconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the number of nanoseconds (n), where 0 <= n < 1 microsecond.

        Returns
        -------
        int
            Number of nanoseconds.

        See Also
        --------
        Timedelta.components : Return all attributes with assigned values
            (i.e. days, hours, minutes, seconds, milliseconds, microseconds,
            nanoseconds).

        Examples
        --------
        **Using string input**

        >>> td = pd.Timedelta('1 days 2 min 3 us 42 ns')
        >>> td.nanoseconds
        42

        **Using integer input**

        >>> td = pd.Timedelta(42, unit='ns')
        >>> td.nanoseconds
        42
        """

    resolution_string = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return a string representing the lowest timedelta resolution.

        Each timedelta has a defined resolution that represents the lowest OR
        most granular level of precision. Each level of resolution is
        represented by a short string as defined below:

        Resolution:     Return value

        * Days:         'D'
        * Hours:        'H'
        * Minutes:      'T'
        * Seconds:      'S'
        * Milliseconds: 'L'
        * Microseconds: 'U'
        * Nanoseconds:  'N'

        Returns
        -------
        str
            Timedelta resolution.

        Examples
        --------
        >>> td = pd.Timedelta('1 days 2 min 3 us 42 ns')
        >>> td.resolution
        'N'

        >>> td = pd.Timedelta('1 days 2 min 3 us')
        >>> td.resolution
        'U'

        >>> td = pd.Timedelta('2 min 3 s')
        >>> td.resolution
        'S'

        >>> td = pd.Timedelta(36, unit='us')
        >>> td.resolution
        'U'
        """

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _d = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _h = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _m = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _ms = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _ns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _s = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _us = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __array_priority__ = 100
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001A337CB9A80>'


class Timedelta(_Timedelta):
    """
    Represents a duration, the difference between two dates or times.
    
        Timedelta is the pandas equivalent of python's ``datetime.timedelta``
        and is interchangeable with it in most cases.
    
        Parameters
        ----------
        value : Timedelta, timedelta, np.timedelta64, string, or integer
        unit : str, default 'ns'
            Denote the unit of the input, if input is an integer.
    
            Possible values:
    
            * 'Y', 'M', 'W', 'D', 'T', 'S', 'L', 'U', or 'N'
            * 'days' or 'day'
            * 'hours', 'hour', 'hr', or 'h'
            * 'minutes', 'minute', 'min', or 'm'
            * 'seconds', 'second', or 'sec'
            * 'milliseconds', 'millisecond', 'millis', or 'milli'
            * 'microseconds', 'microsecond', 'micros', or 'micro'
            * 'nanoseconds', 'nanosecond', 'nanos', 'nano', or 'ns'.
    
        **kwargs
            Available kwargs: {days, seconds, microseconds,
            milliseconds, minutes, hours, weeks}.
            Values for construction in compat with datetime.timedelta.
            Numpy ints and floats will be coerced to python ints and floats.
    
        Notes
        -----
        The ``.value`` attribute is always in ns.
    """
    def ceil(self, *args, **kwargs): # real signature unknown
        """
        Return a new Timedelta ceiled to this resolution.
        
                Parameters
                ----------
                freq : str
                    Frequency string indicating the ceiling resolution.
        """
        pass

    def floor(self, *args, **kwargs): # real signature unknown
        """
        Return a new Timedelta floored to this resolution.
        
                Parameters
                ----------
                freq : str
                    Frequency string indicating the flooring resolution.
        """
        pass

    def round(self, *args, **kwargs): # real signature unknown
        """
        Round the Timedelta to the specified resolution.
        
                Parameters
                ----------
                freq : str
                    Frequency string indicating the rounding resolution.
        
                Returns
                -------
                a new Timedelta rounded to the given resolution of `freq`
        
                Raises
                ------
                ValueError if the freq cannot be converted
        """
        pass

    def _round(self, *args, **kwargs): # real signature unknown
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __inv__(self, *args, **kwargs): # real signature unknown
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    max = Timedelta('106751 days 23:47:16.854775')
    min = Timedelta('-106752 days +00:12:43.145224')
    resolution = Timedelta('0 days 00:00:00.000000')
    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pandas._libs.tslibs.timedeltas\', \'__doc__\': "\\n    Represents a duration, the difference between two dates or times.\\n\\n    Timedelta is the pandas equivalent of python\'s ``datetime.timedelta``\\n    and is interchangeable with it in most cases.\\n\\n    Parameters\\n    ----------\\n    value : Timedelta, timedelta, np.timedelta64, string, or integer\\n    unit : str, default \'ns\'\\n        Denote the unit of the input, if input is an integer.\\n\\n        Possible values:\\n\\n        * \'Y\', \'M\', \'W\', \'D\', \'T\', \'S\', \'L\', \'U\', or \'N\'\\n        * \'days\' or \'day\'\\n        * \'hours\', \'hour\', \'hr\', or \'h\'\\n        * \'minutes\', \'minute\', \'min\', or \'m\'\\n        * \'seconds\', \'second\', or \'sec\'\\n        * \'milliseconds\', \'millisecond\', \'millis\', or \'milli\'\\n        * \'microseconds\', \'microsecond\', \'micros\', or \'micro\'\\n        * \'nanoseconds\', \'nanosecond\', \'nanos\', \'nano\', or \'ns\'.\\n\\n    **kwargs\\n        Available kwargs: {days, seconds, microseconds,\\n        milliseconds, minutes, hours, weeks}.\\n        Values for construction in compat with datetime.timedelta.\\n        Numpy ints and floats will be coerced to python ints and floats.\\n\\n    Notes\\n    -----\\n    The ``.value`` attribute is always in ns.\\n    ", \'__new__\': <cyfunction Timedelta.__new__ at 0x000001A337DA2270>, \'__setstate__\': <cyfunction Timedelta.__setstate__ at 0x000001A337DA2328>, \'__reduce__\': <cyfunction Timedelta.__reduce__ at 0x000001A337DA23E0>, \'_round\': <cyfunction Timedelta._round at 0x000001A337DA2498>, \'round\': <cyfunction Timedelta.round at 0x000001A337DA2550>, \'floor\': <cyfunction Timedelta.floor at 0x000001A337DA2608>, \'ceil\': <cyfunction Timedelta.ceil at 0x000001A337DA26C0>, \'__inv__\': <cyfunction _op_unary_method.<locals>.f at 0x000001A337DA2830>, \'__neg__\': <cyfunction _op_unary_method.<locals>.f at 0x000001A337DA29A0>, \'__pos__\': <cyfunction _op_unary_method.<locals>.f at 0x000001A337DA2B10>, \'__abs__\': <cyfunction _op_unary_method.<locals>.f at 0x000001A337DA2C80>, \'__add__\': <cyfunction _binary_op_method_timedeltalike.<locals>.f at 0x000001A337DA2DF0>, \'__radd__\': <cyfunction _binary_op_method_timedeltalike.<locals>.f at 0x000001A337DA2F60>, \'__sub__\': <cyfunction _binary_op_method_timedeltalike.<locals>.f at 0x000001A337DA5100>, \'__rsub__\': <cyfunction _binary_op_method_timedeltalike.<locals>.f at 0x000001A337DA5270>, \'__mul__\': <cyfunction Timedelta.__mul__ at 0x000001A337DA5328>, \'__rmul__\': <cyfunction Timedelta.__mul__ at 0x000001A337DA5328>, \'__truediv__\': <cyfunction Timedelta.__truediv__ at 0x000001A337DA53E0>, \'__rtruediv__\': <cyfunction Timedelta.__rtruediv__ at 0x000001A337DA5498>, \'__floordiv__\': <cyfunction Timedelta.__floordiv__ at 0x000001A337DA5550>, \'__rfloordiv__\': <cyfunction Timedelta.__rfloordiv__ at 0x000001A337DA5608>, \'__mod__\': <cyfunction Timedelta.__mod__ at 0x000001A337DA56C0>, \'__rmod__\': <cyfunction Timedelta.__rmod__ at 0x000001A337DA5778>, \'__divmod__\': <cyfunction Timedelta.__divmod__ at 0x000001A337DA5830>, \'__rdivmod__\': <cyfunction Timedelta.__rdivmod__ at 0x000001A337DA58E8>, \'__dict__\': <attribute \'__dict__\' of \'Timedelta\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'Timedelta\' objects>, \'min\': Timedelta(\'-106752 days +00:12:43.145224\'), \'max\': Timedelta(\'106751 days 23:47:16.854775\'), \'resolution\': Timedelta(\'0 days 00:00:00.000000\')})'


# variables with complex values

nat_strings = None # (!) real value is "{'nat', 'NAN', 'NAT', 'NaT', 'NaN', 'nan'}"

_no_input = None # (!) real value is '<object object at 0x000001A326D9E6C0>'

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001A337E0DA58>'

__pyx_capi__ = {
    'cast_from_unit': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (PyObject *, PyObject *)" at 0x000001A337CB99C0>'
    'convert_to_timedelta64': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyObject *)" at 0x000001A337CB9A50>'
    'delta_to_nanoseconds': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (PyObject *, int __pyx_skip_dispatch)" at 0x000001A337CB9A20>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.tslibs.timedeltas', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001A337E0DA58>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\pandas\\\\_libs\\\\tslibs\\\\timedeltas.cp37-win_amd64.pyd')"

__test__ = {
    '_Timedelta.asm8.__get__ (line 915)': "\n        Return a numpy timedelta64 array scalar view.\n\n        Provides access to the array scalar view (i.e. a combination of the\n        value and the units) associated with the numpy.timedelta64().view(),\n        including a 64-bit integer representation of the timedelta in\n        nanoseconds (Python int compatible).\n\n        Returns\n        -------\n        numpy timedelta64 array scalar view\n            Array scalar view of the timedelta in nanoseconds.\n\n        Examples\n        --------\n        >>> td = pd.Timedelta('1 days 2 min 3 us 42 ns')\n        >>> td.asm8\n        numpy.timedelta64(86520000003042,'ns')\n\n        >>> td = pd.Timedelta('2 min 3 s')\n        >>> td.asm8\n        numpy.timedelta64(123000000000,'ns')\n\n        >>> td = pd.Timedelta('3 ms 5 us')\n        >>> td.asm8\n        numpy.timedelta64(3005000,'ns')\n\n        >>> td = pd.Timedelta(42, unit='ns')\n        >>> td.asm8\n        numpy.timedelta64(42,'ns')\n        ",
    '_Timedelta.delta.__get__ (line 885)': "\n        Return the timedelta in nanoseconds (ns), for internal compatibility.\n\n        Returns\n        -------\n        int\n            Timedelta in nanoseconds.\n\n        Examples\n        --------\n        >>> td = pd.Timedelta('1 days 42 ns')\n        >>> td.delta\n        86400000000042\n\n        >>> td = pd.Timedelta('3 s')\n        >>> td.delta\n        3000000000\n\n        >>> td = pd.Timedelta('3 ms 5 us')\n        >>> td.delta\n        3005000\n\n        >>> td = pd.Timedelta(42, unit='ns')\n        >>> td.delta\n        42\n        ",
    '_Timedelta.isoformat (line 1097)': "\n        Format Timedelta as ISO 8601 Duration like\n        ``P[n]Y[n]M[n]DT[n]H[n]M[n]S``, where the ``[n]`` s are replaced by the\n        values. See https://en.wikipedia.org/wiki/ISO_8601#Durations.\n\n        Returns\n        -------\n        formatted : str\n\n        See Also\n        --------\n        Timestamp.isoformat\n\n        Notes\n        -----\n        The longest component is days, whose value may be larger than\n        365.\n        Every component is always included, even if its value is 0.\n        Pandas uses nanosecond precision, so up to 9 decimal places may\n        be included in the seconds component.\n        Trailing 0's are removed from the seconds component after the decimal.\n        We do not 0 pad components, so it's `...T5H...`, not `...T05H...`\n\n        Examples\n        --------\n        >>> td = pd.Timedelta(days=6, minutes=50, seconds=3,\n        ...                   milliseconds=10, microseconds=10, nanoseconds=12)\n        >>> td.isoformat()\n        'P6DT0H50M3.010010012S'\n        >>> pd.Timedelta(hours=1, seconds=10).isoformat()\n        'P0DT0H0M10S'\n        >>> pd.Timedelta(hours=1, seconds=10).isoformat()\n        'P0DT0H0M10S'\n        >>> pd.Timedelta(days=500.5).isoformat()\n        'P500DT12H0MS'\n        ",
    '_Timedelta.nanoseconds.__get__ (line 1008)': "\n        Return the number of nanoseconds (n), where 0 <= n < 1 microsecond.\n\n        Returns\n        -------\n        int\n            Number of nanoseconds.\n\n        See Also\n        --------\n        Timedelta.components : Return all attributes with assigned values\n            (i.e. days, hours, minutes, seconds, milliseconds, microseconds,\n            nanoseconds).\n\n        Examples\n        --------\n        **Using string input**\n\n        >>> td = pd.Timedelta('1 days 2 min 3 us 42 ns')\n        >>> td.nanoseconds\n        42\n\n        **Using integer input**\n\n        >>> td = pd.Timedelta(42, unit='ns')\n        >>> td.nanoseconds\n        42\n        ",
    '_Timedelta.resolution_string.__get__ (line 950)': "\n        Return a string representing the lowest timedelta resolution.\n\n        Each timedelta has a defined resolution that represents the lowest OR\n        most granular level of precision. Each level of resolution is\n        represented by a short string as defined below:\n\n        Resolution:     Return value\n\n        * Days:         'D'\n        * Hours:        'H'\n        * Minutes:      'T'\n        * Seconds:      'S'\n        * Milliseconds: 'L'\n        * Microseconds: 'U'\n        * Nanoseconds:  'N'\n\n        Returns\n        -------\n        str\n            Timedelta resolution.\n\n        Examples\n        --------\n        >>> td = pd.Timedelta('1 days 2 min 3 us 42 ns')\n        >>> td.resolution\n        'N'\n\n        >>> td = pd.Timedelta('1 days 2 min 3 us')\n        >>> td.resolution\n        'U'\n\n        >>> td = pd.Timedelta('2 min 3 s')\n        >>> td.resolution\n        'S'\n\n        >>> td = pd.Timedelta(36, unit='us')\n        >>> td.resolution\n        'U'\n        ",
}

