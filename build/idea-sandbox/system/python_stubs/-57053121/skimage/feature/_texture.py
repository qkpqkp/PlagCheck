# encoding: utf-8
# module skimage.feature._texture
# from C:\Users\Doly\Anaconda3\lib\site-packages\skimage\feature\_texture.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py

# functions

def _glcm_loop(*args, **kwargs): # real signature unknown
    """
    Perform co-occurrence matrix accumulation.
    
        Parameters
        ----------
        image : ndarray
            Integer typed input image. Only positive valued images are supported.
            If type is other than uint8, the argument `levels` needs to be set.
        distances : ndarray
            List of pixel pair distance offsets.
        angles : ndarray
            List of pixel pair angles in radians.
        levels : int
            The input image should contain integers in [0, `levels`-1],
            where levels indicate the number of gray-levels counted
            (typically 256 for an 8-bit image).
        out : ndarray
            On input a 4D array of zeros, and on output it contains
            the results of the GLCM computation.
    """
    pass

def _local_binary_pattern(*args, **kwargs): # real signature unknown
    """
    Gray scale and rotation invariant LBP (Local Binary Patterns).
    
        LBP is an invariant descriptor that can be used for texture classification.
    
        Parameters
        ----------
        image : (N, M) double array
            Graylevel image.
        P : int
            Number of circularly symmetric neighbour set points (quantization of
            the angular space).
        R : float
            Radius of circle (spatial resolution of the operator).
        method : {'D', 'R', 'U', 'N', 'V'}
            Method to determine the pattern.
    
            * 'D': 'default'
            * 'R': 'ror'
            * 'U': 'uniform'
            * 'N': 'nri_uniform'
            * 'V': 'var'
    
        Returns
        -------
        output : (N, M) array
            LBP image.
    """
    pass

def _multiblock_lbp(*args, **kwargs): # real signature unknown
    """
    Multi-block local binary pattern (MB-LBP) [1]_.
    
        Parameters
        ----------
        int_image : (N, M) float array
            Integral image.
        r : int
            Row-coordinate of top left corner of a rectangle containing feature.
        c : int
            Column-coordinate of top left corner of a rectangle containing feature.
        width : int
            Width of one of 9 equal rectangles that will be used to compute
            a feature.
        height : int
            Height of one of 9 equal rectangles that will be used to compute
            a feature.
    
        Returns
        -------
        output : int
            8-bit MB-LBP feature descriptor.
    
        References
        ----------
        .. [1] Face Detection Based on Multi-Block LBP
               Representation. Lun Zhang, Rufeng Chu, Shiming Xiang, Shengcai Liao,
               Stan Z. Li
               http://www.cbsr.ia.ac.cn/users/scliao/papers/Zhang-ICB07-MBLBP.pdf
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001F7A529A400>'

__pyx_capi__ = {
    '_multiblock_lbp': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice, Py_ssize_t, Py_ssize_t, Py_ssize_t, Py_ssize_t, int __pyx_skip_dispatch)" at 0x000001F7A5290720>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='skimage.feature._texture', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001F7A529A400>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\skimage\\\\feature\\\\_texture.cp37-win_amd64.pyd')"

__test__ = {}

