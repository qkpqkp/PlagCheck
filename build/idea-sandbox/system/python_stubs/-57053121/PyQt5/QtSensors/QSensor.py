# encoding: utf-8
# module PyQt5.QtSensors
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtSensors.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QSensor(__PyQt5_QtCore.QObject):
    """ QSensor(Union[QByteArray, bytes, bytearray], parent: QObject = None) """
    def activeChanged(self): # real signature unknown; restored from __doc__
        """ activeChanged(self) [signal] """
        pass

    def addFilter(self, QSensorFilter): # real signature unknown; restored from __doc__
        """ addFilter(self, QSensorFilter) """
        pass

    def alwaysOnChanged(self): # real signature unknown; restored from __doc__
        """ alwaysOnChanged(self) [signal] """
        pass

    def availableDataRates(self): # real signature unknown; restored from __doc__
        """ availableDataRates(self) -> List[Tuple[int, int]] """
        return []

    def availableSensorsChanged(self): # real signature unknown; restored from __doc__
        """ availableSensorsChanged(self) [signal] """
        pass

    def axesOrientationMode(self): # real signature unknown; restored from __doc__
        """ axesOrientationMode(self) -> QSensor.AxesOrientationMode """
        pass

    def axesOrientationModeChanged(self, QSensor_AxesOrientationMode): # real signature unknown; restored from __doc__
        """ axesOrientationModeChanged(self, QSensor.AxesOrientationMode) [signal] """
        pass

    def bufferSize(self): # real signature unknown; restored from __doc__
        """ bufferSize(self) -> int """
        return 0

    def bufferSizeChanged(self, p_int): # real signature unknown; restored from __doc__
        """ bufferSizeChanged(self, int) [signal] """
        pass

    def busyChanged(self): # real signature unknown; restored from __doc__
        """ busyChanged(self) [signal] """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def connectToBackend(self): # real signature unknown; restored from __doc__
        """ connectToBackend(self) -> bool """
        return False

    def currentOrientation(self): # real signature unknown; restored from __doc__
        """ currentOrientation(self) -> int """
        return 0

    def currentOrientationChanged(self, p_int): # real signature unknown; restored from __doc__
        """ currentOrientationChanged(self, int) [signal] """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dataRate(self): # real signature unknown; restored from __doc__
        """ dataRate(self) -> int """
        return 0

    def dataRateChanged(self): # real signature unknown; restored from __doc__
        """ dataRateChanged(self) [signal] """
        pass

    def defaultSensorForType(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ defaultSensorForType(Union[QByteArray, bytes, bytearray]) -> QByteArray """
        pass

    def description(self): # real signature unknown; restored from __doc__
        """ description(self) -> str """
        return ""

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def efficientBufferSize(self): # real signature unknown; restored from __doc__
        """ efficientBufferSize(self) -> int """
        return 0

    def efficientBufferSizeChanged(self, p_int): # real signature unknown; restored from __doc__
        """ efficientBufferSizeChanged(self, int) [signal] """
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> int """
        return 0

    def filters(self): # real signature unknown; restored from __doc__
        """ filters(self) -> List[QSensorFilter] """
        return []

    def identifier(self): # real signature unknown; restored from __doc__
        """ identifier(self) -> QByteArray """
        pass

    def isActive(self): # real signature unknown; restored from __doc__
        """ isActive(self) -> bool """
        return False

    def isAlwaysOn(self): # real signature unknown; restored from __doc__
        """ isAlwaysOn(self) -> bool """
        return False

    def isBusy(self): # real signature unknown; restored from __doc__
        """ isBusy(self) -> bool """
        return False

    def isConnectedToBackend(self): # real signature unknown; restored from __doc__
        """ isConnectedToBackend(self) -> bool """
        return False

    def isFeatureSupported(self, QSensor_Feature): # real signature unknown; restored from __doc__
        """ isFeatureSupported(self, QSensor.Feature) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def maxBufferSize(self): # real signature unknown; restored from __doc__
        """ maxBufferSize(self) -> int """
        return 0

    def maxBufferSizeChanged(self, p_int): # real signature unknown; restored from __doc__
        """ maxBufferSizeChanged(self, int) [signal] """
        pass

    def outputRange(self): # real signature unknown; restored from __doc__
        """ outputRange(self) -> int """
        return 0

    def outputRanges(self): # real signature unknown; restored from __doc__
        """ outputRanges(self) -> List[qoutputrange] """
        return []

    def reading(self): # real signature unknown; restored from __doc__
        """ reading(self) -> QSensorReading """
        return QSensorReading

    def readingChanged(self): # real signature unknown; restored from __doc__
        """ readingChanged(self) [signal] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeFilter(self, QSensorFilter): # real signature unknown; restored from __doc__
        """ removeFilter(self, QSensorFilter) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def sensorError(self, p_int): # real signature unknown; restored from __doc__
        """ sensorError(self, int) [signal] """
        pass

    def sensorsForType(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ sensorsForType(Union[QByteArray, bytes, bytearray]) -> List[QByteArray] """
        return []

    def sensorTypes(self): # real signature unknown; restored from __doc__
        """ sensorTypes() -> List[QByteArray] """
        return []

    def setActive(self, bool): # real signature unknown; restored from __doc__
        """ setActive(self, bool) """
        pass

    def setAlwaysOn(self, bool): # real signature unknown; restored from __doc__
        """ setAlwaysOn(self, bool) """
        pass

    def setAxesOrientationMode(self, QSensor_AxesOrientationMode): # real signature unknown; restored from __doc__
        """ setAxesOrientationMode(self, QSensor.AxesOrientationMode) """
        pass

    def setBufferSize(self, p_int): # real signature unknown; restored from __doc__
        """ setBufferSize(self, int) """
        pass

    def setCurrentOrientation(self, p_int): # real signature unknown; restored from __doc__
        """ setCurrentOrientation(self, int) """
        pass

    def setDataRate(self, p_int): # real signature unknown; restored from __doc__
        """ setDataRate(self, int) """
        pass

    def setEfficientBufferSize(self, p_int): # real signature unknown; restored from __doc__
        """ setEfficientBufferSize(self, int) """
        pass

    def setIdentifier(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setIdentifier(self, Union[QByteArray, bytes, bytearray]) """
        pass

    def setMaxBufferSize(self, p_int): # real signature unknown; restored from __doc__
        """ setMaxBufferSize(self, int) """
        pass

    def setOutputRange(self, p_int): # real signature unknown; restored from __doc__
        """ setOutputRange(self, int) """
        pass

    def setSkipDuplicates(self, bool): # real signature unknown; restored from __doc__
        """ setSkipDuplicates(self, bool) """
        pass

    def setUserOrientation(self, p_int): # real signature unknown; restored from __doc__
        """ setUserOrientation(self, int) """
        pass

    def skipDuplicates(self): # real signature unknown; restored from __doc__
        """ skipDuplicates(self) -> bool """
        return False

    def skipDuplicatesChanged(self, bool): # real signature unknown; restored from __doc__
        """ skipDuplicatesChanged(self, bool) [signal] """
        pass

    def start(self): # real signature unknown; restored from __doc__
        """ start(self) -> bool """
        return False

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QByteArray """
        pass

    def userOrientation(self): # real signature unknown; restored from __doc__
        """ userOrientation(self) -> int """
        return 0

    def userOrientationChanged(self, p_int): # real signature unknown; restored from __doc__
        """ userOrientationChanged(self, int) [signal] """
        pass

    def __init__(self, Union, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    AccelerationMode = 4
    AlwaysOn = 1
    AutomaticOrientation = 1
    AxesOrientation = 6
    Buffering = 0
    FieldOfView = 3
    FixedOrientation = 0
    GeoValues = 2
    PressureSensorTemperature = 7
    SkipDuplicates = 5
    UserOrientation = 2


