# encoding: utf-8
# module gevent.libev.corecext
# from C:\Users\Doly\Anaconda3\lib\site-packages\gevent\libev\corecext.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import sys as sys # <module 'sys' (built-in)>
import os as os # C:\Users\Doly\Anaconda3\lib\os.py
import traceback as traceback # C:\Users\Doly\Anaconda3\lib\traceback.py
import signal as signalmodule # C:\Users\Doly\Anaconda3\lib\signal.py
from sys import getswitchinterval


# Variables with simple values

ASYNC = 524288

BACKEND_EPOLL = 4
BACKEND_KQUEUE = 8
BACKEND_POLL = 2
BACKEND_PORT = 32
BACKEND_SELECT = 1

CHECK = 32768
CHILD = 2048

CLEANUP = 262144

CUSTOM = 16777216

EMBED = 65536

ERROR = -2147483648

EV_USE_4HEAP = 2

EV_USE_CLOCK_SYSCALL = 0

EV_USE_EVENTFD = 0
EV_USE_FLOOR = 0
EV_USE_INOTIFY = 0
EV_USE_MONOTONIC = 0
EV_USE_NANOSLEEP = 0
EV_USE_REALTIME = 0
EV_USE_SIGNALFD = 0

FORK = 131072
FORKCHECK = 33554432

IDLE = 8192

LIBEV_EMBED = True

MAXPRI = 2

MINPRI = -2

NOINOTIFY = 1048576
NONE = 0
NOSIGMASK = 4194304

PERIODIC = 512

PREPARE = 16384

READ = 1
READWRITE = 3

SIGNAL = 1024
SIGNALFD = 2097152

STAT = 4096

TIMER = 256

UNDEF = -1

WRITE = 2

__SYSERR_CALLBACK = None

# functions

def embeddable_backends(*args, **kwargs): # real signature unknown
    pass

def get_header_version(*args, **kwargs): # real signature unknown
    pass

def get_version(*args, **kwargs): # real signature unknown
    pass

def recommended_backends(*args, **kwargs): # real signature unknown
    pass

def set_syserr_cb(*args, **kwargs): # real signature unknown
    pass

def supported_backends(*args, **kwargs): # real signature unknown
    pass

def time(*args, **kwargs): # real signature unknown
    pass

def _check_flags(*args, **kwargs): # real signature unknown
    pass

def _events_to_str(*args, **kwargs): # real signature unknown
    pass

def _flags_to_int(*args, **kwargs): # real signature unknown
    pass

def _flags_to_list(*args, **kwargs): # real signature unknown
    pass

# classes

