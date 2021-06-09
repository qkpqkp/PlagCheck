# encoding: utf-8
# module PyQt5.QtDBus
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtDBus.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


# no functions
# classes

class QDBus(__sip.simplewrapper):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AutoDetect = 3
    Block = 1
    BlockWithGui = 2
    NoBlock = 0


class QDBusAbstractAdaptor(__PyQt5_QtCore.QObject):
    """ QDBusAbstractAdaptor(QObject) """
    def autoRelaySignals(self): # real signature unknown; restored from __doc__
        """ autoRelaySignals(self) -> bool """
        return False

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

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAutoRelaySignals(self, bool): # real signature unknown; restored from __doc__
        """ setAutoRelaySignals(self, bool) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, QObject): # real signature unknown; restored from __doc__
        pass


class QDBusAbstractInterface(__PyQt5_QtCore.QObject):
    """ QDBusAbstractInterface(str, str, str, QDBusConnection, QObject) """
    def asyncCall(self, p_str, arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None, arg7=None, arg8=None): # real signature unknown; restored from __doc__
        """ asyncCall(self, str, arg1: Any = None, arg2: Any = None, arg3: Any = None, arg4: Any = None, arg5: Any = None, arg6: Any = None, arg7: Any = None, arg8: Any = None) -> QDBusPendingCall """
        return QDBusPendingCall

    def asyncCallWithArgumentList(self, p_str, Iterable, Any=None): # real signature unknown; restored from __doc__
        """ asyncCallWithArgumentList(self, str, Iterable[Any]) -> QDBusPendingCall """
        return QDBusPendingCall

    def call(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        call(self, str, arg1: Any = None, arg2: Any = None, arg3: Any = None, arg4: Any = None, arg5: Any = None, arg6: Any = None, arg7: Any = None, arg8: Any = None) -> QDBusMessage
        call(self, QDBus.CallMode, str, arg1: Any = None, arg2: Any = None, arg3: Any = None, arg4: Any = None, arg5: Any = None, arg6: Any = None, arg7: Any = None, arg8: Any = None) -> QDBusMessage
        """
        return QDBusMessage

    def callWithArgumentList(self, QDBus_CallMode, p_str, Iterable, Any=None): # real signature unknown; restored from __doc__
        """ callWithArgumentList(self, QDBus.CallMode, str, Iterable[Any]) -> QDBusMessage """
        return QDBusMessage

    def callWithCallback(self, p_str, Iterable, Any=None, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        """
        callWithCallback(self, str, Iterable[Any], PYQT_SLOT, PYQT_SLOT) -> bool
        callWithCallback(self, str, Iterable[Any], PYQT_SLOT) -> bool
        """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connection(self): # real signature unknown; restored from __doc__
        """ connection(self) -> QDBusConnection """
        return QDBusConnection

    def connectNotify(self, QMetaMethod): # real signature unknown; restored from __doc__
        """ connectNotify(self, QMetaMethod) """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, QMetaMethod): # real signature unknown; restored from __doc__
        """ disconnectNotify(self, QMetaMethod) """
        pass

    def interface(self): # real signature unknown; restored from __doc__
        """ interface(self) -> str """
        return ""

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def lastError(self): # real signature unknown; restored from __doc__
        """ lastError(self) -> QDBusError """
        return QDBusError

    def path(self): # real signature unknown; restored from __doc__
        """ path(self) -> str """
        return ""

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def service(self): # real signature unknown; restored from __doc__
        """ service(self) -> str """
        return ""

    def setTimeout(self, p_int): # real signature unknown; restored from __doc__
        """ setTimeout(self, int) """
        pass

    def timeout(self): # real signature unknown; restored from __doc__
        """ timeout(self) -> int """
        return 0

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, p_str, p_str_1, p_str_2, QDBusConnection, QObject): # real signature unknown; restored from __doc__
        pass


