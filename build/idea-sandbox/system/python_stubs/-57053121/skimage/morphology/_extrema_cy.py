# encoding: utf-8
# module skimage.morphology._extrema_cy
# from C:\Users\Doly\Anaconda3\lib\site-packages\skimage\morphology\_extrema_cy.cp37-win_amd64.pyd
# by generator 1.147
""" Cython code used in extrema.py. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

# functions

def _local_maxima(*args, **kwargs): # real signature unknown
    """
    Detect local maxima in n-dimensional array.
    
        Inner function to `local_maxima` that detects all local maxima (including
        plateaus) in the image. The result is stored inplace inside `flags` with
        the value of "QUEUED_CANDIDATE".
    
        Parameters
        ----------
        image : ndarray, one-dimensional
            The raveled view of a n-dimensional array.
        flags : ndarray
            An array of flags that is used to store the state of each pixel during
            evaluation and is MODIFIED INPLACE. Initially, pixels that border the
            image edge must be marked as "BORDER_INDEX" while all other pixels
            should be marked with "NOT_MAXIMUM".
        neighbor_offsets : ndarray
            A one-dimensional array that contains the offsets to find the
            connected neighbors for any index in `image`.
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000022439182DA0>'

__spec__ = None # (!) real value is "ModuleSpec(name='skimage.morphology._extrema_cy', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000022439182DA0>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\skimage\\\\morphology\\\\_extrema_cy.cp37-win_amd64.pyd')"

__test__ = {}

