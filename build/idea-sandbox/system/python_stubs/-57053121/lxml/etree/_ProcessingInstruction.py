# encoding: utf-8
# module lxml.etree
# from C:\Users\Doly\Anaconda3\lib\site-packages\lxml\etree.cp37-win_amd64.pyd
# by generator 1.147
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from .__ContentOnlyElement import __ContentOnlyElement

class _ProcessingInstruction(__ContentOnlyElement):
    # no doc
    def get(self, key, default=None): # real signature unknown; restored from __doc__
        """
        get(self, key, default=None)
        
                Try to parse pseudo-attributes from the text content of the
                processing instruction, search for one with the given key as
                name and return its associated value.
        
                Note that this is only a convenience method for the most
                common case that all text content is structured in
                attribute-like name-value pairs with properly quoted values.
                It is not guaranteed to work for all possible text content.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    attrib = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns a dict containing all pseudo-attributes that can be
        parsed from the text content of this processing instruction.
        Note that modifying the dict currently has no effect on the
        XML node, although this is not guaranteed to stay this way.
        """

    tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    target = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002467EEF83C0>'


