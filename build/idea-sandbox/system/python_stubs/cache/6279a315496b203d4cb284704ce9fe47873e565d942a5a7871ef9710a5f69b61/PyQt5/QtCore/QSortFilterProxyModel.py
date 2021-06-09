# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QAbstractProxyModel import QAbstractProxyModel

class QSortFilterProxyModel(QAbstractProxyModel):
    """ QSortFilterProxyModel(parent: QObject = None) """
    def beginInsertColumns(self, *args, **kwargs): # real signature unknown
        pass

    def beginInsertRows(self, *args, **kwargs): # real signature unknown
        pass

    def beginMoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def beginMoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def beginRemoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def beginRemoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def beginResetModel(self, *args, **kwargs): # real signature unknown
        pass

    def buddy(self, QModelIndex): # real signature unknown; restored from __doc__
        """ buddy(self, QModelIndex) -> QModelIndex """
        return QModelIndex

    def canFetchMore(self, QModelIndex): # real signature unknown; restored from __doc__
        """ canFetchMore(self, QModelIndex) -> bool """
        return False

    def changePersistentIndex(self, *args, **kwargs): # real signature unknown
        pass

    def changePersistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def columnCount(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ columnCount(self, parent: QModelIndex = QModelIndex()) -> int """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createIndex(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def data(self, QModelIndex, role=None): # real signature unknown; restored from __doc__
        """ data(self, QModelIndex, role: int = Qt.DisplayRole) -> Any """
        pass

    def decodeData(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dropMimeData(self, QMimeData, Qt_DropAction, p_int, p_int_1, QModelIndex): # real signature unknown; restored from __doc__
        """ dropMimeData(self, QMimeData, Qt.DropAction, int, int, QModelIndex) -> bool """
        return False

    def dynamicSortFilter(self): # real signature unknown; restored from __doc__
        """ dynamicSortFilter(self) -> bool """
        return False

    def encodeData(self, *args, **kwargs): # real signature unknown
        pass

    def endInsertColumns(self, *args, **kwargs): # real signature unknown
        pass

    def endInsertRows(self, *args, **kwargs): # real signature unknown
        pass

    def endMoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def endMoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def endRemoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def endRemoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def endResetModel(self, *args, **kwargs): # real signature unknown
        pass

    def fetchMore(self, QModelIndex): # real signature unknown; restored from __doc__
        """ fetchMore(self, QModelIndex) """
        pass

    def filterAcceptsColumn(self, p_int, QModelIndex): # real signature unknown; restored from __doc__
        """ filterAcceptsColumn(self, int, QModelIndex) -> bool """
        return False

    def filterAcceptsRow(self, p_int, QModelIndex): # real signature unknown; restored from __doc__
        """ filterAcceptsRow(self, int, QModelIndex) -> bool """
        return False

    def filterCaseSensitivity(self): # real signature unknown; restored from __doc__
        """ filterCaseSensitivity(self) -> Qt.CaseSensitivity """
        pass

    def filterKeyColumn(self): # real signature unknown; restored from __doc__
        """ filterKeyColumn(self) -> int """
        return 0

    def filterRegExp(self): # real signature unknown; restored from __doc__
        """ filterRegExp(self) -> QRegExp """
        return QRegExp

    def filterRegularExpression(self): # real signature unknown; restored from __doc__
        """ filterRegularExpression(self) -> QRegularExpression """
        return QRegularExpression

    def filterRole(self): # real signature unknown; restored from __doc__
        """ filterRole(self) -> int """
        return 0

    def flags(self, QModelIndex): # real signature unknown; restored from __doc__
        """ flags(self, QModelIndex) -> Qt.ItemFlags """
        pass

    def hasChildren(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ hasChildren(self, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def headerData(self, p_int, Qt_Orientation, role=None): # real signature unknown; restored from __doc__
        """ headerData(self, int, Qt.Orientation, role: int = Qt.DisplayRole) -> Any """
        pass

    def index(self, p_int, p_int_1, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ index(self, int, int, parent: QModelIndex = QModelIndex()) -> QModelIndex """
        pass

    def insertColumns(self, p_int, p_int_1, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ insertColumns(self, int, int, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def insertRows(self, p_int, p_int_1, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ insertRows(self, int, int, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def invalidate(self): # real signature unknown; restored from __doc__
        """ invalidate(self) """
        pass

    def invalidateFilter(self): # real signature unknown; restored from __doc__
        """ invalidateFilter(self) """
        pass

    def isRecursiveFilteringEnabled(self): # real signature unknown; restored from __doc__
        """ isRecursiveFilteringEnabled(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isSortLocaleAware(self): # real signature unknown; restored from __doc__
        """ isSortLocaleAware(self) -> bool """
        return False

    def lessThan(self, QModelIndex, QModelIndex_1): # real signature unknown; restored from __doc__
        """ lessThan(self, QModelIndex, QModelIndex) -> bool """
        return False

    def mapFromSource(self, QModelIndex): # real signature unknown; restored from __doc__
        """ mapFromSource(self, QModelIndex) -> QModelIndex """
        return QModelIndex

    def mapSelectionFromSource(self, QItemSelection): # real signature unknown; restored from __doc__
        """ mapSelectionFromSource(self, QItemSelection) -> QItemSelection """
        return QItemSelection

    def mapSelectionToSource(self, QItemSelection): # real signature unknown; restored from __doc__
        """ mapSelectionToSource(self, QItemSelection) -> QItemSelection """
        return QItemSelection

    def mapToSource(self, QModelIndex): # real signature unknown; restored from __doc__
        """ mapToSource(self, QModelIndex) -> QModelIndex """
        return QModelIndex

    def match(self, QModelIndex, p_int, Any, hits=1, flags, Qt_MatchFlags=None, Qt_MatchFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ match(self, QModelIndex, int, Any, hits: int = 1, flags: Union[Qt.MatchFlags, Qt.MatchFlag] = Qt.MatchStartsWith|Qt.MatchWrap) -> List[QModelIndex] """
        pass

    def mimeData(self, Iterable, QModelIndex=None): # real signature unknown; restored from __doc__
        """ mimeData(self, Iterable[QModelIndex]) -> QMimeData """
        return QMimeData

    def mimeTypes(self): # real signature unknown; restored from __doc__
        """ mimeTypes(self) -> List[str] """
        return []

    def parent(self, QModelIndex=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        parent(self, QModelIndex) -> QModelIndex
        parent(self) -> QObject
        """
        return QModelIndex or QObject

    def persistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeColumns(self, p_int, p_int_1, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ removeColumns(self, int, int, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def removeRows(self, p_int, p_int_1, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ removeRows(self, int, int, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def resetInternalData(self, *args, **kwargs): # real signature unknown
        pass

    def rowCount(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ rowCount(self, parent: QModelIndex = QModelIndex()) -> int """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setData(self, QModelIndex, Any, role=None): # real signature unknown; restored from __doc__
        """ setData(self, QModelIndex, Any, role: int = Qt.EditRole) -> bool """
        return False

    def setDynamicSortFilter(self, bool): # real signature unknown; restored from __doc__
        """ setDynamicSortFilter(self, bool) """
        pass

    def setFilterCaseSensitivity(self, Qt_CaseSensitivity): # real signature unknown; restored from __doc__
        """ setFilterCaseSensitivity(self, Qt.CaseSensitivity) """
        pass

    def setFilterFixedString(self, p_str): # real signature unknown; restored from __doc__
        """ setFilterFixedString(self, str) """
        pass

    def setFilterKeyColumn(self, p_int): # real signature unknown; restored from __doc__
        """ setFilterKeyColumn(self, int) """
        pass

    def setFilterRegExp(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setFilterRegExp(self, QRegExp)
        setFilterRegExp(self, str)
        """
        pass

    def setFilterRegularExpression(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setFilterRegularExpression(self, QRegularExpression)
        setFilterRegularExpression(self, str)
        """
        pass

    def setFilterRole(self, p_int): # real signature unknown; restored from __doc__
        """ setFilterRole(self, int) """
        pass

    def setFilterWildcard(self, p_str): # real signature unknown; restored from __doc__
        """ setFilterWildcard(self, str) """
        pass

    def setHeaderData(self, p_int, Qt_Orientation, Any, role=None): # real signature unknown; restored from __doc__
        """ setHeaderData(self, int, Qt.Orientation, Any, role: int = Qt.EditRole) -> bool """
        return False

    def setRecursiveFilteringEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setRecursiveFilteringEnabled(self, bool) """
        pass

    def setSortCaseSensitivity(self, Qt_CaseSensitivity): # real signature unknown; restored from __doc__
        """ setSortCaseSensitivity(self, Qt.CaseSensitivity) """
        pass

    def setSortLocaleAware(self, bool): # real signature unknown; restored from __doc__
        """ setSortLocaleAware(self, bool) """
        pass

    def setSortRole(self, p_int): # real signature unknown; restored from __doc__
        """ setSortRole(self, int) """
        pass

    def setSourceModel(self, QAbstractItemModel): # real signature unknown; restored from __doc__
        """ setSourceModel(self, QAbstractItemModel) """
        pass

    def sibling(self, p_int, p_int_1, QModelIndex): # real signature unknown; restored from __doc__
        """ sibling(self, int, int, QModelIndex) -> QModelIndex """
        return QModelIndex

    def sort(self, p_int, order=None): # real signature unknown; restored from __doc__
        """ sort(self, int, order: Qt.SortOrder = Qt.AscendingOrder) """
        pass

    def sortCaseSensitivity(self): # real signature unknown; restored from __doc__
        """ sortCaseSensitivity(self) -> Qt.CaseSensitivity """
        pass

    def sortColumn(self): # real signature unknown; restored from __doc__
        """ sortColumn(self) -> int """
        return 0

    def sortOrder(self): # real signature unknown; restored from __doc__
        """ sortOrder(self) -> Qt.SortOrder """
        pass

    def sortRole(self): # real signature unknown; restored from __doc__
        """ sortRole(self) -> int """
        return 0

    def span(self, QModelIndex): # real signature unknown; restored from __doc__
        """ span(self, QModelIndex) -> QSize """
        return QSize

    def supportedDropActions(self): # real signature unknown; restored from __doc__
        """ supportedDropActions(self) -> Qt.DropActions """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


