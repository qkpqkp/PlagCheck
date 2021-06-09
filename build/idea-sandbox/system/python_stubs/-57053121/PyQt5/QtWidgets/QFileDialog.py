# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QDialog import QDialog

class QFileDialog(QDialog):
    """
    QFileDialog(QWidget, Union[Qt.WindowFlags, Qt.WindowType])
    QFileDialog(parent: QWidget = None, caption: str = '', directory: str = '', filter: str = '')
    """
    def accept(self): # real signature unknown; restored from __doc__
        """ accept(self) """
        pass

    def acceptMode(self): # real signature unknown; restored from __doc__
        """ acceptMode(self) -> QFileDialog.AcceptMode """
        pass

    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ changeEvent(self, QEvent) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def currentChanged(self, p_str): # real signature unknown; restored from __doc__
        """ currentChanged(self, str) [signal] """
        pass

    def currentUrlChanged(self, QUrl): # real signature unknown; restored from __doc__
        """ currentUrlChanged(self, QUrl) [signal] """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultSuffix(self): # real signature unknown; restored from __doc__
        """ defaultSuffix(self) -> str """
        return ""

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def directory(self): # real signature unknown; restored from __doc__
        """ directory(self) -> QDir """
        pass

    def directoryEntered(self, p_str): # real signature unknown; restored from __doc__
        """ directoryEntered(self, str) [signal] """
        pass

    def directoryUrl(self): # real signature unknown; restored from __doc__
        """ directoryUrl(self) -> QUrl """
        pass

    def directoryUrlEntered(self, QUrl): # real signature unknown; restored from __doc__
        """ directoryUrlEntered(self, QUrl) [signal] """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def done(self, p_int): # real signature unknown; restored from __doc__
        """ done(self, int) """
        pass

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def eventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def fileMode(self): # real signature unknown; restored from __doc__
        """ fileMode(self) -> QFileDialog.FileMode """
        pass

    def fileSelected(self, p_str): # real signature unknown; restored from __doc__
        """ fileSelected(self, str) [signal] """
        pass

    def filesSelected(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ filesSelected(self, Iterable[str]) [signal] """
        pass

    def filter(self): # real signature unknown; restored from __doc__
        """ filter(self) -> QDir.Filters """
        pass

    def filterSelected(self, p_str): # real signature unknown; restored from __doc__
        """ filterSelected(self, str) [signal] """
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

    def getExistingDirectory(self, parent=None, caption='', directory='', options, QFileDialog_Options=None, QFileDialog_Option=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ getExistingDirectory(parent: QWidget = None, caption: str = '', directory: str = '', options: Union[QFileDialog.Options, QFileDialog.Option] = QFileDialog.ShowDirsOnly) -> str """
        pass

    def getExistingDirectoryUrl(self, parent=None, caption='', directory=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ getExistingDirectoryUrl(parent: QWidget = None, caption: str = '', directory: QUrl = QUrl(), options: Union[QFileDialog.Options, QFileDialog.Option] = QFileDialog.ShowDirsOnly, supportedSchemes: Iterable[str] = []) -> QUrl """
        pass

    def getOpenFileName(self, parent=None, caption='', directory='', filter='', initialFilter='', options, QFileDialog_Options=None, QFileDialog_Option=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ getOpenFileName(parent: QWidget = None, caption: str = '', directory: str = '', filter: str = '', initialFilter: str = '', options: Union[QFileDialog.Options, QFileDialog.Option] = 0) -> Tuple[str, str] """
        pass

    def getOpenFileNames(self, parent=None, caption='', directory='', filter='', initialFilter='', options, QFileDialog_Options=None, QFileDialog_Option=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ getOpenFileNames(parent: QWidget = None, caption: str = '', directory: str = '', filter: str = '', initialFilter: str = '', options: Union[QFileDialog.Options, QFileDialog.Option] = 0) -> Tuple[List[str], str] """
        pass

    def getOpenFileUrl(self, parent=None, caption='', directory='', filter='', initialFilter='', options, QFileDialog_Options=None, QFileDialog_Option=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ getOpenFileUrl(parent: QWidget = None, caption: str = '', directory: str = '', filter: str = '', initialFilter: str = '', options: Union[QFileDialog.Options, QFileDialog.Option] = 0, supportedSchemes: Iterable[str] = []) -> Tuple[QUrl, str] """
        pass

    def getOpenFileUrls(self, parent=None, caption='', directory='', filter='', initialFilter='', options, QFileDialog_Options=None, QFileDialog_Option=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ getOpenFileUrls(parent: QWidget = None, caption: str = '', directory: str = '', filter: str = '', initialFilter: str = '', options: Union[QFileDialog.Options, QFileDialog.Option] = 0, supportedSchemes: Iterable[str] = []) -> Tuple[List[QUrl], str] """
        pass

    def getSaveFileName(self, parent=None, caption='', directory='', filter='', initialFilter='', options, QFileDialog_Options=None, QFileDialog_Option=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ getSaveFileName(parent: QWidget = None, caption: str = '', directory: str = '', filter: str = '', initialFilter: str = '', options: Union[QFileDialog.Options, QFileDialog.Option] = 0) -> Tuple[str, str] """
        pass

    def getSaveFileUrl(self, parent=None, caption='', directory='', filter='', initialFilter='', options, QFileDialog_Options=None, QFileDialog_Option=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ getSaveFileUrl(parent: QWidget = None, caption: str = '', directory: str = '', filter: str = '', initialFilter: str = '', options: Union[QFileDialog.Options, QFileDialog.Option] = 0, supportedSchemes: Iterable[str] = []) -> Tuple[QUrl, str] """
        pass

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def history(self): # real signature unknown; restored from __doc__
        """ history(self) -> List[str] """
        return []

    def iconProvider(self): # real signature unknown; restored from __doc__
        """ iconProvider(self) -> QFileIconProvider """
        return QFileIconProvider

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def itemDelegate(self): # real signature unknown; restored from __doc__
        """ itemDelegate(self) -> QAbstractItemDelegate """
        return QAbstractItemDelegate

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def labelText(self, QFileDialog_DialogLabel): # real signature unknown; restored from __doc__
        """ labelText(self, QFileDialog.DialogLabel) -> str """
        return ""

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def mimeTypeFilters(self): # real signature unknown; restored from __doc__
        """ mimeTypeFilters(self) -> List[str] """
        return []

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

    def nameFilters(self): # real signature unknown; restored from __doc__
        """ nameFilters(self) -> List[str] """
        return []

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def open(self, PYQT_SLOT=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        open(self)
        open(self, PYQT_SLOT)
        """
        pass

    def options(self): # real signature unknown; restored from __doc__
        """ options(self) -> QFileDialog.Options """
        pass

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def proxyModel(self): # real signature unknown; restored from __doc__
        """ proxyModel(self) -> QAbstractProxyModel """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def restoreState(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ restoreState(self, Union[QByteArray, bytes, bytearray]) -> bool """
        return False

    def saveState(self): # real signature unknown; restored from __doc__
        """ saveState(self) -> QByteArray """
        pass

    def selectedFiles(self): # real signature unknown; restored from __doc__
        """ selectedFiles(self) -> List[str] """
        return []

    def selectedMimeTypeFilter(self): # real signature unknown; restored from __doc__
        """ selectedMimeTypeFilter(self) -> str """
        return ""

    def selectedNameFilter(self): # real signature unknown; restored from __doc__
        """ selectedNameFilter(self) -> str """
        return ""

    def selectedUrls(self): # real signature unknown; restored from __doc__
        """ selectedUrls(self) -> List[QUrl] """
        return []

    def selectFile(self, p_str): # real signature unknown; restored from __doc__
        """ selectFile(self, str) """
        pass

    def selectMimeTypeFilter(self, p_str): # real signature unknown; restored from __doc__
        """ selectMimeTypeFilter(self, str) """
        pass

    def selectNameFilter(self, p_str): # real signature unknown; restored from __doc__
        """ selectNameFilter(self, str) """
        pass

    def selectUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ selectUrl(self, QUrl) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAcceptMode(self, QFileDialog_AcceptMode): # real signature unknown; restored from __doc__
        """ setAcceptMode(self, QFileDialog.AcceptMode) """
        pass

    def setDefaultSuffix(self, p_str): # real signature unknown; restored from __doc__
        """ setDefaultSuffix(self, str) """
        pass

    def setDirectory(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setDirectory(self, str)
        setDirectory(self, QDir)
        """
        pass

    def setDirectoryUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ setDirectoryUrl(self, QUrl) """
        pass

    def setFileMode(self, QFileDialog_FileMode): # real signature unknown; restored from __doc__
        """ setFileMode(self, QFileDialog.FileMode) """
        pass

    def setFilter(self, Union, QDir_Filters=None, QDir_Filter=None): # real signature unknown; restored from __doc__
        """ setFilter(self, Union[QDir.Filters, QDir.Filter]) """
        pass

    def setHistory(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ setHistory(self, Iterable[str]) """
        pass

    def setIconProvider(self, QFileIconProvider): # real signature unknown; restored from __doc__
        """ setIconProvider(self, QFileIconProvider) """
        pass

    def setItemDelegate(self, QAbstractItemDelegate): # real signature unknown; restored from __doc__
        """ setItemDelegate(self, QAbstractItemDelegate) """
        pass

    def setLabelText(self, QFileDialog_DialogLabel, p_str): # real signature unknown; restored from __doc__
        """ setLabelText(self, QFileDialog.DialogLabel, str) """
        pass

    def setMimeTypeFilters(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ setMimeTypeFilters(self, Iterable[str]) """
        pass

    def setNameFilter(self, p_str): # real signature unknown; restored from __doc__
        """ setNameFilter(self, str) """
        pass

    def setNameFilters(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ setNameFilters(self, Iterable[str]) """
        pass

    def setOption(self, QFileDialog_Option, on=True): # real signature unknown; restored from __doc__
        """ setOption(self, QFileDialog.Option, on: bool = True) """
        pass

    def setOptions(self, Union, QFileDialog_Options=None, QFileDialog_Option=None): # real signature unknown; restored from __doc__
        """ setOptions(self, Union[QFileDialog.Options, QFileDialog.Option]) """
        pass

    def setProxyModel(self, QAbstractProxyModel): # real signature unknown; restored from __doc__
        """ setProxyModel(self, QAbstractProxyModel) """
        pass

    def setSidebarUrls(self, Iterable, QUrl=None): # real signature unknown; restored from __doc__
        """ setSidebarUrls(self, Iterable[QUrl]) """
        pass

    def setSupportedSchemes(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ setSupportedSchemes(self, Iterable[str]) """
        pass

    def setViewMode(self, QFileDialog_ViewMode): # real signature unknown; restored from __doc__
        """ setViewMode(self, QFileDialog.ViewMode) """
        pass

    def setVisible(self, bool): # real signature unknown; restored from __doc__
        """ setVisible(self, bool) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sidebarUrls(self): # real signature unknown; restored from __doc__
        """ sidebarUrls(self) -> List[QUrl] """
        return []

    def supportedSchemes(self): # real signature unknown; restored from __doc__
        """ supportedSchemes(self) -> List[str] """
        return []

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def testOption(self, QFileDialog_Option): # real signature unknown; restored from __doc__
        """ testOption(self, QFileDialog.Option) -> bool """
        return False

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def urlSelected(self, QUrl): # real signature unknown; restored from __doc__
        """ urlSelected(self, QUrl) [signal] """
        pass

    def urlsSelected(self, Iterable, QUrl=None): # real signature unknown; restored from __doc__
        """ urlsSelected(self, Iterable[QUrl]) [signal] """
        pass

    def viewMode(self): # real signature unknown; restored from __doc__
        """ viewMode(self) -> QFileDialog.ViewMode """
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    Accept = 3
    AcceptOpen = 0
    AcceptSave = 1
    AnyFile = 0
    Detail = 0
    Directory = 2
    DirectoryOnly = 4
    DontConfirmOverwrite = 4
    DontResolveSymlinks = 2
    DontUseCustomDirectoryIcons = 128
    DontUseNativeDialog = 16
    DontUseSheet = 8
    ExistingFile = 1
    ExistingFiles = 3
    FileName = 1
    FileType = 2
    HideNameFilterDetails = 64
    List = 1
    LookIn = 0
    ReadOnly = 32
    Reject = 4
    ShowDirsOnly = 1


