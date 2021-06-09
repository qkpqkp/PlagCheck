# encoding: utf-8
# module pandas._libs.missing
# from C:\Users\Doly\Anaconda3\lib\site-packages\pandas\_libs\missing.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numbers as numbers # C:\Users\Doly\Anaconda3\lib\numbers.py
import numpy as np # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py
from pandas._libs.ops_dispatch import maybe_dispatch_ufunc_to_dunder_op


# functions

def checknull(*args, **kwargs): # real signature unknown
    """
    Return boolean describing of the input is NA-like, defined here as any
        of:
         - None
         - nan
         - NaT
         - np.datetime64 representation of NaT
         - np.timedelta64 representation of NaT
    
        Parameters
        ----------
        val : object
    
        Returns
        -------
        result : bool
    
        Notes
        -----
        The difference between `checknull` and `checknull_old` is that `checknull`
        does *not* consider INF or NEGINF to be NA.
    """
    pass

def checknull_old(*args, **kwargs): # real signature unknown
    """
    Return boolean describing of the input is NA-like, defined here as any
        of:
         - None
         - nan
         - INF
         - NEGINF
         - NaT
         - np.datetime64 representation of NaT
         - np.timedelta64 representation of NaT
    
        Parameters
        ----------
        val : object
    
        Returns
        -------
        result : bool
    
        Notes
        -----
        The difference between `checknull` and `checknull_old` is that `checknull`
        does *not* consider INF or NEGINF to be NA.
    """
    pass

def isnaobj(*args, **kwargs): # real signature unknown
    """
    Return boolean mask denoting which elements of a 1-D array are na-like,
        according to the criteria defined in `checknull`:
         - None
         - nan
         - NaT
         - np.datetime64 representation of NaT
         - np.timedelta64 representation of NaT
    
        Parameters
        ----------
        arr : ndarray
    
        Returns
        -------
        result : ndarray (dtype=np.bool_)
    """
    pass

def isnaobj2d(*args, **kwargs): # real signature unknown
    """
    Return boolean mask denoting which elements of a 2-D array are na-like,
        according to the criteria defined in `checknull`:
         - None
         - nan
         - NaT
         - np.datetime64 representation of NaT
         - np.timedelta64 representation of NaT
    
        Parameters
        ----------
        arr : ndarray
    
        Returns
        -------
        result : ndarray (dtype=np.bool_)
    
        Notes
        -----
        The difference between `isnaobj2d` and `isnaobj2d_old` is that `isnaobj2d`
        does *not* consider INF or NEGINF to be NA.
    """
    pass

def isnaobj2d_old(*args, **kwargs): # real signature unknown
    """
    Return boolean mask denoting which elements of a 2-D array are na-like,
        according to the criteria defined in `checknull_old`:
         - None
         - nan
         - INF
         - NEGINF
         - NaT
         - np.datetime64 representation of NaT
         - np.timedelta64 representation of NaT
    
        Parameters
        ----------
        arr : ndarray
    
        Returns
        -------
        result : ndarray (dtype=np.bool_)
    
        Notes
        -----
        The difference between `isnaobj2d` and `isnaobj2d_old` is that `isnaobj2d`
        does *not* consider INF or NEGINF to be NA.
    """
    pass

def isnaobj_old(*args, **kwargs): # real signature unknown
    """
    Return boolean mask denoting which elements of a 1-D array are na-like,
        defined as being any of:
         - None
         - nan
         - INF
         - NEGINF
         - NaT
    
        Parameters
        ----------
        arr : ndarray
    
        Returns
        -------
        result : ndarray (dtype=np.bool_)
    """
    pass

def isneginf_scalar(*args, **kwargs): # real signature unknown
    pass

def isposinf_scalar(*args, **kwargs): # real signature unknown
    pass

def is_platform_32bit(): # reliably restored by inspect
    """
    Checking if the running platform is 32-bit.
    
        Returns
        -------
        bool
            True if the running platform is 32-bit.
    """
    pass

