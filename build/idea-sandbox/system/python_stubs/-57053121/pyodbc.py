# encoding: utf-8
# module pyodbc
# from C:\Users\Doly\Anaconda3\lib\site-packages\pyodbc.cp37-win_amd64.pyd
# by generator 1.147
"""
A database module for accessing databases via ODBC.

This module conforms to the DB API 2.0 specification while providing
non-standard convenience features.  Only standard Python data types are used
so additional DLLs are not required.

Static Variables:

version
  The module version string.  Official builds will have a version in the format
  `major.minor.revision`, such as 2.1.7.  Beta versions will have -beta appended,
  such as 2.1.8-beta03.  (This would be a build before the official 2.1.8 release.)
  Some special test builds will have a test name (the git branch name) prepended,
  such as fixissue90-2.1.8-beta03.

apilevel
  The string constant '2.0' indicating this module supports DB API level 2.0.

lowercase
  A Boolean that controls whether column names in result rows are lowercased.
  This can be changed any time and affects queries executed after the change.
  The default is False.  This can be useful when database columns have
  inconsistent capitalization.

pooling
  A Boolean indicating whether connection pooling is enabled.  This is a
  global (HENV) setting, so it can only be modified before the first
  connection is made.  The default is True, which enables ODBC connection
  pooling.

threadsafety
  The integer 1, indicating that threads may share the module but not
  connections.  Note that connections and cursors may be used by different
  threads, just not at the same time.

qmark
  The string constant 'qmark' to indicate parameters are identified using
  question marks.
"""

# imports
import datetime as __datetime


# Variables with simple values

apilevel = '2.0'

lowercase = False

native_uuid = False

paramstyle = 'qmark'

pooling = True

SQLWCHAR_SIZE = 2

SQL_ACCESSIBLE_PROCEDURES = 20
SQL_ACCESSIBLE_TABLES = 19

SQL_ACCESS_MODE = 101

SQL_ACTIVE_ENVIRONMENTS = 116

SQL_AGGREGATE_FUNCTIONS = 169

SQL_ALTER_DOMAIN = 117
SQL_ALTER_TABLE = 86

SQL_ASYNC_MODE = 10021

SQL_ATTR_ACCESS_MODE = 101

SQL_ATTR_ANSI_APP = 115

SQL_ATTR_AUTOCOMMIT = 102

SQL_ATTR_CURRENT_CATALOG = 109

SQL_ATTR_LOGIN_TIMEOUT = 103

SQL_ATTR_ODBC_CURSORS = 110

SQL_ATTR_QUIET_MODE = 111

SQL_ATTR_TRACE = 104
SQL_ATTR_TRACEFILE = 105

SQL_ATTR_TRANSLATE_LIB = 106
SQL_ATTR_TRANSLATE_OPTION = 107

SQL_ATTR_TXN_ISOLATION = 108

SQL_AUTOCOMMIT = 102

SQL_BATCH_ROW_COUNT = 120

SQL_BATCH_SUPPORT = 121

SQL_BIGINT = -5
SQL_BINARY = -2
SQL_BIT = -7

SQL_BOOKMARK_PERSISTENCE = 82

SQL_CATALOG_LOCATION = 114
SQL_CATALOG_NAME = 10003

SQL_CATALOG_NAME_SEPARATOR = 41

SQL_CATALOG_TERM = 42
SQL_CATALOG_USAGE = 92

SQL_CHAR = 1

SQL_COLLATION_SEQ = 10004

SQL_COLUMN_ALIAS = 87

SQL_CONCAT_NULL_BEHAVIOR = 22

SQL_CONVERT_BIGINT = 53
SQL_CONVERT_BINARY = 54
SQL_CONVERT_BIT = 55
SQL_CONVERT_CHAR = 56
SQL_CONVERT_DATE = 57
SQL_CONVERT_DECIMAL = 58
SQL_CONVERT_DOUBLE = 59
SQL_CONVERT_FLOAT = 60
SQL_CONVERT_FUNCTIONS = 48
SQL_CONVERT_GUID = 173
SQL_CONVERT_INTEGER = 61

SQL_CONVERT_INTERVAL_DAY_TIME = 123

SQL_CONVERT_INTERVAL_YEAR_MONTH = 124

SQL_CONVERT_LONGVARBINARY = 71
SQL_CONVERT_LONGVARCHAR = 62
SQL_CONVERT_NUMERIC = 63
SQL_CONVERT_REAL = 64
SQL_CONVERT_SMALLINT = 65
SQL_CONVERT_TIME = 66
SQL_CONVERT_TIMESTAMP = 67
SQL_CONVERT_TINYINT = 68
SQL_CONVERT_VARBINARY = 69
SQL_CONVERT_VARCHAR = 70
SQL_CONVERT_WCHAR = 122
SQL_CONVERT_WLONGVARCHAR = 125
SQL_CONVERT_WVARCHAR = 126

SQL_CORRELATION_NAME = 74

SQL_CREATE_ASSERTION = 127

SQL_CREATE_CHARACTER_SET = 128

SQL_CREATE_COLLATION = 129
SQL_CREATE_DOMAIN = 130
SQL_CREATE_SCHEMA = 131
SQL_CREATE_TABLE = 132
SQL_CREATE_TRANSLATION = 133
SQL_CREATE_VIEW = 134

SQL_CURRENT_QUALIFIER = 109

SQL_CURSOR_COMMIT_BEHAVIOR = 23

SQL_CURSOR_ROLLBACK_BEHAVIOR = 24

SQL_DATABASE_NAME = 16

SQL_DATA_SOURCE_NAME = 2

SQL_DATA_SOURCE_READ_ONLY = 25

SQL_DATETIME_LITERALS = 119

SQL_DBMS_NAME = 17
SQL_DBMS_VER = 18

SQL_DDL_INDEX = 170

SQL_DECIMAL = 3

SQL_DEFAULT_TXN_ISOLATION = 26

SQL_DESCRIBE_PARAMETER = 10002

SQL_DM_VER = 171

SQL_DOUBLE = 8

SQL_DRIVER_HDESC = 135
SQL_DRIVER_HENV = 4
SQL_DRIVER_HLIB = 76
SQL_DRIVER_HSTMT = 5
SQL_DRIVER_NAME = 6

SQL_DRIVER_ODBC_VER = 77

SQL_DRIVER_VER = 7

SQL_DROP_ASSERTION = 136

SQL_DROP_CHARACTER_SET = 137

SQL_DROP_COLLATION = 138
SQL_DROP_DOMAIN = 139
SQL_DROP_SCHEMA = 140
SQL_DROP_TABLE = 141
SQL_DROP_TRANSLATION = 142
SQL_DROP_VIEW = 143

SQL_DYNAMIC_CURSOR_ATTRIBUTES1 = 144
SQL_DYNAMIC_CURSOR_ATTRIBUTES2 = 145

SQL_EXPRESSIONS_IN_ORDERBY = 27

SQL_FILE_USAGE = 84

SQL_FLOAT = 6

SQL_FORWARD_ONLY_CURSOR_ATTRIBUTES1 = 146
SQL_FORWARD_ONLY_CURSOR_ATTRIBUTES2 = 147

SQL_GETDATA_EXTENSIONS = 81

SQL_GROUP_BY = 88

SQL_GUID = -11

SQL_IDENTIFIER_CASE = 28

SQL_IDENTIFIER_QUOTE_CHAR = 29

SQL_INDEX_KEYWORDS = 148

SQL_INFO_SCHEMA_VIEWS = 149

SQL_INSERT_STATEMENT = 172

SQL_INTEGER = 4
SQL_INTEGRITY = 73

SQL_INTERVAL_DAY = 103

SQL_INTERVAL_DAY_TO_HOUR = 108
SQL_INTERVAL_DAY_TO_MINUTE = 109
SQL_INTERVAL_DAY_TO_SECOND = 110

SQL_INTERVAL_HOUR = 104

SQL_INTERVAL_HOUR_TO_MINUTE = 111
SQL_INTERVAL_HOUR_TO_SECOND = 112

SQL_INTERVAL_MINUTE = 105

SQL_INTERVAL_MINUTE_TO_SECOND = 113

SQL_INTERVAL_MONTH = 102
SQL_INTERVAL_SECOND = 106
SQL_INTERVAL_YEAR = 101

SQL_INTERVAL_YEAR_TO_MONTH = 107

SQL_KEYSET_CURSOR_ATTRIBUTES1 = 150
SQL_KEYSET_CURSOR_ATTRIBUTES2 = 151

SQL_KEYWORDS = 89

SQL_LIKE_ESCAPE_CLAUSE = 113

SQL_LOGIN_TIMEOUT = 103

SQL_LONGVARBINARY = -4
SQL_LONGVARCHAR = -1

