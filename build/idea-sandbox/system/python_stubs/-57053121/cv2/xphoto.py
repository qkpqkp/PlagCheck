# encoding: utf-8
# module cv2.xphoto
# from C:\Users\Doly\Anaconda3\lib\site-packages\cv2\cv2.cp37-win_amd64.pyd
# by generator 1.147
# no doc
# no imports

# Variables with simple values

BM3D_STEP1 = 1
BM3D_STEP2 = 2
BM3D_STEPALL = 0

HAAR = 0

INPAINT_SHIFTMAP = 0

__loader__ = None

__spec__ = None

# functions

def applyChannelGains(src, gainB, gainG, gainR, dst=None): # real signature unknown; restored from __doc__
    """
    applyChannelGains(src, gainB, gainG, gainR[, dst]) -> dst
    .   @brief Implements an efficient fixed-point approximation for applying channel gains, which is
    .       the last step of multiple white balance algorithms.
    .   
    .   @param src Input three-channel image in the BGR color space (either CV_8UC3 or CV_16UC3)
    .   @param dst Output image of the same size and type as src.
    .   @param gainB gain for the B channel
    .   @param gainG gain for the G channel
    .   @param gainR gain for the R channel
    """
    pass

def bm3dDenoising(src, dstStep1, dstStep2=None, h=None, templateWindowSize=None, searchWindowSize=None, blockMatchingStep1=None, blockMatchingStep2=None, groupSize=None, slidingStep=None, beta=None, normType=None, step=None, transformType=None): # real signature unknown; restored from __doc__
    """
    bm3dDenoising(src, dstStep1[, dstStep2[, h[, templateWindowSize[, searchWindowSize[, blockMatchingStep1[, blockMatchingStep2[, groupSize[, slidingStep[, beta[, normType[, step[, transformType]]]]]]]]]]]]) -> dstStep1, dstStep2
    .   @brief Performs image denoising using the Block-Matching and 3D-filtering algorithm
    .           <http://www.cs.tut.fi/~foi/GCF-BM3D/BM3D_TIP_2007.pdf> with several computational
    .           optimizations. Noise expected to be a gaussian white noise.
    .   
    .           @param src Input 8-bit or 16-bit 1-channel image.
    .           @param dstStep1 Output image of the first step of BM3D with the same size and type as src.
    .           @param dstStep2 Output image of the second step of BM3D with the same size and type as src.
    .           @param h Parameter regulating filter strength. Big h value perfectly removes noise but also
    .           removes image details, smaller h value preserves details but also preserves some noise.
    .           @param templateWindowSize Size in pixels of the template patch that is used for block-matching.
    .           Should be power of 2.
    .           @param searchWindowSize Size in pixels of the window that is used to perform block-matching.
    .           Affect performance linearly: greater searchWindowsSize - greater denoising time.
    .           Must be larger than templateWindowSize.
    .           @param blockMatchingStep1 Block matching threshold for the first step of BM3D (hard thresholding),
    .           i.e. maximum distance for which two blocks are considered similar.
    .           Value expressed in euclidean distance.
    .           @param blockMatchingStep2 Block matching threshold for the second step of BM3D (Wiener filtering),
    .           i.e. maximum distance for which two blocks are considered similar.
    .           Value expressed in euclidean distance.
    .           @param groupSize Maximum size of the 3D group for collaborative filtering.
    .           @param slidingStep Sliding step to process every next reference block.
    .           @param beta Kaiser window parameter that affects the sidelobe attenuation of the transform of the
    .           window. Kaiser window is used in order to reduce border effects. To prevent usage of the window,
    .           set beta to zero.
    .           @param normType Norm used to calculate distance between blocks. L2 is slower than L1
    .           but yields more accurate results.
    .           @param step Step of BM3D to be executed. Possible variants are: step 1, step 2, both steps.
    .           @param transformType Type of the orthogonal transform used in collaborative filtering step.
    .           Currently only Haar transform is supported.
    .   
    .           This function expected to be applied to grayscale images. Advanced usage of this function
    .           can be manual denoising of colored image in different colorspaces.
    .   
    .           @sa
    .           fastNlMeansDenoising
    
    
    
    bm3dDenoising(src[, dst[, h[, templateWindowSize[, searchWindowSize[, blockMatchingStep1[, blockMatchingStep2[, groupSize[, slidingStep[, beta[, normType[, step[, transformType]]]]]]]]]]]]) -> dst
    .   @brief Performs image denoising using the Block-Matching and 3D-filtering algorithm
    .           <http://www.cs.tut.fi/~foi/GCF-BM3D/BM3D_TIP_2007.pdf> with several computational
    .           optimizations. Noise expected to be a gaussian white noise.
    .   
    .           @param src Input 8-bit or 16-bit 1-channel image.
    .           @param dst Output image with the same size and type as src.
    .           @param h Parameter regulating filter strength. Big h value perfectly removes noise but also
    .           removes image details, smaller h value preserves details but also preserves some noise.
    .           @param templateWindowSize Size in pixels of the template patch that is used for block-matching.
    .           Should be power of 2.
    .           @param searchWindowSize Size in pixels of the window that is used to perform block-matching.
    .           Affect performance linearly: greater searchWindowsSize - greater denoising time.
    .           Must be larger than templateWindowSize.
    .           @param blockMatchingStep1 Block matching threshold for the first step of BM3D (hard thresholding),
    .           i.e. maximum distance for which two blocks are considered similar.
    .           Value expressed in euclidean distance.
    .           @param blockMatchingStep2 Block matching threshold for the second step of BM3D (Wiener filtering),
    .           i.e. maximum distance for which two blocks are considered similar.
    .           Value expressed in euclidean distance.
    .           @param groupSize Maximum size of the 3D group for collaborative filtering.
    .           @param slidingStep Sliding step to process every next reference block.
    .           @param beta Kaiser window parameter that affects the sidelobe attenuation of the transform of the
    .           window. Kaiser window is used in order to reduce border effects. To prevent usage of the window,
    .           set beta to zero.
    .           @param normType Norm used to calculate distance between blocks. L2 is slower than L1
    .           but yields more accurate results.
    .           @param step Step of BM3D to be executed. Allowed are only BM3D_STEP1 and BM3D_STEPALL.
    .           BM3D_STEP2 is not allowed as it requires basic estimate to be present.
    .           @param transformType Type of the orthogonal transform used in collaborative filtering step.
    .           Currently only Haar transform is supported.
    .   
    .           This function expected to be applied to grayscale images. Advanced usage of this function
    .           can be manual denoising of colored image in different colorspaces.
    .   
    .           @sa
    .           fastNlMeansDenoising
    """
    pass

