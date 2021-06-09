# encoding: utf-8
# module cv2.optflow
# from C:\Users\Doly\Anaconda3\lib\site-packages\cv2\cv2.cp37-win_amd64.pyd
# by generator 1.147
# no doc
# no imports

# Variables with simple values

GPC_DESCRIPTOR_DCT = 0
GPC_DESCRIPTOR_WHT = 1

INTERP_EPIC = 1
INTERP_GEO = 0

SR_CROSS = 1
SR_FIXED = 0

ST_BILINEAR = 1
ST_STANDART = 0

__loader__ = None

__spec__ = None

# functions

def calcOpticalFlowDenseRLOF(I0, I1, flow, rlofParam=None, forwardBackwardThreshold=None, gridStep=None, interp_type=None, epicK=None, epicSigma=None, epicLambda=None, use_post_proc=None, fgsLambda=None, fgsSigma=None): # real signature unknown; restored from __doc__
    """
    calcOpticalFlowDenseRLOF(I0, I1, flow[, rlofParam[, forwardBackwardThreshold[, gridStep[, interp_type[, epicK[, epicSigma[, epicLambda[, use_post_proc[, fgsLambda[, fgsSigma]]]]]]]]]]) -> flow
    .   @brief Fast dense optical flow computation based on robust local optical flow (RLOF) algorithms and sparse-to-dense interpolation scheme.
    .    *
    .    * The RLOF is a fast local optical flow approach described in @cite Senst2012 @cite Senst2013 @cite Senst2014
    .    * and @cite Senst2016 similar to the pyramidal iterative Lucas-Kanade method as
    .    * proposed by @cite Bouguet00. The implementation is derived from optflow::calcOpticalFlowPyrLK().
    .    *
    .    * The sparse-to-dense interpolation scheme allows for fast computation of dense optical flow using RLOF (see @cite Geistert2016).
    .    * For this scheme the following steps are applied:
    .    * -# motion vector seeded at a regular sampled grid are computed. The sparsity of this grid can be configured with setGridStep
    .    * -# (optinally) errornous motion vectors are filter based on the forward backward confidence. The threshold can be configured
    .    * with setForwardBackward. The filter is only applied if the threshold >0 but than the runtime is doubled due to the estimation
    .    * of the backward flow.
    .    * -# Vector field interpolation is applied to the motion vector set to obtain a dense vector field.
    .    *
    .    * @param I0 first 8-bit input image. If The cross-based RLOF is used (by selecting optflow::RLOFOpticalFlowParameter::supportRegionType
    .    * = SupportRegionType::SR_CROSS) image has to be a 8-bit 3 channel image.
    .    * @param I1 second 8-bit input image. If The cross-based RLOF is used (by selecting optflow::RLOFOpticalFlowParameter::supportRegionType
    .    * = SupportRegionType::SR_CROSS) image has to be a 8-bit 3 channel image.
    .    * @param flow computed flow image that has the same size as I0 and type CV_32FC2.
    .    * @param rlofParam see optflow::RLOFOpticalFlowParameter
    .    * @param forwardBackwardThreshold Threshold for the forward backward confidence check.
    .    * For each grid point \f$ \mathbf{x} \f$ a motion vector \f$ d_{I0,I1}(\mathbf{x}) \f$ is computed.
    .    * If the forward backward error \f[ EP_{FB} = || d_{I0,I1} + d_{I1,I0} || \f]
    .    * is larger than threshold given by this function then the motion vector will not be used by the following
    .    * vector field interpolation. \f$ d_{I1,I0} \f$ denotes the backward flow. Note, the forward backward test
    .    *    will only be applied if the threshold > 0. This may results into a doubled runtime for the motion estimation.
    .    * @param gridStep Size of the grid to spawn the motion vectors. For each grid point a motion vector is computed.
    .    * Some motion vectors will be removed due to the forwatd backward threshold (if set >0). The rest will be the
    .    * base of the vector field interpolation.
    .    * @param interp_type interpolation method used to compute the dense optical flow. Two interpolation algorithms are
    .    * supported:
    .    * - **INTERP_GEO** applies the fast geodesic interpolation, see @cite Geistert2016.
    .    * - **INTERP_EPIC_RESIDUAL** applies the edge-preserving interpolation, see @cite Revaud2015,Geistert2016.
    .    * @param epicK see ximgproc::EdgeAwareInterpolator() sets the respective parameter.
    .    * @param epicSigma see ximgproc::EdgeAwareInterpolator() sets the respective parameter.
    .    * @param epicLambda see ximgproc::EdgeAwareInterpolator() sets the respective parameter.
    .    * @param use_post_proc enables ximgproc::fastGlobalSmootherFilter() parameter.
    .    * @param fgsLambda sets the respective ximgproc::fastGlobalSmootherFilter() parameter.
    .    * @param fgsSigma sets the respective ximgproc::fastGlobalSmootherFilter() parameter.
    .    *
    .    * Parameters have been described in @cite Senst2012, @cite Senst2013, @cite Senst2014, @cite Senst2016.
    .    * For the RLOF configuration see optflow::RLOFOpticalFlowParameter for further details.
    .    * @note If the grid size is set to (1,1) and the forward backward threshold <= 0 that the dense optical flow field is purely
    .    * computed with the RLOF.
    .    *
    .    * @note SIMD parallelization is only available when compiling with SSE4.1.
    .    *
    .    * @sa optflow::DenseRLOFOpticalFlow, optflow::RLOFOpticalFlowParameter
    """
    pass

