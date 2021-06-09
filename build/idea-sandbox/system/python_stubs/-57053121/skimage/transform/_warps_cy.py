# encoding: utf-8
# module skimage.transform._warps_cy
# from C:\Users\Doly\Anaconda3\lib\site-packages\skimage\transform\_warps_cy.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py

# functions

def _warp_fast(*args, **kwargs): # real signature unknown
    """
    Projective transformation (homography).
    
        Perform a projective transformation (homography) of a
        floating point image, using interpolation.
    
        For each pixel, given its homogeneous coordinate :math:`\mathbf{x}
        = [x, y, 1]^T`, its target position is calculated by multiplying
        with the given matrix, :math:`H`, to give :math:`H \mathbf{x}`.
        E.g., to rotate by theta degrees clockwise, the matrix should be::
    
          [[cos(theta) -sin(theta) 0]
           [sin(theta)  cos(theta) 0]
           [0            0         1]]
    
        or, to translate x by 10 and y by 20::
    
          [[1 0 10]
           [0 1 20]
           [0 0 1 ]].
    
        Parameters
        ----------
        image : 2-D array
            Input image.
        H : array of shape ``(3, 3)``
            Transformation matrix H that defines the homography.
        output_shape : tuple (rows, cols), optional
            Shape of the output image generated (default None).
        order : {0, 1, 2, 3}, optional
            Order of interpolation::
            * 0: Nearest-neighbor
            * 1: Bi-linear (default)
            * 2: Bi-quadratic
            * 3: Bi-cubic
        mode : {'constant', 'edge', 'symmetric', 'reflect', 'wrap'}, optional
            Points outside the boundaries of the input are filled according
            to the given mode.  Modes match the behaviour of `numpy.pad`.
        cval : string, optional (default 0)
            Used in conjunction with mode 'C' (constant), the value
            outside the image boundaries.
    
        Notes
        -----
        Modes 'reflect' and 'symmetric' are similar, but differ in whether the edge
        pixels are duplicated during the reflection.  As an example, if an array
        has values [0, 1, 2] and was padded to the right by four values using
        symmetric, the result would be [0, 1, 2, 2, 1, 0, 0], while for reflect it
        would be [0, 1, 2, 1, 0, 1, 2].
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000251EBA770B8>'

__spec__ = None # (!) real value is "ModuleSpec(name='skimage.transform._warps_cy', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000251EBA770B8>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\skimage\\\\transform\\\\_warps_cy.cp37-win_amd64.pyd')"

__test__ = {}

