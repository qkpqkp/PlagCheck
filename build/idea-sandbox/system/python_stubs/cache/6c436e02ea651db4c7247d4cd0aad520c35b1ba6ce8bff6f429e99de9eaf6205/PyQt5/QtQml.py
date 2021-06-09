# encoding: utf-8
# module PyQt5.QtQml
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtQml.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


# functions

def qjsEngine(QObject): # real signature unknown; restored from __doc__
    """ qjsEngine(QObject) -> QJSEngine """
    return QJSEngine

def qmlAttachedPropertiesObject(type, QObject, create=True): # real signature unknown; restored from __doc__
    """ qmlAttachedPropertiesObject(type, QObject, create: bool = True) -> QObject """
    pass

def qmlClearTypeRegistrations(): # real signature unknown; restored from __doc__
    """ qmlClearTypeRegistrations() """
    pass

def qmlRegisterRevision(type, p_int, p_str, p_int_1, p_int_2, attachedProperties=0): # real signature unknown; restored from __doc__
    """ qmlRegisterRevision(type, int, str, int, int, attachedProperties: type = 0) -> int """
    return 0

def qmlRegisterSingletonType(QUrl, p_str, p_int, p_int_1, p_str_1): # real signature unknown; restored from __doc__
    """
    qmlRegisterSingletonType(QUrl, str, int, int, str) -> int
    qmlRegisterSingletonType(type, str, int, int, str, Callable[[QQmlEngine, QJSEngine], Any]) -> int
    """
    return 0

def qmlRegisterType(QUrl, p_str, p_int, p_int_1, p_str_1): # real signature unknown; restored from __doc__
    """
    qmlRegisterType(QUrl, str, int, int, str) -> int
    qmlRegisterType(type, attachedProperties: type = 0) -> int
    qmlRegisterType(type, str, int, int, str, attachedProperties: type = 0) -> int
    qmlRegisterType(type, int, str, int, int, str, attachedProperties: type = 0) -> int
    """
    return 0

def qmlRegisterUncreatableType(type, p_str, p_int, p_int_1, p_str_1, p_str_2): # real signature unknown; restored from __doc__
    """
    qmlRegisterUncreatableType(type, str, int, int, str, str) -> int
    qmlRegisterUncreatableType(type, int, str, int, int, str, str) -> int
    """
    return 0

def qmlTypeId(p_str, p_int, p_int_1, p_str_1): # real signature unknown; restored from __doc__
    """ qmlTypeId(str, int, int, str) -> int """
    return 0

def QQmlListProperty(type, p_object, p_list): # real signature unknown; restored from __doc__
    """
    QQmlListProperty(type, object, list)
    QQmlListProperty(type, object, append=None, count=None, at=None, clear=None)
    """
    pass

# classes

