# encoding: utf-8
# module gevent.__semaphore
# from C:\Users\Doly\Anaconda3\lib\site-packages\gevent\__semaphore.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
from gevent.__abstract_linkable import AbstractLinkable

import gevent.__abstract_linkable as __gevent___abstract_linkable


# functions

def import_c_accel(globs, cname): # reliably restored by inspect
    """
    Import the C-accelerator for the __name__
        and copy its globals.
    """
    pass

# classes

class Semaphore(__gevent___abstract_linkable.AbstractLinkable):
    """
    Semaphore(value=1)
    
        Semaphore(value=1) -> Semaphore
    
        A semaphore manages a counter representing the number of release()
        calls minus the number of acquire() calls, plus an initial value.
        The acquire() method blocks if necessary until it can return
        without making the counter negative.
    
        If not given, ``value`` defaults to 1.
    
        The semaphore is a context manager and can be used in ``with`` statements.
    
        This Semaphore's ``__exit__`` method does not call the trace function
        on CPython, but does under PyPy.
    
        .. seealso:: :class:`BoundedSemaphore` for a safer version that prevents
           some classes of bugs.
    
        .. versionchanged:: 1.4.0
    
            The order in which waiters are awakened is not specified. It was not
            specified previously, but usually went in FIFO order.
    """
    def acquire(self, int_blocking=True, timeout=None): # real signature unknown; restored from __doc__
        """
        Semaphore.acquire(self, int blocking=True, timeout=None) -> bool
        
                acquire(blocking=True, timeout=None) -> bool
        
                Acquire the semaphore.
        
                .. caution:: If this semaphore was initialized with a size of 0,
                   this method will block forever (unless a timeout is given or blocking is
                   set to false).
        
                :keyword bool blocking: If True (the default), this function will block
                   until the semaphore is acquired.
                :keyword float timeout: If given, specifies the maximum amount of seconds
                   this method will block.
                :return: A boolean indicating whether the semaphore was acquired.
                   If ``blocking`` is True and ``timeout`` is None (the default), then
                   (so long as this semaphore was initialized with a size greater than 0)
                   this will always return True. If a timeout was given, and it expired before
                   the semaphore was acquired, False will be returned. (Note that this can still
                   raise a ``Timeout`` exception, if some other caller had already started a timer.)
        """
        return False

    def locked(self): # real signature unknown; restored from __doc__
        """
        Semaphore.locked(self) -> bool
        Return a boolean indicating whether the semaphore can be acquired.
                Most useful with binary semaphores.
        """
        return False

    def ready(self): # real signature unknown; restored from __doc__
        """ Semaphore.ready(self) -> bool """
        return False

    def release(self): # real signature unknown; restored from __doc__
        """
        Semaphore.release(self) -> int
        
                Release the semaphore, notifying any waiters if needed.
        """
        return 0

    def wait(self, timeout=None): # real signature unknown; restored from __doc__
        """
        Semaphore.wait(self, timeout=None) -> int
        
                wait(timeout=None) -> int
        
                Wait until it is possible to acquire this semaphore, or until the optional
                *timeout* elapses.
        
                .. caution:: If this semaphore was initialized with a size of 0,
                   this method will block forever if no timeout is given.
        
                :keyword float timeout: If given, specifies the maximum amount of seconds
                   this method will block.
                :return: A number indicating how many times the semaphore can be acquired
                    before blocking.
        """
        return 0

    def _py3k_acquire(self, *args, **kwargs): # real signature unknown
        """
        Semaphore.acquire(self, int blocking=True, timeout=None) -> bool
        
                acquire(blocking=True, timeout=None) -> bool
        
                Acquire the semaphore.
        
                .. caution:: If this semaphore was initialized with a size of 0,
                   this method will block forever (unless a timeout is given or blocking is
                   set to false).
        
                :keyword bool blocking: If True (the default), this function will block
                   until the semaphore is acquired.
                :keyword float timeout: If given, specifies the maximum amount of seconds
                   this method will block.
                :return: A boolean indicating whether the semaphore was acquired.
                   If ``blocking`` is True and ``timeout`` is None (the default), then
                   (so long as this semaphore was initialized with a size greater than 0)
                   this will always return True. If a timeout was given, and it expired before
                   the semaphore was acquired, False will be returned. (Note that this can still
                   raise a ``Timeout`` exception, if some other caller had already started a timer.)
        """
        pass

    def _start_notify(self): # real signature unknown; restored from __doc__
        """ Semaphore._start_notify(self) """
        pass

    def __enter__(self): # real signature unknown; restored from __doc__
        """ Semaphore.__enter__(self) """
        pass

    def __exit__(self, t, v, tb): # real signature unknown; restored from __doc__
        """ Semaphore.__exit__(self, t, v, tb) """
        pass

    def __init__(self, value=1): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    counter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """counter: 'int'"""


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000025C3C095690>'


class BoundedSemaphore(Semaphore):
    """
    BoundedSemaphore(*args, **kwargs)
    
        BoundedSemaphore(value=1) -> BoundedSemaphore
    
        A bounded semaphore checks to make sure its current value doesn't
        exceed its initial value. If it does, :class:`ValueError` is
        raised. In most situations semaphores are used to guard resources
        with limited capacity. If the semaphore is released too many times
        it's a sign of a bug.
    
        If not given, *value* defaults to 1.
    """
    def release(self): # real signature unknown; restored from __doc__
        """ BoundedSemaphore.release(self) -> int """
        return 0

    def __init__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    _initial_value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    _OVER_RELEASE_ERROR = ValueError
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000025C3C0956C0>'


# variables with complex values

__all__ = [
    'Semaphore',
    'BoundedSemaphore',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000025C3C1261D0>'

__pyx_capi__ = {
    'Timeout': None, # (!) real value is '<capsule object "PyObject *" at 0x0000025C3BFE9750>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='gevent.__semaphore', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000025C3C1261D0>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\gevent\\\\__semaphore.cp37-win_amd64.pyd')"

__test__ = {}

