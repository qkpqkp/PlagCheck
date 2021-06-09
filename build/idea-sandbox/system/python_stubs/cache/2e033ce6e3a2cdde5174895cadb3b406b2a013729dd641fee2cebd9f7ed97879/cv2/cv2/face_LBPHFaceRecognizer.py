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


class face_LBPHFaceRecognizer(__cv2.face_FaceRecognizer):
    # no doc
    def create(self, radius=None, neighbors=None, grid_x=None, grid_y=None, threshold=None): # real signature unknown; restored from __doc__
        """
        create([, radius[, neighbors[, grid_x[, grid_y[, threshold]]]]]) -> retval
        .   @param radius The radius used for building the Circular Local Binary Pattern. The greater the
        .       radius, the smoother the image but more spatial information you can get.
        .       @param neighbors The number of sample points to build a Circular Local Binary Pattern from. An
        .       appropriate value is to use `8` sample points. Keep in mind: the more sample points you include,
        .       the higher the computational cost.
        .       @param grid_x The number of cells in the horizontal direction, 8 is a common value used in
        .       publications. The more cells, the finer the grid, the higher the dimensionality of the resulting
        .       feature vector.
        .       @param grid_y The number of cells in the vertical direction, 8 is a common value used in
        .       publications. The more cells, the finer the grid, the higher the dimensionality of the resulting
        .       feature vector.
        .       @param threshold The threshold applied in the prediction. If the distance to the nearest neighbor
        .       is larger than the threshold, this method returns -1.
        .   
        .       ### Notes:
        .   
        .       -   The Circular Local Binary Patterns (used in training and prediction) expect the data given as
        .           grayscale images, use cvtColor to convert between the color spaces.
        .       -   This model supports updating.
        .   
        .       ### Model internal data:
        .   
        .       -   radius see LBPHFaceRecognizer::create.
        .       -   neighbors see LBPHFaceRecognizer::create.
        .       -   grid_x see LLBPHFaceRecognizer::create.
        .       -   grid_y see LBPHFaceRecognizer::create.
        .       -   threshold see LBPHFaceRecognizer::create.
        .       -   histograms Local Binary Patterns Histograms calculated from the given training data (empty if
        .           none was given).
        .       -   labels Labels corresponding to the calculated Local Binary Patterns Histograms.
        """
        pass

    def getGridX(self): # real signature unknown; restored from __doc__
        """
        getGridX() -> retval
        .   @see setGridX
        """
        pass

    def getGridY(self): # real signature unknown; restored from __doc__
        """
        getGridY() -> retval
        .   @see setGridY
        """
        pass

    def getHistograms(self): # real signature unknown; restored from __doc__
        """
        getHistograms() -> retval
        .
        """
        pass

    def getLabels(self): # real signature unknown; restored from __doc__
        """
        getLabels() -> retval
        .
        """
        pass

    def getNeighbors(self): # real signature unknown; restored from __doc__
        """
        getNeighbors() -> retval
        .   @see setNeighbors
        """
        pass

    def getRadius(self): # real signature unknown; restored from __doc__
        """
        getRadius() -> retval
        .   @see setRadius
        """
        pass

    def getThreshold(self): # real signature unknown; restored from __doc__
        """
        getThreshold() -> retval
        .   @see setThreshold
        """
        pass

    def setGridX(self, val): # real signature unknown; restored from __doc__
        """
        setGridX(val) -> None
        .   @copybrief getGridX @see getGridX
        """
        pass

    def setGridY(self, val): # real signature unknown; restored from __doc__
        """
        setGridY(val) -> None
        .   @copybrief getGridY @see getGridY
        """
        pass

    def setNeighbors(self, val): # real signature unknown; restored from __doc__
        """
        setNeighbors(val) -> None
        .   @copybrief getNeighbors @see getNeighbors
        """
        pass

    def setRadius(self, val): # real signature unknown; restored from __doc__
        """
        setRadius(val) -> None
        .   @copybrief getRadius @see getRadius
        """
        pass

    def setThreshold(self, val): # real signature unknown; restored from __doc__
        """
        setThreshold(val) -> None
        .   @copybrief getThreshold @see getThreshold
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


