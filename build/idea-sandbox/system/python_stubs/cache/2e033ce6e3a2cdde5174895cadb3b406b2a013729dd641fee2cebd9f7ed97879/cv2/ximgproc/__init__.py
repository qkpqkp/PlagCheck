# encoding: utf-8
# module cv2.ximgproc
# from C:\Users\Doly\Anaconda3\lib\site-packages\cv2\cv2.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import cv2.ximgproc.segmentation as segmentation # <module 'cv2.ximgproc.segmentation'>

# Variables with simple values

AM_FILTER = 4

ARO_0_45 = 0

ARO_315_0 = 3
ARO_315_135 = 6
ARO_315_45 = 4

ARO_45_135 = 5
ARO_45_90 = 1

ARO_90_135 = 2

ARO_CTR_HOR = 7
ARO_CTR_VER = 8

BINARIZATION_NIBLACK = 0
BINARIZATION_NICK = 3
BINARIZATION_SAUVOLA = 1
BINARIZATION_WOLF = 2

DTF_IC = 1
DTF_NC = 0
DTF_RF = 2

FHT_ADD = 2
FHT_AVE = 3
FHT_MAX = 1
FHT_MIN = 0

GUIDED_FILTER = 3

HDO_DESKEW = 1
HDO_RAW = 0

MSLIC = 102

SLIC = 100
SLICO = 101

THINNING_GUOHALL = 1
THINNING_ZHANGSUEN = 0

WMF_COS = 8
WMF_EXP = 1
WMF_IV1 = 2
WMF_IV2 = 4
WMF_JAC = 16
WMF_OFF = 32

__loader__ = None

__spec__ = None

# functions

def AdaptiveManifoldFilter_create(): # real signature unknown; restored from __doc__
    """
    AdaptiveManifoldFilter_create() -> retval
    .
    """
    pass

def amFilter(joint, src, sigma_s, sigma_r, dst=None, adjust_outliers=None): # real signature unknown; restored from __doc__
    """
    amFilter(joint, src, sigma_s, sigma_r[, dst[, adjust_outliers]]) -> dst
    .   @brief Simple one-line Adaptive Manifold Filter call.
    .   
    .   @param joint joint (also called as guided) image or array of images with any numbers of channels.
    .   
    .   @param src filtering image with any numbers of channels.
    .   
    .   @param dst output image.
    .   
    .   @param sigma_s spatial standard deviation.
    .   
    .   @param sigma_r color space standard deviation, it is similar to the sigma in the color space into
    .   bilateralFilter.
    .   
    .   @param adjust_outliers optional, specify perform outliers adjust operation or not, (Eq. 9) in the
    .   original paper.
    .   
    .   @note Joint images with CV_8U and CV_16U depth converted to images with CV_32F depth and [0; 1]
    .   color range before processing. Hence color space sigma sigma_r must be in [0; 1] range, unlike same
    .   sigmas in bilateralFilter and dtFilter functions. @sa bilateralFilter, dtFilter, guidedFilter
    """
    pass

def anisotropicDiffusion(src, alpha, K, niters, dst=None): # real signature unknown; restored from __doc__
    """
    anisotropicDiffusion(src, alpha, K, niters[, dst]) -> dst
    .   @brief Performs anisotropic diffusian on an image.
    .   
    .    The function applies Perona-Malik anisotropic diffusion to an image. This is the solution to the partial differential equation:
    .   
    .    \f[{\frac  {\partial I}{\partial t}}={\mathrm  {div}}\left(c(x,y,t)\nabla I\right)=\nabla c\cdot \nabla I+c(x,y,t)\Delta I\f]
    .   
    .    Suggested functions for c(x,y,t) are:
    .   
    .    \f[c\left(\|\nabla I\|\right)=e^{{-\left(\|\nabla I\|/K\right)^{2}}}\f]
    .   
    .    or
    .   
    .    \f[ c\left(\|\nabla I\|\right)={\frac {1}{1+\left({\frac  {\|\nabla I\|}{K}}\right)^{2}}} \f]
    .   
    .    @param src Source image with 3 channels.
    .    @param dst Destination image of the same size and the same number of channels as src .
    .    @param alpha The amount of time to step forward by on each iteration (normally, it's between 0 and 1).
    .    @param K sensitivity to the edges
    .    @param niters The number of iterations
    """
    pass

def bilateralTextureFilter(src, dst=None, fr=None, numIter=None, sigmaAlpha=None, sigmaAvg=None): # real signature unknown; restored from __doc__
    """
    bilateralTextureFilter(src[, dst[, fr[, numIter[, sigmaAlpha[, sigmaAvg]]]]]) -> dst
    .   @brief Applies the bilateral texture filter to an image. It performs structure-preserving texture filter.
    .   For more details about this filter see @cite Cho2014.
    .   
    .   @param src Source image whose depth is 8-bit UINT or 32-bit FLOAT
    .   
    .   @param dst Destination image of the same size and type as src.
    .   
    .   @param fr Radius of kernel to be used for filtering. It should be positive integer
    .   
    .   @param numIter Number of iterations of algorithm, It should be positive integer
    .   
    .   @param sigmaAlpha Controls the sharpness of the weight transition from edges to smooth/texture regions, where
    .   a bigger value means sharper transition. When the value is negative, it is automatically calculated.
    .   
    .   @param sigmaAvg Range blur parameter for texture blurring. Larger value makes result to be more blurred. When the
    .   value is negative, it is automatically calculated as described in the paper.
    .   
    .   @sa rollingGuidanceFilter, bilateralFilter
    """
    pass

