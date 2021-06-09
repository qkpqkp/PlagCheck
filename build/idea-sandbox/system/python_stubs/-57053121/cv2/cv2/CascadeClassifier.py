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


from .object import object

class CascadeClassifier(object):
    # no doc
    def convert(self, oldcascade, newcascade): # real signature unknown; restored from __doc__
        """
        convert(oldcascade, newcascade) -> retval
        .
        """
        pass

    def detectMultiScale(self, image, scaleFactor=None, minNeighbors=None, flags=None, minSize=None, maxSize=None): # real signature unknown; restored from __doc__
        """
        detectMultiScale(image[, scaleFactor[, minNeighbors[, flags[, minSize[, maxSize]]]]]) -> objects
        .   @brief Detects objects of different sizes in the input image. The detected objects are returned as a list
        .       of rectangles.
        .   
        .       @param image Matrix of the type CV_8U containing an image where objects are detected.
        .       @param objects Vector of rectangles where each rectangle contains the detected object, the
        .       rectangles may be partially outside the original image.
        .       @param scaleFactor Parameter specifying how much the image size is reduced at each image scale.
        .       @param minNeighbors Parameter specifying how many neighbors each candidate rectangle should have
        .       to retain it.
        .       @param flags Parameter with the same meaning for an old cascade as in the function
        .       cvHaarDetectObjects. It is not used for a new cascade.
        .       @param minSize Minimum possible object size. Objects smaller than that are ignored.
        .       @param maxSize Maximum possible object size. Objects larger than that are ignored. If `maxSize == minSize` model is evaluated on single scale.
        .   
        .       The function is parallelized with the TBB library.
        .   
        .       @note
        .          -   (Python) A face detection example using cascade classifiers can be found at
        .               opencv_source_code/samples/python/facedetect.py
        """
        pass

    def detectMultiScale2(self, image, scaleFactor=None, minNeighbors=None, flags=None, minSize=None, maxSize=None): # real signature unknown; restored from __doc__
        """
        detectMultiScale2(image[, scaleFactor[, minNeighbors[, flags[, minSize[, maxSize]]]]]) -> objects, numDetections
        .   @overload
        .       @param image Matrix of the type CV_8U containing an image where objects are detected.
        .       @param objects Vector of rectangles where each rectangle contains the detected object, the
        .       rectangles may be partially outside the original image.
        .       @param numDetections Vector of detection numbers for the corresponding objects. An object's number
        .       of detections is the number of neighboring positively classified rectangles that were joined
        .       together to form the object.
        .       @param scaleFactor Parameter specifying how much the image size is reduced at each image scale.
        .       @param minNeighbors Parameter specifying how many neighbors each candidate rectangle should have
        .       to retain it.
        .       @param flags Parameter with the same meaning for an old cascade as in the function
        .       cvHaarDetectObjects. It is not used for a new cascade.
        .       @param minSize Minimum possible object size. Objects smaller than that are ignored.
        .       @param maxSize Maximum possible object size. Objects larger than that are ignored. If `maxSize == minSize` model is evaluated on single scale.
        """
        pass

    def detectMultiScale3(self, image, scaleFactor=None, minNeighbors=None, flags=None, minSize=None, maxSize=None, outputRejectLevels=None): # real signature unknown; restored from __doc__
        """
        detectMultiScale3(image[, scaleFactor[, minNeighbors[, flags[, minSize[, maxSize[, outputRejectLevels]]]]]]) -> objects, rejectLevels, levelWeights
        .   @overload
        .       This function allows you to retrieve the final stage decision certainty of classification.
        .       For this, one needs to set `outputRejectLevels` on true and provide the `rejectLevels` and `levelWeights` parameter.
        .       For each resulting detection, `levelWeights` will then contain the certainty of classification at the final stage.
        .       This value can then be used to separate strong from weaker classifications.
        .   
        .       A code sample on how to use it efficiently can be found below:
        .       @code
        .       Mat img;
        .       vector<double> weights;
        .       vector<int> levels;
        .       vector<Rect> detections;
        .       CascadeClassifier model("/path/to/your/model.xml");
        .       model.detectMultiScale(img, detections, levels, weights, 1.1, 3, 0, Size(), Size(), true);
        .       cerr << "Detection " << detections[0] << " with weight " << weights[0] << endl;
        .       @endcode
        """
        pass

    def empty(self): # real signature unknown; restored from __doc__
        """
        empty() -> retval
        .   @brief Checks whether the classifier has been loaded.
        """
        pass

    def getFeatureType(self): # real signature unknown; restored from __doc__
        """
        getFeatureType() -> retval
        .
        """
        pass

    def getOriginalWindowSize(self): # real signature unknown; restored from __doc__
        """
        getOriginalWindowSize() -> retval
        .
        """
        pass

    def isOldFormatCascade(self): # real signature unknown; restored from __doc__
        """
        isOldFormatCascade() -> retval
        .
        """
        pass

    def load(self, filename): # real signature unknown; restored from __doc__
        """
        load(filename) -> retval
        .   @brief Loads a classifier from a file.
        .   
        .       @param filename Name of the file from which the classifier is loaded. The file may contain an old
        .       HAAR classifier trained by the haartraining application or a new cascade classifier trained by the
        .       traincascade application.
        """
        pass

    def read(self, node): # real signature unknown; restored from __doc__
        """
        read(node) -> retval
        .   @brief Reads a classifier from a FileStorage node.
        .   
        .       @note The file may contain a new cascade classifier (trained traincascade application) only.
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


