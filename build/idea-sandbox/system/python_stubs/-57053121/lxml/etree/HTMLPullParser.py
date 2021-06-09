# encoding: utf-8
# module lxml.etree
# from C:\Users\Doly\Anaconda3\lib\site-packages\lxml\etree.cp37-win_amd64.pyd
# by generator 1.147
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from .HTMLParser import HTMLParser

class HTMLPullParser(HTMLParser):
    """
    HTMLPullParser(self, events=None, *, tag=None, base_url=None, **kwargs)
    
        HTML parser that collects parse events in an iterator.
    
        The collected events are the same as for iterparse(), but the
        parser itself is non-blocking in the sense that it receives
        data chunks incrementally through its .feed() method, instead
        of reading them directly from a file(-like) object all by itself.
    
        By default, it collects Element end events.  To change that,
        pass any subset of the available events into the ``events``
        argument: ``'start'``, ``'end'``, ``'start-ns'``,
        ``'end-ns'``, ``'comment'``, ``'pi'``.
    
        To support loading external dependencies relative to the input
        source, you can pass the ``base_url``.
    """
    def read_events(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, events=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002467EEF8C00>'


