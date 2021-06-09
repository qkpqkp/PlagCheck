# encoding: utf-8
# module cv2.xfeatures2d
# from C:\Users\Doly\Anaconda3\lib\site-packages\cv2\cv2.cp37-win_amd64.pyd
# by generator 1.147
# no doc
# no imports

# Variables with simple values

DAISY_NRM_FULL = 102
DAISY_NRM_NONE = 100
DAISY_NRM_PARTIAL = 101
DAISY_NRM_SIFT = 103

PCTSignatures_GAUSSIAN = 1

PCTSIGNATURES_GAUSSIAN = 1

PCTSignatures_HEURISTIC = 2

PCTSIGNATURES_HEURISTIC = 2

PCTSignatures_L0_25 = 0

PCTSIGNATURES_L0_25 = 0

PCTSignatures_L0_5 = 1

PCTSIGNATURES_L0_5 = 1

PCTSignatures_L1 = 2

PCTSIGNATURES_L1 = 2

PCTSignatures_L2 = 3

PCTSIGNATURES_L2 = 3

PCTSignatures_L2SQUARED = 4

PCTSIGNATURES_L2SQUARED = 4

PCTSignatures_L5 = 5

PCTSIGNATURES_L5 = 5

PCTSignatures_L_INFINITY = 6

PCTSIGNATURES_L_INFINITY = 6

PCTSignatures_MINUS = 0

PCTSIGNATURES_MINUS = 0

PCTSignatures_NORMAL = 2

PCTSIGNATURES_NORMAL = 2

PCTSignatures_REGULAR = 1

PCTSIGNATURES_REGULAR = 1

PCTSignatures_UNIFORM = 0

PCTSIGNATURES_UNIFORM = 0

__loader__ = None

__spec__ = None

# functions

def BoostDesc_create(desc=None, use_scale_orientation=None, scale_factor=None): # real signature unknown; restored from __doc__
    """
    BoostDesc_create([, desc[, use_scale_orientation[, scale_factor]]]) -> retval
    .
    """
    pass

def BriefDescriptorExtractor_create(bytes=None, use_orientation=None): # real signature unknown; restored from __doc__
    """
    BriefDescriptorExtractor_create([, bytes[, use_orientation]]) -> retval
    .
    """
    pass

def DAISY_create(radius=None, q_radius=None, q_theta=None, q_hist=None, norm=None, H=None, interpolation=None, use_orientation=None): # real signature unknown; restored from __doc__
    """
    DAISY_create([, radius[, q_radius[, q_theta[, q_hist[, norm[, H[, interpolation[, use_orientation]]]]]]]]) -> retval
    .
    """
    pass

def FREAK_create(orientationNormalized=None, scaleNormalized=None, patternScale=None, nOctaves=None, selectedPairs=None): # real signature unknown; restored from __doc__
    """
    FREAK_create([, orientationNormalized[, scaleNormalized[, patternScale[, nOctaves[, selectedPairs]]]]]) -> retval
    .   @param orientationNormalized Enable orientation normalization.
    .       @param scaleNormalized Enable scale normalization.
    .       @param patternScale Scaling of the description pattern.
    .       @param nOctaves Number of octaves covered by the detected keypoints.
    .       @param selectedPairs (Optional) user defined selected pairs indexes,
    """
    pass

def HarrisLaplaceFeatureDetector_create(numOctaves=None, corn_thresh=None, DOG_thresh=None, maxCorners=None, num_layers=None): # real signature unknown; restored from __doc__
    """
    HarrisLaplaceFeatureDetector_create([, numOctaves[, corn_thresh[, DOG_thresh[, maxCorners[, num_layers]]]]]) -> retval
    .   * @brief Creates a new implementation instance.
    .        *
    .        * @param numOctaves the number of octaves in the scale-space pyramid
    .        * @param corn_thresh the threshold for the Harris cornerness measure
    .        * @param DOG_thresh the threshold for the Difference-of-Gaussians scale selection
    .        * @param maxCorners the maximum number of corners to consider
    .        * @param num_layers the number of intermediate scales per octave
    """
    pass

