# encoding: utf-8
# module lxml.etree
# from C:\Users\Doly\Anaconda3\lib\site-packages\lxml\etree.cp37-win_amd64.pyd
# by generator 1.147
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from .object import object

class ElementDepthFirstIterator(object):
    """
    ElementDepthFirstIterator(self, node, tag=None, inclusive=True)
        Iterates over an element and its sub-elements in document order (depth
        first pre-order).
    
        Note that this also includes comments, entities and processing
        instructions.  To filter them out, check if the ``tag`` property
        of the returned element is a string (i.e. not None and not a
        factory function), or pass the ``Element`` factory for the ``tag``
        argument to receive only Elements.
    
        If the optional ``tag`` argument is not None, the iterator returns only
        the elements that match the respective name and namespace.
    
        The optional boolean argument 'inclusive' defaults to True and can be set
        to False to exclude the start element itself.
    
        Note that the behaviour of this iterator is completely undefined if the
        tree it traverses is modified during iteration.
    """
    def __init__(self, node, tag=None, inclusive=True): # real signature unknown; restored from __doc__
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002467EEF85A0>'


