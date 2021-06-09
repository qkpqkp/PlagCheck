# encoding: utf-8
# module skimage.measure._pnpoly
# from C:\Users\Doly\Anaconda3\lib\site-packages\skimage\measure\_pnpoly.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py

# functions

def _grid_points_in_poly(*args, **kwargs): # real signature unknown
    """
    Test whether points on a specified grid are inside a polygon.
    
        For each ``(r, c)`` coordinate on a grid, i.e. ``(0, 0)``, ``(0, 1)`` etc.,
        test whether that point lies inside a polygon.
    
        Parameters
        ----------
        shape : tuple (M, N)
            Shape of the grid.
        verts : (V, 2) array
            Specify the V vertices of the polygon, sorted either clockwise
            or anti-clockwise.  The first point may (but does not need to be)
            duplicated.
    
        See Also
        --------
        points_in_poly
    
        Returns
        -------
        mask : (M, N) ndarray of bool
            True where the grid falls inside the polygon.
    """
    pass

def _points_in_poly(*args, **kwargs): # real signature unknown
    """
    Test whether points lie inside a polygon.
    
        Parameters
        ----------
        points : (N, 2) array
            Input points, ``(x, y)``.
        verts : (M, 2) array
            Vertices of the polygon, sorted either clockwise or anti-clockwise.
            The first point may (but does not need to be) duplicated.
    
        See Also
        --------
        grid_points_in_poly
    
        Returns
        -------
        mask : (N,) array of bool
            True if corresponding point is inside the polygon.
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001FA2C757048>'

__spec__ = None # (!) real value is "ModuleSpec(name='skimage.measure._pnpoly', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001FA2C757048>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\skimage\\\\measure\\\\_pnpoly.cp37-win_amd64.pyd')"

__test__ = {}

