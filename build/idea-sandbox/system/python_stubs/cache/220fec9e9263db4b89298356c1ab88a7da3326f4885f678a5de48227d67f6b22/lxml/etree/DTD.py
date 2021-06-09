# encoding: utf-8
# module lxml.etree
# from C:\Users\Doly\Anaconda3\lib\site-packages\lxml\etree.cp37-win_amd64.pyd
# by generator 1.147
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from ._Validator import _Validator

class DTD(_Validator):
    """
    DTD(self, file=None, external_id=None)
        A DTD validator.
    
        Can load from filesystem directly given a filename or file-like object.
        Alternatively, pass the keyword parameter ``external_id`` to load from a
        catalog.
    """
    def elements(self, *args, **kwargs): # real signature unknown
        pass

    def entities(self, *args, **kwargs): # real signature unknown
        pass

    def iterelements(self, *args, **kwargs): # real signature unknown
        pass

    def iterentities(self, *args, **kwargs): # real signature unknown
        pass

    def __call__(self, etree): # real signature unknown; restored from __doc__
        """
        __call__(self, etree)
        
                Validate doc using the DTD.
        
                Returns true if the document is valid, false if not.
        """
        pass

    def __init__(self, file=None, external_id=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    external_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    system_url = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002467EF171B0>'


