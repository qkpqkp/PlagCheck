# encoding: utf-8
# module skimage.segmentation._slic
# from C:\Users\Doly\Anaconda3\lib\site-packages\skimage\segmentation\_slic.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py

# functions

def regular_grid(ar_shape, n_points): # reliably restored by inspect
    """
    Find `n_points` regularly spaced along `ar_shape`.
    
        The returned points (as slices) should be as close to cubically-spaced as
        possible. Essentially, the points are spaced by the Nth root of the input
        array size, where N is the number of dimensions. However, if an array
        dimension cannot fit a full step size, it is "discarded", and the
        computation is done for only the remaining dimensions.
    
        Parameters
        ----------
        ar_shape : array-like of ints
            The shape of the space embedding the grid. ``len(ar_shape)`` is the
            number of dimensions.
        n_points : int
            The (approximate) number of points to embed in the space.
    
        Returns
        -------
        slices : tuple of slice objects
            A slice along each dimension of `ar_shape`, such that the intersection
            of all the slices give the coordinates of regularly spaced points.
    
            .. versionchanged:: 0.14.1
                In scikit-image 0.14.1 and 0.15, the return type was changed from a
                list to a tuple to ensure `compatibility with Numpy 1.15`_ and
                higher. If your code requires the returned result to be a list, you
                may convert the output of this function to a list with:
    
                >>> result = list(regular_grid(ar_shape=(3, 20, 40), n_points=8))
    
                .. _compatibility with NumPy 1.15: https://github.com/numpy/numpy/blob/master/doc/release/1.15.0-notes.rst#deprecations
    
        Examples
        --------
        >>> ar = np.zeros((20, 40))
        >>> g = regular_grid(ar.shape, 8)
        >>> g
        (slice(5, None, 10), slice(5, None, 10))
        >>> ar[g] = 1
        >>> ar.sum()
        8.0
        >>> ar = np.zeros((20, 40))
        >>> g = regular_grid(ar.shape, 32)
        >>> g
        (slice(2, None, 5), slice(2, None, 5))
        >>> ar[g] = 1
        >>> ar.sum()
        32.0
        >>> ar = np.zeros((3, 20, 40))
        >>> g = regular_grid(ar.shape, 8)
        >>> g
        (slice(1, None, 3), slice(5, None, 10), slice(5, None, 10))
        >>> ar[g] = 1
        >>> ar.sum()
        8.0
    """
    pass

def _enforce_label_connectivity_cython(*args, **kwargs): # real signature unknown
    """
    Helper function to remove small disconnected regions from the labels
    
        Parameters
        ----------
        segments : 3D array of int, shape (Z, Y, X)
            The label field/superpixels found by SLIC.
        min_size: int
            Minimum size of the segment
        max_size: int
            Maximum size of the segment. This is done for performance reasons,
            to pre-allocate a sufficiently large array for the breadth first search
        Returns
        -------
        connected_segments : 3D array of int, shape (Z, Y, X)
            A label field with connected labels starting at label=1
    """
    pass

def _slic_cython(*args, **kwargs): # real signature unknown
    """
    Helper function for SLIC segmentation.
    
        Parameters
        ----------
        image_zyx : 4D array of double, shape (Z, Y, X, C)
            The input image.
        segments : 2D array of double, shape (N, 3 + C)
            The initial centroids obtained by SLIC as [Z, Y, X, C...].
        step : double
            The size of the step between two seeds in voxels.
        max_iter : int
            The maximum number of k-means iterations.
        spacing : 1D array of double, shape (3,)
            The voxel spacing along each image dimension. This parameter
            controls the weights of the distances along z, y, and x during
            k-means clustering.
        slic_zero : bool
            True to run SLIC-zero, False to run original SLIC.
    
        Returns
        -------
        nearest_segments : 3D array of int, shape (Z, Y, X)
            The label field/superpixels found by SLIC.
    
        Notes
        -----
        The image is considered to be in (z, y, x) order, which can be
        surprising. More commonly, the order (x, y, z) is used. However,
        in 3D image analysis, 'z' is usually the "special" dimension, with,
        for example, a different effective resolution than the other two
        axes. Therefore, x and y are often processed together, or viewed as
        a cut-plane through the volume. So, if the order was (x, y, z) and
        we wanted to look at the 5th cut plane, we would write::
    
            my_z_plane = img3d[:, :, 5]
    
        but, assuming a C-contiguous array, this would grab a discontiguous
        slice of memory, which is bad for performance. In contrast, if we
        see the image as (z, y, x) ordered, we would do::
    
            my_z_plane = img3d[5]
    
        and get back a contiguous block of memory. This is better both for
        performance and for readability.
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000019A18DB9B00>'

__spec__ = None # (!) real value is "ModuleSpec(name='skimage.segmentation._slic', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000019A18DB9B00>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\skimage\\\\segmentation\\\\_slic.cp37-win_amd64.pyd')"

__test__ = {}