SQL_MAX_ASYNC_CONCURRENT_STATEMENTS = 10022

SQL_MAX_BINARY_LITERAL_LEN = 112

SQL_MAX_CATALOG_NAME_LEN = 34

SQL_MAX_CHAR_LITERAL_LEN = 108

SQL_MAX_COLUMNS_IN_GROUP_BY = 97

SQL_MAX_COLUMNS_IN_INDEX = 98

SQL_MAX_COLUMNS_IN_ORDER_BY = 99

SQL_MAX_COLUMNS_IN_SELECT = 100
SQL_MAX_COLUMNS_IN_TABLE = 101

SQL_MAX_COLUMN_NAME_LEN = 30

SQL_MAX_CONCURRENT_ACTIVITIES = 1

SQL_MAX_CURSOR_NAME_LEN = 31

SQL_MAX_DRIVER_CONNECTIONS = 0

SQL_MAX_IDENTIFIER_LEN = 10005

SQL_MAX_INDEX_SIZE = 102

SQL_MAX_PROCEDURE_NAME_LEN = 33

SQL_MAX_ROW_SIZE = 104

SQL_MAX_ROW_SIZE_INCLUDES_LONG = 103

SQL_MAX_SCHEMA_NAME_LEN = 32

SQL_MAX_STATEMENT_LEN = 105

SQL_MAX_TABLES_IN_SELECT = 106

SQL_MAX_TABLE_NAME_LEN = 35

SQL_MAX_USER_NAME_LEN = 107

SQL_MULTIPLE_ACTIVE_TXN = 37

SQL_MULT_RESULT_SETS = 36

SQL_NEED_LONG_DATA_LEN = 111

SQL_NON_NULLABLE_COLUMNS = 75

SQL_NO_NULLS = 0

SQL_NULLABLE = 1

SQL_NULLABLE_UNKNOWN = 2

SQL_NULL_COLLATION = 85

SQL_NUMERIC = 2

SQL_NUMERIC_FUNCTIONS = 49

SQL_ODBC_CURSORS = 110

SQL_ODBC_INTERFACE_CONFORMANCE = 152

SQL_ODBC_VER = 10

SQL_OJ_ALL_COMPARISON_OPS = 64

SQL_OJ_CAPABILITIES = 115
SQL_OJ_FULL = 4
SQL_OJ_INNER = 32
SQL_OJ_LEFT = 1
SQL_OJ_NESTED = 8

SQL_OJ_NOT_ORDERED = 16

SQL_OJ_RIGHT = 2

SQL_OPT_TRACE = 104
SQL_OPT_TRACEFILE = 105

SQL_ORDER_BY_COLUMNS_IN_SELECT = 90

SQL_PACKET_SIZE = 112

SQL_PARAM_ARRAY_ROW_COUNTS = 153

SQL_PARAM_ARRAY_SELECTS = 154

SQL_PARAM_INPUT = 1

SQL_PARAM_INPUT_OUTPUT = 2

SQL_PARAM_OUTPUT = 4

SQL_PARAM_TYPE_UNKNOWN = 0

SQL_PC_NOT_PSEUDO = 1

SQL_PC_PSEUDO = 2
SQL_PC_UNKNOWN = 0

SQL_PROCEDURES = 21

SQL_PROCEDURE_TERM = 40

SQL_QUIET_MODE = 111

SQL_QUOTED_IDENTIFIER_CASE = 93

SQL_REAL = 7

SQL_RESULT_COL = 3

SQL_RETURN_VALUE = 5

SQL_ROW_UPDATES = 11

SQL_SCHEMA_TERM = 39
SQL_SCHEMA_USAGE = 91

SQL_SCOPE_CURROW = 0
SQL_SCOPE_SESSION = 2
SQL_SCOPE_TRANSACTION = 1

SQL_SCROLL_OPTIONS = 44

SQL_SEARCH_PATTERN_ESCAPE = 14

SQL_SERVER_NAME = 13

SQL_SMALLINT = 5

SQL_SPECIAL_CHARACTERS = 94

SQL_SQL92_DATETIME_FUNCTIONS = 155

SQL_SQL92_FOREIGN_KEY_DELETE_RULE = 156

SQL_SQL92_FOREIGN_KEY_UPDATE_RULE = 157

SQL_SQL92_GRANT = 158

SQL_SQL92_NUMERIC_VALUE_FUNCTIONS = 159

SQL_SQL92_PREDICATES = 160

SQL_SQL92_RELATIONAL_JOIN_OPERATORS = 161

SQL_SQL92_REVOKE = 162

SQL_SQL92_ROW_VALUE_CONSTRUCTOR = 163

SQL_SQL92_STRING_FUNCTIONS = 164

SQL_SQL92_VALUE_EXPRESSIONS = 165

SQL_SQL_CONFORMANCE = 118

SQL_SS_TIME2 = -154
SQL_SS_XML = -152

SQL_STANDARD_CLI_CONFORMANCE = 166

SQL_STATIC_CURSOR_ATTRIBUTES1 = 167
SQL_STATIC_CURSOR_ATTRIBUTES2 = 168

SQL_STRING_FUNCTIONS = 50

SQL_SUBQUERIES = 95

SQL_SYSTEM_FUNCTIONS = 51

SQL_TABLE_TERM = 45

SQL_TIMEDATE_ADD_INTERVALS = 109

SQL_TIMEDATE_DIFF_INTERVALS = 110

SQL_TIMEDATE_FUNCTIONS = 52

SQL_TINYINT = -6

SQL_TRANSLATE_DLL = 106
SQL_TRANSLATE_OPTION = 107

SQL_TXN_CAPABLE = 46
SQL_TXN_ISOLATION = 108

SQL_TXN_ISOLATION_OPTION = 72

SQL_TXN_READ_COMMITTED = 2
SQL_TXN_READ_UNCOMMITTED = 1

SQL_TXN_REPEATABLE_READ = 4

SQL_TXN_SERIALIZABLE = 8

SQL_TYPE_DATE = 91
SQL_TYPE_TIME = 92
SQL_TYPE_TIMESTAMP = 93

SQL_UNION = 96

SQL_UNKNOWN_TYPE = 0

SQL_USER_NAME = 47

SQL_VARBINARY = -3
SQL_VARCHAR = 12
SQL_WCHAR = -8
SQL_WLONGVARCHAR = -10
SQL_WMETADATA = -888
SQL_WVARCHAR = -9

SQL_XOPEN_CLI_YEAR = 10000

threadsafety = 1

UNICODE_SIZE = 2

version = '4.0.26'

# functions

def connect(p_str, autocommit=False, ansi=False, timeout=0, **kwargs): # real signature unknown; restored from __doc__
    """
    connect(str, autocommit=False, ansi=False, timeout=0, **kwargs) --> Connection
    
    Accepts an ODBC connection string and returns a new Connection object.
    
    The connection string will be passed to SQLDriverConnect, so a DSN connection
    can be created using:
    
      cnxn = pyodbc.connect('DSN=DataSourceName;UID=user;PWD=password')
    
    To connect without requiring a DSN, specify the driver and connection
    information:
    
      DRIVER={SQL Server};SERVER=localhost;DATABASE=testdb;UID=user;PWD=password
    
    Note the use of braces when a value contains spaces.  Refer to SQLDriverConnect
    documentation or the documentation of your ODBC driver for details.
    
    The connection string can be passed as the string `str`, as a list of keywords,
    or a combination of the two.  Any keywords except autocommit, ansi, and timeout
    (see below) are simply added to the connection string.
    
      connect('server=localhost;user=me')
      connect(server='localhost', user='me')
      connect('server=localhost', user='me')
    
    The DB API recommends the keywords 'user', 'password', and 'host', but these
    are not valid ODBC keywords, so these will be converted to 'uid', 'pwd', and
    'server'.
    
    Special Keywords
    
    The following specal keywords are processed by pyodbc and are not added to the
    connection string.  (If you must use these in your connection string, pass them
    as a string, not as keywords.)
    
      autocommit
        If False or zero, the default, transactions are created automatically as
        defined in the DB API 2.  If True or non-zero, the connection is put into
        ODBC autocommit mode and statements are committed automatically.
       
      ansi
        By default, pyodbc first attempts to connect using the Unicode version of
        SQLDriverConnectW.  If the driver returns IM001 indicating it does not
        support the Unicode version, the ANSI version is tried.  Any other SQLSTATE
        is turned into an exception.  Setting ansi to true skips the Unicode
        attempt and only connects using the ANSI version.  This is useful for
        drivers that return the wrong SQLSTATE (or if pyodbc is out of date and
        should support other SQLSTATEs).
       
      timeout
        An integer login timeout in seconds, used to set the SQL_ATTR_LOGIN_TIMEOUT
        attribute of the connection.  The default is 0 which means the database's
        default timeout, if any, is used.
    """
    pass

