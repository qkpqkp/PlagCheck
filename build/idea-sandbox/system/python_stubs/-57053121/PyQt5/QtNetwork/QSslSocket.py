# encoding: utf-8
# module PyQt5.QtNetwork
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QTcpSocket import QTcpSocket

class QSslSocket(QTcpSocket):
    """ QSslSocket(parent: QObject = None) """
    def abort(self): # real signature unknown; restored from __doc__
        """ abort(self) """
        pass

    def addCaCertificate(self, QSslCertificate): # real signature unknown; restored from __doc__
        """ addCaCertificate(self, QSslCertificate) """
        pass

    def addCaCertificates(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addCaCertificates(self, str, format: QSsl.EncodingFormat = QSsl.Pem, syntax: QRegExp.PatternSyntax = QRegExp.FixedString) -> bool
        addCaCertificates(self, Iterable[QSslCertificate])
        """
        return False

    def addDefaultCaCertificate(self, QSslCertificate): # real signature unknown; restored from __doc__
        """ addDefaultCaCertificate(QSslCertificate) """
        pass

    def addDefaultCaCertificates(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addDefaultCaCertificates(str, format: QSsl.EncodingFormat = QSsl.Pem, syntax: QRegExp.PatternSyntax = QRegExp.FixedString) -> bool
        addDefaultCaCertificates(Iterable[QSslCertificate])
        """
        return False

    def atEnd(self): # real signature unknown; restored from __doc__
        """ atEnd(self) -> bool """
        return False

    def bytesAvailable(self): # real signature unknown; restored from __doc__
        """ bytesAvailable(self) -> int """
        return 0

    def bytesToWrite(self): # real signature unknown; restored from __doc__
        """ bytesToWrite(self) -> int """
        return 0

    def caCertificates(self): # real signature unknown; restored from __doc__
        """ caCertificates(self) -> List[QSslCertificate] """
        return []

    def canReadLine(self): # real signature unknown; restored from __doc__
        """ canReadLine(self) -> bool """
        return False

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def ciphers(self): # real signature unknown; restored from __doc__
        """ ciphers(self) -> List[QSslCipher] """
        return []

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def connectToHost(self, p_str, p_int, mode, QIODevice_OpenMode=None, QIODevice_OpenModeFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ connectToHost(self, str, int, mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.ReadWrite, protocol: QAbstractSocket.NetworkLayerProtocol = QAbstractSocket.AnyIPProtocol) """
        pass

    def connectToHostEncrypted(self, p_str, p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        connectToHostEncrypted(self, str, int, mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.ReadWrite, protocol: QAbstractSocket.NetworkLayerProtocol = QAbstractSocket.AnyIPProtocol)
        connectToHostEncrypted(self, str, int, str, mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.ReadWrite, protocol: QAbstractSocket.NetworkLayerProtocol = QAbstractSocket.AnyIPProtocol)
        """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultCaCertificates(self): # real signature unknown; restored from __doc__
        """ defaultCaCertificates() -> List[QSslCertificate] """
        return []

    def defaultCiphers(self): # real signature unknown; restored from __doc__
        """ defaultCiphers() -> List[QSslCipher] """
        return []

    def disconnectFromHost(self): # real signature unknown; restored from __doc__
        """ disconnectFromHost(self) """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def encrypted(self): # real signature unknown; restored from __doc__
        """ encrypted(self) [signal] """
        pass

    def encryptedBytesAvailable(self): # real signature unknown; restored from __doc__
        """ encryptedBytesAvailable(self) -> int """
        return 0

    def encryptedBytesToWrite(self): # real signature unknown; restored from __doc__
        """ encryptedBytesToWrite(self) -> int """
        return 0

    def encryptedBytesWritten(self, p_int): # real signature unknown; restored from __doc__
        """ encryptedBytesWritten(self, int) [signal] """
        pass

    def flush(self): # real signature unknown; restored from __doc__
        """ flush(self) -> bool """
        return False

    def ignoreSslErrors(self, Iterable=None, QSslError=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        ignoreSslErrors(self)
        ignoreSslErrors(self, Iterable[QSslError])
        """
        pass

    def isEncrypted(self): # real signature unknown; restored from __doc__
        """ isEncrypted(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def localCertificate(self): # real signature unknown; restored from __doc__
        """ localCertificate(self) -> QSslCertificate """
        return QSslCertificate

    def localCertificateChain(self): # real signature unknown; restored from __doc__
        """ localCertificateChain(self) -> List[QSslCertificate] """
        return []

    def mode(self): # real signature unknown; restored from __doc__
        """ mode(self) -> QSslSocket.SslMode """
        pass

    def modeChanged(self, QSslSocket_SslMode): # real signature unknown; restored from __doc__
        """ modeChanged(self, QSslSocket.SslMode) [signal] """
        pass

    def peerCertificate(self): # real signature unknown; restored from __doc__
        """ peerCertificate(self) -> QSslCertificate """
        return QSslCertificate

    def peerCertificateChain(self): # real signature unknown; restored from __doc__
        """ peerCertificateChain(self) -> List[QSslCertificate] """
        return []

    def peerVerifyDepth(self): # real signature unknown; restored from __doc__
        """ peerVerifyDepth(self) -> int """
        return 0

    def peerVerifyError(self, QSslError): # real signature unknown; restored from __doc__
        """ peerVerifyError(self, QSslError) [signal] """
        pass

    def peerVerifyMode(self): # real signature unknown; restored from __doc__
        """ peerVerifyMode(self) -> QSslSocket.PeerVerifyMode """
        pass

    def peerVerifyName(self): # real signature unknown; restored from __doc__
        """ peerVerifyName(self) -> str """
        return ""

    def preSharedKeyAuthenticationRequired(self, QSslPreSharedKeyAuthenticator): # real signature unknown; restored from __doc__
        """ preSharedKeyAuthenticationRequired(self, QSslPreSharedKeyAuthenticator) [signal] """
        pass

    def privateKey(self): # real signature unknown; restored from __doc__
        """ privateKey(self) -> QSslKey """
        return QSslKey

    def protocol(self): # real signature unknown; restored from __doc__
        """ protocol(self) -> QSsl.SslProtocol """
        pass

    def readData(self, p_int): # real signature unknown; restored from __doc__
        """ readData(self, int) -> bytes """
        return b""

    def readLineData(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resume(self): # real signature unknown; restored from __doc__
        """ resume(self) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def sessionCipher(self): # real signature unknown; restored from __doc__
        """ sessionCipher(self) -> QSslCipher """
        return QSslCipher

    def sessionProtocol(self): # real signature unknown; restored from __doc__
        """ sessionProtocol(self) -> QSsl.SslProtocol """
        pass

    def setCaCertificates(self, Iterable, QSslCertificate=None): # real signature unknown; restored from __doc__
        """ setCaCertificates(self, Iterable[QSslCertificate]) """
        pass

    def setCiphers(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setCiphers(self, Iterable[QSslCipher])
        setCiphers(self, str)
        """
        pass

    def setDefaultCaCertificates(self, Iterable, QSslCertificate=None): # real signature unknown; restored from __doc__
        """ setDefaultCaCertificates(Iterable[QSslCertificate]) """
        pass

    def setDefaultCiphers(self, Iterable, QSslCipher=None): # real signature unknown; restored from __doc__
        """ setDefaultCiphers(Iterable[QSslCipher]) """
        pass

    def setErrorString(self, *args, **kwargs): # real signature unknown
        pass

    def setLocalAddress(self, *args, **kwargs): # real signature unknown
        pass

    def setLocalCertificate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setLocalCertificate(self, QSslCertificate)
        setLocalCertificate(self, str, format: QSsl.EncodingFormat = QSsl.Pem)
        """
        pass

    def setLocalCertificateChain(self, Iterable, QSslCertificate=None): # real signature unknown; restored from __doc__
        """ setLocalCertificateChain(self, Iterable[QSslCertificate]) """
        pass

    def setLocalPort(self, *args, **kwargs): # real signature unknown
        pass

    def setOpenMode(self, *args, **kwargs): # real signature unknown
        pass

    def setPeerAddress(self, *args, **kwargs): # real signature unknown
        pass

    def setPeerName(self, *args, **kwargs): # real signature unknown
        pass

    def setPeerPort(self, *args, **kwargs): # real signature unknown
        pass

    def setPeerVerifyDepth(self, p_int): # real signature unknown; restored from __doc__
        """ setPeerVerifyDepth(self, int) """
        pass

    def setPeerVerifyMode(self, QSslSocket_PeerVerifyMode): # real signature unknown; restored from __doc__
        """ setPeerVerifyMode(self, QSslSocket.PeerVerifyMode) """
        pass

    def setPeerVerifyName(self, p_str): # real signature unknown; restored from __doc__
        """ setPeerVerifyName(self, str) """
        pass

    def setPrivateKey(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setPrivateKey(self, QSslKey)
        setPrivateKey(self, str, algorithm: QSsl.KeyAlgorithm = QSsl.Rsa, format: QSsl.EncodingFormat = QSsl.Pem, passPhrase: Union[QByteArray, bytes, bytearray] = QByteArray())
        """
        pass

    def setProtocol(self, QSsl_SslProtocol): # real signature unknown; restored from __doc__
        """ setProtocol(self, QSsl.SslProtocol) """
        pass

    def setReadBufferSize(self, p_int): # real signature unknown; restored from __doc__
        """ setReadBufferSize(self, int) """
        pass

    def setSocketDescriptor(self, sip_voidptr, state=None, mode, QIODevice_OpenMode=None, QIODevice_OpenModeFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setSocketDescriptor(self, sip.voidptr, state: QAbstractSocket.SocketState = QAbstractSocket.ConnectedState, mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.ReadWrite) -> bool """
        pass

    def setSocketError(self, *args, **kwargs): # real signature unknown
        pass

    def setSocketOption(self, QAbstractSocket_SocketOption, Any): # real signature unknown; restored from __doc__
        """ setSocketOption(self, QAbstractSocket.SocketOption, Any) """
        pass

    def setSocketState(self, *args, **kwargs): # real signature unknown
        pass

    def setSslConfiguration(self, QSslConfiguration): # real signature unknown; restored from __doc__
        """ setSslConfiguration(self, QSslConfiguration) """
        pass

    def socketOption(self, QAbstractSocket_SocketOption): # real signature unknown; restored from __doc__
        """ socketOption(self, QAbstractSocket.SocketOption) -> Any """
        pass

    def sslConfiguration(self): # real signature unknown; restored from __doc__
        """ sslConfiguration(self) -> QSslConfiguration """
        return QSslConfiguration

    def sslErrors(self, Iterable=None, QSslError=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        sslErrors(self) -> List[QSslError]
        sslErrors(self, Iterable[QSslError]) [signal]
        """
        return []

    def sslLibraryBuildVersionNumber(self): # real signature unknown; restored from __doc__
        """ sslLibraryBuildVersionNumber() -> int """
        return 0

    def sslLibraryBuildVersionString(self): # real signature unknown; restored from __doc__
        """ sslLibraryBuildVersionString() -> str """
        return ""

    def sslLibraryVersionNumber(self): # real signature unknown; restored from __doc__
        """ sslLibraryVersionNumber() -> int """
        return 0

    def sslLibraryVersionString(self): # real signature unknown; restored from __doc__
        """ sslLibraryVersionString() -> str """
        return ""

    def startClientEncryption(self): # real signature unknown; restored from __doc__
        """ startClientEncryption(self) """
        pass

    def startServerEncryption(self): # real signature unknown; restored from __doc__
        """ startServerEncryption(self) """
        pass

    def supportedCiphers(self): # real signature unknown; restored from __doc__
        """ supportedCiphers() -> List[QSslCipher] """
        return []

    def supportsSsl(self): # real signature unknown; restored from __doc__
        """ supportsSsl() -> bool """
        return False

    def systemCaCertificates(self): # real signature unknown; restored from __doc__
        """ systemCaCertificates() -> List[QSslCertificate] """
        return []

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

    def waitForEncrypted(self, msecs=30000): # real signature unknown; restored from __doc__
        """ waitForEncrypted(self, msecs: int = 30000) -> bool """
        return False

    def waitForReadyRead(self, msecs=30000): # real signature unknown; restored from __doc__
        """ waitForReadyRead(self, msecs: int = 30000) -> bool """
        return False

    def writeData(self, bytes): # real signature unknown; restored from __doc__
        """ writeData(self, bytes) -> int """
        return 0

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    AutoVerifyPeer = 3
    QueryPeer = 1
    SslClientMode = 1
    SslServerMode = 2
    UnencryptedMode = 0
    VerifyNone = 0
    VerifyPeer = 2


