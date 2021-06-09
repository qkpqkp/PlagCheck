# encoding: utf-8
# module cv2.dnn
# from C:\Users\Doly\Anaconda3\lib\site-packages\cv2\cv2.cp37-win_amd64.pyd
# by generator 1.147
# no doc
# no imports

# Variables with simple values

DNN_BACKEND_DEFAULT = 0
DNN_BACKEND_HALIDE = 1

DNN_BACKEND_INFERENCE_ENGINE = 2

DNN_BACKEND_OPENCV = 3
DNN_BACKEND_VKCOM = 4

DNN_TARGET_CPU = 0
DNN_TARGET_FPGA = 5
DNN_TARGET_MYRIAD = 3
DNN_TARGET_OPENCL = 1

DNN_TARGET_OPENCL_FP16 = 2

DNN_TARGET_VULKAN = 4

__loader__ = None

__spec__ = None

# functions

def blobFromImage(image, scalefactor=None, size=None, mean=None, swapRB=None, crop=None, ddepth=None): # real signature unknown; restored from __doc__
    """
    blobFromImage(image[, scalefactor[, size[, mean[, swapRB[, crop[, ddepth]]]]]]) -> retval
    .   @brief Creates 4-dimensional blob from image. Optionally resizes and crops @p image from center,
    .        *  subtract @p mean values, scales values by @p scalefactor, swap Blue and Red channels.
    .        *  @param image input image (with 1-, 3- or 4-channels).
    .        *  @param size spatial size for output image
    .        *  @param mean scalar with mean values which are subtracted from channels. Values are intended
    .        *  to be in (mean-R, mean-G, mean-B) order if @p image has BGR ordering and @p swapRB is true.
    .        *  @param scalefactor multiplier for @p image values.
    .        *  @param swapRB flag which indicates that swap first and last channels
    .        *  in 3-channel image is necessary.
    .        *  @param crop flag which indicates whether image will be cropped after resize or not
    .        *  @param ddepth Depth of output blob. Choose CV_32F or CV_8U.
    .        *  @details if @p crop is true, input image is resized so one side after resize is equal to corresponding
    .        *  dimension in @p size and another one is equal or larger. Then, crop from the center is performed.
    .        *  If @p crop is false, direct resize without cropping and preserving aspect ratio is performed.
    .        *  @returns 4-dimensional Mat with NCHW dimensions order.
    """
    pass

def blobFromImages(images, scalefactor=None, size=None, mean=None, swapRB=None, crop=None, ddepth=None): # real signature unknown; restored from __doc__
    """
    blobFromImages(images[, scalefactor[, size[, mean[, swapRB[, crop[, ddepth]]]]]]) -> retval
    .   @brief Creates 4-dimensional blob from series of images. Optionally resizes and
    .        *  crops @p images from center, subtract @p mean values, scales values by @p scalefactor,
    .        *  swap Blue and Red channels.
    .        *  @param images input images (all with 1-, 3- or 4-channels).
    .        *  @param size spatial size for output image
    .        *  @param mean scalar with mean values which are subtracted from channels. Values are intended
    .        *  to be in (mean-R, mean-G, mean-B) order if @p image has BGR ordering and @p swapRB is true.
    .        *  @param scalefactor multiplier for @p images values.
    .        *  @param swapRB flag which indicates that swap first and last channels
    .        *  in 3-channel image is necessary.
    .        *  @param crop flag which indicates whether image will be cropped after resize or not
    .        *  @param ddepth Depth of output blob. Choose CV_32F or CV_8U.
    .        *  @details if @p crop is true, input image is resized so one side after resize is equal to corresponding
    .        *  dimension in @p size and another one is equal or larger. Then, crop from the center is performed.
    .        *  If @p crop is false, direct resize without cropping and preserving aspect ratio is performed.
    .        *  @returns 4-dimensional Mat with NCHW dimensions order.
    """
    pass

