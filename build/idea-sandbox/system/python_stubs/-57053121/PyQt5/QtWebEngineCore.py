# encoding: utf-8
# module PyQt5.QtWebEngineCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWebEngineCore.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


# no functions
# classes

class QtWebEngineCore(__sip.simplewrapper):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QWebEngineCookieStore(__PyQt5_QtCore.QObject):
    # no doc
    def cookieAdded(self, QNetworkCookie): # real signature unknown; restored from __doc__
        """ cookieAdded(self, QNetworkCookie) [signal] """
        pass

    def cookieRemoved(self, QNetworkCookie): # real signature unknown; restored from __doc__
        """ cookieRemoved(self, QNetworkCookie) [signal] """
        pass

    def deleteAllCookies(self): # real signature unknown; restored from __doc__
        """ deleteAllCookies(self) """
        pass

    def deleteCookie(self, QNetworkCookie, origin=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ deleteCookie(self, QNetworkCookie, origin: QUrl = QUrl()) """
        pass

    def deleteSessionCookies(self): # real signature unknown; restored from __doc__
        """ deleteSessionCookies(self) """
        pass

    def loadAllCookies(self): # real signature unknown; restored from __doc__
        """ loadAllCookies(self) """
        pass

    def setCookie(self, QNetworkCookie, origin=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setCookie(self, QNetworkCookie, origin: QUrl = QUrl()) """
        pass

    def setCookieFilter(self, filterCallback, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setCookieFilter(self, filterCallback: Callable[[FilterRequest], bool] = 0) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass



class QWebEngineHttpRequest(__sip.simplewrapper):
    """
    QWebEngineHttpRequest(url: QUrl = QUrl(), method: QWebEngineHttpRequest.Method = QWebEngineHttpRequest.Method.Get)
    QWebEngineHttpRequest(QWebEngineHttpRequest)
    """
    def hasHeader(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ hasHeader(self, Union[QByteArray, bytes, bytearray]) -> bool """
        return False

    def header(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ header(self, Union[QByteArray, bytes, bytearray]) -> QByteArray """
        pass

    def headers(self): # real signature unknown; restored from __doc__
        """ headers(self) -> List[QByteArray] """
        return []

    def method(self): # real signature unknown; restored from __doc__
        """ method(self) -> QWebEngineHttpRequest.Method """
        pass

    def postData(self): # real signature unknown; restored from __doc__
        """ postData(self) -> QByteArray """
        pass

    def postRequest(self, QUrl, Dict, p_str=None, p_str=None_1): # real signature unknown; restored from __doc__
        """ postRequest(QUrl, Dict[str, str]) -> QWebEngineHttpRequest """
        return QWebEngineHttpRequest

    def setHeader(self, Union, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setHeader(self, Union[QByteArray, bytes, bytearray], Union[QByteArray, bytes, bytearray]) """
        pass

    def setMethod(self, QWebEngineHttpRequest_Method): # real signature unknown; restored from __doc__
        """ setMethod(self, QWebEngineHttpRequest.Method) """
        pass

    def setPostData(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setPostData(self, Union[QByteArray, bytes, bytearray]) """
        pass

    def setUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ setUrl(self, QUrl) """
        pass

    def swap(self, QWebEngineHttpRequest): # real signature unknown; restored from __doc__
        """ swap(self, QWebEngineHttpRequest) """
        pass

    def unsetHeader(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ unsetHeader(self, Union[QByteArray, bytes, bytearray]) """
        pass

    def url(self): # real signature unknown; restored from __doc__
        """ url(self) -> QUrl """
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


    Get = 0
    Post = 1
    __hash__ = None


class QWebEngineQuotaRequest(__sip.simplewrapper):
    """
    QWebEngineQuotaRequest()
    QWebEngineQuotaRequest(QWebEngineQuotaRequest)
    """
    def accept(self): # real signature unknown; restored from __doc__
        """ accept(self) """
        pass

    def origin(self): # real signature unknown; restored from __doc__
        """ origin(self) -> QUrl """
        pass

    def reject(self): # real signature unknown; restored from __doc__
        """ reject(self) """
        pass

    def requestedSize(self): # real signature unknown; restored from __doc__
        """ requestedSize(self) -> int """
        return 0

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, QWebEngineQuotaRequest=None): # real signature unknown; restored from __doc__ with multiple overloads
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


    __hash__ = None


class QWebEngineRegisterProtocolHandlerRequest(__sip.simplewrapper):
    """
    QWebEngineRegisterProtocolHandlerRequest()
    QWebEngineRegisterProtocolHandlerRequest(QWebEngineRegisterProtocolHandlerRequest)
    """
    def accept(self): # real signature unknown; restored from __doc__
        """ accept(self) """
        pass

    def origin(self): # real signature unknown; restored from __doc__
        """ origin(self) -> QUrl """
        pass

    def reject(self): # real signature unknown; restored from __doc__
        """ reject(self) """
        pass

    def scheme(self): # real signature unknown; restored from __doc__
        """ scheme(self) -> str """
        return ""

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, QWebEngineRegisterProtocolHandlerRequest=None): # real signature unknown; restored from __doc__ with multiple overloads
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


    __hash__ = None


class QWebEngineUrlRequestInfo(__sip.simplewrapper):
    # no doc
    def block(self, bool): # real signature unknown; restored from __doc__
        """ block(self, bool) """
        pass

    def firstPartyUrl(self): # real signature unknown; restored from __doc__
        """ firstPartyUrl(self) -> QUrl """
        pass

    def navigationType(self): # real signature unknown; restored from __doc__
        """ navigationType(self) -> QWebEngineUrlRequestInfo.NavigationType """
        pass

    def redirect(self, QUrl): # real signature unknown; restored from __doc__
        """ redirect(self, QUrl) """
        pass

    def requestMethod(self): # real signature unknown; restored from __doc__
        """ requestMethod(self) -> QByteArray """
        pass

    def requestUrl(self): # real signature unknown; restored from __doc__
        """ requestUrl(self) -> QUrl """
        pass

    def resourceType(self): # real signature unknown; restored from __doc__
        """ resourceType(self) -> QWebEngineUrlRequestInfo.ResourceType """
        pass

    def setHttpHeader(self, Union, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setHttpHeader(self, Union[QByteArray, bytes, bytearray], Union[QByteArray, bytes, bytearray]) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    NavigationTypeBackForward = 3
    NavigationTypeFormSubmitted = 2
    NavigationTypeLink = 0
    NavigationTypeOther = 5
    NavigationTypeReload = 4
    NavigationTypeTyped = 1
    ResourceTypeCspReport = 16
    ResourceTypeFavicon = 12
    ResourceTypeFontResource = 5
    ResourceTypeImage = 4
    ResourceTypeMainFrame = 0
    ResourceTypeMedia = 8
    ResourceTypeObject = 7
    ResourceTypePing = 14
    ResourceTypePluginResource = 17
    ResourceTypePrefetch = 11
    ResourceTypeScript = 3
    ResourceTypeServiceWorker = 15
    ResourceTypeSharedWorker = 10
    ResourceTypeStylesheet = 2
    ResourceTypeSubFrame = 1
    ResourceTypeSubResource = 6
    ResourceTypeUnknown = 255
    ResourceTypeWorker = 9
    ResourceTypeXhr = 13


class QWebEngineUrlRequestInterceptor(__PyQt5_QtCore.QObject):
    """ QWebEngineUrlRequestInterceptor(parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def interceptRequest(self, QWebEngineUrlRequestInfo): # real signature unknown; restored from __doc__
        """ interceptRequest(self, QWebEngineUrlRequestInfo) """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


class QWebEngineUrlRequestJob(__PyQt5_QtCore.QObject):
    # no doc
    def fail(self, QWebEngineUrlRequestJob_Error): # real signature unknown; restored from __doc__
        """ fail(self, QWebEngineUrlRequestJob.Error) """
        pass

    def initiator(self): # real signature unknown; restored from __doc__
        """ initiator(self) -> QUrl """
        pass

    def redirect(self, QUrl): # real signature unknown; restored from __doc__
        """ redirect(self, QUrl) """
        pass

    def reply(self, Union, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ reply(self, Union[QByteArray, bytes, bytearray], QIODevice) """
        pass

    def requestMethod(self): # real signature unknown; restored from __doc__
        """ requestMethod(self) -> QByteArray """
        pass

    def requestUrl(self): # real signature unknown; restored from __doc__
        """ requestUrl(self) -> QUrl """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    NoError = 0
    RequestAborted = 3
    RequestDenied = 4
    RequestFailed = 5
    UrlInvalid = 2
    UrlNotFound = 1


class QWebEngineUrlScheme(__sip.simplewrapper):
    """
    QWebEngineUrlScheme()
    QWebEngineUrlScheme(Union[QByteArray, bytes, bytearray])
    QWebEngineUrlScheme(QWebEngineUrlScheme)
    """
    def defaultPort(self): # real signature unknown; restored from __doc__
        """ defaultPort(self) -> int """
        return 0

    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> QWebEngineUrlScheme.Flags """
        pass

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> QByteArray """
        pass

    def registerScheme(self, QWebEngineUrlScheme): # real signature unknown; restored from __doc__
        """ registerScheme(QWebEngineUrlScheme) """
        pass

    def schemeByName(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ schemeByName(Union[QByteArray, bytes, bytearray]) -> QWebEngineUrlScheme """
        return QWebEngineUrlScheme

    def setDefaultPort(self, p_int): # real signature unknown; restored from __doc__
        """ setDefaultPort(self, int) """
        pass

    def setFlags(self, Union, QWebEngineUrlScheme_Flags=None, QWebEngineUrlScheme_Flag=None): # real signature unknown; restored from __doc__
        """ setFlags(self, Union[QWebEngineUrlScheme.Flags, QWebEngineUrlScheme.Flag]) """
        pass

    def setName(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setName(self, Union[QByteArray, bytes, bytearray]) """
        pass

    def setSyntax(self, QWebEngineUrlScheme_Syntax): # real signature unknown; restored from __doc__
        """ setSyntax(self, QWebEngineUrlScheme.Syntax) """
        pass

    def syntax(self): # real signature unknown; restored from __doc__
        """ syntax(self) -> QWebEngineUrlScheme.Syntax """
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


    ContentSecurityPolicyIgnored = 64
    LocalAccessAllowed = 4
    LocalScheme = 2
    NoAccessAllowed = 8
    PortUnspecified = -1
    SecureScheme = 1
    ServiceWorkersAllowed = 16
    ViewSourceAllowed = 32
    __hash__ = None


class QWebEngineUrlSchemeHandler(__PyQt5_QtCore.QObject):
    """ QWebEngineUrlSchemeHandler(parent: QObject = None) """
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

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def requestStarted(self, QWebEngineUrlRequestJob): # real signature unknown; restored from __doc__
        """ requestStarted(self, QWebEngineUrlRequestJob) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


# variables with complex values



