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

class ml_TrainData(object):
    # no doc
    def create(self, samples, layout, responses, varIdx=None, sampleIdx=None, sampleWeights=None, varType=None): # real signature unknown; restored from __doc__
        """
        create(samples, layout, responses[, varIdx[, sampleIdx[, sampleWeights[, varType]]]]) -> retval
        .   @brief Creates training data from in-memory arrays.
        .   
        .       @param samples matrix of samples. It should have CV_32F type.
        .       @param layout see ml::SampleTypes.
        .       @param responses matrix of responses. If the responses are scalar, they should be stored as a
        .           single row or as a single column. The matrix should have type CV_32F or CV_32S (in the
        .           former case the responses are considered as ordered by default; in the latter case - as
        .           categorical)
        .       @param varIdx vector specifying which variables to use for training. It can be an integer vector
        .           (CV_32S) containing 0-based variable indices or byte vector (CV_8U) containing a mask of
        .           active variables.
        .       @param sampleIdx vector specifying which samples to use for training. It can be an integer
        .           vector (CV_32S) containing 0-based sample indices or byte vector (CV_8U) containing a mask
        .           of training samples.
        .       @param sampleWeights optional vector with weights for each sample. It should have CV_32F type.
        .       @param varType optional vector of type CV_8U and size `<number_of_variables_in_samples> +
        .           <number_of_variables_in_responses>`, containing types of each input and output variable. See
        .           ml::VariableTypes.
        """
        pass

    def getCatCount(self, vi): # real signature unknown; restored from __doc__
        """
        getCatCount(vi) -> retval
        .
        """
        pass

    def getCatMap(self): # real signature unknown; restored from __doc__
        """
        getCatMap() -> retval
        .
        """
        pass

    def getCatOfs(self): # real signature unknown; restored from __doc__
        """
        getCatOfs() -> retval
        .
        """
        pass

    def getClassLabels(self): # real signature unknown; restored from __doc__
        """
        getClassLabels() -> retval
        .   @brief Returns the vector of class labels
        .   
        .       The function returns vector of unique labels occurred in the responses.
        """
        pass

    def getDefaultSubstValues(self): # real signature unknown; restored from __doc__
        """
        getDefaultSubstValues() -> retval
        .
        """
        pass

    def getLayout(self): # real signature unknown; restored from __doc__
        """
        getLayout() -> retval
        .
        """
        pass

    def getMissing(self): # real signature unknown; restored from __doc__
        """
        getMissing() -> retval
        .
        """
        pass

    def getNAllVars(self): # real signature unknown; restored from __doc__
        """
        getNAllVars() -> retval
        .
        """
        pass

    def getNames(self, names): # real signature unknown; restored from __doc__
        """
        getNames(names) -> None
        .   @brief Returns vector of symbolic names captured in loadFromCSV()
        """
        pass

    def getNormCatResponses(self): # real signature unknown; restored from __doc__
        """
        getNormCatResponses() -> retval
        .
        """
        pass

    def getNSamples(self): # real signature unknown; restored from __doc__
        """
        getNSamples() -> retval
        .
        """
        pass

    def getNTestSamples(self): # real signature unknown; restored from __doc__
        """
        getNTestSamples() -> retval
        .
        """
        pass

    def getNTrainSamples(self): # real signature unknown; restored from __doc__
        """
        getNTrainSamples() -> retval
        .
        """
        pass

    def getNVars(self): # real signature unknown; restored from __doc__
        """
        getNVars() -> retval
        .
        """
        pass

    def getResponses(self): # real signature unknown; restored from __doc__
        """
        getResponses() -> retval
        .
        """
        pass

    def getResponseType(self): # real signature unknown; restored from __doc__
        """
        getResponseType() -> retval
        .
        """
        pass

    def getSample(self, varIdx, sidx, buf): # real signature unknown; restored from __doc__
        """
        getSample(varIdx, sidx, buf) -> None
        .
        """
        pass

    def getSamples(self): # real signature unknown; restored from __doc__
        """
        getSamples() -> retval
        .
        """
        pass

    def getSampleWeights(self): # real signature unknown; restored from __doc__
        """
        getSampleWeights() -> retval
        .
        """
        pass

    def getSubMatrix(self, matrix, idx, layout): # real signature unknown; restored from __doc__
        """
        getSubMatrix(matrix, idx, layout) -> retval
        .   @brief Extract from matrix rows/cols specified by passed indexes.
        .       @param matrix input matrix (supported types: CV_32S, CV_32F, CV_64F)
        .       @param idx 1D index vector
        .       @param layout specifies to extract rows (cv::ml::ROW_SAMPLES) or to extract columns (cv::ml::COL_SAMPLES)
        """
        pass

    def getSubVector(self, vec, idx): # real signature unknown; restored from __doc__
        """
        getSubVector(vec, idx) -> retval
        .   @brief Extract from 1D vector elements specified by passed indexes.
        .       @param vec input vector (supported types: CV_32S, CV_32F, CV_64F)
        .       @param idx 1D index vector
        """
        pass

    def getTestNormCatResponses(self): # real signature unknown; restored from __doc__
        """
        getTestNormCatResponses() -> retval
        .
        """
        pass

    def getTestResponses(self): # real signature unknown; restored from __doc__
        """
        getTestResponses() -> retval
        .
        """
        pass

    def getTestSampleIdx(self): # real signature unknown; restored from __doc__
        """
        getTestSampleIdx() -> retval
        .
        """
        pass

    def getTestSamples(self): # real signature unknown; restored from __doc__
        """
        getTestSamples() -> retval
        .   @brief Returns matrix of test samples
        """
        pass

    def getTestSampleWeights(self): # real signature unknown; restored from __doc__
        """
        getTestSampleWeights() -> retval
        .
        """
        pass

    def getTrainNormCatResponses(self): # real signature unknown; restored from __doc__
        """
        getTrainNormCatResponses() -> retval
        .   @brief Returns the vector of normalized categorical responses
        .   
        .       The function returns vector of responses. Each response is integer from `0` to `<number of
        .       classes>-1`. The actual label value can be retrieved then from the class label vector, see
        .       TrainData::getClassLabels.
        """
        pass

    def getTrainResponses(self): # real signature unknown; restored from __doc__
        """
        getTrainResponses() -> retval
        .   @brief Returns the vector of responses
        .   
        .       The function returns ordered or the original categorical responses. Usually it's used in
        .       regression algorithms.
        """
        pass

    def getTrainSampleIdx(self): # real signature unknown; restored from __doc__
        """
        getTrainSampleIdx() -> retval
        .
        """
        pass

    def getTrainSamples(self, layout=None, compressSamples=None, compressVars=None): # real signature unknown; restored from __doc__
        """
        getTrainSamples([, layout[, compressSamples[, compressVars]]]) -> retval
        .   @brief Returns matrix of train samples
        .   
        .       @param layout The requested layout. If it's different from the initial one, the matrix is
        .           transposed. See ml::SampleTypes.
        .       @param compressSamples if true, the function returns only the training samples (specified by
        .           sampleIdx)
        .       @param compressVars if true, the function returns the shorter training samples, containing only
        .           the active variables.
        .   
        .       In current implementation the function tries to avoid physical data copying and returns the
        .       matrix stored inside TrainData (unless the transposition or compression is needed).
        """
        pass

    def getTrainSampleWeights(self): # real signature unknown; restored from __doc__
        """
        getTrainSampleWeights() -> retval
        .
        """
        pass

    def getValues(self, vi, sidx, values): # real signature unknown; restored from __doc__
        """
        getValues(vi, sidx, values) -> None
        .
        """
        pass

    def getVarIdx(self): # real signature unknown; restored from __doc__
        """
        getVarIdx() -> retval
        .
        """
        pass

    def getVarSymbolFlags(self): # real signature unknown; restored from __doc__
        """
        getVarSymbolFlags() -> retval
        .
        """
        pass

    def getVarType(self): # real signature unknown; restored from __doc__
        """
        getVarType() -> retval
        .
        """
        pass

    def setTrainTestSplit(self, count, shuffle=None): # real signature unknown; restored from __doc__
        """
        setTrainTestSplit(count[, shuffle]) -> None
        .   @brief Splits the training data into the training and test parts
        .       @sa TrainData::setTrainTestSplitRatio
        """
        pass

    def setTrainTestSplitRatio(self, ratio, shuffle=None): # real signature unknown; restored from __doc__
        """
        setTrainTestSplitRatio(ratio[, shuffle]) -> None
        .   @brief Splits the training data into the training and test parts
        .   
        .       The function selects a subset of specified relative size and then returns it as the training
        .       set. If the function is not called, all the data is used for training. Please, note that for
        .       each of TrainData::getTrain\* there is corresponding TrainData::getTest\*, so that the test
        .       subset can be retrieved and processed as well.
        .       @sa TrainData::setTrainTestSplit
        """
        pass

    def shuffleTrainTest(self): # real signature unknown; restored from __doc__
        """
        shuffleTrainTest() -> None
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