def calcOpticalFlowSF(from_, to, layers, averaging_block_size, max_flow, flow=None): # real signature unknown; restored from __doc__
    """
    calcOpticalFlowSF(from, to, layers, averaging_block_size, max_flow[, flow]) -> flow
    .   @overload
    
    
    
    calcOpticalFlowSF(from, to, layers, averaging_block_size, max_flow, sigma_dist, sigma_color, postprocess_window, sigma_dist_fix, sigma_color_fix, occ_thr, upscale_averaging_radius, upscale_sigma_dist, upscale_sigma_color, speed_up_thr[, flow]) -> flow
    .   @brief Calculate an optical flow using "SimpleFlow" algorithm.
    .   
    .   @param from First 8-bit 3-channel image.
    .   @param to Second 8-bit 3-channel image of the same size as prev
    .   @param flow computed flow image that has the same size as prev and type CV_32FC2
    .   @param layers Number of layers
    .   @param averaging_block_size Size of block through which we sum up when calculate cost function
    .   for pixel
    .   @param max_flow maximal flow that we search at each level
    .   @param sigma_dist vector smooth spatial sigma parameter
    .   @param sigma_color vector smooth color sigma parameter
    .   @param postprocess_window window size for postprocess cross bilateral filter
    .   @param sigma_dist_fix spatial sigma for postprocess cross bilateralf filter
    .   @param sigma_color_fix color sigma for postprocess cross bilateral filter
    .   @param occ_thr threshold for detecting occlusions
    .   @param upscale_averaging_radius window size for bilateral upscale operation
    .   @param upscale_sigma_dist spatial sigma for bilateral upscale operation
    .   @param upscale_sigma_color color sigma for bilateral upscale operation
    .   @param speed_up_thr threshold to detect point with irregular flow - where flow should be
    .   recalculated after upscale
    .   
    .   See @cite Tao2012 . And site of project - <http://graphics.berkeley.edu/papers/Tao-SAN-2012-05/>.
    .   
    .   @note
    .      -   An example using the simpleFlow algorithm can be found at samples/simpleflow_demo.cpp
    """
    pass

