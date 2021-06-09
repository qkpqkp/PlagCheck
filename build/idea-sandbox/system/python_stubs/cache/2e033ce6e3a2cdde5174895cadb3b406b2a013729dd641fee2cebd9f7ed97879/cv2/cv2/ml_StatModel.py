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


class ml_StatModel(__cv2.Algorithm):
    # no doc
    def calcError(self, data, test, resp=None): # real signature unknown; restored from __doc__
        """
        calcError(data, test[, resp]) -> retval, resp
        .   @brief Computes error on the training or test dataset
        .   
        .       @param data the training data
        .       @param test if true, the error is computed over the test subset of the data, otherwise it's
        .           computed over the training subset of the data. Please note that if you loaded a completely
        .           different dataset to evaluate already trained classifier, you will probably want not to set
        .           the test subset at all with TrainData::setTrainTestSplitRatio and specify test=false, so
        .           that the error is computed for the whole new set. Yes, this sounds a bit confusing.
        .       @param resp the optional output responses.
        .   
        .       The method uses StatModel::predict to compute the error. For regression models the error is
        .       computed as RMS, for classifiers - as a percent of missclassified samples (0%-100%).
        """
        pass

    def empty(self): # real signature unknown; restored from __doc__
        """
        empty() -> retval
        .
        """
        pass

    def getVarCount(self): # real signature unknown; restored from __doc__
        """
        getVarCount() -> retval
        .   @brief Returns the number of variables in training samples
        """
        pass

    def isClassifier(self): # real signature unknown; restored from __doc__
        """
        isClassifier() -> retval
        .   @brief Returns true if the model is classifier
        """
        pass

    def isTrained(self): # real signature unknown; restored from __doc__
        """
        isTrained() -> retval
        .   @brief Returns true if the model is trained
        """
        pass

    def predict(self, samples, results=None, flags=None): # real signature unknown; restored from __doc__
        """
        predict(samples[, results[, flags]]) -> retval, results
        .   @brief Predicts response(s) for the provided sample(s)
        .   
        .       @param samples The input samples, floating-point matrix
        .       @param results The optional output matrix of results.
        .       @param flags The optional flags, model-dependent. See cv::ml::StatModel::Flags.
        """
        pass

    def train(self, trainData, flags=None): # real signature unknown; restored from __doc__
        """
        train(trainData[, flags]) -> retval
        .   @brief Trains the statistical model
        .   
        .       @param trainData training data that can be loaded from file using TrainData::loadFromCSV or
        .           created with TrainData::create.
        .       @param flags optional flags, depending on the model. Some of the models can be updated with the
        .           new training samples, not completely overwritten (such as NormalBayesClassifier or ANN_MLP).
        
        
        
        train(samples, layout, responses) -> retval
        .   @brief Trains the statistical model
        .   
        .       @param samples training samples
        .       @param layout See ml::SampleTypes.
        .       @param responses vector of responses associated with the training samples.
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