def imagesFromBlob(blob_, images_=None): # real signature unknown; restored from __doc__
    """
    imagesFromBlob(blob_[, images_]) -> images_
    .   @brief Parse a 4D blob and output the images it contains as 2D arrays through a simpler data structure
    .        *  (std::vector<cv::Mat>).
    .        *  @param[in] blob_ 4 dimensional array (images, channels, height, width) in floating point precision (CV_32F) from
    .        *  which you would like to extract the images.
    .        *  @param[out] images_ array of 2D Mat containing the images extracted from the blob in floating point precision
    .        *  (CV_32F). They are non normalized neither mean added. The number of returned images equals the first dimension
    .        *  of the blob (batch size). Every image has a number of channels equals to the second dimension of the blob (depth).
    """
    pass

def Net_readFromModelOptimizer(xml, bin): # real signature unknown; restored from __doc__
    """
    Net_readFromModelOptimizer(xml, bin) -> retval
    .   @brief Create a network from Intel's Model Optimizer intermediate representation.
    .            *  @param[in] xml XML configuration file with network's topology.
    .            *  @param[in] bin Binary file with trained weights.
    .            *  Networks imported from Intel's Model Optimizer are launched in Intel's Inference Engine
    .            *  backend.
    """
    pass

def NMSBoxes(bboxes, scores, score_threshold, nms_threshold, eta=None, top_k=None): # real signature unknown; restored from __doc__
    """
    NMSBoxes(bboxes, scores, score_threshold, nms_threshold[, eta[, top_k]]) -> indices
    .   @brief Performs non maximum suppression given boxes and corresponding scores.
    .   
    .        * @param bboxes a set of bounding boxes to apply NMS.
    .        * @param scores a set of corresponding confidences.
    .        * @param score_threshold a threshold used to filter boxes by score.
    .        * @param nms_threshold a threshold used in non maximum suppression.
    .        * @param indices the kept indices of bboxes after NMS.
    .        * @param eta a coefficient in adaptive threshold formula: \f$nms\_threshold_{i+1}=eta\cdot nms\_threshold_i\f$.
    .        * @param top_k if `>0`, keep at most @p top_k picked indices.
    """
    pass

def NMSBoxesRotated(bboxes, scores, score_threshold, nms_threshold, eta=None, top_k=None): # real signature unknown; restored from __doc__
    """
    NMSBoxesRotated(bboxes, scores, score_threshold, nms_threshold[, eta[, top_k]]) -> indices
    .
    """
    pass

def readNet(model, config=None, framework=None): # real signature unknown; restored from __doc__
    """
    readNet(model[, config[, framework]]) -> retval
    .   * @brief Read deep learning network represented in one of the supported formats.
    .         * @param[in] model Binary file contains trained weights. The following file
    .         *                  extensions are expected for models from different frameworks:
    .         *                  * `*.caffemodel` (Caffe, http://caffe.berkeleyvision.org/)
    .         *                  * `*.pb` (TensorFlow, https://www.tensorflow.org/)
    .         *                  * `*.t7` | `*.net` (Torch, http://torch.ch/)
    .         *                  * `*.weights` (Darknet, https://pjreddie.com/darknet/)
    .         *                  * `*.bin` (DLDT, https://software.intel.com/openvino-toolkit)
    .         *                  * `*.onnx` (ONNX, https://onnx.ai/)
    .         * @param[in] config Text file contains network configuration. It could be a
    .         *                   file with the following extensions:
    .         *                  * `*.prototxt` (Caffe, http://caffe.berkeleyvision.org/)
    .         *                  * `*.pbtxt` (TensorFlow, https://www.tensorflow.org/)
    .         *                  * `*.cfg` (Darknet, https://pjreddie.com/darknet/)
    .         *                  * `*.xml` (DLDT, https://software.intel.com/openvino-toolkit)
    .         * @param[in] framework Explicit framework name tag to determine a format.
    .         * @returns Net object.
    .         *
    .         * This function automatically detects an origin framework of trained model
    .         * and calls an appropriate function such @ref readNetFromCaffe, @ref readNetFromTensorflow,
    .         * @ref readNetFromTorch or @ref readNetFromDarknet. An order of @p model and @p config
    .         * arguments does not matter.
    
    
    
    readNet(framework, bufferModel[, bufferConfig]) -> retval
    .   * @brief Read deep learning network represented in one of the supported formats.
    .         * @details This is an overloaded member function, provided for convenience.
    .         *          It differs from the above function only in what argument(s) it accepts.
    .         * @param[in] framework    Name of origin framework.
    .         * @param[in] bufferModel  A buffer with a content of binary file with weights
    .         * @param[in] bufferConfig A buffer with a content of text file contains network configuration.
    .         * @returns Net object.
    """
    pass

