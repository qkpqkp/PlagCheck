# encoding: utf-8
# module cv2.quality
# from C:\Users\Doly\Anaconda3\lib\site-packages\cv2\cv2.cp37-win_amd64.pyd
# by generator 1.147
# no doc
# no imports

# Variables with simple values

__loader__ = None

__spec__ = None

# functions

def QualityBRISQUE_compute(img, model_file_path, range_file_path): # real signature unknown; restored from __doc__
    """
    QualityBRISQUE_compute(img, model_file_path, range_file_path) -> retval
    .   @brief static method for computing quality
    .       @param img image for which to compute quality
    .       @param model_file_path cv::String which contains a path to the BRISQUE model data, eg. /path/to/brisque_model_live.yml
    .       @param range_file_path cv::String which contains a path to the BRISQUE range data, eg. /path/to/brisque_range_live.yml
    .       @returns cv::Scalar with the score in the first element.  The score ranges from 0 (best quality) to 100 (worst quality)
    """
    pass

def QualityBRISQUE_computeFeatures(img, features=None): # real signature unknown; restored from __doc__
    """
    QualityBRISQUE_computeFeatures(img[, features]) -> features
    .   @brief static method for computing image features used by the BRISQUE algorithm
    .       @param img image (BGR(A) or grayscale) for which to compute features
    .       @param features output row vector of features to cv::Mat or cv::UMat
    """
    pass

def QualityBRISQUE_create(model_file_path, range_file_path): # real signature unknown; restored from __doc__
    """
    QualityBRISQUE_create(model_file_path, range_file_path) -> retval
    .   @brief Create an object which calculates quality
    .       @param model_file_path cv::String which contains a path to the BRISQUE model data, eg. /path/to/brisque_model_live.yml
    .       @param range_file_path cv::String which contains a path to the BRISQUE range data, eg. /path/to/brisque_range_live.yml
    
    
    
    QualityBRISQUE_create(model, range) -> retval
    .   @brief Create an object which calculates quality
    .       @param model cv::Ptr<cv::ml::SVM> which contains a loaded BRISQUE model
    .       @param range cv::Mat which contains BRISQUE range data
    """
    pass

def QualityGMSD_compute(ref, cmp, qualityMap=None): # real signature unknown; restored from __doc__
    """
    QualityGMSD_compute(ref, cmp[, qualityMap]) -> retval, qualityMap
    .   @brief static method for computing quality
    .       @param ref reference image
    .       @param cmp comparison image
    .       @param qualityMap output quality map, or cv::noArray()
    .       @returns cv::Scalar with per-channel quality value.  Values range from 0 (worst) to 1 (best)
    """
    pass

def QualityGMSD_create(ref): # real signature unknown; restored from __doc__
    """
    QualityGMSD_create(ref) -> retval
    .   @brief Create an object which calculates image quality
    .       @param ref reference image
    """
    pass

def QualityMSE_compute(ref, cmp, qualityMap=None): # real signature unknown; restored from __doc__
    """
    QualityMSE_compute(ref, cmp[, qualityMap]) -> retval, qualityMap
    .   @brief static method for computing quality
    .       @param ref reference image
    .       @param cmp comparison image=
    .       @param qualityMap output quality map, or cv::noArray()
    .       @returns cv::Scalar with per-channel quality values.  Values range from 0 (best) to max float (worst)
    """
    pass

def QualityMSE_create(ref): # real signature unknown; restored from __doc__
    """
    QualityMSE_create(ref) -> retval
    .   @brief Create an object which calculates quality
    .       @param ref input image to use as the reference for comparison
    """
    pass

def QualityPSNR_compute(ref, cmp, qualityMap=None, maxPixelValue=None): # real signature unknown; restored from __doc__
    """
    QualityPSNR_compute(ref, cmp[, qualityMap[, maxPixelValue]]) -> retval, qualityMap
    .   @brief static method for computing quality
    .       @param ref reference image
    .       @param cmp comparison image
    .       @param qualityMap output quality map, or cv::noArray()
    .       @param maxPixelValue maximum per-channel value for any individual pixel; eg 255 for uint8 image
    .       @returns PSNR value, or std::numeric_limits<double>::infinity() if the MSE between the two images == 0
    """
    pass

def QualityPSNR_create(ref, maxPixelValue=None): # real signature unknown; restored from __doc__
    """
    QualityPSNR_create(ref[, maxPixelValue]) -> retval
    .   @brief Create an object which calculates quality
    .       @param ref input image to use as the source for comparison
    .       @param maxPixelValue maximum per-channel value for any individual pixel; eg 255 for uint8 image
    """
    pass

def QualitySSIM_compute(ref, cmp, qualityMap=None): # real signature unknown; restored from __doc__
    """
    QualitySSIM_compute(ref, cmp[, qualityMap]) -> retval, qualityMap
    .   @brief static method for computing quality
    .       @param ref reference image
    .       @param cmp comparison image
    .       @param qualityMap output quality map, or cv::noArray()
    .       @returns cv::Scalar with per-channel quality values.  Values range from 0 (worst) to 1 (best)
    """
    pass

def QualitySSIM_create(ref): # real signature unknown; restored from __doc__
    """
    QualitySSIM_create(ref) -> retval
    .   @brief Create an object which calculates quality
    .       @param ref input image to use as the reference image for comparison
    """
    pass

# no classes
