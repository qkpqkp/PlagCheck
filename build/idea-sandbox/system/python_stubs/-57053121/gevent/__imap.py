# encoding: utf-8
# module gevent.__imap
# from C:\Users\Doly\Anaconda3\lib\site-packages\gevent\__imap.cp37-win_amd64.pyd
# by generator 1.147
""" Iterators across greenlets or AsyncResult objects. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import gevent.__semaphore as _semaphore # C:\Users\Doly\Anaconda3\lib\site-packages\gevent\__semaphore.cp37-win_amd64.pyd
import gevent._queue as queue # C:\Users\Doly\Anaconda3\lib\site-packages\gevent\_queue.cp37-win_amd64.pyd
from gevent._greenlet import Greenlet

from gevent._queue import UnboundQueue

from gevent.__semaphore import Semaphore

import gevent._greenlet as __gevent__greenlet


# functions

def import_c_accel(globs, cname): # reliably restored by inspect
    """
    Import the C-accelerator for the __name__
        and copy its globals.
    """
    pass

# classes

class Failure(object):
    """ Failure(exc, raise_exception=None) """
    def __init__(self, exc, raise_exception=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    exc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __slots__ = (
        'exc',
        'raise_exception',
    )


class IMapUnordered(__gevent__greenlet.Greenlet):
    """
    IMapUnordered(func, iterable, spawn, maxsize=None, _zipped=False)
    
        At iterator of map results.
    """
    def next(self, *args, **kwargs): # real signature unknown
        pass

    def _on_result(self, greenlet): # real signature unknown; restored from __doc__
        """ IMapUnordered._on_result(self, greenlet) """
        pass

    def _run(self): # real signature unknown; restored from __doc__
        """ IMapUnordered._run(self) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """
        An iterator that.
        
                :param callable spawn: The function we use to create new greenlets.
                :keyword int maxsize: If given and not-None, specifies the maximum number of
                    finished results that will be allowed to accumulated awaiting the reader;
                    more than that number of results will cause map function greenlets to begin
                    to block. This is most useful is there is a great disparity in the speed of
                    the mapping code and the consumer and the results consume a great deal of resources.
                    Using a bound is more computationally expensive than not using a bound.
        
                .. versionchanged:: 1.1b3
                    Added the *maxsize* parameter.
        """
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

    finished = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    queue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001F0126F55A0>'


class IMap(IMapUnordered):
    """ IMap(*args, **kwargs) """
    def __init__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001F0126F55D0>'


# variables with complex values

__all__ = [
    'IMapUnordered',
    'IMap',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001F0127E1048>'

__pyx_capi__ = {
    '_raise_exc': None, # (!) real value is '<capsule object "PyObject *(struct __pyx_obj_6gevent_6__imap_Failure *)" at 0x000001F012689750>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='gevent.__imap', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001F0127E1048>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\gevent\\\\__imap.cp37-win_amd64.pyd')"

__test__ = {}

