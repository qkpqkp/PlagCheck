# encoding: utf-8
# module skimage.morphology._greyreconstruct
# from C:\Users\Doly\Anaconda3\lib\site-packages\skimage\morphology\_greyreconstruct.cp37-win_amd64.pyd
# by generator 1.147
"""
`reconstruction_loop` originally part of CellProfiler, code licensed under both GPL and BSD licenses.

Website: http://www.cellprofiler.org
Copyright (c) 2003-2009 Massachusetts Institute of Technology
Copyright (c) 2009-2011 Broad Institute
All rights reserved.
Original author: Lee Kamentsky
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

# functions

def reconstruction_loop(*args, **kwargs): # real signature unknown
    """
    The inner loop for reconstruction.
    
        This algorithm uses the rank-order of pixels. If low intensity pixels have
        a low rank and high intensity pixels have a high rank, then this loop
        performs reconstruction by dilation. If this ranking is reversed, the
        result is reconstruction by erosion.
    
        For each pixel in the seed image, check its neighbors. If its neighbor's
        rank is below that of the current pixel, replace the neighbor's rank with
        the rank of the current pixel. This dilation is limited by the mask, i.e.
        the rank at each pixel cannot exceed the mask as that pixel.
    
        Parameters
        ----------
        aranks : array
            The rank order of the flattened seed and mask images.
        aprev, anext: arrays
            Indices of previous and next pixels in rank sorted order.
        astrides : array
            Strides to neighbors of the current pixel.
        current_idx : int
            Index of highest-ranked pixel used as starting point in loop.
        image_stride : int
            Stride between seed image and mask image in `aranks`.
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001A2C689B908>'

__spec__ = None # (!) real value is "ModuleSpec(name='skimage.morphology._greyreconstruct', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001A2C689B908>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\skimage\\\\morphology\\\\_greyreconstruct.cp37-win_amd64.pyd')"

__test__ = {}