class watcher(object):
    """ Abstract base class for all the watchers """
    def close(self, *args, **kwargs): # real signature unknown
        pass

    def feed(self, *args, **kwargs): # real signature unknown
        pass

    def start(self, *args, **kwargs): # real signature unknown
        pass

    def stop(self, *args, **kwargs): # real signature unknown
        pass

    def _format(self, *args, **kwargs): # real signature unknown
        pass

    def __enter__(self, *args, **kwargs): # real signature unknown
        pass

    def __exit__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    args = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    callback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    loop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pending = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class async_(watcher):
    # no doc
    def send(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    pending = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



async = async_


class callback(object):
    # no doc
    def close(self, *args, **kwargs): # real signature unknown
        pass

    def stop(self, *args, **kwargs): # real signature unknown
        pass

    def _format(self, *args, **kwargs): # real signature unknown
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    args = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    callback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pending = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class check(watcher):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class child(watcher):
    # no doc
    def _format(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    pid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rpid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rstatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class fork(watcher):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class idle(watcher):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class io(watcher):
    # no doc
    def start(self, *args, **kwargs): # real signature unknown
        pass

    def _format(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    events_str = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class loop(object):
    # no doc
    def async_(self, *args, **kwargs): # real signature unknown
        pass

    def break_(self, *args, **kwargs): # real signature unknown
        pass

    def check(self, *args, **kwargs): # real signature unknown
        pass

    def child(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def fileno(self, *args, **kwargs): # real signature unknown
        pass

    def fork(self, *args, **kwargs): # real signature unknown
        pass

    def handle_error(self, *args, **kwargs): # real signature unknown
        pass

    def idle(self, *args, **kwargs): # real signature unknown
        pass

    def install_sigchld(self, *args, **kwargs): # real signature unknown
        pass

    def io(self, *args, **kwargs): # real signature unknown
        pass

    def now(self, *args, **kwargs): # real signature unknown
        pass

    def prepare(self, *args, **kwargs): # real signature unknown
        pass

    def ref(self, *args, **kwargs): # real signature unknown
        pass

    def reinit(self, *args, **kwargs): # real signature unknown
        pass

    def reset_sigchld(self, *args, **kwargs): # real signature unknown
        pass

    def run(self, *args, **kwargs): # real signature unknown
        pass

    def run_callback(self, *args, **kwargs): # real signature unknown
        pass

    def signal(self, *args, **kwargs): # real signature unknown
        pass

    def stat(self, *args, **kwargs): # real signature unknown
        pass

    def timer(self, *args, **kwargs): # real signature unknown
        pass

    def unref(self, *args, **kwargs): # real signature unknown
        pass

    def update(self, *args, **kwargs): # real signature unknown
        pass

    def update_now(self, *args, **kwargs): # real signature unknown
        pass

    def verify(self, *args, **kwargs): # real signature unknown
        pass

    def _default_handle_error(self, *args, **kwargs): # real signature unknown
        pass

    def _format(self, *args, **kwargs): # real signature unknown
        pass

    def _format_details(self, *args, **kwargs): # real signature unknown
        pass

    def _handle_syserr(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    activecnt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    approx_timer_resolution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    backend = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    backend_int = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    default = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    depth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    error_handler = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    iteration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    MAXPRI = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    MINPRI = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    origflags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    origflags_int = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pendingcnt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ptr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sigfd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sig_pending = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    WatcherType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _callbacks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001AEFECE55A0>'


class prepare(watcher):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class signal(watcher):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class stat(watcher):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    attr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    interval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    prev = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _paths = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class timer(watcher):
    # no doc
    def again(self, *args, **kwargs): # real signature unknown
        pass

    def start(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    at = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

basestring = (
    bytes,
    str,
)

EVENTS = None # (!) real value is 'gevent.core.EVENTS'

_events = [
    (
        1,
        'READ',
    ),
    (
        2,
        'WRITE',
    ),
    (
        128,
        '_IOFDSET',
    ),
    (
        512,
        'PERIODIC',
    ),
    (
        1024,
        'SIGNAL',
    ),
    (
        2048,
        'CHILD',
    ),
    (
        4096,
        'STAT',
    ),
    (
        8192,
        'IDLE',
    ),
    (
        16384,
        'PREPARE',
    ),
    (
        32768,
        'CHECK',
    ),
    (
        65536,
        'EMBED',
    ),
    (
        131072,
        'FORK',
    ),
    (
        262144,
        'CLEANUP',
    ),
    (
        524288,
        'ASYNC',
    ),
    (
        16777216,
        'CUSTOM',
    ),
    (
        -2147483648,
        'ERROR',
    ),
]

_flags = [
    (
        32,
        'port',
    ),
    (
        8,
        'kqueue',
    ),
    (
        4,
        'epoll',
    ),
    (
        2,
        'poll',
    ),
    (
        1,
        'select',
    ),
    (
        16777216,
        'noenv',
    ),
    (
        33554432,
        'forkcheck',
    ),
    (
        1048576,
        'noinotify',
    ),
    (
        2097152,
        'signalfd',
    ),
    (
        4194304,
        'nosigmask',
    ),
]

_flags_str2int = {
    'epoll': 4,
    'forkcheck': 33554432,
    'kqueue': 8,
    'noenv': 16777216,
    'noinotify': 1048576,
    'nosigmask': 4194304,
    'poll': 2,
    'port': 32,
    'select': 1,
    'signalfd': 2097152,
}

__all__ = [
    'get_version',
    'get_header_version',
    'supported_backends',
    'recommended_backends',
    'embeddable_backends',
    'time',
    'loop',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001AEFEC9ACF8>'

__spec__ = None # (!) real value is "ModuleSpec(name='gevent.libev.corecext', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001AEFEC9ACF8>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\gevent\\\\libev\\\\corecext.cp37-win_amd64.pyd')"

__test__ = {}

