# encoding: utf-8
# module gevent.__waiter
# from C:\Users\Doly\Anaconda3\lib\site-packages\gevent\__waiter.cp37-win_amd64.pyd
# by generator 1.147
""" Low-level waiting primitives. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
from gevent.__hub_local import get_hub_noargs

from greenlet import getcurrent


# functions

def greenlet_init(*args, **kwargs): # real signature unknown
    pass

def import_c_accel(globs, cname): # reliably restored by inspect
    """
    Import the C-accelerator for the __name__
        and copy its globals.
    """
    pass

def _init(): # real signature unknown; restored from __doc__
    """ _init() """
    pass

# classes

class Waiter(object):
    """
    Waiter(hub=None)
    
        A low level communication utility for greenlets.
    
        Waiter is a wrapper around greenlet's ``switch()`` and ``throw()`` calls that makes them somewhat safer:
    
        * switching will occur only if the waiting greenlet is executing :meth:`get` method currently;
        * any error raised in the greenlet is handled inside :meth:`switch` and :meth:`throw`
        * if :meth:`switch`/:meth:`throw` is called before the receiver calls :meth:`get`, then :class:`Waiter`
          will store the value/exception. The following :meth:`get` will return the value/raise the exception.
    
        The :meth:`switch` and :meth:`throw` methods must only be called from the :class:`Hub` greenlet.
        The :meth:`get` method must be called from a greenlet other than :class:`Hub`.
    
            >>> result = Waiter()
            >>> timer = get_hub().loop.timer(0.1)
            >>> timer.start(result.switch, 'hello from Waiter')
            >>> result.get() # blocks for 0.1 seconds
            'hello from Waiter'
            >>> timer.close()
    
        If switch is called before the greenlet gets a chance to call :meth:`get` then
        :class:`Waiter` stores the value.
    
            >>> result = Waiter()
            >>> timer = get_hub().loop.timer(0.1)
            >>> timer.start(result.switch, 'hi from Waiter')
            >>> sleep(0.2)
            >>> result.get() # returns immediately without blocking
            'hi from Waiter'
            >>> timer.close()
    
        .. warning::
    
            This a limited and dangerous way to communicate between
            greenlets. It can easily leave a greenlet unscheduled forever
            if used incorrectly. Consider using safer classes such as
            :class:`gevent.event.Event`, :class:`gevent.event.AsyncResult`,
            or :class:`gevent.queue.Queue`.
    """
    def clear(self): # real signature unknown; restored from __doc__
        """ Waiter.clear(self) """
        pass

    def get(self): # real signature unknown; restored from __doc__
        """
        Waiter.get(self)
        If a value/an exception is stored, return/raise it. Otherwise until switch() or throw() is called.
        """
        pass

    def ready(self): # real signature unknown; restored from __doc__
        """
        Waiter.ready(self)
        Return true if and only if it holds a value or an exception
        """
        pass

    def successful(self): # real signature unknown; restored from __doc__
        """
        Waiter.successful(self)
        Return true if and only if it is ready and holds a value
        """
        pass

    def switch(self, value): # real signature unknown; restored from __doc__
        """
        Waiter.switch(self, value)
        
                Switch to the greenlet if one's available. Otherwise store the
                *value*.
        
                .. versionchanged:: 1.3b1
                   The *value* is no longer optional.
        """
        pass

    def switch_args(self, *args): # real signature unknown; restored from __doc__
        """ Waiter.switch_args(self, *args) """
        pass

    def throw(self, *throw_args): # real signature unknown; restored from __doc__
        """
        Waiter.throw(self, *throw_args)
        Switch to the greenlet with the exception. If there's no greenlet, store the exception.
        """
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __init__(self, hub=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    exc_info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Holds the exception info passed to :meth:`throw` if :meth:`throw` was called. Otherwise ``None``."""

    greenlet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hub = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000246E1813450>'
    __slots__ = [
        'hub',
        'greenlet',
        'value',
        '_exception',
    ]


class MultipleWaiter(Waiter):
    """
    MultipleWaiter(hub=None)
    
        An internal extension of Waiter that can be used if multiple objects
        must be waited on, and there is a chance that in between waits greenlets
        might be switched out. All greenlets that switch to this waiter
        will have their value returned.
    
        This does not handle exceptions or throw methods.
    """
    def get(self): # real signature unknown; restored from __doc__
        """ MultipleWaiter.get(self) """
        pass

    def switch(self, value): # real signature unknown; restored from __doc__
        """ MultipleWaiter.switch(self, value) """
        pass

    def __init__(self, hub=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000246E1813480>'
    __slots__ = [
        '_values',
    ]


# variables with complex values

__all__ = [
    'Waiter',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000246E181BC18>'

__pyx_capi__ = {
    'ConcurrentObjectUseError': None, # (!) real value is '<capsule object "PyObject *" at 0x00000246E18133C0>'
    '_NONE': None, # (!) real value is '<capsule object "PyObject *" at 0x00000246E1813420>'
    '_greenlet_imported': None, # (!) real value is '<capsule object "int" at 0x00000246E18133F0>'
    'sys': None, # (!) real value is '<capsule object "PyObject *" at 0x00000246E1813390>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='gevent.__waiter', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000246E181BC18>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\gevent\\\\__waiter.cp37-win_amd64.pyd')"

__test__ = {}

