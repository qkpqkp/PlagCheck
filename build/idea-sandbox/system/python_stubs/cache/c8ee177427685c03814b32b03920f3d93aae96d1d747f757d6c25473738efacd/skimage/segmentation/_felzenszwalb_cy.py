# encoding: utf-8
# module skimage.segmentation._felzenszwalb_cy
# from C:\Users\Doly\Anaconda3\lib\site-packages\skimage\segmentation\_felzenszwalb_cy.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py
import scipy.ndimage as ndi # C:\Users\Doly\Anaconda3\lib\site-packages\scipy\ndimage\__init__.py

# functions

def img_as_float64(image, force_copy=False): # reliably restored by inspect
    """
    Convert an image to double-precision (64-bit) floating point format.
    
        Parameters
        ----------
        image : ndarray
            Input image.
        force_copy : bool, optional
            Force a copy of the data, irrespective of its current dtype.
    
        Returns
        -------
        out : ndarray of float64
            Output image.
    
        Notes
        -----
        The range of a floating point image is [0.0, 1.0] or [-1.0, 1.0] when
        converting from unsigned or signed datatypes, respectively.
        If the input image has a float type, intensity values are not modified
        and can be outside the ranges [0.0, 1.0] or [-1.0, 1.0].
    """
    pass

def warn(message, category=None, stacklevel=2): # reliably restored by inspect
    """ A version of `warnings.warn` with a default stacklevel of 2. """
    pass

def _felzenszwalb_cython(*args, **kwargs): # real signature unknown
    """
    Felzenszwalb's efficient graph based segmentation for
        single or multiple channels.
    
        Produces an oversegmentation of a single or multi-channel image
        using a fast, minimum spanning tree based clustering on the image grid.
        The number of produced segments as well as their size can only be
        controlled indirectly through ``scale``. Segment size within an image can
        vary greatly depending on local contrast.
    
        Parameters
        ----------
        image : (N, M, C) ndarray
            Input image.
        scale : float, optional (default 1)
            Sets the obervation level. Higher means larger clusters.
        sigma : float, optional (default 0.8)
            Width of Gaussian smoothing kernel used in preprocessing.
            Larger sigma gives smother segment boundaries.
        min_size : int, optional (default 20)
            Minimum component size. Enforced using postprocessing.
    
        Returns
        -------
        segment_mask : (N, M) ndarray
            Integer mask indicating segment labels.
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001EA5D8B9588>'

__spec__ = None # (!) real value is "ModuleSpec(name='skimage.segmentation._felzenszwalb_cy', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001EA5D8B9588>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\skimage\\\\segmentation\\\\_felzenszwalb_cy.cp37-win_amd64.pyd')"

__test__ = {}

