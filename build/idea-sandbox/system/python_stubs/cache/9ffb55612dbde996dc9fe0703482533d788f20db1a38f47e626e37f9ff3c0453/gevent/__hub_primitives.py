# encoding: utf-8
# module gevent.__hub_primitives
# from C:\Users\Doly\Anaconda3\lib\site-packages\gevent\__hub_primitives.cp37-win_amd64.pyd
# by generator 1.147
"""
A collection of primitives used by the hub, and suitable for
compilation with Cython because of their frequency of use.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
from gevent.__greenlet_primitives import SwitchOutGreenletWithLoop

from gevent.__hub_local import get_hub_noargs

from gevent.__waiter import MultipleWaiter, Waiter

from greenlet import getcurrent

import gevent.__greenlet_primitives as __gevent___greenlet_primitives


# functions

def greenlet_init(*args, **kwargs): # real signature unknown
    pass

def import_c_accel(globs, cname): # reliably restored by inspect
    """
    Import the C-accelerator for the __name__
        and copy its globals.
    """
    pass

def iwait_on_objects(objects, timeout=None, count=None): # real signature unknown; restored from __doc__
    """
    iwait_on_objects(objects, timeout=None, count=None)
    
        Iteratively yield *objects* as they are ready, until all (or *count*) are ready
        or *timeout* expired.
    
        If you will only be consuming a portion of the *objects*, you should
        do so inside a ``with`` block on this object to avoid leaking resources::
    
            with gevent.iwait((a, b, c)) as it:
                for i in it:
                    if i is a:
                        break
    
        :param objects: A sequence (supporting :func:`len`) containing objects
            implementing the wait protocol (rawlink() and unlink()).
        :keyword int count: If not `None`, then a number specifying the maximum number
            of objects to wait for. If ``None`` (the default), all objects
            are waited for.
        :keyword float timeout: If given, specifies a maximum number of seconds
            to wait. If the timeout expires before the desired waited-for objects
            are available, then this method returns immediately.
    
        .. seealso:: :func:`wait`
    
        .. versionchanged:: 1.1a1
           Add the *count* parameter.
        .. versionchanged:: 1.1a2
           No longer raise :exc:`LoopExit` if our caller switches greenlets
           in between items yielded by this function.
        .. versionchanged:: 1.4
           Add support to use the returned object as a context manager.
    """
    pass

def set_default_timeout_error(e): # real signature unknown; restored from __doc__
    """ set_default_timeout_error(e) """
    pass

def wait_on_objects(objects=None, timeout=None, count=None): # real signature unknown; restored from __doc__
    """
    wait_on_objects(objects=None, timeout=None, count=None)
    
        Wait for ``objects`` to become ready or for event loop to finish.
    
        If ``objects`` is provided, it must be a list containing objects
        implementing the wait protocol (rawlink() and unlink() methods):
    
        - :class:`gevent.Greenlet` instance
        - :class:`gevent.event.Event` instance
        - :class:`gevent.lock.Semaphore` instance
        - :class:`gevent.subprocess.Popen` instance
    
        If ``objects`` is ``None`` (the default), ``wait()`` blocks until
        the current event loop has nothing to do (or until ``timeout`` passes):
    
        - all greenlets have finished
        - all servers were stopped
        - all event loop watchers were stopped.
    
        If ``count`` is ``None`` (the default), wait for all ``objects``
        to become ready.
    
        If ``count`` is a number, wait for (up to) ``count`` objects to become
        ready. (For example, if count is ``1`` then the function exits
        when any object in the list is ready).
    
        If ``timeout`` is provided, it specifies the maximum number of
        seconds ``wait()`` will block.
    
        Returns the list of ready objects, in the order in which they were
        ready.
    
        .. seealso:: :func:`iwait`
    """
    pass

def wait_on_socket(socket, watcher, timeout_exc=None): # real signature unknown; restored from __doc__
    """ wait_on_socket(socket, watcher, timeout_exc=None) """
    pass

def wait_on_watcher(watcher, timeout=None, timeout_exc=None, WaitOperationsGreenlet_hub=None): # real signature unknown; restored from __doc__
    """
    wait_on_watcher(watcher, timeout=None, timeout_exc=_NONE, WaitOperationsGreenlet hub=None)
    
        wait(watcher, timeout=None, [timeout_exc=None]) -> None
    
        Block the current greenlet until *watcher* is ready.
    
        If *timeout* is non-negative, then *timeout_exc* is raised after
        *timeout* second has passed.
    
        If :func:`cancel_wait` is called on *io* by another greenlet,
        raise an exception in this blocking greenlet
        (``socket.error(EBADF, 'File descriptor was closed in another
        greenlet')`` by default).
    
        :param io: An event loop watcher, most commonly an IO watcher obtained from
            :meth:`gevent.core.loop.io`
        :keyword timeout_exc: The exception to raise if the timeout expires.
            By default, a :class:`socket.timeout` exception is raised.
            If you pass a value for this keyword, it is interpreted as for
            :class:`gevent.timeout.Timeout`.
    
        :raises ~gevent.hub.ConcurrentObjectUseError: If the *watcher* is
            already started.
    """
    pass

def wait_read(fileno, timeout=None, timeout_exc=None): # real signature unknown; restored from __doc__
    """
    wait_read(fileno, timeout=None, timeout_exc=_NONE)
    
        wait_read(fileno, timeout=None, [timeout_exc=None]) -> None
    
        Block the current greenlet until *fileno* is ready to read.
    
        For the meaning of the other parameters and possible exceptions,
        see :func:`wait`.
    
        .. seealso:: :func:`cancel_wait`
    """
    pass

def wait_readwrite(fileno, timeout=None, timeout_exc=None, event=None): # real signature unknown; restored from __doc__
    """
    wait_readwrite(fileno, timeout=None, timeout_exc=_NONE, event=_NONE)
    
        wait_readwrite(fileno, timeout=None, [timeout_exc=None]) -> None
    
        Block the current greenlet until *fileno* is ready to read or
        write.
    
        For the meaning of the other parameters and possible exceptions,
        see :func:`wait`.
    
        .. deprecated:: 1.1
           The keyword argument *event* is ignored. Applications should not pass this parameter.
           In the future, doing so will become an error.
    
        .. seealso:: :func:`cancel_wait`
    """
    pass

def wait_write(fileno, timeout=None, timeout_exc=None, event=None): # real signature unknown; restored from __doc__
    """
    wait_write(fileno, timeout=None, timeout_exc=_NONE, event=_NONE)
    
        wait_write(fileno, timeout=None, [timeout_exc=None]) -> None
    
        Block the current greenlet until *fileno* is ready to write.
    
        For the meaning of the other parameters and possible exceptions,
        see :func:`wait`.
    
        .. deprecated:: 1.1
           The keyword argument *event* is ignored. Applications should not pass this parameter.
           In the future, doing so will become an error.
    
        .. seealso:: :func:`cancel_wait`
    """
    pass

def _init(): # real signature unknown; restored from __doc__
    """ _init() """
    pass

# classes

class ConcurrentObjectUseError(AssertionError):
    """
    Raised when an object is used (waited on) by two greenlets
        independently, meaning the object was entered into a blocking
        state by one greenlet and then another while still blocking in the
        first one.
    
        This is usually a programming error.
    
        .. seealso:: `gevent.socket.wait`
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class WaitOperationsGreenlet(__gevent___greenlet_primitives.SwitchOutGreenletWithLoop):
    # no doc
    def cancel_wait(self, watcher, error, close_watcher=False): # real signature unknown; restored from __doc__
        """
        WaitOperationsGreenlet.cancel_wait(self, watcher, error, close_watcher=False)
        
                Cancel an in-progress call to :meth:`wait` by throwing the given *error*
                in the waiting greenlet.
        
                .. versionchanged:: 1.3a1
                   Added the *close_watcher* parameter. If true, the watcher
                   will be closed after the exception is thrown. The watcher should then
                   be discarded. Closing the watcher is important to release native resources.
                .. versionchanged:: 1.3a2
                   Allow the *watcher* to be ``None``. No action is taken in that case.
        """
        pass

    def wait(self, watcher): # real signature unknown; restored from __doc__
        """
        WaitOperationsGreenlet.wait(self, watcher)
        
                Wait until the *watcher* (which must not be started) is ready.
        
                The current greenlet will be unscheduled during this time.
        """
        pass

    def _cancel_wait(self, watcher, error, close_watcher): # real signature unknown; restored from __doc__
        """ WaitOperationsGreenlet._cancel_wait(self, watcher, error, close_watcher) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001A21FA337E0>'


class _WaitIterator(object):
    """ _WaitIterator(objects, hub, timeout, count) """
    def next(self, *args, **kwargs): # real signature unknown
        pass

    def __enter__(self): # real signature unknown; restored from __doc__
        """ _WaitIterator.__enter__(self) """
        pass

    def __exit__(self, typ, value, tb): # real signature unknown; restored from __doc__
        """ _WaitIterator.__exit__(self, typ, value, tb) """
        pass

    def __init__(self, objects, hub, timeout, count): # real signature unknown; restored from __doc__
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

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001A21FA33810>'


# variables with complex values

_NONE = None # (!) real value is '<default value>'

__all__ = [
    'WaitOperationsGreenlet',
    'iwait_on_objects',
    'wait_on_objects',
    'wait_read',
    'wait_write',
    'wait_readwrite',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001A21FA43358>'

__pyx_capi__ = {
    'InvalidSwitchError': None, # (!) real value is '<capsule object "PyObject *" at 0x000001A21FA33510>'
    'Timeout': None, # (!) real value is '<capsule object "PyObject *" at 0x000001A21FA33600>'
    '_greenlet_imported': None, # (!) real value is '<capsule object "int" at 0x000001A21FA33630>'
    '_greenlet_primitives': None, # (!) real value is '<capsule object "PyObject *" at 0x000001A21FA33570>'
    '_primitive_wait': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyObject *, PyObject *, struct __pyx_obj_6gevent_16__hub_primitives_WaitOperationsGreenlet *)" at 0x000001A21FA336C0>'
    '_timeout_error': None, # (!) real value is '<capsule object "PyObject *" at 0x000001A21FA335D0>'
    '_waiter': None, # (!) real value is '<capsule object "PyObject *" at 0x000001A21FA33540>'
    'iwait_on_objects': None, # (!) real value is '<capsule object "PyObject *(PyObject *, int __pyx_skip_dispatch, struct __pyx_opt_args_6gevent_16__hub_primitives_iwait_on_objects *__pyx_optional_args)" at 0x000001A21FA33660>'
    'traceback': None, # (!) real value is '<capsule object "PyObject *" at 0x000001A21FA335A0>'
    'wait_on_objects': None, # (!) real value is '<capsule object "PyObject *(int __pyx_skip_dispatch, struct __pyx_opt_args_6gevent_16__hub_primitives_wait_on_objects *__pyx_optional_args)" at 0x000001A21FA33690>'
    'wait_on_socket': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyObject *, int __pyx_skip_dispatch, struct __pyx_opt_args_6gevent_16__hub_primitives_wait_on_socket *__pyx_optional_args)" at 0x000001A21FA337B0>'
    'wait_on_watcher': None, # (!) real value is '<capsule object "PyObject *(PyObject *, int __pyx_skip_dispatch, struct __pyx_opt_args_6gevent_16__hub_primitives_wait_on_watcher *__pyx_optional_args)" at 0x000001A21FA336F0>'
    'wait_read': None, # (!) real value is '<capsule object "PyObject *(PyObject *, int __pyx_skip_dispatch, struct __pyx_opt_args_6gevent_16__hub_primitives_wait_read *__pyx_optional_args)" at 0x000001A21FA33720>'
    'wait_readwrite': None, # (!) real value is '<capsule object "PyObject *(PyObject *, int __pyx_skip_dispatch, struct __pyx_opt_args_6gevent_16__hub_primitives_wait_readwrite *__pyx_optional_args)" at 0x000001A21FA33780>'
    'wait_write': None, # (!) real value is '<capsule object "PyObject *(PyObject *, int __pyx_skip_dispatch, struct __pyx_opt_args_6gevent_16__hub_primitives_wait_write *__pyx_optional_args)" at 0x000001A21FA33750>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='gevent.__hub_primitives', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001A21FA43358>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\gevent\\\\__hub_primitives.cp37-win_amd64.pyd')"

__test__ = {}

