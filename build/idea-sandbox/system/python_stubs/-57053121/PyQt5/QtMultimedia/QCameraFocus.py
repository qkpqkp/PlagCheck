# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QCameraFocus(__PyQt5_QtCore.QObject):
    # no doc
    def customFocusPoint(self): # real signature unknown; restored from __doc__
        """ customFocusPoint(self) -> QPointF """
        pass

    def digitalZoom(self): # real signature unknown; restored from __doc__
        """ digitalZoom(self) -> float """
        return 0.0

    def digitalZoomChanged(self, p_float): # real signature unknown; restored from __doc__
        """ digitalZoomChanged(self, float) [signal] """
        pass

    def focusMode(self): # real signature unknown; restored from __doc__
        """ focusMode(self) -> QCameraFocus.FocusModes """
        pass

    def focusPointMode(self): # real signature unknown; restored from __doc__
        """ focusPointMode(self) -> QCameraFocus.FocusPointMode """
        pass

    def focusZones(self): # real signature unknown; restored from __doc__
        """ focusZones(self) -> List[QCameraFocusZone] """
        return []

    def focusZonesChanged(self): # real signature unknown; restored from __doc__
        """ focusZonesChanged(self) [signal] """
        pass

    def isAvailable(self): # real signature unknown; restored from __doc__
        """ isAvailable(self) -> bool """
        return False

    def isFocusModeSupported(self, QCameraFocus_FocusModes): # real signature unknown; restored from __doc__
        """ isFocusModeSupported(self, QCameraFocus.FocusModes) -> bool """
        return False

    def isFocusPointModeSupported(self, QCameraFocus_FocusPointMode): # real signature unknown; restored from __doc__
        """ isFocusPointModeSupported(self, QCameraFocus.FocusPointMode) -> bool """
        return False

    def maximumDigitalZoom(self): # real signature unknown; restored from __doc__
        """ maximumDigitalZoom(self) -> float """
        return 0.0

    def maximumDigitalZoomChanged(self, p_float): # real signature unknown; restored from __doc__
        """ maximumDigitalZoomChanged(self, float) [signal] """
        pass

    def maximumOpticalZoom(self): # real signature unknown; restored from __doc__
        """ maximumOpticalZoom(self) -> float """
        return 0.0

    def maximumOpticalZoomChanged(self, p_float): # real signature unknown; restored from __doc__
        """ maximumOpticalZoomChanged(self, float) [signal] """
        pass

    def opticalZoom(self): # real signature unknown; restored from __doc__
        """ opticalZoom(self) -> float """
        return 0.0

    def opticalZoomChanged(self, p_float): # real signature unknown; restored from __doc__
        """ opticalZoomChanged(self, float) [signal] """
        pass

    def setCustomFocusPoint(self, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ setCustomFocusPoint(self, Union[QPointF, QPoint]) """
        pass

    def setFocusMode(self, QCameraFocus_FocusModes): # real signature unknown; restored from __doc__
        """ setFocusMode(self, QCameraFocus.FocusModes) """
        pass

    def setFocusPointMode(self, QCameraFocus_FocusPointMode): # real signature unknown; restored from __doc__
        """ setFocusPointMode(self, QCameraFocus.FocusPointMode) """
        pass

    def zoomTo(self, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ zoomTo(self, float, float) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    AutoFocus = 8
    ContinuousFocus = 16
    FocusPointAuto = 0
    FocusPointCenter = 1
    FocusPointCustom = 3
    FocusPointFaceDetection = 2
    HyperfocalFocus = 2
    InfinityFocus = 4
    MacroFocus = 32
    ManualFocus = 1


