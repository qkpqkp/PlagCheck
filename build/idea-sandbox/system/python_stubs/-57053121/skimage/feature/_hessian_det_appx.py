# encoding: utf-8
# module skimage.feature._hessian_det_appx
# from C:\Users\Doly\Anaconda3\lib\site-packages\skimage\feature\_hessian_det_appx.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py

# functions

def _hessian_matrix_det(*args, **kwargs): # real signature unknown
    """
    Computes the approximate Hessian Determinant over an image.
    
        This method uses box filters over integral images to compute the
        approximate Hessian Determinant as described in [1]_.
    
        Parameters
        ----------
        img : array
            The integral image over which to compute Hessian Determinant.
        sigma : float
            Standard deviation used for the Gaussian kernel, used for the Hessian
            matrix
    
        Returns
        -------
        out : array
            The array of the Determinant of Hessians.
    
        References
        ----------
        .. [1] Herbert Bay, Andreas Ess, Tinne Tuytelaars, Luc Van Gool,
               "SURF: Speeded Up Robust Features"
               ftp://ftp.vision.ee.ethz.ch/publications/articles/eth_biwi_00517.pdf
    
        Notes
        -----
        The running time of this method only depends on size of the image. It is
        independent of `sigma` as one would expect. The downside is that the
        result for `sigma` less than `3` is not accurate, i.e., not similar to
        the result obtained if someone computed the Hessian and took it's
        determinant.
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000002ED1BD6DFD0>'

__spec__ = None # (!) real value is "ModuleSpec(name='skimage.feature._hessian_det_appx', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000002ED1BD6DFD0>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\skimage\\\\feature\\\\_hessian_det_appx.cp37-win_amd64.pyd')"

__test__ = {}

