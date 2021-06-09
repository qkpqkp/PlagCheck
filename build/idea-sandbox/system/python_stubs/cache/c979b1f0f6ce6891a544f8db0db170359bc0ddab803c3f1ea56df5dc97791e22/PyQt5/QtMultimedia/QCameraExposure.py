# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QCameraExposure(__PyQt5_QtCore.QObject):
    # no doc
    def aperture(self): # real signature unknown; restored from __doc__
        """ aperture(self) -> float """
        return 0.0

    def apertureChanged(self, p_float): # real signature unknown; restored from __doc__
        """ apertureChanged(self, float) [signal] """
        pass

    def apertureRangeChanged(self): # real signature unknown; restored from __doc__
        """ apertureRangeChanged(self) [signal] """
        pass

    def exposureCompensation(self): # real signature unknown; restored from __doc__
        """ exposureCompensation(self) -> float """
        return 0.0

    def exposureCompensationChanged(self, p_float): # real signature unknown; restored from __doc__
        """ exposureCompensationChanged(self, float) [signal] """
        pass

    def exposureMode(self): # real signature unknown; restored from __doc__
        """ exposureMode(self) -> QCameraExposure.ExposureMode """
        pass

    def flashMode(self): # real signature unknown; restored from __doc__
        """ flashMode(self) -> QCameraExposure.FlashModes """
        pass

    def flashReady(self, bool): # real signature unknown; restored from __doc__
        """ flashReady(self, bool) [signal] """
        pass

    def isAvailable(self): # real signature unknown; restored from __doc__
        """ isAvailable(self) -> bool """
        return False

    def isExposureModeSupported(self, QCameraExposure_ExposureMode): # real signature unknown; restored from __doc__
        """ isExposureModeSupported(self, QCameraExposure.ExposureMode) -> bool """
        return False

    def isFlashModeSupported(self, Union, QCameraExposure_FlashModes=None, QCameraExposure_FlashMode=None): # real signature unknown; restored from __doc__
        """ isFlashModeSupported(self, Union[QCameraExposure.FlashModes, QCameraExposure.FlashMode]) -> bool """
        return False

    def isFlashReady(self): # real signature unknown; restored from __doc__
        """ isFlashReady(self) -> bool """
        return False

    def isMeteringModeSupported(self, QCameraExposure_MeteringMode): # real signature unknown; restored from __doc__
        """ isMeteringModeSupported(self, QCameraExposure.MeteringMode) -> bool """
        return False

    def isoSensitivity(self): # real signature unknown; restored from __doc__
        """ isoSensitivity(self) -> int """
        return 0

    def isoSensitivityChanged(self, p_int): # real signature unknown; restored from __doc__
        """ isoSensitivityChanged(self, int) [signal] """
        pass

    def meteringMode(self): # real signature unknown; restored from __doc__
        """ meteringMode(self) -> QCameraExposure.MeteringMode """
        pass

    def requestedAperture(self): # real signature unknown; restored from __doc__
        """ requestedAperture(self) -> float """
        return 0.0

    def requestedIsoSensitivity(self): # real signature unknown; restored from __doc__
        """ requestedIsoSensitivity(self) -> int """
        return 0

    def requestedShutterSpeed(self): # real signature unknown; restored from __doc__
        """ requestedShutterSpeed(self) -> float """
        return 0.0

    def setAutoAperture(self): # real signature unknown; restored from __doc__
        """ setAutoAperture(self) """
        pass

    def setAutoIsoSensitivity(self): # real signature unknown; restored from __doc__
        """ setAutoIsoSensitivity(self) """
        pass

    def setAutoShutterSpeed(self): # real signature unknown; restored from __doc__
        """ setAutoShutterSpeed(self) """
        pass

    def setExposureCompensation(self, p_float): # real signature unknown; restored from __doc__
        """ setExposureCompensation(self, float) """
        pass

    def setExposureMode(self, QCameraExposure_ExposureMode): # real signature unknown; restored from __doc__
        """ setExposureMode(self, QCameraExposure.ExposureMode) """
        pass

    def setFlashMode(self, Union, QCameraExposure_FlashModes=None, QCameraExposure_FlashMode=None): # real signature unknown; restored from __doc__
        """ setFlashMode(self, Union[QCameraExposure.FlashModes, QCameraExposure.FlashMode]) """
        pass

    def setManualAperture(self, p_float): # real signature unknown; restored from __doc__
        """ setManualAperture(self, float) """
        pass

    def setManualIsoSensitivity(self, p_int): # real signature unknown; restored from __doc__
        """ setManualIsoSensitivity(self, int) """
        pass

    def setManualShutterSpeed(self, p_float): # real signature unknown; restored from __doc__
        """ setManualShutterSpeed(self, float) """
        pass

    def setMeteringMode(self, QCameraExposure_MeteringMode): # real signature unknown; restored from __doc__
        """ setMeteringMode(self, QCameraExposure.MeteringMode) """
        pass

    def setSpotMeteringPoint(self, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ setSpotMeteringPoint(self, Union[QPointF, QPoint]) """
        pass

    def shutterSpeed(self): # real signature unknown; restored from __doc__
        """ shutterSpeed(self) -> float """
        return 0.0

    def shutterSpeedChanged(self, p_float): # real signature unknown; restored from __doc__
        """ shutterSpeedChanged(self, float) [signal] """
        pass

    def shutterSpeedRangeChanged(self): # real signature unknown; restored from __doc__
        """ shutterSpeedRangeChanged(self) [signal] """
        pass

    def spotMeteringPoint(self): # real signature unknown; restored from __doc__
        """ spotMeteringPoint(self) -> QPointF """
        pass

    def supportedApertures(self): # real signature unknown; restored from __doc__
        """ supportedApertures(self) -> Tuple[List[float], bool] """
        pass

    def supportedIsoSensitivities(self): # real signature unknown; restored from __doc__
        """ supportedIsoSensitivities(self) -> Tuple[List[int], bool] """
        pass

    def supportedShutterSpeeds(self): # real signature unknown; restored from __doc__
        """ supportedShutterSpeeds(self) -> Tuple[List[float], bool] """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    ExposureAction = 11
    ExposureAuto = 0
    ExposureBacklight = 4
    ExposureBarcode = 20
    ExposureBeach = 8
    ExposureCandlelight = 19
    ExposureFireworks = 17
    ExposureLandscape = 12
    ExposureLargeAperture = 9
    ExposureManual = 1
    ExposureModeVendor = 1000
    ExposureNight = 3
    ExposureNightPortrait = 13
    ExposureParty = 18
    ExposurePortrait = 2
    ExposureSmallAperture = 10
    ExposureSnow = 7
    ExposureSports = 6
    ExposureSpotlight = 5
    ExposureSteadyPhoto = 16
    ExposureSunset = 15
    ExposureTheatre = 14
    FlashAuto = 1
    FlashFill = 16
    FlashManual = 512
    FlashOff = 2
    FlashOn = 4
    FlashRedEyeReduction = 8
    FlashSlowSyncFrontCurtain = 128
    FlashSlowSyncRearCurtain = 256
    FlashTorch = 32
    FlashVideoLight = 64
    MeteringAverage = 2
    MeteringMatrix = 1
    MeteringSpot = 3


