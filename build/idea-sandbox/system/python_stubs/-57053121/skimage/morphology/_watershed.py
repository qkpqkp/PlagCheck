# encoding: utf-8
# module skimage.morphology._watershed
# from C:\Users\Doly\Anaconda3\lib\site-packages\skimage\morphology\_watershed.cp37-win_amd64.pyd
# by generator 1.147
"""
watershed.pyx - scithon implementation of guts of watershed

Originally part of CellProfiler, code licensed under both GPL and BSD licenses.
Website: http://www.cellprofiler.org

Copyright (c) 2003-2009 Massachusetts Institute of Technology
Copyright (c) 2009-2011 Broad Institute
All rights reserved.

Original author: Lee Kamentsky
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py

# functions

def watershed_raveled(*args, **kwargs): # real signature unknown
    """
    Perform watershed algorithm using a raveled image and neighborhood.
    
        Parameters
        ----------
    
        image : array of float
            The flattened image pixels.
        marker_locations : array of int
            The raveled coordinates of the initial markers (aka seeds) for the
            watershed. NOTE: these should *all* point to nonzero entries in the
            output, or the algorithm will never terminate and blow up your memory!
        structure : array of int
            A list of coordinate offsets to compute the raveled coordinates of each
            neighbor from the raveled coordinates of the current pixel.
        mask : array of int
            An array of the same shape as `image` where each pixel contains a
            nonzero value if it is to be considered for flooding with watershed,
            zero otherwise. NOTE: it is *essential* that the border pixels (those
            with neighbors falling outside the volume) are all set to zero, or
            segfaults could occur.
        strides : array of int
            An array representing the number of steps to move along each dimension.
            This is used in computing the Euclidean distance between raveled
            indices.
        compactness : float
            A value greater than 0 implements the compact watershed algorithm
            (see .py file).
        output : array of int
            The output array, which must already contain nonzero entries at all the
            seed locations.
        wsl : bool
            Parameter indicating whether the watershed line is calculated.
            If wsl is set to True, the watershed line is calculated.
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001FB1CF989B0>'

__spec__ = None # (!) real value is "ModuleSpec(name='skimage.morphology._watershed', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001FB1CF989B0>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\skimage\\\\morphology\\\\_watershed.cp37-win_amd64.pyd')"

__test__ = {}

