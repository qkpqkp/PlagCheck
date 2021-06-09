# encoding: utf-8
# module skimage.feature.corner_cy
# from C:\Users\Doly\Anaconda3\lib\site-packages\skimage\feature\corner_cy.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py

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

def rgb2grey(rgb): # reliably restored by inspect
    """
    Compute luminance of an RGB image.
    
        Parameters
        ----------
        rgb : array_like
            The image in RGB format, in a 3-D or 4-D array of shape
            ``(.., ..,[ ..,] 3)``, or in RGBA format with shape
            ``(.., ..,[ ..,] 4)``.
    
        Returns
        -------
        out : ndarray
            The luminance image - an array which is the same size as the input
            array, but with the channel dimension removed.
    
        Raises
        ------
        ValueError
            If `rgb2gray` is not a 3-D or 4-D arrays of shape
            ``(.., ..,[ ..,] 3)`` or ``(.., ..,[ ..,] 4)``.
    
        References
        ----------
        .. [1] http://www.poynton.com/PDFs/ColorFAQ.pdf
    
        Notes
        -----
        The weights used in this conversion are calibrated for contemporary
        CRT phosphors::
    
            Y = 0.2125 R + 0.7154 G + 0.0721 B
    
        If there is an alpha channel present, it is ignored.
    
        Examples
        --------
        >>> from skimage.color import rgb2gray
        >>> from skimage import data
        >>> img = data.astronaut()
        >>> img_gray = rgb2gray(img)
    """
    pass

def _corner_fast(*args, **kwargs): # real signature unknown
    pass

def _corner_moravec(*args, **kwargs): # real signature unknown
    """
    Compute Moravec corner measure response image.
    
        This is one of the simplest corner detectors and is comparatively fast but
        has several limitations (e.g. not rotation invariant).
    
        Parameters
        ----------
        image : ndarray
            Input image.
        window_size : int, optional (default 1)
            Window size.
    
        Returns
        -------
        response : ndarray
            Moravec response image.
    
        References
        ----------
        .. [1] http://kiwi.cs.dal.ca/~dparks/CornerDetection/moravec.htm
        .. [2] https://en.wikipedia.org/wiki/Corner_detection
    
        Examples
        --------
        >>> from skimage.feature import corner_moravec
        >>> square = np.zeros([7, 7])
        >>> square[3, 3] = 1
        >>> square.astype(int)
        array([[0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0]])
        >>> corner_moravec(square).astype(int)
        array([[0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 1, 1, 1, 0, 0],
               [0, 0, 1, 2, 1, 0, 0],
               [0, 0, 1, 1, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0]])
    """
    pass

def _corner_orientations(*args, **kwargs): # real signature unknown
    """
    Compute the orientation of corners.
    
        The orientation of corners is computed using the first order central moment
        i.e. the center of mass approach. The corner orientation is the angle of
        the vector from the corner coordinate to the intensity centroid in the
        local neighborhood around the corner calculated using first order central
        moment.
    
        Parameters
        ----------
        image : 2D array
            Input grayscale image.
        corners : (N, 2) array
            Corner coordinates as ``(row, col)``.
        mask : 2D array
            Mask defining the local neighborhood of the corner used for the
            calculation of the central moment.
    
        Returns
        -------
        orientations : (N, 1) array
            Orientations of corners in the range [-pi, pi].
    
        References
        ----------
        .. [1] Ethan Rublee, Vincent Rabaud, Kurt Konolige and Gary Bradski
              "ORB : An efficient alternative to SIFT and SURF"
              http://www.vision.cs.chubu.ac.jp/CV-R/pdf/Rublee_iccv2011.pdf
        .. [2] Paul L. Rosin, "Measuring Corner Properties"
              http://users.cs.cf.ac.uk/Paul.Rosin/corner2.pdf
    
        Examples
        --------
        >>> from skimage.morphology import octagon
        >>> from skimage.feature import (corner_fast, corner_peaks,
        ...                              corner_orientations)
        >>> square = np.zeros((12, 12))
        >>> square[3:9, 3:9] = 1
        >>> square.astype(int)
        array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
        >>> corners = corner_peaks(corner_fast(square, 9), min_distance=1)
        >>> corners
        array([[3, 3],
               [3, 8],
               [8, 3],
               [8, 8]])
        >>> orientations = corner_orientations(square, corners, octagon(3, 2))
        >>> np.rad2deg(orientations)
        array([  45.,  135.,  -45., -135.])
    """
    pass

