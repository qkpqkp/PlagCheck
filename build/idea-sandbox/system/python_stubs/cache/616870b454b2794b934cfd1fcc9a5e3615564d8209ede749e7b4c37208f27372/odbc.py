# encoding: utf-8
# module odbc
# from C:\Users\Doly\Anaconda3\lib\site-packages\win32\odbc.pyd
# by generator 1.147
""" A Python wrapper around the ODBC API. """
# no imports

# Variables with simple values

DATE = 'DATE'

NUMBER = 'NUMBER'

RAW = 'RAW'

SQL_FETCH_ABSOLUTE = 5
SQL_FETCH_FIRST = 2

SQL_FETCH_FIRST_SYSTEM = 32
SQL_FETCH_FIRST_USER = 31

SQL_FETCH_LAST = 3
SQL_FETCH_NEXT = 1
SQL_FETCH_PRIOR = 4
SQL_FETCH_RELATIVE = 6

STRING = 'STRING'

# functions

def odbc(*args, **kwargs): # real signature unknown
    pass

def SQLDataSources(*args, **kwargs): # real signature unknown
    pass

# classes

class dataError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class integrityError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class internalError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class noError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class opError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class progError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

TYPES = (
    'STRING',
    'RAW',
    'NUMBER',
    'DATE',
)

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000204C2C15470>'

__spec__ = None # (!) real value is "ModuleSpec(name='odbc', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000204C2C15470>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\win32\\\\odbc.pyd')"