def createGrayworldWB(): # real signature unknown; restored from __doc__
    """
    createGrayworldWB() -> retval
    .   @brief Creates an instance of GrayworldWB
    """
    pass

def createLearningBasedWB(path_to_model=None): # real signature unknown; restored from __doc__
    """
    createLearningBasedWB([, path_to_model]) -> retval
    .   @brief Creates an instance of LearningBasedWB
    .   
    .   @param path_to_model Path to a .yml file with the model. If not specified, the default model is used
    """
    pass

def createSimpleWB(): # real signature unknown; restored from __doc__
    """
    createSimpleWB() -> retval
    .   @brief Creates an instance of SimpleWB
    """
    pass

def createTonemapDurand(gamma=None, contrast=None, saturation=None, sigma_space=None, sigma_color=None): # real signature unknown; restored from __doc__
    """
    createTonemapDurand([, gamma[, contrast[, saturation[, sigma_space[, sigma_color]]]]]) -> retval
    .   @brief Creates TonemapDurand object
    .   
    .   You need to set the OPENCV_ENABLE_NONFREE option in cmake to use those. Use them at your own risk.
    .   
    .   @param gamma gamma value for gamma correction. See createTonemap
    .   @param contrast resulting contrast on logarithmic scale, i. e. log(max / min), where max and min
    .   are maximum and minimum luminance values of the resulting image.
    .   @param saturation saturation enhancement value. See createTonemapDrago
    .   @param sigma_space bilateral filter sigma in color space
    .   @param sigma_color bilateral filter sigma in coordinate space
    """
    pass

def dctDenoising(src, dst, sigma, psize=None): # real signature unknown; restored from __doc__
    """
    dctDenoising(src, dst, sigma[, psize]) -> None
    .   @brief The function implements simple dct-based denoising
    .   
    .       <http://www.ipol.im/pub/art/2011/ys-dct/>.
    .       @param src source image
    .       @param dst destination image
    .       @param sigma expected noise standard deviation
    .       @param psize size of block side where dct is computed
    .   
    .       @sa
    .          fastNlMeansDenoising
    """
    pass

def inpaint(src, mask, dst, algorithmType): # real signature unknown; restored from __doc__
    """
    inpaint(src, mask, dst, algorithmType) -> None
    .   @brief The function implements different single-image inpainting algorithms.
    .   
    .       See the original paper @cite He2012 for details.
    .   
    .       @param src source image, it could be of any type and any number of channels from 1 to 4. In case of
    .       3- and 4-channels images the function expect them in CIELab colorspace or similar one, where first
    .       color component shows intensity, while second and third shows colors. Nonetheless you can try any
    .       colorspaces.
    .       @param mask mask (CV_8UC1), where non-zero pixels indicate valid image area, while zero pixels
    .       indicate area to be inpainted
    .       @param dst destination image
    .       @param algorithmType see xphoto::InpaintTypes
    """
    pass

def oilPainting(src, size, dynRatio, code, dst=None): # real signature unknown; restored from __doc__
    """
    oilPainting(src, size, dynRatio, code[, dst]) -> dst
    .   @brief oilPainting
    .   See the book @cite Holzmann1988 for details.
    .   @param src Input three-channel or one channel image (either CV_8UC3 or CV_8UC1)
    .   @param dst Output image of the same size and type as src.
    .   @param size neighbouring size is 2-size+1
    .   @param dynRatio image is divided by dynRatio before histogram processing
    .   @param code	color space conversion code(see ColorConversionCodes). Histogram will used only first plane
    
    
    
    oilPainting(src, size, dynRatio[, dst]) -> dst
    .   @brief oilPainting
    .   See the book @cite Holzmann1988 for details.
    .   @param src Input three-channel or one channel image (either CV_8UC3 or CV_8UC1)
    .   @param dst Output image of the same size and type as src.
    .   @param size neighbouring size is 2-size+1
    .   @param dynRatio image is divided by dynRatio before histogram processing
    """
    pass

# no classes
