# encoding: utf-8
# module skimage.morphology._skeletonize_cy
# from C:\Users\Doly\Anaconda3\lib\site-packages\skimage\morphology\_skeletonize_cy.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py

# functions

def _fast_skeletonize(*args, **kwargs): # real signature unknown
    """
    Optimized parts of the Zhang-Suen [1]_ skeletonization.
        Iteratively, pixels meeting removal criteria are removed,
        till only the skeleton remains (that is, no further removable pixel
        was found).
    
        Performs a hard-coded correlation to assign every neighborhood of 8 a
        unique number, which in turn is used in conjunction with a look up
        table to select the appropriate thinning criteria.
    
        Parameters
        ----------
        image : numpy.ndarray
            A binary image containing the objects to be skeletonized. '1'
            represents foreground, and '0' represents background.
    
        Returns
        -------
        skeleton : ndarray
            A matrix containing the thinned image.
    
        References
        ----------
        .. [1] A fast parallel algorithm for thinning digital patterns,
               T. Y. Zhang and C. Y. Suen, Communications of the ACM,
               March 1984, Volume 27, Number 3.
    """
    pass

def _skeletonize_loop(*args, **kwargs): # real signature unknown
    """
    Inner loop of skeletonize function
    
        Parameters
        ----------
    
        result : ndarray of uint8
            On input, the image to be skeletonized, on output the skeletonized
            image.
    
        i, j : ndarrays
            The coordinates of each foreground pixel in the image
    
        order : ndarray
            The index of each pixel, in the order of processing (order[0] is
            the first pixel to process, etc.)
    
        table : ndarray
            The 512-element lookup table of values after transformation
            (whether to keep or not each configuration in a binary 3x3 array)
    
        Notes
        -----
    
        The loop determines whether each pixel in the image can be removed without
        changing the Euler number of the image. The pixels are ordered by
        increasing distance from the background which means a point nearer to
        the quench-line of the brushfire will be evaluated later than a
        point closer to the edge.
    
        Note that the neighbourhood of a pixel may evolve before the loop
        arrives at this pixel. This is why it is possible to compute the
        skeleton in only one pass, thanks to an adapted ordering of the
        pixels.
    """
    pass

def _table_lookup_index(*args, **kwargs): # real signature unknown
    """
    Return an index into a table per pixel of a binary image
    
        Take the sum of true neighborhood pixel values where the neighborhood
        looks like this::
    
           1   2   4
           8  16  32
          64 128 256
    
        This code could be replaced by a convolution with the kernel::
    
          256 128 64
           32  16  8
            4   2  1
    
        but this runs about twice as fast because of inlining and the
        hardwired kernel.
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000211550C9DA0>'

__spec__ = None # (!) real value is "ModuleSpec(name='skimage.morphology._skeletonize_cy', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000211550C9DA0>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\skimage\\\\morphology\\\\_skeletonize_cy.cp37-win_amd64.pyd')"

__test__ = {}

