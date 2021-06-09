# encoding: utf-8
# module gevent.__greenlet_primitives
# from C:\Users\Doly\Anaconda3\lib\site-packages\gevent\__greenlet_primitives.cp37-win_amd64.pyd
# by generator 1.147
"""
A collection of primitives used by the hub, and suitable for
compilation with Cython because of their frequency of use.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
from greenlet import getcurrent

import greenlet as __greenlet


# functions

def get_reachable_greenlets(): # real signature unknown; restored from __doc__
    """ get_reachable_greenlets() -> list """
    return []

def greenlet_init(*args, **kwargs): # real signature unknown
    pass

def import_c_accel(globs, cname): # reliably restored by inspect
    """
    Import the C-accelerator for the __name__
        and copy its globals.
    """
    pass

def _greenlet_switch(*args, **kwargs): # real signature unknown
    """
    switch(*args, **kwargs)
    
    Switch execution to this greenlet.
    
    If this greenlet has never been run, then this greenlet
    will be switched to using the body of self.run(*args, **kwargs).
    
    If the greenlet is active (has been run, but was switch()'ed
    out before leaving its run function), then this greenlet will
    be resumed and the return value to its switch call will be
    None if no arguments are given, the given argument if one
    argument is given, or the args tuple and keyword args dict if
    multiple arguments are given.
    
    If the greenlet is dead, or is the current greenlet then this
    function will simply return the arguments using the same rules as
    above.
    """
    pass

def _init(): # real signature unknown; restored from __doc__
    """ _init() """
    pass

# classes

class TrackedRawGreenlet(__greenlet.greenlet):
    """ TrackedRawGreenlet(function, parent) """
    def __init__(self, function, parent): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class SwitchOutGreenletWithLoop(TrackedRawGreenlet):
    # no doc
    def switch(self): # real signature unknown; restored from __doc__
        """ SwitchOutGreenletWithLoop.switch(self) """
        pass

    def switch_out(self): # real signature unknown; restored from __doc__
        """ SwitchOutGreenletWithLoop.switch_out(self) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    loop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """loop: object"""


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001C8A1B083F0>'


# variables with complex values

__all__ = [
    'TrackedRawGreenlet',
    'SwitchOutGreenletWithLoop',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001C8A1B425F8>'

__pyx_capi__ = {
    'BlockingSwitchOutError': None, # (!) real value is '<capsule object "PyObject *" at 0x000001C8A1C082A0>'
    '_greenlet_imported': None, # (!) real value is '<capsule object "int" at 0x000001C8A1B08360>'
    'get_objects': None, # (!) real value is '<capsule object "PyObject *" at 0x000001C8A1AB9CF0>'
    'get_reachable_greenlets': None, # (!) real value is '<capsule object "PyObject *(int __pyx_skip_dispatch)" at 0x000001C8A1B08390>'
    'wref': None, # (!) real value is '<capsule object "PyObject *" at 0x000001C8A1C08240>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='gevent.__greenlet_primitives', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001C8A1B425F8>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\gevent\\\\__greenlet_primitives.cp37-win_amd64.pyd')"

__test__ = {}

