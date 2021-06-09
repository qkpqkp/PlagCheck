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


class hfs_HfsSegment(__cv2.Algorithm):
    # no doc
    def create(self, height, width, segEgbThresholdI=None, minRegionSizeI=None, segEgbThresholdII=None, minRegionSizeII=None, spatialWeight=None, slicSpixelSize=None, numSlicIter=None): # real signature unknown; restored from __doc__
        """
        create(height, width[, segEgbThresholdI[, minRegionSizeI[, segEgbThresholdII[, minRegionSizeII[, spatialWeight[, slicSpixelSize[, numSlicIter]]]]]]]) -> retval
        .   @brief: create a hfs object
        .   * @param height: the height of the input image
        .   * @param width: the width of the input image
        .   * @param segEgbThresholdI: parameter segEgbThresholdI
        .   * @param minRegionSizeI: parameter minRegionSizeI
        .   * @param segEgbThresholdII: parameter segEgbThresholdII
        .   * @param minRegionSizeII: parameter minRegionSizeII
        .   * @param spatialWeight: parameter spatialWeight
        .   * @param slicSpixelSize: parameter slicSpixelSize
        .   * @param numSlicIter: parameter numSlicIter
        """
        pass

    def getMinRegionSizeI(self): # real signature unknown; restored from __doc__
        """
        getMinRegionSizeI() -> retval
        .
        """
        pass

    def getMinRegionSizeII(self): # real signature unknown; restored from __doc__
        """
        getMinRegionSizeII() -> retval
        .
        """
        pass

    def getNumSlicIter(self): # real signature unknown; restored from __doc__
        """
        getNumSlicIter() -> retval
        .
        """
        pass

    def getSegEgbThresholdI(self): # real signature unknown; restored from __doc__
        """
        getSegEgbThresholdI() -> retval
        .
        """
        pass

    def getSegEgbThresholdII(self): # real signature unknown; restored from __doc__
        """
        getSegEgbThresholdII() -> retval
        .
        """
        pass

    def getSlicSpixelSize(self): # real signature unknown; restored from __doc__
        """
        getSlicSpixelSize() -> retval
        .
        """
        pass

    def getSpatialWeight(self): # real signature unknown; restored from __doc__
        """
        getSpatialWeight() -> retval
        .
        """
        pass

    def performSegmentCpu(self, src, ifDraw=None): # real signature unknown; restored from __doc__
        """
        performSegmentCpu(src[, ifDraw]) -> retval
        .   @brief do segmentation with cpu
        .   * This method is only implemented for reference.
        .   * It is highly NOT recommanded to use it.
        """
        pass

    def performSegmentGpu(self, src, ifDraw=None): # real signature unknown; restored from __doc__
        """
        performSegmentGpu(src[, ifDraw]) -> retval
        .   @brief do segmentation gpu
        .   * @param src: the input image
        .   * @param ifDraw: if draw the image in the returned Mat. if this parameter is false,
        .   * then the content of the returned Mat is a matrix of index, describing the region
        .   * each pixel belongs to. And it's data type is CV_16U. If this parameter is true,
        .   * then the returned Mat is a segmented picture, and color of each region is the
        .   * average color of all pixels in that region. And it's data type is the same as
        .   * the input image
        """
        pass

    def setMinRegionSizeI(self, n): # real signature unknown; restored from __doc__
        """
        setMinRegionSizeI(n) -> None
        .   @brief: set and get the parameter minRegionSizeI.
        .   * This parameter is used in the second stage
        .   * mentioned above. After the EGB segmentation, regions that have fewer
        .   * pixels then this parameter will be merged into it's adjacent region.
        """
        pass

    def setMinRegionSizeII(self, n): # real signature unknown; restored from __doc__
        """
        setMinRegionSizeII(n) -> None
        .   @brief: set and get the parameter minRegionSizeII.
        .   * This parameter is used in the third stage
        .   * mentioned above. It serves the same purpose as minRegionSizeI
        """
        pass

    def setNumSlicIter(self, n): # real signature unknown; restored from __doc__
        """
        setNumSlicIter(n) -> None
        .   @brief: set and get the parameter numSlicIter.
        .   * This parameter is used in the first stage. It
        .   * describes how many iteration to perform when executing SLIC.
        """
        pass

    def setSegEgbThresholdI(self, c): # real signature unknown; restored from __doc__
        """
        setSegEgbThresholdI(c) -> None
        .   @brief: set and get the parameter segEgbThresholdI.
        .   * This parameter is used in the second stage mentioned above.
        .   * It is a constant used to threshold weights of the edge when merging
        .   * adjacent nodes when applying EGB algorithm. The segmentation result
        .   * tends to have more regions remained if this value is large and vice versa.
        """
        pass

    def setSegEgbThresholdII(self, c): # real signature unknown; restored from __doc__
        """
        setSegEgbThresholdII(c) -> None
        .   @brief: set and get the parameter segEgbThresholdII.
        .   * This parameter is used in the third stage
        .   * mentioned above. It serves the same purpose as segEgbThresholdI.
        .   * The segmentation result tends to have more regions remained if
        .   * this value is large and vice versa.
        """
        pass

    def setSlicSpixelSize(self, n): # real signature unknown; restored from __doc__
        """
        setSlicSpixelSize(n) -> None
        .   @brief: set and get the parameter slicSpixelSize.
        .   * This parameter is used in the first stage mentioned
        .   * above(the SLIC stage). It describes the size of each
        .   * superpixel when initializing SLIC. Every superpixel
        .   * approximately has \f$slicSpixelSize \times slicSpixelSize\f$
        .   * pixels in the begining.
        """
        pass

    def setSpatialWeight(self, w): # real signature unknown; restored from __doc__
        """
        setSpatialWeight(w) -> None
        .   @brief: set and get the parameter spatialWeight.
        .   * This parameter is used in the first stage
        .   * mentioned above(the SLIC stage). It describes how important is the role
        .   * of position when calculating the distance between each pixel and it's
        .   * center. The exact formula to calculate the distance is
        .   * \f$colorDistance + spatialWeight \times spatialDistance\f$.
        .   * The segmentation result tends to have more local consistency
        .   * if this value is larger.
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


