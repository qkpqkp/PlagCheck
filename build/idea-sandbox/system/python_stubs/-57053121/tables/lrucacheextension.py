# encoding: utf-8
# module tables.lrucacheextension
# from C:\Users\Doly\Anaconda3\lib\site-packages\tables\lrucacheextension.cp37-win_amd64.pyd
# by generator 1.147
"""
Cython interface for several LRU cache systems.

Classes (type extensions):

    NodeCache
    ObjectCache
    NumCache

Functions:

Misc variables:
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import sys as sys # <module 'sys' (built-in)>
import numpy as numpy # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py

# Variables with simple values

DISABLE_EVERY_CYCLES = 10

ENABLE_EVERY_CYCLES = 50

LOWEST_HIT_RATIO = 0.6

# functions

def __pyx_unpickle_NodeCache(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_ObjectNode(*args, **kwargs): # real signature unknown
    pass

# classes

class BaseCache(object):
    """ Base class that implements automatic probing/disabling of the cache. """
    def couldenablecache(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001D436924C60>'


class NodeCache(object):
    """ Least-Recently-Used (LRU) cache for PyTables nodes. """
    def pop(self, *args, **kwargs): # real signature unknown
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """
        Maximum nslots of the cache.
        
            If more than 'nslots' elements are added to the cache,
            the least-recently-used ones will be discarded.
        """
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    nslots = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __marker = None # (!) real value is '<object object at 0x000001D4258BE620>'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001D436924C30>'


class NumCache(BaseCache):
    """ Least-Recently-Used (LRU) cache specific for Numerical data. """
    def getitem(self, *args, **kwargs): # real signature unknown
        pass

    def getslot(self, *args, **kwargs): # real signature unknown
        pass

    def setitem(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """
        Maximum size of the cache.
        
            If more than 'nslots' elements are added to the cache,
            the least-recently-used ones will be discarded.
        
            Parameters:
            shape - The rectangular shape of the cache (nslots, nelemsperslot)
            itemsize - The size of the element base in cache
            name - A descriptive name for this cache
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001D436924CC0>'


class ObjectCache(BaseCache):
    """ Least-Recently-Used (LRU) cache specific for python objects. """
    def getitem(self, *args, **kwargs): # real signature unknown
        pass

    def getslot(self, *args, **kwargs): # real signature unknown
        pass

    def setitem(self, *args, **kwargs): # real signature unknown
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """
        Maximum size of the cache.
        
            If more than 'nslots' elements are added to the cache,
            the least-recently-used ones will be discarded.
        
            Parameters:
            nslots - The number of slots in cache
            name - A descriptive name for this cache
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001D436924C90>'


class ObjectNode(object):
    """ Record of a cached value. Not for public consumption. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001D43694CF60>'

__spec__ = None # (!) real value is "ModuleSpec(name='tables.lrucacheextension', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001D43694CF60>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\tables\\\\lrucacheextension.cp37-win_amd64.pyd')"

__test__ = {}

