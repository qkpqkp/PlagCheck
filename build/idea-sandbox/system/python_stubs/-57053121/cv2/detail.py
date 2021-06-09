# encoding: utf-8
# module cv2.detail
# from C:\Users\Doly\Anaconda3\lib\site-packages\cv2\cv2.cp37-win_amd64.pyd
# by generator 1.147
# no doc
# no imports

# Variables with simple values

Blender_FEATHER = 1

BLENDER_FEATHER = 1

Blender_MULTI_BAND = 2

BLENDER_MULTI_BAND = 2

Blender_NO = 0

BLENDER_NO = 0

DpSeamFinder_COLOR = 0

DpSeamFinder_COLOR_GRAD = 1

DP_SEAM_FINDER_COLOR = 0

DP_SEAM_FINDER_COLOR_GRAD = 1

ExposureCompensator_CHANNELS = 3

ExposureCompensator_CHANNELS_BLOCKS = 4

ExposureCompensator_GAIN = 1

ExposureCompensator_GAIN_BLOCKS = 2

ExposureCompensator_NO = 0

EXPOSURE_COMPENSATOR_CHANNELS = 3

EXPOSURE_COMPENSATOR_CHANNELS_BLOCKS = 4

EXPOSURE_COMPENSATOR_GAIN = 1

EXPOSURE_COMPENSATOR_GAIN_BLOCKS = 2

EXPOSURE_COMPENSATOR_NO = 0

GraphCutSeamFinderBase_COST_COLOR = 0

GraphCutSeamFinderBase_COST_COLOR_GRAD = 1

GRAPH_CUT_SEAM_FINDER_BASE_COST_COLOR = 0

GRAPH_CUT_SEAM_FINDER_BASE_COST_COLOR_GRAD = 1

SeamFinder_DP_SEAM = 2

SeamFinder_NO = 0

SeamFinder_VORONOI_SEAM = 1

SEAM_FINDER_DP_SEAM = 2

SEAM_FINDER_NO = 0

SEAM_FINDER_VORONOI_SEAM = 1

TEST_CUSTOM = 0
TEST_EQ = 1
TEST_GE = 5
TEST_GT = 6
TEST_LE = 3
TEST_LT = 4
TEST_NE = 2

Timelapser_AS_IS = 0

TIMELAPSER_AS_IS = 0

Timelapser_CROP = 1

TIMELAPSER_CROP = 1

WAVE_CORRECT_HORIZ = 0
WAVE_CORRECT_VERT = 1

__loader__ = None

__spec__ = None

# functions

def BestOf2NearestMatcher_create(try_use_gpu=None, match_conf=None, num_matches_thresh1=None, num_matches_thresh2=None): # real signature unknown; restored from __doc__
    """
    BestOf2NearestMatcher_create([, try_use_gpu[, match_conf[, num_matches_thresh1[, num_matches_thresh2]]]]) -> retval
    .
    """
    pass

def Blender_createDefault(type, try_gpu=None): # real signature unknown; restored from __doc__
    """
    Blender_createDefault(type[, try_gpu]) -> retval
    .
    """
    pass

def calibrateRotatingCamera(Hs, K=None): # real signature unknown; restored from __doc__
    """
    calibrateRotatingCamera(Hs[, K]) -> retval, K
    .   @brief Estimates focal lengths for each given camera.
    .   
    .   @param features Features of images.
    .   @param pairwise_matches Matches between all image pairs.
    .   @param focals Estimated focal lengths for each camera.
    """
    pass

def computeImageFeatures(featuresFinder, images, masks=None): # real signature unknown; restored from __doc__
    """
    computeImageFeatures(featuresFinder, images[, masks]) -> features
    .   @brief
    .   
    .   @param featuresFinder
    .   @param images
    .   @param features
    .   @param masks
    """
    pass

def computeImageFeatures2(featuresFinder, image, mask=None): # real signature unknown; restored from __doc__
    """
    computeImageFeatures2(featuresFinder, image[, mask]) -> features
    .   @brief
    .   
    .   @param featuresFinder
    .   @param image
    .   @param features
    .   @param mask
    """
    pass

def createLaplacePyr(img, num_levels, pyr): # real signature unknown; restored from __doc__
    """
    createLaplacePyr(img, num_levels, pyr) -> pyr
    .
    """
    pass