def colorMatchTemplate(img, templ, result=None): # real signature unknown; restored from __doc__
    """
    colorMatchTemplate(img, templ[, result]) -> result
    .   * @brief    Compares a color template against overlapped color image regions.
    .   *
    .   * @param   img        Image where the search is running. It must be 3 channels image
    .   * @param   templ       Searched template. It must be not greater than the source image and have 3 channels
    .   * @param   result     Map of comparison results. It must be single-channel 64-bit floating-point
    """
    pass

def contourSampling(src, nbElt, out=None): # real signature unknown; restored from __doc__
    """
    contourSampling(src, nbElt[, out]) -> out
    .   * @brief   Contour sampling .
    .       *
    .       * @param   src   contour type vector<Point> , vector<Point2f>  or vector<Point2d>
    .       * @param   out   Mat of type CV_64FC2 and nbElt rows
    .       * @param   nbElt number of points in out contour
    .       *
    """
    pass

def covarianceEstimation(src, windowRows, windowCols, dst=None): # real signature unknown; restored from __doc__
    """
    covarianceEstimation(src, windowRows, windowCols[, dst]) -> dst
    .   @brief Computes the estimated covariance matrix of an image using the sliding
    .   window forumlation.
    .   
    .   @param src The source image. Input image must be of a complex type.
    .   @param dst The destination estimated covariance matrix. Output matrix will be size (windowRows*windowCols, windowRows*windowCols).
    .   @param windowRows The number of rows in the window.
    .   @param windowCols The number of cols in the window.
    .   The window size parameters control the accuracy of the estimation.
    .   The sliding window moves over the entire image from the top-left corner
    .   to the bottom right corner. Each location of the window represents a sample.
    .   If the window is the size of the image, then this gives the exact covariance matrix.
    .   For all other cases, the sizes of the window will impact the number of samples
    .   and the number of elements in the estimated covariance matrix.
    """
    pass

def createAMFilter(sigma_s, sigma_r, adjust_outliers=None): # real signature unknown; restored from __doc__
    """
    createAMFilter(sigma_s, sigma_r[, adjust_outliers]) -> retval
    .   @brief Factory method, create instance of AdaptiveManifoldFilter and produce some initialization routines.
    .   
    .   @param sigma_s spatial standard deviation.
    .   
    .   @param sigma_r color space standard deviation, it is similar to the sigma in the color space into
    .   bilateralFilter.
    .   
    .   @param adjust_outliers optional, specify perform outliers adjust operation or not, (Eq. 9) in the
    .   original paper.
    .   
    .   For more details about Adaptive Manifold Filter parameters, see the original article @cite Gastal12 .
    .   
    .   @note Joint images with CV_8U and CV_16U depth converted to images with CV_32F depth and [0; 1]
    .   color range before processing. Hence color space sigma sigma_r must be in [0; 1] range, unlike same
    .   sigmas in bilateralFilter and dtFilter functions.
    """
    pass

def createContourFitting(ctr=None, fd=None): # real signature unknown; restored from __doc__
    """
    createContourFitting([, ctr[, fd]]) -> retval
    .   * @brief create ContourFitting algorithm object
    .       *
    .       * @param ctr number of Fourier descriptors equal to number of contour points after resampling.
    .       * @param fd Contour defining second shape (Target).
    """
    pass

def createDisparityWLSFilter(matcher_left): # real signature unknown; restored from __doc__
    """
    createDisparityWLSFilter(matcher_left) -> retval
    .   @brief Convenience factory method that creates an instance of DisparityWLSFilter and sets up all the relevant
    .   filter parameters automatically based on the matcher instance. Currently supports only StereoBM and StereoSGBM.
    .   
    .   @param matcher_left stereo matcher instance that will be used with the filter
    """
    pass

def createDisparityWLSFilterGeneric(use_confidence): # real signature unknown; restored from __doc__
    """
    createDisparityWLSFilterGeneric(use_confidence) -> retval
    .   @brief More generic factory method, create instance of DisparityWLSFilter and execute basic
    .   initialization routines. When using this method you will need to set-up the ROI, matchers and
    .   other parameters by yourself.
    .   
    .   @param use_confidence filtering with confidence requires two disparity maps (for the left and right views) and is
    .   approximately two times slower. However, quality is typically significantly better.
    """
    pass

def createDTFilter(guide, sigmaSpatial, sigmaColor, mode=None, numIters=None): # real signature unknown; restored from __doc__
    """
    createDTFilter(guide, sigmaSpatial, sigmaColor[, mode[, numIters]]) -> retval
    .   @brief Factory method, create instance of DTFilter and produce initialization routines.
    .   
    .   @param guide guided image (used to build transformed distance, which describes edge structure of
    .   guided image).
    .   
    .   @param sigmaSpatial \f${\sigma}_H\f$ parameter in the original article, it's similar to the sigma in the
    .   coordinate space into bilateralFilter.
    .   
    .   @param sigmaColor \f${\sigma}_r\f$ parameter in the original article, it's similar to the sigma in the
    .   color space into bilateralFilter.
    .   
    .   @param mode one form three modes DTF_NC, DTF_RF and DTF_IC which corresponds to three modes for
    .   filtering 2D signals in the article.
    .   
    .   @param numIters optional number of iterations used for filtering, 3 is quite enough.
    .   
    .   For more details about Domain Transform filter parameters, see the original article @cite Gastal11 and
    .   [Domain Transform filter homepage](http://www.inf.ufrgs.br/~eslgastal/DomainTransform/).
    """
    pass

def createEdgeAwareInterpolator(): # real signature unknown; restored from __doc__
    """
    createEdgeAwareInterpolator() -> retval
    .   @brief Factory method that creates an instance of the
    .   EdgeAwareInterpolator.
    """
    pass

