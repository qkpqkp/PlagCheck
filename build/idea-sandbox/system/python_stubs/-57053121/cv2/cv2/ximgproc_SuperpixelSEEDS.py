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


class ximgproc_SuperpixelSEEDS(__cv2.Algorithm):
    # no doc
    def getLabelContourMask(self, image=None, thick_line=None): # real signature unknown; restored from __doc__
        """
        getLabelContourMask([, image[, thick_line]]) -> image
        .   @brief Returns the mask of the superpixel segmentation stored in SuperpixelSEEDS object.
        .   
        .       @param image Return: CV_8UC1 image mask where -1 indicates that the pixel is a superpixel border,
        .       and 0 otherwise.
        .   
        .       @param thick_line If false, the border is only one pixel wide, otherwise all pixels at the border
        .       are masked.
        .   
        .       The function return the boundaries of the superpixel segmentation.
        .   
        .       @note
        .          -   (Python) A demo on how to generate superpixels in images from the webcam can be found at
        .               opencv_source_code/samples/python2/seeds.py
        .           -   (cpp) A demo on how to generate superpixels in images from the webcam can be found at
        .               opencv_source_code/modules/ximgproc/samples/seeds.cpp. By adding a file image as a command
        .               line argument, the static image will be used instead of the webcam.
        .           -   It will show a window with the video from the webcam with the superpixel boundaries marked
        .               in red (see below). Use Space to switch between different output modes. At the top of the
        .               window there are 4 sliders, from which the user can change on-the-fly the number of
        .               superpixels, the number of block levels, the strength of the boundary prior term to modify
        .               the shape, and the number of iterations at pixel level. This is useful to play with the
        .               parameters and set them to the user convenience. In the console the frame-rate of the
        .               algorithm is indicated.
        .   
        .       ![image](pics/superpixels_demo.png)
        """
        pass

    def getLabels(self, labels_out=None): # real signature unknown; restored from __doc__
        """
        getLabels([, labels_out]) -> labels_out
        .   @brief Returns the segmentation labeling of the image.
        .   
        .       Each label represents a superpixel, and each pixel is assigned to one superpixel label.
        .   
        .       @param labels_out Return: A CV_32UC1 integer array containing the labels of the superpixel
        .       segmentation. The labels are in the range [0, getNumberOfSuperpixels()].
        .   
        .       The function returns an image with ssthe labels of the superpixel segmentation. The labels are in
        .       the range [0, getNumberOfSuperpixels()].
        """
        pass

    def getNumberOfSuperpixels(self): # real signature unknown; restored from __doc__
        """
        getNumberOfSuperpixels() -> retval
        .   @brief Calculates the superpixel segmentation on a given image stored in SuperpixelSEEDS object.
        .   
        .       The function computes the superpixels segmentation of an image with the parameters initialized
        .       with the function createSuperpixelSEEDS().
        """
        pass

    def iterate(self, img, num_iterations=None): # real signature unknown; restored from __doc__
        """
        iterate(img[, num_iterations]) -> None
        .   @brief Calculates the superpixel segmentation on a given image with the initialized
        .       parameters in the SuperpixelSEEDS object.
        .   
        .       This function can be called again for other images without the need of initializing the
        .       algorithm with createSuperpixelSEEDS(). This save the computational cost of allocating memory
        .       for all the structures of the algorithm.
        .   
        .       @param img Input image. Supported formats: CV_8U, CV_16U, CV_32F. Image size & number of
        .       channels must match with the initialized image size & channels with the function
        .       createSuperpixelSEEDS(). It should be in HSV or Lab color space. Lab is a bit better, but also
        .       slower.
        .   
        .       @param num_iterations Number of pixel level iterations. Higher number improves the result.
        .   
        .       The function computes the superpixels segmentation of an image with the parameters initialized
        .       with the function createSuperpixelSEEDS(). The algorithms starts from a grid of superpixels and
        .       then refines the boundaries by proposing updates of blocks of pixels that lie at the boundaries
        .       from large to smaller size, finalizing with proposing pixel updates. An illustrative example
        .       can be seen below.
        .   
        .       ![image](pics/superpixels_blocks2.png)
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


