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


class bioinspired_TransientAreasSegmentationModule(__cv2.Algorithm):
    # no doc
    def clearAllBuffers(self): # real signature unknown; restored from __doc__
        """
        clearAllBuffers() -> None
        .   @brief cleans all the buffers of the instance
        """
        pass

    def create(self, inputSize): # real signature unknown; restored from __doc__
        """
        create(inputSize) -> retval
        .   @brief allocator
        .       @param inputSize : size of the images input to segment (output will be the same size)
        """
        pass

    def getSegmentationPicture(self, transientAreas=None): # real signature unknown; restored from __doc__
        """
        getSegmentationPicture([, transientAreas]) -> transientAreas
        .   @brief access function
        .       return the last segmentation result: a boolean picture which is resampled between 0 and 255 for a display purpose
        """
        pass

    def getSize(self): # real signature unknown; restored from __doc__
        """
        getSize() -> retval
        .   @brief return the sze of the manage input and output images
        """
        pass

    def printSetup(self): # real signature unknown; restored from __doc__
        """
        printSetup() -> retval
        .   @brief parameters setup display method
        .       @return a string which contains formatted parameters information
        """
        pass

    def run(self, inputToSegment, channelIndex=None): # real signature unknown; restored from __doc__
        """
        run(inputToSegment[, channelIndex]) -> None
        .   @brief main processing method, get result using methods getSegmentationPicture()
        .       @param inputToSegment : the image to process, it must match the instance buffer size !
        .       @param channelIndex : the channel to process in case of multichannel images
        """
        pass

    def setup(self, segmentationParameterFile=None, applyDefaultSetupOnFailure=None): # real signature unknown; restored from __doc__
        """
        setup([, segmentationParameterFile[, applyDefaultSetupOnFailure]]) -> None
        .   @brief try to open an XML segmentation parameters file to adjust current segmentation instance setup
        .   
        .       - if the xml file does not exist, then default setup is applied
        .       - warning, Exceptions are thrown if read XML file is not valid
        .       @param segmentationParameterFile : the parameters filename
        .       @param applyDefaultSetupOnFailure : set to true if an error must be thrown on error
        """
        pass

    def write(self, fs): # real signature unknown; restored from __doc__
        """
        write(fs) -> None
        .   @brief write xml/yml formated parameters information
        .       @param fs : the filename of the xml file that will be open and writen with formatted parameters information
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


