# encoding: utf-8
# module PyQt5.QtNetwork
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QSslError(__sip.simplewrapper):
    """
    QSslError()
    QSslError(QSslError.SslError)
    QSslError(QSslError.SslError, QSslCertificate)
    QSslError(QSslError)
    """
    def certificate(self): # real signature unknown; restored from __doc__
        """ certificate(self) -> QSslCertificate """
        return QSslCertificate

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> QSslError.SslError """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def swap(self, QSslError): # real signature unknown; restored from __doc__
        """ swap(self, QSslError) """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
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


    AuthorityIssuerSerialNumberMismatch = 20
    CertificateBlacklisted = 24
    CertificateExpired = 6
    CertificateNotYetValid = 5
    CertificateRejected = 18
    CertificateRevoked = 13
    CertificateSignatureFailed = 4
    CertificateUntrusted = 17
    HostNameMismatch = 22
    InvalidCaCertificate = 14
    InvalidNotAfterField = 8
    InvalidNotBeforeField = 7
    InvalidPurpose = 16
    NoError = 0
    NoPeerCertificate = 21
    NoSslSupport = 23
    PathLengthExceeded = 15
    SelfSignedCertificate = 9
    SelfSignedCertificateInChain = 10
    SubjectIssuerMismatch = 19
    UnableToDecodeIssuerPublicKey = 3
    UnableToDecryptCertificateSignature = 2
    UnableToGetIssuerCertificate = 1
    UnableToGetLocalIssuerCertificate = 11
    UnableToVerifyFirstCertificate = 12
    UnspecifiedError = -1


