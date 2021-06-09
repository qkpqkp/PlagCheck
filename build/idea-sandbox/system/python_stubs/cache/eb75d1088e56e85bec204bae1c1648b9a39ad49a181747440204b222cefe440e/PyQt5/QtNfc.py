# encoding: utf-8
# module PyQt5.QtNfc
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtNfc.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


# no functions
# classes

class QNdefFilter(__sip.simplewrapper):
    """
    QNdefFilter()
    QNdefFilter(QNdefFilter)
    """
    def appendRecord(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        appendRecord(self, QNdefRecord.TypeNameFormat, Union[QByteArray, bytes, bytearray], min: int = 1, max: int = 1)
        appendRecord(self, QNdefFilter.Record)
        """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def orderMatch(self): # real signature unknown; restored from __doc__
        """ orderMatch(self) -> bool """
        return False

    def recordAt(self, p_int): # real signature unknown; restored from __doc__
        """ recordAt(self, int) -> QNdefFilter.Record """
        pass

    def recordCount(self): # real signature unknown; restored from __doc__
        """ recordCount(self) -> int """
        return 0

    def setOrderMatch(self, bool): # real signature unknown; restored from __doc__
        """ setOrderMatch(self, bool) """
        pass

    def __init__(self, QNdefFilter=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""




class QNdefMessage(__sip.simplewrapper):
    """
    QNdefMessage()
    QNdefMessage(QNdefRecord)
    QNdefMessage(QNdefMessage)
    QNdefMessage(Iterable[QNdefRecord])
    """
    def fromByteArray(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ fromByteArray(Union[QByteArray, bytes, bytearray]) -> QNdefMessage """
        return QNdefMessage

    def toByteArray(self): # real signature unknown; restored from __doc__
        """ toByteArray(self) -> QByteArray """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
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

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __hash__ = None


class QNdefRecord(__sip.simplewrapper):
    """
    QNdefRecord()
    QNdefRecord(QNdefRecord)
    """
    def id(self): # real signature unknown; restored from __doc__
        """ id(self) -> QByteArray """
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def payload(self): # real signature unknown; restored from __doc__
        """ payload(self) -> QByteArray """
        pass

    def setId(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setId(self, Union[QByteArray, bytes, bytearray]) """
        pass

    def setPayload(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setPayload(self, Union[QByteArray, bytes, bytearray]) """
        pass

    def setType(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setType(self, Union[QByteArray, bytes, bytearray]) """
        pass

    def setTypeNameFormat(self, QNdefRecord_TypeNameFormat): # real signature unknown; restored from __doc__
        """ setTypeNameFormat(self, QNdefRecord.TypeNameFormat) """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QByteArray """
        pass

    def typeNameFormat(self): # real signature unknown; restored from __doc__
        """ typeNameFormat(self) -> QNdefRecord.TypeNameFormat """
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

    def __init__(self, QNdefRecord=None): # real signature unknown; restored from __doc__ with multiple overloads
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


    Empty = 0
    ExternalRtd = 4
    Mime = 2
    NfcRtd = 1
    Unknown = 5
    Uri = 3


class QNdefNfcIconRecord(QNdefRecord):
    """
    QNdefNfcIconRecord()
    QNdefNfcIconRecord(QNdefRecord)
    QNdefNfcIconRecord(QNdefNfcIconRecord)
    """
    def data(self): # real signature unknown; restored from __doc__
        """ data(self) -> QByteArray """
        pass

    def setData(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setData(self, Union[QByteArray, bytes, bytearray]) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


class QNdefNfcSmartPosterRecord(QNdefRecord):
    """
    QNdefNfcSmartPosterRecord()
    QNdefNfcSmartPosterRecord(QNdefNfcSmartPosterRecord)
    QNdefNfcSmartPosterRecord(QNdefRecord)
    """
    def action(self): # real signature unknown; restored from __doc__
        """ action(self) -> QNdefNfcSmartPosterRecord.Action """
        pass

    def addIcon(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addIcon(self, QNdefNfcIconRecord)
        addIcon(self, Union[QByteArray, bytes, bytearray], Union[QByteArray, bytes, bytearray])
        """
        pass

    def addTitle(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addTitle(self, QNdefNfcTextRecord) -> bool
        addTitle(self, str, str, QNdefNfcTextRecord.Encoding) -> bool
        """
        return False

    def hasAction(self): # real signature unknown; restored from __doc__
        """ hasAction(self) -> bool """
        return False

    def hasIcon(self, mimetype, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ hasIcon(self, mimetype: Union[QByteArray, bytes, bytearray] = QByteArray()) -> bool """
        pass

    def hasSize(self): # real signature unknown; restored from __doc__
        """ hasSize(self) -> bool """
        return False

    def hasTitle(self, locale=''): # real signature unknown; restored from __doc__
        """ hasTitle(self, locale: str = '') -> bool """
        return False

    def hasTypeInfo(self): # real signature unknown; restored from __doc__
        """ hasTypeInfo(self) -> bool """
        return False

    def icon(self, mimetype, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ icon(self, mimetype: Union[QByteArray, bytes, bytearray] = QByteArray()) -> QByteArray """
        pass

    def iconCount(self): # real signature unknown; restored from __doc__
        """ iconCount(self) -> int """
        return 0

    def iconRecord(self, p_int): # real signature unknown; restored from __doc__
        """ iconRecord(self, int) -> QNdefNfcIconRecord """
        return QNdefNfcIconRecord

    def iconRecords(self): # real signature unknown; restored from __doc__
        """ iconRecords(self) -> List[QNdefNfcIconRecord] """
        return []

    def removeIcon(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        removeIcon(self, QNdefNfcIconRecord) -> bool
        removeIcon(self, Union[QByteArray, bytes, bytearray]) -> bool
        """
        return False

    def removeTitle(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        removeTitle(self, QNdefNfcTextRecord) -> bool
        removeTitle(self, str) -> bool
        """
        return False

    def setAction(self, QNdefNfcSmartPosterRecord_Action): # real signature unknown; restored from __doc__
        """ setAction(self, QNdefNfcSmartPosterRecord.Action) """
        pass

    def setIcons(self, Iterable, QNdefNfcIconRecord=None): # real signature unknown; restored from __doc__
        """ setIcons(self, Iterable[QNdefNfcIconRecord]) """
        pass

    def setPayload(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setPayload(self, Union[QByteArray, bytes, bytearray]) """
        pass

    def setSize(self, p_int): # real signature unknown; restored from __doc__
        """ setSize(self, int) """
        pass

    def setTitles(self, Iterable, QNdefNfcTextRecord=None): # real signature unknown; restored from __doc__
        """ setTitles(self, Iterable[QNdefNfcTextRecord]) """
        pass

    def setTypeInfo(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setTypeInfo(self, Union[QByteArray, bytes, bytearray]) """
        pass

    def setUri(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setUri(self, QNdefNfcUriRecord)
        setUri(self, QUrl)
        """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def title(self, locale=''): # real signature unknown; restored from __doc__
        """ title(self, locale: str = '') -> str """
        return ""

    def titleCount(self): # real signature unknown; restored from __doc__
        """ titleCount(self) -> int """
        return 0

    def titleRecord(self, p_int): # real signature unknown; restored from __doc__
        """ titleRecord(self, int) -> QNdefNfcTextRecord """
        return QNdefNfcTextRecord

    def titleRecords(self): # real signature unknown; restored from __doc__
        """ titleRecords(self) -> List[QNdefNfcTextRecord] """
        return []

    def typeInfo(self): # real signature unknown; restored from __doc__
        """ typeInfo(self) -> QByteArray """
        pass

    def uri(self): # real signature unknown; restored from __doc__
        """ uri(self) -> QUrl """
        pass

    def uriRecord(self): # real signature unknown; restored from __doc__
        """ uriRecord(self) -> QNdefNfcUriRecord """
        return QNdefNfcUriRecord

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    DoAction = 0
    EditAction = 2
    SaveAction = 1
    UnspecifiedAction = -1


class QNdefNfcTextRecord(QNdefRecord):
    """
    QNdefNfcTextRecord()
    QNdefNfcTextRecord(QNdefRecord)
    QNdefNfcTextRecord(QNdefNfcTextRecord)
    """
    def encoding(self): # real signature unknown; restored from __doc__
        """ encoding(self) -> QNdefNfcTextRecord.Encoding """
        pass

    def locale(self): # real signature unknown; restored from __doc__
        """ locale(self) -> str """
        return ""

    def setEncoding(self, QNdefNfcTextRecord_Encoding): # real signature unknown; restored from __doc__
        """ setEncoding(self, QNdefNfcTextRecord.Encoding) """
        pass

    def setLocale(self, p_str): # real signature unknown; restored from __doc__
        """ setLocale(self, str) """
        pass

    def setText(self, p_str): # real signature unknown; restored from __doc__
        """ setText(self, str) """
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    Utf16 = 1
    Utf8 = 0


class QNdefNfcUriRecord(QNdefRecord):
    """
    QNdefNfcUriRecord()
    QNdefNfcUriRecord(QNdefRecord)
    QNdefNfcUriRecord(QNdefNfcUriRecord)
    """
    def setUri(self, QUrl): # real signature unknown; restored from __doc__
        """ setUri(self, QUrl) """
        pass

    def uri(self): # real signature unknown; restored from __doc__
        """ uri(self) -> QUrl """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


class QNearFieldManager(__PyQt5_QtCore.QObject):
    """ QNearFieldManager(parent: QObject = None) """
    def adapterStateChanged(self, QNearFieldManager_AdapterState): # real signature unknown; restored from __doc__
        """ adapterStateChanged(self, QNearFieldManager.AdapterState) [signal] """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isAvailable(self): # real signature unknown; restored from __doc__
        """ isAvailable(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isSupported(self): # real signature unknown; restored from __doc__
        """ isSupported(self) -> bool """
        return False

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def registerNdefMessageHandler(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        registerNdefMessageHandler(self, PYQT_SLOT) -> int
        registerNdefMessageHandler(self, QNdefRecord.TypeNameFormat, Union[QByteArray, bytes, bytearray], PYQT_SLOT) -> int
        registerNdefMessageHandler(self, QNdefFilter, PYQT_SLOT) -> int
        """
        return 0

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setTargetAccessModes(self, Union, QNearFieldManager_TargetAccessModes=None, QNearFieldManager_TargetAccessMode=None): # real signature unknown; restored from __doc__
        """ setTargetAccessModes(self, Union[QNearFieldManager.TargetAccessModes, QNearFieldManager.TargetAccessMode]) """
        pass

    def startTargetDetection(self): # real signature unknown; restored from __doc__
        """ startTargetDetection(self) -> bool """
        return False

    def stopTargetDetection(self): # real signature unknown; restored from __doc__
        """ stopTargetDetection(self) """
        pass

    def targetAccessModes(self): # real signature unknown; restored from __doc__
        """ targetAccessModes(self) -> QNearFieldManager.TargetAccessModes """
        pass

    def targetDetected(self, QNearFieldTarget): # real signature unknown; restored from __doc__
        """ targetDetected(self, QNearFieldTarget) [signal] """
        pass

    def targetLost(self, QNearFieldTarget): # real signature unknown; restored from __doc__
        """ targetLost(self, QNearFieldTarget) [signal] """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def unregisterNdefMessageHandler(self, p_int): # real signature unknown; restored from __doc__
        """ unregisterNdefMessageHandler(self, int) -> bool """
        return False

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    NdefReadTargetAccess = 1
    NdefWriteTargetAccess = 2
    NoTargetAccess = 0
    TagTypeSpecificTargetAccess = 4


class QNearFieldShareManager(__PyQt5_QtCore.QObject):
    """ QNearFieldShareManager(parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, QNearFieldShareManager_ShareError): # real signature unknown; restored from __doc__
        """ error(self, QNearFieldShareManager.ShareError) [signal] """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setShareModes(self, Union, QNearFieldShareManager_ShareModes=None, QNearFieldShareManager_ShareMode=None): # real signature unknown; restored from __doc__
        """ setShareModes(self, Union[QNearFieldShareManager.ShareModes, QNearFieldShareManager.ShareMode]) """
        pass

    def shareError(self): # real signature unknown; restored from __doc__
        """ shareError(self) -> QNearFieldShareManager.ShareError """
        pass

    def shareModes(self): # real signature unknown; restored from __doc__
        """ shareModes(self) -> QNearFieldShareManager.ShareModes """
        pass

    def shareModesChanged(self, Union, QNearFieldShareManager_ShareModes=None, QNearFieldShareManager_ShareMode=None): # real signature unknown; restored from __doc__
        """ shareModesChanged(self, Union[QNearFieldShareManager.ShareModes, QNearFieldShareManager.ShareMode]) [signal] """
        pass

    def supportedShareModes(self): # real signature unknown; restored from __doc__
        """ supportedShareModes() -> QNearFieldShareManager.ShareModes """
        pass

    def targetDetected(self, QNearFieldShareTarget): # real signature unknown; restored from __doc__
        """ targetDetected(self, QNearFieldShareTarget) [signal] """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    FileShare = 2
    InvalidShareContentError = 2
    NdefShare = 1
    NoError = 0
    NoShare = 0
    ShareAlreadyInProgressError = 7
    ShareCanceledError = 3
    ShareInterruptedError = 4
    SharePermissionDeniedError = 8
    ShareRejectedError = 5
    UnknownError = 1
    UnsupportedShareModeError = 6


class QNearFieldShareTarget(__PyQt5_QtCore.QObject):
    # no doc
    def cancel(self): # real signature unknown; restored from __doc__
        """ cancel(self) """
        pass

    def error(self, QNearFieldShareManager_ShareError): # real signature unknown; restored from __doc__
        """ error(self, QNearFieldShareManager.ShareError) [signal] """
        pass

    def isShareInProgress(self): # real signature unknown; restored from __doc__
        """ isShareInProgress(self) -> bool """
        return False

    def share(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        share(self, QNdefMessage) -> bool
        share(self, Iterable[QFileInfo]) -> bool
        """
        return False

    def shareError(self): # real signature unknown; restored from __doc__
        """ shareError(self) -> QNearFieldShareManager.ShareError """
        pass

    def shareFinished(self): # real signature unknown; restored from __doc__
        """ shareFinished(self) [signal] """
        pass

    def shareModes(self): # real signature unknown; restored from __doc__
        """ shareModes(self) -> QNearFieldShareManager.ShareModes """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QNearFieldTarget(__PyQt5_QtCore.QObject):
    """ QNearFieldTarget(parent: QObject = None) """
    def accessMethods(self): # real signature unknown; restored from __doc__
        """ accessMethods(self) -> QNearFieldTarget.AccessMethods """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnect(self): # real signature unknown; restored from __doc__
        """ disconnect(self) -> bool """
        return False

    def disconnected(self): # real signature unknown; restored from __doc__
        """ disconnected(self) [signal] """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, QNearFieldTarget_Error, QNearFieldTarget_RequestId): # real signature unknown; restored from __doc__
        """ error(self, QNearFieldTarget.Error, QNearFieldTarget.RequestId) [signal] """
        pass

    def handleResponse(self, QNearFieldTarget_RequestId, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ handleResponse(self, QNearFieldTarget.RequestId, Union[QByteArray, bytes, bytearray]) -> bool """
        return False

    def hasNdefMessage(self): # real signature unknown; restored from __doc__
        """ hasNdefMessage(self) -> bool """
        return False

    def isProcessingCommand(self): # real signature unknown; restored from __doc__
        """ isProcessingCommand(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keepConnection(self): # real signature unknown; restored from __doc__
        """ keepConnection(self) -> bool """
        return False

    def maxCommandLength(self): # real signature unknown; restored from __doc__
        """ maxCommandLength(self) -> int """
        return 0

    def ndefMessageRead(self, QNdefMessage): # real signature unknown; restored from __doc__
        """ ndefMessageRead(self, QNdefMessage) [signal] """
        pass

    def ndefMessagesWritten(self): # real signature unknown; restored from __doc__
        """ ndefMessagesWritten(self) [signal] """
        pass

    def readNdefMessages(self): # real signature unknown; restored from __doc__
        """ readNdefMessages(self) -> QNearFieldTarget.RequestId """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def reportError(self, QNearFieldTarget_Error, QNearFieldTarget_RequestId): # real signature unknown; restored from __doc__
        """ reportError(self, QNearFieldTarget.Error, QNearFieldTarget.RequestId) """
        pass

    def requestCompleted(self, QNearFieldTarget_RequestId): # real signature unknown; restored from __doc__
        """ requestCompleted(self, QNearFieldTarget.RequestId) [signal] """
        pass

    def requestResponse(self, QNearFieldTarget_RequestId): # real signature unknown; restored from __doc__
        """ requestResponse(self, QNearFieldTarget.RequestId) -> Any """
        pass

    def sendCommand(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ sendCommand(self, Union[QByteArray, bytes, bytearray]) -> QNearFieldTarget.RequestId """
        pass

    def sendCommands(self, Iterable, Union=None, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ sendCommands(self, Iterable[Union[QByteArray, bytes, bytearray]]) -> QNearFieldTarget.RequestId """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setKeepConnection(self, bool): # real signature unknown; restored from __doc__
        """ setKeepConnection(self, bool) -> bool """
        return False

    def setResponseForRequest(self, QNearFieldTarget_RequestId, Any, emitRequestCompleted=True): # real signature unknown; restored from __doc__
        """ setResponseForRequest(self, QNearFieldTarget.RequestId, Any, emitRequestCompleted: bool = True) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QNearFieldTarget.Type """
        pass

    def uid(self): # real signature unknown; restored from __doc__
        """ uid(self) -> QByteArray """
        pass

    def url(self): # real signature unknown; restored from __doc__
        """ url(self) -> QUrl """
        pass

    def waitForRequestCompleted(self, QNearFieldTarget_RequestId, msecs=5000): # real signature unknown; restored from __doc__
        """ waitForRequestCompleted(self, QNearFieldTarget.RequestId, msecs: int = 5000) -> bool """
        return False

    def writeNdefMessages(self, Iterable, QNdefMessage=None): # real signature unknown; restored from __doc__
        """ writeNdefMessages(self, Iterable[QNdefMessage]) -> QNearFieldTarget.RequestId """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    ChecksumMismatchError = 5
    CommandError = 9
    InvalidParametersError = 6
    LlcpAccess = 4
    MifareTag = 5
    NdefAccess = 1
    NdefReadError = 7
    NdefWriteError = 8
    NfcTagType1 = 1
    NfcTagType2 = 2
    NfcTagType3 = 3
    NfcTagType4 = 4
    NoError = 0
    NoResponseError = 4
    ProprietaryTag = 0
    TagTypeSpecificAccess = 2
    TargetOutOfRangeError = 3
    UnknownAccess = 0
    UnknownError = 1
    UnsupportedError = 2


class QQmlNdefRecord(__PyQt5_QtCore.QObject):
    """
    QQmlNdefRecord(parent: QObject = None)
    QQmlNdefRecord(QNdefRecord, parent: QObject = None)
    """
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

    def record(self): # real signature unknown; restored from __doc__
        """ record(self) -> QNdefRecord """
        return QNdefRecord

    def recordChanged(self): # real signature unknown; restored from __doc__
        """ recordChanged(self) [signal] """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setRecord(self, QNdefRecord): # real signature unknown; restored from __doc__
        """ setRecord(self, QNdefRecord) """
        pass

    def setType(self, p_str): # real signature unknown; restored from __doc__
        """ setType(self, str) """
        pass

    def setTypeNameFormat(self, QQmlNdefRecord_TypeNameFormat): # real signature unknown; restored from __doc__
        """ setTypeNameFormat(self, QQmlNdefRecord.TypeNameFormat) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> str """
        return ""

    def typeChanged(self): # real signature unknown; restored from __doc__
        """ typeChanged(self) [signal] """
        pass

    def typeNameFormat(self): # real signature unknown; restored from __doc__
        """ typeNameFormat(self) -> QQmlNdefRecord.TypeNameFormat """
        pass

    def typeNameFormatChanged(self): # real signature unknown; restored from __doc__
        """ typeNameFormatChanged(self) [signal] """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    Empty = 0
    ExternalRtd = 4
    Mime = 2
    NfcRtd = 1
    Unknown = 5
    Uri = 3


# variables with complex values



