# encoding: utf-8
# module pandas._libs.tslibs.parsing
# from C:\Users\Doly\Anaconda3\lib\site-packages\pandas\_libs\tslibs\parsing.cp37-win_amd64.pyd
# by generator 1.147
""" Parsing functions for datetime and datetime-like strings. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import re as re # C:\Users\Doly\Anaconda3\lib\re.py
import time as time # <module 'time' (built-in)>
import numpy as np # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py
from pandas._libs.tslibs.nattype import NaT

import datetime as __datetime
import dateutil.tz.tz as __dateutil_tz_tz
import dateutil.tz._common as __dateutil_tz__common


# functions

def du_parse(timestr, parserinfo=None, **kwargs): # reliably restored by inspect
    """
    Parse a string in one of the supported formats, using the
        ``parserinfo`` parameters.
    
        :param timestr:
            A string containing a date/time stamp.
    
        :param parserinfo:
            A :class:`parserinfo` object containing parameters for the parser.
            If ``None``, the default arguments to the :class:`parserinfo`
            constructor are used.
    
        The ``**kwargs`` parameter takes the following keyword arguments:
    
        :param default:
            The default datetime object, if this is a datetime object and not
            ``None``, elements specified in ``timestr`` replace elements in the
            default object.
    
        :param ignoretz:
            If set ``True``, time zones in parsed strings are ignored and a naive
            :class:`datetime` object is returned.
    
        :param tzinfos:
            Additional time zone names / aliases which may be present in the
            string. This argument maps time zone names (and optionally offsets
            from those time zones) to time zones. This parameter can be a
            dictionary with timezone aliases mapping time zone names to time
            zones or a function taking two parameters (``tzname`` and
            ``tzoffset``) and returning a time zone.
    
            The timezones to which the names are mapped can be an integer
            offset from UTC in seconds or a :class:`tzinfo` object.
    
            .. doctest::
               :options: +NORMALIZE_WHITESPACE
    
                >>> from dateutil.parser import parse
                >>> from dateutil.tz import gettz
                >>> tzinfos = {"BRST": -7200, "CST": gettz("America/Chicago")}
                >>> parse("2012-01-19 17:21:00 BRST", tzinfos=tzinfos)
                datetime.datetime(2012, 1, 19, 17, 21, tzinfo=tzoffset(u'BRST', -7200))
                >>> parse("2012-01-19 17:21:00 CST", tzinfos=tzinfos)
                datetime.datetime(2012, 1, 19, 17, 21,
                                  tzinfo=tzfile('/usr/share/zoneinfo/America/Chicago'))
    
            This parameter is ignored if ``ignoretz`` is set.
    
        :param dayfirst:
            Whether to interpret the first value in an ambiguous 3-integer date
            (e.g. 01/05/09) as the day (``True``) or month (``False``). If
            ``yearfirst`` is set to ``True``, this distinguishes between YDM and
            YMD. If set to ``None``, this value is retrieved from the current
            :class:`parserinfo` object (which itself defaults to ``False``).
    
        :param yearfirst:
            Whether to interpret the first value in an ambiguous 3-integer date
            (e.g. 01/05/09) as the year. If ``True``, the first number is taken to
            be the year, otherwise the last number is taken to be the year. If
            this is set to ``None``, the value is retrieved from the current
            :class:`parserinfo` object (which itself defaults to ``False``).
    
        :param fuzzy:
            Whether to allow fuzzy parsing, allowing for string like "Today is
            January 1, 2047 at 8:21:00AM".
    
        :param fuzzy_with_tokens:
            If ``True``, ``fuzzy`` is automatically set to True, and the parser
            will return a tuple where the first element is the parsed
            :class:`datetime.datetime` datetimestamp and the second element is
            a tuple containing the portions of the string which were ignored:
    
            .. doctest::
    
                >>> from dateutil.parser import parse
                >>> parse("Today is January 1, 2047 at 8:21:00AM", fuzzy_with_tokens=True)
                (datetime.datetime(2047, 1, 1, 8, 21), (u'Today is ', u' ', u'at '))
    
        :return:
            Returns a :class:`datetime.datetime` object or, if the
            ``fuzzy_with_tokens`` option is ``True``, returns a tuple, the
            first element being a :class:`datetime.datetime` object, the second
            a tuple containing the fuzzy tokens.
    
        :raises ValueError:
            Raised for invalid or unknown string format, if the provided
            :class:`tzinfo` is not in a valid format, or if an invalid date
            would be created.
    
        :raises OverflowError:
            Raised if the parsed date exceeds the largest valid C integer on
            your system.
    """
    pass

def get_option(pat): # real signature unknown; restored from __doc__
    """
    get_option(pat)
    
    Retrieves the value of the specified option.
    
    Available options:
    
    - compute.[use_bottleneck, use_numexpr]
    - display.[chop_threshold, colheader_justify, column_space, date_dayfirst,
      date_yearfirst, encoding, expand_frame_repr, float_format]
    - display.html.[border, table_schema, use_mathjax]
    - display.[large_repr]
    - display.latex.[escape, longtable, multicolumn, multicolumn_format, multirow,
      repr]
    - display.[max_categories, max_columns, max_colwidth, max_info_columns,
      max_info_rows, max_rows, max_seq_items, memory_usage, min_rows, multi_sparse,
      notebook_repr_html, pprint_nest_depth, precision, show_dimensions]
    - display.unicode.[ambiguous_as_wide, east_asian_width]
    - display.[width]
    - io.excel.ods.[reader]
    - io.excel.xls.[reader, writer]
    - io.excel.xlsb.[reader]
    - io.excel.xlsm.[reader, writer]
    - io.excel.xlsx.[reader, writer]
    - io.hdf.[default_format, dropna_table]
    - io.parquet.[engine]
    - mode.[chained_assignment, sim_interactive, use_inf_as_na, use_inf_as_null]
    - plotting.[backend]
    - plotting.matplotlib.[register_converters]
    
    Parameters
    ----------
    pat : str
        Regexp which should match a single option.
        Note: partial matches are supported for convenience, but unless you use the
        full option name (e.g. x.y.z.option_name), your code may break in future
        versions if new options with similar names are introduced.
    
    Returns
    -------
    result : the value of the option
    
    Raises
    ------
    OptionError : if no such option exists
    
    Notes
    -----
    The available options with its descriptions:
    
    compute.use_bottleneck : bool
        Use the bottleneck library to accelerate if it is installed,
        the default is True
        Valid values: False,True
        [default: True] [currently: True]
    compute.use_numexpr : bool
        Use the numexpr library to accelerate computation if it is installed,
        the default is True
        Valid values: False,True
        [default: True] [currently: True]
    display.chop_threshold : float or None
        if set to a float value, all float values smaller then the given threshold
        will be displayed as exactly 0 by repr and friends.
        [default: None] [currently: None]
    display.colheader_justify : 'left'/'right'
        Controls the justification of column headers. used by DataFrameFormatter.
        [default: right] [currently: right]
    display.column_space No description available.
        [default: 12] [currently: 12]
    display.date_dayfirst : boolean
        When True, prints and parses dates with the day first, eg 20/01/2005
        [default: False] [currently: False]
    display.date_yearfirst : boolean
        When True, prints and parses dates with the year first, eg 2005/01/20
        [default: False] [currently: False]
    display.encoding : str/unicode
        Defaults to the detected encoding of the console.
        Specifies the encoding to be used for strings returned by to_string,
        these are generally strings meant to be displayed on the console.
        [default: cp936] [currently: cp936]
    display.expand_frame_repr : boolean
        Whether to print out the full DataFrame repr for wide DataFrames across
        multiple lines, `max_columns` is still respected, but the output will
        wrap-around across multiple "pages" if its width exceeds `display.width`.
        [default: True] [currently: True]
    display.float_format : callable
        The callable should accept a floating point number and return
        a string with the desired format of the number. This is used
        in some places like SeriesFormatter.
        See formats.format.EngFormatter for an example.
        [default: None] [currently: None]
    display.html.border : int
        A ``border=value`` attribute is inserted in the ``<table>`` tag
        for the DataFrame HTML repr.
        [default: 1] [currently: 1]
    display.html.table_schema : boolean
        Whether to publish a Table Schema representation for frontends
        that support it.
        (default: False)
        [default: False] [currently: False]
    display.html.use_mathjax : boolean
        When True, Jupyter notebook will process table contents using MathJax,
        rendering mathematical expressions enclosed by the dollar symbol.
        (default: True)
        [default: True] [currently: True]
    display.large_repr : 'truncate'/'info'
        For DataFrames exceeding max_rows/max_cols, the repr (and HTML repr) can
        show a truncated table (the default from 0.13), or switch to the view from
        df.info() (the behaviour in earlier versions of pandas).
        [default: truncate] [currently: truncate]
    display.latex.escape : bool
        This specifies if the to_latex method of a Dataframe uses escapes special
        characters.
        Valid values: False,True
        [default: True] [currently: True]
    display.latex.longtable :bool
        This specifies if the to_latex method of a Dataframe uses the longtable
        format.
        Valid values: False,True
        [default: False] [currently: False]
    display.latex.multicolumn : bool
        This specifies if the to_latex method of a Dataframe uses multicolumns
        to pretty-print MultiIndex columns.
        Valid values: False,True
        [default: True] [currently: True]
    display.latex.multicolumn_format : bool
        This specifies if the to_latex method of a Dataframe uses multicolumns
        to pretty-print MultiIndex columns.
        Valid values: False,True
        [default: l] [currently: l]
    display.latex.multirow : bool
        This specifies if the to_latex method of a Dataframe uses multirows
        to pretty-print MultiIndex rows.
        Valid values: False,True
        [default: False] [currently: False]
    display.latex.repr : boolean
        Whether to produce a latex DataFrame representation for jupyter
        environments that support it.
        (default: False)
        [default: False] [currently: False]
    display.max_categories : int
        This sets the maximum number of categories pandas should output when
        printing out a `Categorical` or a Series of dtype "category".
        [default: 8] [currently: 8]
    display.max_columns : int
        If max_cols is exceeded, switch to truncate view. Depending on
        `large_repr`, objects are either centrally truncated or printed as
        a summary view. 'None' value means unlimited.
    
        In case python/IPython is running in a terminal and `large_repr`
        equals 'truncate' this can be set to 0 and pandas will auto-detect
        the width of the terminal and print a truncated object which fits
        the screen width. The IPython notebook, IPython qtconsole, or IDLE
        do not run in a terminal and hence it is not possible to do
        correct auto-detection.
        [default: 0] [currently: 0]
    display.max_colwidth : int or None
        The maximum width in characters of a column in the repr of
        a pandas data structure. When the column overflows, a "..."
        placeholder is embedded in the output. A 'None' value means unlimited.
        [default: 50] [currently: 50]
    display.max_info_columns : int
        max_info_columns is used in DataFrame.info method to decide if
        per column information will be printed.
        [default: 100] [currently: 100]
    display.max_info_rows : int or None
        df.info() will usually show null-counts for each column.
        For large frames this can be quite slow. max_info_rows and max_info_cols
        limit this null check only to frames with smaller dimensions than
        specified.
        [default: 1690785] [currently: 1690785]
    display.max_rows : int
        If max_rows is exceeded, switch to truncate view. Depending on
        `large_repr`, objects are either centrally truncated or printed as
        a summary view. 'None' value means unlimited.
    
        In case python/IPython is running in a terminal and `large_repr`
        equals 'truncate' this can be set to 0 and pandas will auto-detect
        the height of the terminal and print a truncated object which fits
        the screen height. The IPython notebook, IPython qtconsole, or
        IDLE do not run in a terminal and hence it is not possible to do
        correct auto-detection.
        [default: 60] [currently: 60]
    display.max_seq_items : int or None
        when pretty-printing a long sequence, no more then `max_seq_items`
        will be printed. If items are omitted, they will be denoted by the
        addition of "..." to the resulting string.
    
        If set to None, the number of items to be printed is unlimited.
        [default: 100] [currently: 100]
    display.memory_usage : bool, string or None
        This specifies if the memory usage of a DataFrame should be displayed when
        df.info() is called. Valid values True,False,'deep'
        [default: True] [currently: True]
    display.min_rows : int
        The numbers of rows to show in a truncated view (when `max_rows` is
        exceeded). Ignored when `max_rows` is set to None or 0. When set to
        None, follows the value of `max_rows`.
        [default: 10] [currently: 10]
    display.multi_sparse : boolean
        "sparsify" MultiIndex display (don't display repeated
        elements in outer levels within groups)
        [default: True] [currently: True]
    display.notebook_repr_html : boolean
        When True, IPython notebook will use html representation for
        pandas objects (if it is available).
        [default: True] [currently: True]
    display.pprint_nest_depth : int
        Controls the number of nested levels to process when pretty-printing
        [default: 3] [currently: 3]
    display.precision : int
        Floating point output precision (number of significant digits). This is
        only a suggestion
        [default: 6] [currently: 6]
    display.show_dimensions : boolean or 'truncate'
        Whether to print out dimensions at the end of DataFrame repr.
        If 'truncate' is specified, only print out the dimensions if the
        frame is truncated (e.g. not display all rows and/or columns)
        [default: truncate] [currently: truncate]
    display.unicode.ambiguous_as_wide : boolean
        Whether to use the Unicode East Asian Width to calculate the display text
        width.
        Enabling this may affect to the performance (default: False)
        [default: False] [currently: False]
    display.unicode.east_asian_width : boolean
        Whether to use the Unicode East Asian Width to calculate the display text
        width.
        Enabling this may affect to the performance (default: False)
        [default: False] [currently: False]
    display.width : int
        Width of the display in characters. In case python/IPython is running in
        a terminal this can be set to None and pandas will correctly auto-detect
        the width.
        Note that the IPython notebook, IPython qtconsole, or IDLE do not run in a
        terminal and hence it is not possible to correctly detect the width.
        [default: 80] [currently: 80]
    io.excel.ods.reader : string
        The default Excel reader engine for 'ods' files. Available options:
        auto, odf.
        [default: auto] [currently: auto]
    io.excel.xls.reader : string
        The default Excel reader engine for 'xls' files. Available options:
        auto, xlrd.
        [default: auto] [currently: auto]
    io.excel.xls.writer : string
        The default Excel writer engine for 'xls' files. Available options:
        auto, xlwt.
        [default: auto] [currently: auto]
    io.excel.xlsb.reader : string
        The default Excel reader engine for 'xlsb' files. Available options:
        auto, pyxlsb.
        [default: auto] [currently: auto]
    io.excel.xlsm.reader : string
        The default Excel reader engine for 'xlsm' files. Available options:
        auto, xlrd, openpyxl.
        [default: auto] [currently: auto]
    io.excel.xlsm.writer : string
        The default Excel writer engine for 'xlsm' files. Available options:
        auto, openpyxl.
        [default: auto] [currently: auto]
    io.excel.xlsx.reader : string
        The default Excel reader engine for 'xlsx' files. Available options:
        auto, xlrd, openpyxl.
        [default: auto] [currently: auto]
    io.excel.xlsx.writer : string
        The default Excel writer engine for 'xlsx' files. Available options:
        auto, openpyxl, xlsxwriter.
        [default: auto] [currently: auto]
    io.hdf.default_format : format
        default format writing format, if None, then
        put will default to 'fixed' and append will default to 'table'
        [default: None] [currently: None]
    io.hdf.dropna_table : boolean
        drop ALL nan rows when appending to a table
        [default: False] [currently: False]
    io.parquet.engine : string
        The default parquet reader/writer engine. Available options:
        'auto', 'pyarrow', 'fastparquet', the default is 'auto'
        [default: auto] [currently: auto]
    mode.chained_assignment : string
        Raise an exception, warn, or no action if trying to use chained assignment,
        The default is warn
        [default: warn] [currently: warn]
    mode.sim_interactive : boolean
        Whether to simulate interactive mode for purposes of testing
        [default: False] [currently: False]
    mode.use_inf_as_na : boolean
        True means treat None, NaN, INF, -INF as NA (old way),
        False means None and NaN are null, but INF, -INF are not NA
        (new way).
        [default: False] [currently: False]
    mode.use_inf_as_null : boolean
        use_inf_as_null had been deprecated and will be removed in a future
        version. Use `use_inf_as_na` instead.
        [default: False] [currently: False]
        (Deprecated, use `mode.use_inf_as_na` instead.)
    plotting.backend : str
        The plotting backend to use. The default value is "matplotlib", the
        backend provided with pandas. Other backends can be specified by
        prodiving the name of the module that implements the backend.
        [default: matplotlib] [currently: matplotlib]
    plotting.matplotlib.register_converters : bool or 'auto'.
        Whether to register converters with matplotlib's units registry for
        dates, times, datetimes, and Periods. Toggling to False will remove
        the converters, restoring any converters that pandas overwrote.
        [default: auto] [currently: auto]
    """
    pass

def parse_datetime_string(*args, **kwargs): # real signature unknown
    """
    Parse datetime string, only returns datetime.
        Also cares special handling matching time patterns.
    
        Returns
        -------
        datetime
    """
    pass

def parse_time_string(*args, **kwargs): # real signature unknown
    """
    Try hard to parse datetime string, leveraging dateutil plus some extra
        goodies like quarter recognition.
    
        Parameters
        ----------
        arg : str
        freq : str or DateOffset, default None
            Helps with interpreting time string if supplied
        dayfirst : bool, default None
            If None uses default from print_config
        yearfirst : bool, default None
            If None uses default from print_config
    
        Returns
        -------
        datetime, datetime/dateutil.parser._result, str
    """
    pass

def try_parse_dates(*args, **kwargs): # real signature unknown
    pass

def try_parse_datetime_components(*args, **kwargs): # real signature unknown
    pass

def try_parse_date_and_time(*args, **kwargs): # real signature unknown
    pass

def try_parse_year_month_day(*args, **kwargs): # real signature unknown
    pass

def _concat_date_cols((dates, times)): # real signature unknown; restored from __doc__
    """
    Concatenates elements from numpy arrays in `date_cols` into strings.
    
        Parameters
        ----------
        date_cols : tuple[ndarray]
        keep_trivial_numbers : bool, default True
            if True and len(date_cols) == 1, then
            conversion (to string from integer/float zero) is not performed
    
        Returns
        -------
        arr_of_rows : ndarray[object]
    
        Examples
        --------
        >>> dates=np.array(['3/31/2019', '4/31/2019'], dtype=object)
        >>> times=np.array(['11:20', '10:45'], dtype=object)
        >>> result = _concat_date_cols((dates, times))
        >>> result
        array(['3/31/2019 11:20', '4/31/2019 10:45'], dtype=object)
    """
    pass

def _DATEUTIL_LEXER_SPLIT(*args, **kwargs): # real signature unknown
    pass

def _does_string_look_like_datetime(*args, **kwargs): # real signature unknown
    """
    Checks whether given string is a datetime: it has to start with '0' or
        be greater than 1000.
    
        Parameters
        ----------
        py_string: str
    
        Returns
        -------
        bool
            Whether given string is potentially a datetime.
    """
    pass

def _format_is_iso(*args, **kwargs): # real signature unknown
    """
    Does format match the iso8601 set that can be handled by the C parser?
        Generally of form YYYY-MM-DDTHH:MM:SS - date separator can be different
        but must be consistent.  Leading 0s in dates and times are optional.
    """
    pass

def _guess_datetime_format(*args, **kwargs): # real signature unknown
    """
    Guess the datetime format of a given datetime string.
    
        Parameters
        ----------
        dt_str : string, datetime string to guess the format of
        dayfirst : boolean, default False
            If True parses dates with the day first, eg 20/01/2005
            Warning: dayfirst=True is not strict, but will prefer to parse
            with day first (this is a known bug).
        dt_str_parse : function, defaults to `dateutil.parser.parse`
            This function should take in a datetime string and return
            a `datetime.datetime` guess that the datetime string represents
        dt_str_split : function, defaults to `_DATEUTIL_LEXER_SPLIT` (dateutil)
            This function should take in a datetime string and return
            a list of strings, the guess of the various specific parts
            e.g. '2011/12/30' -> ['2011', '/', '12', '/', '30']
    
        Returns
        -------
        ret : datetime format string (for `strftime` or `strptime`)
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class DateParseError(ValueError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class relativedelta(object):
    """
    The relativedelta type is designed to be applied to an existing datetime and
        can replace specific components of that datetime, or represents an interval
        of time.
    
        It is based on the specification of the excellent work done by M.-A. Lemburg
        in his
        `mx.DateTime <https://www.egenix.com/products/python/mxBase/mxDateTime/>`_ extension.
        However, notice that this type does *NOT* implement the same algorithm as
        his work. Do *NOT* expect it to behave like mx.DateTime's counterpart.
    
        There are two different ways to build a relativedelta instance. The
        first one is passing it two date/datetime classes::
    
            relativedelta(datetime1, datetime2)
    
        The second one is passing it any number of the following keyword arguments::
    
            relativedelta(arg1=x,arg2=y,arg3=z...)
    
            year, month, day, hour, minute, second, microsecond:
                Absolute information (argument is singular); adding or subtracting a
                relativedelta with absolute information does not perform an arithmetic
                operation, but rather REPLACES the corresponding value in the
                original datetime with the value(s) in relativedelta.
    
            years, months, weeks, days, hours, minutes, seconds, microseconds:
                Relative information, may be negative (argument is plural); adding
                or subtracting a relativedelta with relative information performs
                the corresponding aritmetic operation on the original datetime value
                with the information in the relativedelta.
    
            weekday: 
                One of the weekday instances (MO, TU, etc) available in the
                relativedelta module. These instances may receive a parameter N,
                specifying the Nth weekday, which could be positive or negative
                (like MO(+1) or MO(-2)). Not specifying it is the same as specifying
                +1. You can also use an integer, where 0=MO. This argument is always
                relative e.g. if the calculated date is already Monday, using MO(1)
                or MO(-1) won't change the day. To effectively make it absolute, use
                it in combination with the day argument (e.g. day=1, MO(1) for first
                Monday of the month).
    
            leapdays:
                Will add given days to the date found, if year is a leap
                year, and the date found is post 28 of february.
    
            yearday, nlyearday:
                Set the yearday or the non-leap year day (jump leap days).
                These are converted to day/month/leapdays information.
    
        There are relative and absolute forms of the keyword
        arguments. The plural is relative, and the singular is
        absolute. For each argument in the order below, the absolute form
        is applied first (by setting each attribute to that value) and
        then the relative form (by adding the value to the attribute).
    
        The order of attributes considered when this relativedelta is
        added to a datetime is:
    
        1. Year
        2. Month
        3. Day
        4. Hours
        5. Minutes
        6. Seconds
        7. Microseconds
    
        Finally, weekday is applied, using the rule described above.
    
        For example
    
        >>> from datetime import datetime
        >>> from dateutil.relativedelta import relativedelta, MO
        >>> dt = datetime(2018, 4, 9, 13, 37, 0)
        >>> delta = relativedelta(hours=25, day=1, weekday=MO(1))
        >>> dt + delta
        datetime.datetime(2018, 4, 2, 14, 37)
    
        First, the day is set to 1 (the first of the month), then 25 hours
        are added, to get to the 2nd day and 14th hour, finally the
        weekday is applied, but since the 2nd is already a Monday there is
        no effect.
    """
    def normalized(self): # reliably restored by inspect
        """
        Return a version of this object represented entirely using integer
                values for the relative attributes.
        
                >>> relativedelta(days=1.5, hours=2).normalized()
                relativedelta(days=+1, hours=+14)
        
                :return:
                    Returns a :class:`dateutil.relativedelta.relativedelta` object.
        """
        pass

    def _fix(self): # reliably restored by inspect
        # no doc
        pass

    def _set_months(self, months): # reliably restored by inspect
        # no doc
        pass

    def __abs__(self): # reliably restored by inspect
        # no doc
        pass

    def __add__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __bool__(self): # reliably restored by inspect
        # no doc
        pass

    def __div__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __eq__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __hash__(self): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, dt1=None, dt2=None, years=0, months=0, days=0, leapdays=0, weeks=0, hours=0, minutes=0, seconds=0, microseconds=0, year=None, month=None, day=None, weekday=None, yearday=None, nlyearday=None, hour=None, minute=None, second=None, microsecond=None): # reliably restored by inspect
        # no doc
        pass

    def __mul__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __neg__(self): # reliably restored by inspect
        # no doc
        pass

    def __ne__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __nonzero__(self): # reliably restored by inspect
        # no doc
        pass

    def __radd__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    def __rmul__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __rsub__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __sub__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __truediv__(self, other): # reliably restored by inspect
        # no doc
        pass

    weeks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'dateutil.relativedelta\', \'__doc__\': "\\n    The relativedelta type is designed to be applied to an existing datetime and\\n    can replace specific components of that datetime, or represents an interval\\n    of time.\\n\\n    It is based on the specification of the excellent work done by M.-A. Lemburg\\n    in his\\n    `mx.DateTime <https://www.egenix.com/products/python/mxBase/mxDateTime/>`_ extension.\\n    However, notice that this type does *NOT* implement the same algorithm as\\n    his work. Do *NOT* expect it to behave like mx.DateTime\'s counterpart.\\n\\n    There are two different ways to build a relativedelta instance. The\\n    first one is passing it two date/datetime classes::\\n\\n        relativedelta(datetime1, datetime2)\\n\\n    The second one is passing it any number of the following keyword arguments::\\n\\n        relativedelta(arg1=x,arg2=y,arg3=z...)\\n\\n        year, month, day, hour, minute, second, microsecond:\\n            Absolute information (argument is singular); adding or subtracting a\\n            relativedelta with absolute information does not perform an arithmetic\\n            operation, but rather REPLACES the corresponding value in the\\n            original datetime with the value(s) in relativedelta.\\n\\n        years, months, weeks, days, hours, minutes, seconds, microseconds:\\n            Relative information, may be negative (argument is plural); adding\\n            or subtracting a relativedelta with relative information performs\\n            the corresponding aritmetic operation on the original datetime value\\n            with the information in the relativedelta.\\n\\n        weekday: \\n            One of the weekday instances (MO, TU, etc) available in the\\n            relativedelta module. These instances may receive a parameter N,\\n            specifying the Nth weekday, which could be positive or negative\\n            (like MO(+1) or MO(-2)). Not specifying it is the same as specifying\\n            +1. You can also use an integer, where 0=MO. This argument is always\\n            relative e.g. if the calculated date is already Monday, using MO(1)\\n            or MO(-1) won\'t change the day. To effectively make it absolute, use\\n            it in combination with the day argument (e.g. day=1, MO(1) for first\\n            Monday of the month).\\n\\n        leapdays:\\n            Will add given days to the date found, if year is a leap\\n            year, and the date found is post 28 of february.\\n\\n        yearday, nlyearday:\\n            Set the yearday or the non-leap year day (jump leap days).\\n            These are converted to day/month/leapdays information.\\n\\n    There are relative and absolute forms of the keyword\\n    arguments. The plural is relative, and the singular is\\n    absolute. For each argument in the order below, the absolute form\\n    is applied first (by setting each attribute to that value) and\\n    then the relative form (by adding the value to the attribute).\\n\\n    The order of attributes considered when this relativedelta is\\n    added to a datetime is:\\n\\n    1. Year\\n    2. Month\\n    3. Day\\n    4. Hours\\n    5. Minutes\\n    6. Seconds\\n    7. Microseconds\\n\\n    Finally, weekday is applied, using the rule described above.\\n\\n    For example\\n\\n    >>> from datetime import datetime\\n    >>> from dateutil.relativedelta import relativedelta, MO\\n    >>> dt = datetime(2018, 4, 9, 13, 37, 0)\\n    >>> delta = relativedelta(hours=25, day=1, weekday=MO(1))\\n    >>> dt + delta\\n    datetime.datetime(2018, 4, 2, 14, 37)\\n\\n    First, the day is set to 1 (the first of the month), then 25 hours\\n    are added, to get to the 2nd day and 14th hour, finally the\\n    weekday is applied, but since the 2nd is already a Monday there is\\n    no effect.\\n\\n    ", \'__init__\': <function relativedelta.__init__ at 0x0000024E991B8C80>, \'_fix\': <function relativedelta._fix at 0x0000024E991BE048>, \'weeks\': <property object at 0x0000024E991BC318>, \'_set_months\': <function relativedelta._set_months at 0x0000024E991BE1E0>, \'normalized\': <function relativedelta.normalized at 0x0000024E991BE268>, \'__add__\': <function relativedelta.__add__ at 0x0000024E991BE2F0>, \'__radd__\': <function relativedelta.__radd__ at 0x0000024E991BE378>, \'__rsub__\': <function relativedelta.__rsub__ at 0x0000024E991BE400>, \'__sub__\': <function relativedelta.__sub__ at 0x0000024E991BE488>, \'__abs__\': <function relativedelta.__abs__ at 0x0000024E991BE510>, \'__neg__\': <function relativedelta.__neg__ at 0x0000024E991BE598>, \'__bool__\': <function relativedelta.__bool__ at 0x0000024E991BE620>, \'__nonzero__\': <function relativedelta.__bool__ at 0x0000024E991BE620>, \'__mul__\': <function relativedelta.__mul__ at 0x0000024E991BE6A8>, \'__rmul__\': <function relativedelta.__mul__ at 0x0000024E991BE6A8>, \'__eq__\': <function relativedelta.__eq__ at 0x0000024E991BE730>, \'__hash__\': <function relativedelta.__hash__ at 0x0000024E991BE7B8>, \'__ne__\': <function relativedelta.__ne__ at 0x0000024E991BE840>, \'__div__\': <function relativedelta.__div__ at 0x0000024E991BE8C8>, \'__truediv__\': <function relativedelta.__div__ at 0x0000024E991BE8C8>, \'__repr__\': <function relativedelta.__repr__ at 0x0000024E991BE950>, \'__dict__\': <attribute \'__dict__\' of \'relativedelta\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'relativedelta\' objects>})'


