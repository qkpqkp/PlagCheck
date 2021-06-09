# encoding: utf-8
# module skimage.draw._draw
# from C:\Users\Doly\Anaconda3\lib\site-packages\skimage\draw\_draw.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import math as math # <module 'math' (built-in)>
import numpy as np # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py

# functions

def _bezier_curve(*args, **kwargs): # real signature unknown
    """
    Generate Bezier curve coordinates.
    
        Parameters
        ----------
        r0, c0 : int
            Coordinates of the first control point.
        r1, c1 : int
            Coordinates of the middle control point.
        r2, c2 : int
            Coordinates of the last control point.
        weight : double
            Middle control point weight, it describes the line tension.
        shape : tuple
            Image shape which is used to determine the maximum extent of output
            pixel coordinates. This is useful for curves that exceed the image
            size. If None, the full extent of the curve is used.
    
        Returns
        -------
        rr, cc : (N,) ndarray of int
            Indices of pixels that belong to the Bezier curve.
            May be used to directly index into an array, e.g.
            ``img[rr, cc] = 1``.
    
        Notes
        -----
        The algorithm is the rational quadratic algorithm presented in
        reference [1]_.
    
        References
        ----------
        .. [1] A Rasterizing Algorithm for Drawing Curves, A. Zingl, 2012
               http://members.chello.at/easyfilter/Bresenham.pdf
    """
    pass

def _bezier_segment(*args, **kwargs): # real signature unknown
    """
    Generate Bezier segment coordinates.
    
        Parameters
        ----------
        r0, c0 : int
            Coordinates of the first control point.
        r1, c1 : int
            Coordinates of the middle control point.
        r2, c2 : int
            Coordinates of the last control point.
        weight : double
            Middle control point weight, it describes the line tension.
    
        Returns
        -------
        rr, cc : (N,) ndarray of int
            Indices of pixels that belong to the Bezier curve.
            May be used to directly index into an array, e.g.
            ``img[rr, cc] = 1``.
    
        Notes
        -----
        The algorithm is the rational quadratic algorithm presented in
        reference [1]_.
    
        References
        ----------
        .. [1] A Rasterizing Algorithm for Drawing Curves, A. Zingl, 2012
               http://members.chello.at/easyfilter/Bresenham.pdf
    """
    pass

def _circle_perimeter(*args, **kwargs): # real signature unknown
    """
    Generate circle perimeter coordinates.
    
        Parameters
        ----------
        r_o, c_o : int
            Centre coordinate of circle.
        radius : int
            Radius of circle.
        method : {'bresenham', 'andres'}
            bresenham : Bresenham method (default)
            andres : Andres method
        shape : tuple
            Image shape which is used to determine the maximum extent of output pixel
            coordinates. This is useful for circles that exceed the image size.
            If None, the full extent of the circle is used.
    
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
    """
    pass

def _circle_perimeter_aa(*args, **kwargs): # real signature unknown
    """
    Generate anti-aliased circle perimeter coordinates.
    
        Parameters
        ----------
        r_o, c_o : int
            Centre coordinate of circle.
        radius : int
            Radius of circle.
        shape : tuple
            Image shape which is used to determine the maximum extent of output
            pixel coordinates. This is useful for circles that exceed the image
            size. If None, the full extent of the circle is used.
    
        Returns
        -------
        rr, cc, val : (N,) ndarray (int, int, float)
            Indices of pixels (`rr`, `cc`) and intensity values (`val`).
            ``img[rr, cc] = val``.
    
        Notes
        -----
        Wu's method draws anti-aliased circle. This implementation doesn't use
        lookup table optimization.
    
        References
        ----------
        .. [1] X. Wu, "An efficient antialiasing technique", In ACM SIGGRAPH
               Computer Graphics, 25 (1991) 143-152.
    """
    pass

def _coords_inside_image(*args, **kwargs): # real signature unknown
    """
    Return the coordinates inside an image of a given shape.
    
        Parameters
        ----------
        rr, cc : (N,) ndarray of int
            Indices of pixels.
        shape : tuple
            Image shape which is used to determine the maximum extent of output
            pixel coordinates.
        val : (N, D) ndarray of float, optional
            Values of pixels at coordinates ``[rr, cc]``.
    
        Returns
        -------
        rr, cc : (M,) array of int
            Row and column indices of valid pixels (i.e. those inside `shape`).
        val : (M, D) array of float, optional
            Values at `rr, cc`. Returned only if `val` is given as input.
    """
    pass

def _ellipse_perimeter(*args, **kwargs): # real signature unknown
    """
    Generate ellipse perimeter coordinates.
    
        Parameters
        ----------
        r_o, c_o : int
            Centre coordinate of ellipse.
        r_radius, c_radius : int
            Minor and major semi-axes. ``(r/r_radius)**2 + (c/c_radius)**2 = 1``.
        orientation : double
            Major axis orientation in clockwise direction as radians.
        shape : tuple
            Image shape which is used to determine the maximum extent of output pixel
            coordinates. This is useful for ellipses that exceed the image size.
            If None, the full extent of the ellipse is used.
    
        Returns
        -------
        rr, cc : (N,) ndarray of int
            Indices of pixels that belong to the ellipse perimeter.
            May be used to directly index into an array, e.g.
            ``img[rr, cc] = 1``.
    
        References
        ----------
        .. [1] A Rasterizing Algorithm for Drawing Curves, A. Zingl, 2012
               http://members.chello.at/easyfilter/Bresenham.pdf
    """
    pass

def _line(*args, **kwargs): # real signature unknown
    """
    Generate line pixel coordinates.
    
        Parameters
        ----------
        r0, c0 : int
            Starting position (row, column).
        r1, c1 : int
            End position (row, column).
    
        Returns
        -------
        rr, cc : (N,) ndarray of int
            Indices of pixels that belong to the line.
            May be used to directly index into an array, e.g.
            ``img[rr, cc] = 1``.
    
        See Also
        --------
        line_aa : Anti-aliased line generator
    """
    pass

def _line_aa(*args, **kwargs): # real signature unknown
    """
    Generate anti-aliased line pixel coordinates.
    
        Parameters
        ----------
        r0, c0 : int
            Starting position (row, column).
        r1, c1 : int
            End position (row, column).
    
        Returns
        -------
        rr, cc, val : (N,) ndarray (int, int, float)
            Indices of pixels (`rr`, `cc`) and intensity values (`val`).
            ``img[rr, cc] = val``.
    
        References
        ----------
        .. [1] A Rasterizing Algorithm for Drawing Curves, A. Zingl, 2012
               http://members.chello.at/easyfilter/Bresenham.pdf
    """
    pass

def _polygon(*args, **kwargs): # real signature unknown
    """
    Generate coordinates of pixels within polygon.
    
        Parameters
        ----------
        r : (N,) ndarray
            Row coordinates of vertices of polygon.
        c : (N,) ndarray
            Column coordinates of vertices of polygon.
        shape : tuple
            Image shape which is used to determine the maximum extent of output
            pixel coordinates. This is useful for polygons that exceed the image
            size. If None, the full extent of the polygon is used.
    
        Returns
        -------
        rr, cc : ndarray of int
            Pixel coordinates of polygon.
            May be used to directly index into an array, e.g.
            ``img[rr, cc] = 1``.
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000002367B035F28>'

__spec__ = None # (!) real value is "ModuleSpec(name='skimage.draw._draw', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000002367B035F28>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\skimage\\\\draw\\\\_draw.cp37-win_amd64.pyd')"

__test__ = {}

