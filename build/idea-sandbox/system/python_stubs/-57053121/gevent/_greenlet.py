# encoding: utf-8
# module gevent._greenlet
# from C:\Users\Doly\Anaconda3\lib\site-packages\gevent\_greenlet.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import gevent.__waiter as _waiter # C:\Users\Doly\Anaconda3\lib\site-packages\gevent\__waiter.cp37-win_amd64.pyd
from gevent.__hub_local import get_hub_noargs

from gevent.__waiter import Waiter

from greenlet import getcurrent

import greenlet as __greenlet


# functions

def greenlet_init(*args, **kwargs): # real signature unknown
    pass

def import_c_accel(globs, cname): # reliably restored by inspect
    """
    Import the C-accelerator for the __name__
        and copy its globals.
    """
    pass

def joinall(greenlets, timeout=None, raise_error=False, count=None): # real signature unknown; restored from __doc__
    """
    joinall(greenlets, timeout=None, raise_error=False, count=None)
    
        Wait for the ``greenlets`` to finish.
    
        :param greenlets: A sequence (supporting :func:`len`) of greenlets to wait for.
        :keyword float timeout: If given, the maximum number of seconds to wait.
        :return: A sequence of the greenlets that finished before the timeout (if any)
            expired.
    """
    pass

def killall(greenlets, exception=None, block=True, timeout=None): # real signature unknown; restored from __doc__
    """
    killall(greenlets, exception=GreenletExit, block=True, timeout=None)
    
        Forceably terminate all the ``greenlets`` by causing them to raise ``exception``.
    
        .. caution:: Use care when killing greenlets. If they are not prepared for exceptions,
           this could result in corrupted state.
    
        :param greenlets: A **bounded** iterable of the non-None greenlets to terminate.
           *All* the items in this iterable must be greenlets that belong to the same thread.
        :keyword exception: The exception to raise in the greenlets. By default this is
            :class:`GreenletExit`.
        :keyword bool block: If True (the default) then this function only returns when all the
            greenlets are dead; the current greenlet is unscheduled during that process.
            If greenlets ignore the initial exception raised in them,
            then they will be joined (with :func:`gevent.joinall`) and allowed to die naturally.
            If False, this function returns immediately and greenlets will raise
            the exception asynchronously.
        :keyword float timeout: A time in seconds to wait for greenlets to die. If given, it is
            only honored when ``block`` is True.
        :raise Timeout: If blocking and a timeout is given that elapses before
            all the greenlets are dead.
    
        .. versionchanged:: 1.1a2
            *greenlets* can be any iterable of greenlets, like an iterator or a set.
            Previously it had to be a list or tuple.
    """
    pass

def _kill(glet, exception, waiter): # real signature unknown; restored from __doc__
    """ _kill(glet, exception, waiter) """
    pass

# classes

class SpawnedLink(object):
    """
    SpawnedLink(callback)
    
        A wrapper around link that calls it in another greenlet.
    
        Can be called only from main loop.
    """
    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getattr__(self, *args, **kwargs): # real signature unknown
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, callback): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    callback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """callback: object"""


    __slots__ = [
        'callback',
    ]


class FailureSpawnedLink(SpawnedLink):
    """
    A wrapper around link that calls it in another greenlet only if source failed.
    
        Can be called only from main loop.
    """
    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __slots__ = []


