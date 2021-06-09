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


class xfeatures2d_PCTSignatures(__cv2.Algorithm):
    # no doc
    def computeSignature(self, image, signature=None): # real signature unknown; restored from __doc__
        """
        computeSignature(image[, signature]) -> signature
        .   * @brief Computes signature of given image.
        .       * @param image Input image of CV_8U type.
        .       * @param signature Output computed signature.
        """
        pass

    def computeSignatures(self, images, signatures): # real signature unknown; restored from __doc__
        """
        computeSignatures(images, signatures) -> None
        .   * @brief Computes signatures for multiple images in parallel.
        .       * @param images Vector of input images of CV_8U type.
        .       * @param signatures Vector of computed signatures.
        """
        pass

    def create(self, initSampleCount=None, initSeedCount=None, pointDistribution=None): # real signature unknown; restored from __doc__
        """
        create([, initSampleCount[, initSeedCount[, pointDistribution]]]) -> retval
        .   * @brief Creates PCTSignatures algorithm using sample and seed count.
        .       *       It generates its own sets of sampling points and clusterization seed indexes.
        .       * @param initSampleCount Number of points used for image sampling.
        .       * @param initSeedCount Number of initial clusterization seeds.
        .       *       Must be lower or equal to initSampleCount
        .       * @param pointDistribution Distribution of generated points. Default: UNIFORM.
        .       *       Available: UNIFORM, REGULAR, NORMAL.
        .       * @return Created algorithm.
        
        
        
        create(initSamplingPoints, initSeedCount) -> retval
        .   * @brief Creates PCTSignatures algorithm using pre-generated sampling points
        .       *       and number of clusterization seeds. It uses the provided
        .       *       sampling points and generates its own clusterization seed indexes.
        .       * @param initSamplingPoints Sampling points used in image sampling.
        .       * @param initSeedCount Number of initial clusterization seeds.
        .       *       Must be lower or equal to initSamplingPoints.size().
        .       * @return Created algorithm.
        
        
        
        create(initSamplingPoints, initClusterSeedIndexes) -> retval
        .   * @brief Creates PCTSignatures algorithm using pre-generated sampling points
        .       *       and clusterization seeds indexes.
        .       * @param initSamplingPoints Sampling points used in image sampling.
        .       * @param initClusterSeedIndexes Indexes of initial clusterization seeds.
        .       *       Its size must be lower or equal to initSamplingPoints.size().
        .       * @return Created algorithm.
        """
        pass

    def drawSignature(self, source, signature, result=None, radiusToShorterSideRatio=None, borderThickness=None): # real signature unknown; restored from __doc__
        """
        drawSignature(source, signature[, result[, radiusToShorterSideRatio[, borderThickness]]]) -> result
        .   * @brief Draws signature in the source image and outputs the result.
        .       *       Signatures are visualized as a circle
        .       *       with radius based on signature weight
        .       *       and color based on signature color.
        .       *       Contrast and entropy are not visualized.
        .       * @param source Source image.
        .       * @param signature Image signature.
        .       * @param result Output result.
        .       * @param radiusToShorterSideRatio Determines maximal radius of signature in the output image.
        .       * @param borderThickness Border thickness of the visualized signature.
        """
        pass

    def generateInitPoints(self, initPoints, count, pointDistribution): # real signature unknown; restored from __doc__
        """
        generateInitPoints(initPoints, count, pointDistribution) -> None
        .   * @brief Generates initial sampling points according to selected point distribution.
        .       * @param initPoints Output vector where the generated points will be saved.
        .       * @param count Number of points to generate.
        .       * @param pointDistribution Point distribution selector.
        .       *       Available: UNIFORM, REGULAR, NORMAL.
        .       * @note Generated coordinates are in range [0..1)
        """
        pass

    def getClusterMinSize(self): # real signature unknown; restored from __doc__
        """
        getClusterMinSize() -> retval
        .   * @brief This parameter multiplied by the index of iteration gives lower limit for cluster size.
        .       *       Clusters containing fewer points than specified by the limit have their centroid dismissed
        .       *       and points are reassigned.
        """
        pass

    def getDistanceFunction(self): # real signature unknown; restored from __doc__
        """
        getDistanceFunction() -> retval
        .   * @brief Distance function selector used for measuring distance between two points in k-means.
        """
        pass

    def getDropThreshold(self): # real signature unknown; restored from __doc__
        """
        getDropThreshold() -> retval
        .   * @brief Remove centroids in k-means whose weight is lesser or equal to given threshold.
        """
        pass

    def getGrayscaleBits(self): # real signature unknown; restored from __doc__
        """
        getGrayscaleBits() -> retval
        .   * @brief Color resolution of the greyscale bitmap represented in allocated bits
        .       *       (i.e., value 4 means that 16 shades of grey are used).
        .       *       The greyscale bitmap is used for computing contrast and entropy values.
        """
        pass

    def getInitSeedCount(self): # real signature unknown; restored from __doc__
        """
        getInitSeedCount() -> retval
        .   * @brief Number of initial seeds (initial number of clusters) for the k-means algorithm.
        """
        pass

    def getInitSeedIndexes(self): # real signature unknown; restored from __doc__
        """
        getInitSeedIndexes() -> retval
        .   * @brief Initial seeds (initial number of clusters) for the k-means algorithm.
        """
        pass

    def getIterationCount(self): # real signature unknown; restored from __doc__
        """
        getIterationCount() -> retval
        .   * @brief Number of iterations of the k-means clustering.
        .       *       We use fixed number of iterations, since the modified clustering is pruning clusters
        .       *       (not iteratively refining k clusters).
        """
        pass

    def getJoiningDistance(self): # real signature unknown; restored from __doc__
        """
        getJoiningDistance() -> retval
        .   * @brief Threshold euclidean distance between two centroids.
        .       *       If two cluster centers are closer than this distance,
        .       *       one of the centroid is dismissed and points are reassigned.
        """
        pass

    def getMaxClustersCount(self): # real signature unknown; restored from __doc__
        """
        getMaxClustersCount() -> retval
        .   * @brief Maximal number of generated clusters. If the number is exceeded,
        .       *       the clusters are sorted by their weights and the smallest clusters are cropped.
        """
        pass

    def getSampleCount(self): # real signature unknown; restored from __doc__
        """
        getSampleCount() -> retval
        .   * @brief Number of initial samples taken from the image.
        """
        pass

    def getSamplingPoints(self): # real signature unknown; restored from __doc__
        """
        getSamplingPoints() -> retval
        .   * @brief Initial samples taken from the image.
        .       *       These sampled features become the input for clustering.
        """
        pass

    def getWeightA(self): # real signature unknown; restored from __doc__
        """
        getWeightA() -> retval
        .   * @brief Weights (multiplicative constants) that linearly stretch individual axes of the feature space
        .       *       (x,y = position; L,a,b = color in CIE Lab space; c = contrast. e = entropy)
        """
        pass

    def getWeightB(self): # real signature unknown; restored from __doc__
        """
        getWeightB() -> retval
        .   * @brief Weights (multiplicative constants) that linearly stretch individual axes of the feature space
        .       *       (x,y = position; L,a,b = color in CIE Lab space; c = contrast. e = entropy)
        """
        pass

    def getWeightContrast(self): # real signature unknown; restored from __doc__
        """
        getWeightContrast() -> retval
        .   * @brief Weights (multiplicative constants) that linearly stretch individual axes of the feature space
        .       *       (x,y = position; L,a,b = color in CIE Lab space; c = contrast. e = entropy)
        """
        pass

    def getWeightEntropy(self): # real signature unknown; restored from __doc__
        """
        getWeightEntropy() -> retval
        .   * @brief Weights (multiplicative constants) that linearly stretch individual axes of the feature space
        .       *       (x,y = position; L,a,b = color in CIE Lab space; c = contrast. e = entropy)
        """
        pass

    def getWeightL(self): # real signature unknown; restored from __doc__
        """
        getWeightL() -> retval
        .   * @brief Weights (multiplicative constants) that linearly stretch individual axes of the feature space
        .       *       (x,y = position; L,a,b = color in CIE Lab space; c = contrast. e = entropy)
        """
        pass

    def getWeightX(self): # real signature unknown; restored from __doc__
        """
        getWeightX() -> retval
        .   * @brief Weights (multiplicative constants) that linearly stretch individual axes of the feature space
        .       *       (x,y = position; L,a,b = color in CIE Lab space; c = contrast. e = entropy)
        """
        pass

    def getWeightY(self): # real signature unknown; restored from __doc__
        """
        getWeightY() -> retval
        .   * @brief Weights (multiplicative constants) that linearly stretch individual axes of the feature space
        .       *       (x,y = position; L,a,b = color in CIE Lab space; c = contrast. e = entropy)
        """
        pass

    def getWindowRadius(self): # real signature unknown; restored from __doc__
        """
        getWindowRadius() -> retval
        .   * @brief Size of the texture sampling window used to compute contrast and entropy
        .       *       (center of the window is always in the pixel selected by x,y coordinates
        .       *       of the corresponding feature sample).
        """
        pass

    def setClusterMinSize(self, clusterMinSize): # real signature unknown; restored from __doc__
        """
        setClusterMinSize(clusterMinSize) -> None
        .   * @brief This parameter multiplied by the index of iteration gives lower limit for cluster size.
        .       *       Clusters containing fewer points than specified by the limit have their centroid dismissed
        .       *       and points are reassigned.
        """
        pass

    def setDistanceFunction(self, distanceFunction): # real signature unknown; restored from __doc__
        """
        setDistanceFunction(distanceFunction) -> None
        .   * @brief Distance function selector used for measuring distance between two points in k-means.
        .       *       Available: L0_25, L0_5, L1, L2, L2SQUARED, L5, L_INFINITY.
        """
        pass

    def setDropThreshold(self, dropThreshold): # real signature unknown; restored from __doc__
        """
        setDropThreshold(dropThreshold) -> None
        .   * @brief Remove centroids in k-means whose weight is lesser or equal to given threshold.
        """
        pass

    def setGrayscaleBits(self, grayscaleBits): # real signature unknown; restored from __doc__
        """
        setGrayscaleBits(grayscaleBits) -> None
        .   * @brief Color resolution of the greyscale bitmap represented in allocated bits
        .       *       (i.e., value 4 means that 16 shades of grey are used).
        .       *       The greyscale bitmap is used for computing contrast and entropy values.
        """
        pass

    def setInitSeedIndexes(self, initSeedIndexes): # real signature unknown; restored from __doc__
        """
        setInitSeedIndexes(initSeedIndexes) -> None
        .   * @brief Initial seed indexes for the k-means algorithm.
        """
        pass

    def setIterationCount(self, iterationCount): # real signature unknown; restored from __doc__
        """
        setIterationCount(iterationCount) -> None
        .   * @brief Number of iterations of the k-means clustering.
        .       *       We use fixed number of iterations, since the modified clustering is pruning clusters
        .       *       (not iteratively refining k clusters).
        """
        pass

    def setJoiningDistance(self, joiningDistance): # real signature unknown; restored from __doc__
        """
        setJoiningDistance(joiningDistance) -> None
        .   * @brief Threshold euclidean distance between two centroids.
        .       *       If two cluster centers are closer than this distance,
        .       *       one of the centroid is dismissed and points are reassigned.
        """
        pass

    def setMaxClustersCount(self, maxClustersCount): # real signature unknown; restored from __doc__
        """
        setMaxClustersCount(maxClustersCount) -> None
        .   * @brief Maximal number of generated clusters. If the number is exceeded,
        .       *       the clusters are sorted by their weights and the smallest clusters are cropped.
        """
        pass

    def setSamplingPoints(self, samplingPoints): # real signature unknown; restored from __doc__
        """
        setSamplingPoints(samplingPoints) -> None
        .   * @brief Sets sampling points used to sample the input image.
        .       * @param samplingPoints Vector of sampling points in range [0..1)
        .       * @note Number of sampling points must be greater or equal to clusterization seed count.
        """
        pass

    def setTranslation(self, idx, value): # real signature unknown; restored from __doc__
        """
        setTranslation(idx, value) -> None
        .   * @brief Translations of the individual axes of the feature space.
        .       * @param idx ID of the translation
        .       * @param value Value of the translation
        .       * @note
        .       *       WEIGHT_IDX = 0;
        .       *       X_IDX = 1;
        .       *       Y_IDX = 2;
        .       *       L_IDX = 3;
        .       *       A_IDX = 4;
        .       *       B_IDX = 5;
        .       *       CONTRAST_IDX = 6;
        .       *       ENTROPY_IDX = 7;
        """
        pass

    def setTranslations(self, translations): # real signature unknown; restored from __doc__
        """
        setTranslations(translations) -> None
        .   * @brief Translations of the individual axes of the feature space.
        .       * @param translations Values of all translations.
        .       * @note
        .       *       WEIGHT_IDX = 0;
        .       *       X_IDX = 1;
        .       *       Y_IDX = 2;
        .       *       L_IDX = 3;
        .       *       A_IDX = 4;
        .       *       B_IDX = 5;
        .       *       CONTRAST_IDX = 6;
        .       *       ENTROPY_IDX = 7;
        """
        pass

    def setWeight(self, idx, value): # real signature unknown; restored from __doc__
        """
        setWeight(idx, value) -> None
        .   * @brief Weights (multiplicative constants) that linearly stretch individual axes of the feature space.
        .       * @param idx ID of the weight
        .       * @param value Value of the weight
        .       * @note
        .       *       WEIGHT_IDX = 0;
        .       *       X_IDX = 1;
        .       *       Y_IDX = 2;
        .       *       L_IDX = 3;
        .       *       A_IDX = 4;
        .       *       B_IDX = 5;
        .       *       CONTRAST_IDX = 6;
        .       *       ENTROPY_IDX = 7;
        """
        pass

    def setWeightA(self, weight): # real signature unknown; restored from __doc__
        """
        setWeightA(weight) -> None
        .   * @brief Weights (multiplicative constants) that linearly stretch individual axes of the feature space
        .       *       (x,y = position; L,a,b = color in CIE Lab space; c = contrast. e = entropy)
        """
        pass

    def setWeightB(self, weight): # real signature unknown; restored from __doc__
        """
        setWeightB(weight) -> None
        .   * @brief Weights (multiplicative constants) that linearly stretch individual axes of the feature space
        .       *       (x,y = position; L,a,b = color in CIE Lab space; c = contrast. e = entropy)
        """
        pass

    def setWeightContrast(self, weight): # real signature unknown; restored from __doc__
        """
        setWeightContrast(weight) -> None
        .   * @brief Weights (multiplicative constants) that linearly stretch individual axes of the feature space
        .       *       (x,y = position; L,a,b = color in CIE Lab space; c = contrast. e = entropy)
        """
        pass

    def setWeightEntropy(self, weight): # real signature unknown; restored from __doc__
        """
        setWeightEntropy(weight) -> None
        .   * @brief Weights (multiplicative constants) that linearly stretch individual axes of the feature space
        .       *       (x,y = position; L,a,b = color in CIE Lab space; c = contrast. e = entropy)
        """
        pass

    def setWeightL(self, weight): # real signature unknown; restored from __doc__
        """
        setWeightL(weight) -> None
        .   * @brief Weights (multiplicative constants) that linearly stretch individual axes of the feature space
        .       *       (x,y = position; L,a,b = color in CIE Lab space; c = contrast. e = entropy)
        """
        pass

    def setWeights(self, weights): # real signature unknown; restored from __doc__
        """
        setWeights(weights) -> None
        .   * @brief Weights (multiplicative constants) that linearly stretch individual axes of the feature space.
        .       * @param weights Values of all weights.
        .       * @note
        .       *       WEIGHT_IDX = 0;
        .       *       X_IDX = 1;
        .       *       Y_IDX = 2;
        .       *       L_IDX = 3;
        .       *       A_IDX = 4;
        .       *       B_IDX = 5;
        .       *       CONTRAST_IDX = 6;
        .       *       ENTROPY_IDX = 7;
        """
        pass

    def setWeightX(self, weight): # real signature unknown; restored from __doc__
        """
        setWeightX(weight) -> None
        .   * @brief Weights (multiplicative constants) that linearly stretch individual axes of the feature space
        .       *       (x,y = position; L,a,b = color in CIE Lab space; c = contrast. e = entropy)
        """
        pass

    def setWeightY(self, weight): # real signature unknown; restored from __doc__
        """
        setWeightY(weight) -> None
        .   * @brief Weights (multiplicative constants) that linearly stretch individual axes of the feature space
        .       *       (x,y = position; L,a,b = color in CIE Lab space; c = contrast. e = entropy)
        """
        pass

    def setWindowRadius(self, radius): # real signature unknown; restored from __doc__
        """
        setWindowRadius(radius) -> None
        .   * @brief Size of the texture sampling window used to compute contrast and entropy
        .       *       (center of the window is always in the pixel selected by x,y coordinates
        .       *       of the corresponding feature sample).
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


