# encoding: utf-8
# module PyQt5.QtWebEngine
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWebEngine.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


# no functions
# classes

class QQuickWebEngineProfile(__PyQt5_QtCore.QObject):
    """ QQuickWebEngineProfile(parent: QObject = None) """
    def cachePath(self): # real signature unknown; restored from __doc__
        """ cachePath(self) -> str """
        return ""

    def cachePathChanged(self): # real signature unknown; restored from __doc__
        """ cachePathChanged(self) [signal] """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clearHttpCache(self): # real signature unknown; restored from __doc__
        """ clearHttpCache(self) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def cookieStore(self): # real signature unknown; restored from __doc__
        """ cookieStore(self) -> QWebEngineCookieStore """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultProfile(self): # real signature unknown; restored from __doc__
        """ defaultProfile() -> QQuickWebEngineProfile """
        return QQuickWebEngineProfile

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def httpAcceptLanguage(self): # real signature unknown; restored from __doc__
        """ httpAcceptLanguage(self) -> str """
        return ""

    def httpAcceptLanguageChanged(self): # real signature unknown; restored from __doc__
        """ httpAcceptLanguageChanged(self) [signal] """
        pass

    def httpCacheMaximumSize(self): # real signature unknown; restored from __doc__
        """ httpCacheMaximumSize(self) -> int """
        return 0

    def httpCacheMaximumSizeChanged(self): # real signature unknown; restored from __doc__
        """ httpCacheMaximumSizeChanged(self) [signal] """
        pass

    def httpCacheType(self): # real signature unknown; restored from __doc__
        """ httpCacheType(self) -> QQuickWebEngineProfile.HttpCacheType """
        pass

    def httpCacheTypeChanged(self): # real signature unknown; restored from __doc__
        """ httpCacheTypeChanged(self) [signal] """
        pass

    def httpUserAgent(self): # real signature unknown; restored from __doc__
        """ httpUserAgent(self) -> str """
        return ""

    def httpUserAgentChanged(self): # real signature unknown; restored from __doc__
        """ httpUserAgentChanged(self) [signal] """
        pass

    def installUrlSchemeHandler(self, Union, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ installUrlSchemeHandler(self, Union[QByteArray, bytes, bytearray], QWebEngineUrlSchemeHandler) """
        pass

    def isOffTheRecord(self): # real signature unknown; restored from __doc__
        """ isOffTheRecord(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isSpellCheckEnabled(self): # real signature unknown; restored from __doc__
        """ isSpellCheckEnabled(self) -> bool """
        return False

    def offTheRecordChanged(self): # real signature unknown; restored from __doc__
        """ offTheRecordChanged(self) [signal] """
        pass

    def persistentCookiesPolicy(self): # real signature unknown; restored from __doc__
        """ persistentCookiesPolicy(self) -> QQuickWebEngineProfile.PersistentCookiesPolicy """
        pass

    def persistentCookiesPolicyChanged(self): # real signature unknown; restored from __doc__
        """ persistentCookiesPolicyChanged(self) [signal] """
        pass

    def persistentStoragePath(self): # real signature unknown; restored from __doc__
        """ persistentStoragePath(self) -> str """
        return ""

    def persistentStoragePathChanged(self): # real signature unknown; restored from __doc__
        """ persistentStoragePathChanged(self) [signal] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeAllUrlSchemeHandlers(self): # real signature unknown; restored from __doc__
        """ removeAllUrlSchemeHandlers(self) """
        pass

    def removeUrlScheme(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ removeUrlScheme(self, Union[QByteArray, bytes, bytearray]) """
        pass

    def removeUrlSchemeHandler(self, QWebEngineUrlSchemeHandler): # real signature unknown; restored from __doc__
        """ removeUrlSchemeHandler(self, QWebEngineUrlSchemeHandler) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCachePath(self, p_str): # real signature unknown; restored from __doc__
        """ setCachePath(self, str) """
        pass

    def setHttpAcceptLanguage(self, p_str): # real signature unknown; restored from __doc__
        """ setHttpAcceptLanguage(self, str) """
        pass

    def setHttpCacheMaximumSize(self, p_int): # real signature unknown; restored from __doc__
        """ setHttpCacheMaximumSize(self, int) """
        pass

    def setHttpCacheType(self, QQuickWebEngineProfile_HttpCacheType): # real signature unknown; restored from __doc__
        """ setHttpCacheType(self, QQuickWebEngineProfile.HttpCacheType) """
        pass

    def setHttpUserAgent(self, p_str): # real signature unknown; restored from __doc__
        """ setHttpUserAgent(self, str) """
        pass

    def setOffTheRecord(self, bool): # real signature unknown; restored from __doc__
        """ setOffTheRecord(self, bool) """
        pass

    def setPersistentCookiesPolicy(self, QQuickWebEngineProfile_PersistentCookiesPolicy): # real signature unknown; restored from __doc__
        """ setPersistentCookiesPolicy(self, QQuickWebEngineProfile.PersistentCookiesPolicy) """
        pass

    def setPersistentStoragePath(self, p_str): # real signature unknown; restored from __doc__
        """ setPersistentStoragePath(self, str) """
        pass

    def setRequestInterceptor(self, QWebEngineUrlRequestInterceptor): # real signature unknown; restored from __doc__
        """ setRequestInterceptor(self, QWebEngineUrlRequestInterceptor) """
        pass

    def setSpellCheckEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setSpellCheckEnabled(self, bool) """
        pass

    def setSpellCheckLanguages(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ setSpellCheckLanguages(self, Iterable[str]) """
        pass

    def setStorageName(self, p_str): # real signature unknown; restored from __doc__
        """ setStorageName(self, str) """
        pass

    def spellCheckEnabledChanged(self): # real signature unknown; restored from __doc__
        """ spellCheckEnabledChanged(self) [signal] """
        pass

    def spellCheckLanguages(self): # real signature unknown; restored from __doc__
        """ spellCheckLanguages(self) -> List[str] """
        return []

    def spellCheckLanguagesChanged(self): # real signature unknown; restored from __doc__
        """ spellCheckLanguagesChanged(self) [signal] """
        pass

    def storageName(self): # real signature unknown; restored from __doc__
        """ storageName(self) -> str """
        return ""

    def storageNameChanged(self): # real signature unknown; restored from __doc__
        """ storageNameChanged(self) [signal] """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def urlSchemeHandler(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ urlSchemeHandler(self, Union[QByteArray, bytes, bytearray]) -> QWebEngineUrlSchemeHandler """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    AllowPersistentCookies = 1
    DiskHttpCache = 1
    ForcePersistentCookies = 2
    MemoryHttpCache = 0
    NoCache = 2
    NoPersistentCookies = 0


class QQuickWebEngineScript(__PyQt5_QtCore.QObject):
    """ QQuickWebEngineScript(parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def injectionPoint(self): # real signature unknown; restored from __doc__
        """ injectionPoint(self) -> QQuickWebEngineScript.InjectionPoint """
        pass

    def injectionPointChanged(self, QQuickWebEngineScript_InjectionPoint): # real signature unknown; restored from __doc__
        """ injectionPointChanged(self, QQuickWebEngineScript.InjectionPoint) [signal] """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def nameChanged(self, p_str): # real signature unknown; restored from __doc__
        """ nameChanged(self, str) [signal] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def runOnSubframes(self): # real signature unknown; restored from __doc__
        """ runOnSubframes(self) -> bool """
        return False

    def runOnSubframesChanged(self, bool): # real signature unknown; restored from __doc__
        """ runOnSubframesChanged(self, bool) [signal] """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setInjectionPoint(self, QQuickWebEngineScript_InjectionPoint): # real signature unknown; restored from __doc__
        """ setInjectionPoint(self, QQuickWebEngineScript.InjectionPoint) """
        pass

    def setName(self, p_str): # real signature unknown; restored from __doc__
        """ setName(self, str) """
        pass

    def setRunOnSubframes(self, bool): # real signature unknown; restored from __doc__
        """ setRunOnSubframes(self, bool) """
        pass

    def setSourceCode(self, p_str): # real signature unknown; restored from __doc__
        """ setSourceCode(self, str) """
        pass

    def setSourceUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ setSourceUrl(self, QUrl) """
        pass

    def setWorldId(self, QQuickWebEngineScript_ScriptWorldId): # real signature unknown; restored from __doc__
        """ setWorldId(self, QQuickWebEngineScript.ScriptWorldId) """
        pass

    def sourceCode(self): # real signature unknown; restored from __doc__
        """ sourceCode(self) -> str """
        return ""

    def sourceCodeChanged(self, p_str): # real signature unknown; restored from __doc__
        """ sourceCodeChanged(self, str) [signal] """
        pass

    def sourceUrl(self): # real signature unknown; restored from __doc__
        """ sourceUrl(self) -> QUrl """
        pass

    def sourceUrlChanged(self, QUrl): # real signature unknown; restored from __doc__
        """ sourceUrlChanged(self, QUrl) [signal] """
        pass

    def timerEvent(self, QTimerEvent): # real signature unknown; restored from __doc__
        """ timerEvent(self, QTimerEvent) """
        pass

    def toString(self): # real signature unknown; restored from __doc__
        """ toString(self) -> str """
        return ""

    def worldId(self): # real signature unknown; restored from __doc__
        """ worldId(self) -> QQuickWebEngineScript.ScriptWorldId """
        pass

    def worldIdChanged(self, QQuickWebEngineScript_ScriptWorldId): # real signature unknown; restored from __doc__
        """ worldIdChanged(self, QQuickWebEngineScript.ScriptWorldId) [signal] """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    ApplicationWorld = 1
    Deferred = 0
    DocumentCreation = 2
    DocumentReady = 1
    MainWorld = 0
    UserWorld = 2


class QtWebEngine(__sip.simplewrapper):
    # no doc
    def initialize(self): # real signature unknown; restored from __doc__
        """ initialize() """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values



