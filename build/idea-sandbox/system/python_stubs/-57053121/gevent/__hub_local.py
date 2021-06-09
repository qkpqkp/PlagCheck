# encoding: utf-8
# module gevent.__hub_local
# from C:\Users\Doly\Anaconda3\lib\site-packages\gevent\__hub_local.cp37-win_amd64.pyd
# by generator 1.147
""" Maintains the thread local hub. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import gevent.__hub_primitives as __gevent___hub_primitives
import _thread as ___thread


# Variables with simple values

thread_mod_name = '_thread'

# functions

def get_hub(*args, **kwargs): # real signature unknown
    """
    Return the hub for the current thread.
    
        If a hub does not exist in the current thread, a new one is
        created of the type returned by :func:`get_hub_class`.
    
        .. deprecated:: 1.3b1
           The ``*args`` and ``**kwargs`` arguments are deprecated. They were
           only used when the hub was created, and so were non-deterministic---to be
           sure they were used, *all* callers had to pass them, or they were order-dependent.
           Use ``set_hub`` instead.
    """
    pass

def get_hub_class(*args, **kwargs): # real signature unknown
    """
    Return the type of hub to use for the current thread.
    
        If there's no type of hub for the current thread yet, 'gevent.hub.Hub' is used.
    """
    pass

def get_hub_if_exists(*args, **kwargs): # real signature unknown
    """
    Return the hub for the current thread.
    
        Return ``None`` if no hub has been created yet.
    """
    pass

def get_hub_noargs(*args, **kwargs): # real signature unknown
    pass

def get_loop(*args, **kwargs): # real signature unknown
    pass

def import_c_accel(globs, cname): # reliably restored by inspect
    """
    Import the C-accelerator for the __name__
        and copy its globals.
    """
    pass

def set_default_hub_class(*args, **kwargs): # real signature unknown
    pass

def set_hub(*args, **kwargs): # real signature unknown
    pass

def set_loop(*args, **kwargs): # real signature unknown
    pass

# classes

class Hub(__gevent___hub_primitives.WaitOperationsGreenlet):
    """
    A greenlet that runs the event loop.
    
        It is created automatically by :func:`get_hub`.
    
        .. rubric:: Switching
    
        Every time this greenlet (i.e., the event loop) is switched *to*,
        if the current greenlet has a ``switch_out`` method, it will be
        called. This allows a greenlet to take some cleanup actions before
        yielding control. This method should not call any gevent blocking
        functions.
    """
    def destroy(self, destroy_loop=None): # reliably restored by inspect
        """
        Destroy this hub and clean up its resources.
        
                If you manually create hubs, you *should* call this
                method before disposing of the hub object reference.
        """
        pass

    def handle_error(self, context, type, value, tb): # reliably restored by inspect
        """
        Called by the event loop when an error occurs. The arguments
                type, value, and tb are the standard tuple returned by :func:`sys.exc_info`.
        
                Applications can set a property on the hub with this same signature
                to override the error handling provided by this class.
        
                Errors that are :attr:`system errors <SYSTEM_ERROR>` are passed
                to :meth:`handle_system_error`.
        
                :param context: If this is ``None``, indicates a system error that
                    should generally result in exiting the loop and being thrown to the
                    parent greenlet.
        """
        pass

    def handle_system_error(self, type, value): # reliably restored by inspect
        """
        Called from `handle_error` when the exception type is determined
                to be a :attr:`system error <SYSTEM_ERROR>`.
        
                System errors cause the exception to be raised in the main
                greenlet (the parent of this hub).
        """
        pass

    def join(self, timeout=None): # reliably restored by inspect
        """
        Wait for the event loop to finish. Exits only when there are
                no more spawned greenlets, started servers, active timeouts or watchers.
        
                If *timeout* is provided, wait no longer for the specified number of seconds.
        
                Returns True if exited because the loop finished execution.
                Returns False if exited because of timeout expired.
        """
        pass

    def print_exception(self, context, type, value, tb): # reliably restored by inspect
        # no doc
        pass

    def run(self): # reliably restored by inspect
        """
        Entry-point to running the loop. This method is called automatically
                when the hub greenlet is scheduled; do not call it directly.
        
                :raises gevent.exceptions.LoopExit: If the loop finishes running. This means
                   that there are no other scheduled greenlets, and no active
                   watchers or servers. In some situations, this indicates a
                   programming error.
        """
        pass

    def start_periodic_monitoring_thread(self): # reliably restored by inspect
        # no doc
        pass

    def _del_resolver(self): # reliably restored by inspect
        # no doc
        pass

    def _del_threadpool(self): # reliably restored by inspect
        # no doc
        pass

    def _get_resolver(self): # reliably restored by inspect
        # no doc
        pass

    def _get_threadpool(self): # reliably restored by inspect
        # no doc
        pass

    def _set_resolver(self, value): # reliably restored by inspect
        # no doc
        pass

    def _set_threadpool(self, value): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, loop=None, default=None): # reliably restored by inspect
        # no doc
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    backend = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    loop_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    main_hub = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Is this the hub for the main thread?

        .. versionadded:: 1.3b1
        """

    resolver = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
                        The DNS resolver that the socket functions will use.

                        .. seealso:: :doc:`/dns`
                        """

    resolver_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    threadpool = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
                          The threadpool associated with this hub.

                          Usually this is a
                          :class:`gevent.threadpool.ThreadPool`, but
                          you :attr:`can customize that
                          <gevent._config.Config.threadpool>`.

                          Use this object to schedule blocking
                          (non-cooperative) operations in a different
                          thread to prevent them from halting the event loop.
                          """

    threadpool_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    exception_stream = None # (!) real value is '<gevent._util.readproperty object at 0x000001AE2FBAE320>'
    ident_registry = None # (!) real value is '<gevent._util.Lazy object at 0x000001AE2FBAE2E8>'
    name = ''
    NOT_ERROR = (
        None, # (!) real value is "<class 'greenlet.GreenletExit'>"
        SystemExit,
    )
    periodic_monitoring_thread = None
    SYSTEM_ERROR = (
        KeyboardInterrupt,
        SystemExit,
        SystemError,
    )
    threadpool_size = 10
    thread_ident = None
    _hub_counter = 0