def readNetFromCaffe(prototxt, caffeModel=None): # real signature unknown; restored from __doc__
    """
    readNetFromCaffe(prototxt[, caffeModel]) -> retval
    .   @brief Reads a network model stored in <a href="http://caffe.berkeleyvision.org">Caffe</a> framework's format.
    .         * @param prototxt   path to the .prototxt file with text description of the network architecture.
    .         * @param caffeModel path to the .caffemodel file with learned network.
    .         * @returns Net object.
    
    
    
    readNetFromCaffe(bufferProto[, bufferModel]) -> retval
    .   @brief Reads a network model stored in Caffe model in memory.
    .         * @param bufferProto buffer containing the content of the .prototxt file
    .         * @param bufferModel buffer containing the content of the .caffemodel file
    .         * @returns Net object.
    """
    pass

def readNetFromDarknet(cfgFile, darknetModel=None): # real signature unknown; restored from __doc__
    """
    readNetFromDarknet(cfgFile[, darknetModel]) -> retval
    .   @brief Reads a network model stored in <a href="https://pjreddie.com/darknet/">Darknet</a> model files.
    .       *  @param cfgFile      path to the .cfg file with text description of the network architecture.
    .       *  @param darknetModel path to the .weights file with learned network.
    .       *  @returns Network object that ready to do forward, throw an exception in failure cases.
    .       *  @returns Net object.
    
    
    
    readNetFromDarknet(bufferCfg[, bufferModel]) -> retval
    .   @brief Reads a network model stored in <a href="https://pjreddie.com/darknet/">Darknet</a> model files.
    .        *  @param bufferCfg   A buffer contains a content of .cfg file with text description of the network architecture.
    .        *  @param bufferModel A buffer contains a content of .weights file with learned network.
    .        *  @returns Net object.
    """
    pass

def readNetFromModelOptimizer(xml, bin): # real signature unknown; restored from __doc__
    """
    readNetFromModelOptimizer(xml, bin) -> retval
    .   @brief Load a network from Intel's Model Optimizer intermediate representation.
    .        *  @param[in] xml XML configuration file with network's topology.
    .        *  @param[in] bin Binary file with trained weights.
    .        *  @returns Net object.
    .        *  Networks imported from Intel's Model Optimizer are launched in Intel's Inference Engine
    .        *  backend.
    """
    pass

def readNetFromONNX(onnxFile): # real signature unknown; restored from __doc__
    """
    readNetFromONNX(onnxFile) -> retval
    .   @brief Reads a network model <a href="https://onnx.ai/">ONNX</a>.
    .        *  @param onnxFile path to the .onnx file with text description of the network architecture.
    .        *  @returns Network object that ready to do forward, throw an exception in failure cases.
    
    
    
    readNetFromONNX(buffer) -> retval
    .   @brief Reads a network model from <a href="https://onnx.ai/">ONNX</a>
    .        *         in-memory buffer.
    .        *  @param buffer in-memory buffer that stores the ONNX model bytes.
    .        *  @returns Network object that ready to do forward, throw an exception
    .        *        in failure cases.
    """
    pass

