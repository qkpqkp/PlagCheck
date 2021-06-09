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


class plot_Plot2d(__cv2.Algorithm):
    # no doc
    def create(self, data): # real signature unknown; restored from __doc__
        """
        create(data) -> retval
        .   * @brief Creates Plot2d object
        .                *
        .                * @param data \f$1xN\f$ or \f$Nx1\f$ matrix containing \f$Y\f$ values of points to plot. \f$X\f$ values
        .                * will be equal to indexes of correspondind elements in data matrix.
        
        
        
        create(dataX, dataY) -> retval
        .   * @brief Creates Plot2d object
        .                *
        .                * @param dataX \f$1xN\f$ or \f$Nx1\f$ matrix \f$X\f$ values of points to plot.
        .                * @param dataY \f$1xN\f$ or \f$Nx1\f$ matrix containing \f$Y\f$ values of points to plot.
        """
        pass

    def render(self, _plotResult=None): # real signature unknown; restored from __doc__
        """
        render([, _plotResult]) -> _plotResult
        .
        """
        pass

    def setGridLinesNumber(self, gridLinesNumber): # real signature unknown; restored from __doc__
        """
        setGridLinesNumber(gridLinesNumber) -> None
        .
        """
        pass

    def setInvertOrientation(self, _invertOrientation): # real signature unknown; restored from __doc__
        """
        setInvertOrientation(_invertOrientation) -> None
        .
        """
        pass

    def setMaxX(self, _plotMaxX): # real signature unknown; restored from __doc__
        """
        setMaxX(_plotMaxX) -> None
        .
        """
        pass

    def setMaxY(self, _plotMaxY): # real signature unknown; restored from __doc__
        """
        setMaxY(_plotMaxY) -> None
        .
        """
        pass

    def setMinX(self, _plotMinX): # real signature unknown; restored from __doc__
        """
        setMinX(_plotMinX) -> None
        .
        """
        pass

    def setMinY(self, _plotMinY): # real signature unknown; restored from __doc__
        """
        setMinY(_plotMinY) -> None
        .
        """
        pass

    def setNeedPlotLine(self, _needPlotLine): # real signature unknown; restored from __doc__
        """
        setNeedPlotLine(_needPlotLine) -> None
        .   * @brief Switches data visualization mode
        .                *
        .                * @param _needPlotLine if true then neighbour plot points will be connected by lines.
        .                * In other case data will be plotted as a set of standalone points.
        """
        pass

    def setPlotAxisColor(self, _plotAxisColor): # real signature unknown; restored from __doc__
        """
        setPlotAxisColor(_plotAxisColor) -> None
        .
        """
        pass

    def setPlotBackgroundColor(self, _plotBackgroundColor): # real signature unknown; restored from __doc__
        """
        setPlotBackgroundColor(_plotBackgroundColor) -> None
        .
        """
        pass

    def setPlotGridColor(self, _plotGridColor): # real signature unknown; restored from __doc__
        """
        setPlotGridColor(_plotGridColor) -> None
        .
        """
        pass

    def setPlotLineColor(self, _plotLineColor): # real signature unknown; restored from __doc__
        """
        setPlotLineColor(_plotLineColor) -> None
        .
        """
        pass

    def setPlotLineWidth(self, _plotLineWidth): # real signature unknown; restored from __doc__
        """
        setPlotLineWidth(_plotLineWidth) -> None
        .
        """
        pass

    def setPlotSize(self, _plotSizeWidth, _plotSizeHeight): # real signature unknown; restored from __doc__
        """
        setPlotSize(_plotSizeWidth, _plotSizeHeight) -> None
        .
        """
        pass

    def setPlotTextColor(self, _plotTextColor): # real signature unknown; restored from __doc__
        """
        setPlotTextColor(_plotTextColor) -> None
        .
        """
        pass

    def setPointIdxToPrint(self, pointIdx): # real signature unknown; restored from __doc__
        """
        setPointIdxToPrint(pointIdx) -> None
        .   * @brief Sets the index of a point which coordinates will be printed on the top left corner of the plot (if ShowText flag is true).
        .                *
        .                * @param pointIdx index of the required point in data array.
        """
        pass

    def setShowGrid(self, needShowGrid): # real signature unknown; restored from __doc__
        """
        setShowGrid(needShowGrid) -> None
        .
        """
        pass

    def setShowText(self, needShowText): # real signature unknown; restored from __doc__
        """
        setShowText(needShowText) -> None
        .
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


