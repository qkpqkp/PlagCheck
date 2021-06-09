# encoding: utf-8
# module tables.linkextension
# from C:\Users\Doly\Anaconda3\lib\site-packages\tables\linkextension.cp37-win_amd64.pyd
# by generator 1.147
""" Cython functions and classes for supporting links in HDF5. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import tables.hdf5extension as __tables_hdf5extension


# functions

def _get_link_class(*args, **kwargs): # real signature unknown
    """ Guess the link class. """
    pass

def _g_create_hard_link(*args, **kwargs): # real signature unknown
    """ Create a hard link in the file. """
    pass

def __pyx_unpickle_ExternalLink(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Link(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_SoftLink(*args, **kwargs): # real signature unknown
    pass

# classes

class Link(__tables_hdf5extension.Node):
    """ Extension class from which all link extensions inherits. """
    def _g_copy(self, *args, **kwargs): # real signature unknown
        """ Private part for the _f_copy() method. """
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


class ExternalLink(Link):
    """ Extension class representing an external link. """
    def _g_create(self, *args, **kwargs): # real signature unknown
        """ Create the link in file. """
        pass

    def _g_open(self, *args, **kwargs): # real signature unknown
        """ Open the link in file. """
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


class SoftLink(Link):
    """ Extension class representing a soft link. """
    def _g_create(self, *args, **kwargs): # real signature unknown
        """ Create the link in file. """
        pass

    def _g_open(self, *args, **kwargs): # real signature unknown
        """ Open the link in file. """
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


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000018E3E1099B0>'

__spec__ = None # (!) real value is "ModuleSpec(name='tables.linkextension', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000018E3E1099B0>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\tables\\\\linkextension.cp37-win_amd64.pyd')"

__test__ = {}

