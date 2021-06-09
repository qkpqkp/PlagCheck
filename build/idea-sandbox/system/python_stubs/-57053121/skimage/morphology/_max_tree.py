# encoding: utf-8
# module skimage.morphology._max_tree
# from C:\Users\Doly\Anaconda3\lib\site-packages\skimage\morphology\_max_tree.cp37-win_amd64.pyd
# by generator 1.147
"""
_max_tree.pyx - building a max-tree from an image.

This is an implementation of the max-tree, which is a morphological
representation of the image. Many morphological operators can be built
from this representation, namely attribute openings and closings.

This file also contains implementations of max-tree based filters and
functions to characterize the tree components.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py

# functions

def _compute_area(*args, **kwargs): # real signature unknown
    """
    Compute the area of all max-tree components.
    
        This attribute is used for area opening and closing
    """
    pass

def _compute_extension(*args, **kwargs): # real signature unknown
    """
    Compute the bounding box extension of all max-tree components.
    
        This attribute is used for diameter opening and closing.
    """
    pass

def _direct_filter(*args, **kwargs): # real signature unknown
    """
    Apply a direct filtering.
    
        This produces an image in which for all possible thresholds, each connected
        component has the specified attribute value greater than that threshold.
        This is the basic function called by :func:`area_opening`,
        :func:`diameter_opening`, and similar.
    
        For :func:`area_opening`, for instance, the attribute is the area.  In this
        case, an image is produced for which all connected components for all
        thresholds have at least an area (pixel count) of the threshold given by
        the user.
    
        Parameters
        ----------
    
        image : array
            The flattened image pixels.
        output : array, same size and type as `image`
            The array into which to write the output values. **This array will be
            modified in-place.**
        parent : array of int, same shape as `image`
            Image of indices. The value at each pixel is the index of this pixel's
            parent in the max-tree reprentation.
        sorted_indices : array of int, same shape as `image`
            "List" of pixel indices, which contains an ordering of elements in the
            tree such that a parent of a pixel always comes before the element
            itself. More formally: i < j implies that j cannot be the parent of i.
        attribute : array of float
            Contains the attributes computed for the max-tree.
        attribute_threshold : float
            The threshold to be applied to the attribute.
    """
    pass

def _max_tree(*args, **kwargs): # real signature unknown
    """
    Build a max-tree.
    
        Parameters
        ----------
        image : array
            The flattened image pixels.
        mask : array of int
            An array of the same shape as `image` where each pixel contains a
            nonzero value if it is to be considered for the filtering.  NOTE: it is
            *essential* that the border pixels (those with neighbors falling
            outside the volume) are all set to zero, or segfaults could occur.
        structure : array of int
            A list of coordinate offsets to compute the raveled coordinates of each
            neighbor from the raveled coordinates of the current pixel.
        parent : array of int
            Output image of the same shape as the input image. The value at each
            pixel is the parent index of this pixel in the max-tree reprentation.
            **This array will be written to in-place.**
        sorted_indices : array of int
            Output "list" of pixel indices, which contains an ordering of elements
            in the tree such that a parent of a pixel always comes before the
            element itself. More formally: i < j implies that j cannot be the
            the parent of i. **This array will be written to in-place.**
    """
    pass

def _max_tree_local_maxima(*args, **kwargs): # real signature unknown
    """
    Find the local maxima in image from the max-tree representation.
    
        Parameters
        ----------
    
        image : array of arbitrary type
            The flattened image pixels.
        output : array of the same shape and type as image.
            The output image must contain only ones.
        parent : array of int
            Image of the same shape as the input image. The value
            at each pixel is the parent index of this pixel in the max-tree
            reprentation.
        sorted_indices : array of int
            List of length = number of pixels. Each element
            corresponds to one pixel index in the image. It encodes the order
            of elements in the tree: a parent of a pixel always comes before
            the element itself. More formally: i < j implies that j cannot be
            the parent of i.
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000002391FBBE748>'

__spec__ = None # (!) real value is "ModuleSpec(name='skimage.morphology._max_tree', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000002391FBBE748>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\skimage\\\\morphology\\\\_max_tree.cp37-win_amd64.pyd')"

__test__ = {}

