# encoding: utf-8
# module PyQt5.QtHelp
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtHelp.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtWidgets as __PyQt5_QtWidgets
import sip as __sip


# no functions
# classes

class QHelpContentItem(__sip.simplewrapper):
    # no doc
    def child(self, p_int): # real signature unknown; restored from __doc__
        """ child(self, int) -> QHelpContentItem """
        return QHelpContentItem

    def childCount(self): # real signature unknown; restored from __doc__
        """ childCount(self) -> int """
        return 0

    def childPosition(self, QHelpContentItem): # real signature unknown; restored from __doc__
        """ childPosition(self, QHelpContentItem) -> int """
        return 0

    def parent(self): # real signature unknown; restored from __doc__
        """ parent(self) -> QHelpContentItem """
        return QHelpContentItem

    def row(self): # real signature unknown; restored from __doc__
        """ row(self) -> int """
        return 0

    def title(self): # real signature unknown; restored from __doc__
        """ title(self) -> str """
        return ""

    def url(self): # real signature unknown; restored from __doc__
        """ url(self) -> QUrl """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QHelpContentModel(__PyQt5_QtCore.QAbstractItemModel):
    # no doc
    def columnCount(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ columnCount(self, parent: QModelIndex = QModelIndex()) -> int """
        pass

    def contentItemAt(self, QModelIndex): # real signature unknown; restored from __doc__
        """ contentItemAt(self, QModelIndex) -> QHelpContentItem """
        return QHelpContentItem

    def contentsCreated(self): # real signature unknown; restored from __doc__
        """ contentsCreated(self) [signal] """
        pass

    def contentsCreationStarted(self): # real signature unknown; restored from __doc__
        """ contentsCreationStarted(self) [signal] """
        pass

    def createContents(self, p_str): # real signature unknown; restored from __doc__
        """ createContents(self, str) """
        pass

    def data(self, QModelIndex, p_int): # real signature unknown; restored from __doc__
        """ data(self, QModelIndex, int) -> Any """
        pass

    def index(self, p_int, p_int_1, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ index(self, int, int, parent: QModelIndex = QModelIndex()) -> QModelIndex """
        pass

    def isCreatingContents(self): # real signature unknown; restored from __doc__
        """ isCreatingContents(self) -> bool """
        return False

    def parent(self, QModelIndex): # real signature unknown; restored from __doc__
        """ parent(self, QModelIndex) -> QModelIndex """
        pass

    def rowCount(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ rowCount(self, parent: QModelIndex = QModelIndex()) -> int """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QHelpContentWidget(__PyQt5_QtWidgets.QTreeView):
    # no doc
    def indexOf(self, QUrl): # real signature unknown; restored from __doc__
        """ indexOf(self, QUrl) -> QModelIndex """
        pass

    def linkActivated(self, QUrl): # real signature unknown; restored from __doc__
        """ linkActivated(self, QUrl) [signal] """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QHelpEngineCore(__PyQt5_QtCore.QObject):
    """ QHelpEngineCore(str, parent: QObject = None) """
    def addCustomFilter(self, p_str, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ addCustomFilter(self, str, Iterable[str]) -> bool """
        return False

    def autoSaveFilter(self): # real signature unknown; restored from __doc__
        """ autoSaveFilter(self) -> bool """
        return False

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def collectionFile(self): # real signature unknown; restored from __doc__
        """ collectionFile(self) -> str """
        return ""

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def copyCollectionFile(self, p_str): # real signature unknown; restored from __doc__
        """ copyCollectionFile(self, str) -> bool """
        return False

    def currentFilter(self): # real signature unknown; restored from __doc__
        """ currentFilter(self) -> str """
        return ""

    def currentFilterChanged(self, p_str): # real signature unknown; restored from __doc__
        """ currentFilterChanged(self, str) [signal] """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def customFilters(self): # real signature unknown; restored from __doc__
        """ customFilters(self) -> List[str] """
        return []

    def customValue(self, p_str, defaultValue=None): # real signature unknown; restored from __doc__
        """ customValue(self, str, defaultValue: Any = None) -> Any """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def documentationFileName(self, p_str): # real signature unknown; restored from __doc__
        """ documentationFileName(self, str) -> str """
        return ""

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> str """
        return ""

    def fileData(self, QUrl): # real signature unknown; restored from __doc__
        """ fileData(self, QUrl) -> QByteArray """
        pass

    def files(self, p_str, Iterable, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ files(self, str, Iterable[str], extensionFilter: str = '') -> List[QUrl] """
        pass

    def filterAttributes(self, p_str=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        filterAttributes(self) -> List[str]
        filterAttributes(self, str) -> List[str]
        """
        return []

    def filterAttributeSets(self, p_str): # real signature unknown; restored from __doc__
        """ filterAttributeSets(self, str) -> List[List[str]] """
        return []

    def findFile(self, QUrl): # real signature unknown; restored from __doc__
        """ findFile(self, QUrl) -> QUrl """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def linksForIdentifier(self, p_str): # real signature unknown; restored from __doc__
        """ linksForIdentifier(self, str) -> Dict[str, QUrl] """
        return {}

    def linksForKeyword(self, p_str): # real signature unknown; restored from __doc__
        """ linksForKeyword(self, str) -> Dict[str, QUrl] """
        return {}

    def metaData(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ metaData(str, str) -> Any """
        pass

    def namespaceName(self, p_str): # real signature unknown; restored from __doc__
        """ namespaceName(str) -> str """
        return ""

    def readersAboutToBeInvalidated(self): # real signature unknown; restored from __doc__
        """ readersAboutToBeInvalidated(self) [signal] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def registerDocumentation(self, p_str): # real signature unknown; restored from __doc__
        """ registerDocumentation(self, str) -> bool """
        return False

    def registeredDocumentations(self): # real signature unknown; restored from __doc__
        """ registeredDocumentations(self) -> List[str] """
        return []

    def removeCustomFilter(self, p_str): # real signature unknown; restored from __doc__
        """ removeCustomFilter(self, str) -> bool """
        return False

    def removeCustomValue(self, p_str): # real signature unknown; restored from __doc__
        """ removeCustomValue(self, str) -> bool """
        return False

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAutoSaveFilter(self, bool): # real signature unknown; restored from __doc__
        """ setAutoSaveFilter(self, bool) """
        pass

    def setCollectionFile(self, p_str): # real signature unknown; restored from __doc__
        """ setCollectionFile(self, str) """
        pass

    def setCurrentFilter(self, p_str): # real signature unknown; restored from __doc__
        """ setCurrentFilter(self, str) """
        pass

    def setCustomValue(self, p_str, Any): # real signature unknown; restored from __doc__
        """ setCustomValue(self, str, Any) -> bool """
        return False

    def setupData(self): # real signature unknown; restored from __doc__
        """ setupData(self) -> bool """
        return False

    def setupFinished(self): # real signature unknown; restored from __doc__
        """ setupFinished(self) [signal] """
        pass

    def setupStarted(self): # real signature unknown; restored from __doc__
        """ setupStarted(self) [signal] """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def unregisterDocumentation(self, p_str): # real signature unknown; restored from __doc__
        """ unregisterDocumentation(self, str) -> bool """
        return False

    def warning(self, p_str): # real signature unknown; restored from __doc__
        """ warning(self, str) [signal] """
        pass

    def __init__(self, p_str, parent=None): # real signature unknown; restored from __doc__
        pass


class QHelpEngine(QHelpEngineCore):
    """ QHelpEngine(str, parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contentModel(self): # real signature unknown; restored from __doc__
        """ contentModel(self) -> QHelpContentModel """
        return QHelpContentModel

    def contentWidget(self): # real signature unknown; restored from __doc__
        """ contentWidget(self) -> QHelpContentWidget """
        return QHelpContentWidget

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def indexModel(self): # real signature unknown; restored from __doc__
        """ indexModel(self) -> QHelpIndexModel """
        return QHelpIndexModel

    def indexWidget(self): # real signature unknown; restored from __doc__
        """ indexWidget(self) -> QHelpIndexWidget """
        return QHelpIndexWidget

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def searchEngine(self): # real signature unknown; restored from __doc__
        """ searchEngine(self) -> QHelpSearchEngine """
        return QHelpSearchEngine

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, p_str, parent=None): # real signature unknown; restored from __doc__
        pass


class QHelpIndexModel(__PyQt5_QtCore.QStringListModel):
    # no doc
    def createIndex(self, p_str): # real signature unknown; restored from __doc__
        """ createIndex(self, str) """
        pass

    def filter(self, p_str, wildcard=''): # real signature unknown; restored from __doc__
        """ filter(self, str, wildcard: str = '') -> QModelIndex """
        pass

    def indexCreated(self): # real signature unknown; restored from __doc__
        """ indexCreated(self) [signal] """
        pass

    def indexCreationStarted(self): # real signature unknown; restored from __doc__
        """ indexCreationStarted(self) [signal] """
        pass

    def isCreatingIndex(self): # real signature unknown; restored from __doc__
        """ isCreatingIndex(self) -> bool """
        return False

    def linksForKeyword(self, p_str): # real signature unknown; restored from __doc__
        """ linksForKeyword(self, str) -> Dict[str, QUrl] """
        return {}

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QHelpIndexWidget(__PyQt5_QtWidgets.QListView):
    # no doc
    def activateCurrentItem(self): # real signature unknown; restored from __doc__
        """ activateCurrentItem(self) """
        pass

    def filterIndices(self, p_str, wildcard=''): # real signature unknown; restored from __doc__
        """ filterIndices(self, str, wildcard: str = '') """
        pass

    def linkActivated(self, QUrl, p_str): # real signature unknown; restored from __doc__
        """ linkActivated(self, QUrl, str) [signal] """
        pass

    def linksActivated(self, Dict, p_str=None, QUrl=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ linksActivated(self, Dict[str, QUrl], str) [signal] """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QHelpSearchEngine(__PyQt5_QtCore.QObject):
    """ QHelpSearchEngine(QHelpEngineCore, parent: QObject = None) """
    def cancelIndexing(self): # real signature unknown; restored from __doc__
        """ cancelIndexing(self) """
        pass

    def cancelSearching(self): # real signature unknown; restored from __doc__
        """ cancelSearching(self) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def hitCount(self): # real signature unknown; restored from __doc__
        """ hitCount(self) -> int """
        return 0

    def hits(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ hits(self, int, int) -> List[Tuple[str, str]] """
        return []

    def indexingFinished(self): # real signature unknown; restored from __doc__
        """ indexingFinished(self) [signal] """
        pass

    def indexingStarted(self): # real signature unknown; restored from __doc__
        """ indexingStarted(self) [signal] """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def query(self): # real signature unknown; restored from __doc__
        """ query(self) -> List[QHelpSearchQuery] """
        return []

    def queryWidget(self): # real signature unknown; restored from __doc__
        """ queryWidget(self) -> QHelpSearchQueryWidget """
        return QHelpSearchQueryWidget

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def reindexDocumentation(self): # real signature unknown; restored from __doc__
        """ reindexDocumentation(self) """
        pass

    def resultWidget(self): # real signature unknown; restored from __doc__
        """ resultWidget(self) -> QHelpSearchResultWidget """
        return QHelpSearchResultWidget

    def search(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        search(self, Iterable[QHelpSearchQuery])
        search(self, str)
        """
        pass

    def searchingFinished(self, p_int): # real signature unknown; restored from __doc__
        """ searchingFinished(self, int) [signal] """
        pass

    def searchingStarted(self): # real signature unknown; restored from __doc__
        """ searchingStarted(self) [signal] """
        pass

    def searchInput(self): # real signature unknown; restored from __doc__
        """ searchInput(self) -> str """
        return ""

    def searchResultCount(self): # real signature unknown; restored from __doc__
        """ searchResultCount(self) -> int """
        return 0

    def searchResults(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ searchResults(self, int, int) -> List[QHelpSearchResult] """
        return []

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, QHelpEngineCore, parent=None): # real signature unknown; restored from __doc__
        pass


class QHelpSearchQuery(__sip.simplewrapper):
    """
    QHelpSearchQuery()
    QHelpSearchQuery(QHelpSearchQuery.FieldName, Iterable[str])
    QHelpSearchQuery(QHelpSearchQuery)
    """
    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    ALL = 4
    ATLEAST = 5
    DEFAULT = 0
    FUZZY = 1
    PHRASE = 3
    WITHOUT = 2


class QHelpSearchQueryWidget(__PyQt5_QtWidgets.QWidget):
    """ QHelpSearchQueryWidget(parent: QWidget = None) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def collapseExtendedSearch(self): # real signature unknown; restored from __doc__
        """ collapseExtendedSearch(self) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
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

    def expandExtendedSearch(self): # real signature unknown; restored from __doc__
        """ expandExtendedSearch(self) """
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

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isCompactMode(self): # real signature unknown; restored from __doc__
        """ isCompactMode(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
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

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def query(self): # real signature unknown; restored from __doc__
        """ query(self) -> List[QHelpSearchQuery] """
        return []

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def search(self): # real signature unknown; restored from __doc__
        """ search(self) [signal] """
        pass

    def searchInput(self): # real signature unknown; restored from __doc__
        """ searchInput(self) -> str """
        return ""

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCompactMode(self, bool): # real signature unknown; restored from __doc__
        """ setCompactMode(self, bool) """
        pass

    def setQuery(self, Iterable, QHelpSearchQuery=None): # real signature unknown; restored from __doc__
        """ setQuery(self, Iterable[QHelpSearchQuery]) """
        pass

    def setSearchInput(self, p_str): # real signature unknown; restored from __doc__
        """ setSearchInput(self, str) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


class QHelpSearchResult(__sip.simplewrapper):
    """
    QHelpSearchResult()
    QHelpSearchResult(QHelpSearchResult)
    QHelpSearchResult(QUrl, str, str)
    """
    def snippet(self): # real signature unknown; restored from __doc__
        """ snippet(self) -> str """
        return ""

    def title(self): # real signature unknown; restored from __doc__
        """ title(self) -> str """
        return ""

    def url(self): # real signature unknown; restored from __doc__
        """ url(self) -> QUrl """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QHelpSearchResultWidget(__PyQt5_QtWidgets.QWidget):
    # no doc
    def linkAt(self, QPoint): # real signature unknown; restored from __doc__
        """ linkAt(self, QPoint) -> QUrl """
        pass

    def requestShowLink(self, QUrl): # real signature unknown; restored from __doc__
        """ requestShowLink(self, QUrl) [signal] """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


# variables with complex values



