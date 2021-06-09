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


class optflow_DenseRLOFOpticalFlow(__cv2.DenseOpticalFlow):
    # no doc
    def create(self, rlofParam=None, forwardBackwardThreshold=None, gridStep=None, interp_type=None, epicK=None, epicSigma=None, epicLambda=None, use_post_proc=None, fgsLambda=None, fgsSigma=None): # real signature unknown; restored from __doc__
        """
        create([, rlofParam[, forwardBackwardThreshold[, gridStep[, interp_type[, epicK[, epicSigma[, epicLambda[, use_post_proc[, fgsLambda[, fgsSigma]]]]]]]]]]) -> retval
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

    def getEPICK(self): # real signature unknown; restored from __doc__
        """
        getEPICK() -> retval
        .   K is a number of nearest-neighbor matches considered, when fitting a locally affine
        .        *    model. Usually it should be around 128. However, lower values would make the interpolation noticeably faster.
        .        *    @see ximgproc::EdgeAwareInterpolator,  setEPICK
        """
        pass

    def getEPICLambda(self): # real signature unknown; restored from __doc__
        """
        getEPICLambda() -> retval
        .   Lambda is a parameter defining the weight of the edge-aware term in geodesic distance,
        .        *    should be in the range of 0 to 1000.
        .        *    @see ximgproc::EdgeAwareInterpolator, setEPICSigma
        """
        pass

    def getEPICSigma(self): # real signature unknown; restored from __doc__
        """
        getEPICSigma() -> retval
        .   Sigma is a parameter defining how fast the weights decrease in the locally-weighted affine
        .        *  fitting. Higher values can help preserve fine details, lower values can help to get rid of noise in the
        .        *  output flow.
        .        *    @see ximgproc::EdgeAwareInterpolator, setEPICSigma
        """
        pass

    def getFgsLambda(self): # real signature unknown; restored from __doc__
        """
        getFgsLambda() -> retval
        .   Sets the respective fastGlobalSmootherFilter() parameter.
        .        *    @see ximgproc::EdgeAwareInterpolator, setFgsLambda
        """
        pass

    def getFgsSigma(self): # real signature unknown; restored from __doc__
        """
        getFgsSigma() -> retval
        .   Sets the respective fastGlobalSmootherFilter() parameter.
        .        *    @see ximgproc::EdgeAwareInterpolator, ximgproc::fastGlobalSmootherFilter, setFgsSigma
        """
        pass

    def getForwardBackward(self): # real signature unknown; restored from __doc__
        """
        getForwardBackward() -> retval
        .   @copybrief setForwardBackward
        .           @see setForwardBackward
        """
        pass

    def getGridStep(self): # real signature unknown; restored from __doc__
        """
        getGridStep() -> retval
        .   For each grid point a motion vector is computed. Some motion vectors will be removed due to the forwatd backward
        .        *  threshold (if set >0). The rest will be the base of the vector field interpolation.
        .        *    @see getForwardBackward, setGridStep
        """
        pass

    def getInterpolation(self): # real signature unknown; restored from __doc__
        """
        getInterpolation() -> retval
        .   @copybrief setInterpolation
        .        *    @see ximgproc::EdgeAwareInterpolator, setInterpolation
        """
        pass

    def getRLOFOpticalFlowParameter(self): # real signature unknown; restored from __doc__
        """
        getRLOFOpticalFlowParameter() -> retval
        .   @copybrief setRLOFOpticalFlowParameter
        .           @see optflow::RLOFOpticalFlowParameter, setRLOFOpticalFlowParameter
        """
        pass

    def getUsePostProc(self): # real signature unknown; restored from __doc__
        """
        getUsePostProc() -> retval
        .   @copybrief setUsePostProc
        .        *    @see ximgproc::fastGlobalSmootherFilter, setUsePostProc
        """
        pass

    def setEPICK(self, val): # real signature unknown; restored from __doc__
        """
        setEPICK(val) -> None
        .   @copybrief getEPICK
        .        *    @see ximgproc::EdgeAwareInterpolator, getEPICK
        """
        pass

    def setEPICLambda(self, val): # real signature unknown; restored from __doc__
        """
        setEPICLambda(val) -> None
        .   @copybrief getEPICLambda
        .        *    @see ximgproc::EdgeAwareInterpolator, getEPICLambda
        """
        pass

    def setEPICSigma(self, val): # real signature unknown; restored from __doc__
        """
        setEPICSigma(val) -> None
        .   @copybrief getEPICSigma
        .        *  @see ximgproc::EdgeAwareInterpolator, getEPICSigma
        """
        pass

    def setFgsLambda(self, val): # real signature unknown; restored from __doc__
        """
        setFgsLambda(val) -> None
        .   @copybrief getFgsLambda
        .        *    @see ximgproc::EdgeAwareInterpolator, ximgproc::fastGlobalSmootherFilter, getFgsLambda
        """
        pass

    def setFgsSigma(self, val): # real signature unknown; restored from __doc__
        """
        setFgsSigma(val) -> None
        .   @copybrief getFgsSigma
        .        *    @see ximgproc::EdgeAwareInterpolator, ximgproc::fastGlobalSmootherFilter, getFgsSigma
        """
        pass

    def setForwardBackward(self, val): # real signature unknown; restored from __doc__
        """
        setForwardBackward(val) -> None
        .   For each grid point \f$ \mathbf{x} \f$ a motion vector \f$ d_{I0,I1}(\mathbf{x}) \f$ is computed.
        .        *     If the forward backward error \f[ EP_{FB} = || d_{I0,I1} + d_{I1,I0} || \f]
        .        *     is larger than threshold given by this function then the motion vector will not be used by the following
        .        *    vector field interpolation. \f$ d_{I1,I0} \f$ denotes the backward flow. Note, the forward backward test
        .        *    will only be applied if the threshold > 0. This may results into a doubled runtime for the motion estimation.
        .        *    @see getForwardBackward, setGridStep
        """
        pass

    def setGridStep(self, val): # real signature unknown; restored from __doc__
        """
        setGridStep(val) -> None
        .   @copybrief getGridStep
        .        *    @see getGridStep
        """
        pass

    def setInterpolation(self, val): # real signature unknown; restored from __doc__
        """
        setInterpolation(val) -> None
        .   Two interpolation algorithms are supported
        .        * - **INTERP_GEO** applies the fast geodesic interpolation, see @cite Geistert2016.
        .        * - **INTERP_EPIC_RESIDUAL** applies the edge-preserving interpolation, see @cite Revaud2015,Geistert2016.
        .        * @see ximgproc::EdgeAwareInterpolator, getInterpolation
        """
        pass

    def setRLOFOpticalFlowParameter(self, val): # real signature unknown; restored from __doc__
        """
        setRLOFOpticalFlowParameter(val) -> None
        .   @see optflow::RLOFOpticalFlowParameter, getRLOFOpticalFlowParameter
        """
        pass

    def setUsePostProc(self, val): # real signature unknown; restored from __doc__
        """
        setUsePostProc(val) -> None
        .   * @see getUsePostProc
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


