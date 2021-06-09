# encoding: utf-8
# module gevent.__tracer
# from C:\Users\Doly\Anaconda3\lib\site-packages\gevent\__tracer.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

# functions

def import_c_accel(globs, cname): # reliably restored by inspect
    """
    Import the C-accelerator for the __name__
        and copy its globals.
    """
    pass

# classes

class GreenletTracer(object):
    """ GreenletTracer() """
    def did_block_hub(self, hub): # real signature unknown; restored from __doc__
        """ GreenletTracer.did_block_hub(self, hub) """
        pass

    def did_block_hub_report(self, hub, active_greenlet, format_kwargs): # real signature unknown; restored from __doc__
        """ GreenletTracer.did_block_hub_report(self, hub, active_greenlet, format_kwargs) """
        pass

    def ignore_current_greenlet_blocking(self): # real signature unknown; restored from __doc__
        """ GreenletTracer.ignore_current_greenlet_blocking(self) """
        pass

    def kill(self): # real signature unknown; restored from __doc__
        """ GreenletTracer.kill(self) """
        pass

    def monitor_current_greenlet_blocking(self): # real signature unknown; restored from __doc__
        """ GreenletTracer.monitor_current_greenlet_blocking(self) """
        pass

    def _trace(self, str_event, tuple_args): # real signature unknown; restored from __doc__
        """ GreenletTracer._trace(self, str event, tuple args) """
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    active_greenlet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    greenlet_switch_counter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    previous_trace_function = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001C4940E56C0>'


class _HubTracer(GreenletTracer):
    """ _HubTracer(hub, max_blocking_time) """
    def kill(self): # real signature unknown; restored from __doc__
        """ _HubTracer.kill(self) """
        pass

    def __init__(self, hub, max_blocking_time): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    hub = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_blocking_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001C4940E56F0>'


class HubSwitchTracer(_HubTracer):
    """ HubSwitchTracer(hub, max_blocking_time) """
    def did_block_hub(self, hub): # real signature unknown; restored from __doc__
        """ HubSwitchTracer.did_block_hub(self, hub) """
        pass

    def _trace(self, str_event, tuple_args): # real signature unknown; restored from __doc__
        """ HubSwitchTracer._trace(self, str event, tuple args) """
        pass

    def __init__(self, hub, max_blocking_time): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    last_entered_hub = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001C4940E5720>'


class MaxSwitchTracer(_HubTracer):
    """ MaxSwitchTracer(hub, max_blocking_time) """
    def did_block_hub(self, hub): # real signature unknown; restored from __doc__
        """ MaxSwitchTracer.did_block_hub(self, hub) """
        pass

    def _trace(self, str_event, tuple_args): # real signature unknown; restored from __doc__
        """ MaxSwitchTracer._trace(self, str event, tuple args) """
        pass

    def __init__(self, hub, max_blocking_time): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    last_switch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_blocking = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001C4940E5750>'


# variables with complex values

__all__ = [
    'GreenletTracer',
    'HubSwitchTracer',
    'MaxSwitchTracer',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001C4941751D0>'

__pyx_capi__ = {
    'format_run_info': None, # (!) real value is '<capsule object "PyObject *" at 0x000001C4940E5630>'
    'getcurrent': None, # (!) real value is '<capsule object "PyObject *" at 0x000001C4940E5600>'
    'gmctime': None, # (!) real value is '<capsule object "PyObject *" at 0x000001C4940E5690>'
    'perf_counter': None, # (!) real value is '<capsule object "PyObject *" at 0x000001C4940E5660>'
    'settrace': None, # (!) real value is '<capsule object "PyObject *" at 0x000001C4940E55D0>'
    'sys': None, # (!) real value is '<capsule object "PyObject *" at 0x000001C494039750>'
    'traceback': None, # (!) real value is '<capsule object "PyObject *" at 0x000001C4940E55A0>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='gevent.__tracer', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001C4941751D0>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\gevent\\\\__tracer.cp37-win_amd64.pyd')"

__test__ = {}

