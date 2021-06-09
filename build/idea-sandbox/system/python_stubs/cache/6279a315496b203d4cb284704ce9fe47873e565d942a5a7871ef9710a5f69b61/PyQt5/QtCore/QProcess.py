# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QIODevice import QIODevice

class QProcess(QIODevice):
    """ QProcess(parent: QObject = None) """
    def arguments(self): # real signature unknown; restored from __doc__
        """ arguments(self) -> List[str] """
        return []

    def atEnd(self): # real signature unknown; restored from __doc__
        """ atEnd(self) -> bool """
        return False

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

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) """
        pass

    def closeReadChannel(self, QProcess_ProcessChannel): # real signature unknown; restored from __doc__
        """ closeReadChannel(self, QProcess.ProcessChannel) """
        pass

    def closeWriteChannel(self): # real signature unknown; restored from __doc__
        """ closeWriteChannel(self) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, QProcess_ProcessError=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        error(self) -> QProcess.ProcessError
        error(self, QProcess.ProcessError) [signal]
        """
        pass

    def errorOccurred(self, QProcess_ProcessError): # real signature unknown; restored from __doc__
        """ errorOccurred(self, QProcess.ProcessError) [signal] """
        pass

    def execute(self, p_str, Iterable=None, p_str=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        execute(str, Iterable[str]) -> int
        execute(str) -> int
        """
        return 0

    def exitCode(self): # real signature unknown; restored from __doc__
        """ exitCode(self) -> int """
        return 0

    def exitStatus(self): # real signature unknown; restored from __doc__
        """ exitStatus(self) -> QProcess.ExitStatus """
        pass

    def finished(self, p_int, QProcess_ExitStatus): # real signature unknown; restored from __doc__
        """ finished(self, int, QProcess.ExitStatus) [signal] """
        pass

    def inputChannelMode(self): # real signature unknown; restored from __doc__
        """ inputChannelMode(self) -> QProcess.InputChannelMode """
        pass

    def isSequential(self): # real signature unknown; restored from __doc__
        """ isSequential(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def kill(self): # real signature unknown; restored from __doc__
        """ kill(self) """
        pass

    def nullDevice(self): # real signature unknown; restored from __doc__
        """ nullDevice() -> str """
        return ""

    def open(self, mode, QIODevice_OpenMode=None, QIODevice_OpenModeFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ open(self, mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.ReadWrite) -> bool """
        pass

    def pid(self): # real signature unknown; restored from __doc__
        """ pid(self) -> sip.voidptr """
        pass

    def processChannelMode(self): # real signature unknown; restored from __doc__
        """ processChannelMode(self) -> QProcess.ProcessChannelMode """
        pass

    def processEnvironment(self): # real signature unknown; restored from __doc__
        """ processEnvironment(self) -> QProcessEnvironment """
        return QProcessEnvironment

    def processId(self): # real signature unknown; restored from __doc__
        """ processId(self) -> int """
        return 0

    def program(self): # real signature unknown; restored from __doc__
        """ program(self) -> str """
        return ""

    def readAllStandardError(self): # real signature unknown; restored from __doc__
        """ readAllStandardError(self) -> QByteArray """
        return QByteArray

    def readAllStandardOutput(self): # real signature unknown; restored from __doc__
        """ readAllStandardOutput(self) -> QByteArray """
        return QByteArray

    def readChannel(self): # real signature unknown; restored from __doc__
        """ readChannel(self) -> QProcess.ProcessChannel """
        pass

    def readData(self, p_int): # real signature unknown; restored from __doc__
        """ readData(self, int) -> bytes """
        return b""

    def readLineData(self, *args, **kwargs): # real signature unknown
        pass

    def readyReadStandardError(self): # real signature unknown; restored from __doc__
        """ readyReadStandardError(self) [signal] """
        pass

    def readyReadStandardOutput(self): # real signature unknown; restored from __doc__
        """ readyReadStandardOutput(self) [signal] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setArguments(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ setArguments(self, Iterable[str]) """
        pass

    def setErrorString(self, *args, **kwargs): # real signature unknown
        pass

    def setInputChannelMode(self, QProcess_InputChannelMode): # real signature unknown; restored from __doc__
        """ setInputChannelMode(self, QProcess.InputChannelMode) """
        pass

    def setOpenMode(self, *args, **kwargs): # real signature unknown
        pass

    def setProcessChannelMode(self, QProcess_ProcessChannelMode): # real signature unknown; restored from __doc__
        """ setProcessChannelMode(self, QProcess.ProcessChannelMode) """
        pass

    def setProcessEnvironment(self, QProcessEnvironment): # real signature unknown; restored from __doc__
        """ setProcessEnvironment(self, QProcessEnvironment) """
        pass

    def setProcessState(self, QProcess_ProcessState): # real signature unknown; restored from __doc__
        """ setProcessState(self, QProcess.ProcessState) """
        pass

    def setProgram(self, p_str): # real signature unknown; restored from __doc__
        """ setProgram(self, str) """
        pass

    def setReadChannel(self, QProcess_ProcessChannel): # real signature unknown; restored from __doc__
        """ setReadChannel(self, QProcess.ProcessChannel) """
        pass

    def setStandardErrorFile(self, p_str, mode, QIODevice_OpenMode=None, QIODevice_OpenModeFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setStandardErrorFile(self, str, mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.Truncate) """
        pass

    def setStandardInputFile(self, p_str): # real signature unknown; restored from __doc__
        """ setStandardInputFile(self, str) """
        pass

    def setStandardOutputFile(self, p_str, mode, QIODevice_OpenMode=None, QIODevice_OpenModeFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setStandardOutputFile(self, str, mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.Truncate) """
        pass

    def setStandardOutputProcess(self, QProcess): # real signature unknown; restored from __doc__
        """ setStandardOutputProcess(self, QProcess) """
        pass

    def setupChildProcess(self): # real signature unknown; restored from __doc__
        """ setupChildProcess(self) """
        pass

    def setWorkingDirectory(self, p_str): # real signature unknown; restored from __doc__
        """ setWorkingDirectory(self, str) """
        pass

    def start(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        start(self, str, Iterable[str], mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.ReadWrite)
        start(self, str, mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.ReadWrite)
        start(self, mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.ReadWrite)
        """
        pass

    def startDetached(self, p_str=None, Iterable=None, p_str=None, *args=None, **kwargs=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        startDetached(str, Iterable[str], str) -> Tuple[bool, int]
        startDetached(str, Iterable[str]) -> bool
        startDetached(str) -> bool
        startDetached(self) -> Tuple[bool, int]
        """
        return False

    def started(self): # real signature unknown; restored from __doc__
        """ started(self) [signal] """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QProcess.ProcessState """
        pass

    def stateChanged(self, QProcess_ProcessState): # real signature unknown; restored from __doc__
        """ stateChanged(self, QProcess.ProcessState) [signal] """
        pass

    def systemEnvironment(self): # real signature unknown; restored from __doc__
        """ systemEnvironment() -> List[str] """
        return []

    def terminate(self): # real signature unknown; restored from __doc__
        """ terminate(self) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def waitForBytesWritten(self, msecs=30000): # real signature unknown; restored from __doc__
        """ waitForBytesWritten(self, msecs: int = 30000) -> bool """
        return False

    def waitForFinished(self, msecs=30000): # real signature unknown; restored from __doc__
        """ waitForFinished(self, msecs: int = 30000) -> bool """
        return False

    def waitForReadyRead(self, msecs=30000): # real signature unknown; restored from __doc__
        """ waitForReadyRead(self, msecs: int = 30000) -> bool """
        return False

    def waitForStarted(self, msecs=30000): # real signature unknown; restored from __doc__
        """ waitForStarted(self, msecs: int = 30000) -> bool """
        return False

    def workingDirectory(self): # real signature unknown; restored from __doc__
        """ workingDirectory(self) -> str """
        return ""

    def writeData(self, bytes): # real signature unknown; restored from __doc__
        """ writeData(self, bytes) -> int """
        return 0

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    Crashed = 1
    CrashExit = 1
    FailedToStart = 0
    ForwardedChannels = 2
    ForwardedErrorChannel = 4
    ForwardedInputChannel = 1
    ForwardedOutputChannel = 3
    ManagedInputChannel = 0
    MergedChannels = 1
    NormalExit = 0
    NotRunning = 0
    ReadError = 3
    Running = 2
    SeparateChannels = 0
    StandardError = 1
    StandardOutput = 0
    Starting = 1
    Timedout = 2
    UnknownError = 5
    WriteError = 4


