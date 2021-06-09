# encoding: utf-8
# module PyQt5.QtNetwork
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QNetworkAccessManager(__PyQt5_QtCore.QObject):
    """ QNetworkAccessManager(parent: QObject = None) """
    def activeConfiguration(self): # real signature unknown; restored from __doc__
        """ activeConfiguration(self) -> QNetworkConfiguration """
        return QNetworkConfiguration

    def addStrictTransportSecurityHosts(self, Iterable, QHstsPolicy=None): # real signature unknown; restored from __doc__
        """ addStrictTransportSecurityHosts(self, Iterable[QHstsPolicy]) """
        pass

    def authenticationRequired(self, QNetworkReply, QAuthenticator): # real signature unknown; restored from __doc__
        """ authenticationRequired(self, QNetworkReply, QAuthenticator) [signal] """
        pass

    def cache(self): # real signature unknown; restored from __doc__
        """ cache(self) -> QAbstractNetworkCache """
        return QAbstractNetworkCache

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clearAccessCache(self): # real signature unknown; restored from __doc__
        """ clearAccessCache(self) """
        pass

    def clearConnectionCache(self): # real signature unknown; restored from __doc__
        """ clearConnectionCache(self) """
        pass

    def configuration(self): # real signature unknown; restored from __doc__
        """ configuration(self) -> QNetworkConfiguration """
        return QNetworkConfiguration

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def connectToHost(self, p_str, port=80): # real signature unknown; restored from __doc__
        """ connectToHost(self, str, port: int = 80) """
        pass

    def connectToHostEncrypted(self, p_str, port=443, sslConfiguration=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ connectToHostEncrypted(self, str, port: int = 443, sslConfiguration: QSslConfiguration = QSslConfiguration.defaultConfiguration()) """
        pass

    def cookieJar(self): # real signature unknown; restored from __doc__
        """ cookieJar(self) -> QNetworkCookieJar """
        return QNetworkCookieJar

    def createRequest(self, QNetworkAccessManager_Operation, QNetworkRequest, device=None): # real signature unknown; restored from __doc__
        """ createRequest(self, QNetworkAccessManager.Operation, QNetworkRequest, device: QIODevice = None) -> QNetworkReply """
        return QNetworkReply

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def deleteResource(self, QNetworkRequest): # real signature unknown; restored from __doc__
        """ deleteResource(self, QNetworkRequest) -> QNetworkReply """
        return QNetworkReply

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def enableStrictTransportSecurityStore(self, bool, storeDir=''): # real signature unknown; restored from __doc__
        """ enableStrictTransportSecurityStore(self, bool, storeDir: str = '') """
        pass

    def encrypted(self, QNetworkReply): # real signature unknown; restored from __doc__
        """ encrypted(self, QNetworkReply) [signal] """
        pass

    def finished(self, QNetworkReply): # real signature unknown; restored from __doc__
        """ finished(self, QNetworkReply) [signal] """
        pass

    def get(self, QNetworkRequest): # real signature unknown; restored from __doc__
        """ get(self, QNetworkRequest) -> QNetworkReply """
        return QNetworkReply

    def head(self, QNetworkRequest): # real signature unknown; restored from __doc__
        """ head(self, QNetworkRequest) -> QNetworkReply """
        return QNetworkReply

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isStrictTransportSecurityEnabled(self): # real signature unknown; restored from __doc__
        """ isStrictTransportSecurityEnabled(self) -> bool """
        return False

    def isStrictTransportSecurityStoreEnabled(self): # real signature unknown; restored from __doc__
        """ isStrictTransportSecurityStoreEnabled(self) -> bool """
        return False

    def networkAccessible(self): # real signature unknown; restored from __doc__
        """ networkAccessible(self) -> QNetworkAccessManager.NetworkAccessibility """
        pass

    def networkAccessibleChanged(self, QNetworkAccessManager_NetworkAccessibility): # real signature unknown; restored from __doc__
        """ networkAccessibleChanged(self, QNetworkAccessManager.NetworkAccessibility) [signal] """
        pass

    def post(self, QNetworkRequest, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        post(self, QNetworkRequest, QIODevice) -> QNetworkReply
        post(self, QNetworkRequest, Union[QByteArray, bytes, bytearray]) -> QNetworkReply
        post(self, QNetworkRequest, QHttpMultiPart) -> QNetworkReply
        """
        return QNetworkReply

    def preSharedKeyAuthenticationRequired(self, QNetworkReply, QSslPreSharedKeyAuthenticator): # real signature unknown; restored from __doc__
        """ preSharedKeyAuthenticationRequired(self, QNetworkReply, QSslPreSharedKeyAuthenticator) [signal] """
        pass

    def proxy(self): # real signature unknown; restored from __doc__
        """ proxy(self) -> QNetworkProxy """
        return QNetworkProxy

    def proxyAuthenticationRequired(self, QNetworkProxy, QAuthenticator): # real signature unknown; restored from __doc__
        """ proxyAuthenticationRequired(self, QNetworkProxy, QAuthenticator) [signal] """
        pass

    def proxyFactory(self): # real signature unknown; restored from __doc__
        """ proxyFactory(self) -> QNetworkProxyFactory """
        return QNetworkProxyFactory

    def put(self, QNetworkRequest, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        put(self, QNetworkRequest, QIODevice) -> QNetworkReply
        put(self, QNetworkRequest, Union[QByteArray, bytes, bytearray]) -> QNetworkReply
        put(self, QNetworkRequest, QHttpMultiPart) -> QNetworkReply
        """
        return QNetworkReply

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def redirectPolicy(self): # real signature unknown; restored from __doc__
        """ redirectPolicy(self) -> QNetworkRequest.RedirectPolicy """
        pass

    def sendCustomRequest(self, QNetworkRequest, Union, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        """
        sendCustomRequest(self, QNetworkRequest, Union[QByteArray, bytes, bytearray], data: QIODevice = None) -> QNetworkReply
        sendCustomRequest(self, QNetworkRequest, Union[QByteArray, bytes, bytearray], Union[QByteArray, bytes, bytearray]) -> QNetworkReply
        sendCustomRequest(self, QNetworkRequest, Union[QByteArray, bytes, bytearray], QHttpMultiPart) -> QNetworkReply
        """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCache(self, QAbstractNetworkCache): # real signature unknown; restored from __doc__
        """ setCache(self, QAbstractNetworkCache) """
        pass

    def setConfiguration(self, QNetworkConfiguration): # real signature unknown; restored from __doc__
        """ setConfiguration(self, QNetworkConfiguration) """
        pass

    def setCookieJar(self, QNetworkCookieJar): # real signature unknown; restored from __doc__
        """ setCookieJar(self, QNetworkCookieJar) """
        pass

    def setNetworkAccessible(self, QNetworkAccessManager_NetworkAccessibility): # real signature unknown; restored from __doc__
        """ setNetworkAccessible(self, QNetworkAccessManager.NetworkAccessibility) """
        pass

    def setProxy(self, QNetworkProxy): # real signature unknown; restored from __doc__
        """ setProxy(self, QNetworkProxy) """
        pass

    def setProxyFactory(self, QNetworkProxyFactory): # real signature unknown; restored from __doc__
        """ setProxyFactory(self, QNetworkProxyFactory) """
        pass

    def setRedirectPolicy(self, QNetworkRequest_RedirectPolicy): # real signature unknown; restored from __doc__
        """ setRedirectPolicy(self, QNetworkRequest.RedirectPolicy) """
        pass

    def setStrictTransportSecurityEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setStrictTransportSecurityEnabled(self, bool) """
        pass

    def sslErrors(self, QNetworkReply, Iterable, QSslError=None): # real signature unknown; restored from __doc__
        """ sslErrors(self, QNetworkReply, Iterable[QSslError]) [signal] """
        pass

    def strictTransportSecurityHosts(self): # real signature unknown; restored from __doc__
        """ strictTransportSecurityHosts(self) -> List[QHstsPolicy] """
        return []

    def supportedSchemes(self): # real signature unknown; restored from __doc__
        """ supportedSchemes(self) -> List[str] """
        return []

    def supportedSchemesImplementation(self): # real signature unknown; restored from __doc__
        """ supportedSchemesImplementation(self) -> List[str] """
        return []

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    Accessible = 1
    CustomOperation = 6
    DeleteOperation = 5
    GetOperation = 2
    HeadOperation = 1
    NotAccessible = 0
    PostOperation = 4
    PutOperation = 3
    UnknownAccessibility = -1


