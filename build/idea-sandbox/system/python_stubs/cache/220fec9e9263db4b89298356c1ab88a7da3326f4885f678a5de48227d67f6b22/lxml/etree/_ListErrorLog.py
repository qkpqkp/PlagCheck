# encoding: utf-8
# module lxml.etree
# from C:\Users\Doly\Anaconda3\lib\site-packages\lxml\etree.cp37-win_amd64.pyd
# by generator 1.147
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from ._BaseErrorLog import _BaseErrorLog

class _ListErrorLog(_BaseErrorLog):
    """ Immutable base version of a list based error log. """
    def copy(self, *args, **kwargs): # real signature unknown
        """
        Creates a shallow copy of this error log.  Reuses the list of
                entries.
        """
        pass

    def filter_domains(self, *args, **kwargs): # real signature unknown
        """
        Filter the errors by the given domains and return a new error log
                containing the matches.
        """
        pass

    def filter_from_errors(self): # real signature unknown; restored from __doc__
        """
        filter_from_errors(self)
        
                Convenience method to get all error messages or worse.
        """
        pass

    def filter_from_fatals(self): # real signature unknown; restored from __doc__
        """
        filter_from_fatals(self)
        
                Convenience method to get all fatal error messages.
        """
        pass

    def filter_from_level(self, level): # real signature unknown; restored from __doc__
        """
        filter_from_level(self, level)
        
                Return a log with all messages of the requested level of worse.
        """
        pass

    def filter_from_warnings(self): # real signature unknown; restored from __doc__
        """
        filter_from_warnings(self)
        
                Convenience method to get all warnings or worse.
        """
        pass

    def filter_levels(self, levels): # real signature unknown; restored from __doc__
        """
        filter_levels(self, levels)
        
                Filter the errors by the given error levels and return a new
                error log containing the matches.
        """
        pass

    def filter_types(self, types): # real signature unknown; restored from __doc__
        """
        filter_types(self, types)
        
                Filter the errors by the given types and return a new error
                log containing the matches.
        """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002467EEF81E0>'


