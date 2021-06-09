# encoding: utf-8
# module skimage.morphology._flood_fill_cy
# from C:\Users\Doly\Anaconda3\lib\site-packages\skimage\morphology\_flood_fill_cy.cp37-win_amd64.pyd
# by generator 1.147
""" Cython code used in _flood_fill.py. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

# functions

def _flood_fill_equal(*args, **kwargs): # real signature unknown
    """
    Find connected areas to fill, requiring strict equality.
    
        Parameters
        ----------
        image : ndarray, one-dimensional
            The raveled view of a n-dimensional array.
        flags : ndarray, one-dimensional
            An array of flags that is used to store the state of each pixel during
            evaluation.
        neighbor_offsets : ndarray
            A one-dimensional array that contains the offsets to find the
            connected neighbors for any index in `image`.
        start_index : int
            Start position for the flood-fill.
        seed_value :
            Value of `image[start_index]`.
    """
    pass

def _flood_fill_tolerance(*args, **kwargs): # real signature unknown
    """
    Find connected areas to fill, within a tolerance.
    
        Parameters
        ----------
        image : ndarray, one-dimensional
            The raveled view of a n-dimensional array.
        flags : ndarray, one-dimensional
            An array of flags that is used to store the state of each pixel during
            evaluation.
        neighbor_offsets : ndarray
            A one-dimensional array that contains the offsets to find the
            connected neighbors for any index in `image`.
        start_index : int
            Start position for the flood-fill.
        seed_value :
            Value of `image[start_index]`.
        low_tol :
            Lower limit for tolerance comparison.
        high_tol :
            Upper limit for tolerance comparison.
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000019F120A8B00>'

__spec__ = None # (!) real value is "ModuleSpec(name='skimage.morphology._flood_fill_cy', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000019F120A8B00>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\skimage\\\\morphology\\\\_flood_fill_cy.cp37-win_amd64.pyd')"

__test__ = {}

