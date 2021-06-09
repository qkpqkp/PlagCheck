# encoding: utf-8
# module PyQt5.QtWebSockets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWebSockets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


# no functions
# classes

class QMaskGenerator(__PyQt5_QtCore.QObject):
    """ QMaskGenerator(parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def nextMask(self): # real signature unknown; restored from __doc__
        """ nextMask(self) -> int """
        return 0

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def seed(self): # real signature unknown; restored from __doc__
        """ seed(self) -> bool """
        return False

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


class QWebSocket(__PyQt5_QtCore.QObject):
    """ QWebSocket(origin: str = '', version: QWebSocketProtocol.Version = QWebSocketProtocol.VersionLatest, parent: QObject = None) """
    def abort(self): # real signature unknown; restored from __doc__
        """ abort(self) """
        pass

    def aboutToClose(self): # real signature unknown; restored from __doc__
        """ aboutToClose(self) [signal] """
        pass

    def binaryFrameReceived(self, Union, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ binaryFrameReceived(self, Union[QByteArray, bytes, bytearray], bool) [signal] """
        pass

    def binaryMessageReceived(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ binaryMessageReceived(self, Union[QByteArray, bytes, bytearray]) [signal] """
        pass

    def bytesToWrite(self): # real signature unknown; restored from __doc__
        """ bytesToWrite(self) -> int """
        return 0

    def bytesWritten(self, p_int): # real signature unknown; restored from __doc__
        """ bytesWritten(self, int) [signal] """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def close(self, closeCode=None, reason=''): # real signature unknown; restored from __doc__
        """ close(self, closeCode: QWebSocketProtocol.CloseCode = QWebSocketProtocol.CloseCodeNormal, reason: str = '') """
        pass

    def closeCode(self): # real signature unknown; restored from __doc__
        """ closeCode(self) -> QWebSocketProtocol.CloseCode """
        pass

    def closeReason(self): # real signature unknown; restored from __doc__
        """ closeReason(self) -> str """
        return ""

    def connected(self): # real signature unknown; restored from __doc__
        """ connected(self) [signal] """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnected(self): # real signature unknown; restored from __doc__
        """ disconnected(self) [signal] """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, QAbstractSocket_SocketError=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        error(self) -> QAbstractSocket.SocketError
        error(self, QAbstractSocket.SocketError) [signal]
        """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def flush(self): # real signature unknown; restored from __doc__
        """ flush(self) -> bool """
        return False

    def ignoreSslErrors(self, Iterable=None, QSslError=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        ignoreSslErrors(self, Iterable[QSslError])
        ignoreSslErrors(self)
        """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def localAddress(self): # real signature unknown; restored from __doc__
        """ localAddress(self) -> QHostAddress """
        pass

    def localPort(self): # real signature unknown; restored from __doc__
        """ localPort(self) -> int """
        return 0

    def maskGenerator(self): # real signature unknown; restored from __doc__
        """ maskGenerator(self) -> QMaskGenerator """
        return QMaskGenerator

    def open(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        open(self, QUrl)
        open(self, QNetworkRequest)
        """
        pass

    def origin(self): # real signature unknown; restored from __doc__
        """ origin(self) -> str """
        return ""

    def pauseMode(self): # real signature unknown; restored from __doc__
        """ pauseMode(self) -> QAbstractSocket.PauseModes """
        pass

    def peerAddress(self): # real signature unknown; restored from __doc__
        """ peerAddress(self) -> QHostAddress """
        pass

    def peerName(self): # real signature unknown; restored from __doc__
        """ peerName(self) -> str """
        return ""

    def peerPort(self): # real signature unknown; restored from __doc__
        """ peerPort(self) -> int """
        return 0

    def ping(self, payload, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ ping(self, payload: Union[QByteArray, bytes, bytearray] = QByteArray()) """
        pass

    def pong(self, p_int, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ pong(self, int, Union[QByteArray, bytes, bytearray]) [signal] """
        pass

    def preSharedKeyAuthenticationRequired(self, QSslPreSharedKeyAuthenticator): # real signature unknown; restored from __doc__
        """ preSharedKeyAuthenticationRequired(self, QSslPreSharedKeyAuthenticator) [signal] """
        pass

    def proxy(self): # real signature unknown; restored from __doc__
        """ proxy(self) -> QNetworkProxy """
        pass

    def proxyAuthenticationRequired(self, QNetworkProxy, QAuthenticator): # real signature unknown; restored from __doc__
        """ proxyAuthenticationRequired(self, QNetworkProxy, QAuthenticator) [signal] """
        pass

    def readBufferSize(self): # real signature unknown; restored from __doc__
        """ readBufferSize(self) -> int """
        return 0

    def readChannelFinished(self): # real signature unknown; restored from __doc__
        """ readChannelFinished(self) [signal] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def request(self): # real signature unknown; restored from __doc__
        """ request(self) -> QNetworkRequest """
        pass

    def requestUrl(self): # real signature unknown; restored from __doc__
        """ requestUrl(self) -> QUrl """
        pass

    def resourceName(self): # real signature unknown; restored from __doc__
        """ resourceName(self) -> str """
        return ""

    def resume(self): # real signature unknown; restored from __doc__
        """ resume(self) """
        pass

    def sendBinaryMessage(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ sendBinaryMessage(self, Union[QByteArray, bytes, bytearray]) -> int """
        return 0

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def sendTextMessage(self, p_str): # real signature unknown; restored from __doc__
        """ sendTextMessage(self, str) -> int """
        return 0

    def setMaskGenerator(self, QMaskGenerator): # real signature unknown; restored from __doc__
        """ setMaskGenerator(self, QMaskGenerator) """
        pass

    def setPauseMode(self, Union, QAbstractSocket_PauseModes=None, QAbstractSocket_PauseMode=None): # real signature unknown; restored from __doc__
        """ setPauseMode(self, Union[QAbstractSocket.PauseModes, QAbstractSocket.PauseMode]) """
        pass

    def setProxy(self, QNetworkProxy): # real signature unknown; restored from __doc__
        """ setProxy(self, QNetworkProxy) """
        pass

    def setReadBufferSize(self, p_int): # real signature unknown; restored from __doc__
        """ setReadBufferSize(self, int) """
        pass

    def setSslConfiguration(self, QSslConfiguration): # real signature unknown; restored from __doc__
        """ setSslConfiguration(self, QSslConfiguration) """
        pass

    def sslConfiguration(self): # real signature unknown; restored from __doc__
        """ sslConfiguration(self) -> QSslConfiguration """
        pass

    def sslErrors(self, Iterable, QSslError=None): # real signature unknown; restored from __doc__
        """ sslErrors(self, Iterable[QSslError]) [signal] """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QAbstractSocket.SocketState """
        pass

    def stateChanged(self, QAbstractSocket_SocketState): # real signature unknown; restored from __doc__
        """ stateChanged(self, QAbstractSocket.SocketState) [signal] """
        pass

    def textFrameReceived(self, p_str, bool): # real signature unknown; restored from __doc__
        """ textFrameReceived(self, str, bool) [signal] """
        pass

    def textMessageReceived(self, p_str): # real signature unknown; restored from __doc__
        """ textMessageReceived(self, str) [signal] """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def version(self): # real signature unknown; restored from __doc__
        """ version(self) -> QWebSocketProtocol.Version """
        pass

    def __init__(self, origin='', version=None, parent=None): # real signature unknown; restored from __doc__
        pass


class QWebSocketCorsAuthenticator(__sip.simplewrapper):
    """
    QWebSocketCorsAuthenticator(str)
    QWebSocketCorsAuthenticator(QWebSocketCorsAuthenticator)
    """
    def allowed(self): # real signature unknown; restored from __doc__
        """ allowed(self) -> bool """
        return False

    def origin(self): # real signature unknown; restored from __doc__
        """ origin(self) -> str """
        return ""

    def setAllowed(self, bool): # real signature unknown; restored from __doc__
        """ setAllowed(self, bool) """
        pass

    def swap(self, QWebSocketCorsAuthenticator): # real signature unknown; restored from __doc__
        """ swap(self, QWebSocketCorsAuthenticator) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QWebSocketProtocol(__sip.simplewrapper):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    CloseCodeAbnormalDisconnection = 1006
    CloseCodeBadOperation = 1011
    CloseCodeDatatypeNotSupported = 1003
    CloseCodeGoingAway = 1001
    CloseCodeMissingExtension = 1010
    CloseCodeMissingStatusCode = 1005
    CloseCodeNormal = 1000
    CloseCodePolicyViolated = 1008
    CloseCodeProtocolError = 1002
    CloseCodeReserved1004 = 1004
    CloseCodeTlsHandshakeFailed = 1015
    CloseCodeTooMuchData = 1009
    CloseCodeWrongDatatype = 1007
    Version0 = 0
    Version13 = 13
    Version4 = 4
    Version5 = 5
    Version6 = 6
    Version7 = 7
    Version8 = 8
    VersionLatest = 13
    VersionUnknown = -1


class QWebSocketServer(__PyQt5_QtCore.QObject):
    """ QWebSocketServer(str, QWebSocketServer.SslMode, parent: QObject = None) """
    def acceptError(self, QAbstractSocket_SocketError): # real signature unknown; restored from __doc__
        """ acceptError(self, QAbstractSocket.SocketError) [signal] """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) """
        pass

    def closed(self): # real signature unknown; restored from __doc__
        """ closed(self) [signal] """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> QWebSocketProtocol.CloseCode """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def handleConnection(self, QTcpSocket): # real signature unknown; restored from __doc__
        """ handleConnection(self, QTcpSocket) """
        pass

    def hasPendingConnections(self): # real signature unknown; restored from __doc__
        """ hasPendingConnections(self) -> bool """
        return False

    def isListening(self): # real signature unknown; restored from __doc__
        """ isListening(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def listen(self, address, QHostAddress=None, QHostAddress_SpecialAddress=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ listen(self, address: Union[QHostAddress, QHostAddress.SpecialAddress] = QHostAddress.Any, port: int = 0) -> bool """
        pass

    def maxPendingConnections(self): # real signature unknown; restored from __doc__
        """ maxPendingConnections(self) -> int """
        return 0

    def nativeDescriptor(self): # real signature unknown; restored from __doc__
        """ nativeDescriptor(self) -> sip.voidptr """
        pass

    def newConnection(self): # real signature unknown; restored from __doc__
        """ newConnection(self) [signal] """
        pass

    def nextPendingConnection(self): # real signature unknown; restored from __doc__
        """ nextPendingConnection(self) -> QWebSocket """
        return QWebSocket

    def originAuthenticationRequired(self, QWebSocketCorsAuthenticator): # real signature unknown; restored from __doc__
        """ originAuthenticationRequired(self, QWebSocketCorsAuthenticator) [signal] """
        pass

    def pauseAccepting(self): # real signature unknown; restored from __doc__
        """ pauseAccepting(self) """
        pass

    def peerVerifyError(self, QSslError): # real signature unknown; restored from __doc__
        """ peerVerifyError(self, QSslError) [signal] """
        pass

    def preSharedKeyAuthenticationRequired(self, QSslPreSharedKeyAuthenticator): # real signature unknown; restored from __doc__
        """ preSharedKeyAuthenticationRequired(self, QSslPreSharedKeyAuthenticator) [signal] """
        pass

    def proxy(self): # real signature unknown; restored from __doc__
        """ proxy(self) -> QNetworkProxy """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resumeAccepting(self): # real signature unknown; restored from __doc__
        """ resumeAccepting(self) """
        pass

    def secureMode(self): # real signature unknown; restored from __doc__
        """ secureMode(self) -> QWebSocketServer.SslMode """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def serverAddress(self): # real signature unknown; restored from __doc__
        """ serverAddress(self) -> QHostAddress """
        pass

    def serverError(self, QWebSocketProtocol_CloseCode): # real signature unknown; restored from __doc__
        """ serverError(self, QWebSocketProtocol.CloseCode) [signal] """
        pass

    def serverName(self): # real signature unknown; restored from __doc__
        """ serverName(self) -> str """
        return ""

    def serverPort(self): # real signature unknown; restored from __doc__
        """ serverPort(self) -> int """
        return 0

    def serverUrl(self): # real signature unknown; restored from __doc__
        """ serverUrl(self) -> QUrl """
        pass

    def setMaxPendingConnections(self, p_int): # real signature unknown; restored from __doc__
        """ setMaxPendingConnections(self, int) """
        pass

    def setNativeDescriptor(self, sip_voidptr): # real signature unknown; restored from __doc__
        """ setNativeDescriptor(self, sip.voidptr) -> bool """
        return False

    def setProxy(self, QNetworkProxy): # real signature unknown; restored from __doc__
        """ setProxy(self, QNetworkProxy) """
        pass

    def setServerName(self, p_str): # real signature unknown; restored from __doc__
        """ setServerName(self, str) """
        pass

    def setSocketDescriptor(self, p_int): # real signature unknown; restored from __doc__
        """ setSocketDescriptor(self, int) -> bool """
        return False

    def setSslConfiguration(self, QSslConfiguration): # real signature unknown; restored from __doc__
        """ setSslConfiguration(self, QSslConfiguration) """
        pass

    def socketDescriptor(self): # real signature unknown; restored from __doc__
        """ socketDescriptor(self) -> int """
        return 0

    def sslConfiguration(self): # real signature unknown; restored from __doc__
        """ sslConfiguration(self) -> QSslConfiguration """
        pass

    def sslErrors(self, Iterable, QSslError=None): # real signature unknown; restored from __doc__
        """ sslErrors(self, Iterable[QSslError]) [signal] """
        pass

    def supportedVersions(self): # real signature unknown; restored from __doc__
        """ supportedVersions(self) -> List[QWebSocketProtocol.Version] """
        return []

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, p_str, QWebSocketServer_SslMode, parent=None): # real signature unknown; restored from __doc__
        pass

    NonSecureMode = 1
    SecureMode = 0


# variables with complex values