def _prepare_grayscale_input_2D(image): # reliably restored by inspect
    # no doc
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000002FD203AD630>'

__spec__ = None # (!) real value is "ModuleSpec(name='skimage.feature.corner_cy', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000002FD203AD630>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\skimage\\\\feature\\\\corner_cy.cp37-win_amd64.pyd')"

__test__ = {
    '_corner_moravec (line 16)': 'Compute Moravec corner measure response image.\n\n    This is one of the simplest corner detectors and is comparatively fast but\n    has several limitations (e.g. not rotation invariant).\n\n    Parameters\n    ----------\n    image : ndarray\n        Input image.\n    window_size : int, optional (default 1)\n        Window size.\n\n    Returns\n    -------\n    response : ndarray\n        Moravec response image.\n\n    References\n    ----------\n    .. [1] http://kiwi.cs.dal.ca/~dparks/CornerDetection/moravec.htm\n    .. [2] https://en.wikipedia.org/wiki/Corner_detection\n\n    Examples\n    --------\n    >>> from skimage.feature import corner_moravec\n    >>> square = np.zeros([7, 7])\n    >>> square[3, 3] = 1\n    >>> square.astype(int)\n    array([[0, 0, 0, 0, 0, 0, 0],\n           [0, 0, 0, 0, 0, 0, 0],\n           [0, 0, 0, 0, 0, 0, 0],\n           [0, 0, 0, 1, 0, 0, 0],\n           [0, 0, 0, 0, 0, 0, 0],\n           [0, 0, 0, 0, 0, 0, 0],\n           [0, 0, 0, 0, 0, 0, 0]])\n    >>> corner_moravec(square).astype(int)\n    array([[0, 0, 0, 0, 0, 0, 0],\n           [0, 0, 0, 0, 0, 0, 0],\n           [0, 0, 1, 1, 1, 0, 0],\n           [0, 0, 1, 2, 1, 0, 0],\n           [0, 0, 1, 1, 1, 0, 0],\n           [0, 0, 0, 0, 0, 0, 0],\n           [0, 0, 0, 0, 0, 0, 0]])\n    ',
    '_corner_orientations (line 178)': 'Compute the orientation of corners.\n\n    The orientation of corners is computed using the first order central moment\n    i.e. the center of mass approach. The corner orientation is the angle of\n    the vector from the corner coordinate to the intensity centroid in the\n    local neighborhood around the corner calculated using first order central\n    moment.\n\n    Parameters\n    ----------\n    image : 2D array\n        Input grayscale image.\n    corners : (N, 2) array\n        Corner coordinates as ``(row, col)``.\n    mask : 2D array\n        Mask defining the local neighborhood of the corner used for the\n        calculation of the central moment.\n\n    Returns\n    -------\n    orientations : (N, 1) array\n        Orientations of corners in the range [-pi, pi].\n\n    References\n    ----------\n    .. [1] Ethan Rublee, Vincent Rabaud, Kurt Konolige and Gary Bradski\n          "ORB : An efficient alternative to SIFT and SURF"\n          http://www.vision.cs.chubu.ac.jp/CV-R/pdf/Rublee_iccv2011.pdf\n    .. [2] Paul L. Rosin, "Measuring Corner Properties"\n          http://users.cs.cf.ac.uk/Paul.Rosin/corner2.pdf\n\n    Examples\n    --------\n    >>> from skimage.morphology import octagon\n    >>> from skimage.feature import (corner_fast, corner_peaks,\n    ...                              corner_orientations)\n    >>> square = np.zeros((12, 12))\n    >>> square[3:9, 3:9] = 1\n    >>> square.astype(int)\n    array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n           [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],\n           [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],\n           [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],\n           [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],\n           [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],\n           [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],\n           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])\n    >>> corners = corner_peaks(corner_fast(square, 9), min_distance=1)\n    >>> corners\n    array([[3, 3],\n           [3, 8],\n           [8, 3],\n           [8, 8]])\n    >>> orientations = corner_orientations(square, corners, octagon(3, 2))\n    >>> np.rad2deg(orientations)\n    array([  45.,  135.,  -45., -135.])\n\n    ',
}

