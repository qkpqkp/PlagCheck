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


class ml_ANN_MLP(__cv2.ml_StatModel):
    # no doc
    def create(self): # real signature unknown; restored from __doc__
        """
        create() -> retval
        .   @brief Creates empty model
        .   
        .       Use StatModel::train to train the model, Algorithm::load\<ANN_MLP\>(filename) to load the pre-trained model.
        .       Note that the train method has optional flags: ANN_MLP::TrainFlags.
        """
        pass

    def getAnnealCoolingRatio(self): # real signature unknown; restored from __doc__
        """
        getAnnealCoolingRatio() -> retval
        .   @see setAnnealCoolingRatio
        """
        pass

    def getAnnealFinalT(self): # real signature unknown; restored from __doc__
        """
        getAnnealFinalT() -> retval
        .   @see setAnnealFinalT
        """
        pass

    def getAnnealInitialT(self): # real signature unknown; restored from __doc__
        """
        getAnnealInitialT() -> retval
        .   @see setAnnealInitialT
        """
        pass

    def getAnnealItePerStep(self): # real signature unknown; restored from __doc__
        """
        getAnnealItePerStep() -> retval
        .   @see setAnnealItePerStep
        """
        pass

    def getBackpropMomentumScale(self): # real signature unknown; restored from __doc__
        """
        getBackpropMomentumScale() -> retval
        .   @see setBackpropMomentumScale
        """
        pass

    def getBackpropWeightScale(self): # real signature unknown; restored from __doc__
        """
        getBackpropWeightScale() -> retval
        .   @see setBackpropWeightScale
        """
        pass

    def getLayerSizes(self): # real signature unknown; restored from __doc__
        """
        getLayerSizes() -> retval
        .   Integer vector specifying the number of neurons in each layer including the input and output layers.
        .       The very first element specifies the number of elements in the input layer.
        .       The last element - number of elements in the output layer.
        .   @sa setLayerSizes
        """
        pass

    def getRpropDW0(self): # real signature unknown; restored from __doc__
        """
        getRpropDW0() -> retval
        .   @see setRpropDW0
        """
        pass

    def getRpropDWMax(self): # real signature unknown; restored from __doc__
        """
        getRpropDWMax() -> retval
        .   @see setRpropDWMax
        """
        pass

    def getRpropDWMin(self): # real signature unknown; restored from __doc__
        """
        getRpropDWMin() -> retval
        .   @see setRpropDWMin
        """
        pass

    def getRpropDWMinus(self): # real signature unknown; restored from __doc__
        """
        getRpropDWMinus() -> retval
        .   @see setRpropDWMinus
        """
        pass

    def getRpropDWPlus(self): # real signature unknown; restored from __doc__
        """
        getRpropDWPlus() -> retval
        .   @see setRpropDWPlus
        """
        pass

    def getTermCriteria(self): # real signature unknown; restored from __doc__
        """
        getTermCriteria() -> retval
        .   @see setTermCriteria
        """
        pass

    def getTrainMethod(self): # real signature unknown; restored from __doc__
        """
        getTrainMethod() -> retval
        .   Returns current training method
        """
        pass

    def getWeights(self, layerIdx): # real signature unknown; restored from __doc__
        """
        getWeights(layerIdx) -> retval
        .
        """
        pass

    def load(self, filepath): # real signature unknown; restored from __doc__
        """
        load(filepath) -> retval
        .   @brief Loads and creates a serialized ANN from a file
        .        *
        .        * Use ANN::save to serialize and store an ANN to disk.
        .        * Load the ANN from this file again, by calling this function with the path to the file.
        .        *
        .        * @param filepath path to serialized ANN
        """
        pass

    def setActivationFunction(self, type, param1=None, param2=None): # real signature unknown; restored from __doc__
        """
        setActivationFunction(type[, param1[, param2]]) -> None
        .   Initialize the activation function for each neuron.
        .       Currently the default and the only fully supported activation function is ANN_MLP::SIGMOID_SYM.
        .       @param type The type of activation function. See ANN_MLP::ActivationFunctions.
        .       @param param1 The first parameter of the activation function, \f$\alpha\f$. Default value is 0.
        .       @param param2 The second parameter of the activation function, \f$\beta\f$. Default value is 0.
        """
        pass

    def setAnnealCoolingRatio(self, val): # real signature unknown; restored from __doc__
        """
        setAnnealCoolingRatio(val) -> None
        .   @copybrief getAnnealCoolingRatio @see getAnnealCoolingRatio
        """
        pass

    def setAnnealFinalT(self, val): # real signature unknown; restored from __doc__
        """
        setAnnealFinalT(val) -> None
        .   @copybrief getAnnealFinalT @see getAnnealFinalT
        """
        pass

    def setAnnealInitialT(self, val): # real signature unknown; restored from __doc__
        """
        setAnnealInitialT(val) -> None
        .   @copybrief getAnnealInitialT @see getAnnealInitialT
        """
        pass

    def setAnnealItePerStep(self, val): # real signature unknown; restored from __doc__
        """
        setAnnealItePerStep(val) -> None
        .   @copybrief getAnnealItePerStep @see getAnnealItePerStep
        """
        pass

    def setBackpropMomentumScale(self, val): # real signature unknown; restored from __doc__
        """
        setBackpropMomentumScale(val) -> None
        .   @copybrief getBackpropMomentumScale @see getBackpropMomentumScale
        """
        pass

    def setBackpropWeightScale(self, val): # real signature unknown; restored from __doc__
        """
        setBackpropWeightScale(val) -> None
        .   @copybrief getBackpropWeightScale @see getBackpropWeightScale
        """
        pass

    def setLayerSizes(self, _layer_sizes): # real signature unknown; restored from __doc__
        """
        setLayerSizes(_layer_sizes) -> None
        .   Integer vector specifying the number of neurons in each layer including the input and output layers.
        .       The very first element specifies the number of elements in the input layer.
        .       The last element - number of elements in the output layer. Default value is empty Mat.
        .   @sa getLayerSizes
        """
        pass

    def setRpropDW0(self, val): # real signature unknown; restored from __doc__
        """
        setRpropDW0(val) -> None
        .   @copybrief getRpropDW0 @see getRpropDW0
        """
        pass

    def setRpropDWMax(self, val): # real signature unknown; restored from __doc__
        """
        setRpropDWMax(val) -> None
        .   @copybrief getRpropDWMax @see getRpropDWMax
        """
        pass

    def setRpropDWMin(self, val): # real signature unknown; restored from __doc__
        """
        setRpropDWMin(val) -> None
        .   @copybrief getRpropDWMin @see getRpropDWMin
        """
        pass

    def setRpropDWMinus(self, val): # real signature unknown; restored from __doc__
        """
        setRpropDWMinus(val) -> None
        .   @copybrief getRpropDWMinus @see getRpropDWMinus
        """
        pass

    def setRpropDWPlus(self, val): # real signature unknown; restored from __doc__
        """
        setRpropDWPlus(val) -> None
        .   @copybrief getRpropDWPlus @see getRpropDWPlus
        """
        pass

    def setTermCriteria(self, val): # real signature unknown; restored from __doc__
        """
        setTermCriteria(val) -> None
        .   @copybrief getTermCriteria @see getTermCriteria
        """
        pass

    def setTrainMethod(self, method, param1=None, param2=None): # real signature unknown; restored from __doc__
        """
        setTrainMethod(method[, param1[, param2]]) -> None
        .   Sets training method and common parameters.
        .       @param method Default value is ANN_MLP::RPROP. See ANN_MLP::TrainingMethods.
        .       @param param1 passed to setRpropDW0 for ANN_MLP::RPROP and to setBackpropWeightScale for ANN_MLP::BACKPROP and to initialT for ANN_MLP::ANNEAL.
        .       @param param2 passed to setRpropDWMin for ANN_MLP::RPROP and to setBackpropMomentumScale for ANN_MLP::BACKPROP and to finalT for ANN_MLP::ANNEAL.
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


