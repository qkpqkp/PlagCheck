# encoding: utf-8
# module skimage.feature._haar
# from C:\Users\Doly\Anaconda3\lib\site-packages\skimage\feature\_haar.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py

# functions

def haar_like_feature_coord_wrapper(*args, **kwargs): # real signature unknown
    """
    Compute the coordinates of Haar-like features.
    
        Parameters
        ----------
        width : int
            Width of the detection window.
        height : int
            Height of the detection window.
        feature_type : str
            The type of feature to consider:
    
            - 'type-2-x': 2 rectangles varying along the x axis;
            - 'type-2-y': 2 rectangles varying along the y axis;
            - 'type-3-x': 3 rectangles varying along the x axis;
            - 'type-3-y': 3 rectangles varying along the y axis;
            - 'type-4': 4 rectangles varying along x and y axis.
    
        Returns
        -------
        feature_coord : (n_features, n_rectangles, 2, 2), ndarray of list of tuple coord
            Coordinates of the rectangles for each feature.
        feature_type : (n_features,), ndarray of str
            The corresponding type for each feature.
    """
    pass

def haar_like_feature_wrapper(*args, **kwargs): # real signature unknown
    """
    Compute the Haar-like features for a region of interest (ROI) of an
        integral image.
    
        Haar-like features have been successfully used for image classification and
        object detection [1]_. It has been used for real-time face detection
        algorithm proposed in [2]_.
    
        Parameters
        ----------
        int_image : (M, N) ndarray
            Integral image for which the features need to be computed.
        r : int
            Row-coordinate of top left corner of the detection window.
        c : int
            Column-coordinate of top left corner of the detection window.
        width : int
            Width of the detection window.
        height : int
            Height of the detection window.
        feature_type : str
            The type of feature to consider:
    
            - 'type-2-x': 2 rectangles varying along the x axis;
            - 'type-2-y': 2 rectangles varying along the y axis;
            - 'type-3-x': 3 rectangles varying along the x axis;
            - 'type-3-y': 3 rectangles varying along the y axis;
            - 'type-4': 4 rectangles varying along x and y axis.
    
        Returns
        -------
        haar_features : (n_features,) ndarray
            Resulting Haar-like features. Each value is equal to the subtraction of
            sums of the positive and negative rectangles. The data type depends of
            the data type of `int_image`: `int` when the data type of `int_image`
            is `uint` or `int` and `float` when the data type of `int_image` is
            `float`.
    
        References
        ----------
        .. [1] https://en.wikipedia.org/wiki/Haar-like_feature
        .. [2] Oren, M., Papageorgiou, C., Sinha, P., Osuna, E., & Poggio, T.
               (1997, June). Pedestrian detection using wavelet templates.
               In Computer Vision and Pattern Recognition, 1997. Proceedings.,
               1997 IEEE Computer Society Conference on (pp. 193-199). IEEE.
               http://tinyurl.com/y6ulxfta
               :DOI:`10.1109/CVPR.1997.609319`
        .. [3] Viola, Paul, and Michael J. Jones. "Robust real-time face
               detection." International journal of computer vision 57.2
               (2004): 137-154.
               http://www.merl.com/publications/docs/TR2004-043.pdf
               :DOI:`10.1109/CVPR.2001.990517`
    """
    pass

