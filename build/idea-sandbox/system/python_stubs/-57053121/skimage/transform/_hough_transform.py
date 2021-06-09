# encoding: utf-8
# module skimage.transform._hough_transform
# from C:\Users\Doly\Anaconda3\lib\site-packages\skimage\transform\_hough_transform.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py

# functions

def circle_perimeter(r, c, radius, method=None, shape=None): # reliably restored by inspect
    """
    Generate circle perimeter coordinates.
    
        Parameters
        ----------
        r, c : int
            Centre coordinate of circle.
        radius: int
            Radius of circle.
        method : {'bresenham', 'andres'}, optional
            bresenham : Bresenham method (default)
            andres : Andres method
        shape : tuple, optional
            Image shape which is used to determine the maximum extent of output
            pixel coordinates. This is useful for circles that exceed the image
            size. If None, the full extent of the circle is used.
    
        Returns
        -------
        rr, cc : (N,) ndarray of int
            Bresenham and Andres' method:
            Indices of pixels that belong to the circle perimeter.
            May be used to directly index into an array, e.g.
            ``img[rr, cc] = 1``.
    
        Notes
        -----
        Andres method presents the advantage that concentric
        circles create a disc whereas Bresenham can make holes. There
        is also less distortions when Andres circles are rotated.
        Bresenham method is also known as midpoint circle algorithm.
        Anti-aliased circle generator is available with `circle_perimeter_aa`.
    
        References
        ----------
        .. [1] J.E. Bresenham, "Algorithm for computer control of a digital
               plotter", IBM Systems journal, 4 (1965) 25-30.
        .. [2] E. Andres, "Discrete circles, rings and spheres", Computers &
               Graphics, 18 (1994) 695-706.
    
        Examples
        --------
        >>> from skimage.draw import circle_perimeter
        >>> img = np.zeros((10, 10), dtype=np.uint8)
        >>> rr, cc = circle_perimeter(4, 4, 3)
        >>> img[rr, cc] = 1
        >>> img
        array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
               [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
               [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=uint8)
    """
    pass

def _hough_circle(*args, **kwargs): # real signature unknown
    """
    Perform a circular Hough transform.
    
        Parameters
        ----------
        img : (M, N) ndarray
            Input image with nonzero values representing edges.
        radius : ndarray
            Radii at which to compute the Hough transform.
        normalize : boolean, optional (default True)
            Normalize the accumulator with the number
            of pixels used to draw the radius.
        full_output : boolean, optional (default False)
            Extend the output size by twice the largest
            radius in order to detect centers outside the
            input picture.
    
        Returns
        -------
        H : 3D ndarray (radius index, (M + 2R, N + 2R) ndarray)
            Hough transform accumulator for each radius.
            R designates the larger radius if full_output is True.
            Otherwise, R = 0.
    """
    pass

def _hough_ellipse(*args, **kwargs): # real signature unknown
    """
    Perform an elliptical Hough transform.
    
        Parameters
        ----------
        img : (M, N) ndarray
            Input image with nonzero values representing edges.
        threshold: int, optional (default 4)
            Accumulator threshold value.
        accuracy : double, optional (default 1)
            Bin size on the minor axis used in the accumulator.
        min_size : int, optional (default 4)
            Minimal major axis length.
        max_size : int, optional
            Maximal minor axis length. (default None)
            If None, the value is set to the half of the smaller
            image dimension.
    
        Returns
        -------
        result : ndarray with fields [(accumulator, yc, xc, a, b, orientation)]
              Where ``(yc, xc)`` is the center, ``(a, b)`` the major and minor
              axes, respectively. The `orientation` value follows
              `skimage.draw.ellipse_perimeter` convention.
    
        Examples
        --------
        >>> img = np.zeros((25, 25), dtype=np.uint8)
        >>> rr, cc = ellipse_perimeter(10, 10, 6, 8)
        >>> img[cc, rr] = 1
        >>> result = hough_ellipse(img, threshold=8)
        [(10, 10.0, 8.0, 6.0, 0.0, 10.0)]
    
        Notes
        -----
        The accuracy must be chosen to produce a peak in the accumulator
        distribution. In other words, a flat accumulator distribution with low
        values may be caused by a too low bin size.
    
        References
        ----------
        .. [1] Xie, Yonghong, and Qiang Ji. "A new efficient ellipse detection
               method." Pattern Recognition, 2002. Proceedings. 16th International
               Conference on. Vol. 2. IEEE, 2002
    """
    pass