class tzoffset(__datetime.tzinfo):
    """
    A simple class for representing a fixed offset from UTC.
    
        :param name:
            The timezone name, to be returned when ``tzname()`` is called.
        :param offset:
            The time zone offset in seconds, or (since version 2.6.0, represented
            as a :py:class:`datetime.timedelta` object).
    """
    def dst(self, dt): # reliably restored by inspect
        # no doc
        pass

    def fromutc(self, dt): # reliably restored by inspect
        # no doc
        pass

    def is_ambiguous(self, dt): # reliably restored by inspect
        """
        Whether or not the "wall time" of a given datetime is ambiguous in this
                zone.
        
                :param dt:
                    A :py:class:`datetime.datetime`, naive or time zone aware.
                :return:
                    Returns ``True`` if ambiguous, ``False`` otherwise.
        
                .. versionadded:: 2.6.0
        """
        pass

    def tzname(self, dt): # reliably restored by inspect
        # no doc
        pass

    def utcoffset(self, dt): # reliably restored by inspect
        # no doc
        pass

    def __eq__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, name, offset): # reliably restored by inspect
        # no doc
        pass

    def __ne__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _TzOffsetFactory__instances = None # (!) real value is '<WeakValueDictionary at 0x24e990da128>'
    _TzOffsetFactory__strong_cache = OrderedDict()
    _TzOffsetFactory__strong_cache_size = 8
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'dateutil.tz.tz', '__doc__': '\\n    A simple class for representing a fixed offset from UTC.\\n\\n    :param name:\\n        The timezone name, to be returned when ``tzname()`` is called.\\n    :param offset:\\n        The time zone offset in seconds, or (since version 2.6.0, represented\\n        as a :py:class:`datetime.timedelta` object).\\n    ', '__init__': <function tzoffset.__init__ at 0x0000024E99226620>, 'utcoffset': <function tzoffset.utcoffset at 0x0000024E992266A8>, 'dst': <function tzoffset.dst at 0x0000024E99226730>, 'tzname': <function tzoffset.tzname at 0x0000024E992267B8>, 'fromutc': <function tzoffset.fromutc at 0x0000024E992268C8>, 'is_ambiguous': <function tzoffset.is_ambiguous at 0x0000024E99226950>, '__eq__': <function tzoffset.__eq__ at 0x0000024E992269D8>, '__hash__': None, '__ne__': <function tzoffset.__ne__ at 0x0000024E99226A60>, '__repr__': <function tzoffset.__repr__ at 0x0000024E99226AE8>, '__reduce__': <method '__reduce__' of 'object' objects>, '__dict__': <attribute '__dict__' of 'tzoffset' objects>, '__weakref__': <attribute '__weakref__' of 'tzoffset' objects>, '_TzOffsetFactory__instances': <WeakValueDictionary at 0x24e990da128>, '_TzOffsetFactory__strong_cache': OrderedDict(), '_TzOffsetFactory__strong_cache_size': 8})"
    __hash__ = None