def createEdgeBoxes(alpha=None, beta=None, eta=None, minScore=None, maxBoxes=None, edgeMinMag=None, edgeMergeThr=None, clusterMinMag=None, maxAspectRatio=None, minBoxArea=None, gamma=None, kappa=None): # real signature unknown; restored from __doc__
    """
    createEdgeBoxes([, alpha[, beta[, eta[, minScore[, maxBoxes[, edgeMinMag[, edgeMergeThr[, clusterMinMag[, maxAspectRatio[, minBoxArea[, gamma[, kappa]]]]]]]]]]]]) -> retval
    .   @brief Creates a Edgeboxes
    .   
    .   @param alpha step size of sliding window search.
    .   @param beta nms threshold for object proposals.
    .   @param eta adaptation rate for nms threshold.
    .   @param minScore min score of boxes to detect.
    .   @param maxBoxes max number of boxes to detect.
    .   @param edgeMinMag edge min magnitude. Increase to trade off accuracy for speed.
    .   @param edgeMergeThr edge merge threshold. Increase to trade off accuracy for speed.
    .   @param clusterMinMag cluster min magnitude. Increase to trade off accuracy for speed.
    .   @param maxAspectRatio max aspect ratio of boxes.
    .   @param minBoxArea minimum area of boxes.
    .   @param gamma affinity sensitivity.
    .   @param kappa scale sensitivity.
    """
    pass

def createFastBilateralSolverFilter(guide, sigma_spatial, sigma_luma, sigma_chroma, lambda=None, num_iter=None, max_tol=None): # real signature unknown; restored from __doc__
    """
    createFastBilateralSolverFilter(guide, sigma_spatial, sigma_luma, sigma_chroma[, lambda[, num_iter[, max_tol]]]) -> retval
    .   @brief Factory method, create instance of FastBilateralSolverFilter and execute the initialization routines.
    .   
    .   @param guide image serving as guide for filtering. It should have 8-bit depth and either 1 or 3 channels.
    .   
    .   @param sigma_spatial parameter, that is similar to spatial space sigma (bandwidth) in bilateralFilter.
    .   
    .   @param sigma_luma parameter, that is similar to luma space sigma (bandwidth) in bilateralFilter.
    .   
    .   @param sigma_chroma parameter, that is similar to chroma space sigma (bandwidth) in bilateralFilter.
    .   
    .   @param lambda smoothness strength parameter for solver.
    .   
    .   @param num_iter number of iterations used for solver, 25 is usually enough.
    .   
    .   @param max_tol convergence tolerance used for solver.
    .   
    .   For more details about the Fast Bilateral Solver parameters, see the original paper @cite BarronPoole2016.
    """
    pass

def createFastGlobalSmootherFilter(guide, lambda_, sigma_color, lambda_attenuation=None, num_iter=None): # real signature unknown; restored from __doc__
    """
    createFastGlobalSmootherFilter(guide, lambda, sigma_color[, lambda_attenuation[, num_iter]]) -> retval
    .   @brief Factory method, create instance of FastGlobalSmootherFilter and execute the initialization routines.
    .   
    .   @param guide image serving as guide for filtering. It should have 8-bit depth and either 1 or 3 channels.
    .   
    .   @param lambda parameter defining the amount of regularization
    .   
    .   @param sigma_color parameter, that is similar to color space sigma in bilateralFilter.
    .   
    .   @param lambda_attenuation internal parameter, defining how much lambda decreases after each iteration. Normally,
    .   it should be 0.25. Setting it to 1.0 may lead to streaking artifacts.
    .   
    .   @param num_iter number of iterations used for filtering, 3 is usually enough.
    .   
    .   For more details about Fast Global Smoother parameters, see the original paper @cite Min2014. However, please note that
    .   there are several differences. Lambda attenuation described in the paper is implemented a bit differently so do not
    .   expect the results to be identical to those from the paper; sigma_color values from the paper should be multiplied by 255.0 to
    .   achieve the same effect. Also, in case of image filtering where source and guide image are the same, authors
    .   propose to dynamically update the guide image after each iteration. To maximize the performance this feature
    .   was not implemented here.
    """
    pass

def createFastLineDetector(_length_threshold=None, _distance_threshold=None, _canny_th1=None, _canny_th2=None, _canny_aperture_size=None, _do_merge=None): # real signature unknown; restored from __doc__
    """
    createFastLineDetector([, _length_threshold[, _distance_threshold[, _canny_th1[, _canny_th2[, _canny_aperture_size[, _do_merge]]]]]]) -> retval
    .   @brief Creates a smart pointer to a FastLineDetector object and initializes it
    .   
    .   @param _length_threshold    10         - Segment shorter than this will be discarded
    .   @param _distance_threshold  1.41421356 - A point placed from a hypothesis line
    .                                            segment farther than this will be
    .                                            regarded as an outlier
    .   @param _canny_th1           50         - First threshold for
    .                                            hysteresis procedure in Canny()
    .   @param _canny_th2           50         - Second threshold for
    .                                            hysteresis procedure in Canny()
    .   @param _canny_aperture_size 3          - Aperturesize for the sobel
    .                                            operator in Canny()
    .   @param _do_merge            false      - If true, incremental merging of segments
    .                                            will be perfomred
    """
    pass

