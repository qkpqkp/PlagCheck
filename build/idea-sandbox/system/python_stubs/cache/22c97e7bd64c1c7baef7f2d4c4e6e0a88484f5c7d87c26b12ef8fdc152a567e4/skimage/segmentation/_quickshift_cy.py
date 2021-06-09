# encoding: utf-8
# module skimage.segmentation._quickshift_cy
# from C:\Users\Doly\Anaconda3\lib\site-packages\skimage\segmentation\_quickshift_cy.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py

# functions

def _quickshift_cython(*args, **kwargs): # real signature unknown
    """
    Segments image using quickshift clustering in Color-(x,y) space.
    
        Produces an oversegmentation of the image using the quickshift mode-seeking
        algorithm.
    
        Parameters
        ----------
        image : (width, height, channels) ndarray
            Input image.
        kernel_size : float
            Width of Gaussian kernel used in smoothing the
            sample density. Higher means fewer clusters.
        max_dist : float
            Cut-off point for data distances.
            Higher means fewer clusters.
        return_tree : bool
            Whether to return the full segmentation hierarchy tree and distances.
        random_seed : int
            Random seed used for breaking ties.
    
        Returns
        -------
        segment_mask : (width, height) ndarray
            Integer mask indicating segment labels.
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001E64951F4A8>'

__spec__ = None # (!) real value is "ModuleSpec(name='skimage.segmentation._quickshift_cy', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001E64951F4A8>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\skimage\\\\segmentation\\\\_quickshift_cy.cp37-win_amd64.pyd')"

__test__ = {}

