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


class DISOpticalFlow(__cv2.DenseOpticalFlow):
    # no doc
    def create(self, preset=None): # real signature unknown; restored from __doc__
        """
        create([, preset]) -> retval
        .   @brief Creates an instance of DISOpticalFlow
        .   
        .       @param preset one of PRESET_ULTRAFAST, PRESET_FAST and PRESET_MEDIUM
        """
        pass

    def getFinestScale(self): # real signature unknown; restored from __doc__
        """
        getFinestScale() -> retval
        .   @brief Finest level of the Gaussian pyramid on which the flow is computed (zero level
        .           corresponds to the original image resolution). The final flow is obtained by bilinear upscaling.
        .   @see setFinestScale
        """
        pass

    def getGradientDescentIterations(self): # real signature unknown; restored from __doc__
        """
        getGradientDescentIterations() -> retval
        .   @brief Maximum number of gradient descent iterations in the patch inverse search stage. Higher values
        .           may improve quality in some cases.
        .   @see setGradientDescentIterations
        """
        pass

    def getPatchSize(self): # real signature unknown; restored from __doc__
        """
        getPatchSize() -> retval
        .   @brief Size of an image patch for matching (in pixels). Normally, default 8x8 patches work well
        .           enough in most cases.
        .   @see setPatchSize
        """
        pass

    def getPatchStride(self): # real signature unknown; restored from __doc__
        """
        getPatchStride() -> retval
        .   @brief Stride between neighbor patches. Must be less than patch size. Lower values correspond
        .           to higher flow quality.
        .   @see setPatchStride
        """
        pass

    def getUseMeanNormalization(self): # real signature unknown; restored from __doc__
        """
        getUseMeanNormalization() -> retval
        .   @brief Whether to use mean-normalization of patches when computing patch distance. It is turned on
        .           by default as it typically provides a noticeable quality boost because of increased robustness to
        .           illumination variations. Turn it off if you are certain that your sequence doesn't contain any changes
        .           in illumination.
        .   @see setUseMeanNormalization
        """
        pass

    def getUseSpatialPropagation(self): # real signature unknown; restored from __doc__
        """
        getUseSpatialPropagation() -> retval
        .   @brief Whether to use spatial propagation of good optical flow vectors. This option is turned on by
        .           default, as it tends to work better on average and can sometimes help recover from major errors
        .           introduced by the coarse-to-fine scheme employed by the DIS optical flow algorithm. Turning this
        .           option off can make the output flow field a bit smoother, however.
        .   @see setUseSpatialPropagation
        """
        pass

    def getVariationalRefinementAlpha(self): # real signature unknown; restored from __doc__
        """
        getVariationalRefinementAlpha() -> retval
        .   @brief Weight of the smoothness term
        .   @see setVariationalRefinementAlpha
        """
        pass

    def getVariationalRefinementDelta(self): # real signature unknown; restored from __doc__
        """
        getVariationalRefinementDelta() -> retval
        .   @brief Weight of the color constancy term
        .   @see setVariationalRefinementDelta
        """
        pass

    def getVariationalRefinementGamma(self): # real signature unknown; restored from __doc__
        """
        getVariationalRefinementGamma() -> retval
        .   @brief Weight of the gradient constancy term
        .   @see setVariationalRefinementGamma
        """
        pass

    def getVariationalRefinementIterations(self): # real signature unknown; restored from __doc__
        """
        getVariationalRefinementIterations() -> retval
        .   @brief Number of fixed point iterations of variational refinement per scale. Set to zero to
        .           disable variational refinement completely. Higher values will typically result in more smooth and
        .           high-quality flow.
        .   @see setGradientDescentIterations
        """
        pass

    def setFinestScale(self, val): # real signature unknown; restored from __doc__
        """
        setFinestScale(val) -> None
        .   @copybrief getFinestScale @see getFinestScale
        """
        pass

    def setGradientDescentIterations(self, val): # real signature unknown; restored from __doc__
        """
        setGradientDescentIterations(val) -> None
        .   @copybrief getGradientDescentIterations @see getGradientDescentIterations
        """
        pass

    def setPatchSize(self, val): # real signature unknown; restored from __doc__
        """
        setPatchSize(val) -> None
        .   @copybrief getPatchSize @see getPatchSize
        """
        pass

    def setPatchStride(self, val): # real signature unknown; restored from __doc__
        """
        setPatchStride(val) -> None
        .   @copybrief getPatchStride @see getPatchStride
        """
        pass

    def setUseMeanNormalization(self, val): # real signature unknown; restored from __doc__
        """
        setUseMeanNormalization(val) -> None
        .   @copybrief getUseMeanNormalization @see getUseMeanNormalization
        """
        pass

    def setUseSpatialPropagation(self, val): # real signature unknown; restored from __doc__
        """
        setUseSpatialPropagation(val) -> None
        .   @copybrief getUseSpatialPropagation @see getUseSpatialPropagation
        """
        pass

    def setVariationalRefinementAlpha(self, val): # real signature unknown; restored from __doc__
        """
        setVariationalRefinementAlpha(val) -> None
        .   @copybrief getVariationalRefinementAlpha @see getVariationalRefinementAlpha
        """
        pass

    def setVariationalRefinementDelta(self, val): # real signature unknown; restored from __doc__
        """
        setVariationalRefinementDelta(val) -> None
        .   @copybrief getVariationalRefinementDelta @see getVariationalRefinementDelta
        """
        pass

    def setVariationalRefinementGamma(self, val): # real signature unknown; restored from __doc__
        """
        setVariationalRefinementGamma(val) -> None
        .   @copybrief getVariationalRefinementGamma @see getVariationalRefinementGamma
        """
        pass

    def setVariationalRefinementIterations(self, val): # real signature unknown; restored from __doc__
        """
        setVariationalRefinementIterations(val) -> None
        .   @copybrief getGradientDescentIterations @see getGradientDescentIterations
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