def createGuidedFilter(guide, radius, eps): # real signature unknown; restored from __doc__
    """
    createGuidedFilter(guide, radius, eps) -> retval
    .   @brief Factory method, create instance of GuidedFilter and produce initialization routines.
    .   
    .   @param guide guided image (or array of images) with up to 3 channels, if it have more then 3
    .   channels then only first 3 channels will be used.
    .   
    .   @param radius radius of Guided Filter.
    .   
    .   @param eps regularization term of Guided Filter. \f${eps}^2\f$ is similar to the sigma in the color
    .   space into bilateralFilter.
    .   
    .   For more details about Guided Filter parameters, see the original article @cite Kaiming10 .
    """
    pass

def createQuaternionImage(img, qimg=None): # real signature unknown; restored from __doc__
    """
    createQuaternionImage(img[, qimg]) -> qimg
    .   * @brief   creates a quaternion image.
    .   *
    .   * @param   img         Source 8-bit, 32-bit or 64-bit image, with 3-channel image.
    .   * @param   qimg        result CV_64FC4 a quaternion image( 4 chanels zero channel and B,G,R).
    """
    pass

def createRFFeatureGetter(): # real signature unknown; restored from __doc__
    """
    createRFFeatureGetter() -> retval
    .
    """
    pass

def createRightMatcher(matcher_left): # real signature unknown; restored from __doc__
    """
    createRightMatcher(matcher_left) -> retval
    .   @brief Convenience method to set up the matcher for computing the right-view disparity map
    .   that is required in case of filtering with confidence.
    .   
    .   @param matcher_left main stereo matcher instance that will be used with the filter
    """
    pass

def createStructuredEdgeDetection(model, howToGetFeatures=None): # real signature unknown; restored from __doc__
    """
    createStructuredEdgeDetection(model[, howToGetFeatures]) -> retval
    .
    """
    pass

def createSuperpixelLSC(image, region_size=None, ratio=None): # real signature unknown; restored from __doc__
    """
    createSuperpixelLSC(image[, region_size[, ratio]]) -> retval
    .   @brief Class implementing the LSC (Linear Spectral Clustering) superpixels
    .   
    .   @param image Image to segment
    .   @param region_size Chooses an average superpixel size measured in pixels
    .   @param ratio Chooses the enforcement of superpixel compactness factor of superpixel
    .   
    .   The function initializes a SuperpixelLSC object for the input image. It sets the parameters of
    .   superpixel algorithm, which are: region_size and ruler. It preallocate some buffers for future
    .   computing iterations over the given image. An example of LSC is ilustrated in the following picture.
    .   For enanched results it is recommended for color images to preprocess image with little gaussian blur
    .   with a small 3 x 3 kernel and additional conversion into CieLAB color space.
    .   
    .   ![image](pics/superpixels_lsc.png)
    """
    pass

def createSuperpixelSEEDS(image_width, image_height, image_channels, num_superpixels, num_levels, prior=None, histogram_bins=None, double_step=None): # real signature unknown; restored from __doc__
    """
    createSuperpixelSEEDS(image_width, image_height, image_channels, num_superpixels, num_levels[, prior[, histogram_bins[, double_step]]]) -> retval
    .   @brief Initializes a SuperpixelSEEDS object.
    .   
    .   @param image_width Image width.
    .   @param image_height Image height.
    .   @param image_channels Number of channels of the image.
    .   @param num_superpixels Desired number of superpixels. Note that the actual number may be smaller
    .   due to restrictions (depending on the image size and num_levels). Use getNumberOfSuperpixels() to
    .   get the actual number.
    .   @param num_levels Number of block levels. The more levels, the more accurate is the segmentation,
    .   but needs more memory and CPU time.
    .   @param prior enable 3x3 shape smoothing term if \>0. A larger value leads to smoother shapes. prior
    .   must be in the range [0, 5].
    .   @param histogram_bins Number of histogram bins.
    .   @param double_step If true, iterate each block level twice for higher accuracy.
    .   
    .   The function initializes a SuperpixelSEEDS object for the input image. It stores the parameters of
    .   the image: image_width, image_height and image_channels. It also sets the parameters of the SEEDS
    .   superpixel algorithm, which are: num_superpixels, num_levels, use_prior, histogram_bins and
    .   double_step.
    .   
    .   The number of levels in num_levels defines the amount of block levels that the algorithm use in the
    .   optimization. The initialization is a grid, in which the superpixels are equally distributed through
    .   the width and the height of the image. The larger blocks correspond to the superpixel size, and the
    .   levels with smaller blocks are formed by dividing the larger blocks into 2 x 2 blocks of pixels,
    .   recursively until the smaller block level. An example of initialization of 4 block levels is
    .   illustrated in the following figure.
    .   
    .   ![image](pics/superpixels_blocks.png)
    """
    pass

def createSuperpixelSLIC(image, algorithm=None, region_size=None, ruler=None): # real signature unknown; restored from __doc__
    """
    createSuperpixelSLIC(image[, algorithm[, region_size[, ruler]]]) -> retval
    .   @brief Initialize a SuperpixelSLIC object
    .   
    .   @param image Image to segment
    .   @param algorithm Chooses the algorithm variant to use:
    .   SLIC segments image using a desired region_size, and in addition SLICO will optimize using adaptive compactness factor,
    .   while MSLIC will optimize using manifold methods resulting in more content-sensitive superpixels.
    .   @param region_size Chooses an average superpixel size measured in pixels
    .   @param ruler Chooses the enforcement of superpixel smoothness factor of superpixel
    .   
    .   The function initializes a SuperpixelSLIC object for the input image. It sets the parameters of choosed
    .   superpixel algorithm, which are: region_size and ruler. It preallocate some buffers for future
    .   computing iterations over the given image. For enanched results it is recommended for color images to
    .   preprocess image with little gaussian blur using a small 3 x 3 kernel and additional conversion into
    .   CieLAB color space. An example of SLIC versus SLICO and MSLIC is ilustrated in the following picture.
    .   
    .   ![image](pics/superpixels_slic.png)
    """
    pass

