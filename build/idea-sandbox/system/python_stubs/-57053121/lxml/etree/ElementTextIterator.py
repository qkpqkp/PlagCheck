# encoding: utf-8
# module lxml.etree
# from C:\Users\Doly\Anaconda3\lib\site-packages\lxml\etree.cp37-win_amd64.pyd
# by generator 1.147
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from .object import object

class ElementTextIterator(object):
    """
    ElementTextIterator(self, element, tag=None, with_tail=True)
        Iterates over the text content of a subtree.
    
        You can pass the ``tag`` keyword argument to restrict text content to a
        specific tag name.
    
        You can set the ``with_tail`` keyword argument to ``False`` to skip over
        tail text (e.g. if you know that it's only whitespace from pretty-printing).
    """
    def __init__(self, element, tag=None, with_tail=True): # real signature unknown; restored from __doc__
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


