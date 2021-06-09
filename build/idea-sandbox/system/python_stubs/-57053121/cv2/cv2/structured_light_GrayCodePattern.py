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


class structured_light_GrayCodePattern(__cv2.structured_light_StructuredLightPattern):
    # no doc
    def create(self, width, height): # real signature unknown; restored from __doc__
        """
        create(width, height) -> retval
        .   @brief Constructor
        .      @param parameters GrayCodePattern parameters GrayCodePattern::Params: the width and the height of the projector.
        """
        pass

    def getImagesForShadowMasks(self, blackImage, whiteImage): # real signature unknown; restored from __doc__
        """
        getImagesForShadowMasks(blackImage, whiteImage) -> blackImage, whiteImage
        .   @brief Generates the all-black and all-white images needed for shadowMasks computation.
        .      *
        .      *  To identify shadow regions, the regions of two images where the pixels are not lit by projector's light and thus where there is not coded information,
        .      *  the 3DUNDERWORLD algorithm computes a shadow mask for the two cameras views, starting from a white and a black images captured by each camera.
        .      *  This method generates these two additional images to project.
        .      *
        .      *  @param blackImage The generated all-black CV_8U image, at projector's resolution.
        .      *  @param whiteImage The generated all-white CV_8U image, at projector's resolution.
        """
        pass

    def getNumberOfPatternImages(self): # real signature unknown; restored from __doc__
        """
        getNumberOfPatternImages() -> retval
        .   @brief Get the number of pattern images needed for the graycode pattern.
        .      *
        .      * @return The number of pattern images needed for the graycode pattern.
        .      *
        """
        pass

    def getProjPixel(self, patternImages, x, y): # real signature unknown; restored from __doc__
        """
        getProjPixel(patternImages, x, y) -> retval, projPix
        .   @brief For a (x,y) pixel of a camera returns the corresponding projector pixel.
        .      *
        .      *  The function decodes each pixel in the pattern images acquired by a camera into their corresponding decimal numbers representing the projector's column and row,
        .      *  providing a mapping between camera's and projector's pixel.
        .      *
        .      *  @param patternImages The pattern images acquired by the camera, stored in a grayscale vector < Mat >.
        .      *  @param x x coordinate of the image pixel.
        .      *  @param y y coordinate of the image pixel.
        .      *  @param projPix Projector's pixel corresponding to the camera's pixel: projPix.x and projPix.y are the image coordinates of the projector's pixel corresponding to the pixel being decoded in a camera.
        """
        pass

    def setBlackThreshold(self, value): # real signature unknown; restored from __doc__
        """
        setBlackThreshold(value) -> None
        .   @brief Sets the value for black threshold, needed for decoding (shadowsmasks computation).
        .      *
        .      *  Black threshold is a number between 0-255 that represents the minimum brightness difference required for valid pixels, between the fully illuminated (white) and the not illuminated images (black); used in computeShadowMasks method.
        .      *
        .      *  @param value The desired black threshold value.
        .      *
        """
        pass

    def setWhiteThreshold(self, value): # real signature unknown; restored from __doc__
        """
        setWhiteThreshold(value) -> None
        .   @brief Sets the value for white threshold, needed for decoding.
        .      *
        .      *  White threshold is a number between 0-255 that represents the minimum brightness difference required for valid pixels, between the graycode pattern and its inverse images; used in getProjPixel method.
        .      *
        .      *  @param value The desired white threshold value.
        .      *
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


