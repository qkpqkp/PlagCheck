# encoding: utf-8
# module lxml.etree
# from C:\Users\Doly\Anaconda3\lib\site-packages\lxml\etree.cp37-win_amd64.pyd
# by generator 1.147
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from .object import object

class _LogEntry(object):
    """
    A log message entry from an error log.
    
        Attributes:
    
        - message: the message text
        - domain: the domain ID (see lxml.etree.ErrorDomains)
        - type: the message type ID (see lxml.etree.ErrorTypes)
        - level: the log level ID (see lxml.etree.ErrorLevels)
        - line: the line at which the message originated (if applicable)
        - column: the character column at which the message originated (if applicable)
        - filename: the name of the file in which the message originated (if applicable)
        - path: the location in which the error was found (if available)
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    column = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    domain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    domain_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the error domain.  See lxml.etree.ErrorDomains
        """

    filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The file path where the report originated, if any.
        """

    level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    level_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the error level.  See lxml.etree.ErrorLevels
        """

    line = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The log message string.
        """

    path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The XPath for the node where the error was detected.
        """

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the error type.  See lxml.etree.ErrorTypes
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002467EEF8180>'


