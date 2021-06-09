# encoding: utf-8
# module gevent._local
# from C:\Users\Doly\Anaconda3\lib\site-packages\gevent\_local.cp37-win_amd64.pyd
# by generator 1.147
"""
Greenlet-local objects.

This module is based on `_threading_local.py`__ from the standard
library of Python 3.4.

__ https://github.com/python/cpython/blob/3.4/Lib/_threading_local.py

Greenlet-local objects support the management of greenlet-local data.
If you have data that you want to be local to a greenlet, simply create
a greenlet-local object and use its attributes:

  >>> mydata = local()
  >>> mydata.number = 42
  >>> mydata.number
  42

You can also access the local-object's dictionary:

  >>> mydata.__dict__
  {'number': 42}
  >>> mydata.__dict__.setdefault('widgets', [])
  []
  >>> mydata.widgets
  []

What's important about greenlet-local objects is that their data are
local to a greenlet. If we access the data in a different greenlet:

  >>> log = []
  >>> def f():
  ...     items = list(mydata.__dict__.items())
  ...     items.sort()
  ...     log.append(items)
  ...     mydata.number = 11
  ...     log.append(mydata.number)
  >>> greenlet = gevent.spawn(f)
  >>> greenlet.join()
  >>> log
  [[], 11]

we get different data.  Furthermore, changes made in the other greenlet
don't affect data seen in this greenlet:

  >>> mydata.number
  42

Of course, values you get from a local object, including a __dict__
attribute, are for whatever greenlet was current at the time the
attribute was read.  For that reason, you generally don't want to save
these values across greenlets, as they apply only to the greenlet they
came from.

You can create custom local objects by subclassing the local class:

  >>> class MyLocal(local):
  ...     number = 2
  ...     initialized = False
  ...     def __init__(self, **kw):
  ...         if self.initialized:
  ...             raise SystemError('__init__ called too many times')
  ...         self.initialized = True
  ...         self.__dict__.update(kw)
  ...     def squared(self):
  ...         return self.number ** 2

This can be useful to support default values, methods and
initialization.  Note that if you define an __init__ method, it will be
called each time the local object is used in a separate greenlet.  This
is necessary to initialize each greenlet's dictionary.

Now if we create a local object:

  >>> mydata = MyLocal(color='red')

Now we have a default number:

  >>> mydata.number
  2

an initial color:

  >>> mydata.color
  'red'
  >>> del mydata.color

And a method that operates on the data:

  >>> mydata.squared()
  4

As before, we can access the data in a separate greenlet:

  >>> log = []
  >>> greenlet = gevent.spawn(f)
  >>> greenlet.join()
  >>> log
  [[('color', 'red'), ('initialized', True)], 11]

without affecting this greenlet's data:

  >>> mydata.number
  2
  >>> mydata.color
  Traceback (most recent call last):
  ...
  AttributeError: 'MyLocal' object has no attribute 'color'

Note that subclasses can define slots, but they are not greenlet
local. They are shared across greenlets::

  >>> class MyLocal(local):
  ...     __slots__ = 'number'

  >>> mydata = MyLocal()
  >>> mydata.number = 42
  >>> mydata.color = 'red'

So, the separate greenlet:

  >>> greenlet = gevent.spawn(f)
  >>> greenlet.join()

affects what we see:

  >>> mydata.number
  11

>>> del mydata

.. versionchanged:: 1.1a2
   Update the implementation to match Python 3.4 instead of Python 2.5.
   This results in locals being eligible for garbage collection as soon
   as their greenlet exits.

.. versionchanged:: 1.2.3
   Use a weak-reference to clear the greenlet link we establish in case
   the local object dies before the greenlet does.

.. versionchanged:: 1.3a1
   Implement the methods for attribute access directly, handling
   descriptors directly here. This allows removing the use of a lock
   and facilitates greatly improved performance.

.. versionchanged:: 1.3a1
   The ``__init__`` method of subclasses of ``local`` is no longer
   called with a lock held. CPython does not use such a lock in its
   native implementation. This could potentially show as a difference
   if code that uses multiple dependent attributes in ``__slots__``
   (which are shared across all greenlets) switches during ``__init__``.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
from greenlet import getcurrent


# functions

def all_local_dicts_for_greenlet(greenlet_greenlet): # real signature unknown; restored from __doc__
    """
    all_local_dicts_for_greenlet(greenlet greenlet)
    
        Internal debug helper for getting the local values associated
        with a greenlet. This is subject to change or removal at any time.
    
        :return: A list of ((type, id), {}) pairs, where the first element
          is the type and id of the local object and the second object is its
          instance dictionary, as seen from this greenlet.
    
        .. versionadded:: 1.3a2
    """
    pass

def greenlet_init(*args, **kwargs): # real signature unknown
    pass

def import_c_accel(globs, cname): # reliably restored by inspect
    """
    Import the C-accelerator for the __name__
        and copy its globals.
    """
    pass

@staticmethod # known case of __new__
def __new__(cls, *args, **kw): # real signature unknown; restored from __doc__
    """ __new__(cls, *args, **kw) """
    pass

# classes

class local(object):
    """ An object whose attributes are greenlet-local. """
    def __copy__(self): # real signature unknown; restored from __doc__
        """ local.__copy__(self) -> local """
        return local

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000264B1F757E0>'
    __slots__ = (
        '_local_type_get_descriptors',
        '_local_type_set_or_del_descriptors',
        '_local_type_del_descriptors',
        '_local__impl',
        '_local_type_set_descriptors',
        '_local_type_vars',
        '_local_type',
    )


class _greenlet_deleted(object):
    """
    _greenlet_deleted(idt, wrdicts)
    
        A weakref callback for when the greenlet
        is deleted.
    
        If the greenlet is a `gevent.greenlet.Greenlet` and
        supplies ``rawlink``, that will be used instead of a
        weakref.
    """
    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __init__(self, idt, wrdicts): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __slots__ = (
        'idt',
        'wrdicts',
    )


class _localimpl(object):
    """
    _localimpl(args, kwargs, local_type, id_local)
    A class managing thread-local dicts
    """
    def __init__(self, args, kwargs, local_type, id_local): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __slots__ = (
        'key',
        'dicts',
        'localargs',
        'localkwargs',
        'localtypeid',
        '__weakref__',
    )


class _localimpl_dict_entry(object):
    """
    _localimpl_dict_entry(wrgreenlet, localdict)
    
        The object that goes in the ``dicts`` of ``_localimpl``
        object for each thread.
    """
    def __init__(self, wrgreenlet, localdict): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __slots__ = (
        'wrgreenlet',
        'localdict',
    )


class _local_deleted(object):
    """ _local_deleted(key, wrthread, greenlet_deleted) """
    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __init__(self, key, wrthread, greenlet_deleted): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __slots__ = (
        'key',
        'wrthread',
        'greenlet_deleted',
    )


class _wrefdict(dict):
    """ A dict that can be weak referenced """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


# variables with complex values

__all__ = [
    'local',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000264B20200B8>'

__pyx_capi__ = {
    '_PYPY': None, # (!) real value is '<capsule object "int" at 0x00000264B1EC9750>'
    '_greenlet_imported': None, # (!) real value is '<capsule object "int" at 0x00000264B1F75660>'
    '_init': None, # (!) real value is '<capsule object "void (void)" at 0x00000264B1F756C0>'
    '_local__copy_dict_from': None, # (!) real value is '<capsule object "PyObject *(struct __pyx_obj_6gevent_6_local_local *, struct __pyx_obj_6gevent_6_local__localimpl *, PyObject *)" at 0x00000264B1F75750>'
    '_local_attrs': None, # (!) real value is '<capsule object "PyObject *" at 0x00000264B1F75690>'
    '_local_find_descriptors': None, # (!) real value is '<capsule object "PyObject *(struct __pyx_obj_6gevent_6_local_local *)" at 0x00000264B1F75780>'
    '_local_get_dict': None, # (!) real value is '<capsule object "PyObject *(struct __pyx_obj_6gevent_6_local_local *)" at 0x00000264B1F75720>'
    '_localimpl_create_dict': None, # (!) real value is '<capsule object "PyObject *(struct __pyx_obj_6gevent_6_local__localimpl *, PyGreenlet *, PyObject *)" at 0x00000264B1F756F0>'
    '_marker': None, # (!) real value is '<capsule object "PyObject *" at 0x00000264B1F75600>'
    'all_local_dicts_for_greenlet': None, # (!) real value is '<capsule object "PyObject *(PyGreenlet *, int __pyx_skip_dispatch)" at 0x00000264B1F757B0>'
    'copy': None, # (!) real value is '<capsule object "PyObject *" at 0x00000264B1F755D0>'
    'key_prefix': None, # (!) real value is '<capsule object "PyObject *" at 0x00000264B1F75630>'
    'ref': None, # (!) real value is '<capsule object "PyObject *" at 0x00000264B1F755A0>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='gevent._local', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000264B20200B8>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\gevent\\\\_local.cp37-win_amd64.pyd')"

__test__ = {}

