# encoding: utf-8
# module cv2.img_hash
# from C:\Users\Doly\Anaconda3\lib\site-packages\cv2\cv2.cp37-win_amd64.pyd
# by generator 1.147
# no doc
# no imports

# Variables with simple values

BLOCK_MEAN_HASH_MODE_0 = 0
BLOCK_MEAN_HASH_MODE_1 = 1

__loader__ = None

__spec__ = None

# functions

def averageHash(inputArr, outputArr=None): # real signature unknown; restored from __doc__
    """
    averageHash(inputArr[, outputArr]) -> outputArr
    .   @brief Calculates img_hash::AverageHash in one call
    .   @param inputArr input image want to compute hash value, type should be CV_8UC4, CV_8UC3 or CV_8UC1.
    .   @param outputArr Hash value of input, it will contain 16 hex decimal number, return type is CV_8U
    """
    pass

def AverageHash_create(): # real signature unknown; restored from __doc__
    """
    AverageHash_create() -> retval
    .
    """
    pass

def blockMeanHash(inputArr, outputArr=None, mode=None): # real signature unknown; restored from __doc__
    """
    blockMeanHash(inputArr[, outputArr[, mode]]) -> outputArr
    .   @brief Computes block mean hash of the input image
    .       @param inputArr input image want to compute hash value, type should be CV_8UC4, CV_8UC3 or CV_8UC1.
    .       @param outputArr Hash value of input, it will contain 16 hex decimal number, return type is CV_8U
    .       @param mode the mode
    """
    pass

def BlockMeanHash_create(mode=None): # real signature unknown; restored from __doc__
    """
    BlockMeanHash_create([, mode]) -> retval
    .
    """
    pass

def colorMomentHash(inputArr, outputArr=None): # real signature unknown; restored from __doc__
    """
    colorMomentHash(inputArr[, outputArr]) -> outputArr
    .   @brief Computes color moment hash of the input, the algorithm
    .       is come from the paper "Perceptual  Hashing  for  Color  Images
    .       Using  Invariant Moments"
    .       @param inputArr input image want to compute hash value,
    .       type should be CV_8UC4, CV_8UC3 or CV_8UC1.
    .       @param outputArr 42 hash values with type CV_64F(double)
    """
    pass

def ColorMomentHash_create(): # real signature unknown; restored from __doc__
    """
    ColorMomentHash_create() -> retval
    .
    """
    pass

def marrHildrethHash(inputArr, outputArr=None, alpha=None, scale=None): # real signature unknown; restored from __doc__
    """
    marrHildrethHash(inputArr[, outputArr[, alpha[, scale]]]) -> outputArr
    .   @brief Computes average hash value of the input image
    .       @param inputArr input image want to compute hash value,
    .       type should be CV_8UC4, CV_8UC3, CV_8UC1.
    .       @param outputArr Hash value of input, it will contain 16 hex
    .       decimal number, return type is CV_8U
    .       @param alpha int scale factor for marr wavelet (default=2).
    .       @param scale int level of scale factor (default = 1)
    """
    pass

def MarrHildrethHash_create(alpha=None, scale=None): # real signature unknown; restored from __doc__
    """
    MarrHildrethHash_create([, alpha[, scale]]) -> retval
    .   @param alpha int scale factor for marr wavelet (default=2).
    .           @param scale int level of scale factor (default = 1)
    """
    pass

def pHash(inputArr, outputArr=None): # real signature unknown; restored from __doc__
    """
    pHash(inputArr[, outputArr]) -> outputArr
    .   @brief Computes pHash value of the input image
    .       @param inputArr input image want to compute hash value,
    .        type should be CV_8UC4, CV_8UC3, CV_8UC1.
    .       @param outputArr Hash value of input, it will contain 8 uchar value
    """
    pass

def PHash_create(): # real signature unknown; restored from __doc__
    """
    PHash_create() -> retval
    .
    """
    pass

def radialVarianceHash(inputArr, outputArr=None, sigma=None, numOfAngleLine=None): # real signature unknown; restored from __doc__
    """
    radialVarianceHash(inputArr[, outputArr[, sigma[, numOfAngleLine]]]) -> outputArr
    .   @brief Computes radial variance hash of the input image
    .       @param inputArr input image want to compute hash value,
    .       type should be CV_8UC4, CV_8UC3, CV_8UC1.
    .       @param outputArr Hash value of input
    .       @param sigma Gaussian kernel standard deviation
    .       @param numOfAngleLine The number of angles to consider
    """
    pass

def RadialVarianceHash_create(sigma=None, numOfAngleLine=None): # real signature unknown; restored from __doc__
    """
    RadialVarianceHash_create([, sigma[, numOfAngleLine]]) -> retval
    .
    """
    pass

# no classes