def dtFilter(guide, src, sigmaSpatial, sigmaColor, dst=None, mode=None, numIters=None): # real signature unknown; restored from __doc__
    """
    dtFilter(guide, src, sigmaSpatial, sigmaColor[, dst[, mode[, numIters]]]) -> dst
    .   @brief Simple one-line Domain Transform filter call. If you have multiple images to filter with the same
    .   guided image then use DTFilter interface to avoid extra computations on initialization stage.
    .   
    .   @param guide guided image (also called as joint image) with unsigned 8-bit or floating-point 32-bit
    .   depth and up to 4 channels.
    .   @param src filtering image with unsigned 8-bit or floating-point 32-bit depth and up to 4 channels.
    .   @param dst destination image
    .   @param sigmaSpatial \f${\sigma}_H\f$ parameter in the original article, it's similar to the sigma in the
    .   coordinate space into bilateralFilter.
    .   @param sigmaColor \f${\sigma}_r\f$ parameter in the original article, it's similar to the sigma in the
    .   color space into bilateralFilter.
    .   @param mode one form three modes DTF_NC, DTF_RF and DTF_IC which corresponds to three modes for
    .   filtering 2D signals in the article.
    .   @param numIters optional number of iterations used for filtering, 3 is quite enough.
    .   @sa bilateralFilter, guidedFilter, amFilter
    """
    pass

def edgePreservingFilter(src, d, threshold, dst=None): # real signature unknown; restored from __doc__
    """
    edgePreservingFilter(src, d, threshold[, dst]) -> dst
    .   * @brief Smoothes an image using the Edge-Preserving filter.
    .       *
    .       * The function smoothes Gaussian noise as well as salt & pepper noise.
    .       * For more details about this implementation, please see
    .       * [ReiWoe18]  Reich, S. and W&#246;rg&#246;tter, F. and Dellen, B. (2018). A Real-Time Edge-Preserving Denoising Filter. Proceedings of the 13th International Joint Conference on Computer Vision, Imaging and Computer Graphics Theory and Applications (VISIGRAPP): Visapp, 85-94, 4. DOI: 10.5220/0006509000850094.
    .       *
    .       * @param src Source 8-bit 3-channel image.
    .       * @param dst Destination image of the same size and type as src.
    .       * @param d Diameter of each pixel neighborhood that is used during filtering. Must be greater or equal 3.
    .       * @param threshold Threshold, which distinguishes between noise, outliers, and data.
    """
    pass

def fastBilateralSolverFilter(guide, src, confidence, dst=None, sigma_spatial=None, sigma_luma=None, sigma_chroma=None, lambda=None, num_iter=None, max_tol=None): # real signature unknown; restored from __doc__
    """
    fastBilateralSolverFilter(guide, src, confidence[, dst[, sigma_spatial[, sigma_luma[, sigma_chroma[, lambda[, num_iter[, max_tol]]]]]]]) -> dst
    .   @brief Simple one-line Fast Bilateral Solver filter call. If you have multiple images to filter with the same
    .   guide then use FastBilateralSolverFilter interface to avoid extra computations.
    .   
    .   @param guide image serving as guide for filtering. It should have 8-bit depth and either 1 or 3 channels.
    .   
    .   @param src source image for filtering with unsigned 8-bit or signed 16-bit or floating-point 32-bit depth and up to 4 channels.
    .   
    .   @param confidence confidence image with unsigned 8-bit or floating-point 32-bit confidence and 1 channel.
    .   
    .   @param dst destination image.
    .   
    .   @param sigma_spatial parameter, that is similar to spatial space sigma (bandwidth) in bilateralFilter.
    .   
    .   @param sigma_luma parameter, that is similar to luma space sigma (bandwidth) in bilateralFilter.
    .   
    .   @param sigma_chroma parameter, that is similar to chroma space sigma (bandwidth) in bilateralFilter.
    .   
    .   @param lambda smoothness strength parameter for solver.
    .   
    .   @param num_iter number of iterations used for solver, 25 is usually enough.
    .   
    .   @param max_tol convergence tolerance used for solver.
    .   
    .   For more details about the Fast Bilateral Solver parameters, see the original paper @cite BarronPoole2016.
    .   
    .   @note Confidence images with CV_8U depth are expected to in [0, 255] and CV_32F in [0, 1] range.
    """
    pass

def fastGlobalSmootherFilter(guide, src, lambda_, sigma_color, dst=None, lambda_attenuation=None, num_iter=None): # real signature unknown; restored from __doc__
    """
    fastGlobalSmootherFilter(guide, src, lambda, sigma_color[, dst[, lambda_attenuation[, num_iter]]]) -> dst
    .   @brief Simple one-line Fast Global Smoother filter call. If you have multiple images to filter with the same
    .   guide then use FastGlobalSmootherFilter interface to avoid extra computations.
    .   
    .   @param guide image serving as guide for filtering. It should have 8-bit depth and either 1 or 3 channels.
    .   
    .   @param src source image for filtering with unsigned 8-bit or signed 16-bit or floating-point 32-bit depth and up to 4 channels.
    .   
    .   @param dst destination image.
    .   
    .   @param lambda parameter defining the amount of regularization
    .   
    .   @param sigma_color parameter, that is similar to color space sigma in bilateralFilter.
    .   
    .   @param lambda_attenuation internal parameter, defining how much lambda decreases after each iteration. Normally,
    .   it should be 0.25. Setting it to 1.0 may lead to streaking artifacts.
    .   
    .   @param num_iter number of iterations used for filtering, 3 is usually enough.
    """
    pass

