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


class rgbd_RgbdOdometry(__cv2.rgbd_Odometry):
    # no doc
    def create(self, cameraMatrix=None, minDepth=None, maxDepth=None, maxDepthDiff=None, iterCounts=None, minGradientMagnitudes=None, maxPointsPart=None, transformType=None): # real signature unknown; restored from __doc__
        """
        create([, cameraMatrix[, minDepth[, maxDepth[, maxDepthDiff[, iterCounts[, minGradientMagnitudes[, maxPointsPart[, transformType]]]]]]]]) -> retval
        .   Constructor.
        .        * @param cameraMatrix Camera matrix
        .        * @param minDepth Pixels with depth less than minDepth will not be used (in meters)
        .        * @param maxDepth Pixels with depth larger than maxDepth will not be used (in meters)
        .        * @param maxDepthDiff Correspondences between pixels of two given frames will be filtered out
        .        *                     if their depth difference is larger than maxDepthDiff (in meters)
        .        * @param iterCounts Count of iterations on each pyramid level.
        .        * @param minGradientMagnitudes For each pyramid level the pixels will be filtered out
        .        *                              if they have gradient magnitude less than minGradientMagnitudes[level].
        .        * @param maxPointsPart The method uses a random pixels subset of size frameWidth x frameHeight x pointsPart
        .        * @param transformType Class of transformation
        """
        pass

    def getCameraMatrix(self): # real signature unknown; restored from __doc__
        """
        getCameraMatrix() -> retval
        .
        """
        pass

    def getIterationCounts(self): # real signature unknown; restored from __doc__
        """
        getIterationCounts() -> retval
        .
        """
        pass

    def getMaxDepth(self): # real signature unknown; restored from __doc__
        """
        getMaxDepth() -> retval
        .
        """
        pass

    def getMaxDepthDiff(self): # real signature unknown; restored from __doc__
        """
        getMaxDepthDiff() -> retval
        .
        """
        pass

    def getMaxPointsPart(self): # real signature unknown; restored from __doc__
        """
        getMaxPointsPart() -> retval
        .
        """
        pass

    def getMaxRotation(self): # real signature unknown; restored from __doc__
        """
        getMaxRotation() -> retval
        .
        """
        pass

    def getMaxTranslation(self): # real signature unknown; restored from __doc__
        """
        getMaxTranslation() -> retval
        .
        """
        pass

    def getMinDepth(self): # real signature unknown; restored from __doc__
        """
        getMinDepth() -> retval
        .
        """
        pass

    def getMinGradientMagnitudes(self): # real signature unknown; restored from __doc__
        """
        getMinGradientMagnitudes() -> retval
        .
        """
        pass

    def getTransformType(self): # real signature unknown; restored from __doc__
        """
        getTransformType() -> retval
        .
        """
        pass

    def prepareFrameCache(self, frame, cacheType): # real signature unknown; restored from __doc__
        """
        prepareFrameCache(frame, cacheType) -> retval
        .
        """
        pass

    def setCameraMatrix(self, val): # real signature unknown; restored from __doc__
        """
        setCameraMatrix(val) -> None
        .
        """
        pass

    def setIterationCounts(self, val): # real signature unknown; restored from __doc__
        """
        setIterationCounts(val) -> None
        .
        """
        pass

    def setMaxDepth(self, val): # real signature unknown; restored from __doc__
        """
        setMaxDepth(val) -> None
        .
        """
        pass

    def setMaxDepthDiff(self, val): # real signature unknown; restored from __doc__
        """
        setMaxDepthDiff(val) -> None
        .
        """
        pass

    def setMaxPointsPart(self, val): # real signature unknown; restored from __doc__
        """
        setMaxPointsPart(val) -> None
        .
        """
        pass

    def setMaxRotation(self, val): # real signature unknown; restored from __doc__
        """
        setMaxRotation(val) -> None
        .
        """
        pass

    def setMaxTranslation(self, val): # real signature unknown; restored from __doc__
        """
        setMaxTranslation(val) -> None
        .
        """
        pass

    def setMinDepth(self, val): # real signature unknown; restored from __doc__
        """
        setMinDepth(val) -> None
        .
        """
        pass

    def setMinGradientMagnitudes(self, val): # real signature unknown; restored from __doc__
        """
        setMinGradientMagnitudes(val) -> None
        .
        """
        pass

    def setTransformType(self, val): # real signature unknown; restored from __doc__
        """
        setTransformType(val) -> None
        .
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

