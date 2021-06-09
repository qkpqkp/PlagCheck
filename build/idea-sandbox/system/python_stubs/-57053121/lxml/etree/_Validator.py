# encoding: utf-8
# module lxml.etree
# from C:\Users\Doly\Anaconda3\lib\site-packages\lxml\etree.cp37-win_amd64.pyd
# by generator 1.147
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from .object import object

class _Validator(object):
    """ Base class for XML validators. """
    def assertValid(self, etree): # real signature unknown; restored from __doc__
        """
        assertValid(self, etree)
        
                Raises `DocumentInvalid` if the document does not comply with the schema.
        """
        pass

    def assert_(self, etree): # real signature unknown; restored from __doc__
        """
        assert_(self, etree)
        
                Raises `AssertionError` if the document does not comply with the schema.
        """
        pass

    def validate(self, etree): # real signature unknown; restored from __doc__
        """
        validate(self, etree)
        
                Validate the document using this schema.
        
                Returns true if document is valid, false if not.
        """
        pass

    def _append_log_message(self, *args, **kwargs): # real signature unknown
        pass

    def _clear_error_log(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    error_log = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The log of validation errors and warnings."""


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002467EF17180>'