def dataSources(): # real signature unknown; restored from __doc__
    """
    dataSources() --> { DSN : Description }
    
    Returns a dictionary mapping available DSNs to their descriptions.
    """
    pass

def DateFromTicks(ticks): # real signature unknown; restored from __doc__
    """
    DateFromTicks(ticks) --> datetime.date
    
    Returns a date object initialized from the given ticks value (number of seconds
    since the epoch; see the documentation of the standard Python time module for
    details).
    """
    pass

def drivers(): # real signature unknown; restored from __doc__
    """
    drivers() --> [ DriverName1, DriverName2 ... DriverNameN ]
    
    Returns a list of installed drivers.
    """
    pass

def getDecimalSeparator(): # real signature unknown; restored from __doc__
    """
    getDecimalSeparator() -> string
    
    Gets the decimal separator character used when parsing NUMERIC from the database.
    """
    return ""

def setDecimalSeparator(string): # real signature unknown; restored from __doc__
    """
    setDecimalSeparator(string) -> None
    
    Sets the decimal separator character used when parsing NUMERIC from the database.
    """
    pass

def TimeFromTicks(ticks): # real signature unknown; restored from __doc__
    """
    TimeFromTicks(ticks) --> datetime.time
    
    Returns a time object initialized from the given ticks value (number of seconds
    since the epoch; see the documentation of the standard Python time module for
    details).
    """
    pass

def TimestampFromTicks(ticks): # real signature unknown; restored from __doc__
    """
    TimestampFromTicks(ticks) --> datetime.datetime
    
    Returns a datetime object initialized from the given ticks value (number of
    seconds since the epoch; see the documentation of the standard Python time
    module for details
    """
    pass

# classes

