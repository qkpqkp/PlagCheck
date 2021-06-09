# encoding: utf-8
# module PyQt5.QtSerialPort
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtSerialPort.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


# no functions
# classes

class QSerialPort(__PyQt5_QtCore.QIODevice):
    """
    QSerialPort(parent: QObject = None)
    QSerialPort(str, parent: QObject = None)
    QSerialPort(QSerialPortInfo, parent: QObject = None)
    """
    def atEnd(self): # real signature unknown; restored from __doc__
        """ atEnd(self) -> bool """
        return False

    def baudRate(self, dir, QSerialPort_Directions=None, QSerialPort_Direction=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ baudRate(self, dir: Union[QSerialPort.Directions, QSerialPort.Direction] = QSerialPort.AllDirections) -> int """
        pass

    def baudRateChanged(self, p_int, Union, QSerialPort_Directions=None, QSerialPort_Direction=None): # real signature unknown; restored from __doc__
        """ baudRateChanged(self, int, Union[QSerialPort.Directions, QSerialPort.Direction]) [signal] """
        pass

    def breakEnabledChanged(self, bool): # real signature unknown; restored from __doc__
        """ breakEnabledChanged(self, bool) [signal] """
        pass

    def bytesAvailable(self): # real signature unknown; restored from __doc__
        """ bytesAvailable(self) -> int """
        return 0

    def bytesToWrite(self): # real signature unknown; restored from __doc__
        """ bytesToWrite(self) -> int """
        return 0

    def canReadLine(self): # real signature unknown; restored from __doc__
        """ canReadLine(self) -> bool """
        return False

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self, dir, QSerialPort_Directions=None, QSerialPort_Direction=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ clear(self, dir: Union[QSerialPort.Directions, QSerialPort.Direction] = QSerialPort.AllDirections) -> bool """
        pass

    def clearError(self): # real signature unknown; restored from __doc__
        """ clearError(self) """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dataBits(self): # real signature unknown; restored from __doc__
        """ dataBits(self) -> QSerialPort.DataBits """
        pass

    def dataBitsChanged(self, QSerialPort_DataBits): # real signature unknown; restored from __doc__
        """ dataBitsChanged(self, QSerialPort.DataBits) [signal] """
        pass

    def dataErrorPolicy(self): # real signature unknown; restored from __doc__
        """ dataErrorPolicy(self) -> QSerialPort.DataErrorPolicy """
        pass

    def dataErrorPolicyChanged(self, QSerialPort_DataErrorPolicy): # real signature unknown; restored from __doc__
        """ dataErrorPolicyChanged(self, QSerialPort.DataErrorPolicy) [signal] """
        pass

    def dataTerminalReadyChanged(self, bool): # real signature unknown; restored from __doc__
        """ dataTerminalReadyChanged(self, bool) [signal] """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, QSerialPort_SerialPortError=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        error(self) -> QSerialPort.SerialPortError
        error(self, QSerialPort.SerialPortError) [signal]
        """
        pass

    def errorOccurred(self, QSerialPort_SerialPortError): # real signature unknown; restored from __doc__
        """ errorOccurred(self, QSerialPort.SerialPortError) [signal] """
        pass

    def flowControl(self): # real signature unknown; restored from __doc__
        """ flowControl(self) -> QSerialPort.FlowControl """
        pass

    def flowControlChanged(self, QSerialPort_FlowControl): # real signature unknown; restored from __doc__
        """ flowControlChanged(self, QSerialPort.FlowControl) [signal] """
        pass

    def flush(self): # real signature unknown; restored from __doc__
        """ flush(self) -> bool """
        return False

    def handle(self): # real signature unknown; restored from __doc__
        """ handle(self) -> sip.voidptr """
        pass

    def isBreakEnabled(self): # real signature unknown; restored from __doc__
        """ isBreakEnabled(self) -> bool """
        return False

    def isDataTerminalReady(self): # real signature unknown; restored from __doc__
        """ isDataTerminalReady(self) -> bool """
        return False

    def isRequestToSend(self): # real signature unknown; restored from __doc__
        """ isRequestToSend(self) -> bool """
        return False

    def isSequential(self): # real signature unknown; restored from __doc__
        """ isSequential(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def open(self, Union, QIODevice_OpenMode=None, QIODevice_OpenModeFlag=None): # real signature unknown; restored from __doc__
        """ open(self, Union[QIODevice.OpenMode, QIODevice.OpenModeFlag]) -> bool """
        return False

    def parity(self): # real signature unknown; restored from __doc__
        """ parity(self) -> QSerialPort.Parity """
        pass

    def parityChanged(self, QSerialPort_Parity): # real signature unknown; restored from __doc__
        """ parityChanged(self, QSerialPort.Parity) [signal] """
        pass

    def pinoutSignals(self): # real signature unknown; restored from __doc__
        """ pinoutSignals(self) -> QSerialPort.PinoutSignals """
        pass

    def portName(self): # real signature unknown; restored from __doc__
        """ portName(self) -> str """
        return ""

    def readBufferSize(self): # real signature unknown; restored from __doc__
        """ readBufferSize(self) -> int """
        return 0

    def readData(self, p_int): # real signature unknown; restored from __doc__
        """ readData(self, int) -> bytes """
        return b""

    def readLineData(self, p_int): # real signature unknown; restored from __doc__
        """ readLineData(self, int) -> bytes """
        return b""

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def requestToSendChanged(self, bool): # real signature unknown; restored from __doc__
        """ requestToSendChanged(self, bool) [signal] """
        pass

    def sendBreak(self, duration=0): # real signature unknown; restored from __doc__
        """ sendBreak(self, duration: int = 0) -> bool """
        return False

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setBaudRate(self, p_int, dir, QSerialPort_Directions=None, QSerialPort_Direction=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setBaudRate(self, int, dir: Union[QSerialPort.Directions, QSerialPort.Direction] = QSerialPort.AllDirections) -> bool """
        pass

    def setBreakEnabled(self, enabled=True): # real signature unknown; restored from __doc__
        """ setBreakEnabled(self, enabled: bool = True) -> bool """
        return False

    def setDataBits(self, QSerialPort_DataBits): # real signature unknown; restored from __doc__
        """ setDataBits(self, QSerialPort.DataBits) -> bool """
        return False

    def setDataErrorPolicy(self, policy=None): # real signature unknown; restored from __doc__
        """ setDataErrorPolicy(self, policy: QSerialPort.DataErrorPolicy = QSerialPort.IgnorePolicy) -> bool """
        return False

    def setDataTerminalReady(self, bool): # real signature unknown; restored from __doc__
        """ setDataTerminalReady(self, bool) -> bool """
        return False

    def setErrorString(self, *args, **kwargs): # real signature unknown
        pass

    def setFlowControl(self, QSerialPort_FlowControl): # real signature unknown; restored from __doc__
        """ setFlowControl(self, QSerialPort.FlowControl) -> bool """
        return False

    def setOpenMode(self, *args, **kwargs): # real signature unknown
        pass

    def setParity(self, QSerialPort_Parity): # real signature unknown; restored from __doc__
        """ setParity(self, QSerialPort.Parity) -> bool """
        return False

    def setPort(self, QSerialPortInfo): # real signature unknown; restored from __doc__
        """ setPort(self, QSerialPortInfo) """
        pass

    def setPortName(self, p_str): # real signature unknown; restored from __doc__
        """ setPortName(self, str) """
        pass

    def setReadBufferSize(self, p_int): # real signature unknown; restored from __doc__
        """ setReadBufferSize(self, int) """
        pass

    def setRequestToSend(self, bool): # real signature unknown; restored from __doc__
        """ setRequestToSend(self, bool) -> bool """
        return False

    def setSettingsRestoredOnClose(self, bool): # real signature unknown; restored from __doc__
        """ setSettingsRestoredOnClose(self, bool) """
        pass

    def setStopBits(self, QSerialPort_StopBits): # real signature unknown; restored from __doc__
        """ setStopBits(self, QSerialPort.StopBits) -> bool """
        return False

    def settingsRestoredOnClose(self): # real signature unknown; restored from __doc__
        """ settingsRestoredOnClose(self) -> bool """
        return False

    def settingsRestoredOnCloseChanged(self, bool): # real signature unknown; restored from __doc__
        """ settingsRestoredOnCloseChanged(self, bool) [signal] """
        pass

    def stopBits(self): # real signature unknown; restored from __doc__
        """ stopBits(self) -> QSerialPort.StopBits """
        pass

    def stopBitsChanged(self, QSerialPort_StopBits): # real signature unknown; restored from __doc__
        """ stopBitsChanged(self, QSerialPort.StopBits) [signal] """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def waitForBytesWritten(self, msecs=30000): # real signature unknown; restored from __doc__
        """ waitForBytesWritten(self, msecs: int = 30000) -> bool """
        return False

    def waitForReadyRead(self, msecs=30000): # real signature unknown; restored from __doc__
        """ waitForReadyRead(self, msecs: int = 30000) -> bool """
        return False

    def writeData(self, bytes): # real signature unknown; restored from __doc__
        """ writeData(self, bytes) -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AllDirections = 3
    Baud115200 = 115200
    Baud1200 = 1200
    Baud19200 = 19200
    Baud2400 = 2400
    Baud38400 = 38400
    Baud4800 = 4800
    Baud57600 = 57600
    Baud9600 = 9600
    BreakConditionError = 6
    ClearToSendSignal = 128
    Data5 = 5
    Data6 = 6
    Data7 = 7
    Data8 = 8
    DataCarrierDetectSignal = 8
    DataSetReadySignal = 16
    DataTerminalReadySignal = 4
    DeviceNotFoundError = 1
    EvenParity = 2
    FramingError = 5
    HardwareControl = 1
    IgnorePolicy = 2
    Input = 1
    MarkParity = 5
    NoError = 0
    NoFlowControl = 0
    NoParity = 0
    NoSignal = 0
    NotOpenError = 13
    OddParity = 3
    OneAndHalfStop = 3
    OneStop = 1
    OpenError = 3
    Output = 2
    ParityError = 4
    PassZeroPolicy = 1
    PermissionError = 2
    ReadError = 8
    ReceivedDataSignal = 2
    RequestToSendSignal = 64
    ResourceError = 9
    RingIndicatorSignal = 32
    SecondaryReceivedDataSignal = 512
    SecondaryTransmittedDataSignal = 256
    SkipPolicy = 0
    SoftwareControl = 2
    SpaceParity = 4
    StopReceivingPolicy = 3
    TimeoutError = 12
    TransmittedDataSignal = 1
    TwoStop = 2
    UnknownBaud = -1
    UnknownDataBits = -1
    UnknownError = 11
    UnknownFlowControl = -1
    UnknownParity = -1
    UnknownPolicy = -1
    UnknownStopBits = -1
    UnsupportedOperationError = 10
    WriteError = 7


class QSerialPortInfo(__sip.simplewrapper):
    """
    QSerialPortInfo()
    QSerialPortInfo(QSerialPort)
    QSerialPortInfo(str)
    QSerialPortInfo(QSerialPortInfo)
    """
    def availablePorts(self): # real signature unknown; restored from __doc__
        """ availablePorts() -> List[QSerialPortInfo] """
        return []

    def description(self): # real signature unknown; restored from __doc__
        """ description(self) -> str """
        return ""

    def hasProductIdentifier(self): # real signature unknown; restored from __doc__
        """ hasProductIdentifier(self) -> bool """
        return False

    def hasVendorIdentifier(self): # real signature unknown; restored from __doc__
        """ hasVendorIdentifier(self) -> bool """
        return False

    def isBusy(self): # real signature unknown; restored from __doc__
        """ isBusy(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def manufacturer(self): # real signature unknown; restored from __doc__
        """ manufacturer(self) -> str """
        return ""

    def portName(self): # real signature unknown; restored from __doc__
        """ portName(self) -> str """
        return ""

    def productIdentifier(self): # real signature unknown; restored from __doc__
        """ productIdentifier(self) -> int """
        return 0

    def serialNumber(self): # real signature unknown; restored from __doc__
        """ serialNumber(self) -> str """
        return ""

    def standardBaudRates(self): # real signature unknown; restored from __doc__
        """ standardBaudRates() -> List[int] """
        return []

    def swap(self, QSerialPortInfo): # real signature unknown; restored from __doc__
        """ swap(self, QSerialPortInfo) """
        pass

    def systemLocation(self): # real signature unknown; restored from __doc__
        """ systemLocation(self) -> str """
        return ""

    def vendorIdentifier(self): # real signature unknown; restored from __doc__
        """ vendorIdentifier(self) -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values



