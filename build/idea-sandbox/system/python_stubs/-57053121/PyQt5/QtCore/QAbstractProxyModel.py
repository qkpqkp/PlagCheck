# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QAbstractItemModel import QAbstractItemModel

class QAbstractProxyModel(QAbstractItemModel):
    """ QAbstractProxyModel(parent: QObject = None) """
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

    def canDropMimeData(self, QMimeData, Qt_DropAction, p_int, p_int_1, QModelIndex): # real signature unknown; restored from __doc__
        """ canDropMimeData(self, QMimeData, Qt.DropAction, int, int, QModelIndex) -> bool """
        return False

    def canFetchMore(self, QModelIndex): # real signature unknown; restored from __doc__
        """ canFetchMore(self, QModelIndex) -> bool """
        return False

    def changePersistentIndex(self, *args, **kwargs): # real signature unknown
        pass

    def changePersistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
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

    def flags(self, QModelIndex): # real signature unknown; restored from __doc__
        """ flags(self, QModelIndex) -> Qt.ItemFlags """
        pass

    def hasChildren(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ hasChildren(self, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def headerData(self, p_int, Qt_Orientation, role=None): # real signature unknown; restored from __doc__
        """ headerData(self, int, Qt.Orientation, role: int = Qt.DisplayRole) -> Any """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def itemData(self, QModelIndex): # real signature unknown; restored from __doc__
        """ itemData(self, QModelIndex) -> Dict[int, Any] """
        return {}

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

    def mimeData(self, Iterable, QModelIndex=None): # real signature unknown; restored from __doc__
        """ mimeData(self, Iterable[QModelIndex]) -> QMimeData """
        return QMimeData

    def mimeTypes(self): # real signature unknown; restored from __doc__
        """ mimeTypes(self) -> List[str] """
        return []

    def persistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resetInternalData(self): # real signature unknown; restored from __doc__
        """ resetInternalData(self) """
        pass

    def revert(self): # real signature unknown; restored from __doc__
        """ revert(self) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setData(self, QModelIndex, Any, role=None): # real signature unknown; restored from __doc__
        """ setData(self, QModelIndex, Any, role: int = Qt.EditRole) -> bool """
        return False

    def setHeaderData(self, p_int, Qt_Orientation, Any, role=None): # real signature unknown; restored from __doc__
        """ setHeaderData(self, int, Qt.Orientation, Any, role: int = Qt.EditRole) -> bool """
        return False

    def setItemData(self, QModelIndex, Dict, p_int=None, Any=None): # real signature unknown; restored from __doc__
        """ setItemData(self, QModelIndex, Dict[int, Any]) -> bool """
        return False

    def setSourceModel(self, QAbstractItemModel): # real signature unknown; restored from __doc__
        """ setSourceModel(self, QAbstractItemModel) """
        pass

    def sibling(self, p_int, p_int_1, QModelIndex): # real signature unknown; restored from __doc__
        """ sibling(self, int, int, QModelIndex) -> QModelIndex """
        return QModelIndex

    def sort(self, p_int, order=None): # real signature unknown; restored from __doc__
        """ sort(self, int, order: Qt.SortOrder = Qt.AscendingOrder) """
        pass

    def sourceModel(self): # real signature unknown; restored from __doc__
        """ sourceModel(self) -> QAbstractItemModel """
        return QAbstractItemModel

    def sourceModelChanged(self): # real signature unknown; restored from __doc__
        """ sourceModelChanged(self) [signal] """
        pass

    def span(self, QModelIndex): # real signature unknown; restored from __doc__
        """ span(self, QModelIndex) -> QSize """
        return QSize

    def submit(self): # real signature unknown; restored from __doc__
        """ submit(self) -> bool """
        return False

    def supportedDragActions(self): # real signature unknown; restored from __doc__
        """ supportedDragActions(self) -> Qt.DropActions """
        pass

    def supportedDropActions(self): # real signature unknown; restored from __doc__
        """ supportedDropActions(self) -> Qt.DropActions """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


