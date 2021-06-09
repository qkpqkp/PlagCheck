# encoding: utf-8
# module lxml.etree
# from C:\Users\Doly\Anaconda3\lib\site-packages\lxml\etree.cp37-win_amd64.pyd
# by generator 1.147
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from .FallbackElementClassLookup import FallbackElementClassLookup

class CustomElementClassLookup(FallbackElementClassLookup):
    """
    CustomElementClassLookup(self, fallback=None)
        Element class lookup based on a subclass method.
    
        You can inherit from this class and override the method::
    
            lookup(self, type, doc, namespace, name)
    
        to lookup the element class for a node. Arguments of the method:
        * type:      one of 'element', 'comment', 'PI', 'entity'
        * doc:       document that the node is in
        * namespace: namespace URI of the node (or None for comments/PIs/entities)
        * name:      name of the element/entity, None for comments, target for PIs
    
        If you return None from this method, the fallback will be called.
    """
    def lookup(self, type, doc, namespace, name): # real signature unknown; restored from __doc__
        """ lookup(self, type, doc, namespace, name) """
        pass

    def __init__(self, fallback=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002467EEF88A0>'


