# encoding: utf-8
# module PyQt5.QtNetwork
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QSslConfiguration(__sip.simplewrapper):
    """
    QSslConfiguration()
    QSslConfiguration(QSslConfiguration)
    """
    def allowedNextProtocols(self): # real signature unknown; restored from __doc__
        """ allowedNextProtocols(self) -> List[QByteArray] """
        return []

    def backendConfiguration(self): # real signature unknown; restored from __doc__
        """ backendConfiguration(self) -> Dict[QByteArray, Any] """
        return {}

    def caCertificates(self): # real signature unknown; restored from __doc__
        """ caCertificates(self) -> List[QSslCertificate] """
        return []

    def ciphers(self): # real signature unknown; restored from __doc__
        """ ciphers(self) -> List[QSslCipher] """
        return []

    def defaultConfiguration(self): # real signature unknown; restored from __doc__
        """ defaultConfiguration() -> QSslConfiguration """
        return QSslConfiguration

    def diffieHellmanParameters(self): # real signature unknown; restored from __doc__
        """ diffieHellmanParameters(self) -> QSslDiffieHellmanParameters """
        return QSslDiffieHellmanParameters

    def ellipticCurves(self): # real signature unknown; restored from __doc__
        """ ellipticCurves(self) -> List[QSslEllipticCurve] """
        return []

    def ephemeralServerKey(self): # real signature unknown; restored from __doc__
        """ ephemeralServerKey(self) -> QSslKey """
        return QSslKey

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def localCertificate(self): # real signature unknown; restored from __doc__
        """ localCertificate(self) -> QSslCertificate """
        return QSslCertificate

    def localCertificateChain(self): # real signature unknown; restored from __doc__
        """ localCertificateChain(self) -> List[QSslCertificate] """
        return []

    def nextNegotiatedProtocol(self): # real signature unknown; restored from __doc__
        """ nextNegotiatedProtocol(self) -> QByteArray """
        pass

    def nextProtocolNegotiationStatus(self): # real signature unknown; restored from __doc__
        """ nextProtocolNegotiationStatus(self) -> QSslConfiguration.NextProtocolNegotiationStatus """
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

    def peerVerifyMode(self): # real signature unknown; restored from __doc__
        """ peerVerifyMode(self) -> QSslSocket.PeerVerifyMode """
        pass

    def preSharedKeyIdentityHint(self): # real signature unknown; restored from __doc__
        """ preSharedKeyIdentityHint(self) -> QByteArray """
        pass

    def privateKey(self): # real signature unknown; restored from __doc__
        """ privateKey(self) -> QSslKey """
        return QSslKey

    def protocol(self): # real signature unknown; restored from __doc__
        """ protocol(self) -> QSsl.SslProtocol """
        pass

    def sessionCipher(self): # real signature unknown; restored from __doc__
        """ sessionCipher(self) -> QSslCipher """
        return QSslCipher

    def sessionProtocol(self): # real signature unknown; restored from __doc__
        """ sessionProtocol(self) -> QSsl.SslProtocol """
        pass

    def sessionTicket(self): # real signature unknown; restored from __doc__
        """ sessionTicket(self) -> QByteArray """
        pass

    def sessionTicketLifeTimeHint(self): # real signature unknown; restored from __doc__
        """ sessionTicketLifeTimeHint(self) -> int """
        return 0

    def setAllowedNextProtocols(self, Iterable, Union=None, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setAllowedNextProtocols(self, Iterable[Union[QByteArray, bytes, bytearray]]) """
        pass

    def setBackendConfiguration(self, backendConfiguration, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setBackendConfiguration(self, backendConfiguration: Dict[Union[QByteArray, bytes, bytearray], Any] = {}) """
        pass

    def setBackendConfigurationOption(self, Union, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setBackendConfigurationOption(self, Union[QByteArray, bytes, bytearray], Any) """
        pass

    def setCaCertificates(self, Iterable, QSslCertificate=None): # real signature unknown; restored from __doc__
        """ setCaCertificates(self, Iterable[QSslCertificate]) """
        pass

    def setCiphers(self, Iterable, QSslCipher=None): # real signature unknown; restored from __doc__
        """ setCiphers(self, Iterable[QSslCipher]) """
        pass

    def setDefaultConfiguration(self, QSslConfiguration): # real signature unknown; restored from __doc__
        """ setDefaultConfiguration(QSslConfiguration) """
        pass

    def setDiffieHellmanParameters(self, QSslDiffieHellmanParameters): # real signature unknown; restored from __doc__
        """ setDiffieHellmanParameters(self, QSslDiffieHellmanParameters) """
        pass

    def setEllipticCurves(self, Iterable, QSslEllipticCurve=None): # real signature unknown; restored from __doc__
        """ setEllipticCurves(self, Iterable[QSslEllipticCurve]) """
        pass

    def setLocalCertificate(self, QSslCertificate): # real signature unknown; restored from __doc__
        """ setLocalCertificate(self, QSslCertificate) """
        pass

    def setLocalCertificateChain(self, Iterable, QSslCertificate=None): # real signature unknown; restored from __doc__
        """ setLocalCertificateChain(self, Iterable[QSslCertificate]) """
        pass

    def setPeerVerifyDepth(self, p_int): # real signature unknown; restored from __doc__
        """ setPeerVerifyDepth(self, int) """
        pass

    def setPeerVerifyMode(self, QSslSocket_PeerVerifyMode): # real signature unknown; restored from __doc__
        """ setPeerVerifyMode(self, QSslSocket.PeerVerifyMode) """
        pass

    def setPreSharedKeyIdentityHint(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setPreSharedKeyIdentityHint(self, Union[QByteArray, bytes, bytearray]) """
        pass

    def setPrivateKey(self, QSslKey): # real signature unknown; restored from __doc__
        """ setPrivateKey(self, QSslKey) """
        pass

    def setProtocol(self, QSsl_SslProtocol): # real signature unknown; restored from __doc__
        """ setProtocol(self, QSsl.SslProtocol) """
        pass

    def setSessionTicket(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setSessionTicket(self, Union[QByteArray, bytes, bytearray]) """
        pass

    def setSslOption(self, QSsl_SslOption, bool): # real signature unknown; restored from __doc__
        """ setSslOption(self, QSsl.SslOption, bool) """
        pass

    def supportedCiphers(self): # real signature unknown; restored from __doc__
        """ supportedCiphers() -> List[QSslCipher] """
        return []

    def supportedEllipticCurves(self): # real signature unknown; restored from __doc__
        """ supportedEllipticCurves() -> List[QSslEllipticCurve] """
        return []

    def swap(self, QSslConfiguration): # real signature unknown; restored from __doc__
        """ swap(self, QSslConfiguration) """
        pass

    def systemCaCertificates(self): # real signature unknown; restored from __doc__
        """ systemCaCertificates() -> List[QSslCertificate] """
        return []

    def testSslOption(self, QSsl_SslOption): # real signature unknown; restored from __doc__
        """ testSslOption(self, QSsl.SslOption) -> bool """
        return False

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, QSslConfiguration=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    NextProtocolHttp1_1 = b'http/1.1'
    NextProtocolNegotiationNegotiated = 1
    NextProtocolNegotiationNone = 0
    NextProtocolNegotiationUnsupported = 2
    NextProtocolSpdy3_0 = b'spdy/3'
    __hash__ = None


