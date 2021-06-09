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


class ml_RTrees(__cv2.ml_DTrees):
    # no doc
    def create(self): # real signature unknown; restored from __doc__
        """
        create() -> retval
        .   Creates the empty model.
        .       Use StatModel::train to train the model, StatModel::train to create and train the model,
        .       Algorithm::load to load the pre-trained model.
        """
        pass

    def getActiveVarCount(self): # real signature unknown; restored from __doc__
        """
        getActiveVarCount() -> retval
        .   @see setActiveVarCount
        """
        pass

    def getCalculateVarImportance(self): # real signature unknown; restored from __doc__
        """
        getCalculateVarImportance() -> retval
        .   @see setCalculateVarImportance
        """
        pass

    def getTermCriteria(self): # real signature unknown; restored from __doc__
        """
        getTermCriteria() -> retval
        .   @see setTermCriteria
        """
        pass

    def getVarImportance(self): # real signature unknown; restored from __doc__
        """
        getVarImportance() -> retval
        .   Returns the variable importance array.
        .       The method returns the variable importance vector, computed at the training stage when
        .       CalculateVarImportance is set to true. If this flag was set to false, the empty matrix is
        .       returned.
        """
        pass

    def getVotes(self, samples, flags, results=None): # real signature unknown; restored from __doc__
        """
        getVotes(samples, flags[, results]) -> results
        .   Returns the result of each individual tree in the forest.
        .       In case the model is a regression problem, the method will return each of the trees'
        .       results for each of the sample cases. If the model is a classifier, it will return
        .       a Mat with samples + 1 rows, where the first row gives the class number and the
        .       following rows return the votes each class had for each sample.
        .           @param samples Array containing the samples for which votes will be calculated.
        .           @param results Array where the result of the calculation will be written.
        .           @param flags Flags for defining the type of RTrees.
        """
        pass

    def load(self, filepath, nodeName=None): # real signature unknown; restored from __doc__
        """
        load(filepath[, nodeName]) -> retval
        .   @brief Loads and creates a serialized RTree from a file
        .        *
        .        * Use RTree::save to serialize and store an RTree to disk.
        .        * Load the RTree from this file again, by calling this function with the path to the file.
        .        * Optionally specify the node for the file containing the classifier
        .        *
        .        * @param filepath path to serialized RTree
        .        * @param nodeName name of node containing the classifier
        """
        pass

    def setActiveVarCount(self, val): # real signature unknown; restored from __doc__
        """
        setActiveVarCount(val) -> None
        .   @copybrief getActiveVarCount @see getActiveVarCount
        """
        pass

    def setCalculateVarImportance(self, val): # real signature unknown; restored from __doc__
        """
        setCalculateVarImportance(val) -> None
        .   @copybrief getCalculateVarImportance @see getCalculateVarImportance
        """
        pass

    def setTermCriteria(self, val): # real signature unknown; restored from __doc__
        """
        setTermCriteria(val) -> None
        .   @copybrief getTermCriteria @see getTermCriteria
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


