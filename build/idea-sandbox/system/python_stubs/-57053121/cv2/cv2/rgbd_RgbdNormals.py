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


class rgbd_RgbdNormals(__cv2.Algorithm):
    # no doc
    def apply(self, points, normals=None): # real signature unknown; restored from __doc__
        """
        apply(points[, normals]) -> normals
        .   Given a set of 3d points in a depth image, compute the normals at each point.
        .        * @param points a rows x cols x 3 matrix of CV_32F/CV64F or a rows x cols x 1 CV_U16S
        .        * @param normals a rows x cols x 3 matrix
        """
        pass

    def create(self, rows, cols, depth, K, window_size=None, method=None): # real signature unknown; restored from __doc__
        """
        create(rows, cols, depth, K[, window_size[, method]]) -> retval
        .   Constructor
        .        * @param rows the number of rows of the depth image normals will be computed on
        .        * @param cols the number of cols of the depth image normals will be computed on
        .        * @param depth the depth of the normals (only CV_32F or CV_64F)
        .        * @param K the calibration matrix to use
        .        * @param window_size the window size to compute the normals: can only be 1,3,5 or 7
        .        * @param method one of the methods to use: RGBD_NORMALS_METHOD_SRI, RGBD_NORMALS_METHOD_FALS
        """
        pass

    def getCols(self): # real signature unknown; restored from __doc__
        """
        getCols() -> retval
        .
        """
        pass

    def getDepth(self): # real signature unknown; restored from __doc__
        """
        getDepth() -> retval
        .
        """
        pass

    def getK(self): # real signature unknown; restored from __doc__
        """
        getK() -> retval
        .
        """
        pass

    def getMethod(self): # real signature unknown; restored from __doc__
        """
        getMethod() -> retval
        .
        """
        pass

    def getRows(self): # real signature unknown; restored from __doc__
        """
        getRows() -> retval
        .
        """
        pass

    def getWindowSize(self): # real signature unknown; restored from __doc__
        """
        getWindowSize() -> retval
        .
        """
        pass

    def initialize(self): # real signature unknown; restored from __doc__
        """
        initialize() -> None
        .   Initializes some data that is cached for later computation
        .        * If that function is not called, it will be called the first time normals are computed
        """
        pass

    def setCols(self, val): # real signature unknown; restored from __doc__
        """
        setCols(val) -> None
        .
        """
        pass

    def setDepth(self, val): # real signature unknown; restored from __doc__
        """
        setDepth(val) -> None
        .
        """
        pass

    def setK(self, val): # real signature unknown; restored from __doc__
        """
        setK(val) -> None
        .
        """
        pass

    def setMethod(self, val): # real signature unknown; restored from __doc__
        """
        setMethod(val) -> None
        .
        """
        pass

    def setRows(self, val): # real signature unknown; restored from __doc__
        """
        setRows(val) -> None
        .
        """
        pass

    def setWindowSize(self, val): # real signature unknown; restored from __doc__
        """
        setWindowSize(val) -> None
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


