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


class ml_DTrees(__cv2.ml_StatModel):
    # no doc
    def create(self): # real signature unknown; restored from __doc__
        """
        create() -> retval
        .   @brief Creates the empty model
        .   
        .       The static method creates empty decision tree with the specified parameters. It should be then
        .       trained using train method (see StatModel::train). Alternatively, you can load the model from
        .       file using Algorithm::load\<DTrees\>(filename).
        """
        pass

    def getCVFolds(self): # real signature unknown; restored from __doc__
        """
        getCVFolds() -> retval
        .   @see setCVFolds
        """
        pass

    def getMaxCategories(self): # real signature unknown; restored from __doc__
        """
        getMaxCategories() -> retval
        .   @see setMaxCategories
        """
        pass

    def getMaxDepth(self): # real signature unknown; restored from __doc__
        """
        getMaxDepth() -> retval
        .   @see setMaxDepth
        """
        pass

    def getMinSampleCount(self): # real signature unknown; restored from __doc__
        """
        getMinSampleCount() -> retval
        .   @see setMinSampleCount
        """
        pass

    def getPriors(self): # real signature unknown; restored from __doc__
        """
        getPriors() -> retval
        .   @see setPriors
        """
        pass

    def getRegressionAccuracy(self): # real signature unknown; restored from __doc__
        """
        getRegressionAccuracy() -> retval
        .   @see setRegressionAccuracy
        """
        pass

    def getTruncatePrunedTree(self): # real signature unknown; restored from __doc__
        """
        getTruncatePrunedTree() -> retval
        .   @see setTruncatePrunedTree
        """
        pass

    def getUse1SERule(self): # real signature unknown; restored from __doc__
        """
        getUse1SERule() -> retval
        .   @see setUse1SERule
        """
        pass

    def getUseSurrogates(self): # real signature unknown; restored from __doc__
        """
        getUseSurrogates() -> retval
        .   @see setUseSurrogates
        """
        pass

    def load(self, filepath, nodeName=None): # real signature unknown; restored from __doc__
        """
        load(filepath[, nodeName]) -> retval
        .   @brief Loads and creates a serialized DTrees from a file
        .        *
        .        * Use DTree::save to serialize and store an DTree to disk.
        .        * Load the DTree from this file again, by calling this function with the path to the file.
        .        * Optionally specify the node for the file containing the classifier
        .        *
        .        * @param filepath path to serialized DTree
        .        * @param nodeName name of node containing the classifier
        """
        pass

    def setCVFolds(self, val): # real signature unknown; restored from __doc__
        """
        setCVFolds(val) -> None
        .   @copybrief getCVFolds @see getCVFolds
        """
        pass

    def setMaxCategories(self, val): # real signature unknown; restored from __doc__
        """
        setMaxCategories(val) -> None
        .   @copybrief getMaxCategories @see getMaxCategories
        """
        pass

    def setMaxDepth(self, val): # real signature unknown; restored from __doc__
        """
        setMaxDepth(val) -> None
        .   @copybrief getMaxDepth @see getMaxDepth
        """
        pass

    def setMinSampleCount(self, val): # real signature unknown; restored from __doc__
        """
        setMinSampleCount(val) -> None
        .   @copybrief getMinSampleCount @see getMinSampleCount
        """
        pass

    def setPriors(self, val): # real signature unknown; restored from __doc__
        """
        setPriors(val) -> None
        .   @copybrief getPriors @see getPriors
        """
        pass

    def setRegressionAccuracy(self, val): # real signature unknown; restored from __doc__
        """
        setRegressionAccuracy(val) -> None
        .   @copybrief getRegressionAccuracy @see getRegressionAccuracy
        """
        pass

    def setTruncatePrunedTree(self, val): # real signature unknown; restored from __doc__
        """
        setTruncatePrunedTree(val) -> None
        .   @copybrief getTruncatePrunedTree @see getTruncatePrunedTree
        """
        pass

    def setUse1SERule(self, val): # real signature unknown; restored from __doc__
        """
        setUse1SERule(val) -> None
        .   @copybrief getUse1SERule @see getUse1SERule
        """
        pass

    def setUseSurrogates(self, val): # real signature unknown; restored from __doc__
        """
        setUseSurrogates(val) -> None
        .   @copybrief getUseSurrogates @see getUseSurrogates
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


