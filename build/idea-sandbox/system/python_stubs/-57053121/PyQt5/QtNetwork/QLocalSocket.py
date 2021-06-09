# encoding: utf-8
# module PyQt5.QtNetwork
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QLocalSocket(__PyQt5_QtCore.QIODevice):
    """ QLocalSocket(parent: QObject = None) """
    def abort(self): # real signature unknown; restored from __doc__
        """ abort(self) """
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

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) """
        pass

    def connected(self): # real signature unknown; restored from __doc__
        """ connected(self) [signal] """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def connectToServer(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        connectToServer(self, str, mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.ReadWrite)
        connectToServer(self, mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.ReadWrite)
        """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnected(self): # real signature unknown; restored from __doc__
        """ disconnected(self) [signal] """
        pass

    def disconnectFromServer(self): # real signature unknown; restored from __doc__
        """ disconnectFromServer(self) """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, QLocalSocket_LocalSocketError=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        error(self) -> QLocalSocket.LocalSocketError
        error(self, QLocalSocket.LocalSocketError) [signal]
        """
        pass

    def flush(self): # real signature unknown; restored from __doc__
        """ flush(self) -> bool """
        return False

    def fullServerName(self): # real signature unknown; restored from __doc__
        """ fullServerName(self) -> str """
        return ""

    def isSequential(self): # real signature unknown; restored from __doc__
        """ isSequential(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def open(self, mode, QIODevice_OpenMode=None, QIODevice_OpenModeFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ open(self, mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.ReadWrite) -> bool """
        pass

    def readBufferSize(self): # real signature unknown; restored from __doc__
        """ readBufferSize(self) -> int """
        return 0

    def readData(self, p_int): # real signature unknown; restored from __doc__
        """ readData(self, int) -> bytes """
        return b""

    def readLineData(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def serverName(self): # real signature unknown; restored from __doc__
        """ serverName(self) -> str """
        return ""

    def setErrorString(self, *args, **kwargs): # real signature unknown
        pass

    def setOpenMode(self, *args, **kwargs): # real signature unknown
        pass

    def setReadBufferSize(self, p_int): # real signature unknown; restored from __doc__
        """ setReadBufferSize(self, int) """
        pass

    def setServerName(self, p_str): # real signature unknown; restored from __doc__
        """ setServerName(self, str) """
        pass

    def setSocketDescriptor(self, sip_voidptr, state=None, mode, QIODevice_OpenMode=None, QIODevice_OpenModeFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setSocketDescriptor(self, sip.voidptr, state: QLocalSocket.LocalSocketState = QLocalSocket.ConnectedState, mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.ReadWrite) -> bool """
        pass

    def socketDescriptor(self): # real signature unknown; restored from __doc__
        """ socketDescriptor(self) -> sip.voidptr """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QLocalSocket.LocalSocketState """
        pass

    def stateChanged(self, QLocalSocket_LocalSocketState): # real signature unknown; restored from __doc__
        """ stateChanged(self, QLocalSocket.LocalSocketState) [signal] """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def waitForBytesWritten(self, msecs=30000): # real signature unknown; restored from __doc__
        """ waitForBytesWritten(self, msecs: int = 30000) -> bool """
        return False

    def waitForConnected(self, msecs=30000): # real signature unknown; restored from __doc__
        """ waitForConnected(self, msecs: int = 30000) -> bool """
        return False

    def waitForDisconnected(self, msecs=30000): # real signature unknown; restored from __doc__
        """ waitForDisconnected(self, msecs: int = 30000) -> bool """
        return False

    def waitForReadyRead(self, msecs=30000): # real signature unknown; restored from __doc__
        """ waitForReadyRead(self, msecs: int = 30000) -> bool """
        return False

    def writeData(self, bytes): # real signature unknown; restored from __doc__
        """ writeData(self, bytes) -> int """
        return 0

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    ClosingState = 6
    ConnectedState = 3
    ConnectingState = 2
    ConnectionError = 7
    ConnectionRefusedError = 0
    DatagramTooLargeError = 6
    OperationError = 19
    PeerClosedError = 1
    ServerNotFoundError = 2
    SocketAccessError = 3
    SocketResourceError = 4
    SocketTimeoutError = 5
    UnconnectedState = 0
    UnknownSocketError = -1
    UnsupportedSocketOperationError = 10