class Binary(object):
    """
    bytearray(iterable_of_ints) -> bytearray
    bytearray(string, encoding[, errors]) -> bytearray
    bytearray(bytes_or_buffer) -> mutable copy of bytes_or_buffer
    bytearray(int) -> bytes array of size given by the parameter initialized with null bytes
    bytearray() -> empty bytes array
    
    Construct a mutable bytearray object from:
      - an iterable yielding integers in range(256)
      - a text string encoded using the specified encoding
      - a bytes or a buffer object
      - any object implementing the buffer API.
      - an integer
    """
    def append(self, *args, **kwargs): # real signature unknown
        """
        Append a single item to the end of the bytearray.
        
          item
            The item to be appended.
        """
        pass

    def capitalize(self): # real signature unknown; restored from __doc__
        """
        B.capitalize() -> copy of B
        
        Return a copy of B with only its first character capitalized (ASCII)
        and the rest lower-cased.
        """
        pass

    def center(self, width, fillchar=None): # real signature unknown; restored from __doc__
        """
        B.center(width[, fillchar]) -> copy of B
        
        Return B centered in a string of length width.  Padding is
        done using the specified fill character (default is a space).
        """
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        """ Remove all items from the bytearray. """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        """ Return a copy of B. """
        pass

    def count(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        B.count(sub[, start[, end]]) -> int
        
        Return the number of non-overlapping occurrences of subsection sub in
        bytes B[start:end].  Optional arguments start and end are interpreted
        as in slice notation.
        """
        return 0

    def decode(self, *args, **kwargs): # real signature unknown
        """
        Decode the bytearray using the codec registered for encoding.
        
          encoding
            The encoding with which to decode the bytearray.
          errors
            The error handling scheme to use for the handling of decoding errors.
            The default is 'strict' meaning that decoding errors raise a
            UnicodeDecodeError. Other possible values are 'ignore' and 'replace'
            as well as any other name registered with codecs.register_error that
            can handle UnicodeDecodeErrors.
        """
        pass

    def endswith(self, suffix, start=None, end=None): # real signature unknown; restored from __doc__
        """
        B.endswith(suffix[, start[, end]]) -> bool
        
        Return True if B ends with the specified suffix, False otherwise.
        With optional start, test B beginning at that position.
        With optional end, stop comparing B at that position.
        suffix can also be a tuple of bytes to try.
        """
        return False

    def expandtabs(self, tabsize=8): # real signature unknown; restored from __doc__
        """
        B.expandtabs(tabsize=8) -> copy of B
        
        Return a copy of B where all tab characters are expanded using spaces.
        If tabsize is not given, a tab size of 8 characters is assumed.
        """
        pass

    def extend(self, *args, **kwargs): # real signature unknown
        """
        Append all the items from the iterator or sequence to the end of the bytearray.
        
          iterable_of_ints
            The iterable of items to append.
        """
        pass

    def find(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        B.find(sub[, start[, end]]) -> int
        
        Return the lowest index in B where subsection sub is found,
        such that sub is contained within B[start,end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
        """
        return 0

    @classmethod
    def fromhex(cls, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Create a bytearray object from a string of hexadecimal numbers.
        
        Spaces between two numbers are accepted.
        Example: bytearray.fromhex('B9 01EF') -> bytearray(b'\\xb9\\x01\\xef')
        """
        pass

    def hex(self): # real signature unknown; restored from __doc__
        """
        B.hex() -> string
        
        Create a string of hexadecimal numbers from a bytearray object.
        Example: bytearray([0xb9, 0x01, 0xef]).hex() -> 'b901ef'.
        """
        return ""

    def index(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        B.index(sub[, start[, end]]) -> int
        
        Return the lowest index in B where subsection sub is found,
        such that sub is contained within B[start,end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Raises ValueError when the subsection is not found.
        """
        return 0

    def insert(self, *args, **kwargs): # real signature unknown
        """
        Insert a single item into the bytearray before the given index.
        
          index
            The index where the value is to be inserted.
          item
            The item to be inserted.
        """
        pass

    def isalnum(self): # real signature unknown; restored from __doc__
        """
        B.isalnum() -> bool
        
        Return True if all characters in B are alphanumeric
        and there is at least one character in B, False otherwise.
        """
        return False

    def isalpha(self): # real signature unknown; restored from __doc__
        """
        B.isalpha() -> bool
        
        Return True if all characters in B are alphabetic
        and there is at least one character in B, False otherwise.
        """
        return False

    def isascii(self): # real signature unknown; restored from __doc__
        """
        B.isascii() -> bool
        
        Return True if B is empty or all characters in B are ASCII,
        False otherwise.
        """
        return False

    def isdigit(self): # real signature unknown; restored from __doc__
        """
        B.isdigit() -> bool
        
        Return True if all characters in B are digits
        and there is at least one character in B, False otherwise.
        """
        return False

    def islower(self): # real signature unknown; restored from __doc__
        """
        B.islower() -> bool
        
        Return True if all cased characters in B are lowercase and there is
        at least one cased character in B, False otherwise.
        """
        return False

    def isspace(self): # real signature unknown; restored from __doc__
        """
        B.isspace() -> bool
        
        Return True if all characters in B are whitespace
        and there is at least one character in B, False otherwise.
        """
        return False

    def istitle(self): # real signature unknown; restored from __doc__
        """
        B.istitle() -> bool
        
        Return True if B is a titlecased string and there is at least one
        character in B, i.e. uppercase characters may only follow uncased
        characters and lowercase characters only cased ones. Return False
        otherwise.
        """
        return False

    def isupper(self): # real signature unknown; restored from __doc__
        """
        B.isupper() -> bool
        
        Return True if all cased characters in B are uppercase and there is
        at least one cased character in B, False otherwise.
        """
        return False

    def join(self, *args, **kwargs): # real signature unknown
        """
        Concatenate any number of bytes/bytearray objects.
        
        The bytearray whose method is called is inserted in between each pair.
        
        The result is returned as a new bytearray object.
        """
        pass

    def ljust(self, width, fillchar=None): # real signature unknown; restored from __doc__
        """
        B.ljust(width[, fillchar]) -> copy of B
        
        Return B left justified in a string of length width. Padding is
        done using the specified fill character (default is a space).
        """
        pass

    def lower(self): # real signature unknown; restored from __doc__
        """
        B.lower() -> copy of B
        
        Return a copy of B with all ASCII characters converted to lowercase.
        """
        pass

    def lstrip(self, *args, **kwargs): # real signature unknown
        """
        Strip leading bytes contained in the argument.
        
        If the argument is omitted or None, strip leading ASCII whitespace.
        """
        pass

    def maketrans(self, *args, **kwargs): # real signature unknown
        """
        Return a translation table useable for the bytes or bytearray translate method.
        
        The returned table will be one where each byte in frm is mapped to the byte at
        the same position in to.
        
        The bytes objects frm and to must be of the same length.
        """
        pass

    def partition(self, *args, **kwargs): # real signature unknown
        """
        Partition the bytearray into three parts using the given separator.
        
        This will search for the separator sep in the bytearray. If the separator is
        found, returns a 3-tuple containing the part before the separator, the
        separator itself, and the part after it as new bytearray objects.
        
        If the separator is not found, returns a 3-tuple containing the copy of the
        original bytearray object and two empty bytearray objects.
        """
        pass

    def pop(self, *args, **kwargs): # real signature unknown
        """
        Remove and return a single item from B.
        
          index
            The index from where to remove the item.
            -1 (the default value) means remove the last item.
        
        If no index argument is given, will pop the last item.
        """
        pass

    def remove(self, *args, **kwargs): # real signature unknown
        """
        Remove the first occurrence of a value in the bytearray.
        
          value
            The value to remove.
        """
        pass

    def replace(self, *args, **kwargs): # real signature unknown
        """
        Return a copy with all occurrences of substring old replaced by new.
        
          count
            Maximum number of occurrences to replace.
            -1 (the default value) means replace all occurrences.
        
        If the optional argument count is given, only the first count occurrences are
        replaced.
        """
        pass

    def reverse(self, *args, **kwargs): # real signature unknown
        """ Reverse the order of the values in B in place. """
        pass

    def rfind(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        B.rfind(sub[, start[, end]]) -> int
        
        Return the highest index in B where subsection sub is found,
        such that sub is contained within B[start,end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
        """
        return 0

    def rindex(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        B.rindex(sub[, start[, end]]) -> int
        
        Return the highest index in B where subsection sub is found,
        such that sub is contained within B[start,end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Raise ValueError when the subsection is not found.
        """
        return 0

    def rjust(self, width, fillchar=None): # real signature unknown; restored from __doc__
        """
        B.rjust(width[, fillchar]) -> copy of B
        
        Return B right justified in a string of length width. Padding is
        done using the specified fill character (default is a space)
        """
        pass

    def rpartition(self, *args, **kwargs): # real signature unknown
        """
        Partition the bytearray into three parts using the given separator.
        
        This will search for the separator sep in the bytearray, starting at the end.
        If the separator is found, returns a 3-tuple containing the part before the
        separator, the separator itself, and the part after it as new bytearray
        objects.
        
        If the separator is not found, returns a 3-tuple containing two empty bytearray
        objects and the copy of the original bytearray object.
        """
        pass

    def rsplit(self, *args, **kwargs): # real signature unknown
        """
        Return a list of the sections in the bytearray, using sep as the delimiter.
        
          sep
            The delimiter according which to split the bytearray.
            None (the default value) means split on ASCII whitespace characters
            (space, tab, return, newline, formfeed, vertical tab).
          maxsplit
            Maximum number of splits to do.
            -1 (the default value) means no limit.
        
        Splitting is done starting at the end of the bytearray and working to the front.
        """
        pass

    def rstrip(self, *args, **kwargs): # real signature unknown
        """
        Strip trailing bytes contained in the argument.
        
        If the argument is omitted or None, strip trailing ASCII whitespace.
        """
        pass

    def split(self, *args, **kwargs): # real signature unknown
        """
        Return a list of the sections in the bytearray, using sep as the delimiter.
        
          sep
            The delimiter according which to split the bytearray.
            None (the default value) means split on ASCII whitespace characters
            (space, tab, return, newline, formfeed, vertical tab).
          maxsplit
            Maximum number of splits to do.
            -1 (the default value) means no limit.
        """
        pass

    def splitlines(self, *args, **kwargs): # real signature unknown
        """
        Return a list of the lines in the bytearray, breaking at line boundaries.
        
        Line breaks are not included in the resulting list unless keepends is given and
        true.
        """
        pass

    def startswith(self, prefix, start=None, end=None): # real signature unknown; restored from __doc__
        """
        B.startswith(prefix[, start[, end]]) -> bool
        
        Return True if B starts with the specified prefix, False otherwise.
        With optional start, test B beginning at that position.
        With optional end, stop comparing B at that position.
        prefix can also be a tuple of bytes to try.
        """
        return False

    def strip(self, *args, **kwargs): # real signature unknown
        """
        Strip leading and trailing bytes contained in the argument.
        
        If the argument is omitted or None, strip leading and trailing ASCII whitespace.
        """
        pass

    def swapcase(self): # real signature unknown; restored from __doc__
        """
        B.swapcase() -> copy of B
        
        Return a copy of B with uppercase ASCII characters converted
        to lowercase ASCII and vice versa.
        """
        pass

    def title(self): # real signature unknown; restored from __doc__
        """
        B.title() -> copy of B
        
        Return a titlecased version of B, i.e. ASCII words start with uppercase
        characters, all remaining cased characters have lowercase.
        """
        pass

    def translate(self, *args, **kwargs): # real signature unknown
        """
        Return a copy with each character mapped by the given translation table.
        
          table
            Translation table, which must be a bytes object of length 256.
        
        All characters occurring in the optional argument delete are removed.
        The remaining characters are mapped through the given translation table.
        """
        pass

    def upper(self): # real signature unknown; restored from __doc__
        """
        B.upper() -> copy of B
        
        Return a copy of B with all ASCII characters converted to uppercase.
        """
        pass

    def zfill(self, width): # real signature unknown; restored from __doc__
        """
        B.zfill(width) -> copy of B
        
        Pad a numeric string B with zeros on the left, to fill a field
        of the specified width.  B is never truncated.
        """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __alloc__(self): # real signature unknown; restored from __doc__
        """
        B.__alloc__() -> int
        
        Return the number of bytes actually allocated.
        """
        return 0

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __iadd__(self, *args, **kwargs): # real signature unknown
        """ Implement self+=value. """
        pass

    def __imul__(self, *args, **kwargs): # real signature unknown
        """ Implement self*=value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
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

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Return state information for pickling. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Return state information for pickling. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Returns the size of the bytearray object in memory, in bytes. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    __hash__ = None


BINARY = Binary


class Connection(object):
    """
    Connection objects manage connections to the database.
    
    Each manages a single ODBC HDBC.
    """
    def add_output_converter(self, sqltype, func): # real signature unknown; restored from __doc__
        """
        add_output_converter(sqltype, func) --> None
        
        Register an output converter function that will be called whenever a value with
        the given SQL type is read from the database.
        
        sqltype
          The integer SQL type value to convert, which can be one of the defined
          standard constants (e.g. pyodbc.SQL_VARCHAR) or a database-specific value
          (e.g. -151 for the SQL Server 2008 geometry data type).
        
        func
          The converter function which will be called with a single parameter, the
          value, and should return the converted value.  If the value is NULL, the
          parameter will be None.  Otherwise it will be a bytes object.
        
        If func is None, any existing converter is removed.
        """
        pass

    def clear_output_converters(self): # real signature unknown; restored from __doc__
        """
        clear_output_converters() --> None
        
        Remove all output converter functions.
        """
        pass

    def close(self, *args, **kwargs): # real signature unknown
        """
        Close the connection now (rather than whenever __del__ is called).
        
        The connection will be unusable from this point forward and a ProgrammingError
        will be raised if any operation is attempted with the connection.  The same
        applies to all cursor objects trying to use the connection.
        
        Note that closing a connection without committing the changes first will cause
        an implicit rollback to be performed.
        """
        pass

    def commit(self, *args, **kwargs): # real signature unknown
        """ Commit any pending transaction to the database. """
        pass

    def cursor(self, *args, **kwargs): # real signature unknown
        """ Return a new Cursor object using the connection. """
        pass

    def execute(self, sql, params=None): # real signature unknown; restored from __doc__
        """
        execute(sql, [params]) --> Cursor
        
        Create a new Cursor object, call its execute method, and return it.  See
        Cursor.execute for more details.
        
        This is a convenience method that is not part of the DB API.  Since a new
        Cursor is allocated by each call, this should not be used if more than one SQL
        statement needs to be executed.
        """
        pass

    def getinfo(self, type): # real signature unknown; restored from __doc__
        """
        getinfo(type) --> str | int | bool
        
        Calls SQLGetInfo, passing `type`, and returns the result formatted as a Python object.
        """
        pass

    def get_output_converter(self, sqltype): # real signature unknown; restored from __doc__
        """
        get_output_converter(sqltype) --> <class 'function'>
        
        Get the output converter function that was registered with
        add_output_converter.  It is safe to call if no converter is
        registered for the type (returns None).
        
        sqltype
          The integer SQL type value being converted, which can be one of the defined
          standard constants (e.g. pyodbc.SQL_VARCHAR) or a database-specific value
          (e.g. -151 for the SQL Server 2008 geometry data type).
        """
        pass

    def remove_output_converter(self, sqltype): # real signature unknown; restored from __doc__
        """
        remove_output_converter(sqltype) --> None
        
        Remove an output converter function that was registered with
        add_output_converter.  It is safe to call if no converter is
        registered for the type.
        
        sqltype
          The integer SQL type value being converted, which can be one of the defined
          standard constants (e.g. pyodbc.SQL_VARCHAR) or a database-specific value
          (e.g. -151 for the SQL Server 2008 geometry data type).
        """
        pass

    def rollback(self, *args, **kwargs): # real signature unknown
        """ Causes the the database to roll back to the start of any pending transaction. """
        pass

    def setdecoding(self, sqltype, encoding=None, ctype=None): # real signature unknown; restored from __doc__
        """
        setdecoding(sqltype, encoding=None, ctype=None) --> None
        
        Configures how text of type `ctype` (SQL_CHAR or SQL_WCHAR) is decoded
        when read from the database.
        
        When reading, the database will assign one of the sqltypes to text columns.
        pyodbc uses this lookup the decoding information set by this function.
        sqltype: pyodbc.SQL_CHAR or pyodbc.SQL_WCHAR
        
        encoding: A registered Python encoding such as "utf-8".
        
        ctype: The C data type should be requested.  Set this to SQL_CHAR for
          single-byte encodings like UTF-8 and to SQL_WCHAR for two-byte encodings
          like UTF-16.
        """
        pass

    def setencoding(self, *args, **kwargs): # real signature unknown
        pass

    def set_attr(self, attr_id, value): # real signature unknown; restored from __doc__
        """
        set_attr(attr_id, value) -> None
        
        Calls SQLSetConnectAttr with the given values.
        
        attr_id
          The attribute id (integer) to set.  These are ODBC or driver constants.
        
        value
          An integer value.
        
        At this time, only integer values are supported and are always passed as SQLUINTEGER.
        """
        pass

    def __enter__(self): # real signature unknown; restored from __doc__
        """ __enter__() -> self. """
        return self

    def __exit__(self, *excinfo): # real signature unknown; restored from __doc__
        """ __exit__(*excinfo) -> None.  Commits the connection if necessary. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    autocommit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns True if the connection is in autocommit mode; False otherwise."""

    maxwrite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The maximum bytes to write before using SQLPutData."""

    searchescape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ODBC search pattern escape character, as returned by
SQLGetInfo(SQL_SEARCH_PATTERN_ESCAPE).  These are driver specific."""

    timeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The timeout in seconds, zero means no timeout."""



class Cursor(object):
    """
    Cursor objects represent a database cursor, which is used to manage the context
    of a fetch operation.  Cursors created from the same connection are not
    isolated, i.e., any changes done to the database by a cursor are immediately
    visible by the other cursors.  Cursors created from different connections are
    isolated.
    
    Cursors implement the iterator protocol, so results can be iterated:
    
      cursor.execute(sql)
      for row in cursor:
         print row[0]
    """
    def cancel(self): # real signature unknown; restored from __doc__
        """
        Cursor.cancel() -> None
        Cancels the processing of the current statement.
        
        Cancels the processing of the current statement.
        
        This calls SQLCancel and is designed to be called from another thread tostop processing of an ongoing query.
        """
        pass

    def close(self, *args, **kwargs): # real signature unknown
        """
        Close the cursor now (rather than whenever __del__ is called).  The cursor will
        be unusable from this point forward; a ProgrammingError exception will be
        raised if any operation is attempted with the cursor.
        """
        pass

    def columns(self, table=None, catalog=None, schema=None, column=None): # real signature unknown; restored from __doc__
        """
        C.columns(table=None, catalog=None, schema=None, column=None)
        
        Creates a results set of column names in specified tables by executing the ODBC SQLColumns function.
        Each row fetched has the following columns:
          0) table_cat
          1) table_schem
          2) table_name
          3) column_name
          4) data_type
          5) type_name
          6) column_size
          7) buffer_length
          8) decimal_digits
          9) num_prec_radix
         10) nullable
         11) remarks
         12) column_def
         13) sql_data_type
         14) sql_datetime_sub
         15) char_octet_length
         16) ordinal_position
         17) is_nullable
        """
        pass

    def commit(self, *args, **kwargs): # real signature unknown
        """
        Commits any pending transaction to the database on the current connection,
        including those from other cursors.
        """
        pass

    def execute(self, sql, params=None): # real signature unknown; restored from __doc__
        """
        C.execute(sql, [params]) --> Cursor
        
        Prepare and execute a database query or command.
        
        Parameters may be provided as a sequence (as specified by the DB API) or
        simply passed in one after another (non-standard):
        
          cursor.execute(sql, (param1, param2))
        
            or
        
          cursor.execute(sql, param1, param2)
        """
        pass

    def executemany(self, sql, seq_of_params): # real signature unknown; restored from __doc__
        """
        executemany(sql, seq_of_params) --> Cursor | count | None
        
        Prepare a database query or command and then execute it against all parameter
        sequences  found in the sequence seq_of_params.
        
        Only the result of the final execution is returned.  See `execute` for a
        description of parameter passing the return value.
        """
        pass

    def fetchall(self): # real signature unknown; restored from __doc__
        """
        fetchall() --> list of Rows
        
        Fetch all remaining rows of a query result, returning them as a list of Rows.
        An empty list is returned if there are no more rows.
        
        A ProgrammingError exception is raised if the previous call to execute() did
        not produce any result set or no call was issued yet.
        """
        pass

    def fetchmany(self, size=None): # real signature unknown; restored from __doc__
        """
        fetchmany(size=cursor.arraysize) --> list of Rows
        
        Fetch the next set of rows of a query result, returning a list of Row
        instances. An empty list is returned when no more rows are available.
        
        The number of rows to fetch per call is specified by the parameter.  If it is
        not given, the cursor's arraysize determines the number of rows to be
        fetched. The method should try to fetch as many rows as indicated by the size
        parameter. If this is not possible due to the specified number of rows not
        being available, fewer rows may be returned.
        
        A ProgrammingError exception is raised if the previous call to execute() did
        not produce any result set or no call was issued yet.
        """
        pass

    def fetchone(self): # real signature unknown; restored from __doc__
        """
        fetchone() --> Row | None
        
        Fetch the next row of a query result set, returning a single Row instance, or
        None when no more data is available.
        
        A ProgrammingError exception is raised if the previous call to execute() did
        not produce any result set or no call was issued yet.
        """
        pass

    def fetchval(self): # real signature unknown; restored from __doc__
        """
        fetchval() --> value | None
        
        Returns the first column of the next row in the result set or None
        if there are no more rows.
        """
        pass

    def foreignKeys(self, table=None, catalog=None, schema=None, foreignTable=None, foreignCatalog=None, foreignSchema=None): # real signature unknown; restored from __doc__
        """
        C.foreignKeys(table=None, catalog=None, schema=None,
                    foreignTable=None, foreignCatalog=None, foreignSchema=None) --> self
        
        Executes the SQLForeignKeys function and creates a results set of column names
        that are foreign keys in the specified table (columns in the specified table
        that refer to primary keys in other tables) or foreign keys in other tables
        that refer to the primary key in the specified table.
        
        Each row fetched has the following columns:
          0) pktable_cat
          1) pktable_schem
          2) pktable_name
          3) pkcolumn_name
          4) fktable_cat
          5) fktable_schem
          6) fktable_name
          7) fkcolumn_name
          8) key_seq
          9) update_rule
         10) delete_rule
         11) fk_name
         12) pk_name
         13) deferrability
        """
        pass

    def getTypeInfo(self, sqlType=None): # real signature unknown; restored from __doc__
        """
        C.getTypeInfo(sqlType=None) --> self
        
        Executes SQLGetTypeInfo a creates a result set with information about the
        specified data type or all data types supported by the ODBC driver if not
        specified.
        
        Each row fetched has the following columns:
         0) type_name
         1) data_type
         2) column_size
         3) literal_prefix
         4) literal_suffix
         5) create_params
         6) nullable
         7) case_sensitive
         8) searchable
         9) unsigned_attribute
        10) fixed_prec_scale
        11) auto_unique_value
        12) local_type_name
        13) minimum_scale
        14) maximum_scale
        15) sql_data_type
        16) sql_datetime_sub
        17) num_prec_radix
        18) interval_precision
        """
        pass

    def nextset(self): # real signature unknown; restored from __doc__
        """
        nextset() --> True | None
        
        Jumps to the next resultset if the last sql has multiple resultset.Returns True if there is a next resultset otherwise None.
        """
        pass

    def primaryKeys(self, table, catalog=None, schema=None): # real signature unknown; restored from __doc__
        """
        C.primaryKeys(table, catalog=None, schema=None) --> self
        
        Creates a results set of column names that make up the primary key for a table
        by executing the SQLPrimaryKeys function.
        Each row fetched has the following columns:
         0) table_cat
         1) table_schem
         2) table_name
         3) column_name
         4) key_seq
         5) pk_name
        """
        pass

    def procedureColumns(self, procedure=None, catalog=None, schema=None): # real signature unknown; restored from __doc__
        """
        C.procedureColumns(procedure=None, catalog=None, schema=None) --> self
        
        Executes SQLProcedureColumns and creates a result set of information
        about stored procedure columns and results.
          0) procedure_cat
          1) procedure_schem
          2) procedure_name
          3) column_name
          4) column_type
          5) data_type
          6) type_name
          7) column_size
          8) buffer_length
          9) decimal_digits
         10) num_prec_radix
         11) nullable
         12) remarks
         13) column_def
         14) sql_data_type
         15) sql_datetime_sub
         16) char_octet_length
         17) ordinal_position
         18) is_nullable
        """
        pass

    def procedures(self, procedure=None, catalog=None, schema=None): # real signature unknown; restored from __doc__
        """
        C.procedures(procedure=None, catalog=None, schema=None) --> self
        
        Executes SQLProcedures and creates a result set of information about the
        procedures in the data source.
        Each row fetched has the following columns:
         0) procedure_cat
         1) procedure_schem
         2) procedure_name
         3) num_input_params
         4) num_output_params
         5) num_result_sets
         6) remarks
         7) procedure_type
        """
        pass

    def rollback(self, *args, **kwargs): # real signature unknown
        """
        Rolls back any pending transaction to the database on the current connection,
        including those from other cursors.
        """
        pass

    def rowIdColumns(self, table, catalog=None, schema=None, nullable=True): # real signature unknown; restored from __doc__
        """
        C.rowIdColumns(table, catalog=None, schema=None, nullable=True) -->
        
        Executes SQLSpecialColumns with SQL_BEST_ROWID which creates a result set of columns that
        uniquely identify a row
        
        Each row fetched has the following columns:
         0) scope
         1) column_name
         2) data_type
         3) type_name
         4) column_size
         5) buffer_length
         6) decimal_digits
         7) pseudo_column
        """
        pass

    def rowVerColumns(self, *args, **kwargs): # real signature unknown
        """
        C.rowIdColumns(table, catalog=None, schema=None, nullable=True) --> self
        
        Executes SQLSpecialColumns with SQL_ROWVER which creates a result set of columns that
        are automatically updated when any value in the row is updated.
        
        Each row fetched has the following columns:
         0) scope
         1) column_name
         2) data_type
         3) type_name
         4) column_size
         5) buffer_length
         6) decimal_digits
         7) pseudo_column
        """
        pass

    def setinputsizes(self, sizes): # real signature unknown; restored from __doc__
        """
        setinputsizes(sizes) -> None
        
        Sets the type information to be used when binding parameters.
        sizes must be a sequence of values, one for each input parameter.
        Each value may be an integer to override the column size when binding character
        data, a Type Object to override the SQL type, or a sequence of integers to specify
        (SQL type, column size, decimal digits) where any may be none to use the default.
        
        Parameters beyond the length of the sequence will be bound with the defaults.
        Setting sizes to None reverts all parameters to the defaults.
        """
        pass

    def setoutputsize(self, *args, **kwargs): # real signature unknown
        """ Ignored. """
        pass

    def skip(self, count): # real signature unknown; restored from __doc__
        """
        skip(count) --> None
        
        Skips the next `count` records by calling SQLFetchScroll with SQL_FETCH_NEXT.
        For convenience, skip(0) is accepted and will do nothing.
        """
        pass

    def statistics(self, catalog=None, schema=None, unique=False, quick=True): # real signature unknown; restored from __doc__
        """
        C.statistics(catalog=None, schema=None, unique=False, quick=True) --> self
        
        Creates a results set of statistics about a single table and the indexes associated with 
        the table by executing SQLStatistics.
        unique
          If True, only unique indexes are retured.  Otherwise all indexes are returned.
        quick
          If True, CARDINALITY and PAGES are returned  only if they are readily available
          from the server
        
        Each row fetched has the following columns:
        
          0) table_cat
          1) table_schem
          2) table_name
          3) non_unique
          4) index_qualifier
          5) index_name
          6) type
          7) ordinal_position
          8) column_name
          9) asc_or_desc
         10) cardinality
         11) pages
         12) filter_condition
        """
        pass

    def tables(self, table=None, catalog=None, schema=None, tableType=None): # real signature unknown; restored from __doc__
        """
        C.tables(table=None, catalog=None, schema=None, tableType=None) --> self
        
        Executes SQLTables and creates a results set of tables defined in the data
        source.
        
        The table, catalog, and schema interpret the '_' and '%' characters as
        wildcards.  The escape character is driver specific, so use
        `Connection.searchescape`.
        
        Each row fetched has the following columns:
         0) table_cat: The catalog name.
         1) table_schem: The schema name.
         2) table_name: The table name.
         3) table_type: One of 'TABLE', 'VIEW', SYSTEM TABLE', 'GLOBAL TEMPORARY'
            'LOCAL TEMPORARY', 'ALIAS', 'SYNONYM', or a data source-specific type name.
        """
        pass

    def __enter__(self): # real signature unknown; restored from __doc__
        """ __enter__() -> self. """
        return self

    def __exit__(self, *excinfo): # real signature unknown; restored from __doc__
        """ __exit__(*excinfo) -> None.  Commits the connection if necessary.. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Implement next(self). """
        pass

    arraysize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This read/write attribute specifies the number of rows to fetch at a time with
fetchmany(). It defaults to 1 meaning to fetch a single row at a time."""

    connection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This read-only attribute return a reference to the Connection object on which
the cursor was created.

The attribute simplifies writing polymorph code in multi-connection
environments."""

    description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This read-only attribute is a sequence of 7-item sequences.  Each of these
sequences contains information describing one result column: (name, type_code,
display_size, internal_size, precision, scale, null_ok).  All values except
name, type_code, and internal_size are None.  The type_code entry will be the
type object used to create values for that column (e.g. `str` or
`datetime.datetime`).

This attribute will be None for operations that do not return rows or if the
cursor has not had an operation invoked via the execute() method yet.

The type_code can be interpreted by comparing it to the Type Objects defined in
the DB API and defined the pyodbc module: Date, Time, Timestamp, Binary,
STRING, BINARY, NUMBER, and DATETIME."""

    fast_executemany = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This read/write attribute specifies whether to use a faster executemany() which
uses parameter arrays. Not all drivers may work with this implementation."""

    noscan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """NOSCAN statement attr"""

    rowcount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This read-only attribute specifies the number of rows the last DML statement
 (INSERT, UPDATE, DELETE) affected.  This is set to -1 for SELECT statements."""



class Error(Exception):
    """
    Exception that is the base class of all other error exceptions. You can use
    this to catch all errors with one single 'except' statement.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class DatabaseError(Error):
    """ Exception raised for errors that are related to the database. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class DataError(DatabaseError):
    """
    Exception raised for errors that are due to problems with the processed data
    like division by zero, numeric value out of range, etc.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Date(object):
    """ date(year, month, day) --> date object """
    def ctime(self): # real signature unknown; restored from __doc__
        """ Return ctime() style string. """
        pass

    @classmethod
    def fromisoformat(cls, *args, **kwargs): # real signature unknown
        """ str -> Construct a date from the output of date.isoformat() """
        pass

    @classmethod
    def fromordinal(cls, *args, **kwargs): # real signature unknown
        """ int -> date corresponding to a proleptic Gregorian ordinal. """
        pass

    @classmethod
    def fromtimestamp(cls, *args, **kwargs): # real signature unknown
        """ timestamp -> local date from a POSIX timestamp (like time.time()). """
        pass

    def isocalendar(self, *args, **kwargs): # real signature unknown
        """ Return a 3-tuple containing ISO year, week number, and weekday. """
        pass

    def isoformat(self, *args, **kwargs): # real signature unknown
        """ Return string in ISO 8601 format, YYYY-MM-DD. """
        pass

    def isoweekday(self, *args, **kwargs): # real signature unknown
        """
        Return the day of the week represented by the date.
        Monday == 1 ... Sunday == 7
        """
        pass

    def replace(self, *args, **kwargs): # real signature unknown
        """ Return date with new specified fields. """
        pass

    def strftime(self): # real signature unknown; restored from __doc__
        """ format -> strftime() style string. """
        pass

    def timetuple(self, *args, **kwargs): # real signature unknown
        """ Return time tuple, compatible with time.localtime(). """
        pass

    @classmethod
    def today(cls, *args, **kwargs): # real signature unknown
        """ Current date or datetime:  same as self.__class__.fromtimestamp(time.time()). """
        pass

    def toordinal(self, *args, **kwargs): # real signature unknown
        """ Return proleptic Gregorian ordinal.  January 1 of year 1 is day 1. """
        pass

    def weekday(self, *args, **kwargs): # real signature unknown
        """
        Return the day of the week represented by the date.
        Monday == 0 ... Sunday == 6
        """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
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

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
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

    day = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    max = datetime.date(9999, 12, 31)
    min = datetime.date(1, 1, 1)
    resolution = datetime.timedelta(days=1)


class Timestamp(__datetime.date):
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


DATETIME = Timestamp


class IntegrityError(DatabaseError):
    """
    Exception raised when the relational integrity of the database is affected,
    e.g. a foreign key check fails.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class InterfaceError(Error):
    """
    Exception raised for errors that are related to the database interface rather
    than the database itself.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class InternalError(DatabaseError):
    """
    Exception raised when the database encounters an internal error, e.g. the
    cursor is not valid anymore, the transaction is out of sync, etc.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class NotSupportedError(DatabaseError):
    """
    Exception raised in case a method or database API was used which is not
    supported by the database, e.g. requesting a .rollback() on a connection that
    does not support transaction or has transactions turned off.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class NUMBER(object):
    """ Convert a string or number to a floating point number, if possible. """
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Return integer ratio.
        
        Return a pair of integers, whose ratio is exactly equal to the original float
        and with a positive denominator.
        
        Raise OverflowError on infinities and a ValueError on NaNs.
        
        >>> (10.0).as_integer_ratio()
        (10, 1)
        >>> (0.0).as_integer_ratio()
        (0, 1)
        >>> (-.25).as_integer_ratio()
        (-1, 4)
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Return self, the complex conjugate of any float. """
        pass

    @classmethod
    def fromhex(cls, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Create a floating-point number from a hexadecimal string.
        
        >>> float.fromhex('0x1.ffffp10')
        2047.984375
        >>> float.fromhex('-0x1p-1074')
        -5e-324
        """
        pass

    def hex(self): # real signature unknown; restored from __doc__
        """
        Return a hexadecimal representation of a floating-point number.
        
        >>> (-0.1).hex()
        '-0x1.999999999999ap-4'
        >>> 3.14159.hex()
        '0x1.921f9f01b866ep+1'
        """
        pass

    def is_integer(self, *args, **kwargs): # real signature unknown
        """ Return True if the float is an integer. """
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

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ Formats the float according to format_spec. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    @classmethod
    def __getformat__(cls, *args, **kwargs): # real signature unknown
        """
        You probably don't want to use this function.
        
          typestr
            Must be 'double' or 'float'.
        
        It exists mainly to be used in Python's test suite.
        
        This function returns whichever of 'unknown', 'IEEE, big-endian' or 'IEEE,
        little-endian' best describes the format of floating point numbers used by the
        C type named by typestr.
        """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
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

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
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

    def __round__(self, *args, **kwargs): # real signature unknown
        """
        Return the Integral closest to x, rounding half toward even.
        
        When an argument is passed, work like built-in round(x, ndigits).
        """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    @classmethod
    def __set_format__(cls, *args, **kwargs): # real signature unknown
        """
        You probably don't want to use this function.
        
          typestr
            Must be 'double' or 'float'.
          fmt
            Must be one of 'unknown', 'IEEE, big-endian' or 'IEEE, little-endian',
            and in addition can only be one of the latter two if it appears to
            match the underlying C reality.
        
        It exists mainly to be used in Python's test suite.
        
        Override the automatic determination of C-level floating point type.
        This affects how floats are converted to and from binary strings.
        """
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

    def __trunc__(self, *args, **kwargs): # real signature unknown
        """ Return the Integral closest to x between 0 and x. """
        pass

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""



class OperationalError(DatabaseError):
    """
    Exception raised for errors that are related to the database's operation and
    not necessarily under the control of the programmer, e.g. an unexpected
    disconnect occurs, the data source name is not found, a transaction could not
    be processed, a memory allocation error occurred during processing, etc.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class ProgrammingError(DatabaseError):
    """
    Exception raised for programming errors, e.g. table not found or already
    exists, syntax error in the SQL statement, wrong number of parameters
    specified, etc.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Row(object):
    """
    Row objects are sequence objects that hold query results.
    
    They are similar to tuples in that they cannot be resized and new attributes
    cannot be added, but individual elements can be replaced.  This allows data to
    be "fixed up" after being fetched.  (For example, datetimes may be replaced by
    those with time zones attached.)
    
      row[0] = row[0].replace(tzinfo=timezone)
      print row[0]
    
    Additionally, individual values can be optionally be accessed or replaced by
    name.  Non-alphanumeric characters are replaced with an underscore.
    
      cursor.execute("select customer_id, [Name With Spaces] from tmp")
      row = cursor.fetchone()
      print row.customer_id, row.Name_With_Spaces
    
    If using this non-standard feature, it is often convenient to specifiy the name
    using the SQL 'as' keyword:
    
      cursor.execute("select count(*) as total from tmp")
      row = cursor.fetchone()
      print row.total
    """
    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
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

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    cursor_description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Cursor.description sequence from the Cursor that created this row."""


    __hash__ = None


class ROWID(object):
    """
    int([x]) -> integer
    int(x, base=10) -> integer
    
    Convert a number or string to an integer, or return 0 if no arguments
    are given.  If x is a number, return x.__int__().  For floating point
    numbers, this truncates towards zero.
    
    If x is not a number or if base is given, then x must be a string,
    bytes, or bytearray instance representing an integer literal in the
    given base.  The literal can be preceded by '+' or '-' and be surrounded
    by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
    Base 0 means to interpret the base from the string as an integer literal.
    >>> int('0b100', base=0)
    4
    """
    def bit_length(self): # real signature unknown; restored from __doc__
        """
        Number of bits necessary to represent self in binary.
        
        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Returns self, the complex conjugate of any int. """
        pass

    @classmethod
    def from_bytes(cls, *args, **kwargs): # real signature unknown
        """
        Return the integer represented by the given array of bytes.
        
          bytes
            Holds the array of bytes to convert.  The argument must either
            support the buffer protocol or be an iterable object producing bytes.
            Bytes and bytearray are examples of built-in objects that support the
            buffer protocol.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Indicates whether two's complement is used to represent the integer.
        """
        pass

    def to_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return an array of bytes representing an integer.
        
          length
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Determines whether two's complement is used to represent the integer.
            If signed is False and a negative integer is given, an OverflowError
            is raised.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        """ Ceiling of an Integral returns itself. """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs): # real signature unknown
        """ Flooring an Integral returns itself. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
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

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        """
        Rounding an Integral returns itself.
        Rounding with an ndigits argument also returns an integer.
        """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Returns size in memory, in bytes. """
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

    def __trunc__(self, *args, **kwargs): # real signature unknown
        """ Truncating an Integral returns itself. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the denominator of a rational number in lowest terms"""

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""



class STRING(object):
    """
    str(object='') -> str
    str(bytes_or_buffer[, encoding[, errors]]) -> str
    
    Create a new string object from the given object. If encoding or
    errors is specified, then the object must expose a data buffer
    that will be decoded using the given encoding and error handler.
    Otherwise, returns the result of object.__str__() (if defined)
    or repr(object).
    encoding defaults to sys.getdefaultencoding().
    errors defaults to 'strict'.
    """
    def capitalize(self, *args, **kwargs): # real signature unknown
        """
        Return a capitalized version of the string.
        
        More specifically, make the first character have upper case and the rest lower
        case.
        """
        pass

    def casefold(self, *args, **kwargs): # real signature unknown
        """ Return a version of the string suitable for caseless comparisons. """
        pass

    def center(self, *args, **kwargs): # real signature unknown
        """
        Return a centered string of length width.
        
        Padding is done using the specified fill character (default is a space).
        """
        pass

    def count(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.count(sub[, start[, end]]) -> int
        
        Return the number of non-overlapping occurrences of substring sub in
        string S[start:end].  Optional arguments start and end are
        interpreted as in slice notation.
        """
        return 0

    def encode(self, *args, **kwargs): # real signature unknown
        """
        Encode the string using the codec registered for encoding.
        
          encoding
            The encoding in which to encode the string.
          errors
            The error handling scheme to use for encoding errors.
            The default is 'strict' meaning that encoding errors raise a
            UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
            'xmlcharrefreplace' as well as any other name registered with
            codecs.register_error that can handle UnicodeEncodeErrors.
        """
        pass

    def endswith(self, suffix, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.endswith(suffix[, start[, end]]) -> bool
        
        Return True if S ends with the specified suffix, False otherwise.
        With optional start, test S beginning at that position.
        With optional end, stop comparing S at that position.
        suffix can also be a tuple of strings to try.
        """
        return False

    def expandtabs(self, *args, **kwargs): # real signature unknown
        """
        Return a copy where all tab characters are expanded using spaces.
        
        If tabsize is not given, a tab size of 8 characters is assumed.
        """
        pass

    def find(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.find(sub[, start[, end]]) -> int
        
        Return the lowest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
        """
        return 0

    def format(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        S.format(*args, **kwargs) -> str
        
        Return a formatted version of S, using substitutions from args and kwargs.
        The substitutions are identified by braces ('{' and '}').
        """
        return ""

    def format_map(self, mapping): # real signature unknown; restored from __doc__
        """
        S.format_map(mapping) -> str
        
        Return a formatted version of S, using substitutions from mapping.
        The substitutions are identified by braces ('{' and '}').
        """
        return ""

    def index(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.index(sub[, start[, end]]) -> int
        
        Return the lowest index in S where substring sub is found, 
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Raises ValueError when the substring is not found.
        """
        return 0

    def isalnum(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is an alpha-numeric string, False otherwise.
        
        A string is alpha-numeric if all characters in the string are alpha-numeric and
        there is at least one character in the string.
        """
        pass

    def isalpha(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is an alphabetic string, False otherwise.
        
        A string is alphabetic if all characters in the string are alphabetic and there
        is at least one character in the string.
        """
        pass

    def isascii(self, *args, **kwargs): # real signature unknown
        """
        Return True if all characters in the string are ASCII, False otherwise.
        
        ASCII characters have code points in the range U+0000-U+007F.
        Empty string is ASCII too.
        """
        pass

    def isdecimal(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is a decimal string, False otherwise.
        
        A string is a decimal string if all characters in the string are decimal and
        there is at least one character in the string.
        """
        pass

    def isdigit(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is a digit string, False otherwise.
        
        A string is a digit string if all characters in the string are digits and there
        is at least one character in the string.
        """
        pass

    def isidentifier(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is a valid Python identifier, False otherwise.
        
        Use keyword.iskeyword() to test for reserved identifiers such as "def" and
        "class".
        """
        pass

    def islower(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is a lowercase string, False otherwise.
        
        A string is lowercase if all cased characters in the string are lowercase and
        there is at least one cased character in the string.
        """
        pass

    def isnumeric(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is a numeric string, False otherwise.
        
        A string is numeric if all characters in the string are numeric and there is at
        least one character in the string.
        """
        pass

    def isprintable(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is printable, False otherwise.
        
        A string is printable if all of its characters are considered printable in
        repr() or if it is empty.
        """
        pass

    def isspace(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is a whitespace string, False otherwise.
        
        A string is whitespace if all characters in the string are whitespace and there
        is at least one character in the string.
        """
        pass

    def istitle(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is a title-cased string, False otherwise.
        
        In a title-cased string, upper- and title-case characters may only
        follow uncased characters and lowercase characters only cased ones.
        """
        pass

    def isupper(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is an uppercase string, False otherwise.
        
        A string is uppercase if all cased characters in the string are uppercase and
        there is at least one cased character in the string.
        """
        pass

    def join(self, ab=None, pq=None, rs=None): # real signature unknown; restored from __doc__
        """
        Concatenate any number of strings.
        
        The string whose method is called is inserted in between each given string.
        The result is returned as a new string.
        
        Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
        """
        pass

    def ljust(self, *args, **kwargs): # real signature unknown
        """
        Return a left-justified string of length width.
        
        Padding is done using the specified fill character (default is a space).
        """
        pass

    def lower(self, *args, **kwargs): # real signature unknown
        """ Return a copy of the string converted to lowercase. """
        pass

    def lstrip(self, *args, **kwargs): # real signature unknown
        """
        Return a copy of the string with leading whitespace removed.
        
        If chars is given and not None, remove characters in chars instead.
        """
        pass

    def maketrans(self, *args, **kwargs): # real signature unknown
        """
        Return a translation table usable for str.translate().
        
        If there is only one argument, it must be a dictionary mapping Unicode
        ordinals (integers) or characters to Unicode ordinals, strings or None.
        Character keys will be then converted to ordinals.
        If there are two arguments, they must be strings of equal length, and
        in the resulting dictionary, each character in x will be mapped to the
        character at the same position in y. If there is a third argument, it
        must be a string, whose characters will be mapped to None in the result.
        """
        pass

    def partition(self, *args, **kwargs): # real signature unknown
        """
        Partition the string into three parts using the given separator.
        
        This will search for the separator in the string.  If the separator is found,
        returns a 3-tuple containing the part before the separator, the separator
        itself, and the part after it.
        
        If the separator is not found, returns a 3-tuple containing the original string
        and two empty strings.
        """
        pass

    def replace(self, *args, **kwargs): # real signature unknown
        """
        Return a copy with all occurrences of substring old replaced by new.
        
          count
            Maximum number of occurrences to replace.
            -1 (the default value) means replace all occurrences.
        
        If the optional argument count is given, only the first count occurrences are
        replaced.
        """
        pass

    def rfind(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.rfind(sub[, start[, end]]) -> int
        
        Return the highest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
        """
        return 0

    def rindex(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.rindex(sub[, start[, end]]) -> int
        
        Return the highest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Raises ValueError when the substring is not found.
        """
        return 0

    def rjust(self, *args, **kwargs): # real signature unknown
        """
        Return a right-justified string of length width.
        
        Padding is done using the specified fill character (default is a space).
        """
        pass

    def rpartition(self, *args, **kwargs): # real signature unknown
        """
        Partition the string into three parts using the given separator.
        
        This will search for the separator in the string, starting at the end. If
        the separator is found, returns a 3-tuple containing the part before the
        separator, the separator itself, and the part after it.
        
        If the separator is not found, returns a 3-tuple containing two empty strings
        and the original string.
        """
        pass

    def rsplit(self, *args, **kwargs): # real signature unknown
        """
        Return a list of the words in the string, using sep as the delimiter string.
        
          sep
            The delimiter according which to split the string.
            None (the default value) means split according to any whitespace,
            and discard empty strings from the result.
          maxsplit
            Maximum number of splits to do.
            -1 (the default value) means no limit.
        
        Splits are done starting at the end of the string and working to the front.
        """
        pass

    def rstrip(self, *args, **kwargs): # real signature unknown
        """
        Return a copy of the string with trailing whitespace removed.
        
        If chars is given and not None, remove characters in chars instead.
        """
        pass

    def split(self, *args, **kwargs): # real signature unknown
        """
        Return a list of the words in the string, using sep as the delimiter string.
        
          sep
            The delimiter according which to split the string.
            None (the default value) means split according to any whitespace,
            and discard empty strings from the result.
          maxsplit
            Maximum number of splits to do.
            -1 (the default value) means no limit.
        """
        pass

    def splitlines(self, *args, **kwargs): # real signature unknown
        """
        Return a list of the lines in the string, breaking at line boundaries.
        
        Line breaks are not included in the resulting list unless keepends is given and
        true.
        """
        pass

    def startswith(self, prefix, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.startswith(prefix[, start[, end]]) -> bool
        
        Return True if S starts with the specified prefix, False otherwise.
        With optional start, test S beginning at that position.
        With optional end, stop comparing S at that position.
        prefix can also be a tuple of strings to try.
        """
        return False

    def strip(self, *args, **kwargs): # real signature unknown
        """
        Return a copy of the string with leading and trailing whitespace remove.
        
        If chars is given and not None, remove characters in chars instead.
        """
        pass

    def swapcase(self, *args, **kwargs): # real signature unknown
        """ Convert uppercase characters to lowercase and lowercase characters to uppercase. """
        pass

    def title(self, *args, **kwargs): # real signature unknown
        """
        Return a version of the string where each word is titlecased.
        
        More specifically, words start with uppercased characters and all remaining
        cased characters have lower case.
        """
        pass

    def translate(self, *args, **kwargs): # real signature unknown
        """
        Replace each character in the string using the given translation table.
        
          table
            Translation table, which must be a mapping of Unicode ordinals to
            Unicode ordinals, strings, or None.
        
        The table must implement lookup/indexing via __getitem__, for instance a
        dictionary or list.  If this operation raises LookupError, the character is
        left untouched.  Characters mapped to None are deleted.
        """
        pass

    def upper(self, *args, **kwargs): # real signature unknown
        """ Return a copy of the string converted to uppercase. """
        pass

    def zfill(self, *args, **kwargs): # real signature unknown
        """
        Pad a numeric string with zeros on the left, to fill a field of the given width.
        
        The string is never truncated.
        """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ Return a formatted version of the string as described by format_spec. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
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

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Return the size of the string in memory, in bytes. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass


class Time(object):
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


class Warning(Exception):
    """
    Exception raised for important warnings like data truncations while inserting,
     etc.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

BinaryNull = None # (!) real value is '<pyodbc.NullParam object at 0x000001D8EDB7E3A0>'

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001D8F0095630>'

__spec__ = None # (!) real value is "ModuleSpec(name='pyodbc', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001D8F0095630>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\pyodbc.cp37-win_amd64.pyd')"