def LATCH_create(bytes=None, rotationInvariance=None, half_ssd_size=None, sigma=None): # real signature unknown; restored from __doc__
    """
    LATCH_create([, bytes[, rotationInvariance[, half_ssd_size[, sigma]]]]) -> retval
    .
    """
    pass

def LUCID_create(lucid_kernel=None, blur_kernel=None): # real signature unknown; restored from __doc__
    """
    LUCID_create([, lucid_kernel[, blur_kernel]]) -> retval
    .   * @param lucid_kernel kernel for descriptor construction, where 1=3x3, 2=5x5, 3=7x7 and so forth
    .        * @param blur_kernel kernel for blurring image prior to descriptor construction, where 1=3x3, 2=5x5, 3=7x7 and so forth
    """
    pass

def matchGMS(size1, size2, keypoints1, keypoints2, matches1to2, withRotation=None, withScale=None, thresholdFactor=None): # real signature unknown; restored from __doc__
    """
    matchGMS(size1, size2, keypoints1, keypoints2, matches1to2[, withRotation[, withScale[, thresholdFactor]]]) -> matchesGMS
    .   @brief GMS  (Grid-based Motion Statistics) feature matching strategy by @cite Bian2017gms .
    .       @param size1 Input size of image1.
    .       @param size2 Input size of image2.
    .       @param keypoints1 Input keypoints of image1.
    .       @param keypoints2 Input keypoints of image2.
    .       @param matches1to2 Input 1-nearest neighbor matches.
    .       @param matchesGMS Matches returned by the GMS matching strategy.
    .       @param withRotation Take rotation transformation into account.
    .       @param withScale Take scale transformation into account.
    .       @param thresholdFactor The higher, the less matches.
    .       @note
    .           Since GMS works well when the number of features is large, we recommend to use the ORB feature and set FastThreshold to 0 to get as many as possible features quickly.
    .           If matching results are not satisfying, please add more features. (We use 10000 for images with 640 X 480).
    .           If your images have big rotation and scale changes, please set withRotation or withScale to true.
    """
    pass

def PCTSignaturesSQFD_create(distanceFunction=None, similarityFunction=None, similarityParameter=None): # real signature unknown; restored from __doc__
    """
    PCTSignaturesSQFD_create([, distanceFunction[, similarityFunction[, similarityParameter]]]) -> retval
    .   * @brief Creates the algorithm instance using selected distance function,
    .       *       similarity function and similarity function parameter.
    .       * @param distanceFunction Distance function selector. Default: L2
    .       *       Available: L0_25, L0_5, L1, L2, L2SQUARED, L5, L_INFINITY
    .       * @param similarityFunction Similarity function selector. Default: HEURISTIC
    .       *       Available: MINUS, GAUSSIAN, HEURISTIC
    .       * @param similarityParameter Parameter of the similarity function.
    """
    pass

def PCTSignatures_create(initSampleCount=None, initSeedCount=None, pointDistribution=None): # real signature unknown; restored from __doc__
    """
    PCTSignatures_create([, initSampleCount[, initSeedCount[, pointDistribution]]]) -> retval
    .   * @brief Creates PCTSignatures algorithm using sample and seed count.
    .       *       It generates its own sets of sampling points and clusterization seed indexes.
    .       * @param initSampleCount Number of points used for image sampling.
    .       * @param initSeedCount Number of initial clusterization seeds.
    .       *       Must be lower or equal to initSampleCount
    .       * @param pointDistribution Distribution of generated points. Default: UNIFORM.
    .       *       Available: UNIFORM, REGULAR, NORMAL.
    .       * @return Created algorithm.
    
    
    
    PCTSignatures_create(initSamplingPoints, initSeedCount) -> retval
    .   * @brief Creates PCTSignatures algorithm using pre-generated sampling points
    .       *       and number of clusterization seeds. It uses the provided
    .       *       sampling points and generates its own clusterization seed indexes.
    .       * @param initSamplingPoints Sampling points used in image sampling.
    .       * @param initSeedCount Number of initial clusterization seeds.
    .       *       Must be lower or equal to initSamplingPoints.size().
    .       * @return Created algorithm.
    
    
    
    PCTSignatures_create(initSamplingPoints, initClusterSeedIndexes) -> retval
    .   * @brief Creates PCTSignatures algorithm using pre-generated sampling points
    .       *       and clusterization seeds indexes.
    .       * @param initSamplingPoints Sampling points used in image sampling.
    .       * @param initClusterSeedIndexes Indexes of initial clusterization seeds.
    .       *       Its size must be lower or equal to initSamplingPoints.size().
    .       * @return Created algorithm.
    """
    pass

