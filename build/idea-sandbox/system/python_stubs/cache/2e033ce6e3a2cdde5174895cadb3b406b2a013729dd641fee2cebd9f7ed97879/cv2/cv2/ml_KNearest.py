# encoding: utf-8
# module cv2.cv2
# from C:\Users\Doly\Anaconda3\lib\site-packages\cv2\cv2.cp37-win_amd64.pyd
# by generator 1.147
""" Python wrapper for OpenCV. """

# imports
import cv2.cv2 as  # C:\Users\Doly\Anaconda3\lib\site-packages\cv2\cv2.cp37-win_amd64.pyd
import cv2.Error as Error # <module 'cv2.Error'>
import cv2.aruco as aruco # <module 'cv2.aruco'>
import cv2.bgsegm as bgsegm # <module 'cv2.bgsegm'>
import cv2.bioinspired as bioinspired # <module 'cv2.bioinspired'>
import cv2.cuda as cuda # <module 'cv2.cuda'>
import cv2.datasets as datasets # <module 'cv2.datasets'>
import cv2.detail as detail # <module 'cv2.detail'>
import cv2.dnn as dnn # <module 'cv2.dnn'>
import cv2.face as face # <module 'cv2.face'>
import cv2.fisheye as fisheye # <module 'cv2.fisheye'>
import cv2.flann as flann # <module 'cv2.flann'>
import cv2.ft as ft # <module 'cv2.ft'>
import cv2.hfs as hfs # <module 'cv2.hfs'>
import cv2.img_hash as img_hash # <module 'cv2.img_hash'>
import cv2.instr as instr # <module 'cv2.instr'>
import cv2.ipp as ipp # <module 'cv2.ipp'>
import cv2.kinfu as kinfu # <module 'cv2.kinfu'>
import cv2.line_descriptor as line_descriptor # <module 'cv2.line_descriptor'>
import cv2.linemod as linemod # <module 'cv2.linemod'>
import cv2.ml as ml # <module 'cv2.ml'>
import cv2.motempl as motempl # <module 'cv2.motempl'>
import cv2.multicalib as multicalib # <module 'cv2.multicalib'>
import cv2.ocl as ocl # <module 'cv2.ocl'>
import cv2.ogl as ogl # <module 'cv2.ogl'>
import cv2.omnidir as omnidir # <module 'cv2.omnidir'>
import cv2.optflow as optflow # <module 'cv2.optflow'>
import cv2.plot as plot # <module 'cv2.plot'>
import cv2.ppf_match_3d as ppf_match_3d # <module 'cv2.ppf_match_3d'>
import cv2.quality as quality # <module 'cv2.quality'>
import cv2.reg as reg # <module 'cv2.reg'>
import cv2.rgbd as rgbd # <module 'cv2.rgbd'>
import cv2.saliency as saliency # <module 'cv2.saliency'>
import cv2.samples as samples # <module 'cv2.samples'>
import cv2.structured_light as structured_light # <module 'cv2.structured_light'>
import cv2.text as text # <module 'cv2.text'>
import cv2.utils as utils # <module 'cv2.utils'>
import cv2.videoio_registry as videoio_registry # <module 'cv2.videoio_registry'>
import cv2.videostab as videostab # <module 'cv2.videostab'>
import cv2.xfeatures2d as xfeatures2d # <module 'cv2.xfeatures2d'>
import cv2.ximgproc as ximgproc # <module 'cv2.ximgproc'>
import cv2.xphoto as xphoto # <module 'cv2.xphoto'>
import cv2 as __cv2


class ml_KNearest(__cv2.ml_StatModel):
    # no doc
    def create(self): # real signature unknown; restored from __doc__
        """
        create() -> retval
        .   @brief Creates the empty model
        .   
        .       The static method creates empty %KNearest classifier. It should be then trained using StatModel::train method.
        """
        pass

    def findNearest(self, samples, k, results=None, neighborResponses=None, dist=None): # real signature unknown; restored from __doc__
        """
        findNearest(samples, k[, results[, neighborResponses[, dist]]]) -> retval, results, neighborResponses, dist
        .   @brief Finds the neighbors and predicts responses for input vectors.
        .   
        .       @param samples Input samples stored by rows. It is a single-precision floating-point matrix of
        .           `<number_of_samples> * k` size.
        .       @param k Number of used nearest neighbors. Should be greater than 1.
        .       @param results Vector with results of prediction (regression or classification) for each input
        .           sample. It is a single-precision floating-point vector with `<number_of_samples>` elements.
        .       @param neighborResponses Optional output values for corresponding neighbors. It is a single-
        .           precision floating-point matrix of `<number_of_samples> * k` size.
        .       @param dist Optional output distances from the input vectors to the corresponding neighbors. It
        .           is a single-precision floating-point matrix of `<number_of_samples> * k` size.
        .   
        .       For each input vector (a row of the matrix samples), the method finds the k nearest neighbors.
        .       In case of regression, the predicted result is a mean value of the particular vector's neighbor
        .       responses. In case of classification, the class is determined by voting.
        .   
        .       For each input vector, the neighbors are sorted by their distances to the vector.
        .   
        .       In case of C++ interface you can use output pointers to empty matrices and the function will
        .       allocate memory itself.
        .   
        .       If only a single input vector is passed, all output matrices are optional and the predicted
        .       value is returned by the method.
        .   
        .       The function is parallelized with the TBB library.
        """
        pass

    def getAlgorithmType(self): # real signature unknown; restored from __doc__
        """
        getAlgorithmType() -> retval
        .   @see setAlgorithmType
        """
        pass

    def getDefaultK(self): # real signature unknown; restored from __doc__
        """
        getDefaultK() -> retval
        .   @see setDefaultK
        """
        pass

    def getEmax(self): # real signature unknown; restored from __doc__
        """
        getEmax() -> retval
        .   @see setEmax
        """
        pass

    def getIsClassifier(self): # real signature unknown; restored from __doc__
        """
        getIsClassifier() -> retval
        .   @see setIsClassifier
        """
        pass

    def load(self, filepath): # real signature unknown; restored from __doc__
        """
        load(filepath) -> retval
        .   @brief Loads and creates a serialized knearest from a file
        .        *
        .        * Use KNearest::save to serialize and store an KNearest to disk.
        .        * Load the KNearest from this file again, by calling this function with the path to the file.
        .        *
        .        * @param filepath path to serialized KNearest
        """
        pass

    def setAlgorithmType(self, val): # real signature unknown; restored from __doc__
        """
        setAlgorithmType(val) -> None
        .   @copybrief getAlgorithmType @see getAlgorithmType
        """
        pass

    def setDefaultK(self, val): # real signature unknown; restored from __doc__
        """
        setDefaultK(val) -> None
        .   @copybrief getDefaultK @see getDefaultK
        """
        pass

    def setEmax(self, val): # real signature unknown; restored from __doc__
        """
        setEmax(val) -> None
        .   @copybrief getEmax @see getEmax
        """
        pass

    def setIsClassifier(self, val): # real signature unknown; restored from __doc__
        """
        setIsClassifier(val) -> None
        .   @copybrief getIsClassifier @see getIsClassifier
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass


