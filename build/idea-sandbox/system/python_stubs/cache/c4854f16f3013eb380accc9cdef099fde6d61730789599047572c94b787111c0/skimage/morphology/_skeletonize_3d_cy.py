# encoding: utf-8
# module skimage.morphology._skeletonize_3d_cy
# from C:\Users\Doly\Anaconda3\lib\site-packages\skimage\morphology\_skeletonize_3d_cy.cp37-win_amd64.pyd
# by generator 1.147
"""
This is an implementation of the 2D/3D thinning algorithm
of [Lee94]_ of binary images, based on [IAC15]_.

The original Java code [IAC15]_ carries the following message:

 * This work is an implementation by Ignacio Arganda-Carreras of the
 * 3D thinning algorithm from Lee et al. "Building skeleton models via 3-D
 * medial surface/axis thinning algorithms. Computer Vision, Graphics, and
 * Image Processing, 56(6):462-478, 1994." Based on the ITK version from
 * Hanno Homann <a href="http://hdl.handle.net/1926/1292"> http://hdl.handle.net/1926/1292</a>
 * <p>
 *  More information at Skeletonize3D homepage:
 *  https://imagej.net/Skeletonize3D
 *
 * @version 1.0 11/13/2015 (unique BSD licensed version for scikit-image)
 * @author Ignacio Arganda-Carreras (iargandacarreras at gmail.com)

References
----------
.. [Lee94] T.-C. Lee, R.L. Kashyap and C.-N. Chu, Building skeleton models
       via 3-D medial surface/axis thinning algorithms.
       Computer Vision, Graphics, and Image Processing, 56(6):462-478, 1994.

.. [IAC15] Ignacio Arganda-Carreras, 2015. Skeletonize3D plugin for ImageJ(C).
           https://imagej.net/Skeletonize3D
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py

# functions

def fill_Euler_LUT(*args, **kwargs): # real signature unknown
    """
    Look-up table for preserving Euler characteristic.
    
        This is column $\delta G_{26}$ of Table 2 of [Lee94]_.
    """
    pass

def _compute_thin_image(*args, **kwargs): # real signature unknown
    """
    Compute a thin image.
    
        Loop through the image multiple times, removing "simple" points, i.e.
        those point which can be removed without changing local connectivity in the
        3x3x3 neighborhood of a point.
    
        This routine implements the two-pass algorithm of [Lee94]_. Namely,
        for each of the six border types (positive and negative x-, y- and z-),
        the algorithm first collects all possibly deletable points, and then
        performs a sequential rechecking.
    
        The input, `img`, is assumed to be a 3D binary image in the
        (p, r, c) format [i.e., C ordered array], filled by zeros (background) and
        ones. Furthermore, `img` is assumed to be padded by zeros from all
        directions --- this way the zero boundary conditions are automatic
        and there is need to guard against out-of-bounds access.
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000002ABA040E7F0>'

__spec__ = None # (!) real value is "ModuleSpec(name='skimage.morphology._skeletonize_3d_cy', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000002ABA040E7F0>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\skimage\\\\morphology\\\\_skeletonize_3d_cy.cp37-win_amd64.pyd')"

__test__ = {}