def PCTSignatures_drawSignature(source, signature, result=None, radiusToShorterSideRatio=None, borderThickness=None): # real signature unknown; restored from __doc__
    """
    PCTSignatures_drawSignature(source, signature[, result[, radiusToShorterSideRatio[, borderThickness]]]) -> result
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

def PCTSignatures_generateInitPoints(initPoints, count, pointDistribution): # real signature unknown; restored from __doc__
    """
    PCTSignatures_generateInitPoints(initPoints, count, pointDistribution) -> None
    .   * @brief Generates initial sampling points according to selected point distribution.
    .       * @param initPoints Output vector where the generated points will be saved.
    .       * @param count Number of points to generate.
    .       * @param pointDistribution Point distribution selector.
    .       *       Available: UNIFORM, REGULAR, NORMAL.
    .       * @note Generated coordinates are in range [0..1)
    """
    pass

def SIFT_create(nfeatures=None, nOctaveLayers=None, contrastThreshold=None, edgeThreshold=None, sigma=None): # real signature unknown; restored from __doc__
    """
    SIFT_create([, nfeatures[, nOctaveLayers[, contrastThreshold[, edgeThreshold[, sigma]]]]]) -> retval
    .   @param nfeatures The number of best features to retain. The features are ranked by their scores
    .       (measured in SIFT algorithm as the local contrast)
    .   
    .       @param nOctaveLayers The number of layers in each octave. 3 is the value used in D. Lowe paper. The
    .       number of octaves is computed automatically from the image resolution.
    .   
    .       @param contrastThreshold The contrast threshold used to filter out weak features in semi-uniform
    .       (low-contrast) regions. The larger the threshold, the less features are produced by the detector.
    .   
    .       @param edgeThreshold The threshold used to filter out edge-like features. Note that the its meaning
    .       is different from the contrastThreshold, i.e. the larger the edgeThreshold, the less features are
    .       filtered out (more features are retained).
    .   
    .       @param sigma The sigma of the Gaussian applied to the input image at the octave \#0. If your image
    .       is captured with a weak camera with soft lenses, you might want to reduce the number.
    """
    pass

def StarDetector_create(maxSize=None, responseThreshold=None, lineThresholdProjected=None, lineThresholdBinarized=None, suppressNonmaxSize=None): # real signature unknown; restored from __doc__
    """
    StarDetector_create([, maxSize[, responseThreshold[, lineThresholdProjected[, lineThresholdBinarized[, suppressNonmaxSize]]]]]) -> retval
    .
    """
    pass

def SURF_create(hessianThreshold=None, nOctaves=None, nOctaveLayers=None, extended=None, upright=None): # real signature unknown; restored from __doc__
    """
    SURF_create([, hessianThreshold[, nOctaves[, nOctaveLayers[, extended[, upright]]]]]) -> retval
    .   @param hessianThreshold Threshold for hessian keypoint detector used in SURF.
    .       @param nOctaves Number of pyramid octaves the keypoint detector will use.
    .       @param nOctaveLayers Number of octave layers within each octave.
    .       @param extended Extended descriptor flag (true - use extended 128-element descriptors; false - use
    .       64-element descriptors).
    .       @param upright Up-right or rotated features flag (true - do not compute orientation of features;
    .       false - compute orientation).
    """
    pass

def VGG_create(desc=None, isigma=None, img_normalize=None, use_scale_orientation=None, scale_factor=None, dsc_normalize=None): # real signature unknown; restored from __doc__
    """
    VGG_create([, desc[, isigma[, img_normalize[, use_scale_orientation[, scale_factor[, dsc_normalize]]]]]]) -> retval
    .
    """
    pass

# no classes