class QJSEngine(__PyQt5_QtCore.QObject):
    """
    QJSEngine()
    QJSEngine(QObject)
    """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def collectGarbage(self): # real signature unknown; restored from __doc__
        """ collectGarbage(self) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def evaluate(self, p_str, fileName='', lineNumber=1): # real signature unknown; restored from __doc__
        """ evaluate(self, str, fileName: str = '', lineNumber: int = 1) -> QJSValue """
        return QJSValue

    def globalObject(self): # real signature unknown; restored from __doc__
        """ globalObject(self) -> QJSValue """
        return QJSValue

    def importModule(self, p_str): # real signature unknown; restored from __doc__
        """ importModule(self, str) -> QJSValue """
        return QJSValue

    def installExtensions(self, Union, QJSEngine_Extensions=None, QJSEngine_Extension=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ installExtensions(self, Union[QJSEngine.Extensions, QJSEngine.Extension], object: Union[QJSValue, QJSValue.SpecialValue, bool, int, float, str] = QJSValue()) """
        pass

    def installTranslatorFunctions(self, p_object, QJSValue=None, QJSValue_SpecialValue=None, bool=None, p_int=None, p_float=None, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ installTranslatorFunctions(self, object: Union[QJSValue, QJSValue.SpecialValue, bool, int, float, str] = QJSValue()) """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def newArray(self, length=0): # real signature unknown; restored from __doc__
        """ newArray(self, length: int = 0) -> QJSValue """
        return QJSValue

    def newErrorObject(self, QJSValue_ErrorType, message=''): # real signature unknown; restored from __doc__
        """ newErrorObject(self, QJSValue.ErrorType, message: str = '') -> QJSValue """
        return QJSValue

    def newObject(self): # real signature unknown; restored from __doc__
        """ newObject(self) -> QJSValue """
        return QJSValue

    def newQMetaObject(self, QMetaObject): # real signature unknown; restored from __doc__
        """ newQMetaObject(self, QMetaObject) -> QJSValue """
        return QJSValue

    def newQObject(self, QObject): # real signature unknown; restored from __doc__
        """ newQObject(self, QObject) -> QJSValue """
        return QJSValue

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def throwError(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        throwError(self, str)
        throwError(self, QJSValue.ErrorType, message: str = '')
        """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, QObject=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AllExtensions = -1
    ConsoleExtension = 2
    GarbageCollectionExtension = 4
    TranslationExtension = 1


class QJSValue(__sip.simplewrapper):
    """
    QJSValue(value: QJSValue.SpecialValue = QJSValue.UndefinedValue)
    QJSValue(Union[QJSValue, QJSValue.SpecialValue, bool, int, float, str])
    """
    def call(self, args, Union=None, QJSValue=None, QJSValue_SpecialValue=None, bool=None, p_int=None, p_float=None, p_str=None, *args_1, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ call(self, args: Iterable[Union[QJSValue, QJSValue.SpecialValue, bool, int, float, str]] = []) -> QJSValue """
        pass

    def callAsConstructor(self, args, Union=None, QJSValue=None, QJSValue_SpecialValue=None, bool=None, p_int=None, p_float=None, p_str=None, *args_1, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ callAsConstructor(self, args: Iterable[Union[QJSValue, QJSValue.SpecialValue, bool, int, float, str]] = []) -> QJSValue """
        pass

    def callWithInstance(self, Union, QJSValue=None, QJSValue_SpecialValue=None, bool=None, p_int=None, p_float=None, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ callWithInstance(self, Union[QJSValue, QJSValue.SpecialValue, bool, int, float, str], args: Iterable[Union[QJSValue, QJSValue.SpecialValue, bool, int, float, str]] = []) -> QJSValue """
        pass

    def deleteProperty(self, p_str): # real signature unknown; restored from __doc__
        """ deleteProperty(self, str) -> bool """
        return False

    def equals(self, Union, QJSValue=None, QJSValue_SpecialValue=None, bool=None, p_int=None, p_float=None, p_str=None): # real signature unknown; restored from __doc__
        """ equals(self, Union[QJSValue, QJSValue.SpecialValue, bool, int, float, str]) -> bool """
        return False

    def errorType(self): # real signature unknown; restored from __doc__
        """ errorType(self) -> QJSValue.ErrorType """
        pass

    def hasOwnProperty(self, p_str): # real signature unknown; restored from __doc__
        """ hasOwnProperty(self, str) -> bool """
        return False

    def hasProperty(self, p_str): # real signature unknown; restored from __doc__
        """ hasProperty(self, str) -> bool """
        return False

    def isArray(self): # real signature unknown; restored from __doc__
        """ isArray(self) -> bool """
        return False

    def isBool(self): # real signature unknown; restored from __doc__
        """ isBool(self) -> bool """
        return False

    def isCallable(self): # real signature unknown; restored from __doc__
        """ isCallable(self) -> bool """
        return False

    def isDate(self): # real signature unknown; restored from __doc__
        """ isDate(self) -> bool """
        return False

    def isError(self): # real signature unknown; restored from __doc__
        """ isError(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isNumber(self): # real signature unknown; restored from __doc__
        """ isNumber(self) -> bool """
        return False

    def isObject(self): # real signature unknown; restored from __doc__
        """ isObject(self) -> bool """
        return False

    def isQObject(self): # real signature unknown; restored from __doc__
        """ isQObject(self) -> bool """
        return False

    def isRegExp(self): # real signature unknown; restored from __doc__
        """ isRegExp(self) -> bool """
        return False

    def isString(self): # real signature unknown; restored from __doc__
        """ isString(self) -> bool """
        return False

    def isUndefined(self): # real signature unknown; restored from __doc__
        """ isUndefined(self) -> bool """
        return False

    def isVariant(self): # real signature unknown; restored from __doc__
        """ isVariant(self) -> bool """
        return False

    def property(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        property(self, str) -> QJSValue
        property(self, int) -> QJSValue
        """
        return QJSValue

    def prototype(self): # real signature unknown; restored from __doc__
        """ prototype(self) -> QJSValue """
        return QJSValue

    def setProperty(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setProperty(self, str, Union[QJSValue, QJSValue.SpecialValue, bool, int, float, str])
        setProperty(self, int, Union[QJSValue, QJSValue.SpecialValue, bool, int, float, str])
        """
        pass

    def setPrototype(self, Union, QJSValue=None, QJSValue_SpecialValue=None, bool=None, p_int=None, p_float=None, p_str=None): # real signature unknown; restored from __doc__
        """ setPrototype(self, Union[QJSValue, QJSValue.SpecialValue, bool, int, float, str]) """
        pass

    def strictlyEquals(self, Union, QJSValue=None, QJSValue_SpecialValue=None, bool=None, p_int=None, p_float=None, p_str=None): # real signature unknown; restored from __doc__
        """ strictlyEquals(self, Union[QJSValue, QJSValue.SpecialValue, bool, int, float, str]) -> bool """
        return False

    def toBool(self): # real signature unknown; restored from __doc__
        """ toBool(self) -> bool """
        return False

    def toDateTime(self): # real signature unknown; restored from __doc__
        """ toDateTime(self) -> QDateTime """
        pass

    def toInt(self): # real signature unknown; restored from __doc__
        """ toInt(self) -> int """
        return 0

    def toNumber(self): # real signature unknown; restored from __doc__
        """ toNumber(self) -> float """
        return 0.0

    def toQObject(self): # real signature unknown; restored from __doc__
        """ toQObject(self) -> QObject """
        pass

    def toString(self): # real signature unknown; restored from __doc__
        """ toString(self) -> str """
        return ""

    def toUInt(self): # real signature unknown; restored from __doc__
        """ toUInt(self) -> int """
        return 0

    def toVariant(self): # real signature unknown; restored from __doc__
        """ toVariant(self) -> Any """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    EvalError = 2
    GenericError = 1
    NullValue = 0
    RangeError = 3
    ReferenceError = 4
    SyntaxError = 5
    TypeError = 6
    UndefinedValue = 1
    URIError = 7


class QJSValueIterator(__sip.simplewrapper):
    """ QJSValueIterator(Union[QJSValue, QJSValue.SpecialValue, bool, int, float, str]) """
    def hasNext(self): # real signature unknown; restored from __doc__
        """ hasNext(self) -> bool """
        return False

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def next(self): # real signature unknown; restored from __doc__
        """ next(self) -> bool """
        return False

    def value(self): # real signature unknown; restored from __doc__
        """ value(self) -> QJSValue """
        return QJSValue

    def __init__(self, Union, QJSValue=None, QJSValue_SpecialValue=None, bool=None, p_int=None, p_float=None, p_str=None): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QQmlAbstractUrlInterceptor(__sip.simplewrapper):
    """
    QQmlAbstractUrlInterceptor()
    QQmlAbstractUrlInterceptor(QQmlAbstractUrlInterceptor)
    """
    def intercept(self, QUrl, QQmlAbstractUrlInterceptor_DataType): # real signature unknown; restored from __doc__
        """ intercept(self, QUrl, QQmlAbstractUrlInterceptor.DataType) -> QUrl """
        pass

    def __init__(self, QQmlAbstractUrlInterceptor=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    JavaScriptFile = 1
    QmldirFile = 2
    QmlFile = 0
    UrlString = 4096


class QQmlEngine(QJSEngine):
    """ QQmlEngine(parent: QObject = None) """
    def addImageProvider(self, p_str, QQmlImageProviderBase): # real signature unknown; restored from __doc__
        """ addImageProvider(self, str, QQmlImageProviderBase) """
        pass

    def addImportPath(self, p_str): # real signature unknown; restored from __doc__
        """ addImportPath(self, str) """
        pass

    def addNamedBundle(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ addNamedBundle(self, str, str) -> bool """
        return False

    def addPluginPath(self, p_str): # real signature unknown; restored from __doc__
        """ addPluginPath(self, str) """
        pass

    def baseUrl(self): # real signature unknown; restored from __doc__
        """ baseUrl(self) -> QUrl """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clearComponentCache(self): # real signature unknown; restored from __doc__
        """ clearComponentCache(self) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextForObject(self, QObject): # real signature unknown; restored from __doc__
        """ contextForObject(QObject) -> QQmlContext """
        return QQmlContext

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def exit(self, p_int): # real signature unknown; restored from __doc__
        """ exit(self, int) [signal] """
        pass

    def imageProvider(self, p_str): # real signature unknown; restored from __doc__
        """ imageProvider(self, str) -> QQmlImageProviderBase """
        return QQmlImageProviderBase

    def importPathList(self): # real signature unknown; restored from __doc__
        """ importPathList(self) -> List[str] """
        return []

    def importPlugin(self, p_str, p_str_1, Iterable, QQmlError=None): # real signature unknown; restored from __doc__
        """ importPlugin(self, str, str, Iterable[QQmlError]) -> bool """
        return False

    def incubationController(self): # real signature unknown; restored from __doc__
        """ incubationController(self) -> QQmlIncubationController """
        return QQmlIncubationController

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def networkAccessManager(self): # real signature unknown; restored from __doc__
        """ networkAccessManager(self) -> QNetworkAccessManager """
        pass

    def networkAccessManagerFactory(self): # real signature unknown; restored from __doc__
        """ networkAccessManagerFactory(self) -> QQmlNetworkAccessManagerFactory """
        return QQmlNetworkAccessManagerFactory

    def objectOwnership(self, QObject): # real signature unknown; restored from __doc__
        """ objectOwnership(QObject) -> QQmlEngine.ObjectOwnership """
        pass

    def offlineStorageDatabaseFilePath(self, p_str): # real signature unknown; restored from __doc__
        """ offlineStorageDatabaseFilePath(self, str) -> str """
        return ""

    def offlineStoragePath(self): # real signature unknown; restored from __doc__
        """ offlineStoragePath(self) -> str """
        return ""

    def outputWarningsToStandardError(self): # real signature unknown; restored from __doc__
        """ outputWarningsToStandardError(self) -> bool """
        return False

    def pluginPathList(self): # real signature unknown; restored from __doc__
        """ pluginPathList(self) -> List[str] """
        return []

    def quit(self): # real signature unknown; restored from __doc__
        """ quit(self) [signal] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeImageProvider(self, p_str): # real signature unknown; restored from __doc__
        """ removeImageProvider(self, str) """
        pass

    def retranslate(self): # real signature unknown; restored from __doc__
        """ retranslate(self) """
        pass

    def rootContext(self): # real signature unknown; restored from __doc__
        """ rootContext(self) -> QQmlContext """
        return QQmlContext

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setBaseUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ setBaseUrl(self, QUrl) """
        pass

    def setContextForObject(self, QObject, QQmlContext): # real signature unknown; restored from __doc__
        """ setContextForObject(QObject, QQmlContext) """
        pass

    def setImportPathList(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ setImportPathList(self, Iterable[str]) """
        pass

    def setIncubationController(self, QQmlIncubationController): # real signature unknown; restored from __doc__
        """ setIncubationController(self, QQmlIncubationController) """
        pass

    def setNetworkAccessManagerFactory(self, QQmlNetworkAccessManagerFactory): # real signature unknown; restored from __doc__
        """ setNetworkAccessManagerFactory(self, QQmlNetworkAccessManagerFactory) """
        pass

    def setObjectOwnership(self, QObject, QQmlEngine_ObjectOwnership): # real signature unknown; restored from __doc__
        """ setObjectOwnership(QObject, QQmlEngine.ObjectOwnership) """
        pass

    def setOfflineStoragePath(self, p_str): # real signature unknown; restored from __doc__
        """ setOfflineStoragePath(self, str) """
        pass

    def setOutputWarningsToStandardError(self, bool): # real signature unknown; restored from __doc__
        """ setOutputWarningsToStandardError(self, bool) """
        pass

    def setPluginPathList(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ setPluginPathList(self, Iterable[str]) """
        pass

    def singletonInstance(self, p_int): # real signature unknown; restored from __doc__
        """ singletonInstance(self, int) -> QObject """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def trimComponentCache(self): # real signature unknown; restored from __doc__
        """ trimComponentCache(self) """
        pass

    def warnings(self, Iterable, QQmlError=None): # real signature unknown; restored from __doc__
        """ warnings(self, Iterable[QQmlError]) [signal] """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    CppOwnership = 0
    JavaScriptOwnership = 1


class QQmlApplicationEngine(QQmlEngine):
    """
    QQmlApplicationEngine(parent: QObject = None)
    QQmlApplicationEngine(QUrl, parent: QObject = None)
    QQmlApplicationEngine(str, parent: QObject = None)
    """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def load(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        load(self, QUrl)
        load(self, str)
        """
        pass

    def loadData(self, Union, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ loadData(self, Union[QByteArray, bytes, bytearray], url: QUrl = QUrl()) """
        pass

    def objectCreated(self, QObject, QUrl): # real signature unknown; restored from __doc__
        """ objectCreated(self, QObject, QUrl) [signal] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def rootObjects(self): # real signature unknown; restored from __doc__
        """ rootObjects(self) -> List[QObject] """
        return []

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


class QQmlComponent(__PyQt5_QtCore.QObject):
    """
    QQmlComponent(QQmlEngine, parent: QObject = None)
    QQmlComponent(QQmlEngine, str, parent: QObject = None)
    QQmlComponent(QQmlEngine, str, QQmlComponent.CompilationMode, parent: QObject = None)
    QQmlComponent(QQmlEngine, QUrl, parent: QObject = None)
    QQmlComponent(QQmlEngine, QUrl, QQmlComponent.CompilationMode, parent: QObject = None)
    QQmlComponent(parent: QObject = None)
    """
    def beginCreate(self, QQmlContext): # real signature unknown; restored from __doc__
        """ beginCreate(self, QQmlContext) -> QObject """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def completeCreate(self): # real signature unknown; restored from __doc__
        """ completeCreate(self) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        create(self, context: QQmlContext = None) -> QObject
        create(self, QQmlIncubator, context: QQmlContext = None, forContext: QQmlContext = None)
        """
        pass

    def creationContext(self): # real signature unknown; restored from __doc__
        """ creationContext(self) -> QQmlContext """
        return QQmlContext

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def engine(self): # real signature unknown; restored from __doc__
        """ engine(self) -> QQmlEngine """
        return QQmlEngine

    def errors(self): # real signature unknown; restored from __doc__
        """ errors(self) -> List[QQmlError] """
        return []

    def isError(self): # real signature unknown; restored from __doc__
        """ isError(self) -> bool """
        return False

    def isLoading(self): # real signature unknown; restored from __doc__
        """ isLoading(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isReady(self): # real signature unknown; restored from __doc__
        """ isReady(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def loadUrl(self, QUrl, QQmlComponent_CompilationMode=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        loadUrl(self, QUrl)
        loadUrl(self, QUrl, QQmlComponent.CompilationMode)
        """
        pass

    def progress(self): # real signature unknown; restored from __doc__
        """ progress(self) -> float """
        return 0.0

    def progressChanged(self, p_float): # real signature unknown; restored from __doc__
        """ progressChanged(self, float) [signal] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setData(self, Union, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setData(self, Union[QByteArray, bytes, bytearray], QUrl) """
        pass

    def status(self): # real signature unknown; restored from __doc__
        """ status(self) -> QQmlComponent.Status """
        pass

    def statusChanged(self, QQmlComponent_Status): # real signature unknown; restored from __doc__
        """ statusChanged(self, QQmlComponent.Status) [signal] """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def url(self): # real signature unknown; restored from __doc__
        """ url(self) -> QUrl """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    Asynchronous = 1
    Error = 3
    Loading = 2
    Null = 0
    PreferSynchronous = 0
    Ready = 1


class QQmlContext(__PyQt5_QtCore.QObject):
    """
    QQmlContext(QQmlEngine, parent: QObject = None)
    QQmlContext(QQmlContext, parent: QObject = None)
    """
    def baseUrl(self): # real signature unknown; restored from __doc__
        """ baseUrl(self) -> QUrl """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextObject(self): # real signature unknown; restored from __doc__
        """ contextObject(self) -> QObject """
        pass

    def contextProperty(self, p_str): # real signature unknown; restored from __doc__
        """ contextProperty(self, str) -> Any """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def engine(self): # real signature unknown; restored from __doc__
        """ engine(self) -> QQmlEngine """
        return QQmlEngine

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def nameForObject(self, QObject): # real signature unknown; restored from __doc__
        """ nameForObject(self, QObject) -> str """
        return ""

    def parentContext(self): # real signature unknown; restored from __doc__
        """ parentContext(self) -> QQmlContext """
        return QQmlContext

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resolvedUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ resolvedUrl(self, QUrl) -> QUrl """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setBaseUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ setBaseUrl(self, QUrl) """
        pass

    def setContextObject(self, QObject): # real signature unknown; restored from __doc__
        """ setContextObject(self, QObject) """
        pass

    def setContextProperties(self, Iterable, QQmlContext_PropertyPair=None): # real signature unknown; restored from __doc__
        """ setContextProperties(self, Iterable[QQmlContext.PropertyPair]) """
        pass

    def setContextProperty(self, p_str, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setContextProperty(self, str, QObject)
        setContextProperty(self, str, Any)
        """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass



class QQmlError(__sip.simplewrapper):
    """
    QQmlError()
    QQmlError(QQmlError)
    """
    def column(self): # real signature unknown; restored from __doc__
        """ column(self) -> int """
        return 0

    def description(self): # real signature unknown; restored from __doc__
        """ description(self) -> str """
        return ""

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def line(self): # real signature unknown; restored from __doc__
        """ line(self) -> int """
        return 0

    def messageType(self): # real signature unknown; restored from __doc__
        """ messageType(self) -> QtMsgType """
        pass

    def object(self): # real signature unknown; restored from __doc__
        """ object(self) -> QObject """
        pass

    def setColumn(self, p_int): # real signature unknown; restored from __doc__
        """ setColumn(self, int) """
        pass

    def setDescription(self, p_str): # real signature unknown; restored from __doc__
        """ setDescription(self, str) """
        pass

    def setLine(self, p_int): # real signature unknown; restored from __doc__
        """ setLine(self, int) """
        pass

    def setMessageType(self, QtMsgType): # real signature unknown; restored from __doc__
        """ setMessageType(self, QtMsgType) """
        pass

    def setObject(self, QObject): # real signature unknown; restored from __doc__
        """ setObject(self, QObject) """
        pass

    def setUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ setUrl(self, QUrl) """
        pass

    def toString(self): # real signature unknown; restored from __doc__
        """ toString(self) -> str """
        return ""

    def url(self): # real signature unknown; restored from __doc__
        """ url(self) -> QUrl """
        pass

    def __init__(self, QQmlError=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QQmlExpression(__PyQt5_QtCore.QObject):
    """
    QQmlExpression()
    QQmlExpression(QQmlContext, QObject, str, parent: QObject = None)
    QQmlExpression(QQmlScriptString, context: QQmlContext = None, scope: QObject = None, parent: QObject = None)
    """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clearError(self): # real signature unknown; restored from __doc__
        """ clearError(self) """
        pass

    def columnNumber(self): # real signature unknown; restored from __doc__
        """ columnNumber(self) -> int """
        return 0

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def context(self): # real signature unknown; restored from __doc__
        """ context(self) -> QQmlContext """
        return QQmlContext

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def engine(self): # real signature unknown; restored from __doc__
        """ engine(self) -> QQmlEngine """
        return QQmlEngine

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> QQmlError """
        return QQmlError

    def evaluate(self): # real signature unknown; restored from __doc__
        """ evaluate(self) -> Tuple[Any, bool] """
        pass

    def expression(self): # real signature unknown; restored from __doc__
        """ expression(self) -> str """
        return ""

    def hasError(self): # real signature unknown; restored from __doc__
        """ hasError(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def lineNumber(self): # real signature unknown; restored from __doc__
        """ lineNumber(self) -> int """
        return 0

    def notifyOnValueChanged(self): # real signature unknown; restored from __doc__
        """ notifyOnValueChanged(self) -> bool """
        return False

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def scopeObject(self): # real signature unknown; restored from __doc__
        """ scopeObject(self) -> QObject """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setExpression(self, p_str): # real signature unknown; restored from __doc__
        """ setExpression(self, str) """
        pass

    def setNotifyOnValueChanged(self, bool): # real signature unknown; restored from __doc__
        """ setNotifyOnValueChanged(self, bool) """
        pass

    def setSourceLocation(self, p_str, p_int, column=0): # real signature unknown; restored from __doc__
        """ setSourceLocation(self, str, int, column: int = 0) """
        pass

    def sourceFile(self): # real signature unknown; restored from __doc__
        """ sourceFile(self) -> str """
        return ""

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def valueChanged(self): # real signature unknown; restored from __doc__
        """ valueChanged(self) [signal] """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


class QQmlExtensionPlugin(__PyQt5_QtCore.QObject):
    """ QQmlExtensionPlugin(parent: QObject = None) """
    def baseUrl(self): # real signature unknown; restored from __doc__
        """ baseUrl(self) -> QUrl """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def initializeEngine(self, QQmlEngine, p_str): # real signature unknown; restored from __doc__
        """ initializeEngine(self, QQmlEngine, str) """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def registerTypes(self, p_str): # real signature unknown; restored from __doc__
        """ registerTypes(self, str) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


class QQmlFileSelector(__PyQt5_QtCore.QObject):
    """ QQmlFileSelector(QQmlEngine, parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def get(self, QQmlEngine): # real signature unknown; restored from __doc__
        """ get(QQmlEngine) -> QQmlFileSelector """
        return QQmlFileSelector

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def selector(self): # real signature unknown; restored from __doc__
        """ selector(self) -> QFileSelector """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setExtraSelectors(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ setExtraSelectors(self, Iterable[str]) """
        pass

    def setSelector(self, QFileSelector): # real signature unknown; restored from __doc__
        """ setSelector(self, QFileSelector) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, QQmlEngine, parent=None): # real signature unknown; restored from __doc__
        pass


class QQmlImageProviderBase(__sip.wrapper):
    # no doc
    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> QQmlImageProviderBase.Flags """
        pass

    def imageType(self): # real signature unknown; restored from __doc__
        """ imageType(self) -> QQmlImageProviderBase.ImageType """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    ForceAsynchronousImageLoading = 1
    Image = 0
    ImageResponse = 4
    Pixmap = 1
    Texture = 2


class QQmlIncubationController(__sip.simplewrapper):
    """ QQmlIncubationController() """
    def engine(self): # real signature unknown; restored from __doc__
        """ engine(self) -> QQmlEngine """
        return QQmlEngine

    def incubateFor(self, p_int): # real signature unknown; restored from __doc__
        """ incubateFor(self, int) """
        pass

    def incubatingObjectCount(self): # real signature unknown; restored from __doc__
        """ incubatingObjectCount(self) -> int """
        return 0

    def incubatingObjectCountChanged(self, p_int): # real signature unknown; restored from __doc__
        """ incubatingObjectCountChanged(self, int) """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QQmlIncubator(__sip.simplewrapper):
    """ QQmlIncubator(mode: QQmlIncubator.IncubationMode = QQmlIncubator.Asynchronous) """
    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def errors(self): # real signature unknown; restored from __doc__
        """ errors(self) -> List[QQmlError] """
        return []

    def forceCompletion(self): # real signature unknown; restored from __doc__
        """ forceCompletion(self) """
        pass

    def incubationMode(self): # real signature unknown; restored from __doc__
        """ incubationMode(self) -> QQmlIncubator.IncubationMode """
        pass

    def isError(self): # real signature unknown; restored from __doc__
        """ isError(self) -> bool """
        return False

    def isLoading(self): # real signature unknown; restored from __doc__
        """ isLoading(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isReady(self): # real signature unknown; restored from __doc__
        """ isReady(self) -> bool """
        return False

    def object(self): # real signature unknown; restored from __doc__
        """ object(self) -> QObject """
        pass

    def setInitialState(self, QObject): # real signature unknown; restored from __doc__
        """ setInitialState(self, QObject) """
        pass

    def status(self): # real signature unknown; restored from __doc__
        """ status(self) -> QQmlIncubator.Status """
        pass

    def statusChanged(self, QQmlIncubator_Status): # real signature unknown; restored from __doc__
        """ statusChanged(self, QQmlIncubator.Status) """
        pass

    def __init__(self, mode=None): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Asynchronous = 0
    AsynchronousIfNested = 1
    Error = 3
    Loading = 2
    Null = 0
    Ready = 1
    Synchronous = 2


class QQmlListReference(__sip.simplewrapper):
    """
    QQmlListReference()
    QQmlListReference(QObject, str, engine: QQmlEngine = None)
    QQmlListReference(QQmlListReference)
    """
    def append(self, QObject): # real signature unknown; restored from __doc__
        """ append(self, QObject) -> bool """
        return False

    def at(self, p_int): # real signature unknown; restored from __doc__
        """ at(self, int) -> QObject """
        pass

    def canAppend(self): # real signature unknown; restored from __doc__
        """ canAppend(self) -> bool """
        return False

    def canAt(self): # real signature unknown; restored from __doc__
        """ canAt(self) -> bool """
        return False

    def canClear(self): # real signature unknown; restored from __doc__
        """ canClear(self) -> bool """
        return False

    def canCount(self): # real signature unknown; restored from __doc__
        """ canCount(self) -> bool """
        return False

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> bool """
        return False

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def isManipulable(self): # real signature unknown; restored from __doc__
        """ isManipulable(self) -> bool """
        return False

    def isReadable(self): # real signature unknown; restored from __doc__
        """ isReadable(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def listElementType(self): # real signature unknown; restored from __doc__
        """ listElementType(self) -> QMetaObject """
        pass

    def object(self): # real signature unknown; restored from __doc__
        """ object(self) -> QObject """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QQmlNetworkAccessManagerFactory(__sip.simplewrapper):
    """
    QQmlNetworkAccessManagerFactory()
    QQmlNetworkAccessManagerFactory(QQmlNetworkAccessManagerFactory)
    """
    def create(self, QObject): # real signature unknown; restored from __doc__
        """ create(self, QObject) -> QNetworkAccessManager """
        pass

    def __init__(self, QQmlNetworkAccessManagerFactory=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QQmlParserStatus(__sip.simplewrapper):
    """
    QQmlParserStatus()
    QQmlParserStatus(QQmlParserStatus)
    """
    def classBegin(self): # real signature unknown; restored from __doc__
        """ classBegin(self) """
        pass

    def componentComplete(self): # real signature unknown; restored from __doc__
        """ componentComplete(self) """
        pass

    def __init__(self, QQmlParserStatus=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QQmlProperty(__sip.simplewrapper):
    """
    QQmlProperty()
    QQmlProperty(QObject)
    QQmlProperty(QObject, QQmlContext)
    QQmlProperty(QObject, QQmlEngine)
    QQmlProperty(QObject, str)
    QQmlProperty(QObject, str, QQmlContext)
    QQmlProperty(QObject, str, QQmlEngine)
    QQmlProperty(QQmlProperty)
    """
    def connectNotifySignal(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        connectNotifySignal(self, PYQT_SLOT) -> bool
        connectNotifySignal(self, QObject, int) -> bool
        """
        return False

    def hasNotifySignal(self): # real signature unknown; restored from __doc__
        """ hasNotifySignal(self) -> bool """
        return False

    def index(self): # real signature unknown; restored from __doc__
        """ index(self) -> int """
        return 0

    def isDesignable(self): # real signature unknown; restored from __doc__
        """ isDesignable(self) -> bool """
        return False

    def isProperty(self): # real signature unknown; restored from __doc__
        """ isProperty(self) -> bool """
        return False

    def isResettable(self): # real signature unknown; restored from __doc__
        """ isResettable(self) -> bool """
        return False

    def isSignalProperty(self): # real signature unknown; restored from __doc__
        """ isSignalProperty(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def isWritable(self): # real signature unknown; restored from __doc__
        """ isWritable(self) -> bool """
        return False

    def method(self): # real signature unknown; restored from __doc__
        """ method(self) -> QMetaMethod """
        pass

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def needsNotifySignal(self): # real signature unknown; restored from __doc__
        """ needsNotifySignal(self) -> bool """
        return False

    def object(self): # real signature unknown; restored from __doc__
        """ object(self) -> QObject """
        pass

    def property(self): # real signature unknown; restored from __doc__
        """ property(self) -> QMetaProperty """
        pass

    def propertyType(self): # real signature unknown; restored from __doc__
        """ propertyType(self) -> int """
        return 0

    def propertyTypeCategory(self): # real signature unknown; restored from __doc__
        """ propertyTypeCategory(self) -> QQmlProperty.PropertyTypeCategory """
        pass

    def propertyTypeName(self): # real signature unknown; restored from __doc__
        """ propertyTypeName(self) -> str """
        return ""

    def read(self, QObject=None, p_str=None, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        read(self) -> Any
        read(QObject, str) -> Any
        read(QObject, str, QQmlContext) -> Any
        read(QObject, str, QQmlEngine) -> Any
        """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) -> bool """
        return False

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QQmlProperty.Type """
        pass

    def write(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        write(self, Any) -> bool
        write(QObject, str, Any) -> bool
        write(QObject, str, Any, QQmlContext) -> bool
        write(QObject, str, Any, QQmlEngine) -> bool
        """
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


    Invalid = 0
    InvalidCategory = 0
    List = 1
    Normal = 3
    Object = 2
    Property = 1
    SignalProperty = 2


class QQmlPropertyMap(__PyQt5_QtCore.QObject):
    """ QQmlPropertyMap(parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self, p_str): # real signature unknown; restored from __doc__
        """ clear(self, str) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contains(self, p_str): # real signature unknown; restored from __doc__
        """ contains(self, str) -> bool """
        return False

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def insert(self, p_str, Any): # real signature unknown; restored from __doc__
        """ insert(self, str, Any) """
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keys(self): # real signature unknown; restored from __doc__
        """ keys(self) -> List[str] """
        return []

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateValue(self, p_str, Any): # real signature unknown; restored from __doc__
        """ updateValue(self, str, Any) -> Any """
        pass

    def value(self, p_str): # real signature unknown; restored from __doc__
        """ value(self, str) -> Any """
        pass

    def valueChanged(self, p_str, Any): # real signature unknown; restored from __doc__
        """ valueChanged(self, str, Any) [signal] """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass


class QQmlPropertyValueSource(__sip.simplewrapper):
    """
    QQmlPropertyValueSource()
    QQmlPropertyValueSource(QQmlPropertyValueSource)
    """
    def setTarget(self, QQmlProperty): # real signature unknown; restored from __doc__
        """ setTarget(self, QQmlProperty) """
        pass

    def __init__(self, QQmlPropertyValueSource=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QQmlScriptString(__sip.simplewrapper):
    """
    QQmlScriptString()
    QQmlScriptString(QQmlScriptString)
    """
    def booleanLiteral(self): # real signature unknown; restored from __doc__
        """ booleanLiteral(self) -> Tuple[bool, bool] """
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isNullLiteral(self): # real signature unknown; restored from __doc__
        """ isNullLiteral(self) -> bool """
        return False

    def isUndefinedLiteral(self): # real signature unknown; restored from __doc__
        """ isUndefinedLiteral(self) -> bool """
        return False

    def numberLiteral(self): # real signature unknown; restored from __doc__
        """ numberLiteral(self) -> Tuple[float, bool] """
        pass

    def stringLiteral(self): # real signature unknown; restored from __doc__
        """ stringLiteral(self) -> str """
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

    def __init__(self, QQmlScriptString=None): # real signature unknown; restored from __doc__ with multiple overloads
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


# variables with complex values



