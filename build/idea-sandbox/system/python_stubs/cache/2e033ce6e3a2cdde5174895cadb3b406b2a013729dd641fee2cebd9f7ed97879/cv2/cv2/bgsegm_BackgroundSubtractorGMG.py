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


class bgsegm_BackgroundSubtractorGMG(__cv2.BackgroundSubtractor):
    # no doc
    def getBackgroundPrior(self): # real signature unknown; restored from __doc__
        """
        getBackgroundPrior() -> retval
        .   @brief Returns the prior probability that each individual pixel is a background pixel.
        """
        pass

    def getDecisionThreshold(self): # real signature unknown; restored from __doc__
        """
        getDecisionThreshold() -> retval
        .   @brief Returns the value of decision threshold.
        .   
        .       Decision value is the value above which pixel is determined to be FG.
        """
        pass

    def getDefaultLearningRate(self): # real signature unknown; restored from __doc__
        """
        getDefaultLearningRate() -> retval
        .   @brief Returns the learning rate of the algorithm.
        .   
        .       It lies between 0.0 and 1.0. It determines how quickly features are "forgotten" from
        .       histograms.
        """
        pass

    def getMaxFeatures(self): # real signature unknown; restored from __doc__
        """
        getMaxFeatures() -> retval
        .   @brief Returns total number of distinct colors to maintain in histogram.
        """
        pass

    def getMaxVal(self): # real signature unknown; restored from __doc__
        """
        getMaxVal() -> retval
        .   @brief Returns the maximum value taken on by pixels in image sequence. e.g. 1.0 or 255.
        """
        pass

    def getMinVal(self): # real signature unknown; restored from __doc__
        """
        getMinVal() -> retval
        .   @brief Returns the minimum value taken on by pixels in image sequence. Usually 0.
        """
        pass

    def getNumFrames(self): # real signature unknown; restored from __doc__
        """
        getNumFrames() -> retval
        .   @brief Returns the number of frames used to initialize background model.
        """
        pass

    def getQuantizationLevels(self): # real signature unknown; restored from __doc__
        """
        getQuantizationLevels() -> retval
        .   @brief Returns the parameter used for quantization of color-space.
        .   
        .       It is the number of discrete levels in each channel to be used in histograms.
        """
        pass

    def getSmoothingRadius(self): # real signature unknown; restored from __doc__
        """
        getSmoothingRadius() -> retval
        .   @brief Returns the kernel radius used for morphological operations
        """
        pass

    def getUpdateBackgroundModel(self): # real signature unknown; restored from __doc__
        """
        getUpdateBackgroundModel() -> retval
        .   @brief Returns the status of background model update
        """
        pass

    def setBackgroundPrior(self, bgprior): # real signature unknown; restored from __doc__
        """
        setBackgroundPrior(bgprior) -> None
        .   @brief Sets the prior probability that each individual pixel is a background pixel.
        """
        pass

    def setDecisionThreshold(self, thresh): # real signature unknown; restored from __doc__
        """
        setDecisionThreshold(thresh) -> None
        .   @brief Sets the value of decision threshold.
        """
        pass

    def setDefaultLearningRate(self, lr): # real signature unknown; restored from __doc__
        """
        setDefaultLearningRate(lr) -> None
        .   @brief Sets the learning rate of the algorithm.
        """
        pass

    def setMaxFeatures(self, maxFeatures): # real signature unknown; restored from __doc__
        """
        setMaxFeatures(maxFeatures) -> None
        .   @brief Sets total number of distinct colors to maintain in histogram.
        """
        pass

    def setMaxVal(self, val): # real signature unknown; restored from __doc__
        """
        setMaxVal(val) -> None
        .   @brief Sets the maximum value taken on by pixels in image sequence.
        """
        pass

    def setMinVal(self, val): # real signature unknown; restored from __doc__
        """
        setMinVal(val) -> None
        .   @brief Sets the minimum value taken on by pixels in image sequence.
        """
        pass

    def setNumFrames(self, nframes): # real signature unknown; restored from __doc__
        """
        setNumFrames(nframes) -> None
        .   @brief Sets the number of frames used to initialize background model.
        """
        pass

    def setQuantizationLevels(self, nlevels): # real signature unknown; restored from __doc__
        """
        setQuantizationLevels(nlevels) -> None
        .   @brief Sets the parameter used for quantization of color-space
        """
        pass

    def setSmoothingRadius(self, radius): # real signature unknown; restored from __doc__
        """
        setSmoothingRadius(radius) -> None
        .   @brief Sets the kernel radius used for morphological operations
        """
        pass

    def setUpdateBackgroundModel(self, update): # real signature unknown; restored from __doc__
        """
        setUpdateBackgroundModel(update) -> None
        .   @brief Sets the status of background model update
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


