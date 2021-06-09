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


class text_OCRTesseract(__cv2.text_BaseOCR):
    # no doc
    def create(self, datapath=None, language=None, char_whitelist=None, oem=None, psmode=None): # real signature unknown; restored from __doc__
        """
        create([, datapath[, language[, char_whitelist[, oem[, psmode]]]]]) -> retval
        .   @brief Creates an instance of the OCRTesseract class. Initializes Tesseract.
        .   
        .       @param datapath the name of the parent directory of tessdata ended with "/", or NULL to use the
        .       system's default directory.
        .       @param language an ISO 639-3 code or NULL will default to "eng".
        .       @param char_whitelist specifies the list of characters used for recognition. NULL defaults to
        .       "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".
        .       @param oem tesseract-ocr offers different OCR Engine Modes (OEM), by default
        .       tesseract::OEM_DEFAULT is used. See the tesseract-ocr API documentation for other possible
        .       values.
        .       @param psmode tesseract-ocr offers different Page Segmentation Modes (PSM) tesseract::PSM_AUTO
        .       (fully automatic layout analysis) is used. See the tesseract-ocr API documentation for other
        .       possible values.
        """
        pass

    def run(self, image, min_confidence, component_level=None): # real signature unknown; restored from __doc__
        """
        run(image, min_confidence[, component_level]) -> retval
        .   @brief Recognize text using the tesseract-ocr API.
        .   
        .       Takes image on input and returns recognized text in the output_text parameter. Optionally
        .       provides also the Rects for individual text elements found (e.g. words), and the list of those
        .       text elements with their confidence values.
        .   
        .       @param image Input image CV_8UC1 or CV_8UC3
        .       @param output_text Output text of the tesseract-ocr.
        .       @param component_rects If provided the method will output a list of Rects for the individual
        .       text elements found (e.g. words or text lines).
        .       @param component_texts If provided the method will output a list of text strings for the
        .       recognition of individual text elements found (e.g. words or text lines).
        .       @param component_confidences If provided the method will output a list of confidence values
        .       for the recognition of individual text elements found (e.g. words or text lines).
        .       @param component_level OCR_LEVEL_WORD (by default), or OCR_LEVEL_TEXTLINE.
        
        
        
        run(image, mask, min_confidence[, component_level]) -> retval
        .
        """
        pass

    def setWhiteList(self, char_whitelist): # real signature unknown; restored from __doc__
        """
        setWhiteList(char_whitelist) -> None
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

