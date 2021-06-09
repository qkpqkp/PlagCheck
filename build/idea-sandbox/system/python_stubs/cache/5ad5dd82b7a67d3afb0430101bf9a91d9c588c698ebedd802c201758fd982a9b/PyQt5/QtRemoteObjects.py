# encoding: utf-8
# module PyQt5.QtRemoteObjects
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtRemoteObjects.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


# no functions
# classes

class QAbstractItemModelReplica(__PyQt5_QtCore.QAbstractItemModel):
    # no doc
    def availableRoles(self): # real signature unknown; restored from __doc__
        """ availableRoles(self) -> List[int] """
        return []

    def columnCount(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ columnCount(self, parent: QModelIndex = QModelIndex()) -> int """
        pass

    def data(self, QModelIndex, role=None): # real signature unknown; restored from __doc__
        """ data(self, QModelIndex, role: int = Qt.ItemDataRole.DisplayRole) -> Any """
        pass

    def flags(self, QModelIndex): # real signature unknown; restored from __doc__
        """ flags(self, QModelIndex) -> Qt.ItemFlags """
        pass

    def hasChildren(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ hasChildren(self, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def hasData(self, QModelIndex, p_int): # real signature unknown; restored from __doc__
        """ hasData(self, QModelIndex, int) -> bool """
        return False

    def headerData(self, p_int, Qt_Orientation, p_int_1): # real signature unknown; restored from __doc__
        """ headerData(self, int, Qt.Orientation, int) -> Any """
        pass

    def index(self, p_int, p_int_1, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ index(self, int, int, parent: QModelIndex = QModelIndex()) -> QModelIndex """
        pass

    def initialized(self): # real signature unknown; restored from __doc__
        """ initialized(self) [signal] """
        pass

    def isInitialized(self): # real signature unknown; restored from __doc__
        """ isInitialized(self) -> bool """
        return False

    def parent(self, QModelIndex): # real signature unknown; restored from __doc__
        """ parent(self, QModelIndex) -> QModelIndex """
        pass

    def roleNames(self): # real signature unknown; restored from __doc__
        """ roleNames(self) -> Dict[int, QByteArray] """
        return {}

    def rootCacheSize(self): # real signature unknown; restored from __doc__
        """ rootCacheSize(self) -> int """
        return 0

    def rowCount(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ rowCount(self, parent: QModelIndex = QModelIndex()) -> int """
        pass

    def selectionModel(self): # real signature unknown; restored from __doc__
        """ selectionModel(self) -> QItemSelectionModel """
        pass

    def setData(self, QModelIndex, Any, role=None): # real signature unknown; restored from __doc__
        """ setData(self, QModelIndex, Any, role: int = Qt.ItemDataRole.EditRole) -> bool """
        return False

    def setRootCacheSize(self, p_int): # real signature unknown; restored from __doc__
        """ setRootCacheSize(self, int) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QRemoteObjectAbstractPersistedStore(__PyQt5_QtCore.QObject):
    """ QRemoteObjectAbstractPersistedStore(parent: QObject = None) """
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

    def restoreProperties(self, p_str, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ restoreProperties(self, str, Union[QByteArray, bytes, bytearray]) -> List[Any] """
        return []

    def saveProperties(self, p_str, Union, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ saveProperties(self, str, Union[QByteArray, bytes, bytearray], Iterable[Any]) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


class QRemoteObjectReplica(__PyQt5_QtCore.QObject):
    # no doc
    def initialized(self): # real signature unknown; restored from __doc__
        """ initialized(self) [signal] """
        pass

    def isInitialized(self): # real signature unknown; restored from __doc__
        """ isInitialized(self) -> bool """
        return False

    def isReplicaValid(self): # real signature unknown; restored from __doc__
        """ isReplicaValid(self) -> bool """
        return False

    def node(self): # real signature unknown; restored from __doc__
        """ node(self) -> QRemoteObjectNode """
        return QRemoteObjectNode

    def setNode(self, QRemoteObjectNode): # real signature unknown; restored from __doc__
        """ setNode(self, QRemoteObjectNode) """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QRemoteObjectReplica.State """
        pass

    def stateChanged(self, QRemoteObjectReplica_State, QRemoteObjectReplica_State_1): # real signature unknown; restored from __doc__
        """ stateChanged(self, QRemoteObjectReplica.State, QRemoteObjectReplica.State) [signal] """
        pass

    def waitForSource(self, timeout=30000): # real signature unknown; restored from __doc__
        """ waitForSource(self, timeout: int = 30000) -> bool """
        return False

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    Default = 1
    SignatureMismatch = 4
    Suspect = 3
    Uninitialized = 0
    Valid = 2


class QRemoteObjectDynamicReplica(QRemoteObjectReplica):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QRemoteObjectNode(__PyQt5_QtCore.QObject):
    """
    QRemoteObjectNode(parent: QObject = None)
    QRemoteObjectNode(QUrl, parent: QObject = None)
    """
    def acquireDynamic(self, p_str): # real signature unknown; restored from __doc__
        """ acquireDynamic(self, str) -> QRemoteObjectDynamicReplica """
        return QRemoteObjectDynamicReplica

    def acquireModel(self, p_str, action=None, rolesHint, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ acquireModel(self, str, action: QtRemoteObjects.InitialAction = QtRemoteObjects.FetchRootSize, rolesHint: Iterable[int] = []) -> QAbstractItemModelReplica """
        pass

    def addClientSideConnection(self, QIODevice): # real signature unknown; restored from __doc__
        """ addClientSideConnection(self, QIODevice) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def connectToNode(self, QUrl): # real signature unknown; restored from __doc__
        """ connectToNode(self, QUrl) -> bool """
        return False

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, QRemoteObjectNode_ErrorCode): # real signature unknown; restored from __doc__
        """ error(self, QRemoteObjectNode.ErrorCode) [signal] """
        pass

    def heartbeatInterval(self): # real signature unknown; restored from __doc__
        """ heartbeatInterval(self) -> int """
        return 0

    def heartbeatIntervalChanged(self, p_int): # real signature unknown; restored from __doc__
        """ heartbeatIntervalChanged(self, int) [signal] """
        pass

    def instances(self, p_str): # real signature unknown; restored from __doc__
        """ instances(self, str) -> List[str] """
        return []

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def lastError(self): # real signature unknown; restored from __doc__
        """ lastError(self) -> QRemoteObjectNode.ErrorCode """
        pass

    def persistedStore(self): # real signature unknown; restored from __doc__
        """ persistedStore(self) -> QRemoteObjectAbstractPersistedStore """
        return QRemoteObjectAbstractPersistedStore

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def registry(self): # real signature unknown; restored from __doc__
        """ registry(self) -> QRemoteObjectRegistry """
        return QRemoteObjectRegistry

    def registryUrl(self): # real signature unknown; restored from __doc__
        """ registryUrl(self) -> QUrl """
        pass

    def remoteObjectAdded(self, Tuple, p_str=None, QRemoteObjectSourceLocationInfo=None): # real signature unknown; restored from __doc__
        """ remoteObjectAdded(self, Tuple[str, QRemoteObjectSourceLocationInfo]) [signal] """
        pass

    def remoteObjectRemoved(self, Tuple, p_str=None, QRemoteObjectSourceLocationInfo=None): # real signature unknown; restored from __doc__
        """ remoteObjectRemoved(self, Tuple[str, QRemoteObjectSourceLocationInfo]) [signal] """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setHeartbeatInterval(self, p_int): # real signature unknown; restored from __doc__
        """ setHeartbeatInterval(self, int) """
        pass

    def setName(self, p_str): # real signature unknown; restored from __doc__
        """ setName(self, str) """
        pass

    def setPersistedStore(self, QRemoteObjectAbstractPersistedStore): # real signature unknown; restored from __doc__
        """ setPersistedStore(self, QRemoteObjectAbstractPersistedStore) """
        pass

    def setRegistryUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ setRegistryUrl(self, QUrl) -> bool """
        return False

    def timerEvent(self, QTimerEvent): # real signature unknown; restored from __doc__
        """ timerEvent(self, QTimerEvent) """
        pass

    def waitForRegistry(self, timeout=30000): # real signature unknown; restored from __doc__
        """ waitForRegistry(self, timeout: int = 30000) -> bool """
        return False

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    HostUrlInvalid = 9
    ListenFailed = 11
    MissingObjectName = 8
    NodeIsNoServer = 3
    NoError = 0
    OperationNotValidOnClientNode = 6
    ProtocolMismatch = 10
    RegistryAlreadyHosted = 2
    RegistryNotAcquired = 1
    ServerAlreadyCreated = 4
    SourceNotRegistered = 7
    UnintendedRegistryHosting = 5


class QRemoteObjectHostBase(QRemoteObjectNode):
    # no doc
    def addHostSideConnection(self, QIODevice): # real signature unknown; restored from __doc__
        """ addHostSideConnection(self, QIODevice) """
        pass

    def disableRemoting(self, QObject): # real signature unknown; restored from __doc__
        """ disableRemoting(self, QObject) -> bool """
        return False

    def enableRemoting(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        enableRemoting(self, QObject, name: str = '') -> bool
        enableRemoting(self, QAbstractItemModel, str, Iterable[int], selectionModel: QItemSelectionModel = None) -> bool
        """
        return False

    def proxy(self, QUrl, hostUrl=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ proxy(self, QUrl, hostUrl: QUrl = QUrl()) -> bool """
        pass

    def reverseProxy(self): # real signature unknown; restored from __doc__
        """ reverseProxy(self) -> bool """
        return False

    def setName(self, p_str): # real signature unknown; restored from __doc__
        """ setName(self, str) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    AllowExternalRegistration = 1
    BuiltInSchemasOnly = 0


class QRemoteObjectHost(QRemoteObjectHostBase):
    """
    QRemoteObjectHost(parent: QObject = None)
    QRemoteObjectHost(QUrl, registryAddress: QUrl = QUrl(), allowedSchemas: QRemoteObjectHostBase.AllowedSchemas = QRemoteObjectHostBase.BuiltInSchemasOnly, parent: QObject = None)
    QRemoteObjectHost(QUrl, QObject)
    """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def hostUrl(self): # real signature unknown; restored from __doc__
        """ hostUrl(self) -> QUrl """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setHostUrl(self, QUrl, allowedSchemas=None): # real signature unknown; restored from __doc__
        """ setHostUrl(self, QUrl, allowedSchemas: QRemoteObjectHostBase.AllowedSchemas = QRemoteObjectHostBase.BuiltInSchemasOnly) -> bool """
        return False

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


class QRemoteObjectRegistry(QRemoteObjectReplica):
    # no doc
    def remoteObjectAdded(self, Tuple, p_str=None, QRemoteObjectSourceLocationInfo=None): # real signature unknown; restored from __doc__
        """ remoteObjectAdded(self, Tuple[str, QRemoteObjectSourceLocationInfo]) [signal] """
        pass

    def remoteObjectRemoved(self, Tuple, p_str=None, QRemoteObjectSourceLocationInfo=None): # real signature unknown; restored from __doc__
        """ remoteObjectRemoved(self, Tuple[str, QRemoteObjectSourceLocationInfo]) [signal] """
        pass

    def sourceLocations(self): # real signature unknown; restored from __doc__
        """ sourceLocations(self) -> Dict[str, QRemoteObjectSourceLocationInfo] """
        return {}

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QRemoteObjectRegistryHost(QRemoteObjectHostBase):
    """ QRemoteObjectRegistryHost(registryAddress: QUrl = QUrl(), parent: QObject = None) """
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

    def setRegistryUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ setRegistryUrl(self, QUrl) -> bool """
        return False

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, registryAddress=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


class QRemoteObjectSourceLocationInfo(__sip.simplewrapper):
    """
    QRemoteObjectSourceLocationInfo()
    QRemoteObjectSourceLocationInfo(str, QUrl)
    QRemoteObjectSourceLocationInfo(QRemoteObjectSourceLocationInfo)
    """
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


class QtRemoteObjects(__sip.simplewrapper):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    FetchRootSize = 0
    PrefetchData = 1


# variables with complex values



