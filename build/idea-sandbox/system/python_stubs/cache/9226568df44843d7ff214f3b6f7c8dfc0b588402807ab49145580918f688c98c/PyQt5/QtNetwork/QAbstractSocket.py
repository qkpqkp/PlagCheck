# encoding: utf-8
# module PyQt5.QtNetwork
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QAbstractSocket(__PyQt5_QtCore.QIODevice):
    """ QAbstractSocket(QAbstractSocket.SocketType, QObject) """
    def abort(self): # real signature unknown; restored from __doc__
        """ abort(self) """
        pass

    def atEnd(self): # real signature unknown; restored from __doc__
        """ atEnd(self) -> bool """
        return False

    def bind(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        bind(self, Union[QHostAddress, QHostAddress.SpecialAddress], port: int = 0, mode: Union[QAbstractSocket.BindMode, QAbstractSocket.BindFlag] = QAbstractSocket.DefaultForPlatform) -> bool
        bind(self, port: int = 0, mode: Union[QAbstractSocket.BindMode, QAbstractSocket.BindFlag] = QAbstractSocket.DefaultForPlatform) -> bool
        """
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

    def connectToHost(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        connectToHost(self, str, int, mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.ReadWrite, protocol: QAbstractSocket.NetworkLayerProtocol = QAbstractSocket.AnyIPProtocol)
        connectToHost(self, Union[QHostAddress, QHostAddress.SpecialAddress], int, mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.ReadWrite)
        """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnected(self): # real signature unknown; restored from __doc__
        """ disconnected(self) [signal] """
        pass

    def disconnectFromHost(self): # real signature unknown; restored from __doc__
        """ disconnectFromHost(self) """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, QAbstractSocket_SocketError=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        error(self) -> QAbstractSocket.SocketError
        error(self, QAbstractSocket.SocketError) [signal]
        """
        pass

    def flush(self): # real signature unknown; restored from __doc__
        """ flush(self) -> bool """
        return False

    def hostFound(self): # real signature unknown; restored from __doc__
        """ hostFound(self) [signal] """
        pass

    def isSequential(self): # real signature unknown; restored from __doc__
        """ isSequential(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def localAddress(self): # real signature unknown; restored from __doc__
        """ localAddress(self) -> QHostAddress """
        return QHostAddress

    def localPort(self): # real signature unknown; restored from __doc__
        """ localPort(self) -> int """
        return 0

    def pauseMode(self): # real signature unknown; restored from __doc__
        """ pauseMode(self) -> QAbstractSocket.PauseModes """
        pass

    def peerAddress(self): # real signature unknown; restored from __doc__
        """ peerAddress(self) -> QHostAddress """
        return QHostAddress

    def peerName(self): # real signature unknown; restored from __doc__
        """ peerName(self) -> str """
        return ""

    def peerPort(self): # real signature unknown; restored from __doc__
        """ peerPort(self) -> int """
        return 0

    def proxy(self): # real signature unknown; restored from __doc__
        """ proxy(self) -> QNetworkProxy """
        return QNetworkProxy

    def proxyAuthenticationRequired(self, QNetworkProxy, QAuthenticator): # real signature unknown; restored from __doc__
        """ proxyAuthenticationRequired(self, QNetworkProxy, QAuthenticator) [signal] """
        pass

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

    def resume(self): # real signature unknown; restored from __doc__
        """ resume(self) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setErrorString(self, *args, **kwargs): # real signature unknown
        pass

    def setLocalAddress(self, Union, QHostAddress=None, QHostAddress_SpecialAddress=None): # real signature unknown; restored from __doc__
        """ setLocalAddress(self, Union[QHostAddress, QHostAddress.SpecialAddress]) """
        pass

    def setLocalPort(self, p_int): # real signature unknown; restored from __doc__
        """ setLocalPort(self, int) """
        pass

    def setOpenMode(self, *args, **kwargs): # real signature unknown
        pass

    def setPauseMode(self, Union, QAbstractSocket_PauseModes=None, QAbstractSocket_PauseMode=None): # real signature unknown; restored from __doc__
        """ setPauseMode(self, Union[QAbstractSocket.PauseModes, QAbstractSocket.PauseMode]) """
        pass

    def setPeerAddress(self, Union, QHostAddress=None, QHostAddress_SpecialAddress=None): # real signature unknown; restored from __doc__
        """ setPeerAddress(self, Union[QHostAddress, QHostAddress.SpecialAddress]) """
        pass

    def setPeerName(self, p_str): # real signature unknown; restored from __doc__
        """ setPeerName(self, str) """
        pass

    def setPeerPort(self, p_int): # real signature unknown; restored from __doc__
        """ setPeerPort(self, int) """
        pass

    def setProxy(self, QNetworkProxy): # real signature unknown; restored from __doc__
        """ setProxy(self, QNetworkProxy) """
        pass

    def setReadBufferSize(self, p_int): # real signature unknown; restored from __doc__
        """ setReadBufferSize(self, int) """
        pass

    def setSocketDescriptor(self, sip_voidptr, state=None, mode, QIODevice_OpenMode=None, QIODevice_OpenModeFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setSocketDescriptor(self, sip.voidptr, state: QAbstractSocket.SocketState = QAbstractSocket.ConnectedState, mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.ReadWrite) -> bool """
        pass

    def setSocketError(self, QAbstractSocket_SocketError): # real signature unknown; restored from __doc__
        """ setSocketError(self, QAbstractSocket.SocketError) """
        pass

    def setSocketOption(self, QAbstractSocket_SocketOption, Any): # real signature unknown; restored from __doc__
        """ setSocketOption(self, QAbstractSocket.SocketOption, Any) """
        pass

    def setSocketState(self, QAbstractSocket_SocketState): # real signature unknown; restored from __doc__
        """ setSocketState(self, QAbstractSocket.SocketState) """
        pass

    def socketDescriptor(self): # real signature unknown; restored from __doc__
        """ socketDescriptor(self) -> sip.voidptr """
        pass

    def socketOption(self, QAbstractSocket_SocketOption): # real signature unknown; restored from __doc__
        """ socketOption(self, QAbstractSocket.SocketOption) -> Any """
        pass

    def socketType(self): # real signature unknown; restored from __doc__
        """ socketType(self) -> QAbstractSocket.SocketType """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QAbstractSocket.SocketState """
        pass

    def stateChanged(self, QAbstractSocket_SocketState): # real signature unknown; restored from __doc__
        """ stateChanged(self, QAbstractSocket.SocketState) [signal] """
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

    def __init__(self, QAbstractSocket_SocketType, QObject): # real signature unknown; restored from __doc__
        pass

    AddressInUseError = 8
    AnyIPProtocol = 2
    BoundState = 4
    ClosingState = 6
    ConnectedState = 3
    ConnectingState = 2
    ConnectionRefusedError = 0
    DatagramTooLargeError = 6
    DefaultForPlatform = 0
    DontShareAddress = 2
    HostLookupState = 1
    HostNotFoundError = 2
    IPv4Protocol = 0
    IPv6Protocol = 1
    KeepAliveOption = 1
    ListeningState = 5
    LowDelayOption = 0
    MulticastLoopbackOption = 3
    MulticastTtlOption = 2
    NetworkError = 7
    OperationError = 19
    PathMtuSocketOption = 7
    PauseNever = 0
    PauseOnSslErrors = 1
    ProxyAuthenticationRequiredError = 12
    ProxyConnectionClosedError = 15
    ProxyConnectionRefusedError = 14
    ProxyConnectionTimeoutError = 16
    ProxyNotFoundError = 17
    ProxyProtocolError = 18
    ReceiveBufferSizeSocketOption = 6
    RemoteHostClosedError = 1
    ReuseAddressHint = 4
    SctpSocket = 2
    SendBufferSizeSocketOption = 5
    ShareAddress = 1
    SocketAccessError = 3
    SocketAddressNotAvailableError = 9
    SocketResourceError = 4
    SocketTimeoutError = 5
    SslHandshakeFailedError = 13
    SslInternalError = 20
    SslInvalidUserDataError = 21
    TcpSocket = 0
    TemporaryError = 22
    TypeOfServiceOption = 4
    UdpSocket = 1
    UnconnectedState = 0
    UnfinishedSocketOperationError = 11
    UnknownNetworkLayerProtocol = -1
    UnknownSocketError = -1
    UnknownSocketType = -1
    UnsupportedSocketOperationError = 10