def FastHoughTransform(src, dstMatDepth, dst=None, angleRange=None, op=None, makeSkew=None): # real signature unknown; restored from __doc__
    """
    FastHoughTransform(src, dstMatDepth[, dst[, angleRange[, op[, makeSkew]]]]) -> dst
    .   * @brief   Calculates 2D Fast Hough transform of an image.
    .   * @param   dst         The destination image, result of transformation.
    .   * @param   src         The source (input) image.
    .   * @param   dstMatDepth The depth of destination image
    .   * @param   op          The operation to be applied, see cv::HoughOp
    .   * @param   angleRange  The part of Hough space to calculate, see cv::AngleRangeOption
    .   * @param   makeSkew    Specifies to do or not to do image skewing, see cv::HoughDeskewOption
    .   *
    .   * The function calculates the fast Hough transform for full, half or quarter
    .   * range of angles.
    """
    pass

def fourierDescriptor(src, dst=None, nbElt=None, nbFD=None): # real signature unknown; restored from __doc__
    """
    fourierDescriptor(src[, dst[, nbElt[, nbFD]]]) -> dst
    .   * @brief   Fourier descriptors for planed closed curves
    .       *
    .       * For more details about this implementation, please see @cite PersoonFu1977
    .       *
    .       * @param   src   contour type vector<Point> , vector<Point2f>  or vector<Point2d>
    .       * @param   dst   Mat of type CV_64FC2 and nbElt rows A VERIFIER
    .       * @param   nbElt number of rows in dst or getOptimalDFTSize rows if nbElt=-1
    .       * @param   nbFD number of FD return in dst dst = [FD(1...nbFD/2) FD(nbFD/2-nbElt+1...:nbElt)]
    .       *
    """
    pass

def GradientDericheX(op, alpha, omega, dst=None): # real signature unknown; restored from __doc__
    """
    GradientDericheX(op, alpha, omega[, dst]) -> dst
    .   * @brief   Applies X Deriche filter to an image.
    .   *
    .   * For more details about this implementation, please see http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.476.5736&rep=rep1&type=pdf
    .   *
    .   * @param   op         Source 8-bit or 16bit image, 1-channel or 3-channel image.
    .   * @param   dst        result CV_32FC image with same number of channel than _op.
    .   * @param   alpha double see paper
    .   * @param   omega   double see paper
    .   *
    """
    pass

def GradientDericheY(op, alpha, omega, dst=None): # real signature unknown; restored from __doc__
    """
    GradientDericheY(op, alpha, omega[, dst]) -> dst
    .   * @brief   Applies Y Deriche filter to an image.
    .   *
    .   * For more details about this implementation, please see http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.476.5736&rep=rep1&type=pdf
    .   *
    .   * @param   op         Source 8-bit or 16bit image, 1-channel or 3-channel image.
    .   * @param   dst        result CV_32FC image with same number of channel than _op.
    .   * @param   alpha double see paper
    .   * @param   omega   double see paper
    .   *
    """
    pass

def guidedFilter(guide, src, radius, eps, dst=None, dDepth=None): # real signature unknown; restored from __doc__
    """
    guidedFilter(guide, src, radius, eps[, dst[, dDepth]]) -> dst
    .   @brief Simple one-line Guided Filter call.
    .   
    .   If you have multiple images to filter with the same guided image then use GuidedFilter interface to
    .   avoid extra computations on initialization stage.
    .   
    .   @param guide guided image (or array of images) with up to 3 channels, if it have more then 3
    .   channels then only first 3 channels will be used.
    .   
    .   @param src filtering image with any numbers of channels.
    .   
    .   @param dst output image.
    .   
    .   @param radius radius of Guided Filter.
    .   
    .   @param eps regularization term of Guided Filter. \f${eps}^2\f$ is similar to the sigma in the color
    .   space into bilateralFilter.
    .   
    .   @param dDepth optional depth of the output image.
    .   
    .   @sa bilateralFilter, dtFilter, amFilter
    """
    pass

def HoughPoint2Line(houghPoint, srcImgInfo, angleRange=None, makeSkew=None, rules=None): # real signature unknown; restored from __doc__
    """
    HoughPoint2Line(houghPoint, srcImgInfo[, angleRange[, makeSkew[, rules]]]) -> retval
    .   * @brief   Calculates coordinates of line segment corresponded by point in Hough space.
    .   * @param   houghPoint  Point in Hough space.
    .   * @param   srcImgInfo The source (input) image of Hough transform.
    .   * @param   angleRange  The part of Hough space where point is situated, see cv::AngleRangeOption
    .   * @param   makeSkew    Specifies to do or not to do image skewing, see cv::HoughDeskewOption
    .   * @param   rules       Specifies strictness of line segment calculating, see cv::RulesOption
    .   * @retval  [Vec4i]     Coordinates of line segment corresponded by point in Hough space.
    .   * @remarks If rules parameter set to RO_STRICT
    .              then returned line cut along the border of source image.
    .   * @remarks If rules parameter set to RO_WEAK then in case of point, which belongs
    .              the incorrect part of Hough image, returned line will not intersect source image.
    .   *
    .   * The function calculates coordinates of line segment corresponded by point in Hough space.
    """
    pass