class Greenlet(__greenlet.greenlet):
    """
    Greenlet(run=None, *args, **kwargs)
    
        A light-weight cooperatively-scheduled execution unit.
    """
    def add_spawn_callback(self, callback): # real signature unknown; restored from __doc__
        """
        Greenlet.add_spawn_callback(callback)
        
                add_spawn_callback(callback) -> None
        
                Set up a *callback* to be invoked when :class:`Greenlet` objects
                are started.
        
                The invocation order of spawn callbacks is unspecified.  Adding the
                same callback more than one time will not cause it to be called more
                than once.
        
                .. versionadded:: 1.4.0
        """
        pass

    def get(self, block=True, timeout=None): # real signature unknown; restored from __doc__
        """
        Greenlet.get(self, block=True, timeout=None)
        
                get(block=True, timeout=None) -> object
        
                Return the result the greenlet has returned or re-raise the
                exception it has raised.
        
                If block is ``False``, raise :class:`gevent.Timeout` if the
                greenlet is still alive. If block is ``True``, unschedule the
                current greenlet until the result is available or the timeout
                expires. In the latter case, :class:`gevent.Timeout` is
                raised.
        """
        pass

    def has_links(self): # real signature unknown; restored from __doc__
        """ Greenlet.has_links(self) -> bool """
        return False

    def join(self, timeout=None): # real signature unknown; restored from __doc__
        """
        Greenlet.join(self, timeout=None)
        
                join(timeout=None) -> None
        
                Wait until the greenlet finishes or *timeout* expires. Return
                ``None`` regardless.
        """
        pass

    def kill(self, exception=None, block=True, timeout=None): # real signature unknown; restored from __doc__
        """
        Greenlet.kill(self, exception=GreenletExit, block=True, timeout=None)
        
                Raise the ``exception`` in the greenlet.
        
                If ``block`` is ``True`` (the default), wait until the greenlet dies or the optional timeout expires.
                If block is ``False``, the current greenlet is not unscheduled.
        
                The function always returns ``None`` and never raises an error.
        
                .. note::
        
                    Depending on what this greenlet is executing and the state
                    of the event loop, the exception may or may not be raised
                    immediately when this greenlet resumes execution. It may
                    be raised on a subsequent green call, or, if this greenlet
                    exits before making such a call, it may not be raised at
                    all. As of 1.1, an example where the exception is raised
                    later is if this greenlet had called :func:`sleep(0)
                    <gevent.sleep>`; an example where the exception is raised
                    immediately is if this greenlet had called
                    :func:`sleep(0.1) <gevent.sleep>`.
        
                .. caution::
        
                    Use care when killing greenlets. If the code executing is not
                    exception safe (e.g., makes proper use of ``finally``) then an
                    unexpected exception could result in corrupted state.
        
                See also :func:`gevent.kill`.
        
                :keyword type exception: The type of exception to raise in the greenlet. The default
                    is :class:`GreenletExit`, which indicates a :meth:`successful` completion
                    of the greenlet.
        
                .. versionchanged:: 0.13.0
                    *block* is now ``True`` by default.
                .. versionchanged:: 1.1a2
                    If this greenlet had never been switched to, killing it will prevent it from ever being switched to.
        """
        pass

    def link(self, callback, SpawnedLink=None): # real signature unknown; restored from __doc__
        """
        Greenlet.link(self, callback, SpawnedLink=SpawnedLink)
        
                Link greenlet's completion to a callable.
        
                The *callback* will be called with this instance as an
                argument once this greenlet is dead. A callable is called in
                its own :class:`greenlet.greenlet` (*not* a
                :class:`Greenlet`).
        """
        pass

    def link_exception(self, callback, SpawnedLink=None): # real signature unknown; restored from __doc__
        """
        Greenlet.link_exception(self, callback, SpawnedLink=FailureSpawnedLink)
        
                Like :meth:`link` but *callback* is only notified when the
                greenlet dies because of an unhandled exception.
        """
        pass

    def link_value(self, callback, SpawnedLink=None): # real signature unknown; restored from __doc__
        """
        Greenlet.link_value(self, callback, SpawnedLink=SuccessSpawnedLink)
        
                Like :meth:`link` but *callback* is only notified when the greenlet
                has completed successfully.
        """
        pass

    def rawlink(self, callback): # real signature unknown; restored from __doc__
        """
        Greenlet.rawlink(self, callback)
        
                Register a callable to be executed when the greenlet finishes
                execution.
        
                The *callback* will be called with this instance as an
                argument.
        
                .. caution:: The callable will be called in the HUB greenlet.
        """
        pass

    def ready(self): # real signature unknown; restored from __doc__
        """
        Greenlet.ready(self) -> bool
        
                Return a true value if and only if the greenlet has finished
                execution.
        
                .. versionchanged:: 1.1
                    This function is only guaranteed to return true or false *values*, not
                    necessarily the literal constants ``True`` or ``False``.
        """
        return False

    def remove_spawn_callback(self, callback): # real signature unknown; restored from __doc__
        """
        Greenlet.remove_spawn_callback(callback)
        
                remove_spawn_callback(callback) -> None
        
                Remove *callback* function added with :meth:`Greenlet.add_spawn_callback`.
                This function will not fail if *callback* has been already removed or
                if *callback* was never added.
        
                .. versionadded:: 1.4.0
        """
        pass

    def run(self): # real signature unknown; restored from __doc__
        """ Greenlet.run(self) """
        pass

    @classmethod
    def spawn(cls, type_cls, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        Greenlet.spawn(type cls, *args, **kwargs)
        
                spawn(function, *args, **kwargs) -> Greenlet
        
                Create a new :class:`Greenlet` object and schedule it to run ``function(*args, **kwargs)``.
                This can be used as ``gevent.spawn`` or ``Greenlet.spawn``.
        
                The arguments are passed to :meth:`Greenlet.__init__`.
        
                .. versionchanged:: 1.1b1
                    If a *function* is given that is not callable, immediately raise a :exc:`TypeError`
                    instead of spawning a greenlet that will raise an uncaught TypeError.
        """
        pass

    @classmethod
    def spawn_later(cls, type_cls, seconds, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        Greenlet.spawn_later(type cls, seconds, *args, **kwargs)
        
                spawn_later(seconds, function, *args, **kwargs) -> Greenlet
        
                Create and return a new `Greenlet` object scheduled to run ``function(*args, **kwargs)``
                in a future loop iteration *seconds* later. This can be used as ``Greenlet.spawn_later``
                or ``gevent.spawn_later``.
        
                The arguments are passed to :meth:`Greenlet.__init__`.
        
                .. versionchanged:: 1.1b1
                   If an argument that's meant to be a function (the first argument in *args*, or the ``run`` keyword )
                   is given to this classmethod (and not a classmethod of a subclass),
                   it is verified to be callable. Previously, the spawned greenlet would have failed
                   when it started running.
        """
        pass

    def start(self): # real signature unknown; restored from __doc__
        """
        Greenlet.start(self)
        Schedule the greenlet to run in this loop iteration
        """
        pass

    def start_later(self, seconds): # real signature unknown; restored from __doc__
        """
        Greenlet.start_later(self, seconds)
        
                start_later(seconds) -> None
        
                Schedule the greenlet to run in the future loop iteration
                *seconds* later
        """
        pass

    def successful(self): # real signature unknown; restored from __doc__
        """
        Greenlet.successful(self) -> bool
        
                Return a true value if and only if the greenlet has finished execution
                successfully, that is, without raising an error.
        
                .. tip:: A greenlet that has been killed with the default
                    :class:`GreenletExit` exception is considered successful.
                    That is, ``GreenletExit`` is not considered an error.
        
                .. note:: This function is only guaranteed to return true or false *values*,
                      not necessarily the literal constants ``True`` or ``False``.
        """
        return False

    def throw(self, *args): # real signature unknown; restored from __doc__
        """
        Greenlet.throw(self, *args)
        Immediately switch into the greenlet and raise an exception in it.
        
                Should only be called from the HUB, otherwise the current greenlet is left unscheduled forever.
                To raise an exception in a safe manner from any greenlet, use :meth:`kill`.
        
                If a greenlet was started but never switched to yet, then also
                a) cancel the event that will start it
                b) fire the notifications as if an exception was raised in a greenlet
        """
        pass

    def unlink(self, callback): # real signature unknown; restored from __doc__
        """
        Greenlet.unlink(self, callback)
        Remove the callback set by :meth:`link` or :meth:`rawlink`
        """
        pass

    def unlink_all(self): # real signature unknown; restored from __doc__
        """
        Greenlet.unlink_all(self)
        
                Remove all the callbacks.
        
                .. versionadded:: 1.3a2
        """
        pass

    def _formatinfo(self): # real signature unknown; restored from __doc__
        """ Greenlet._formatinfo(self) -> str """
        return ""

    def _notify_links(self): # real signature unknown; restored from __doc__
        """ Greenlet._notify_links(self) """
        pass

    def _raise_exception(self): # real signature unknown; restored from __doc__
        """ Greenlet._raise_exception(self) """
        pass

    def _run(self): # real signature unknown; restored from __doc__
        """
        Greenlet._run(self)
        
                Subclasses may override this method to take any number of
                arguments and keyword arguments.
        
                .. versionadded:: 1.1a3
                    Previously, if no callable object was
                    passed to the constructor, the spawned greenlet would later
                    fail with an AttributeError.
        """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """
        :param args: The arguments passed to the ``run`` function.
                :param kwargs: The keyword arguments passed to the ``run`` function.
                :keyword callable run: The callable object to run. If not given, this object's
                    `_run` method will be invoked (typically defined by subclasses).
        
                .. versionchanged:: 1.1b1
                    The ``run`` argument to the constructor is now verified to be a callable
                    object. Previously, passing a non-callable object would fail after the greenlet
                    was spawned.
        
                .. versionchanged:: 1.3b1
                   The ``GEVENT_TRACK_GREENLET_TREE`` configuration value may be set to
                   a false value to disable ``spawn_tree_locals``, ``spawning_greenlet``,
                   and ``spawning_stack``. The first two will be None in that case, and the
                   latter will be empty.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    args = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dead = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Boolean indicating that the greenlet is dead and will not run again."""

    exception = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Holds the exception instance raised by the function if the
        greenlet has finished with an error. Otherwise ``None``.
        """

    exc_info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Holds the exc_info three-tuple raised by the function if the
        greenlet finished with an error. Otherwise a false value.

        .. note:: This is a provisional API and may change.

        .. versionadded:: 1.1
        """

    kwargs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    loop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    minimal_ident = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        A small, unique integer that identifies this object.

        This is similar to :attr:`threading.Thread.ident` (and `id`)
        in that as long as this object is alive, no other greenlet *in
        this hub* will have the same id, but it makes a stronger
        guarantee that the assigned values will be small and
        sequential. Sometime after this object has died, the value
        will be available for reuse.

        To get ids that are unique across all hubs, combine this with
        the hub's ``minimal_ident``.

        .. versionadded:: 1.3a2
        """

    spawning_greenlet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    spawn_tree_locals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """spawn_tree_locals: dict"""

    started = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _spawning_stack_frames = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    name = None # (!) real value is '<gevent._util.readproperty object at 0x0000026795B82898>'
    spawning_stack = None # (!) real value is '<gevent._util.Lazy object at 0x0000026795B82748>'
    spawning_stack_limit = 10
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000026795B851E0>'


class Lazy(object):
    """
    A non-data descriptor used just like @property. The
        difference is the function value is assigned to the instance
        dict the first time it is accessed and then the function is never
        called agoin.
    """
    def __get__(self, inst, class_): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, func): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gevent._util', '__doc__': '\\n    A non-data descriptor used just like @property. The\\n    difference is the function value is assigned to the instance\\n    dict the first time it is accessed and then the function is never\\n    called agoin.\\n    ', '__init__': <function Lazy.__init__ at 0x0000026795C4F730>, '__get__': <function Lazy.__get__ at 0x0000026795C4F7B8>, '__dict__': <attribute '__dict__' of 'Lazy' objects>, '__weakref__': <attribute '__weakref__' of 'Lazy' objects>})"


class readproperty(object):
    """
    A non-data descriptor like @property. The difference is that
        when the property is assigned to, it is cached in the instance
        and the function is not called on that instance again.
    """
    def __get__(self, inst, class_): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, func): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gevent._util', '__doc__': '\\n    A non-data descriptor like @property. The difference is that\\n    when the property is assigned to, it is cached in the instance\\n    and the function is not called on that instance again.\\n    ', '__init__': <function readproperty.__init__ at 0x0000026795C4F840>, '__get__': <function readproperty.__get__ at 0x0000026795C4F8C8>, '__dict__': <attribute '__dict__' of 'readproperty' objects>, '__weakref__': <attribute '__weakref__' of 'readproperty' objects>})"


class SuccessSpawnedLink(SpawnedLink):
    """
    A wrapper around link that calls it in another greenlet only if source succeed.
    
        Can be called only from main loop.
    """
    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __slots__ = []


class _dummy_event(object):
    """ _dummy_event() """
    def close(self): # real signature unknown; restored from __doc__
        """ _dummy_event.close(self) """
        pass

    def start(self, cb): # real signature unknown; restored from __doc__
        """ _dummy_event.start(self, cb) """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ _dummy_event.stop(self) """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pending = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000026795B85210>'
    __slots__ = (
        'pending',
        'active',
    )


class _Frame(object):
    """ _Frame(f_code, f_lineno, f_back) """
    def __init__(self, f_code, f_lineno, f_back): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    f_back = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    f_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    f_globals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    f_lineno = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __slots__ = (
        'f_code',
        'f_lineno',
        'f_back',
    )


# variables with complex values

__all__ = [
    'Greenlet',
    'joinall',
    'killall',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000026795B7BF98>'

__pyx_capi__ = {
    'GEVENT_CONFIG': None, # (!) real value is '<capsule object "PyObject *" at 0x0000026795B63F90>'
    'GreenletExit': None, # (!) real value is '<capsule object "PyObject *" at 0x0000026795B63D50>'
    'InvalidSwitchError': None, # (!) real value is '<capsule object "PyObject *" at 0x0000026795B63D80>'
    'Timeout': None, # (!) real value is '<capsule object "PyObject *" at 0x0000026795B63D20>'
    '_Frame_from_list': None, # (!) real value is '<capsule object "struct __pyx_obj_6gevent_9_greenlet__Frame *(PyObject *)" at 0x0000026795B850F0>'
    '_PYPY': None, # (!) real value is '<capsule object "int" at 0x0000026795B632D0>'
    '_call_spawn_callbacks': None, # (!) real value is '<capsule object "void (struct __pyx_obj_6gevent_9_greenlet_Greenlet *)" at 0x0000026795B851B0>'
    '_cancelled_start_event': None, # (!) real value is '<capsule object "struct __pyx_obj_6gevent_9_greenlet__dummy_event *" at 0x0000026795B63FC0>'
    '_extract_stack': None, # (!) real value is '<capsule object "PyObject *(int)" at 0x0000026795B850C0>'
    '_greenlet__init__': None, # (!) real value is '<capsule object "PyObject *" at 0x0000026795B63DE0>'
    '_greenlet_imported': None, # (!) real value is '<capsule object "int" at 0x0000026795B63DB0>'
    '_init': None, # (!) real value is '<capsule object "void (void)" at 0x0000026795B85090>'
    '_killall': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyObject *)" at 0x0000026795B85150>'
    '_killall3': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyObject *, PyObject *)" at 0x0000026795B85120>'
    '_spawn_callbacks': None, # (!) real value is '<capsule object "PyObject *" at 0x0000026795B85060>'
    '_start_completed_event': None, # (!) real value is '<capsule object "struct __pyx_obj_6gevent_9_greenlet__dummy_event *" at 0x0000026795B85030>'
    '_threadlocal': None, # (!) real value is '<capsule object "PyObject *" at 0x0000026795B63E10>'
    'dump_traceback': None, # (!) real value is '<capsule object "PyObject *" at 0x0000026795B63EA0>'
    'get_hub_class': None, # (!) real value is '<capsule object "PyObject *" at 0x0000026795B63E40>'
    'iwait': None, # (!) real value is '<capsule object "PyObject *" at 0x0000026795B63F30>'
    'joinall': None, # (!) real value is '<capsule object "PyObject *(PyObject *, int __pyx_skip_dispatch, struct __pyx_opt_args_6gevent_9_greenlet_joinall *__pyx_optional_args)" at 0x0000026795B85180>'
    'load_traceback': None, # (!) real value is '<capsule object "PyObject *" at 0x0000026795B63ED0>'
    'reraise': None, # (!) real value is '<capsule object "PyObject *" at 0x0000026795B63F60>'
    'sys_exc_info': None, # (!) real value is '<capsule object "PyObject *" at 0x0000026795B63CF0>'
    'sys_getframe': None, # (!) real value is '<capsule object "PyObject *" at 0x0000026795B632A0>'
    'wait': None, # (!) real value is '<capsule object "PyObject *" at 0x0000026795B63F00>'
    'wref': None, # (!) real value is '<capsule object "PyObject *" at 0x0000026795B63E70>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='gevent._greenlet', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000026795B7BF98>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\gevent\\\\_greenlet.cp37-win_amd64.pyd')"

__test__ = {}

