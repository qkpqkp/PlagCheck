# encoding: utf-8
# module gevent.__abstract_linkable
# from C:\Users\Doly\Anaconda3\lib\site-packages\gevent\__abstract_linkable.cp37-win_amd64.pyd
# by generator 1.147
""" Internal module, support for the linkable protocol for "event" like objects. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import sys as sys # <module 'sys' (built-in)>
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

# classes

class AbstractLinkable(object):
    """ AbstractLinkable() """
    def linkcount(self): # real signature unknown; restored from __doc__
        """ AbstractLinkable.linkcount(self) """
        pass

    def rawlink(self, callback): # real signature unknown; restored from __doc__
        """
        AbstractLinkable.rawlink(self, callback)
        
                Register a callback to call when this object is ready.
        
                *callback* will be called in the :class:`Hub
                <gevent.hub.Hub>`, so it must not use blocking gevent API.
                *callback* will be passed one argument: this instance.
        """
        pass

    def ready(self): # real signature unknown; restored from __doc__
        """ AbstractLinkable.ready(self) -> bool """
        return False

    def unlink(self, callback): # real signature unknown; restored from __doc__
        """
        AbstractLinkable.unlink(self, callback)
        Remove the callback set by :meth:`rawlink`
        """
        pass

    def _notify_links(self): # real signature unknown; restored from __doc__
        """ AbstractLinkable._notify_links(self) """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    hub = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000024B60445630>'
    __slots__ = (
        'hub',
        '_links',
        '_notifier',
        '_notify_all',
        '__weakref__',
    )


# variables with complex values

__all__ = [
    'AbstractLinkable',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000024B604D5160>'

__pyx_capi__ = {
    'InvalidSwitchError': None, # (!) real value is '<capsule object "PyObject *" at 0x0000024B60399750>'
    'Timeout': None, # (!) real value is '<capsule object "PyObject *" at 0x0000024B604455A0>'
    '_greenlet_imported': None, # (!) real value is '<capsule object "int" at 0x0000024B604455D0>'
    '_init': None, # (!) real value is '<capsule object "void (void)" at 0x0000024B60445600>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='gevent.__abstract_linkable', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000024B604D5160>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\gevent\\\\__abstract_linkable.cp37-win_amd64.pyd')"

__test__ = {}

