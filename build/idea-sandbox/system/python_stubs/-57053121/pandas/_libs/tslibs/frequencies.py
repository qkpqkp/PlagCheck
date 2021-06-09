# encoding: utf-8
# module pandas._libs.tslibs.frequencies
# from C:\Users\Doly\Anaconda3\lib\site-packages\pandas\_libs\tslibs\frequencies.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import re as re # C:\Users\Doly\Anaconda3\lib\re.py

# Variables with simple values

INVALID_FREQ_ERR_MSG = 'Invalid frequency: {0}'

# functions

def get_base_alias(*args, **kwargs): # real signature unknown
    """
    Returns the base frequency alias, e.g., '5D' -> 'D'
    
        Parameters
        ----------
        freqstr : str
    
        Returns
        -------
        base_alias : str
    """
    pass

def get_freq(A): # real signature unknown; restored from __doc__
    """
    Return frequency code of given frequency str.
        If input is not string, return input as it is.
    
        Examples
        --------
        >>> get_freq('A')
        1000
    
        >>> get_freq('3A')
        1000
    """
    pass

def get_freq_code(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Return freq str or tuple to freq code and stride (mult)
    
        Parameters
        ----------
        freqstr : str or tuple
    
        Returns
        -------
        return : tuple of base frequency code and stride (mult)
    
        Raises
        ------
        TypeError : if passed a tuple witth incorrect types
    
        Examples
        --------
        >>> get_freq_code('3D')
        (6000, 3)
    
        >>> get_freq_code('D')
        (6000, 1)
    
        >>> get_freq_code(('D', 3))
        (6000, 3)
    """
    pass

def get_freq_str(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Return the summary string associated with this offset code, possibly
        adjusted by a multiplier.
    
        Parameters
        ----------
        base : int (member of FreqGroup)
    
        Returns
        -------
        freq_str : str
    
        Examples
        --------
        >>> get_freq_str(1000)
        'A-DEC'
    
        >>> get_freq_str(2000, 2)
        '2Q-DEC'
    
        >>> get_freq_str("foo")
    """
    pass

def get_rule_month(D): # real signature unknown; restored from __doc__
    """
    Return starting month of given freq, default is December.
    
        Parameters
        ----------
        source : object
        default : str, default "DEC"
    
        Returns
        -------
        rule_month: str
    
        Examples
        --------
        >>> get_rule_month('D')
        'DEC'
    
        >>> get_rule_month('A-JAN')
        'JAN'
    """
    pass

def get_to_timestamp_base(get_freq_code, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Return frequency code group used for base of to_timestamp against
        frequency code.
    
        Parameters
        ----------
        base : int (member of FreqGroup)
    
        Returns
        -------
        base : int
    
        Examples
        --------
        # Return day freq code against longer freq than day
        >>> get_to_timestamp_base(get_freq_code('D')[0])
        6000
        >>> get_to_timestamp_base(get_freq_code('W')[0])
        6000
        >>> get_to_timestamp_base(get_freq_code('M')[0])
        6000
    
        # Return second freq code against hour between second
        >>> get_to_timestamp_base(get_freq_code('H')[0])
        9000
        >>> get_to_timestamp_base(get_freq_code('S')[0])
        9000
    """
    pass

def is_subperiod(*args, **kwargs): # real signature unknown
    """
    Returns True if downsampling is possible between source and target
        frequencies
    
        Parameters
        ----------
        source : string or DateOffset
            Frequency converting from
        target : string or DateOffset
            Frequency converting to
    
        Returns
        -------
        is_subperiod : boolean
    """
    pass

def is_superperiod(*args, **kwargs): # real signature unknown
    """
    Returns True if upsampling is possible between source and target
        frequencies
    
        Parameters
        ----------
        source : string
            Frequency converting from
        target : string
            Frequency converting to
    
        Returns
        -------
        is_superperiod : boolean
    """
    pass

def _base_and_stride(*args, **kwargs): # real signature unknown
    """
    Return base freq and stride info from string representation
    
        Returns
        -------
        base : str
        stride : int
    
        Examples
        --------
        _freq_and_stride('5Min') -> 'Min', 5
    """
    pass

def _period_str_to_code(*args, **kwargs): # real signature unknown
    pass

# classes

class FreqGroup(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    FR_ANN = 1000
    FR_BUS = 5000
    FR_DAY = 6000
    FR_HR = 7000
    FR_MIN = 8000
    FR_MS = 10000
    FR_MTH = 3000
    FR_NS = 12000
    FR_QTR = 2000
    FR_SEC = 9000
    FR_US = 11000
    FR_WK = 4000
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'pandas._libs.tslibs.frequencies', 'FR_ANN': 1000, 'FR_QTR': 2000, 'FR_MTH': 3000, 'FR_WK': 4000, 'FR_BUS': 5000, 'FR_DAY': 6000, 'FR_HR': 7000, 'FR_MIN': 8000, 'FR_SEC': 9000, 'FR_MS': 10000, 'FR_US': 11000, 'FR_NS': 12000, '__dict__': <attribute '__dict__' of 'FreqGroup' objects>, '__weakref__': <attribute '__weakref__' of 'FreqGroup' objects>, '__doc__': None})"


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

opattern = None # (!) real value is "re.compile('([+\\\\-]?\\\\d*|[+\\\\-]?\\\\d*\\\\.\\\\d*)\\\\s*([A-Za-z]+([\\\\-][\\\\dA-Za-z\\\\-]+)?)')"

_dont_uppercase = None # (!) real value is "{'ms', 'MS'}"

_lite_rule_alias = {
    'A': 'A-DEC',
    'AS': 'AS-JAN',
    'BA': 'BA-DEC',
    'BAS': 'BAS-JAN',
    'BY': 'BA-DEC',
    'BYS': 'BAS-JAN',
    'Min': 'T',
    'Q': 'Q-DEC',
    'W': 'W-SUN',
    'Y': 'A-DEC',
    'YS': 'AS-JAN',
    'min': 'T',
    'ms': 'L',
    'ns': 'N',
    'us': 'U',
}

_period_code_map = {
    'A': 1000,
    'A-APR': 1004,
    'A-AUG': 1008,
    'A-DEC': 1000,
    'A-FEB': 1002,
    'A-JAN': 1001,
    'A-JUL': 1007,
    'A-JUN': 1006,
    'A-MAR': 1003,
    'A-MAY': 1005,
    'A-NOV': 1011,
    'A-OCT': 1010,
    'A-SEP': 1009,
    'B': 5000,
    'C': 5000,
    'D': 6000,
    'H': 7000,
    'L': 10000,
    'M': 3000,
    'N': 12000,
    'Q': 2000,
    'Q-APR': 2004,
    'Q-AUG': 2008,
    'Q-DEC': 2000,
    'Q-FEB': 2002,
    'Q-JAN': 2001,
    'Q-JUL': 2007,
    'Q-JUN': 2006,
    'Q-MAR': 2003,
    'Q-MAY': 2005,
    'Q-NOV': 2011,
    'Q-OCT': 2010,
    'Q-SEP': 2009,
    'S': 9000,
    'T': 8000,
    'U': 11000,
    'W': 4000,
    'W-FRI': 4005,
    'W-MON': 4001,
    'W-SAT': 4006,
    'W-SUN': 4000,
    'W-THU': 4004,
    'W-TUE': 4002,
    'W-WED': 4003,
    'Y-APR': 1004,
    'Y-AUG': 1008,
    'Y-DEC': 1000,
    'Y-FEB': 1002,
    'Y-JAN': 1001,
    'Y-JUL': 1007,
    'Y-JUN': 1006,
    'Y-MAR': 1003,
    'Y-MAY': 1005,
    'Y-NOV': 1011,
    'Y-OCT': 1010,
    'Y-SEP': 1009,
}

_reverse_period_code_map = {
    1000: 'A-DEC',
    1001: 'A-JAN',
    1002: 'A-FEB',
    1003: 'A-MAR',
    1004: 'A-APR',
    1005: 'A-MAY',
    1006: 'A-JUN',
    1007: 'A-JUL',
    1008: 'A-AUG',
    1009: 'A-SEP',
    1010: 'A-OCT',
    1011: 'A-NOV',
    2000: 'Q-DEC',
    2001: 'Q-JAN',
    2002: 'Q-FEB',
    2003: 'Q-MAR',
    2004: 'Q-APR',
    2005: 'Q-MAY',
    2006: 'Q-JUN',
    2007: 'Q-JUL',
    2008: 'Q-AUG',
    2009: 'Q-SEP',
    2010: 'Q-OCT',
    2011: 'Q-NOV',
    3000: 'M',
    4000: 'W-SUN',
    4001: 'W-MON',
    4002: 'W-TUE',
    4003: 'W-WED',
    4004: 'W-THU',
    4005: 'W-FRI',
    4006: 'W-SAT',
    5000: 'B',
    6000: 'D',
    7000: 'H',
    8000: 'T',
    9000: 'S',
    10000: 'L',
    11000: 'U',
    12000: 'N',
}

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000002EDF340D5F8>'

__pyx_capi__ = {
    'get_base_alias': None, # (!) real value is '<capsule object "PyObject *(PyObject *, int __pyx_skip_dispatch)" at 0x000002EDF340A390>'
    'get_freq': None, # (!) real value is '<capsule object "PyObject *(PyObject *, int __pyx_skip_dispatch)" at 0x000002EDF340A360>'
    'get_freq_code': None, # (!) real value is '<capsule object "PyObject *(PyObject *, int __pyx_skip_dispatch)" at 0x000002EDF340A330>'
    'get_freq_str': None, # (!) real value is '<capsule object "PyObject *(PyObject *, int __pyx_skip_dispatch, struct __pyx_opt_args_6pandas_5_libs_6tslibs_11frequencies_get_freq_str *__pyx_optional_args)" at 0x000002EDF340A3F0>'
    'get_rule_month': None, # (!) real value is '<capsule object "PyObject *(PyObject *, int __pyx_skip_dispatch, struct __pyx_opt_args_6pandas_5_libs_6tslibs_11frequencies_get_rule_month *__pyx_optional_args)" at 0x000002EDF340A300>'
    'get_to_timestamp_base': None, # (!) real value is '<capsule object "int (int, int __pyx_skip_dispatch)" at 0x000002EDF340A3C0>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.tslibs.frequencies', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000002EDF340D5F8>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\pandas\\\\_libs\\\\tslibs\\\\frequencies.cp37-win_amd64.pyd')"

__test__ = {
    'get_freq (line 309)': "\n    Return frequency code of given frequency str.\n    If input is not string, return input as it is.\n\n    Examples\n    --------\n    >>> get_freq('A')\n    1000\n\n    >>> get_freq('3A')\n    1000\n    ",
    'get_freq_code (line 129)': "\n    Return freq str or tuple to freq code and stride (mult)\n\n    Parameters\n    ----------\n    freqstr : str or tuple\n\n    Returns\n    -------\n    return : tuple of base frequency code and stride (mult)\n\n    Raises\n    ------\n    TypeError : if passed a tuple witth incorrect types\n\n    Examples\n    --------\n    >>> get_freq_code('3D')\n    (6000, 3)\n\n    >>> get_freq_code('D')\n    (6000, 1)\n\n    >>> get_freq_code(('D', 3))\n    (6000, 3)\n    ",
    'get_freq_str (line 229)': '\n    Return the summary string associated with this offset code, possibly\n    adjusted by a multiplier.\n\n    Parameters\n    ----------\n    base : int (member of FreqGroup)\n\n    Returns\n    -------\n    freq_str : str\n\n    Examples\n    --------\n    >>> get_freq_str(1000)\n    \'A-DEC\'\n\n    >>> get_freq_str(2000, 2)\n    \'2Q-DEC\'\n\n    >>> get_freq_str("foo")\n    ',
    'get_rule_month (line 488)': '\n    Return starting month of given freq, default is December.\n\n    Parameters\n    ----------\n    source : object\n    default : str, default "DEC"\n\n    Returns\n    -------\n    rule_month: str\n\n    Examples\n    --------\n    >>> get_rule_month(\'D\')\n    \'DEC\'\n\n    >>> get_rule_month(\'A-JAN\')\n    \'JAN\'\n    ',
    'get_to_timestamp_base (line 273)': "\n    Return frequency code group used for base of to_timestamp against\n    frequency code.\n\n    Parameters\n    ----------\n    base : int (member of FreqGroup)\n\n    Returns\n    -------\n    base : int\n\n    Examples\n    --------\n    # Return day freq code against longer freq than day\n    >>> get_to_timestamp_base(get_freq_code('D')[0])\n    6000\n    >>> get_to_timestamp_base(get_freq_code('W')[0])\n    6000\n    >>> get_to_timestamp_base(get_freq_code('M')[0])\n    6000\n\n    # Return second freq code against hour between second\n    >>> get_to_timestamp_base(get_freq_code('H')[0])\n    9000\n    >>> get_to_timestamp_base(get_freq_code('S')[0])\n    9000\n    ",
}