def jointBilateralFilter(joint, src, d, sigmaColor, sigmaSpace, dst=None, borderType=None): # real signature unknown; restored from __doc__
    """
    jointBilateralFilter(joint, src, d, sigmaColor, sigmaSpace[, dst[, borderType]]) -> dst
    .   @brief Applies the joint bilateral filter to an image.
    .   
    .   @param joint Joint 8-bit or floating-point, 1-channel or 3-channel image.
    .   
    .   @param src Source 8-bit or floating-point, 1-channel or 3-channel image with the same depth as joint
    .   image.
    .   
    .   @param dst Destination image of the same size and type as src .
    .   
    .   @param d Diameter of each pixel neighborhood that is used during filtering. If it is non-positive,
    .   it is computed from sigmaSpace .
    .   
    .   @param sigmaColor Filter sigma in the color space. A larger value of the parameter means that
    .   farther colors within the pixel neighborhood (see sigmaSpace ) will be mixed together, resulting in
    .   larger areas of semi-equal color.
    .   
    .   @param sigmaSpace Filter sigma in the coordinate space. A larger value of the parameter means that
    .   farther pixels will influence each other as long as their colors are close enough (see sigmaColor ).
    .   When d\>0 , it specifies the neighborhood size regardless of sigmaSpace . Otherwise, d is
    .   proportional to sigmaSpace .
    .   
    .   @param borderType
    .   
    .   @note bilateralFilter and jointBilateralFilter use L1 norm to compute difference between colors.
    .   
    .   @sa bilateralFilter, amFilter
    """
    pass

def l0Smooth(src, dst=None, lambda=None, kappa=None): # real signature unknown; restored from __doc__
    """
    l0Smooth(src[, dst[, lambda[, kappa]]]) -> dst
    .   @brief Global image smoothing via L0 gradient minimization.
    .   
    .   @param src source image for filtering with unsigned 8-bit or signed 16-bit or floating-point depth.
    .   
    .   @param dst destination image.
    .   
    .   @param lambda parameter defining the smooth term weight.
    .   
    .   @param kappa parameter defining the increasing factor of the weight of the gradient data term.
    .   
    .   For more details about L0 Smoother, see the original paper @cite xu2011image.
    """
    pass

def niBlackThreshold(_src, maxValue, type, blockSize, k, _dst=None, binarizationMethod=None): # real signature unknown; restored from __doc__
    """
    niBlackThreshold(_src, maxValue, type, blockSize, k[, _dst[, binarizationMethod]]) -> _dst
    .   @brief Performs thresholding on input images using Niblack's technique or some of the
    .   popular variations it inspired.
    .   
    .   The function transforms a grayscale image to a binary image according to the formulae:
    .   -   **THRESH_BINARY**
    .       \f[dst(x,y) =  \fork{\texttt{maxValue}}{if \(src(x,y) > T(x,y)\)}{0}{otherwise}\f]
    .   -   **THRESH_BINARY_INV**
    .       \f[dst(x,y) =  \fork{0}{if \(src(x,y) > T(x,y)\)}{\texttt{maxValue}}{otherwise}\f]
    .   where \f$T(x,y)\f$ is a threshold calculated individually for each pixel.
    .   
    .   The threshold value \f$T(x, y)\f$ is determined based on the binarization method chosen. For
    .   classic Niblack, it is the mean minus \f$ k \f$ times standard deviation of
    .   \f$\texttt{blockSize} \times\texttt{blockSize}\f$ neighborhood of \f$(x, y)\f$.
    .   
    .   The function can't process the image in-place.
    .   
    .   @param _src Source 8-bit single-channel image.
    .   @param _dst Destination image of the same size and the same type as src.
    .   @param maxValue Non-zero value assigned to the pixels for which the condition is satisfied,
    .   used with the THRESH_BINARY and THRESH_BINARY_INV thresholding types.
    .   @param type Thresholding type, see cv::ThresholdTypes.
    .   @param blockSize Size of a pixel neighborhood that is used to calculate a threshold value
    .   for the pixel: 3, 5, 7, and so on.
    .   @param k The user-adjustable parameter used by Niblack and inspired techniques. For Niblack, this is
    .   normally a value between 0 and 1 that is multiplied with the standard deviation and subtracted from
    .   the mean.
    .   @param binarizationMethod Binarization method to use. By default, Niblack's technique is used.
    .   Other techniques can be specified, see cv::ximgproc::LocalBinarizationMethods.
    .   
    .   @sa  threshold, adaptiveThreshold
    """
    pass

def PeiLinNormalization(I, T=None): # real signature unknown; restored from __doc__
    """
    PeiLinNormalization(I[, T]) -> T
    .   @overload
    """
    pass

def qconj(qimg, qcimg=None): # real signature unknown; restored from __doc__
    """
    qconj(qimg[, qcimg]) -> qcimg
    .   * @brief   calculates conjugate of a quaternion image.
    .   *
    .   * @param   qimg         quaternion image.
    .   * @param   qcimg        conjugate of qimg
    """
    pass

def qdft(img, flags, sideLeft, qimg=None): # real signature unknown; restored from __doc__
    """
    qdft(img, flags, sideLeft[, qimg]) -> qimg
    .   * @brief    Performs a forward or inverse Discrete quaternion Fourier transform of a 2D quaternion array.
    .   *
    .   * @param   img        quaternion image.
    .   * @param   qimg       quaternion image in dual space.
    .   * @param   flags      quaternion image in dual space. only DFT_INVERSE flags is supported
    .   * @param   sideLeft   true the hypercomplex exponential is to be multiplied on the left (false on the right ).
    """
    pass

def qmultiply(src1, src2, dst=None): # real signature unknown; restored from __doc__
    """
    qmultiply(src1, src2[, dst]) -> dst
    .   * @brief   Calculates the per-element quaternion product of two arrays
    .   *
    .   * @param   src1         quaternion image.
    .   * @param   src2         quaternion image.
    .   * @param   dst        product dst(I)=src1(I) . src2(I)
    """
    pass

