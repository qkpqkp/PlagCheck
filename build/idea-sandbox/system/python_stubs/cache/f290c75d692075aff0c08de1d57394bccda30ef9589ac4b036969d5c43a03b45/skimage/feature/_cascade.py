# encoding: utf-8
# module skimage.feature._cascade
# from C:\Users\Doly\Anaconda3\lib\site-packages\skimage\feature\_cascade.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py
import xml.etree.ElementTree as ET # C:\Users\Doly\Anaconda3\lib\xml\etree\ElementTree.py
import math as math # <module 'math' (built-in)>

# functions

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

def rgb2gray(rgb): # reliably restored by inspect
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

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class Cascade(object):
    """
    Class for cascade of classifiers that is used for object detection.
    
        The main idea behind cascade of classifiers is to create classifiers
        of medium accuracy and ensemble them into one strong classifier
        instead of just creating a strong one. The second advantage of cascade
        classifier is that easy examples can be classified only by evaluating
        some of the classifiers in the cascade, making the process much faster
        than the process of evaluating a one strong classifier.
    
        Attributes
        ----------
        eps : float
            Accuracy parameter. Increasing it, makes the classifier detect less
            false positives but at the same time the false negative score increases.
        stages_number : Py_ssize_t
            Amount of stages in a cascade. Each cascade consists of stumps i.e.
            trained features.
        stumps_number : Py_ssize_t
            The overall amount of stumps in all the stages of cascade.
        features_number : Py_ssize_t
            The overall amount of different features used by cascade.
            Two stumps can use the same features but has different trained
            values.
        window_width : Py_ssize_t
            The width of a detection window that is used. Objects smaller than
            this window can't be detected.
        window_height : Py_ssize_t
            The height of a detection window.
        stages : Stage*
            A link to the c array that stores stages information using
            Stage struct.
        features : MBLBP*
            Link to the c array that stores MBLBP features using MBLBP struct.
        LUTs : cnp.uint32_t*
            The ling to the array with look-up tables that are used by trained
            MBLBP features (MBLBPStumps) to evaluate a particular region.
    """
    def detect_multi_scale(self, *args, **kwargs): # real signature unknown
        """
        Search for the object on multiple scales of input image.
        
                The function takes the input image, the scale factor by which the
                searching window is multiplied on each step, minimum window size
                and maximum window size that specify the interval for the search
                windows that are applied to the input image to detect objects.
        
                Parameters
                ----------
                img : 2-D or 3-D ndarray
                    Ndarray that represents the input image.
                scale_factor : float
                    The scale by which searching window is multiplied on each step.
                step_ratio : float
                    The ratio by which the search step in multiplied on each scale
                    of the image. 1 represents the exaustive search and usually is
                    slow. By setting this parameter to higher values the results will
                    be worse but the computation will be much faster. Usually, values
                    in the interval [1, 1.5] give good results.
                min_size : typle (int, int)
                    Minimum size of the search window.
                max_size : typle (int, int)
                    Maximum size of the search window.
                min_neighbour_number : int
                    Minimum amount of intersecting detections in order for detection
                    to be approved by the function.
                intersection_score_threshold : float
                    The minimum value of value of ratio
                    (intersection area) / (small rectangle ratio) in order to merge
                    two detections into one.
        
                Returns
                -------
                output : list of dicts
                    Dict have form {'r': int, 'c': int, 'width': int, 'height': int},
                    where 'r' represents row position of top left corner of detected
                    window, 'c' - col position, 'width' - width of detected window,
                    'height' - height of detected window.
        """
        pass

    def _get_contiguous_integral_image(self, *args, **kwargs): # real signature unknown
        """
        Get a c-contiguous array that represents the integral image.
        
                The function converts the input image into the integral image in
                a format that is suitable for work of internal functions of
                the cascade classifier class. The function converts the image
                to gray-scale float representation, computes the integral image
                and makes it c-contiguous.
        
                Parameters
                ----------
                img : 2-D or 3-D ndarray
                    Ndarray that represents the input image.
        
                Returns
                -------
                int_img : 2-D floats ndarray
                    C-contiguous integral image of the input image.
        """
        pass

    def _get_valid_scale_factors(self, *args, **kwargs): # real signature unknown
        """
        Get the valid scale multipliers for the original window size.
        
                The function takes the minimal size of window and maximum size of
                window as interval and finds all the multipliers that will give the
                windows which sizes will be not less than the min_size and not bigger
                than the max_size.
        
                Parameters
                ----------
                min_size : typle (int, int)
                    Minimum size of window for which to search the scale factor.
                max_size : typle (int, int)
                    Maximum size of window for which to search the scale factor.
                scale_step : float
                    The scale by which the search window is multiplied
                    on each iteration.
        
                Returns
                -------
                scale_factors : 1-D floats ndarray
                    The scale factors that give the window sizes that are in the
                    specified interval after multiplying the search window.
        """
        pass

    def _load_xml(self, *args, **kwargs): # real signature unknown
        """
        Load the parameters of cascade classifier into the class.
        
                The function takes the file with the parameters that represent
                trained cascade classifier and loads them into class for later
                use.
        
                Parameters
                ----------
                xml_file : filename or file object
                    File that contains the cascade classifier.
                eps : float
                    Accuracy parameter. Increasing it, makes the classifier detect less
                    false positives but at the same time the false negative score increases.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """
        Initialize cascade classifier.
        
                Parameters
                ----------
                xml_file : file's path or file's object
                    A file in a OpenCv format from which all the cascade classifier's
                    parameters are loaded.
                eps : float
                    Accuracy parameter. Increasing it, makes the classifier detect less
                    false positives but at the same time the false negative score increases.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    eps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    features_number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stages_number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stumps_number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    window_height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    window_width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000219071F0270>'


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000219071F6240>'

__spec__ = None # (!) real value is "ModuleSpec(name='skimage.feature._cascade', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000219071F6240>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\skimage\\\\feature\\\\_cascade.cp37-win_amd64.pyd')"

__test__ = {}

