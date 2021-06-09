# encoding: utf-8
# module lxml.etree
# from C:\Users\Doly\Anaconda3\lib\site-packages\lxml\etree.cp37-win_amd64.pyd
# by generator 1.147
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from ._Validator import _Validator

class XMLSchema(_Validator):
    """
    XMLSchema(self, etree=None, file=None)
        Turn a document into an XML Schema validator.
    
        Either pass a schema as Element or ElementTree, or pass a file or
        filename through the ``file`` keyword argument.
    
        Passing the ``attribute_defaults`` boolean option will make the
        schema insert default/fixed attributes into validated documents.
    """
    def __call__(self, etree): # real signature unknown; restored from __doc__
        """
        __call__(self, etree)
        
                Validate doc using XML Schema.
        
                Returns true if document is valid, false if not.
        """
        pass

    def __init__(self, etree=None, file=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002467EF17210>'


