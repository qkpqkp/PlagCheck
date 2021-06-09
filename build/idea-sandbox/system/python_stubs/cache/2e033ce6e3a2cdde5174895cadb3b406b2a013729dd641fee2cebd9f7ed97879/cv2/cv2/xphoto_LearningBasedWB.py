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


class xphoto_LearningBasedWB(__cv2.xphoto_WhiteBalancer):
    # no doc
    def extractSimpleFeatures(self, src, dst=None): # real signature unknown; restored from __doc__
        """
        extractSimpleFeatures(src[, dst]) -> dst
        .   @brief Implements the feature extraction part of the algorithm.
        .   
        .       In accordance with @cite Cheng2015 , computes the following features for the input image:
        .       1. Chromaticity of an average (R,G,B) tuple
        .       2. Chromaticity of the brightest (R,G,B) tuple (while ignoring saturated pixels)
        .       3. Chromaticity of the dominant (R,G,B) tuple (the one that has the highest value in the RGB histogram)
        .       4. Mode of the chromaticity palette, that is constructed by taking 300 most common colors according to
        .          the RGB histogram and projecting them on the chromaticity plane. Mode is the most high-density point
        .          of the palette, which is computed by a straightforward fixed-bandwidth kernel density estimator with
        .          a Epanechnikov kernel function.
        .   
        .       @param src Input three-channel image (BGR color space is assumed).
        .       @param dst An array of four (r,g) chromaticity tuples corresponding to the features listed above.
        """
        pass

    def getHistBinNum(self): # real signature unknown; restored from __doc__
        """
        getHistBinNum() -> retval
        .   @brief Defines the size of one dimension of a three-dimensional RGB histogram that is used internally
        .           by the algorithm. It often makes sense to increase the number of bins for images with higher bit depth
        .           (e.g. 256 bins for a 12 bit image).
        .   @see setHistBinNum
        """
        pass

    def getRangeMaxVal(self): # real signature unknown; restored from __doc__
        """
        getRangeMaxVal() -> retval
        .   @brief Maximum possible value of the input image (e.g. 255 for 8 bit images,
        .                  4095 for 12 bit images)
        .   @see setRangeMaxVal
        """
        pass

    def getSaturationThreshold(self): # real signature unknown; restored from __doc__
        """
        getSaturationThreshold() -> retval
        .   @brief Threshold that is used to determine saturated pixels, i.e. pixels where at least one of the
        .           channels exceeds \f$\texttt{saturation_threshold}\times\texttt{range_max_val}\f$ are ignored.
        .   @see setSaturationThreshold
        """
        pass

    def setHistBinNum(self, val): # real signature unknown; restored from __doc__
        """
        setHistBinNum(val) -> None
        .   @copybrief getHistBinNum @see getHistBinNum
        """
        pass

    def setRangeMaxVal(self, val): # real signature unknown; restored from __doc__
        """
        setRangeMaxVal(val) -> None
        .   @copybrief getRangeMaxVal @see getRangeMaxVal
        """
        pass

    def setSaturationThreshold(self, val): # real signature unknown; restored from __doc__
        """
        setSaturationThreshold(val) -> None
        .   @copybrief getSaturationThreshold @see getSaturationThreshold
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