class _dateutil_tzlocal(__dateutil_tz__common._tzinfo):
    """ A :class:`tzinfo` subclass built around the ``time`` timezone functions. """
    def dst(self, dt): # reliably restored by inspect
        # no doc
        pass

    def is_ambiguous(self, dt): # reliably restored by inspect
        """
        Whether or not the "wall time" of a given datetime is ambiguous in this
                zone.
        
                :param dt:
                    A :py:class:`datetime.datetime`, naive or time zone aware.
        
        
                :return:
                    Returns ``True`` if ambiguous, ``False`` otherwise.
        
                .. versionadded:: 2.6.0
        """
        pass

    def tzname(self, dt): # reliably restored by inspect
        # no doc
        pass

    def utcoffset(self, dt): # reliably restored by inspect
        # no doc
        pass

    def _isdst(self, dt, fold_naive=True): # reliably restored by inspect
        # no doc
        pass

    def _naive_is_dst(self, dt): # reliably restored by inspect
        # no doc
        pass

    def __eq__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __init__(self): # reliably restored by inspect
        # no doc
        pass

    def __ne__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    __hash__ = None


class _dateutil_tzstr(__dateutil_tz_tz.tzrange):
    """
    ``tzstr`` objects are time zone objects specified by a time-zone string as
        it would be passed to a ``TZ`` variable on POSIX-style systems (see
        the `GNU C Library: TZ Variable`_ for more details).
    
        There is one notable exception, which is that POSIX-style time zones use an
        inverted offset format, so normally ``GMT+3`` would be parsed as an offset
        3 hours *behind* GMT. The ``tzstr`` time zone object will parse this as an
        offset 3 hours *ahead* of GMT. If you would like to maintain the POSIX
        behavior, pass a ``True`` value to ``posix_offset``.
    
        The :class:`tzrange` object provides the same functionality, but is
        specified using :class:`relativedelta.relativedelta` objects. rather than
        strings.
    
        :param s:
            A time zone string in ``TZ`` variable format. This can be a
            :class:`bytes` (2.x: :class:`str`), :class:`str` (2.x:
            :class:`unicode`) or a stream emitting unicode characters
            (e.g. :class:`StringIO`).
    
        :param posix_offset:
            Optional. If set to ``True``, interpret strings such as ``GMT+3`` or
            ``UTC+3`` as being 3 hours *behind* UTC rather than ahead, per the
            POSIX standard.
    
        .. caution::
    
            Prior to version 2.7.0, this function also supported time zones
            in the format:
    
                * ``EST5EDT,4,0,6,7200,10,0,26,7200,3600``
                * ``EST5EDT,4,1,0,7200,10,-1,0,7200,3600``
    
            This format is non-standard and has been deprecated; this function
            will raise a :class:`DeprecatedTZFormatWarning` until
            support is removed in a future version.
    
        .. _`GNU C Library: TZ Variable`:
            https://www.gnu.org/software/libc/manual/html_node/TZ-Variable.html
    """
    def _delta(self, x, isend=0): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, s, posix_offset=False): # reliably restored by inspect
        # no doc
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    _TzStrFactory__instances = None # (!) real value is '<WeakValueDictionary at 0x24e9921df28>'
    _TzStrFactory__strong_cache = OrderedDict()
    _TzStrFactory__strong_cache_size = 8