class _Threadlocal(___thread._local):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gevent.__hub_local', '__init__': <cyfunction _Threadlocal.__init__ at 0x000001AE2E29FF60>, '__dict__': <attribute '__dict__' of '_Threadlocal' objects>, '__doc__': None})"


# variables with complex values

__all__ = [
    'get_hub',
    'get_hub_noargs',
    'get_hub_if_exists',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001AE2FB3B160>'

__pyx_capi__ = {
    '_threadlocal': None, # (!) real value is '<capsule object "PyObject *" at 0x000001AE2FAF9B70>'
    'get_hub_class': None, # (!) real value is '<capsule object "PyObject *(int __pyx_skip_dispatch)" at 0x000001AE2FAF9BA0>'
    'get_hub_if_exists': None, # (!) real value is '<capsule object "struct __pyx_obj_6gevent_21__greenlet_primitives_SwitchOutGreenletWithLoop *(int __pyx_skip_dispatch)" at 0x000001AE2FAF9BD0>'
    'get_hub_noargs': None, # (!) real value is '<capsule object "struct __pyx_obj_6gevent_21__greenlet_primitives_SwitchOutGreenletWithLoop *(int __pyx_skip_dispatch)" at 0x000001AE2FAF9CC0>'
    'get_loop': None, # (!) real value is '<capsule object "PyObject *(int __pyx_skip_dispatch)" at 0x000001AE2FAF9C60>'
    'set_hub': None, # (!) real value is '<capsule object "PyObject *(struct __pyx_obj_6gevent_21__greenlet_primitives_SwitchOutGreenletWithLoop *, int __pyx_skip_dispatch)" at 0x000001AE2FAF9C00>'
    'set_loop': None, # (!) real value is '<capsule object "PyObject *(PyObject *, int __pyx_skip_dispatch)" at 0x000001AE2FAF9C90>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='gevent.__hub_local', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001AE2FB3B160>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\gevent\\\\__hub_local.cp37-win_amd64.pyd')"

__test__ = {}