def qunitary(qimg, qnimg=None): # real signature unknown; restored from __doc__
    """
    qunitary(qimg[, qnimg]) -> qnimg
    .   * @brief   divides each element by its modulus.
    .   *
    .   * @param   qimg         quaternion image.
    .   * @param   qnimg        conjugate of qimg
    """
    pass

def RidgeDetectionFilter_create(ddepth=None, dx=None, dy=None, ksize=None, out_dtype=None, scale=None, delta=None, borderType=None): # real signature unknown; restored from __doc__
    """
    RidgeDetectionFilter_create([, ddepth[, dx[, dy[, ksize[, out_dtype[, scale[, delta[, borderType]]]]]]]]) -> retval
    .   @brief Create pointer to the Ridge detection filter.
    .       @param ddepth  Specifies output image depth. Defualt is CV_32FC1
    .       @param dx Order of derivative x, default is 1
    .       @param dy  Order of derivative y, default is 1
    .       @param ksize Sobel kernel size , default is 3
    .       @param out_dtype Converted format for output, default is CV_8UC1
    .       @param scale Optional scale value for derivative values, default is 1
    .       @param delta  Optional bias added to output, default is 0
    .       @param borderType Pixel extrapolation method, default is BORDER_DEFAULT
    .       @see Sobel, threshold, getStructuringElement, morphologyEx.( for additional refinement)
    """
    pass

def rollingGuidanceFilter(src, dst=None, d=None, sigmaColor=None, sigmaSpace=None, numOfIter=None, borderType=None): # real signature unknown; restored from __doc__
    """
    rollingGuidanceFilter(src[, dst[, d[, sigmaColor[, sigmaSpace[, numOfIter[, borderType]]]]]]) -> dst
    .   @brief Applies the rolling guidance filter to an image.
    .   
    .   For more details, please see @cite zhang2014rolling
    .   
    .   @param src Source 8-bit or floating-point, 1-channel or 3-channel image.
    .   
    .   @param dst Destination image of the same size and type as src.
    .   
    .   @param d Diameter of each pixel neighborhood that is used during filtering. If it is non-positive,
    .   it is computed from sigmaSpace .
    .   
    .   @param sigmaColor Filter sigma in the color space. A larger value of the parameter means that
    .   farther colors within the pixel neighborhood (see sigmaSpace ) will be mixed together, resulting in
    .   larger areas of semi-equal color.
    .   
    .   @param sigmaSpace Filter sigma in the coordinate space. A larger value of the parameter means that
    .   farther pixels will influence each other as long as their colors are close enough (see sigmaColor ).
    .   When d\>0 , it specifies the neighborhood size regardless of sigmaSpace . Otherwise, d is
    .   proportional to sigmaSpace .
    .   
    .   @param numOfIter Number of iterations of joint edge-preserving filtering applied on the source image.
    .   
    .   @param borderType
    .   
    .   @note  rollingGuidanceFilter uses jointBilateralFilter as the edge-preserving filter.
    .   
    .   @sa jointBilateralFilter, bilateralFilter, amFilter
    """
    pass

def thinning(src, dst=None, thinningType=None): # real signature unknown; restored from __doc__
    """
    thinning(src[, dst[, thinningType]]) -> dst
    .   @brief Applies a binary blob thinning operation, to achieve a skeletization of the input image.
    .   
    .   The function transforms a binary blob image into a skeletized form using the technique of Zhang-Suen.
    .   
    .   @param src Source 8-bit single-channel image, containing binary blobs, with blobs having 255 pixel values.
    .   @param dst Destination image of the same size and the same type as src. The function can work in-place.
    .   @param thinningType Value that defines which thinning algorithm should be used. See cv::ximgproc::ThinningTypes
    """
    pass

def transformFD(src, t, dst=None, fdContour=None): # real signature unknown; restored from __doc__
    """
    transformFD(src, t[, dst[, fdContour]]) -> dst
    .   * @brief   transform a contour
    .       *
    .       * @param   src   contour or Fourier Descriptors if fd is true
    .       * @param   t   transform Mat given by estimateTransformation
    .       * @param   dst   Mat of type CV_64FC2 and nbElt rows
    .       * @param   fdContour true src are Fourier Descriptors. fdContour false src is a contour
    .       *
    """
    pass

def weightedMedianFilter(joint, src, r, dst=None, sigma=None, weightType=None, mask=None): # real signature unknown; restored from __doc__
    """
    weightedMedianFilter(joint, src, r[, dst[, sigma[, weightType[, mask]]]]) -> dst
    .   * @brief   Applies weighted median filter to an image.
    .   *
    .   * For more details about this implementation, please see @cite zhang2014100+
    .   *
    .   * @param   joint       Joint 8-bit, 1-channel or 3-channel image.
    .   * @param   src         Source 8-bit or floating-point, 1-channel or 3-channel image.
    .   * @param   dst         Destination image.
    .   * @param   r           Radius of filtering kernel, should be a positive integer.
    .   * @param   sigma       Filter range standard deviation for the joint image.
    .   * @param   weightType  weightType The type of weight definition, see WMFWeightType
    .   * @param   mask        A 0-1 mask that has the same size with I. This mask is used to ignore the effect of some pixels. If the pixel value on mask is 0,
    .   *                           the pixel will be ignored when maintaining the joint-histogram. This is useful for applications like optical flow occlusion handling.
    .   *
    .   * @sa medianBlur, jointBilateralFilter
    """
    pass

# no classes
