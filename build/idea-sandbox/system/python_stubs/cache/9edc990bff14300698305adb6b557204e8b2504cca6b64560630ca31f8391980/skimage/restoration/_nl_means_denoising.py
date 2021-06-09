# encoding: utf-8
# module skimage.restoration._nl_means_denoising
# from C:\Users\Doly\Anaconda3\lib\site-packages\skimage\restoration\_nl_means_denoising.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py

# functions

def _fast_nl_means_denoising_2d(*args, **kwargs): # real signature unknown
    """
    Perform fast non-local means denoising on 2-D array, with the outer
        loop on patch shifts in order to reduce the number of operations.
    
        Parameters
        ----------
        image : ndarray
            2-D input data to be denoised, grayscale or RGB.
        s : int, optional
            Size of patches used for denoising.
        d : int, optional
            Maximal distance in pixels where to search patches used for denoising.
        h : double, optional
            Cut-off distance (in gray levels). The higher h, the more permissive
            one is in accepting patches.
        var : double
            Expected noise variance.  If non-zero, this is used to reduce the
            apparent patch distances by the expected distance due to the noise.
    
        Returns
        -------
        result : ndarray
            Denoised image, of same shape as input image.
    
        References
        ----------
        J. Darbon, A. Cunha, T.F. Chan, S. Osher, and G.J. Jensen, Fast
        nonlocal filtering applied to electron cryomicroscopy, in 5th IEEE
        International Symposium on Biomedical Imaging: From Nano to Macro,
        2008, pp. 1331-1334.
    
        Jacques Froment. Parameter-Free Fast Pixelwise Non-Local Means
        Denoising. Image Processing On Line, 2014, vol. 4, p. 300-326.
    """
    pass

def _fast_nl_means_denoising_3d(*args, **kwargs): # real signature unknown
    """
    Perform fast non-local means denoising on 3-D array, with the outer
        loop on patch shifts in order to reduce the number of operations.
    
        Parameters
        ----------
        image : ndarray
            3-D input data to be denoised.
        s : int, optional
            Size of patches used for denoising.
        d : int, optional
            Maximal distance in pixels where to search patches used for denoising.
        h : double, optional
            cut-off distance (in gray levels). The higher h, the more permissive
            one is in accepting patches.
        var : double
            Expected noise variance.  If non-zero, this is used to reduce the
            apparent patch distances by the expected distance due to the noise.
    
        Returns
        -------
        result : ndarray
            Denoised image, of same shape as input image.
    
        References
        ----------
        J. Darbon, A. Cunha, T.F. Chan, S. Osher, and G.J. Jensen, Fast
        nonlocal filtering applied to electron cryomicroscopy, in 5th IEEE
        International Symposium on Biomedical Imaging: From Nano to Macro,
        2008, pp. 1331-1334.
    
        Jacques Froment. Parameter-Free Fast Pixelwise Non-Local Means
        Denoising. Image Processing On Line, 2014, vol. 4, p. 300-326.
    """
    pass

def _nl_means_denoising_2d(*args, **kwargs): # real signature unknown
    """
    Perform non-local means denoising on 2-D RGB image
    
        Parameters
        ----------
        image : ndarray
            Input RGB image to be denoised
        s : int, optional
            Size of patches used for denoising
        d : int, optional
            Maximal distance in pixels where to search patches used for denoising
        h : double, optional
            Cut-off distance (in gray levels). The higher h, the more permissive
            one is in accepting patches.
        var : double
            Expected noise variance.  If non-zero, this is used to reduce the
            apparent patch distances by the expected distance due to the noise.
    
        Notes
        -----
        This function operates on 2D grayscale and multichannel images.  For
        2D grayscale images, the input should be 3D with size 1 along the last
        axis.  The code is compatible with an arbitrary number of channels.
    
        Returns
        -------
        result : ndarray
            Denoised image, of same shape as input image.
    """
    pass

def _nl_means_denoising_3d(*args, **kwargs): # real signature unknown
    """
    Perform non-local means denoising on 3-D array
    
        Parameters
        ----------
        image : ndarray
            Input data to be denoised.
        s : int, optional
            Size of patches used for denoising.
        d : int, optional
            Maximal distance in pixels where to search patches used for denoising.
        h : double, optional
            Cut-off distance (in gray levels).
        var : double
            Expected noise variance.  If non-zero, this is used to reduce the
            apparent patch distances by the expected distance due to the noise.
    
        Returns
        -------
        result : ndarray
            Denoised image, of same shape as input image.
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001B8A17752B0>'

__spec__ = None # (!) real value is "ModuleSpec(name='skimage.restoration._nl_means_denoising', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001B8A17752B0>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\skimage\\\\restoration\\\\_nl_means_denoising.cp37-win_amd64.pyd')"

__test__ = {}

