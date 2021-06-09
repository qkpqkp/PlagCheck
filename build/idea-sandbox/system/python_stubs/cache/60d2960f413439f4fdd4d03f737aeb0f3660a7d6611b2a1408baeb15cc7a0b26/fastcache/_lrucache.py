# encoding: utf-8
# module fastcache._lrucache
# from C:\Users\Doly\Anaconda3\lib\site-packages\fastcache\_lrucache.cp37-win_amd64.pyd
# by generator 1.147
""" Least Recently Used cache """
# no imports

# functions

def clru_cache(maxsize=128, typed=False, state=None, unhashable='error'): # real signature unknown; restored from __doc__
    """
    clru_cache(maxsize=128, typed=False, state=None, unhashable='error')
    
    Least-recently-used cache decorator.
    
    If *maxsize* is set to None, the LRU features are disabled and the
    cache can grow without bound.
    
    If *typed* is True, arguments of different types will be cached
    separately.  For example, f(3.0) and f(3) will be treated as distinct
    calls with distinct results.
    
    If *state* is a list or dict, the items will be incorporated into the
    argument hash.
    
    The result of calling the cached function with unhashable (mutable)
    arguments depends on the value of *unhashable*:
    
        If *unhashable* is 'error', a TypeError will be raised.
    
        If *unhashable* is 'warning', a UserWarning will be raised, and
        the wrapped function will be called with the supplied arguments.
        A miss will be recorded in the cache statistics.
    
        If *unhashable* is 'ignore', the wrapped function will be called
        with the supplied arguments. A miss will will be recorded in
        the cache statistics.
    
    View the cache statistics named tuple (hits, misses, maxsize, currsize)
    with f.cache_info().  Clear the cache and statistics with
    f.cache_clear(). Access the underlying function with f.__wrapped__.
    
    See:  http://en.wikipedia.org/wiki/Cache_algorithms#Least_Recently_Used
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001C75748BDD8>'

__spec__ = None # (!) real value is "ModuleSpec(name='fastcache._lrucache', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001C75748BDD8>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\fastcache\\\\_lrucache.cp37-win_amd64.pyd')"