class _dateutil_tzutc(__datetime.tzinfo):
    """
    This is a tzinfo object that represents the UTC time zone.
    
        **Examples:**
    
        .. doctest::
    
            >>> from datetime import *
            >>> from dateutil.tz import *
    
            >>> datetime.now()
            datetime.datetime(2003, 9, 27, 9, 40, 1, 521290)
    
            >>> datetime.now(tzutc())
            datetime.datetime(2003, 9, 27, 12, 40, 12, 156379, tzinfo=tzutc())
    
            >>> datetime.now(tzutc()).tzname()
            'UTC'
    
        .. versionchanged:: 2.7.0
            ``tzutc()`` is now a singleton, so the result of ``tzutc()`` will
            always return the same object.
    
            .. doctest::
    
                >>> from dateutil.tz import tzutc, UTC
                >>> tzutc() is tzutc()
                True
                >>> tzutc() is UTC
                True
    """
    def dst(self, dt): # reliably restored by inspect
        # no doc
        pass

    def fromutc(self, dt): # reliably restored by inspect
        """
        Fast track version of fromutc() returns the original ``dt`` object for
                any valid :py:class:`datetime.datetime` object.
        """
        pass

    def is_ambiguous(self, dt): # reliably restored by inspect
        """
        Whether or not the "wall time" of a given datetime is ambiguous in this
                zone.
        
                :param dt:
                    A :py:class:`datetime.datetime`, naive or time zone aware.
        
        
                :return:
                    Returns ``True`` if ambiguous, ``False`` otherwise.
        
                .. versionadded:: 2.6.0
        """
        pass

    def tzname(self, dt): # reliably restored by inspect
        # no doc
        pass

    def utcoffset(self, dt): # reliably restored by inspect
        # no doc
        pass

    def __eq__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ne__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _TzSingleton__instance = tzutc()
    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'dateutil.tz.tz\', \'__doc__\': "\\n    This is a tzinfo object that represents the UTC time zone.\\n\\n    **Examples:**\\n\\n    .. doctest::\\n\\n        >>> from datetime import *\\n        >>> from dateutil.tz import *\\n\\n        >>> datetime.now()\\n        datetime.datetime(2003, 9, 27, 9, 40, 1, 521290)\\n\\n        >>> datetime.now(tzutc())\\n        datetime.datetime(2003, 9, 27, 12, 40, 12, 156379, tzinfo=tzutc())\\n\\n        >>> datetime.now(tzutc()).tzname()\\n        \'UTC\'\\n\\n    .. versionchanged:: 2.7.0\\n        ``tzutc()`` is now a singleton, so the result of ``tzutc()`` will\\n        always return the same object.\\n\\n        .. doctest::\\n\\n            >>> from dateutil.tz import tzutc, UTC\\n            >>> tzutc() is tzutc()\\n            True\\n            >>> tzutc() is UTC\\n            True\\n    ", \'utcoffset\': <function tzutc.utcoffset at 0x0000024E99226158>, \'dst\': <function tzutc.dst at 0x0000024E992261E0>, \'tzname\': <function tzutc.tzname at 0x0000024E99226268>, \'is_ambiguous\': <function tzutc.is_ambiguous at 0x0000024E992262F0>, \'fromutc\': <function tzutc.fromutc at 0x0000024E99226400>, \'__eq__\': <function tzutc.__eq__ at 0x0000024E99226488>, \'__hash__\': None, \'__ne__\': <function tzutc.__ne__ at 0x0000024E99226510>, \'__repr__\': <function tzutc.__repr__ at 0x0000024E99226598>, \'__reduce__\': <method \'__reduce__\' of \'object\' objects>, \'__dict__\': <attribute \'__dict__\' of \'tzutc\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'tzutc\' objects>, \'_TzSingleton__instance\': tzutc()})'
    __hash__ = None