def _create_binary_propagating_op(*args, **kwargs): # real signature unknown
    pass

def _create_unary_propagating_op(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_C_NAType(*args, **kwargs): # real signature unknown
    pass

# classes

class C_NAType(object):
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


class NAType(C_NAType):
    """
    NA ("not available") missing value indicator.
    
        .. warning::
    
           Experimental: the behaviour of NA can still change without warning.
    
        .. versionadded:: 1.0.0
    
        The NA singleton is a missing value indicator defined by pandas. It is
        used in certain new extension dtypes (currently the "string" dtype).
    """
    def __abs__(self, *args, **kwargs): # real signature unknown
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        pass

    def __array_ufunc__(self, *args, **kwargs): # real signature unknown
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        pass

    def __matmul__(self, *args, **kwargs): # real signature unknown
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        pass

    def __rmatmul__(self, *args, **kwargs): # real signature unknown
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _HANDLED_TYPES = (
        np.ndarray,
        numbers.Number,
        str,
        np.bool8,
    )
    _instance = None # (!) forward: NA, real value is '<NA>'
    __array_priority__ = 1000
    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pandas._libs.missing\', \'__doc__\': \'\\n    NA ("not available") missing value indicator.\\n\\n    .. warning::\\n\\n       Experimental: the behaviour of NA can still change without warning.\\n\\n    .. versionadded:: 1.0.0\\n\\n    The NA singleton is a missing value indicator defined by pandas. It is\\n    used in certain new extension dtypes (currently the "string" dtype).\\n    \', \'_instance\': <NA>, \'__new__\': <cyfunction NAType.__new__ at 0x000001EADA3E9498>, \'__repr__\': <cyfunction NAType.__repr__ at 0x000001EADA3E9550>, \'__bool__\': <cyfunction NAType.__bool__ at 0x000001EADA3E9608>, \'__hash__\': <cyfunction NAType.__hash__ at 0x000001EADA3E96C0>, \'__reduce__\': <cyfunction NAType.__reduce__ at 0x000001EADA3E9778>, \'__add__\': <cyfunction _create_binary_propagating_op.<locals>.method at 0x000001EADA3E9830>, \'__radd__\': <cyfunction _create_binary_propagating_op.<locals>.method at 0x000001EADA3E98E8>, \'__sub__\': <cyfunction _create_binary_propagating_op.<locals>.method at 0x000001EADA3E99A0>, \'__rsub__\': <cyfunction _create_binary_propagating_op.<locals>.method at 0x000001EADA3E9A58>, \'__mul__\': <cyfunction _create_binary_propagating_op.<locals>.method at 0x000001EADA3E9B10>, \'__rmul__\': <cyfunction _create_binary_propagating_op.<locals>.method at 0x000001EADA3E9BC8>, \'__matmul__\': <cyfunction _create_binary_propagating_op.<locals>.method at 0x000001EADA3E9C80>, \'__rmatmul__\': <cyfunction _create_binary_propagating_op.<locals>.method at 0x000001EADA3E9D38>, \'__truediv__\': <cyfunction _create_binary_propagating_op.<locals>.method at 0x000001EADA3E9DF0>, \'__rtruediv__\': <cyfunction _create_binary_propagating_op.<locals>.method at 0x000001EADA3E9EA8>, \'__floordiv__\': <cyfunction _create_binary_propagating_op.<locals>.method at 0x000001EADA3E9F60>, \'__rfloordiv__\': <cyfunction _create_binary_propagating_op.<locals>.method at 0x000001EADA40F048>, \'__mod__\': <cyfunction _create_binary_propagating_op.<locals>.method at 0x000001EADA40F100>, \'__rmod__\': <cyfunction _create_binary_propagating_op.<locals>.method at 0x000001EADA40F1B8>, \'__divmod__\': <cyfunction _create_binary_propagating_op.<locals>.method at 0x000001EADA40F270>, \'__rdivmod__\': <cyfunction _create_binary_propagating_op.<locals>.method at 0x000001EADA40F328>, \'__eq__\': <cyfunction _create_binary_propagating_op.<locals>.method at 0x000001EADA40F3E0>, \'__ne__\': <cyfunction _create_binary_propagating_op.<locals>.method at 0x000001EADA40F498>, \'__le__\': <cyfunction _create_binary_propagating_op.<locals>.method at 0x000001EADA40F550>, \'__lt__\': <cyfunction _create_binary_propagating_op.<locals>.method at 0x000001EADA40F608>, \'__gt__\': <cyfunction _create_binary_propagating_op.<locals>.method at 0x000001EADA40F6C0>, \'__ge__\': <cyfunction _create_binary_propagating_op.<locals>.method at 0x000001EADA40F778>, \'__neg__\': <cyfunction _create_unary_propagating_op.<locals>.method at 0x000001EADA40F830>, \'__pos__\': <cyfunction _create_unary_propagating_op.<locals>.method at 0x000001EADA40F8E8>, \'__abs__\': <cyfunction _create_unary_propagating_op.<locals>.method at 0x000001EADA40F9A0>, \'__invert__\': <cyfunction _create_unary_propagating_op.<locals>.method at 0x000001EADA40FA58>, \'__pow__\': <cyfunction NAType.__pow__ at 0x000001EADA40FB10>, \'__rpow__\': <cyfunction NAType.__rpow__ at 0x000001EADA40FBC8>, \'__and__\': <cyfunction NAType.__and__ at 0x000001EADA40FC80>, \'__rand__\': <cyfunction NAType.__and__ at 0x000001EADA40FC80>, \'__or__\': <cyfunction NAType.__or__ at 0x000001EADA40FD38>, \'__ror__\': <cyfunction NAType.__or__ at 0x000001EADA40FD38>, \'__xor__\': <cyfunction NAType.__xor__ at 0x000001EADA40FDF0>, \'__rxor__\': <cyfunction NAType.__xor__ at 0x000001EADA40FDF0>, \'__array_priority__\': 1000, \'_HANDLED_TYPES\': (<class \'numpy.ndarray\'>, <class \'numbers.Number\'>, <class \'str\'>, <class \'numpy.bool_\'>), \'__array_ufunc__\': <cyfunction NAType.__array_ufunc__ at 0x000001EADA40FEA8>, \'__dict__\': <attribute \'__dict__\' of \'NAType\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'NAType\' objects>})'


# variables with complex values

NA = None # (!) real value is '<NA>'

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001EADA4037F0>'

__pyx_capi__ = {
    'C_NA': None, # (!) real value is '<capsule object "struct __pyx_obj_6pandas_5_libs_7missing_C_NAType *" at 0x000001EADA3E5AE0>'
    'checknull': None, # (!) real value is '<capsule object "int (PyObject *, int __pyx_skip_dispatch)" at 0x000001EADA3E5B10>'
    'checknull_old': None, # (!) real value is '<capsule object "int (PyObject *, int __pyx_skip_dispatch)" at 0x000001EADA3E5B40>'
    'is_null_datetime64': None, # (!) real value is '<capsule object "int (PyObject *)" at 0x000001EADA3E5BA0>'
    'is_null_period': None, # (!) real value is '<capsule object "int (PyObject *)" at 0x000001EADA3E5C00>'
    'is_null_timedelta64': None, # (!) real value is '<capsule object "int (PyObject *)" at 0x000001EADA3E5BD0>'
    'isnaobj': None, # (!) real value is '<capsule object "PyArrayObject *(PyArrayObject *, int __pyx_skip_dispatch)" at 0x000001EADA3E5B70>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.missing', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001EADA4037F0>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\pandas\\\\_libs\\\\missing.cp37-win_amd64.pyd')"

__test__ = {}