class QDBusArgument(__sip.simplewrapper):
    """
    QDBusArgument()
    QDBusArgument(QDBusArgument)
    QDBusArgument(object, id: int = QMetaType.Int)
    """
    def add(self, p_object, id=None): # real signature unknown; restored from __doc__
        """ add(self, object, id: int = QMetaType.Int) """
        pass

    def beginArray(self, p_int): # real signature unknown; restored from __doc__
        """ beginArray(self, int) """
        pass

    def beginMap(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ beginMap(self, int, int) """
        pass

    def beginMapEntry(self): # real signature unknown; restored from __doc__
        """ beginMapEntry(self) """
        pass

    def beginStructure(self): # real signature unknown; restored from __doc__
        """ beginStructure(self) """
        pass

    def endArray(self): # real signature unknown; restored from __doc__
        """ endArray(self) """
        pass

    def endMap(self): # real signature unknown; restored from __doc__
        """ endMap(self) """
        pass

    def endMapEntry(self): # real signature unknown; restored from __doc__
        """ endMapEntry(self) """
        pass

    def endStructure(self): # real signature unknown; restored from __doc__
        """ endStructure(self) """
        pass

    def swap(self, QDBusArgument): # real signature unknown; restored from __doc__
        """ swap(self, QDBusArgument) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QDBusConnection(__sip.simplewrapper):
    """
    QDBusConnection(str)
    QDBusConnection(QDBusConnection)
    """
    def asyncCall(self, QDBusMessage, timeout=-1): # real signature unknown; restored from __doc__
        """ asyncCall(self, QDBusMessage, timeout: int = -1) -> QDBusPendingCall """
        return QDBusPendingCall

    def baseService(self): # real signature unknown; restored from __doc__
        """ baseService(self) -> str """
        return ""

    def call(self, QDBusMessage, mode=None, timeout=-1): # real signature unknown; restored from __doc__
        """ call(self, QDBusMessage, mode: QDBus.CallMode = QDBus.Block, timeout: int = -1) -> QDBusMessage """
        return QDBusMessage

    def callWithCallback(self, QDBusMessage, PYQT_SLOT, PYQT_SLOT_1, timeout=-1): # real signature unknown; restored from __doc__
        """ callWithCallback(self, QDBusMessage, PYQT_SLOT, PYQT_SLOT, timeout: int = -1) -> bool """
        return False

    def connect(self, p_str, p_str_1, p_str_2, p_str_3, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        connect(self, str, str, str, str, PYQT_SLOT) -> bool
        connect(self, str, str, str, str, str, PYQT_SLOT) -> bool
        connect(self, str, str, str, str, Iterable[str], str, PYQT_SLOT) -> bool
        """
        return False

    def connectionCapabilities(self): # real signature unknown; restored from __doc__
        """ connectionCapabilities(self) -> QDBusConnection.ConnectionCapabilities """
        pass

    def connectToBus(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        connectToBus(QDBusConnection.BusType, str) -> QDBusConnection
        connectToBus(str, str) -> QDBusConnection
        """
        return QDBusConnection

    def connectToPeer(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ connectToPeer(str, str) -> QDBusConnection """
        return QDBusConnection

    def disconnect(self, p_str, p_str_1, p_str_2, p_str_3, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        disconnect(self, str, str, str, str, PYQT_SLOT) -> bool
        disconnect(self, str, str, str, str, str, PYQT_SLOT) -> bool
        disconnect(self, str, str, str, str, Iterable[str], str, PYQT_SLOT) -> bool
        """
        return False

    def disconnectFromBus(self, p_str): # real signature unknown; restored from __doc__
        """ disconnectFromBus(str) """
        pass

    def disconnectFromPeer(self, p_str): # real signature unknown; restored from __doc__
        """ disconnectFromPeer(str) """
        pass

    def interface(self): # real signature unknown; restored from __doc__
        """ interface(self) -> QDBusConnectionInterface """
        return QDBusConnectionInterface

    def isConnected(self): # real signature unknown; restored from __doc__
        """ isConnected(self) -> bool """
        return False

    def lastError(self): # real signature unknown; restored from __doc__
        """ lastError(self) -> QDBusError """
        return QDBusError

    def localMachineId(self): # real signature unknown; restored from __doc__
        """ localMachineId() -> QByteArray """
        pass

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def objectRegisteredAt(self, p_str): # real signature unknown; restored from __doc__
        """ objectRegisteredAt(self, str) -> QObject """
        pass

    def registerObject(self, p_str, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        registerObject(self, str, QObject, options: Union[QDBusConnection.RegisterOptions, QDBusConnection.RegisterOption] = QDBusConnection.ExportAdaptors) -> bool
        registerObject(self, str, str, QObject, options: Union[QDBusConnection.RegisterOptions, QDBusConnection.RegisterOption] = QDBusConnection.ExportAdaptors) -> bool
        """
        pass

    def registerService(self, p_str): # real signature unknown; restored from __doc__
        """ registerService(self, str) -> bool """
        return False

    def send(self, QDBusMessage): # real signature unknown; restored from __doc__
        """ send(self, QDBusMessage) -> bool """
        return False

    def sender(self): # real signature unknown; restored from __doc__
        """ sender() -> QDBusConnection """
        return QDBusConnection

    def sessionBus(self): # real signature unknown; restored from __doc__
        """ sessionBus() -> QDBusConnection """
        return QDBusConnection

    def swap(self, QDBusConnection): # real signature unknown; restored from __doc__
        """ swap(self, QDBusConnection) """
        pass

    def systemBus(self): # real signature unknown; restored from __doc__
        """ systemBus() -> QDBusConnection """
        return QDBusConnection

    def unregisterObject(self, p_str, mode=None): # real signature unknown; restored from __doc__
        """ unregisterObject(self, str, mode: QDBusConnection.UnregisterMode = QDBusConnection.UnregisterNode) """
        pass

    def unregisterService(self, p_str): # real signature unknown; restored from __doc__
        """ unregisterService(self, str) -> bool """
        return False

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    ActivationBus = 2
    ExportAdaptors = 1
    ExportAllContents = 4080
    ExportAllInvokables = 2176
    ExportAllProperties = 1088
    ExportAllSignal = 544
    ExportAllSignals = 544
    ExportAllSlots = 272
    ExportChildObjects = 4096
    ExportNonScriptableContents = 3840
    ExportNonScriptableInvokables = 2048
    ExportNonScriptableProperties = 1024
    ExportNonScriptableSignals = 512
    ExportNonScriptableSlots = 256
    ExportScriptableContents = 240
    ExportScriptableInvokables = 128
    ExportScriptableProperties = 64
    ExportScriptableSignals = 32
    ExportScriptableSlots = 16
    SessionBus = 0
    SystemBus = 1
    UnixFileDescriptorPassing = 1
    UnregisterNode = 0
    UnregisterTree = 1


class QDBusConnectionInterface(QDBusAbstractInterface):
    # no doc
    def callWithCallbackFailed(self, QDBusError, QDBusMessage): # real signature unknown; restored from __doc__
        """ callWithCallbackFailed(self, QDBusError, QDBusMessage) [signal] """
        pass

    def isServiceRegistered(self, p_str): # real signature unknown; restored from __doc__
        """ isServiceRegistered(self, str) -> QDBusReply """
        return QDBusReply

    def registeredServiceNames(self): # real signature unknown; restored from __doc__
        """ registeredServiceNames(self) -> QDBusReply """
        return QDBusReply

    def registerService(self, p_str, qoption=None, roption=None): # real signature unknown; restored from __doc__
        """ registerService(self, str, qoption: QDBusConnectionInterface.ServiceQueueOptions = QDBusConnectionInterface.DontQueueService, roption: QDBusConnectionInterface.ServiceReplacementOptions = QDBusConnectionInterface.DontAllowReplacement) -> QDBusReply """
        return QDBusReply

    def serviceOwner(self, p_str): # real signature unknown; restored from __doc__
        """ serviceOwner(self, str) -> QDBusReply """
        return QDBusReply

    def serviceOwnerChanged(self, p_str, p_str_1, p_str_2): # real signature unknown; restored from __doc__
        """ serviceOwnerChanged(self, str, str, str) [signal] """
        pass

    def servicePid(self, p_str): # real signature unknown; restored from __doc__
        """ servicePid(self, str) -> QDBusReply """
        return QDBusReply

    def serviceRegistered(self, p_str): # real signature unknown; restored from __doc__
        """ serviceRegistered(self, str) [signal] """
        pass

    def serviceUid(self, p_str): # real signature unknown; restored from __doc__
        """ serviceUid(self, str) -> QDBusReply """
        return QDBusReply

    def serviceUnregistered(self, p_str): # real signature unknown; restored from __doc__
        """ serviceUnregistered(self, str) [signal] """
        pass

    def startService(self, p_str): # real signature unknown; restored from __doc__
        """ startService(self, str) -> QDBusReply """
        return QDBusReply

    def unregisterService(self, p_str): # real signature unknown; restored from __doc__
        """ unregisterService(self, str) -> QDBusReply """
        return QDBusReply

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    AllowReplacement = 1
    DontAllowReplacement = 0
    DontQueueService = 0
    QueueService = 1
    ReplaceExistingService = 2
    ServiceNotRegistered = 0
    ServiceQueued = 2
    ServiceRegistered = 1


class QDBusError(__sip.simplewrapper):
    """ QDBusError(QDBusError) """
    def errorString(self, QDBusError_ErrorType): # real signature unknown; restored from __doc__
        """ errorString(QDBusError.ErrorType) -> str """
        return ""

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def message(self): # real signature unknown; restored from __doc__
        """ message(self) -> str """
        return ""

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def swap(self, QDBusError): # real signature unknown; restored from __doc__
        """ swap(self, QDBusError) """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QDBusError.ErrorType """
        pass

    def __init__(self, QDBusError): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AccessDenied = 9
    AddressInUse = 13
    BadAddress = 6
    Disconnected = 14
    Failed = 2
    InternalError = 23
    InvalidArgs = 15
    InvalidInterface = 26
    InvalidMember = 27
    InvalidObjectPath = 25
    InvalidService = 24
    InvalidSignature = 18
    LimitsExceeded = 8
    NoError = 0
    NoMemory = 3
    NoNetwork = 12
    NoReply = 5
    NoServer = 10
    NotSupported = 7
    Other = 1
    PropertyReadOnly = 22
    ServiceUnknown = 4
    TimedOut = 17
    Timeout = 11
    UnknownInterface = 19
    UnknownMethod = 16
    UnknownObject = 20
    UnknownProperty = 21


class QDBusInterface(QDBusAbstractInterface):
    """ QDBusInterface(str, str, interface: str = '', connection: QDBusConnection = QDBusConnection.sessionBus(), parent: QObject = None) """
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

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, p_str, p_str_1, interface='', connection=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


class QDBusMessage(__sip.simplewrapper):
    """
    QDBusMessage()
    QDBusMessage(QDBusMessage)
    """
    def arguments(self): # real signature unknown; restored from __doc__
        """ arguments(self) -> List[Any] """
        return []

    def autoStartService(self): # real signature unknown; restored from __doc__
        """ autoStartService(self) -> bool """
        return False

    def createError(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        createError(str, str) -> QDBusMessage
        createError(QDBusError) -> QDBusMessage
        createError(QDBusError.ErrorType, str) -> QDBusMessage
        """
        return QDBusMessage

    def createErrorReply(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        createErrorReply(self, str, str) -> QDBusMessage
        createErrorReply(self, QDBusError) -> QDBusMessage
        createErrorReply(self, QDBusError.ErrorType, str) -> QDBusMessage
        """
        return QDBusMessage

    def createMethodCall(self, p_str, p_str_1, p_str_2, p_str_3): # real signature unknown; restored from __doc__
        """ createMethodCall(str, str, str, str) -> QDBusMessage """
        return QDBusMessage

    def createReply(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        createReply(self, arguments: Iterable[Any] = []) -> QDBusMessage
        createReply(self, Any) -> QDBusMessage
        """
        return QDBusMessage

    def createSignal(self, p_str, p_str_1, p_str_2): # real signature unknown; restored from __doc__
        """ createSignal(str, str, str) -> QDBusMessage """
        return QDBusMessage

    def createTargetedSignal(self, p_str, p_str_1, p_str_2, p_str_3): # real signature unknown; restored from __doc__
        """ createTargetedSignal(str, str, str, str) -> QDBusMessage """
        return QDBusMessage

    def errorMessage(self): # real signature unknown; restored from __doc__
        """ errorMessage(self) -> str """
        return ""

    def errorName(self): # real signature unknown; restored from __doc__
        """ errorName(self) -> str """
        return ""

    def interface(self): # real signature unknown; restored from __doc__
        """ interface(self) -> str """
        return ""

    def isDelayedReply(self): # real signature unknown; restored from __doc__
        """ isDelayedReply(self) -> bool """
        return False

    def isInteractiveAuthorizationAllowed(self): # real signature unknown; restored from __doc__
        """ isInteractiveAuthorizationAllowed(self) -> bool """
        return False

    def isReplyRequired(self): # real signature unknown; restored from __doc__
        """ isReplyRequired(self) -> bool """
        return False

    def member(self): # real signature unknown; restored from __doc__
        """ member(self) -> str """
        return ""

    def path(self): # real signature unknown; restored from __doc__
        """ path(self) -> str """
        return ""

    def service(self): # real signature unknown; restored from __doc__
        """ service(self) -> str """
        return ""

    def setArguments(self, Iterable, Any=None): # real signature unknown; restored from __doc__
        """ setArguments(self, Iterable[Any]) """
        pass

    def setAutoStartService(self, bool): # real signature unknown; restored from __doc__
        """ setAutoStartService(self, bool) """
        pass

    def setDelayedReply(self, bool): # real signature unknown; restored from __doc__
        """ setDelayedReply(self, bool) """
        pass

    def setInteractiveAuthorizationAllowed(self, bool): # real signature unknown; restored from __doc__
        """ setInteractiveAuthorizationAllowed(self, bool) """
        pass

    def signature(self): # real signature unknown; restored from __doc__
        """ signature(self) -> str """
        return ""

    def swap(self, QDBusMessage): # real signature unknown; restored from __doc__
        """ swap(self, QDBusMessage) """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QDBusMessage.MessageType """
        pass

    def __init__(self, QDBusMessage=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    ErrorMessage = 3
    InvalidMessage = 0
    MethodCallMessage = 1
    ReplyMessage = 2
    SignalMessage = 4


class QDBusObjectPath(__sip.simplewrapper):
    """
    QDBusObjectPath()
    QDBusObjectPath(str)
    QDBusObjectPath(QDBusObjectPath)
    """
    def path(self): # real signature unknown; restored from __doc__
        """ path(self) -> str """
        return ""

    def setPath(self, p_str): # real signature unknown; restored from __doc__
        """ setPath(self, str) """
        pass

    def swap(self, QDBusObjectPath): # real signature unknown; restored from __doc__
        """ swap(self, QDBusObjectPath) """
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



class QDBusPendingCall(__sip.simplewrapper):
    """ QDBusPendingCall(QDBusPendingCall) """
    def fromCompletedCall(self, QDBusMessage): # real signature unknown; restored from __doc__
        """ fromCompletedCall(QDBusMessage) -> QDBusPendingCall """
        return QDBusPendingCall

    def fromError(self, QDBusError): # real signature unknown; restored from __doc__
        """ fromError(QDBusError) -> QDBusPendingCall """
        return QDBusPendingCall

    def swap(self, QDBusPendingCall): # real signature unknown; restored from __doc__
        """ swap(self, QDBusPendingCall) """
        pass

    def __init__(self, QDBusPendingCall): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QDBusPendingCallWatcher(__PyQt5_QtCore.QObject, QDBusPendingCall):
    """ QDBusPendingCallWatcher(QDBusPendingCall, parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def finished(self, watcher=None): # real signature unknown; restored from __doc__
        """ finished(self, watcher: QDBusPendingCallWatcher = None) [signal] """
        pass

    def isFinished(self): # real signature unknown; restored from __doc__
        """ isFinished(self) -> bool """
        return False

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

    def waitForFinished(self): # real signature unknown; restored from __doc__
        """ waitForFinished(self) """
        pass

    def __init__(self, QDBusPendingCall, parent=None): # real signature unknown; restored from __doc__
        pass


class QDBusPendingReply(QDBusPendingCall):
    """
    QDBusPendingReply()
    QDBusPendingReply(QDBusPendingReply)
    QDBusPendingReply(QDBusPendingCall)
    QDBusPendingReply(QDBusMessage)
    """
    def argumentAt(self, p_int): # real signature unknown; restored from __doc__
        """ argumentAt(self, int) -> Any """
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> QDBusError """
        return QDBusError

    def isError(self): # real signature unknown; restored from __doc__
        """ isError(self) -> bool """
        return False

    def isFinished(self): # real signature unknown; restored from __doc__
        """ isFinished(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def reply(self): # real signature unknown; restored from __doc__
        """ reply(self) -> QDBusMessage """
        return QDBusMessage

    def value(self, type=None): # real signature unknown; restored from __doc__
        """ value(self, type: object = None) -> object """
        return object()

    def waitForFinished(self): # real signature unknown; restored from __doc__
        """ waitForFinished(self) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


class QDBusReply(__sip.simplewrapper):
    """
    QDBusReply(QDBusMessage)
    QDBusReply(QDBusPendingCall)
    QDBusReply(QDBusError)
    QDBusReply(QDBusReply)
    """
    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> QDBusError """
        return QDBusError

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def value(self, type=None): # real signature unknown; restored from __doc__
        """ value(self, type: object = None) -> object """
        return object()

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QDBusServiceWatcher(__PyQt5_QtCore.QObject):
    """
    QDBusServiceWatcher(parent: QObject = None)
    QDBusServiceWatcher(str, QDBusConnection, watchMode: Union[QDBusServiceWatcher.WatchMode, QDBusServiceWatcher.WatchModeFlag] = QDBusServiceWatcher.WatchForOwnerChange, parent: QObject = None)
    """
    def addWatchedService(self, p_str): # real signature unknown; restored from __doc__
        """ addWatchedService(self, str) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connection(self): # real signature unknown; restored from __doc__
        """ connection(self) -> QDBusConnection """
        return QDBusConnection

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

    def removeWatchedService(self, p_str): # real signature unknown; restored from __doc__
        """ removeWatchedService(self, str) -> bool """
        return False

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def serviceOwnerChanged(self, p_str, p_str_1, p_str_2): # real signature unknown; restored from __doc__
        """ serviceOwnerChanged(self, str, str, str) [signal] """
        pass

    def serviceRegistered(self, p_str): # real signature unknown; restored from __doc__
        """ serviceRegistered(self, str) [signal] """
        pass

    def serviceUnregistered(self, p_str): # real signature unknown; restored from __doc__
        """ serviceUnregistered(self, str) [signal] """
        pass

    def setConnection(self, QDBusConnection): # real signature unknown; restored from __doc__
        """ setConnection(self, QDBusConnection) """
        pass

    def setWatchedServices(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ setWatchedServices(self, Iterable[str]) """
        pass

    def setWatchMode(self, Union, QDBusServiceWatcher_WatchMode=None, QDBusServiceWatcher_WatchModeFlag=None): # real signature unknown; restored from __doc__
        """ setWatchMode(self, Union[QDBusServiceWatcher.WatchMode, QDBusServiceWatcher.WatchModeFlag]) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def watchedServices(self): # real signature unknown; restored from __doc__
        """ watchedServices(self) -> List[str] """
        return []

    def watchMode(self): # real signature unknown; restored from __doc__
        """ watchMode(self) -> QDBusServiceWatcher.WatchMode """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    WatchForOwnerChange = 3
    WatchForRegistration = 1
    WatchForUnregistration = 2


class QDBusSignature(__sip.simplewrapper):
    """
    QDBusSignature()
    QDBusSignature(str)
    QDBusSignature(QDBusSignature)
    """
    def setSignature(self, p_str): # real signature unknown; restored from __doc__
        """ setSignature(self, str) """
        pass

    def signature(self): # real signature unknown; restored from __doc__
        """ signature(self) -> str """
        return ""

    def swap(self, QDBusSignature): # real signature unknown; restored from __doc__
        """ swap(self, QDBusSignature) """
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



class QDBusUnixFileDescriptor(__sip.simplewrapper):
    """
    QDBusUnixFileDescriptor()
    QDBusUnixFileDescriptor(int)
    QDBusUnixFileDescriptor(QDBusUnixFileDescriptor)
    """
    def fileDescriptor(self): # real signature unknown; restored from __doc__
        """ fileDescriptor(self) -> int """
        return 0

    def isSupported(self): # real signature unknown; restored from __doc__
        """ isSupported() -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def setFileDescriptor(self, p_int): # real signature unknown; restored from __doc__
        """ setFileDescriptor(self, int) """
        pass

    def swap(self, QDBusUnixFileDescriptor): # real signature unknown; restored from __doc__
        """ swap(self, QDBusUnixFileDescriptor) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QDBusVariant(__sip.simplewrapper):
    """
    QDBusVariant()
    QDBusVariant(Any)
    QDBusVariant(QDBusVariant)
    """
    def setVariant(self, Any): # real signature unknown; restored from __doc__
        """ setVariant(self, Any) """
        pass

    def swap(self, QDBusVariant): # real signature unknown; restored from __doc__
        """ swap(self, QDBusVariant) """
        pass

    def variant(self): # real signature unknown; restored from __doc__
        """ variant(self) -> Any """
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


    __hash__ = None


# variables with complex values



