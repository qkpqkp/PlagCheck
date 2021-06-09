# encoding: utf-8
# module tables.indexesextension
# from C:\Users\Doly\Anaconda3\lib\site-packages\tables\indexesextension.cp37-win_amd64.pyd
# by generator 1.147
"""
cython interface for keeping indexes classes.

Classes (type extensions):

    IndexArray
    CacheArray
    LastRowArray

Functions:

    keysort

Misc variables:
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as numpy # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py
import tables.hdf5extension as __tables_hdf5extension


# functions

def keysort(*args, **kwargs): # real signature unknown
    """
    Sort array1 in-place. array2 is also sorted following the array1 order.
    
        array1 can be of any type, except complex or string.  array2 may be made of
        elements on any size.
    """
    pass

def _bisect_left(*args, **kwargs): # real signature unknown
    """
    Return the index where to insert item x in list a, assuming a is sorted.
    
      The return value i is such that all e in a[:i] have e < x, and all e in
      a[i:] have e >= x.  So if x already appears in the list, i points just
      before the leftmost x already there.
    """
    pass

def _bisect_right(*args, **kwargs): # real signature unknown
    """
    Return the index where to insert item x in list a, assuming a is sorted.
    
      The return value i is such that all e in a[:i] have e <= x, and all e in
      a[i:] have e > x.  So if x already appears in the list, i points just
      beyond the rightmost x already there.
    """
    pass

def __pyx_unpickle_Index(*args, **kwargs): # real signature unknown
    pass

# classes

class CacheArray(__tables_hdf5extension.Array):
    """ Container for keeping index caches of 1st and 2nd level. """
    def _g_close(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000017E0F5404B0>'


class HDF5ExtError(RuntimeError):
    """
    A low level HDF5 operation failed.
    
        This exception is raised the low level PyTables components used for
        accessing HDF5 files.  It usually signals that something is not
        going well in the HDF5 library or even at the Input/Output level.
    
        Errors in the HDF5 C library may be accompanied by an extensive
        HDF5 back trace on standard error (see also
        :func:`tables.silence_hdf5_messages`).
    
        .. versionchanged:: 2.4
    
        Parameters
        ----------
        message
            error message
        h5bt
            This parameter (keyword only) controls the HDF5 back trace
            handling. Any keyword arguments other than h5bt is ignored.
    
            * if set to False the HDF5 back trace is ignored and the
              :attr:`HDF5ExtError.h5backtrace` attribute is set to None
            * if set to True the back trace is retrieved from the HDF5
              library and stored in the :attr:`HDF5ExtError.h5backtrace`
              attribute as a list of tuples
            * if set to "VERBOSE" (default) the HDF5 back trace is
              stored in the :attr:`HDF5ExtError.h5backtrace` attribute
              and also included in the string representation of the
              exception
            * if not set (or set to None) the default policy is used
              (see :attr:`HDF5ExtError.DEFAULT_H5_BACKTRACE_POLICY`)
    """
    def format_h5_backtrace(self, backtrace=None): # reliably restored by inspect
        """
        Convert the HDF5 trace back represented as a list of tuples.
                (see :attr:`HDF5ExtError.h5backtrace`) into a string.
        
                .. versionadded:: 2.4
        """
        pass

    @classmethod
    def set_policy_from_env(cls, *args, **kwargs): # real signature unknown
        pass

    def _dump_h5_backtrace(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def __str__(self): # reliably restored by inspect
        """
        Returns a sting representation of the exception.
        
                The actual result depends on policy set in the initializer
                :meth:`HDF5ExtError.__init__`.
        
                .. versionadded:: 2.4
        """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    DEFAULT_H5_BACKTRACE_POLICY = 'VERBOSE'


class Index(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass


class IndexArray(__tables_hdf5extension.Array):
    """ Container for keeping sorted and indices values. """
    def _g_close(self, *args, **kwargs): # real signature unknown
        pass

    def _init_sorted_slice(self, *args, **kwargs): # real signature unknown
        """ Initialize the structures for doing a binary search. """
        pass

    def _read_index_slice(self, *args, **kwargs): # real signature unknown
        pass

    def _read_sorted_slice(self, *args, **kwargs): # real signature unknown
        """ Read the sorted part of an index. """
        pass

    def _search_bin_na_b(self, *args, **kwargs): # real signature unknown
        pass

    def _search_bin_na_d(self, *args, **kwargs): # real signature unknown
        pass

    def _search_bin_na_e(self, *args, **kwargs): # real signature unknown
        pass

    def _search_bin_na_f(self, *args, **kwargs): # real signature unknown
        pass

    def _search_bin_na_g(self, *args, **kwargs): # real signature unknown
        pass

    def _search_bin_na_i(self, *args, **kwargs): # real signature unknown
        pass

    def _search_bin_na_ll(self, *args, **kwargs): # real signature unknown
        pass

    def _search_bin_na_s(self, *args, **kwargs): # real signature unknown
        pass

    def _search_bin_na_ub(self, *args, **kwargs): # real signature unknown
        pass

    def _search_bin_na_ui(self, *args, **kwargs): # real signature unknown
        pass

    def _search_bin_na_ull(self, *args, **kwargs): # real signature unknown
        pass

    def _search_bin_na_us(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000017E0F5404E0>'


class LastRowArray(__tables_hdf5extension.Array):
    """ Container for keeping sorted and indices values of last rows of an index. """
    def _read_index_slice(self, *args, **kwargs): # real signature unknown
        """ Read the reverse index part of an LR index. """
        pass

    def _read_sorted_slice(self, *args, **kwargs): # real signature unknown
        """ Read the sorted part of an LR index. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000017E0F540510>'


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000017E0F558048>'

__spec__ = None # (!) real value is "ModuleSpec(name='tables.indexesextension', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000017E0F558048>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\tables\\\\indexesextension.cp37-win_amd64.pyd')"

__test__ = {}