def createLaplacePyrGpu(img, num_levels, pyr): # real signature unknown; restored from __doc__
    """
    createLaplacePyrGpu(img, num_levels, pyr) -> pyr
    .
    """
    pass

def createWeightMap(mask, sharpness, weight): # real signature unknown; restored from __doc__
    """
    createWeightMap(mask, sharpness, weight) -> weight
    .
    """
    pass

def ExposureCompensator_createDefault(type): # real signature unknown; restored from __doc__
    """
    ExposureCompensator_createDefault(type) -> retval
    .
    """
    pass

def focalsFromHomography(H, f0, f1, f0_ok, f1_ok): # real signature unknown; restored from __doc__
    """
    focalsFromHomography(H, f0, f1, f0_ok, f1_ok) -> None
    .   @brief Tries to estimate focal lengths from the given homography under the assumption that the camera
    .   undergoes rotations around its centre only.
    .   
    .   @param H Homography.
    .   @param f0 Estimated focal length along X axis.
    .   @param f1 Estimated focal length along Y axis.
    .   @param f0_ok True, if f0 was estimated successfully, false otherwise.
    .   @param f1_ok True, if f1 was estimated successfully, false otherwise.
    .   
    .   See "Construction of Panoramic Image Mosaics with Global and Local Alignment"
    .   by Heung-Yeung Shum and Richard Szeliski.
    """
    pass

def leaveBiggestComponent(features, pairwise_matches, conf_threshold): # real signature unknown; restored from __doc__
    """
    leaveBiggestComponent(features, pairwise_matches, conf_threshold) -> retval
    .
    """
    pass

def matchesGraphAsString(pathes, pairwise_matches, conf_threshold): # real signature unknown; restored from __doc__
    """
    matchesGraphAsString(pathes, pairwise_matches, conf_threshold) -> retval
    .
    """
    pass

def normalizeUsingWeightMap(weight, src): # real signature unknown; restored from __doc__
    """
    normalizeUsingWeightMap(weight, src) -> src
    .
    """
    pass

def overlapRoi(tl1, tl2, sz1, sz2, roi): # real signature unknown; restored from __doc__
    """
    overlapRoi(tl1, tl2, sz1, sz2, roi) -> retval
    .
    """
    pass

def restoreImageFromLaplacePyr(pyr): # real signature unknown; restored from __doc__
    """
    restoreImageFromLaplacePyr(pyr) -> pyr
    .
    """
    pass

def restoreImageFromLaplacePyrGpu(pyr): # real signature unknown; restored from __doc__
    """
    restoreImageFromLaplacePyrGpu(pyr) -> pyr
    .
    """
    pass

def resultRoi(corners, images): # real signature unknown; restored from __doc__
    """
    resultRoi(corners, images) -> retval
    .   
    
    
    
    resultRoi(corners, sizes) -> retval
    .
    """
    pass

def resultRoiIntersection(corners, sizes): # real signature unknown; restored from __doc__
    """
    resultRoiIntersection(corners, sizes) -> retval
    .
    """
    pass

def resultTl(corners): # real signature unknown; restored from __doc__
    """
    resultTl(corners) -> retval
    .
    """
    pass

def SeamFinder_createDefault(type): # real signature unknown; restored from __doc__
    """
    SeamFinder_createDefault(type) -> retval
    .
    """
    pass

def selectRandomSubset(count, size, subset): # real signature unknown; restored from __doc__
    """
    selectRandomSubset(count, size, subset) -> None
    .
    """
    pass

def stitchingLogLevel(): # real signature unknown; restored from __doc__
    """
    stitchingLogLevel() -> retval
    .
    """
    pass

def Timelapser_createDefault(type): # real signature unknown; restored from __doc__
    """
    Timelapser_createDefault(type) -> retval
    .
    """
    pass

def waveCorrect(rmats, kind): # real signature unknown; restored from __doc__
    """
    waveCorrect(rmats, kind) -> rmats
    .   @brief Tries to make panorama more horizontal (or vertical).
    .   
    .   @param rmats Camera rotation matrices.
    .   @param kind Correction kind, see detail::WaveCorrectKind.
    """
    pass

# no classes
