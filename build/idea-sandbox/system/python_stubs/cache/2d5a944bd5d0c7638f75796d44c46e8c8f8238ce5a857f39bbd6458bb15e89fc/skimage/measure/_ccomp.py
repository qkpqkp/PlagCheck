# encoding: utf-8
# module skimage.measure._ccomp
# from C:\Users\Doly\Anaconda3\lib\site-packages\skimage\measure\_ccomp.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py
import numpy as __numpy


# functions

def label_cython(*args, **kwargs): # real signature unknown
    pass

def reshape_array(*args, **kwargs): # real signature unknown
    """
    "Rotates" the array so it gains a shape that the algorithm can work with.
        An illegal shape is (3, 1, 4), and correct one is (1, 3, 4) or (1, 4, 3).
        The point is to have all 1s of the shape at the beginning, not in the
        middle of the shape tuple.
    
        Note: The greater-than-one shape component should go from greatest to
        lowest numbers since it is more friendly to the CPU cache (so (1, 3, 4) is
        less optimal than (1, 4, 3). Keyword to this is "memory spatial locality"
    
        Args:
            arr (np.ndarray): The array we want to fix
    
        Returns:
            tuple (result, swaps): The result is the "fixed" array and a record
            of what has been done with it.
    """
    pass

def undo_reshape_array(*args, **kwargs): # real signature unknown
    """
    Does the opposite of what :func:`reshape_array` does
    
        Args:
            arr (np.ndarray): The array to "revert"
            swaps (list): The second result of :func:`reshape_array`
    
        Returns:
            np.ndarray: The array of the original shape
    """
    pass

def warn(message, category=None, stacklevel=2): # reliably restored by inspect
    """ A version of `warnings.warn` with a default stacklevel of 2. """
    pass

def _apply_swaps(*args, **kwargs): # real signature unknown
    pass

def _get_swaps(*args, **kwargs): # real signature unknown
    """
    What axes to swap if we want to convert an illegal array shape
        to a legal one.
    
        Args:
            shp (tuple-like): The array shape
    
        Returns:
            list: List of tuples to be passed to np.swapaxes
    """
    pass

# classes

class DTYPE(__numpy.signedinteger):
    """
    Signed integer type, compatible with C ``long long``.
        Character code: ``'q'``.
        Canonical name: ``np.longlong``.
        Alias *on this platform*: ``np.int64``: 64-bit signed integer (-9223372036854775808 to 9223372036854775807).
        Alias *on this platform*: ``np.intp``: Signed integer large enough to fit pointer, compatible with C ``intptr_t``.
    """
    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000026C0EC22470>'

__pyx_capi__ = {
    'find_root': None, # (!) real value is '<capsule object "__pyx_t_7skimage_7measure_6_ccomp_DTYPE_t (__pyx_t_7skimage_7measure_6_ccomp_DTYPE_t *, __pyx_t_7skimage_7measure_6_ccomp_DTYPE_t)" at 0x0000026C0EBB69C0>'
    'join_trees': None, # (!) real value is '<capsule object "void (__pyx_t_7skimage_7measure_6_ccomp_DTYPE_t *, __pyx_t_7skimage_7measure_6_ccomp_DTYPE_t, __pyx_t_7skimage_7measure_6_ccomp_DTYPE_t)" at 0x0000026C0EBB6A20>'
    'set_root': None, # (!) real value is '<capsule object "void (__pyx_t_7skimage_7measure_6_ccomp_DTYPE_t *, __pyx_t_7skimage_7measure_6_ccomp_DTYPE_t, __pyx_t_7skimage_7measure_6_ccomp_DTYPE_t)" at 0x0000026C0EBB69F0>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='skimage.measure._ccomp', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000026C0EC22470>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\skimage\\\\measure\\\\_ccomp.cp37-win_amd64.pyd')"

__test__ = {}

