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


class LineSegmentDetector(__cv2.Algorithm):
    # no doc
    def compareSegments(self, size, lines1, lines2, _image=None): # real signature unknown; restored from __doc__
        """
        compareSegments(size, lines1, lines2[, _image]) -> retval, _image
        .   @brief Draws two groups of lines in blue and red, counting the non overlapping (mismatching) pixels.
        .   
        .       @param size The size of the image, where lines1 and lines2 were found.
        .       @param lines1 The first group of lines that needs to be drawn. It is visualized in blue color.
        .       @param lines2 The second group of lines. They visualized in red color.
        .       @param _image Optional image, where the lines will be drawn. The image should be color(3-channel)
        .       in order for lines1 and lines2 to be drawn in the above mentioned colors.
        """
        pass

    def detect(self, _image, _lines=None, width=None, prec=None, nfa=None): # real signature unknown; restored from __doc__
        """
        detect(_image[, _lines[, width[, prec[, nfa]]]]) -> _lines, width, prec, nfa
        .   @brief Finds lines in the input image.
        .   
        .       This is the output of the default parameters of the algorithm on the above shown image.
        .   
        .       ![image](pics/building_lsd.png)
        .   
        .       @param _image A grayscale (CV_8UC1) input image. If only a roi needs to be selected, use:
        .       `lsd_ptr-\>detect(image(roi), lines, ...); lines += Scalar(roi.x, roi.y, roi.x, roi.y);`
        .       @param _lines A vector of Vec4i or Vec4f elements specifying the beginning and ending point of a line. Where
        .       Vec4i/Vec4f is (x1, y1, x2, y2), point 1 is the start, point 2 - end. Returned lines are strictly
        .       oriented depending on the gradient.
        .       @param width Vector of widths of the regions, where the lines are found. E.g. Width of line.
        .       @param prec Vector of precisions with which the lines are found.
        .       @param nfa Vector containing number of false alarms in the line region, with precision of 10%. The
        .       bigger the value, logarithmically better the detection.
        .       - -1 corresponds to 10 mean false alarms
        .       - 0 corresponds to 1 mean false alarm
        .       - 1 corresponds to 0.1 mean false alarms
        .       This vector will be calculated only when the objects type is #LSD_REFINE_ADV.
        """
        pass

    def drawSegments(self, _image, lines): # real signature unknown; restored from __doc__
        """
        drawSegments(_image, lines) -> _image
        .   @brief Draws the line segments on a given image.
        .       @param _image The image, where the lines will be drawn. Should be bigger or equal to the image,
        .       where the lines were found.
        .       @param lines A vector of the lines that needed to be drawn.
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