def calcOpticalFlowSparseRLOF(prevImg, nextImg, prevPts, nextPts, status=None, err=None, rlofParam=None, forwardBackwardThreshold=None): # real signature unknown; restored from __doc__
    """
    calcOpticalFlowSparseRLOF(prevImg, nextImg, prevPts, nextPts[, status[, err[, rlofParam[, forwardBackwardThreshold]]]]) -> nextPts, status, err
    .   @brief Calculates fast optical flow for a sparse feature set using the robust local optical flow (RLOF) similar
    .   * to optflow::calcOpticalFlowPyrLK().
    .   *
    .   * The RLOF is a fast local optical flow approach described in @cite Senst2012 @cite Senst2013 @cite Senst2014
    .    * and @cite Senst2016 similar to the pyramidal iterative Lucas-Kanade method as
    .   * proposed by @cite Bouguet00. The implementation is derived from optflow::calcOpticalFlowPyrLK().
    .   *
    .   * @param prevImg first 8-bit input image. If The cross-based RLOF is used (by selecting optflow::RLOFOpticalFlowParameter::supportRegionType
    .   * = SupportRegionType::SR_CROSS) image has to be a 8-bit 3 channel image.
    .   * @param nextImg second 8-bit input image. If The cross-based RLOF is used (by selecting optflow::RLOFOpticalFlowParameter::supportRegionType
    .   * = SupportRegionType::SR_CROSS) image has to be a 8-bit 3 channel image.
    .   * @param prevPts vector of 2D points for which the flow needs to be found; point coordinates must be single-precision
    .   * floating-point numbers.
    .   * @param nextPts output vector of 2D points (with single-precision floating-point coordinates) containing the calculated
    .   * new positions of input features in the second image; when optflow::RLOFOpticalFlowParameter::useInitialFlow variable is true  the vector must
    .   * have the same size as in the input and contain the initialization point correspondences.
    .   * @param status output status vector (of unsigned chars); each element of the vector is set to 1 if the flow for the
    .   * corresponding features has passed the forward backward check.
    .   * @param err output vector of errors; each element of the vector is set to the forward backward error for the corresponding feature.
    .   * @param rlofParam see optflow::RLOFOpticalFlowParameter
    .   * @param forwardBackwardThreshold Threshold for the forward backward confidence check. If forewardBackwardThreshold <=0 the forward
    .   *
    .   * @note SIMD parallelization is only available when compiling with SSE4.1.
    .   *
    .   * Parameters have been described in @cite Senst2012, @cite Senst2013, @cite Senst2014 and @cite Senst2016.
    .   * For the RLOF configuration see optflow::RLOFOpticalFlowParameter for further details.
    """
    pass

def calcOpticalFlowSparseToDense(from_, to, flow=None, grid_step=None, k=None, sigma=None, use_post_proc=None, fgs_lambda=None, fgs_sigma=None): # real signature unknown; restored from __doc__
    """
    calcOpticalFlowSparseToDense(from, to[, flow[, grid_step[, k[, sigma[, use_post_proc[, fgs_lambda[, fgs_sigma]]]]]]]) -> flow
    .   @brief Fast dense optical flow based on PyrLK sparse matches interpolation.
    .   
    .   @param from first 8-bit 3-channel or 1-channel image.
    .   @param to  second 8-bit 3-channel or 1-channel image of the same size as from
    .   @param flow computed flow image that has the same size as from and CV_32FC2 type
    .   @param grid_step stride used in sparse match computation. Lower values usually
    .          result in higher quality but slow down the algorithm.
    .   @param k number of nearest-neighbor matches considered, when fitting a locally affine
    .          model. Lower values can make the algorithm noticeably faster at the cost of
    .          some quality degradation.
    .   @param sigma parameter defining how fast the weights decrease in the locally-weighted affine
    .          fitting. Higher values can help preserve fine details, lower values can help to get rid
    .          of the noise in the output flow.
    .   @param use_post_proc defines whether the ximgproc::fastGlobalSmootherFilter() is used
    .          for post-processing after interpolation
    .   @param fgs_lambda see the respective parameter of the ximgproc::fastGlobalSmootherFilter()
    .   @param fgs_sigma  see the respective parameter of the ximgproc::fastGlobalSmootherFilter()
    """
    pass

def createOptFlow_DeepFlow(): # real signature unknown; restored from __doc__
    """
    createOptFlow_DeepFlow() -> retval
    .   @brief DeepFlow optical flow algorithm implementation.
    .   
    .   The class implements the DeepFlow optical flow algorithm described in @cite Weinzaepfel2013 . See
    .   also <http://lear.inrialpes.fr/src/deepmatching/> .
    .   Parameters - class fields - that may be modified after creating a class instance:
    .   -   member float alpha
    .   Smoothness assumption weight
    .   -   member float delta
    .   Color constancy assumption weight
    .   -   member float gamma
    .   Gradient constancy weight
    .   -   member float sigma
    .   Gaussian smoothing parameter
    .   -   member int minSize
    .   Minimal dimension of an image in the pyramid (next, smaller images in the pyramid are generated
    .   until one of the dimensions reaches this size)
    .   -   member float downscaleFactor
    .   Scaling factor in the image pyramid (must be \< 1)
    .   -   member int fixedPointIterations
    .   How many iterations on each level of the pyramid
    .   -   member int sorIterations
    .   Iterations of Succesive Over-Relaxation (solver)
    .   -   member float omega
    .   Relaxation factor in SOR
    """
    pass

