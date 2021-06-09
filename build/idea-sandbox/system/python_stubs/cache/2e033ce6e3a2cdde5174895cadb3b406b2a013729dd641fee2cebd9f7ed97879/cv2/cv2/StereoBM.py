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


class StereoBM(__cv2.StereoMatcher):
    # no doc
    def create(self, numDisparities=None, blockSize=None): # real signature unknown; restored from __doc__
        """
        create([, numDisparities[, blockSize]]) -> retval
        .   @brief Creates StereoBM object
        .   
        .       @param numDisparities the disparity search range. For each pixel algorithm will find the best
        .       disparity from 0 (default minimum disparity) to numDisparities. The search range can then be
        .       shifted by changing the minimum disparity.
        .       @param blockSize the linear size of the blocks compared by the algorithm. The size should be odd
        .       (as the block is centered at the current pixel). Larger block size implies smoother, though less
        .       accurate disparity map. Smaller block size gives more detailed disparity map, but there is higher
        .       chance for algorithm to find a wrong correspondence.
        .   
        .       The function create StereoBM object. You can then call StereoBM::compute() to compute disparity for
        .       a specific stereo pair.
        """
        pass

    def getPreFilterCap(self): # real signature unknown; restored from __doc__
        """
        getPreFilterCap() -> retval
        .
        """
        pass

    def getPreFilterSize(self): # real signature unknown; restored from __doc__
        """
        getPreFilterSize() -> retval
        .
        """
        pass

    def getPreFilterType(self): # real signature unknown; restored from __doc__
        """
        getPreFilterType() -> retval
        .
        """
        pass

    def getROI1(self): # real signature unknown; restored from __doc__
        """
        getROI1() -> retval
        .
        """
        pass

    def getROI2(self): # real signature unknown; restored from __doc__
        """
        getROI2() -> retval
        .
        """
        pass

    def getSmallerBlockSize(self): # real signature unknown; restored from __doc__
        """
        getSmallerBlockSize() -> retval
        .
        """
        pass

    def getTextureThreshold(self): # real signature unknown; restored from __doc__
        """
        getTextureThreshold() -> retval
        .
        """
        pass

    def getUniquenessRatio(self): # real signature unknown; restored from __doc__
        """
        getUniquenessRatio() -> retval
        .
        """
        pass

    def setPreFilterCap(self, preFilterCap): # real signature unknown; restored from __doc__
        """
        setPreFilterCap(preFilterCap) -> None
        .
        """
        pass

    def setPreFilterSize(self, preFilterSize): # real signature unknown; restored from __doc__
        """
        setPreFilterSize(preFilterSize) -> None
        .
        """
        pass

    def setPreFilterType(self, preFilterType): # real signature unknown; restored from __doc__
        """
        setPreFilterType(preFilterType) -> None
        .
        """
        pass

    def setROI1(self, roi1): # real signature unknown; restored from __doc__
        """
        setROI1(roi1) -> None
        .
        """
        pass

    def setROI2(self, roi2): # real signature unknown; restored from __doc__
        """
        setROI2(roi2) -> None
        .
        """
        pass

    def setSmallerBlockSize(self, blockSize): # real signature unknown; restored from __doc__
        """
        setSmallerBlockSize(blockSize) -> None
        .
        """
        pass

    def setTextureThreshold(self, textureThreshold): # real signature unknown; restored from __doc__
        """
        setTextureThreshold(textureThreshold) -> None
        .
        """
        pass

    def setUniquenessRatio(self, uniquenessRatio): # real signature unknown; restored from __doc__
        """
        setUniquenessRatio(uniquenessRatio) -> None
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


