# encoding: utf-8
# module PyQt5.QtNetwork
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QNetworkReply(__PyQt5_QtCore.QIODevice):
    """ QNetworkReply(parent: QObject = None) """
    def abort(self): # real signature unknown; restored from __doc__
        """ abort(self) """
        pass

    def attribute(self, QNetworkRequest_Attribute): # real signature unknown; restored from __doc__
        """ attribute(self, QNetworkRequest.Attribute) -> Any """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def downloadProgress(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ downloadProgress(self, int, int) [signal] """
        pass

    def encrypted(self): # real signature unknown; restored from __doc__
        """ encrypted(self) [signal] """
        pass

    def error(self, QNetworkReply_NetworkError=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        error(self) -> QNetworkReply.NetworkError
        error(self, QNetworkReply.NetworkError) [signal]
        """
        pass

    def finished(self): # real signature unknown; restored from __doc__
        """ finished(self) [signal] """
        pass

    def hasRawHeader(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ hasRawHeader(self, Union[QByteArray, bytes, bytearray]) -> bool """
        return False

    def header(self, QNetworkRequest_KnownHeaders): # real signature unknown; restored from __doc__
        """ header(self, QNetworkRequest.KnownHeaders) -> Any """
        pass

    def ignoreSslErrors(self, Iterable=None, QSslError=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        ignoreSslErrors(self)
        ignoreSslErrors(self, Iterable[QSslError])
        """
        pass

    def ignoreSslErrorsImplementation(self, Iterable, QSslError=None): # real signature unknown; restored from __doc__
        """ ignoreSslErrorsImplementation(self, Iterable[QSslError]) """
        pass

    def isFinished(self): # real signature unknown; restored from __doc__
        """ isFinished(self) -> bool """
        return False

    def isRunning(self): # real signature unknown; restored from __doc__
        """ isRunning(self) -> bool """
        return False

    def isSequential(self): # real signature unknown; restored from __doc__
        """ isSequential(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def manager(self): # real signature unknown; restored from __doc__
        """ manager(self) -> QNetworkAccessManager """
        return QNetworkAccessManager

    def metaDataChanged(self): # real signature unknown; restored from __doc__
        """ metaDataChanged(self) [signal] """
        pass

    def operation(self): # real signature unknown; restored from __doc__
        """ operation(self) -> QNetworkAccessManager.Operation """
        pass

    def preSharedKeyAuthenticationRequired(self, QSslPreSharedKeyAuthenticator): # real signature unknown; restored from __doc__
        """ preSharedKeyAuthenticationRequired(self, QSslPreSharedKeyAuthenticator) [signal] """
        pass

    def rawHeader(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ rawHeader(self, Union[QByteArray, bytes, bytearray]) -> QByteArray """
        pass

    def rawHeaderList(self): # real signature unknown; restored from __doc__
        """ rawHeaderList(self) -> List[QByteArray] """
        return []

    def rawHeaderPairs(self): # real signature unknown; restored from __doc__
        """ rawHeaderPairs(self) -> List[Tuple[QByteArray, QByteArray]] """
        return []

    def readBufferSize(self): # real signature unknown; restored from __doc__
        """ readBufferSize(self) -> int """
        return 0

    def readData(self, *args, **kwargs): # real signature unknown
        pass

    def readLineData(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def redirectAllowed(self): # real signature unknown; restored from __doc__
        """ redirectAllowed(self) [signal] """
        pass

    def redirected(self, QUrl): # real signature unknown; restored from __doc__
        """ redirected(self, QUrl) [signal] """
        pass

    def request(self): # real signature unknown; restored from __doc__
        """ request(self) -> QNetworkRequest """
        return QNetworkRequest

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAttribute(self, QNetworkRequest_Attribute, Any): # real signature unknown; restored from __doc__
        """ setAttribute(self, QNetworkRequest.Attribute, Any) """
        pass

    def setError(self, QNetworkReply_NetworkError, p_str): # real signature unknown; restored from __doc__
        """ setError(self, QNetworkReply.NetworkError, str) """
        pass

    def setErrorString(self, *args, **kwargs): # real signature unknown
        pass

    def setFinished(self, bool): # real signature unknown; restored from __doc__
        """ setFinished(self, bool) """
        pass

    def setHeader(self, QNetworkRequest_KnownHeaders, Any): # real signature unknown; restored from __doc__
        """ setHeader(self, QNetworkRequest.KnownHeaders, Any) """
        pass

    def setOpenMode(self, *args, **kwargs): # real signature unknown
        pass

    def setOperation(self, QNetworkAccessManager_Operation): # real signature unknown; restored from __doc__
        """ setOperation(self, QNetworkAccessManager.Operation) """
        pass

    def setRawHeader(self, Union, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setRawHeader(self, Union[QByteArray, bytes, bytearray], Union[QByteArray, bytes, bytearray]) """
        pass

    def setReadBufferSize(self, p_int): # real signature unknown; restored from __doc__
        """ setReadBufferSize(self, int) """
        pass

    def setRequest(self, QNetworkRequest): # real signature unknown; restored from __doc__
        """ setRequest(self, QNetworkRequest) """
        pass

    def setSslConfiguration(self, QSslConfiguration): # real signature unknown; restored from __doc__
        """ setSslConfiguration(self, QSslConfiguration) """
        pass

    def setSslConfigurationImplementation(self, QSslConfiguration): # real signature unknown; restored from __doc__
        """ setSslConfigurationImplementation(self, QSslConfiguration) """
        pass

    def setUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ setUrl(self, QUrl) """
        pass

    def sslConfiguration(self): # real signature unknown; restored from __doc__
        """ sslConfiguration(self) -> QSslConfiguration """
        return QSslConfiguration

    def sslConfigurationImplementation(self, QSslConfiguration): # real signature unknown; restored from __doc__
        """ sslConfigurationImplementation(self, QSslConfiguration) """
        pass

    def sslErrors(self, Iterable, QSslError=None): # real signature unknown; restored from __doc__
        """ sslErrors(self, Iterable[QSslError]) [signal] """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def uploadProgress(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ uploadProgress(self, int, int) [signal] """
        pass

    def url(self): # real signature unknown; restored from __doc__
        """ url(self) -> QUrl """
        pass

    def writeData(self, bytes): # real signature unknown; restored from __doc__
        """ writeData(self, bytes) -> int """
        return 0

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    AuthenticationRequiredError = 204
    BackgroundRequestNotAllowedError = 9
    ConnectionRefusedError = 1
    ContentAccessDenied = 201
    ContentConflictError = 206
    ContentGoneError = 207
    ContentNotFoundError = 203
    ContentOperationNotPermittedError = 202
    ContentReSendError = 205
    HostNotFoundError = 3
    InsecureRedirectError = 11
    InternalServerError = 401
    NetworkSessionFailedError = 8
    NoError = 0
    OperationCanceledError = 5
    OperationNotImplementedError = 402
    ProtocolFailure = 399
    ProtocolInvalidOperationError = 302
    ProtocolUnknownError = 301
    ProxyAuthenticationRequiredError = 105
    ProxyConnectionClosedError = 102
    ProxyConnectionRefusedError = 101
    ProxyNotFoundError = 103
    ProxyTimeoutError = 104
    RemoteHostClosedError = 2
    ServiceUnavailableError = 403
    SslHandshakeFailedError = 6
    TemporaryNetworkFailureError = 7
    TimeoutError = 4
    TooManyRedirectsError = 10
    UnknownContentError = 299
    UnknownNetworkError = 99
    UnknownProxyError = 199
    UnknownServerError = 499