def _hough_line(*args, **kwargs): # real signature unknown
    """
    Perform a straight line Hough transform.
    
        Parameters
        ----------
        img : (M, N) ndarray
            Input image with nonzero values representing edges.
        theta : 1D ndarray of double
            Angles at which to compute the transform, in radians.
    
        Returns
        -------
        H : 2-D ndarray of uint64
            Hough transform accumulator.
        theta : ndarray
            Angles at which the transform was computed, in radians.
        distances : ndarray
            Distance values.
    
        Notes
        -----
        The origin is the top left corner of the original image.
        X and Y axis are horizontal and vertical edges respectively.
        The distance is the minimal algebraic distance from the origin
        to the detected line.
    
        Examples
        --------
        Generate a test image:
    
        >>> img = np.zeros((100, 150), dtype=bool)
        >>> img[30, :] = 1
        >>> img[:, 65] = 1
        >>> img[35:45, 35:50] = 1
        >>> for i in range(90):
        ...     img[i, i] = 1
        >>> img += np.random.random(img.shape) > 0.95
    
        Apply the Hough transform:
    
        >>> out, angles, d = hough_line(img)
    
        .. plot:: hough_tf.py
    """
    pass

def _probabilistic_hough_line(*args, **kwargs): # real signature unknown
    """
    Return lines from a progressive probabilistic line Hough transform.
    
        Parameters
        ----------
        img : (M, N) ndarray
            Input image with nonzero values representing edges.
        threshold : int
            Threshold
        line_length : int
            Minimum accepted length of detected lines.
            Increase the parameter to extract longer lines.
        line_gap : int
            Maximum gap between pixels to still form a line.
            Increase the parameter to merge broken lines more aggressively.
        theta : 1D ndarray, dtype=double
            Angles at which to compute the transform, in radians.
        seed : int, optional
            Seed to initialize the random number generator.
    
        Returns
        -------
        lines : list
          List of lines identified, lines in format ((x0, y0), (x1, y0)),
          indicating line start and end.
    
        References
        ----------
        .. [1] C. Galamhos, J. Matas and J. Kittler, "Progressive probabilistic
               Hough transform for line detection", in IEEE Computer Society
               Conference on Computer Vision and Pattern Recognition, 1999.
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000014B8F730390>'

__spec__ = None # (!) real value is "ModuleSpec(name='skimage.transform._hough_transform', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000014B8F730390>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\skimage\\\\transform\\\\_hough_transform.cp37-win_amd64.pyd')"

__test__ = {
    '_hough_ellipse (line 101)': 'Perform an elliptical Hough transform.\n\n    Parameters\n    ----------\n    img : (M, N) ndarray\n        Input image with nonzero values representing edges.\n    threshold: int, optional (default 4)\n        Accumulator threshold value.\n    accuracy : double, optional (default 1)\n        Bin size on the minor axis used in the accumulator.\n    min_size : int, optional (default 4)\n        Minimal major axis length.\n    max_size : int, optional\n        Maximal minor axis length. (default None)\n        If None, the value is set to the half of the smaller\n        image dimension.\n\n    Returns\n    -------\n    result : ndarray with fields [(accumulator, yc, xc, a, b, orientation)]\n          Where ``(yc, xc)`` is the center, ``(a, b)`` the major and minor\n          axes, respectively. The `orientation` value follows\n          `skimage.draw.ellipse_perimeter` convention.\n\n    Examples\n    --------\n    >>> img = np.zeros((25, 25), dtype=np.uint8)\n    >>> rr, cc = ellipse_perimeter(10, 10, 6, 8)\n    >>> img[cc, rr] = 1\n    >>> result = hough_ellipse(img, threshold=8)\n    [(10, 10.0, 8.0, 6.0, 0.0, 10.0)]\n\n    Notes\n    -----\n    The accuracy must be chosen to produce a peak in the accumulator\n    distribution. In other words, a flat accumulator distribution with low\n    values may be caused by a too low bin size.\n\n    References\n    ----------\n    .. [1] Xie, Yonghong, and Qiang Ji. "A new efficient ellipse detection\n           method." Pattern Recognition, 2002. Proceedings. 16th International\n           Conference on. Vol. 2. IEEE, 2002\n    ',
    '_hough_line (line 244)': 'Perform a straight line Hough transform.\n\n    Parameters\n    ----------\n    img : (M, N) ndarray\n        Input image with nonzero values representing edges.\n    theta : 1D ndarray of double\n        Angles at which to compute the transform, in radians.\n\n    Returns\n    -------\n    H : 2-D ndarray of uint64\n        Hough transform accumulator.\n    theta : ndarray\n        Angles at which the transform was computed, in radians.\n    distances : ndarray\n        Distance values.\n\n    Notes\n    -----\n    The origin is the top left corner of the original image.\n    X and Y axis are horizontal and vertical edges respectively.\n    The distance is the minimal algebraic distance from the origin\n    to the detected line.\n\n    Examples\n    --------\n    Generate a test image:\n\n    >>> img = np.zeros((100, 150), dtype=bool)\n    >>> img[30, :] = 1\n    >>> img[:, 65] = 1\n    >>> img[35:45, 35:50] = 1\n    >>> for i in range(90):\n    ...     img[i, i] = 1\n    >>> img += np.random.random(img.shape) > 0.95\n\n    Apply the Hough transform:\n\n    >>> out, angles, d = hough_line(img)\n\n    .. plot:: hough_tf.py\n\n    ',
}