def readNetFromTensorflow(model, config=None): # real signature unknown; restored from __doc__
    """
    readNetFromTensorflow(model[, config]) -> retval
    .   @brief Reads a network model stored in <a href="https://www.tensorflow.org/">TensorFlow</a> framework's format.
    .         * @param model  path to the .pb file with binary protobuf description of the network architecture
    .         * @param config path to the .pbtxt file that contains text graph definition in protobuf format.
    .         *               Resulting Net object is built by text graph using weights from a binary one that
    .         *               let us make it more flexible.
    .         * @returns Net object.
    
    
    
    readNetFromTensorflow(bufferModel[, bufferConfig]) -> retval
    .   @brief Reads a network model stored in <a href="https://www.tensorflow.org/">TensorFlow</a> framework's format.
    .         * @param bufferModel buffer containing the content of the pb file
    .         * @param bufferConfig buffer containing the content of the pbtxt file
    .         * @returns Net object.
    """
    pass

def readNetFromTorch(model, isBinary=None, evaluate=None): # real signature unknown; restored from __doc__
    """
    readNetFromTorch(model[, isBinary[, evaluate]]) -> retval
    .   *  @brief Reads a network model stored in <a href="http://torch.ch">Torch7</a> framework's format.
    .        *  @param model    path to the file, dumped from Torch by using torch.save() function.
    .        *  @param isBinary specifies whether the network was serialized in ascii mode or binary.
    .        *  @param evaluate specifies testing phase of network. If true, it's similar to evaluate() method in Torch.
    .        *  @returns Net object.
    .        *
    .        *  @note Ascii mode of Torch serializer is more preferable, because binary mode extensively use `long` type of C language,
    .        *  which has various bit-length on different systems.
    .        *
    .        * The loading file must contain serialized <a href="https://github.com/torch/nn/blob/master/doc/module.md">nn.Module</a> object
    .        * with importing network. Try to eliminate a custom objects from serialazing data to avoid importing errors.
    .        *
    .        * List of supported layers (i.e. object instances derived from Torch nn.Module class):
    .        * - nn.Sequential
    .        * - nn.Parallel
    .        * - nn.Concat
    .        * - nn.Linear
    .        * - nn.SpatialConvolution
    .        * - nn.SpatialMaxPooling, nn.SpatialAveragePooling
    .        * - nn.ReLU, nn.TanH, nn.Sigmoid
    .        * - nn.Reshape
    .        * - nn.SoftMax, nn.LogSoftMax
    .        *
    .        * Also some equivalents of these classes from cunn, cudnn, and fbcunn may be successfully imported.
    """
    pass

def readTensorFromONNX(path): # real signature unknown; restored from __doc__
    """
    readTensorFromONNX(path) -> retval
    .   @brief Creates blob from .pb file.
    .        *  @param path to the .pb file with input tensor.
    .        *  @returns Mat.
    """
    pass

def readTorchBlob(filename, isBinary=None): # real signature unknown; restored from __doc__
    """
    readTorchBlob(filename[, isBinary]) -> retval
    .   @brief Loads blob which was serialized as torch.Tensor object of Torch7 framework.
    .        *  @warning This function has the same limitations as readNetFromTorch().
    """
    pass

def shrinkCaffeModel(src, dst, layersTypes=None): # real signature unknown; restored from __doc__
    """
    shrinkCaffeModel(src, dst[, layersTypes]) -> None
    .   @brief Convert all weights of Caffe network to half precision floating point.
    .        * @param src Path to origin model from Caffe framework contains single
    .        *            precision floating point weights (usually has `.caffemodel` extension).
    .        * @param dst Path to destination model with updated weights.
    .        * @param layersTypes Set of layers types which parameters will be converted.
    .        *                    By default, converts only Convolutional and Fully-Connected layers'
    .        *                    weights.
    .        *
    .        * @note Shrinked model has no origin float32 weights so it can't be used
    .        *       in origin Caffe framework anymore. However the structure of data
    .        *       is taken from NVidia's Caffe fork: https://github.com/NVIDIA/caffe.
    .        *       So the resulting model may be used there.
    """
    pass

def writeTextGraph(model, output): # real signature unknown; restored from __doc__
    """
    writeTextGraph(model, output) -> None
    .   @brief Create a text representation for a binary network stored in protocol buffer format.
    .        *  @param[in] model  A path to binary network.
    .        *  @param[in] output A path to output text file to be created.
    .        *
    .        *  @note To reduce output file size, trained weights are not included.
    """
    pass

# no classes