class _timelex(object):
    # no doc
    def get_tokens(self, *args, **kwargs): # real signature unknown
        """
        This function breaks the time string into lexical units (tokens), which
                can be parsed by the parser. Lexical units are demarcated by changes in
                the character set, so any continuous string of letters is considered
                one unit, any continuous string of numbers is considered one unit.
                The main complication arises from the fact that dots ('.') can be used
                both as separators (e.g. "Sep.20.2009") or decimal points (e.g.
                "4:30:21.447"). As such, it is necessary to read the full context of
                any dot-separated strings before breaking it into tokens; as such, this
                function maintains a "token stack", for when the ambiguous context
                demands that multiple tokens be parsed at once.
        """
        pass

    @classmethod
    def split(cls, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'pandas._libs.tslibs.parsing', '__init__': <cyfunction _timelex.__init__ at 0x0000024E9925B100>, 'get_tokens': <cyfunction _timelex.get_tokens at 0x0000024E9925B1B8>, 'split': <classmethod object at 0x0000024E991CD4E0>, '__dict__': <attribute '__dict__' of '_timelex' objects>, '__weakref__': <attribute '__weakref__' of '_timelex' objects>, '__doc__': None})"


# variables with complex values

DEFAULTPARSER = None # (!) real value is '<dateutil.parser._parser.parser object at 0x0000024E992540F0>'

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

nat_strings = None # (!) real value is "{'NAT', 'nat', 'NAN', 'nan', 'NaT', 'NaN'}"

_DEFAULT_DATETIME = None # (!) real value is 'datetime.datetime(1, 1, 1, 0, 0)'

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000024E99238A20>'

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.tslibs.parsing', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000024E99238A20>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\pandas\\\\_libs\\\\tslibs\\\\parsing.cp37-win_amd64.pyd')"

__test__ = {
    '_concat_date_cols (line 913)': "\n    Concatenates elements from numpy arrays in `date_cols` into strings.\n\n    Parameters\n    ----------\n    date_cols : tuple[ndarray]\n    keep_trivial_numbers : bool, default True\n        if True and len(date_cols) == 1, then\n        conversion (to string from integer/float zero) is not performed\n\n    Returns\n    -------\n    arr_of_rows : ndarray[object]\n\n    Examples\n    --------\n    >>> dates=np.array(['3/31/2019', '4/31/2019'], dtype=object)\n    >>> times=np.array(['11:20', '10:45'], dtype=object)\n    >>> result = _concat_date_cols((dates, times))\n    >>> result\n    array(['3/31/2019 11:20', '4/31/2019 10:45'], dtype=object)\n    ",
}

