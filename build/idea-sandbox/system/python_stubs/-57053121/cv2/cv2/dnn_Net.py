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

class dnn_Net(object):
    # no doc
    def connect(self, outPin, inpPin): # real signature unknown; restored from __doc__
        """
        connect(outPin, inpPin) -> None
        .   @brief Connects output of the first layer to input of the second layer.
        .            *  @param outPin descriptor of the first layer output.
        .            *  @param inpPin descriptor of the second layer input.
        .            *
        .            * Descriptors have the following template <DFN>&lt;layer_name&gt;[.input_number]</DFN>:
        .            * - the first part of the template <DFN>layer_name</DFN> is string name of the added layer.
        .            *   If this part is empty then the network input pseudo layer will be used;
        .            * - the second optional part of the template <DFN>input_number</DFN>
        .            *   is either number of the layer input, either label one.
        .            *   If this part is omitted then the first layer input will be used.
        .            *
        .            *  @see setNetInputs(), Layer::inputNameToIndex(), Layer::outputNameToIndex()
        """
        pass

    def dump(self): # real signature unknown; restored from __doc__
        """
        dump() -> retval
        .   @brief Dump net to String
        .            *  @returns String with structure, hyperparameters, backend, target and fusion
        .            *  Call method after setInput(). To see correct backend, target and fusion run after forward().
        """
        pass

    def dumpToFile(self, path): # real signature unknown; restored from __doc__
        """
        dumpToFile(path) -> None
        .   @brief Dump net structure, hyperparameters, backend, target and fusion to dot file
        .            *  @param path   path to output file with .dot extension
        .            *  @see dump()
        """
        pass

    def empty(self): # real signature unknown; restored from __doc__
        """
        empty() -> retval
        .   Returns true if there are no layers in the network.
        """
        pass

    def enableFusion(self, fusion): # real signature unknown; restored from __doc__
        """
        enableFusion(fusion) -> None
        .   @brief Enables or disables layer fusion in the network.
        .            * @param fusion true to enable the fusion, false to disable. The fusion is enabled by default.
        """
        pass

    def forward(self, outputName=None): # real signature unknown; restored from __doc__
        """
        forward([, outputName]) -> retval
        .   @brief Runs forward pass to compute output of layer with name @p outputName.
        .            *  @param outputName name for layer which output is needed to get
        .            *  @return blob for first output of specified layer.
        .            *  @details By default runs forward pass for the whole network.
        
        
        
        forward([, outputBlobs[, outputName]]) -> outputBlobs
        .   @brief Runs forward pass to compute output of layer with name @p outputName.
        .            *  @param outputBlobs contains all output blobs for specified layer.
        .            *  @param outputName name for layer which output is needed to get
        .            *  @details If @p outputName is empty, runs forward pass for the whole network.
        
        
        
        forward(outBlobNames[, outputBlobs]) -> outputBlobs
        .   @brief Runs forward pass to compute outputs of layers listed in @p outBlobNames.
        .            *  @param outputBlobs contains blobs for first outputs of specified layers.
        .            *  @param outBlobNames names for layers which outputs are needed to get
        """
        pass

    def forwardAndRetrieve(self, outBlobNames): # real signature unknown; restored from __doc__
        """
        forwardAndRetrieve(outBlobNames) -> outputBlobs
        .   @brief Runs forward pass to compute outputs of layers listed in @p outBlobNames.
        .            *  @param outputBlobs contains all output blobs for each layer specified in @p outBlobNames.
        .            *  @param outBlobNames names for layers which outputs are needed to get
        """
        pass

    def forwardAsync(self, outputName=None): # real signature unknown; restored from __doc__
        """
        forwardAsync([, outputName]) -> retval
        .   @brief Runs forward pass to compute output of layer with name @p outputName.
        .            *  @param outputName name for layer which output is needed to get
        .            *  @details By default runs forward pass for the whole network.
        .            *
        .            *  This is an asynchronous version of forward(const String&).
        .            *  dnn::DNN_BACKEND_INFERENCE_ENGINE backend is required.
        """
        pass

    def getFLOPS(self, netInputShapes): # real signature unknown; restored from __doc__
        """
        getFLOPS(netInputShapes) -> retval
        .   @brief Computes FLOP for whole loaded model with specified input shapes.
        .            * @param netInputShapes vector of shapes for all net inputs.
        .            * @returns computed FLOP.
        
        
        
        getFLOPS(netInputShape) -> retval
        .   @overload
        
        
        
        getFLOPS(layerId, netInputShapes) -> retval
        .   @overload
        
        
        
        getFLOPS(layerId, netInputShape) -> retval
        .   @overload
        """
        pass

    def getLayer(self, layerId): # real signature unknown; restored from __doc__
        """
        getLayer(layerId) -> retval
        .   @brief Returns pointer to layer with specified id or name which the network use.
        """
        pass

    def getLayerId(self, layer): # real signature unknown; restored from __doc__
        """
        getLayerId(layer) -> retval
        .   @brief Converts string name of the layer to the integer identifier.
        .            *  @returns id of the layer, or -1 if the layer wasn't found.
        """
        pass

    def getLayerNames(self): # real signature unknown; restored from __doc__
        """
        getLayerNames() -> retval
        .
        """
        pass

    def getLayersCount(self, layerType): # real signature unknown; restored from __doc__
        """
        getLayersCount(layerType) -> retval
        .   @brief Returns count of layers of specified type.
        .            * @param layerType type.
        .            * @returns count of layers
        """
        pass

    def getLayersShapes(self, netInputShapes): # real signature unknown; restored from __doc__
        """
        getLayersShapes(netInputShapes) -> layersIds, inLayersShapes, outLayersShapes
        .   @brief Returns input and output shapes for all layers in loaded model;
        .            *  preliminary inferencing isn't necessary.
        .            *  @param netInputShapes shapes for all input blobs in net input layer.
        .            *  @param layersIds output parameter for layer IDs.
        .            *  @param inLayersShapes output parameter for input layers shapes;
        .            * order is the same as in layersIds
        .            *  @param outLayersShapes output parameter for output layers shapes;
        .            * order is the same as in layersIds
        
        
        
        getLayersShapes(netInputShape) -> layersIds, inLayersShapes, outLayersShapes
        .   @overload
        """
        pass

    def getLayerTypes(self): # real signature unknown; restored from __doc__
        """
        getLayerTypes() -> layersTypes
        .   @brief Returns list of types for layer used in model.
        .            * @param layersTypes output parameter for returning types.
        """
        pass

    def getMemoryConsumption(self, netInputShape): # real signature unknown; restored from __doc__
        """
        getMemoryConsumption(netInputShape) -> weights, blobs
        .   @overload
        
        
        
        getMemoryConsumption(layerId, netInputShapes) -> weights, blobs
        .   @overload
        
        
        
        getMemoryConsumption(layerId, netInputShape) -> weights, blobs
        .   @overload
        """
        pass

    def getParam(self, layer, numParam=None): # real signature unknown; restored from __doc__
        """
        getParam(layer[, numParam]) -> retval
        .   @brief Returns parameter blob of the layer.
        .            *  @param layer name or id of the layer.
        .            *  @param numParam index of the layer parameter in the Layer::blobs array.
        .            *  @see Layer::blobs
        """
        pass

    def getPerfProfile(self): # real signature unknown; restored from __doc__
        """
        getPerfProfile() -> retval, timings
        .   @brief Returns overall time for inference and timings (in ticks) for layers.
        .            * Indexes in returned vector correspond to layers ids. Some layers can be fused with others,
        .            * in this case zero ticks count will be return for that skipped layers.
        .            * @param timings vector for tick timings for all layers.
        .            * @return overall ticks for model inference.
        """
        pass

    def getUnconnectedOutLayers(self): # real signature unknown; restored from __doc__
        """
        getUnconnectedOutLayers() -> retval
        .   @brief Returns indexes of layers with unconnected outputs.
        """
        pass

    def getUnconnectedOutLayersNames(self): # real signature unknown; restored from __doc__
        """
        getUnconnectedOutLayersNames() -> retval
        .   @brief Returns names of layers with unconnected outputs.
        """
        pass

    def readFromModelOptimizer(self, xml, bin): # real signature unknown; restored from __doc__
        """
        readFromModelOptimizer(xml, bin) -> retval
        .   @brief Create a network from Intel's Model Optimizer intermediate representation.
        .            *  @param[in] xml XML configuration file with network's topology.
        .            *  @param[in] bin Binary file with trained weights.
        .            *  Networks imported from Intel's Model Optimizer are launched in Intel's Inference Engine
        .            *  backend.
        """
        pass

    def setHalideScheduler(self, scheduler): # real signature unknown; restored from __doc__
        """
        setHalideScheduler(scheduler) -> None
        .   * @brief Compile Halide layers.
        .            * @param[in] scheduler Path to YAML file with scheduling directives.
        .            * @see setPreferableBackend
        .            *
        .            * Schedule layers that support Halide backend. Then compile them for
        .            * specific target. For layers that not represented in scheduling file
        .            * or if no manual scheduling used at all, automatic scheduling will be applied.
        """
        pass

    def setInput(self, blob, name=None, scalefactor=None, mean=None): # real signature unknown; restored from __doc__
        """
        setInput(blob[, name[, scalefactor[, mean]]]) -> None
        .   @brief Sets the new input value for the network
        .            *  @param blob        A new blob. Should have CV_32F or CV_8U depth.
        .            *  @param name        A name of input layer.
        .            *  @param scalefactor An optional normalization scale.
        .            *  @param mean        An optional mean subtraction values.
        .            *  @see connect(String, String) to know format of the descriptor.
        .            *
        .            *  If scale or mean values are specified, a final input blob is computed
        .            *  as:
        .            * \f[input(n,c,h,w) = scalefactor \times (blob(n,c,h,w) - mean_c)\f]
        """
        pass

    def setInputsNames(self, inputBlobNames): # real signature unknown; restored from __doc__
        """
        setInputsNames(inputBlobNames) -> None
        .   @brief Sets outputs names of the network input pseudo layer.
        .            *
        .            * Each net always has special own the network input pseudo layer with id=0.
        .            * This layer stores the user blobs only and don't make any computations.
        .            * In fact, this layer provides the only way to pass user data into the network.
        .            * As any other layer, this layer can label its outputs and this function provides an easy way to do this.
        """
        pass

    def setParam(self, layer, numParam, blob): # real signature unknown; restored from __doc__
        """
        setParam(layer, numParam, blob) -> None
        .   @brief Sets the new value for the learned param of the layer.
        .            *  @param layer name or id of the layer.
        .            *  @param numParam index of the layer parameter in the Layer::blobs array.
        .            *  @param blob the new value.
        .            *  @see Layer::blobs
        .            *  @note If shape of the new blob differs from the previous shape,
        .            *  then the following forward pass may fail.
        """
        pass

    def setPreferableBackend(self, backendId): # real signature unknown; restored from __doc__
        """
        setPreferableBackend(backendId) -> None
        .   * @brief Ask network to use specific computation backend where it supported.
        .            * @param[in] backendId backend identifier.
        .            * @see Backend
        .            *
        .            * If OpenCV is compiled with Intel's Inference Engine library, DNN_BACKEND_DEFAULT
        .            * means DNN_BACKEND_INFERENCE_ENGINE. Otherwise it equals to DNN_BACKEND_OPENCV.
        """
        pass

    def setPreferableTarget(self, targetId): # real signature unknown; restored from __doc__
        """
        setPreferableTarget(targetId) -> None
        .   * @brief Ask network to make computations on specific target device.
        .            * @param[in] targetId target identifier.
        .            * @see Target
        .            *
        .            * List of supported combinations backend / target:
        .            * |                        | DNN_BACKEND_OPENCV | DNN_BACKEND_INFERENCE_ENGINE | DNN_BACKEND_HALIDE |
        .            * |------------------------|--------------------|------------------------------|--------------------|
        .            * | DNN_TARGET_CPU         |                  + |                            + |                  + |
        .            * | DNN_TARGET_OPENCL      |                  + |                            + |                  + |
        .            * | DNN_TARGET_OPENCL_FP16 |                  + |                            + |                    |
        .            * | DNN_TARGET_MYRIAD      |                    |                            + |                    |
        .            * | DNN_TARGET_FPGA        |                    |                            + |                    |
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


