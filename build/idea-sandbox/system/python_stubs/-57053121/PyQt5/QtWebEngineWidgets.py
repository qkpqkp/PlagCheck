# encoding: utf-8
# module PyQt5.QtWebEngineWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWebEngineWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtWidgets as __PyQt5_QtWidgets
import sip as __sip


# no functions
# classes

class QWebEngineCertificateError(__sip.simplewrapper):
    # no doc
    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> QWebEngineCertificateError.Error """
        pass

    def errorDescription(self): # real signature unknown; restored from __doc__
        """ errorDescription(self) -> str """
        return ""

    def isOverridable(self): # real signature unknown; restored from __doc__
        """ isOverridable(self) -> bool """
        return False

    def url(self): # real signature unknown; restored from __doc__
        """ url(self) -> QUrl """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    CertificateAuthorityInvalid = -202
    CertificateCommonNameInvalid = -200
    CertificateContainsErrors = -203
    CertificateDateInvalid = -201
    CertificateInvalid = -207
    CertificateNameConstraintViolation = -212
    CertificateNonUniqueName = -210
    CertificateNoRevocationMechanism = -204
    CertificateRevoked = -206
    CertificateTransparencyRequired = -214
    CertificateUnableToCheckRevocation = -205
    CertificateValidityTooLong = -213
    CertificateWeakKey = -211
    CertificateWeakSignatureAlgorithm = -208
    SslPinnedKeyNotInCertificateChain = -150


class QWebEngineClientCertificateSelection(__sip.simplewrapper):
    """ QWebEngineClientCertificateSelection(QWebEngineClientCertificateSelection) """
    def certificates(self): # real signature unknown; restored from __doc__
        """ certificates(self) -> List[QSslCertificate] """
        return []

    def host(self): # real signature unknown; restored from __doc__
        """ host(self) -> QUrl """
        pass

    def select(self, QSslCertificate): # real signature unknown; restored from __doc__
        """ select(self, QSslCertificate) """
        pass

    def selectNone(self): # real signature unknown; restored from __doc__
        """ selectNone(self) """
        pass

    def __init__(self, QWebEngineClientCertificateSelection): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QWebEngineContextMenuData(__sip.simplewrapper):
    """
    QWebEngineContextMenuData()
    QWebEngineContextMenuData(QWebEngineContextMenuData)
    """
    def editFlags(self): # real signature unknown; restored from __doc__
        """ editFlags(self) -> QWebEngineContextMenuData.EditFlags """
        pass

    def isContentEditable(self): # real signature unknown; restored from __doc__
        """ isContentEditable(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def linkText(self): # real signature unknown; restored from __doc__
        """ linkText(self) -> str """
        return ""

    def linkUrl(self): # real signature unknown; restored from __doc__
        """ linkUrl(self) -> QUrl """
        pass

    def mediaFlags(self): # real signature unknown; restored from __doc__
        """ mediaFlags(self) -> QWebEngineContextMenuData.MediaFlags """
        pass

    def mediaType(self): # real signature unknown; restored from __doc__
        """ mediaType(self) -> QWebEngineContextMenuData.MediaType """
        pass

    def mediaUrl(self): # real signature unknown; restored from __doc__
        """ mediaUrl(self) -> QUrl """
        pass

    def misspelledWord(self): # real signature unknown; restored from __doc__
        """ misspelledWord(self) -> str """
        return ""

    def position(self): # real signature unknown; restored from __doc__
        """ position(self) -> QPoint """
        pass

    def selectedText(self): # real signature unknown; restored from __doc__
        """ selectedText(self) -> str """
        return ""

    def spellCheckerSuggestions(self): # real signature unknown; restored from __doc__
        """ spellCheckerSuggestions(self) -> List[str] """
        return []

    def __init__(self, QWebEngineContextMenuData=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    CanCopy = 8
    CanCut = 4
    CanDelete = 32
    CanEditRichly = 256
    CanPaste = 16
    CanRedo = 2
    CanSelectAll = 64
    CanTranslate = 128
    CanUndo = 1
    MediaCanPrint = 256
    MediaCanRotate = 512
    MediaCanSave = 16
    MediaCanToggleControls = 64
    MediaControls = 128
    MediaHasAudio = 32
    MediaInError = 1
    MediaLoop = 8
    MediaMuted = 4
    MediaPaused = 2
    MediaTypeAudio = 3
    MediaTypeCanvas = 4
    MediaTypeFile = 5
    MediaTypeImage = 1
    MediaTypeNone = 0
    MediaTypePlugin = 6
    MediaTypeVideo = 2


class QWebEngineDownloadItem(__PyQt5_QtCore.QObject):
    # no doc
    def accept(self): # real signature unknown; restored from __doc__
        """ accept(self) """
        pass

    def cancel(self): # real signature unknown; restored from __doc__
        """ cancel(self) """
        pass

    def downloadProgress(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ downloadProgress(self, int, int) [signal] """
        pass

    def finished(self): # real signature unknown; restored from __doc__
        """ finished(self) [signal] """
        pass

    def id(self): # real signature unknown; restored from __doc__
        """ id(self) -> int """
        return 0

    def interruptReason(self): # real signature unknown; restored from __doc__
        """ interruptReason(self) -> QWebEngineDownloadItem.DownloadInterruptReason """
        pass

    def interruptReasonString(self): # real signature unknown; restored from __doc__
        """ interruptReasonString(self) -> str """
        return ""

    def isFinished(self): # real signature unknown; restored from __doc__
        """ isFinished(self) -> bool """
        return False

    def isPaused(self): # real signature unknown; restored from __doc__
        """ isPaused(self) -> bool """
        return False

    def isPausedChanged(self, bool): # real signature unknown; restored from __doc__
        """ isPausedChanged(self, bool) [signal] """
        pass

    def isSavePageDownload(self): # real signature unknown; restored from __doc__
        """ isSavePageDownload(self) -> bool """
        return False

    def mimeType(self): # real signature unknown; restored from __doc__
        """ mimeType(self) -> str """
        return ""

    def page(self): # real signature unknown; restored from __doc__
        """ page(self) -> QWebEnginePage """
        return QWebEnginePage

    def path(self): # real signature unknown; restored from __doc__
        """ path(self) -> str """
        return ""

    def pause(self): # real signature unknown; restored from __doc__
        """ pause(self) """
        pass

    def receivedBytes(self): # real signature unknown; restored from __doc__
        """ receivedBytes(self) -> int """
        return 0

    def resume(self): # real signature unknown; restored from __doc__
        """ resume(self) """
        pass

    def savePageFormat(self): # real signature unknown; restored from __doc__
        """ savePageFormat(self) -> QWebEngineDownloadItem.SavePageFormat """
        pass

    def setPath(self, p_str): # real signature unknown; restored from __doc__
        """ setPath(self, str) """
        pass

    def setSavePageFormat(self, QWebEngineDownloadItem_SavePageFormat): # real signature unknown; restored from __doc__
        """ setSavePageFormat(self, QWebEngineDownloadItem.SavePageFormat) """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QWebEngineDownloadItem.DownloadState """
        pass

    def stateChanged(self, QWebEngineDownloadItem_DownloadState): # real signature unknown; restored from __doc__
        """ stateChanged(self, QWebEngineDownloadItem.DownloadState) [signal] """
        pass

    def totalBytes(self): # real signature unknown; restored from __doc__
        """ totalBytes(self) -> int """
        return 0

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QWebEngineDownloadItem.DownloadType """
        pass

    def url(self): # real signature unknown; restored from __doc__
        """ url(self) -> QUrl """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    Attachment = 0
    CompleteHtmlSaveFormat = 1
    DownloadAttribute = 1
    DownloadCancelled = 3
    DownloadCompleted = 2
    DownloadInProgress = 1
    DownloadInterrupted = 4
    DownloadRequested = 0
    FileAccessDenied = 2
    FileBlocked = 11
    FileFailed = 1
    FileHashMismatch = 14
    FileNameTooLong = 5
    FileNoSpace = 3
    FileSecurityCheckFailed = 12
    FileTooLarge = 6
    FileTooShort = 13
    FileTransientError = 10
    FileVirusInfected = 7
    MimeHtmlSaveFormat = 2
    NetworkDisconnected = 22
    NetworkFailed = 20
    NetworkInvalidRequest = 24
    NetworkServerDown = 23
    NetworkTimeout = 21
    NoReason = 0
    SavePage = 3
    ServerBadContent = 33
    ServerCertProblem = 35
    ServerFailed = 30
    ServerForbidden = 36
    ServerUnauthorized = 34
    ServerUnreachable = 37
    SingleHtmlSaveFormat = 0
    UnknownSaveFormat = -1
    UserCanceled = 40
    UserRequested = 2


class QWebEngineFullScreenRequest(__sip.simplewrapper):
    """ QWebEngineFullScreenRequest(QWebEngineFullScreenRequest) """
    def accept(self): # real signature unknown; restored from __doc__
        """ accept(self) """
        pass

    def origin(self): # real signature unknown; restored from __doc__
        """ origin(self) -> QUrl """
        pass

    def reject(self): # real signature unknown; restored from __doc__
        """ reject(self) """
        pass

    def toggleOn(self): # real signature unknown; restored from __doc__
        """ toggleOn(self) -> bool """
        return False

    def __init__(self, QWebEngineFullScreenRequest): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QWebEngineHistory(__sip.simplewrapper):
    # no doc
    def back(self): # real signature unknown; restored from __doc__
        """ back(self) """
        pass

    def backItem(self): # real signature unknown; restored from __doc__
        """ backItem(self) -> QWebEngineHistoryItem """
        return QWebEngineHistoryItem

    def backItems(self, p_int): # real signature unknown; restored from __doc__
        """ backItems(self, int) -> List[QWebEngineHistoryItem] """
        return []

    def canGoBack(self): # real signature unknown; restored from __doc__
        """ canGoBack(self) -> bool """
        return False

    def canGoForward(self): # real signature unknown; restored from __doc__
        """ canGoForward(self) -> bool """
        return False

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def currentItem(self): # real signature unknown; restored from __doc__
        """ currentItem(self) -> QWebEngineHistoryItem """
        return QWebEngineHistoryItem

    def currentItemIndex(self): # real signature unknown; restored from __doc__
        """ currentItemIndex(self) -> int """
        return 0

    def forward(self): # real signature unknown; restored from __doc__
        """ forward(self) """
        pass

    def forwardItem(self): # real signature unknown; restored from __doc__
        """ forwardItem(self) -> QWebEngineHistoryItem """
        return QWebEngineHistoryItem

    def forwardItems(self, p_int): # real signature unknown; restored from __doc__
        """ forwardItems(self, int) -> List[QWebEngineHistoryItem] """
        return []

    def goToItem(self, QWebEngineHistoryItem): # real signature unknown; restored from __doc__
        """ goToItem(self, QWebEngineHistoryItem) """
        pass

    def itemAt(self, p_int): # real signature unknown; restored from __doc__
        """ itemAt(self, int) -> QWebEngineHistoryItem """
        return QWebEngineHistoryItem

    def items(self): # real signature unknown; restored from __doc__
        """ items(self) -> List[QWebEngineHistoryItem] """
        return []

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QWebEngineHistoryItem(__sip.simplewrapper):
    """ QWebEngineHistoryItem(QWebEngineHistoryItem) """
    def iconUrl(self): # real signature unknown; restored from __doc__
        """ iconUrl(self) -> QUrl """
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def lastVisited(self): # real signature unknown; restored from __doc__
        """ lastVisited(self) -> QDateTime """
        pass

    def originalUrl(self): # real signature unknown; restored from __doc__
        """ originalUrl(self) -> QUrl """
        pass

    def swap(self, QWebEngineHistoryItem): # real signature unknown; restored from __doc__
        """ swap(self, QWebEngineHistoryItem) """
        pass

    def title(self): # real signature unknown; restored from __doc__
        """ title(self) -> str """
        return ""

    def url(self): # real signature unknown; restored from __doc__
        """ url(self) -> QUrl """
        pass

    def __init__(self, QWebEngineHistoryItem): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QWebEnginePage(__PyQt5_QtCore.QObject):
    """
    QWebEnginePage(parent: QObject = None)
    QWebEnginePage(QWebEngineProfile, parent: QObject = None)
    """
    def acceptNavigationRequest(self, QUrl, QWebEnginePage_NavigationType, bool): # real signature unknown; restored from __doc__
        """ acceptNavigationRequest(self, QUrl, QWebEnginePage.NavigationType, bool) -> bool """
        return False

    def action(self, QWebEnginePage_WebAction): # real signature unknown; restored from __doc__
        """ action(self, QWebEnginePage.WebAction) -> QAction """
        pass

    def audioMutedChanged(self, bool): # real signature unknown; restored from __doc__
        """ audioMutedChanged(self, bool) [signal] """
        pass

    def authenticationRequired(self, QUrl, QAuthenticator): # real signature unknown; restored from __doc__
        """ authenticationRequired(self, QUrl, QAuthenticator) [signal] """
        pass

    def backgroundColor(self): # real signature unknown; restored from __doc__
        """ backgroundColor(self) -> QColor """
        pass

    def certificateError(self, QWebEngineCertificateError): # real signature unknown; restored from __doc__
        """ certificateError(self, QWebEngineCertificateError) -> bool """
        return False

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def chooseFiles(self, QWebEnginePage_FileSelectionMode, Iterable, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ chooseFiles(self, QWebEnginePage.FileSelectionMode, Iterable[str], Iterable[str]) -> List[str] """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contentsSize(self): # real signature unknown; restored from __doc__
        """ contentsSize(self) -> QSizeF """
        pass

    def contentsSizeChanged(self, QSizeF): # real signature unknown; restored from __doc__
        """ contentsSizeChanged(self, QSizeF) [signal] """
        pass

    def contextMenuData(self): # real signature unknown; restored from __doc__
        """ contextMenuData(self) -> QWebEngineContextMenuData """
        return QWebEngineContextMenuData

    def createStandardContextMenu(self): # real signature unknown; restored from __doc__
        """ createStandardContextMenu(self) -> QMenu """
        pass

    def createWindow(self, QWebEnginePage_WebWindowType): # real signature unknown; restored from __doc__
        """ createWindow(self, QWebEnginePage.WebWindowType) -> QWebEnginePage """
        return QWebEnginePage

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def devToolsPage(self): # real signature unknown; restored from __doc__
        """ devToolsPage(self) -> QWebEnginePage """
        return QWebEnginePage

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def download(self, QUrl, filename=''): # real signature unknown; restored from __doc__
        """ download(self, QUrl, filename: str = '') """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def featurePermissionRequestCanceled(self, QUrl, QWebEnginePage_Feature): # real signature unknown; restored from __doc__
        """ featurePermissionRequestCanceled(self, QUrl, QWebEnginePage.Feature) [signal] """
        pass

    def featurePermissionRequested(self, QUrl, QWebEnginePage_Feature): # real signature unknown; restored from __doc__
        """ featurePermissionRequested(self, QUrl, QWebEnginePage.Feature) [signal] """
        pass

    def findText(self, p_str, options, QWebEnginePage_FindFlags=None, QWebEnginePage_FindFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ findText(self, str, options: Union[QWebEnginePage.FindFlags, QWebEnginePage.FindFlag] = QWebEnginePage.FindFlags(), resultCallback: Callable[[bool], None] = 0) """
        pass

    def fullScreenRequested(self, QWebEngineFullScreenRequest): # real signature unknown; restored from __doc__
        """ fullScreenRequested(self, QWebEngineFullScreenRequest) [signal] """
        pass

    def geometryChangeRequested(self, QRect): # real signature unknown; restored from __doc__
        """ geometryChangeRequested(self, QRect) [signal] """
        pass

    def hasSelection(self): # real signature unknown; restored from __doc__
        """ hasSelection(self) -> bool """
        return False

    def history(self): # real signature unknown; restored from __doc__
        """ history(self) -> QWebEngineHistory """
        return QWebEngineHistory

    def icon(self): # real signature unknown; restored from __doc__
        """ icon(self) -> QIcon """
        pass

    def iconChanged(self, QIcon): # real signature unknown; restored from __doc__
        """ iconChanged(self, QIcon) [signal] """
        pass

    def iconUrl(self): # real signature unknown; restored from __doc__
        """ iconUrl(self) -> QUrl """
        pass

    def iconUrlChanged(self, QUrl): # real signature unknown; restored from __doc__
        """ iconUrlChanged(self, QUrl) [signal] """
        pass

    def inspectedPage(self): # real signature unknown; restored from __doc__
        """ inspectedPage(self) -> QWebEnginePage """
        return QWebEnginePage

    def isAudioMuted(self): # real signature unknown; restored from __doc__
        """ isAudioMuted(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def javaScriptAlert(self, QUrl, p_str): # real signature unknown; restored from __doc__
        """ javaScriptAlert(self, QUrl, str) """
        pass

    def javaScriptConfirm(self, QUrl, p_str): # real signature unknown; restored from __doc__
        """ javaScriptConfirm(self, QUrl, str) -> bool """
        return False

    def javaScriptConsoleMessage(self, QWebEnginePage_JavaScriptConsoleMessageLevel, p_str, p_int, p_str_1): # real signature unknown; restored from __doc__
        """ javaScriptConsoleMessage(self, QWebEnginePage.JavaScriptConsoleMessageLevel, str, int, str) """
        pass

    def javaScriptPrompt(self, QUrl, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ javaScriptPrompt(self, QUrl, str, str) -> Tuple[bool, str] """
        pass

    def linkHovered(self, p_str): # real signature unknown; restored from __doc__
        """ linkHovered(self, str) [signal] """
        pass

    def load(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        load(self, QUrl)
        load(self, QWebEngineHttpRequest)
        """
        pass

    def loadFinished(self, bool): # real signature unknown; restored from __doc__
        """ loadFinished(self, bool) [signal] """
        pass

    def loadProgress(self, p_int): # real signature unknown; restored from __doc__
        """ loadProgress(self, int) [signal] """
        pass

    def loadStarted(self): # real signature unknown; restored from __doc__
        """ loadStarted(self) [signal] """
        pass

    def pdfPrintingFinished(self, p_str, bool): # real signature unknown; restored from __doc__
        """ pdfPrintingFinished(self, str, bool) [signal] """
        pass

    def print(self, QPrinter, Callable, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ print(self, QPrinter, Callable[[bool], None]) """
        pass

    def printRequested(self): # real signature unknown; restored from __doc__
        """ printRequested(self) [signal] """
        pass

    def printToPdf(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        printToPdf(self, str, pageLayout: QPageLayout = QPageLayout(QPageSize(QPageSize.PageSizeId.A4),QPageLayout.Orientation.Portrait,QMarginsF()))
        printToPdf(self, Callable[[Union[QByteArray, bytes, bytearray]], None], pageLayout: QPageLayout = QPageLayout(QPageSize(QPageSize.PageSizeId.A4),QPageLayout.Orientation.Portrait,QMarginsF()))
        """
        pass

    def profile(self): # real signature unknown; restored from __doc__
        """ profile(self) -> QWebEngineProfile """
        return QWebEngineProfile

    def proxyAuthenticationRequired(self, QUrl, QAuthenticator, p_str): # real signature unknown; restored from __doc__
        """ proxyAuthenticationRequired(self, QUrl, QAuthenticator, str) [signal] """
        pass

    def quotaRequested(self, QWebEngineQuotaRequest): # real signature unknown; restored from __doc__
        """ quotaRequested(self, QWebEngineQuotaRequest) [signal] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def recentlyAudible(self): # real signature unknown; restored from __doc__
        """ recentlyAudible(self) -> bool """
        return False

    def recentlyAudibleChanged(self, bool): # real signature unknown; restored from __doc__
        """ recentlyAudibleChanged(self, bool) [signal] """
        pass

    def registerProtocolHandlerRequested(self, QWebEngineRegisterProtocolHandlerRequest): # real signature unknown; restored from __doc__
        """ registerProtocolHandlerRequested(self, QWebEngineRegisterProtocolHandlerRequest) [signal] """
        pass

    def renderProcessTerminated(self, QWebEnginePage_RenderProcessTerminationStatus, p_int): # real signature unknown; restored from __doc__
        """ renderProcessTerminated(self, QWebEnginePage.RenderProcessTerminationStatus, int) [signal] """
        pass

    def replaceMisspelledWord(self, p_str): # real signature unknown; restored from __doc__
        """ replaceMisspelledWord(self, str) """
        pass

    def requestedUrl(self): # real signature unknown; restored from __doc__
        """ requestedUrl(self) -> QUrl """
        pass

    def runJavaScript(self, p_str, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        runJavaScript(self, str, int)
        runJavaScript(self, str, int, Callable[..., None])
        runJavaScript(self, str)
        runJavaScript(self, str, Callable[[Any], None])
        """
        pass

    def save(self, p_str, format=None): # real signature unknown; restored from __doc__
        """ save(self, str, format: QWebEngineDownloadItem.SavePageFormat = QWebEngineDownloadItem.MimeHtmlSaveFormat) """
        pass

    def scripts(self): # real signature unknown; restored from __doc__
        """ scripts(self) -> QWebEngineScriptCollection """
        return QWebEngineScriptCollection

    def scrollPosition(self): # real signature unknown; restored from __doc__
        """ scrollPosition(self) -> QPointF """
        pass

    def scrollPositionChanged(self, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ scrollPositionChanged(self, Union[QPointF, QPoint]) [signal] """
        pass

    def selectClientCertificate(self, QWebEngineClientCertificateSelection): # real signature unknown; restored from __doc__
        """ selectClientCertificate(self, QWebEngineClientCertificateSelection) [signal] """
        pass

    def selectedText(self): # real signature unknown; restored from __doc__
        """ selectedText(self) -> str """
        return ""

    def selectionChanged(self): # real signature unknown; restored from __doc__
        """ selectionChanged(self) [signal] """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAudioMuted(self, bool): # real signature unknown; restored from __doc__
        """ setAudioMuted(self, bool) """
        pass

    def setBackgroundColor(self, Union, QColor=None, Qt_GlobalColor=None): # real signature unknown; restored from __doc__
        """ setBackgroundColor(self, Union[QColor, Qt.GlobalColor]) """
        pass

    def setContent(self, Union, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setContent(self, Union[QByteArray, bytes, bytearray], mimeType: str = '', baseUrl: QUrl = QUrl()) """
        pass

    def setDevToolsPage(self, QWebEnginePage): # real signature unknown; restored from __doc__
        """ setDevToolsPage(self, QWebEnginePage) """
        pass

    def setFeaturePermission(self, QUrl, QWebEnginePage_Feature, QWebEnginePage_PermissionPolicy): # real signature unknown; restored from __doc__
        """ setFeaturePermission(self, QUrl, QWebEnginePage.Feature, QWebEnginePage.PermissionPolicy) """
        pass

    def setHtml(self, p_str, baseUrl=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setHtml(self, str, baseUrl: QUrl = QUrl()) """
        pass

    def setInspectedPage(self, QWebEnginePage): # real signature unknown; restored from __doc__
        """ setInspectedPage(self, QWebEnginePage) """
        pass

    def settings(self): # real signature unknown; restored from __doc__
        """ settings(self) -> QWebEngineSettings """
        return QWebEngineSettings

    def setUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ setUrl(self, QUrl) """
        pass

    def setView(self, QWidget): # real signature unknown; restored from __doc__
        """ setView(self, QWidget) """
        pass

    def setWebChannel(self, QWebChannel, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setWebChannel(self, QWebChannel)
        setWebChannel(self, QWebChannel, int)
        """
        pass

    def setZoomFactor(self, p_float): # real signature unknown; restored from __doc__
        """ setZoomFactor(self, float) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def title(self): # real signature unknown; restored from __doc__
        """ title(self) -> str """
        return ""

    def titleChanged(self, p_str): # real signature unknown; restored from __doc__
        """ titleChanged(self, str) [signal] """
        pass

    def toHtml(self, Callable, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ toHtml(self, Callable[[str], None]) """
        pass

    def toPlainText(self, Callable, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ toPlainText(self, Callable[[str], None]) """
        pass

    def triggerAction(self, QWebEnginePage_WebAction, checked=False): # real signature unknown; restored from __doc__
        """ triggerAction(self, QWebEnginePage.WebAction, checked: bool = False) """
        pass

    def url(self): # real signature unknown; restored from __doc__
        """ url(self) -> QUrl """
        pass

    def urlChanged(self, QUrl): # real signature unknown; restored from __doc__
        """ urlChanged(self, QUrl) [signal] """
        pass

    def view(self): # real signature unknown; restored from __doc__
        """ view(self) -> QWidget """
        pass

    def webChannel(self): # real signature unknown; restored from __doc__
        """ webChannel(self) -> QWebChannel """
        pass

    def windowCloseRequested(self): # real signature unknown; restored from __doc__
        """ windowCloseRequested(self) [signal] """
        pass

    def zoomFactor(self): # real signature unknown; restored from __doc__
        """ zoomFactor(self) -> float """
        return 0.0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AbnormalTerminationStatus = 1
    AlignCenter = 38
    AlignJustified = 40
    AlignLeft = 37
    AlignRight = 39
    Back = 0
    Copy = 5
    CopyImageToClipboard = 17
    CopyImageUrlToClipboard = 18
    CopyLinkToClipboard = 15
    CopyMediaUrlToClipboard = 20
    CrashedTerminationStatus = 2
    Cut = 4
    DesktopAudioVideoCapture = 7
    DesktopVideoCapture = 6
    DownloadImageToDisk = 19
    DownloadLinkToDisk = 16
    DownloadMediaToDisk = 25
    ErrorMessageLevel = 2
    ExitFullScreen = 27
    FileSelectOpen = 0
    FileSelectOpenMultiple = 1
    FindBackward = 1
    FindCaseSensitively = 2
    Forward = 1
    Geolocation = 1
    Indent = 41
    InfoMessageLevel = 0
    InsertOrderedList = 43
    InsertUnorderedList = 44
    InspectElement = 26
    KilledTerminationStatus = 3
    MediaAudioCapture = 2
    MediaAudioVideoCapture = 4
    MediaVideoCapture = 3
    MouseLock = 5
    NavigationTypeBackForward = 3
    NavigationTypeFormSubmitted = 2
    NavigationTypeLinkClicked = 0
    NavigationTypeOther = 5
    NavigationTypeReload = 4
    NavigationTypeTyped = 1
    NormalTerminationStatus = 0
    NoWebAction = -1
    OpenLinkInNewBackgroundTab = 31
    OpenLinkInNewTab = 14
    OpenLinkInNewWindow = 13
    OpenLinkInThisWindow = 12
    Outdent = 42
    Paste = 6
    PasteAndMatchStyle = 11
    PermissionDeniedByUser = 2
    PermissionGrantedByUser = 1
    PermissionUnknown = 0
    Redo = 8
    Reload = 3
    ReloadAndBypassCache = 10
    RequestClose = 28
    SavePage = 30
    SelectAll = 9
    Stop = 2
    ToggleBold = 33
    ToggleItalic = 34
    ToggleMediaControls = 21
    ToggleMediaLoop = 22
    ToggleMediaMute = 24
    ToggleMediaPlayPause = 23
    ToggleStrikethrough = 36
    ToggleUnderline = 35
    Undo = 7
    Unselect = 29
    ViewSource = 32
    WarningMessageLevel = 1
    WebBrowserBackgroundTab = 3
    WebBrowserTab = 1
    WebBrowserWindow = 0
    WebDialog = 2


class QWebEngineProfile(__PyQt5_QtCore.QObject):
    """
    QWebEngineProfile(parent: QObject = None)
    QWebEngineProfile(str, parent: QObject = None)
    """
    def cachePath(self): # real signature unknown; restored from __doc__
        """ cachePath(self) -> str """
        return ""

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clearAllVisitedLinks(self): # real signature unknown; restored from __doc__
        """ clearAllVisitedLinks(self) """
        pass

    def clearHttpCache(self): # real signature unknown; restored from __doc__
        """ clearHttpCache(self) """
        pass

    def clearVisitedLinks(self, Iterable, QUrl=None): # real signature unknown; restored from __doc__
        """ clearVisitedLinks(self, Iterable[QUrl]) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def cookieStore(self): # real signature unknown; restored from __doc__
        """ cookieStore(self) -> QWebEngineCookieStore """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultProfile(self): # real signature unknown; restored from __doc__
        """ defaultProfile() -> QWebEngineProfile """
        return QWebEngineProfile

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def downloadRequested(self, QWebEngineDownloadItem): # real signature unknown; restored from __doc__
        """ downloadRequested(self, QWebEngineDownloadItem) [signal] """
        pass

    def httpAcceptLanguage(self): # real signature unknown; restored from __doc__
        """ httpAcceptLanguage(self) -> str """
        return ""

    def httpCacheMaximumSize(self): # real signature unknown; restored from __doc__
        """ httpCacheMaximumSize(self) -> int """
        return 0

    def httpCacheType(self): # real signature unknown; restored from __doc__
        """ httpCacheType(self) -> QWebEngineProfile.HttpCacheType """
        pass

    def httpUserAgent(self): # real signature unknown; restored from __doc__
        """ httpUserAgent(self) -> str """
        return ""

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

    def persistentCookiesPolicy(self): # real signature unknown; restored from __doc__
        """ persistentCookiesPolicy(self) -> QWebEngineProfile.PersistentCookiesPolicy """
        pass

    def persistentStoragePath(self): # real signature unknown; restored from __doc__
        """ persistentStoragePath(self) -> str """
        return ""

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

    def scripts(self): # real signature unknown; restored from __doc__
        """ scripts(self) -> QWebEngineScriptCollection """
        return QWebEngineScriptCollection

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

    def setHttpCacheType(self, QWebEngineProfile_HttpCacheType): # real signature unknown; restored from __doc__
        """ setHttpCacheType(self, QWebEngineProfile.HttpCacheType) """
        pass

    def setHttpUserAgent(self, p_str): # real signature unknown; restored from __doc__
        """ setHttpUserAgent(self, str) """
        pass

    def setPersistentCookiesPolicy(self, QWebEngineProfile_PersistentCookiesPolicy): # real signature unknown; restored from __doc__
        """ setPersistentCookiesPolicy(self, QWebEngineProfile.PersistentCookiesPolicy) """
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

    def settings(self): # real signature unknown; restored from __doc__
        """ settings(self) -> QWebEngineSettings """
        return QWebEngineSettings

    def spellCheckLanguages(self): # real signature unknown; restored from __doc__
        """ spellCheckLanguages(self) -> List[str] """
        return []

    def storageName(self): # real signature unknown; restored from __doc__
        """ storageName(self) -> str """
        return ""

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def urlSchemeHandler(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ urlSchemeHandler(self, Union[QByteArray, bytes, bytearray]) -> QWebEngineUrlSchemeHandler """
        pass

    def visitedLinksContainsUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ visitedLinksContainsUrl(self, QUrl) -> bool """
        return False

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AllowPersistentCookies = 1
    DiskHttpCache = 1
    ForcePersistentCookies = 2
    MemoryHttpCache = 0
    NoCache = 2
    NoPersistentCookies = 0


class QWebEngineScript(__sip.simplewrapper):
    """
    QWebEngineScript()
    QWebEngineScript(QWebEngineScript)
    """
    def injectionPoint(self): # real signature unknown; restored from __doc__
        """ injectionPoint(self) -> QWebEngineScript.InjectionPoint """
        pass

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def runsOnSubFrames(self): # real signature unknown; restored from __doc__
        """ runsOnSubFrames(self) -> bool """
        return False

    def setInjectionPoint(self, QWebEngineScript_InjectionPoint): # real signature unknown; restored from __doc__
        """ setInjectionPoint(self, QWebEngineScript.InjectionPoint) """
        pass

    def setName(self, p_str): # real signature unknown; restored from __doc__
        """ setName(self, str) """
        pass

    def setRunsOnSubFrames(self, bool): # real signature unknown; restored from __doc__
        """ setRunsOnSubFrames(self, bool) """
        pass

    def setSourceCode(self, p_str): # real signature unknown; restored from __doc__
        """ setSourceCode(self, str) """
        pass

    def setWorldId(self, p_int): # real signature unknown; restored from __doc__
        """ setWorldId(self, int) """
        pass

    def sourceCode(self): # real signature unknown; restored from __doc__
        """ sourceCode(self) -> str """
        return ""

    def swap(self, QWebEngineScript): # real signature unknown; restored from __doc__
        """ swap(self, QWebEngineScript) """
        pass

    def worldId(self): # real signature unknown; restored from __doc__
        """ worldId(self) -> int """
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

    def __init__(self, QWebEngineScript=None): # real signature unknown; restored from __doc__ with multiple overloads
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


    ApplicationWorld = 1
    Deferred = 0
    DocumentCreation = 2
    DocumentReady = 1
    MainWorld = 0
    UserWorld = 2
    __hash__ = None


class QWebEngineScriptCollection(__sip.simplewrapper):
    # no doc
    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def contains(self, QWebEngineScript): # real signature unknown; restored from __doc__
        """ contains(self, QWebEngineScript) -> bool """
        return False

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def findScript(self, p_str): # real signature unknown; restored from __doc__
        """ findScript(self, str) -> QWebEngineScript """
        return QWebEngineScript

    def findScripts(self, p_str): # real signature unknown; restored from __doc__
        """ findScripts(self, str) -> List[QWebEngineScript] """
        return []

    def insert(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        insert(self, QWebEngineScript)
        insert(self, Iterable[QWebEngineScript])
        """
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def remove(self, QWebEngineScript): # real signature unknown; restored from __doc__
        """ remove(self, QWebEngineScript) -> bool """
        return False

    def toList(self): # real signature unknown; restored from __doc__
        """ toList(self) -> List[QWebEngineScript] """
        return []

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QWebEngineSettings(__sip.simplewrapper):
    # no doc
    def defaultSettings(self): # real signature unknown; restored from __doc__
        """ defaultSettings() -> QWebEngineSettings """
        return QWebEngineSettings

    def defaultTextEncoding(self): # real signature unknown; restored from __doc__
        """ defaultTextEncoding(self) -> str """
        return ""

    def fontFamily(self, QWebEngineSettings_FontFamily): # real signature unknown; restored from __doc__
        """ fontFamily(self, QWebEngineSettings.FontFamily) -> str """
        return ""

    def fontSize(self, QWebEngineSettings_FontSize): # real signature unknown; restored from __doc__
        """ fontSize(self, QWebEngineSettings.FontSize) -> int """
        return 0

    def globalSettings(self): # real signature unknown; restored from __doc__
        """ globalSettings() -> QWebEngineSettings """
        return QWebEngineSettings

    def resetAttribute(self, QWebEngineSettings_WebAttribute): # real signature unknown; restored from __doc__
        """ resetAttribute(self, QWebEngineSettings.WebAttribute) """
        pass

    def resetFontFamily(self, QWebEngineSettings_FontFamily): # real signature unknown; restored from __doc__
        """ resetFontFamily(self, QWebEngineSettings.FontFamily) """
        pass

    def resetFontSize(self, QWebEngineSettings_FontSize): # real signature unknown; restored from __doc__
        """ resetFontSize(self, QWebEngineSettings.FontSize) """
        pass

    def resetUnknownUrlSchemePolicy(self): # real signature unknown; restored from __doc__
        """ resetUnknownUrlSchemePolicy(self) """
        pass

    def setAttribute(self, QWebEngineSettings_WebAttribute, bool): # real signature unknown; restored from __doc__
        """ setAttribute(self, QWebEngineSettings.WebAttribute, bool) """
        pass

    def setDefaultTextEncoding(self, p_str): # real signature unknown; restored from __doc__
        """ setDefaultTextEncoding(self, str) """
        pass

    def setFontFamily(self, QWebEngineSettings_FontFamily, p_str): # real signature unknown; restored from __doc__
        """ setFontFamily(self, QWebEngineSettings.FontFamily, str) """
        pass

    def setFontSize(self, QWebEngineSettings_FontSize, p_int): # real signature unknown; restored from __doc__
        """ setFontSize(self, QWebEngineSettings.FontSize, int) """
        pass

    def setUnknownUrlSchemePolicy(self, QWebEngineSettings_UnknownUrlSchemePolicy): # real signature unknown; restored from __doc__
        """ setUnknownUrlSchemePolicy(self, QWebEngineSettings.UnknownUrlSchemePolicy) """
        pass

    def testAttribute(self, QWebEngineSettings_WebAttribute): # real signature unknown; restored from __doc__
        """ testAttribute(self, QWebEngineSettings.WebAttribute) -> bool """
        return False

    def unknownUrlSchemePolicy(self): # real signature unknown; restored from __doc__
        """ unknownUrlSchemePolicy(self) -> QWebEngineSettings.UnknownUrlSchemePolicy """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Accelerated2dCanvasEnabled = 17
    AllowAllUnknownUrlSchemes = 3
    AllowGeolocationOnInsecureOrigins = 23
    AllowRunningInsecureContent = 22
    AllowUnknownUrlSchemesFromUserInteraction = 2
    AllowWindowActivationFromJavaScript = 24
    AutoLoadIconsForPage = 18
    AutoLoadImages = 0
    CursiveFont = 4
    DefaultFixedFontSize = 3
    DefaultFontSize = 2
    DisallowUnknownUrlSchemes = 1
    DnsPrefetchEnabled = 29
    ErrorPageEnabled = 12
    FantasyFont = 5
    FixedFont = 1
    FocusOnNavigationEnabled = 20
    FullScreenSupportEnabled = 14
    HyperlinkAuditingEnabled = 10
    JavascriptCanAccessClipboard = 3
    JavascriptCanOpenWindows = 2
    JavascriptCanPaste = 28
    JavascriptEnabled = 1
    LinksIncludedInFocusChain = 4
    LocalContentCanAccessFileUrls = 9
    LocalContentCanAccessRemoteUrls = 6
    LocalStorageEnabled = 5
    MinimumFontSize = 0
    MinimumLogicalFontSize = 1
    PictographFont = 6
    PlaybackRequiresUserGesture = 26
    PluginsEnabled = 13
    PrintElementBackgrounds = 21
    SansSerifFont = 3
    ScreenCaptureEnabled = 15
    ScrollAnimatorEnabled = 11
    SerifFont = 2
    ShowScrollBars = 25
    SpatialNavigationEnabled = 8
    StandardFont = 0
    TouchIconsEnabled = 19
    WebGLEnabled = 16
    WebRTCPublicInterfacesOnly = 27
    XSSAuditingEnabled = 7


class QWebEngineView(__PyQt5_QtWidgets.QWidget):
    """ QWebEngineView(parent: QWidget = None) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def back(self): # real signature unknown; restored from __doc__
        """ back(self) """
        pass

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, QContextMenuEvent): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, QContextMenuEvent) """
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def createWindow(self, QWebEnginePage_WebWindowType): # real signature unknown; restored from __doc__
        """ createWindow(self, QWebEnginePage.WebWindowType) -> QWebEngineView """
        return QWebEngineView

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dragEnterEvent(self, QDragEnterEvent): # real signature unknown; restored from __doc__
        """ dragEnterEvent(self, QDragEnterEvent) """
        pass

    def dragLeaveEvent(self, QDragLeaveEvent): # real signature unknown; restored from __doc__
        """ dragLeaveEvent(self, QDragLeaveEvent) """
        pass

    def dragMoveEvent(self, QDragMoveEvent): # real signature unknown; restored from __doc__
        """ dragMoveEvent(self, QDragMoveEvent) """
        pass

    def dropEvent(self, QDropEvent): # real signature unknown; restored from __doc__
        """ dropEvent(self, QDropEvent) """
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def findText(self, p_str, options, QWebEnginePage_FindFlags=None, QWebEnginePage_FindFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ findText(self, str, options: Union[QWebEnginePage.FindFlags, QWebEnginePage.FindFlag] = QWebEnginePage.FindFlags(), resultCallback: Callable[[bool], None] = 0) """
        pass

    def focusInEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def forward(self): # real signature unknown; restored from __doc__
        """ forward(self) """
        pass

    def hasSelection(self): # real signature unknown; restored from __doc__
        """ hasSelection(self) -> bool """
        return False

    def hideEvent(self, QHideEvent): # real signature unknown; restored from __doc__
        """ hideEvent(self, QHideEvent) """
        pass

    def history(self): # real signature unknown; restored from __doc__
        """ history(self) -> QWebEngineHistory """
        return QWebEngineHistory

    def icon(self): # real signature unknown; restored from __doc__
        """ icon(self) -> QIcon """
        pass

    def iconChanged(self, QIcon): # real signature unknown; restored from __doc__
        """ iconChanged(self, QIcon) [signal] """
        pass

    def iconUrl(self): # real signature unknown; restored from __doc__
        """ iconUrl(self) -> QUrl """
        pass

    def iconUrlChanged(self, QUrl): # real signature unknown; restored from __doc__
        """ iconUrlChanged(self, QUrl) [signal] """
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def load(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        load(self, QUrl)
        load(self, QWebEngineHttpRequest)
        """
        pass

    def loadFinished(self, bool): # real signature unknown; restored from __doc__
        """ loadFinished(self, bool) [signal] """
        pass

    def loadProgress(self, p_int): # real signature unknown; restored from __doc__
        """ loadProgress(self, int) [signal] """
        pass

    def loadStarted(self): # real signature unknown; restored from __doc__
        """ loadStarted(self) [signal] """
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def page(self): # real signature unknown; restored from __doc__
        """ page(self) -> QWebEnginePage """
        return QWebEnginePage

    def pageAction(self, QWebEnginePage_WebAction): # real signature unknown; restored from __doc__
        """ pageAction(self, QWebEnginePage.WebAction) -> QAction """
        pass

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def reload(self): # real signature unknown; restored from __doc__
        """ reload(self) """
        pass

    def renderProcessTerminated(self, QWebEnginePage_RenderProcessTerminationStatus, p_int): # real signature unknown; restored from __doc__
        """ renderProcessTerminated(self, QWebEnginePage.RenderProcessTerminationStatus, int) [signal] """
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def selectedText(self): # real signature unknown; restored from __doc__
        """ selectedText(self) -> str """
        return ""

    def selectionChanged(self): # real signature unknown; restored from __doc__
        """ selectionChanged(self) [signal] """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setContent(self, Union, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setContent(self, Union[QByteArray, bytes, bytearray], mimeType: str = '', baseUrl: QUrl = QUrl()) """
        pass

    def setHtml(self, p_str, baseUrl=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setHtml(self, str, baseUrl: QUrl = QUrl()) """
        pass

    def setPage(self, QWebEnginePage): # real signature unknown; restored from __doc__
        """ setPage(self, QWebEnginePage) """
        pass

    def settings(self): # real signature unknown; restored from __doc__
        """ settings(self) -> QWebEngineSettings """
        return QWebEngineSettings

    def setUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ setUrl(self, QUrl) """
        pass

    def setZoomFactor(self, p_float): # real signature unknown; restored from __doc__
        """ setZoomFactor(self, float) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, QShowEvent): # real signature unknown; restored from __doc__
        """ showEvent(self, QShowEvent) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def title(self): # real signature unknown; restored from __doc__
        """ title(self) -> str """
        return ""

    def titleChanged(self, p_str): # real signature unknown; restored from __doc__
        """ titleChanged(self, str) [signal] """
        pass

    def triggerPageAction(self, QWebEnginePage_WebAction, checked=False): # real signature unknown; restored from __doc__
        """ triggerPageAction(self, QWebEnginePage.WebAction, checked: bool = False) """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def url(self): # real signature unknown; restored from __doc__
        """ url(self) -> QUrl """
        pass

    def urlChanged(self, QUrl): # real signature unknown; restored from __doc__
        """ urlChanged(self, QUrl) [signal] """
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def zoomFactor(self): # real signature unknown; restored from __doc__
        """ zoomFactor(self) -> float """
        return 0.0

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


# variables with complex values



