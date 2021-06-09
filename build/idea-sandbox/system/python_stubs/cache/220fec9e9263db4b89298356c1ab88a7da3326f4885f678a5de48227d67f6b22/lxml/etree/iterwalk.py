# encoding: utf-8
# module lxml.etree
# from C:\Users\Doly\Anaconda3\lib\site-packages\lxml\etree.cp37-win_amd64.pyd
# by generator 1.147
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from .object import object

class iterwalk(object):
    """
    iterwalk(self, element_or_tree, events=("end",), tag=None)
    
        A tree walker that generates events from an existing tree as if it
        was parsing XML data with ``iterparse()``.
    
        Just as for ``iterparse()``, the ``tag`` argument can be a single tag or a
        sequence of tags.
    
        After receiving a 'start' or 'start-ns' event, the children and
        descendants of the current element can be excluded from iteration
        by calling the ``skip_subtree()`` method.
    """
    def skip_subtree(self, *args, **kwargs): # real signature unknown
        """
        Prevent descending into the current subtree.
                Instead, the next returned event will be the 'end' event of the current element
                (if included), ignoring any children or descendants.
        
                This has no effect right after an 'end' or 'end-ns' event.
        """
        pass

    def __init__(self, element_or_tree, events=None, tag=None): # real signature unknown; restored from __doc__
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

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002467EEF8E10>'