def createOptFlow_DenseRLOF(): # real signature unknown; restored from __doc__
    """
    createOptFlow_DenseRLOF() -> retval
    .
    """
    pass

def createOptFlow_DualTVL1(): # real signature unknown; restored from __doc__
    """
    createOptFlow_DualTVL1() -> retval
    .   @brief Creates instance of cv::DenseOpticalFlow
    """
    pass

def createOptFlow_Farneback(): # real signature unknown; restored from __doc__
    """
    createOptFlow_Farneback() -> retval
    .
    """
    pass

def createOptFlow_PCAFlow(): # real signature unknown; restored from __doc__
    """
    createOptFlow_PCAFlow() -> retval
    .   @brief Creates an instance of PCAFlow
    """
    pass

def createOptFlow_SimpleFlow(): # real signature unknown; restored from __doc__
    """
    createOptFlow_SimpleFlow() -> retval
    .
    """
    pass

def createOptFlow_SparseRLOF(): # real signature unknown; restored from __doc__
    """
    createOptFlow_SparseRLOF() -> retval
    .
    """
    pass

def createOptFlow_SparseToDense(): # real signature unknown; restored from __doc__
    """
    createOptFlow_SparseToDense() -> retval
    .
    """
    pass

def DenseRLOFOpticalFlow_create(rlofParam=None, forwardBackwardThreshold=None, gridStep=None, interp_type=None, epicK=None, epicSigma=None, epicLambda=None, use_post_proc=None, fgsLambda=None, fgsSigma=None): # real signature unknown; restored from __doc__
    """
    DenseRLOFOpticalFlow_create([, rlofParam[, forwardBackwardThreshold[, gridStep[, interp_type[, epicK[, epicSigma[, epicLambda[, use_post_proc[, fgsLambda[, fgsSigma]]]]]]]]]]) -> retval
    .   *    @param rlofParam see optflow::RLOFOpticalFlowParameter
    .        *    @param forwardBackwardThreshold see setForwardBackward
    .        *    @param gridStep see setGridStep
    .        *    @param interp_type see setInterpolation
    .        *    @param epicK see setEPICK
    .        *    @param epicSigma see setEPICSigma
    .        *    @param epicLambda see setEPICLambda
    .        *    @param use_post_proc see setUsePostProc
    .        *    @param fgsLambda see setFgsLambda
    .        *    @param fgsSigma see setFgsSigma
    """
    pass

def DualTVL1OpticalFlow_create(tau=None, lambda=None, theta=None, nscales=None, warps=None, epsilon=None, innnerIterations=None, outerIterations=None, scaleStep=None, gamma=None, medianFiltering=None, useInitialFlow=None): # real signature unknown; restored from __doc__
    """
    DualTVL1OpticalFlow_create([, tau[, lambda[, theta[, nscales[, warps[, epsilon[, innnerIterations[, outerIterations[, scaleStep[, gamma[, medianFiltering[, useInitialFlow]]]]]]]]]]]]) -> retval
    .   @brief Creates instance of cv::DualTVL1OpticalFlow
    """
    pass

def RLOFOpticalFlowParameter_create(): # real signature unknown; restored from __doc__
    """
    RLOFOpticalFlowParameter_create() -> retval
    .
    """
    pass

def SparseRLOFOpticalFlow_create(rlofParam=None, forwardBackwardThreshold=None): # real signature unknown; restored from __doc__
    """
    SparseRLOFOpticalFlow_create([, rlofParam[, forwardBackwardThreshold]]) -> retval
    .   *    @param rlofParam see setRLOFOpticalFlowParameter
    .        *    @param forwardBackwardThreshold see setForwardBackward
    """
    pass

# no classes
