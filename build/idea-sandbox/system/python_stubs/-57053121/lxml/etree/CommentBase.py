# encoding: utf-8
# module lxml.etree
# from C:\Users\Doly\Anaconda3\lib\site-packages\lxml\etree.cp37-win_amd64.pyd
# by generator 1.147
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from ._Comment import _Comment

class CommentBase(_Comment):
    """
    All custom Comment classes must inherit from this one.
    
        To create an XML Comment instance, use the ``Comment()`` factory.
    
        Subclasses *must not* override __init__ or __new__ as it is
        absolutely undefined when these objects will be created or
        destroyed.  All persistent state of Comments must be stored in the
        underlying XML.  If you really need to initialize the object after
        creation, you can implement an ``_init(self)`` method that will be
        called after object creation.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002467EEF8780>'