def integral_image(image): # reliably restored by inspect
    """
    Integral image / summed area table.
    
        The integral image contains the sum of all elements above and to the
        left of it, i.e.:
    
        .. math::
    
           S[m, n] = \sum_{i \leq m} \sum_{j \leq n} X[i, j]
    
        Parameters
        ----------
        image : ndarray
            Input image.
    
        Returns
        -------
        S : ndarray
            Integral image/summed area table of same shape as input image.
    
        References
        ----------
        .. [1] F.C. Crow, "Summed-area tables for texture mapping,"
               ACM SIGGRAPH Computer Graphics, vol. 18, 1984, pp. 207-212.
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

FEATURE_TYPE = {
    'type-2-x': 0,
    'type-2-y': 1,
    'type-3-x': 2,
    'type-3-y': 3,
    'type-4': 4,
}

N_RECTANGLE = {
    'type-2-x': 2,
    'type-2-y': 2,
    'type-3-x': 3,
    'type-3-y': 3,
    'type-4': 4,
}

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000002444420CDA0>'

__pyx_capi__ = {
    '__pyx_fuse_0_haar_like_feature': None, # (!) real value is '<capsule object "__Pyx_memviewslice (__Pyx_memviewslice, std::vector<std::vector<struct __pyx_t_7skimage_7feature_5_haar_Rectangle> > , Py_ssize_t, Py_ssize_t)" at 0x00000244441E76C0>'
    '__pyx_fuse_0haar_like_feature_wrapper': None, # (!) real value is '<capsule object "PyObject *(PyArrayObject *, PyObject *, PyObject *, PyObject *, PyObject *, PyObject *, PyObject *, int __pyx_skip_dispatch)" at 0x00000244441E7930>'
    '__pyx_fuse_1_haar_like_feature': None, # (!) real value is '<capsule object "__Pyx_memviewslice (__Pyx_memviewslice, std::vector<std::vector<struct __pyx_t_7skimage_7feature_5_haar_Rectangle> > , Py_ssize_t, Py_ssize_t)" at 0x00000244441E7690>'
    '__pyx_fuse_1haar_like_feature_wrapper': None, # (!) real value is '<capsule object "PyObject *(PyArrayObject *, PyObject *, PyObject *, PyObject *, PyObject *, PyObject *, PyObject *, int __pyx_skip_dispatch)" at 0x00000244441E7960>'
    '__pyx_fuse_2_haar_like_feature': None, # (!) real value is '<capsule object "__Pyx_memviewslice (__Pyx_memviewslice, std::vector<std::vector<struct __pyx_t_7skimage_7feature_5_haar_Rectangle> > , Py_ssize_t, Py_ssize_t)" at 0x00000244441E7600>'
    '__pyx_fuse_2haar_like_feature_wrapper': None, # (!) real value is '<capsule object "PyObject *(PyArrayObject *, PyObject *, PyObject *, PyObject *, PyObject *, PyObject *, PyObject *, int __pyx_skip_dispatch)" at 0x00000244441E7990>'
    '__pyx_fuse_3_haar_like_feature': None, # (!) real value is '<capsule object "__Pyx_memviewslice (__Pyx_memviewslice, std::vector<std::vector<struct __pyx_t_7skimage_7feature_5_haar_Rectangle> > , Py_ssize_t, Py_ssize_t)" at 0x00000244441E75D0>'
    '__pyx_fuse_3haar_like_feature_wrapper': None, # (!) real value is '<capsule object "PyObject *(PyArrayObject *, PyObject *, PyObject *, PyObject *, PyObject *, PyObject *, PyObject *, int __pyx_skip_dispatch)" at 0x00000244441E79C0>'
    '__pyx_fuse_4_haar_like_feature': None, # (!) real value is '<capsule object "__Pyx_memviewslice (__Pyx_memviewslice, std::vector<std::vector<struct __pyx_t_7skimage_7feature_5_haar_Rectangle> > , Py_ssize_t, Py_ssize_t)" at 0x00000244441E7570>'
    '__pyx_fuse_4haar_like_feature_wrapper': None, # (!) real value is '<capsule object "PyObject *(PyArrayObject *, PyObject *, PyObject *, PyObject *, PyObject *, PyObject *, PyObject *, int __pyx_skip_dispatch)" at 0x00000244441E79F0>'
    '__pyx_fuse_5_haar_like_feature': None, # (!) real value is '<capsule object "__Pyx_memviewslice (__Pyx_memviewslice, std::vector<std::vector<struct __pyx_t_7skimage_7feature_5_haar_Rectangle> > , Py_ssize_t, Py_ssize_t)" at 0x00000244441E7540>'
    '__pyx_fuse_5haar_like_feature_wrapper': None, # (!) real value is '<capsule object "PyObject *(PyArrayObject *, PyObject *, PyObject *, PyObject *, PyObject *, PyObject *, PyObject *, int __pyx_skip_dispatch)" at 0x00000244441E7A20>'
    '__pyx_fuse_6_haar_like_feature': None, # (!) real value is '<capsule object "__Pyx_memviewslice (__Pyx_memviewslice, std::vector<std::vector<struct __pyx_t_7skimage_7feature_5_haar_Rectangle> > , Py_ssize_t, Py_ssize_t)" at 0x00000244441E78A0>'
    '__pyx_fuse_6haar_like_feature_wrapper': None, # (!) real value is '<capsule object "PyObject *(PyArrayObject *, PyObject *, PyObject *, PyObject *, PyObject *, PyObject *, PyObject *, int __pyx_skip_dispatch)" at 0x00000244441E7A50>'
    '__pyx_fuse_7_haar_like_feature': None, # (!) real value is '<capsule object "__Pyx_memviewslice (__Pyx_memviewslice, std::vector<std::vector<struct __pyx_t_7skimage_7feature_5_haar_Rectangle> > , Py_ssize_t, Py_ssize_t)" at 0x00000244441E7870>'
    '__pyx_fuse_7haar_like_feature_wrapper': None, # (!) real value is '<capsule object "PyObject *(PyArrayObject *, PyObject *, PyObject *, PyObject *, PyObject *, PyObject *, PyObject *, int __pyx_skip_dispatch)" at 0x00000244441E7A80>'
    '__pyx_fuse_8_haar_like_feature': None, # (!) real value is '<capsule object "__Pyx_memviewslice (__Pyx_memviewslice, std::vector<std::vector<struct __pyx_t_7skimage_7feature_5_haar_Rectangle> > , Py_ssize_t, Py_ssize_t)" at 0x00000244441E78D0>'
    '__pyx_fuse_8haar_like_feature_wrapper': None, # (!) real value is '<capsule object "PyObject *(PyArrayObject *, PyObject *, PyObject *, PyObject *, PyObject *, PyObject *, PyObject *, int __pyx_skip_dispatch)" at 0x00000244441E7AB0>'
    '__pyx_fuse_9_haar_like_feature': None, # (!) real value is '<capsule object "__Pyx_memviewslice (__Pyx_memviewslice, std::vector<std::vector<struct __pyx_t_7skimage_7feature_5_haar_Rectangle> > , Py_ssize_t, Py_ssize_t)" at 0x00000244441E7900>'
    '__pyx_fuse_9haar_like_feature_wrapper': None, # (!) real value is '<capsule object "PyObject *(PyArrayObject *, PyObject *, PyObject *, PyObject *, PyObject *, PyObject *, PyObject *, int __pyx_skip_dispatch)" at 0x00000244441E7AE0>'
    '_haar_like_feature_coord': None, # (!) real value is '<capsule object "std::vector<std::vector<struct __pyx_t_7skimage_7feature_5_haar_Rectangle> >  (Py_ssize_t, Py_ssize_t, unsigned int)" at 0x00000244441E7720>'
    'haar_like_feature_coord_wrapper': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyObject *, PyObject *, int __pyx_skip_dispatch)" at 0x00000244441E76F0>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='skimage.feature._haar', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000002444420CDA0>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\skimage\\\\feature\\\\_haar.cp37-win_amd64.pyd')"

__test__ = {}

