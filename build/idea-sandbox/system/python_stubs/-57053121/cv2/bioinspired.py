# encoding: utf-8
# module cv2.bioinspired
# from C:\Users\Doly\Anaconda3\lib\site-packages\cv2\cv2.cp37-win_amd64.pyd
# by generator 1.147
# no doc
# no imports

# Variables with simple values

RETINA_COLOR_BAYER = 2
RETINA_COLOR_DIAGONAL = 1
RETINA_COLOR_RANDOM = 0

__loader__ = None

__spec__ = None

# functions

def RetinaFastToneMapping_create(inputSize): # real signature unknown; restored from __doc__
    """
    RetinaFastToneMapping_create(inputSize) -> retval
    .
    """
    pass

def Retina_create(inputSize): # real signature unknown; restored from __doc__
    """
    Retina_create(inputSize) -> retval
    .   @overload
    
    
    
    Retina_create(inputSize, colorMode[, colorSamplingMethod[, useRetinaLogSampling[, reductionFactor[, samplingStrenght]]]]) -> retval
    .   @brief Constructors from standardized interfaces : retreive a smart pointer to a Retina instance
    .   
    .       @param inputSize the input frame size
    .       @param colorMode the chosen processing mode : with or without color processing
    .       @param colorSamplingMethod specifies which kind of color sampling will be used :
    .       -   cv::bioinspired::RETINA_COLOR_RANDOM: each pixel position is either R, G or B in a random choice
    .       -   cv::bioinspired::RETINA_COLOR_DIAGONAL: color sampling is RGBRGBRGB..., line 2 BRGBRGBRG..., line 3, GBRGBRGBR...
    .       -   cv::bioinspired::RETINA_COLOR_BAYER: standard bayer sampling
    .       @param useRetinaLogSampling activate retina log sampling, if true, the 2 following parameters can
    .       be used
    .       @param reductionFactor only usefull if param useRetinaLogSampling=true, specifies the reduction
    .       factor of the output frame (as the center (fovea) is high resolution and corners can be
    .       underscaled, then a reduction of the output is allowed without precision leak
    .       @param samplingStrenght only usefull if param useRetinaLogSampling=true, specifies the strenght of
    .       the log scale that is applied
    """
    pass

def TransientAreasSegmentationModule_create(inputSize): # real signature unknown; restored from __doc__
    """
    TransientAreasSegmentationModule_create(inputSize) -> retval
    .   @brief allocator
    .       @param inputSize : size of the images input to segment (output will be the same size)
    """
    pass

# no classes
