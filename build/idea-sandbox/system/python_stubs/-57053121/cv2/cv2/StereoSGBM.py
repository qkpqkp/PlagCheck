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


class StereoSGBM(__cv2.StereoMatcher):
    # no doc
    def create(self, minDisparity=None, numDisparities=None, blockSize=None, P1=None, P2=None, disp12MaxDiff=None, preFilterCap=None, uniquenessRatio=None, speckleWindowSize=None, speckleRange=None, mode=None): # real signature unknown; restored from __doc__
        """
        create([, minDisparity[, numDisparities[, blockSize[, P1[, P2[, disp12MaxDiff[, preFilterCap[, uniquenessRatio[, speckleWindowSize[, speckleRange[, mode]]]]]]]]]]]) -> retval
        .   @brief Creates StereoSGBM object
        .   
        .       @param minDisparity Minimum possible disparity value. Normally, it is zero but sometimes
        .       rectification algorithms can shift images, so this parameter needs to be adjusted accordingly.
        .       @param numDisparities Maximum disparity minus minimum disparity. The value is always greater than
        .       zero. In the current implementation, this parameter must be divisible by 16.
        .       @param blockSize Matched block size. It must be an odd number \>=1 . Normally, it should be
        .       somewhere in the 3..11 range.
        .       @param P1 The first parameter controlling the disparity smoothness. See below.
        .       @param P2 The second parameter controlling the disparity smoothness. The larger the values are,
        .       the smoother the disparity is. P1 is the penalty on the disparity change by plus or minus 1
        .       between neighbor pixels. P2 is the penalty on the disparity change by more than 1 between neighbor
        .       pixels. The algorithm requires P2 \> P1 . See stereo_match.cpp sample where some reasonably good
        .       P1 and P2 values are shown (like 8\*number_of_image_channels\*SADWindowSize\*SADWindowSize and
        .       32\*number_of_image_channels\*SADWindowSize\*SADWindowSize , respectively).
        .       @param disp12MaxDiff Maximum allowed difference (in integer pixel units) in the left-right
        .       disparity check. Set it to a non-positive value to disable the check.
        .       @param preFilterCap Truncation value for the prefiltered image pixels. The algorithm first
        .       computes x-derivative at each pixel and clips its value by [-preFilterCap, preFilterCap] interval.
        .       The result values are passed to the Birchfield-Tomasi pixel cost function.
        .       @param uniquenessRatio Margin in percentage by which the best (minimum) computed cost function
        .       value should "win" the second best value to consider the found match correct. Normally, a value
        .       within the 5-15 range is good enough.
        .       @param speckleWindowSize Maximum size of smooth disparity regions to consider their noise speckles
        .       and invalidate. Set it to 0 to disable speckle filtering. Otherwise, set it somewhere in the
        .       50-200 range.
        .       @param speckleRange Maximum disparity variation within each connected component. If you do speckle
        .       filtering, set the parameter to a positive value, it will be implicitly multiplied by 16.
        .       Normally, 1 or 2 is good enough.
        .       @param mode Set it to StereoSGBM::MODE_HH to run the full-scale two-pass dynamic programming
        .       algorithm. It will consume O(W\*H\*numDisparities) bytes, which is large for 640x480 stereo and
        .       huge for HD-size pictures. By default, it is set to false .
        .   
        .       The first constructor initializes StereoSGBM with all the default parameters. So, you only have to
        .       set StereoSGBM::numDisparities at minimum. The second constructor enables you to set each parameter
        .       to a custom value.
        """
        pass

    def getMode(self): # real signature unknown; restored from __doc__
        """
        getMode() -> retval
        .
        """
        pass

    def getP1(self): # real signature unknown; restored from __doc__
        """
        getP1() -> retval
        .
        """
        pass

    def getP2(self): # real signature unknown; restored from __doc__
        """
        getP2() -> retval
        .
        """
        pass

    def getPreFilterCap(self): # real signature unknown; restored from __doc__
        """
        getPreFilterCap() -> retval
        .
        """
        pass

    def getUniquenessRatio(self): # real signature unknown; restored from __doc__
        """
        getUniquenessRatio() -> retval
        .
        """
        pass

    def setMode(self, mode): # real signature unknown; restored from __doc__
        """
        setMode(mode) -> None
        .
        """
        pass

    def setP1(self, P1): # real signature unknown; restored from __doc__
        """
        setP1(P1) -> None
        .
        """
        pass

    def setP2(self, P2): # real signature unknown; restored from __doc__
        """
        setP2(P2) -> None
        .
        """
        pass

    def setPreFilterCap(self, preFilterCap): # real signature unknown; restored from __doc__
        """
        setPreFilterCap(preFilterCap) -> None
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


