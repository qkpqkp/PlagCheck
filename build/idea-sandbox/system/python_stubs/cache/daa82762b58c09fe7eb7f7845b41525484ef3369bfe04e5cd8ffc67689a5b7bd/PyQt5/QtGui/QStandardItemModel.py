# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QStandardItemModel(__PyQt5_QtCore.QAbstractItemModel):
    """
    QStandardItemModel(parent: QObject = None)
    QStandardItemModel(int, int, parent: QObject = None)
    """
    def appendColumn(self, Iterable, QStandardItem=None): # real signature unknown; restored from __doc__
        """ appendColumn(self, Iterable[QStandardItem]) """
        pass

    def appendRow(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        appendRow(self, Iterable[QStandardItem])
        appendRow(self, QStandardItem)
        """
        pass

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

    def changePersistentIndex(self, *args, **kwargs): # real signature unknown
        pass

    def changePersistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def clearItemData(self, QModelIndex): # real signature unknown; restored from __doc__
        """ clearItemData(self, QModelIndex) -> bool """
        return False

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

    def findItems(self, p_str, flags, Qt_MatchFlags=None, Qt_MatchFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ findItems(self, str, flags: Union[Qt.MatchFlags, Qt.MatchFlag] = Qt.MatchExactly, column: int = 0) -> List[QStandardItem] """
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

    def horizontalHeaderItem(self, p_int): # real signature unknown; restored from __doc__
        """ horizontalHeaderItem(self, int) -> QStandardItem """
        return QStandardItem

    def index(self, p_int, p_int_1, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ index(self, int, int, parent: QModelIndex = QModelIndex()) -> QModelIndex """
        pass

    def indexFromItem(self, QStandardItem): # real signature unknown; restored from __doc__
        """ indexFromItem(self, QStandardItem) -> QModelIndex """
        pass

    def insertColumn(self, p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        insertColumn(self, int, Iterable[QStandardItem])
        insertColumn(self, int, parent: QModelIndex = QModelIndex()) -> bool
        """
        pass

    def insertColumns(self, p_int, p_int_1, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ insertColumns(self, int, int, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def insertRow(self, p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        insertRow(self, int, Iterable[QStandardItem])
        insertRow(self, int, QStandardItem)
        insertRow(self, int, parent: QModelIndex = QModelIndex()) -> bool
        """
        pass

    def insertRows(self, p_int, p_int_1, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ insertRows(self, int, int, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def invisibleRootItem(self): # real signature unknown; restored from __doc__
        """ invisibleRootItem(self) -> QStandardItem """
        return QStandardItem

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def item(self, p_int, column=0): # real signature unknown; restored from __doc__
        """ item(self, int, column: int = 0) -> QStandardItem """
        return QStandardItem

    def itemChanged(self, QStandardItem): # real signature unknown; restored from __doc__
        """ itemChanged(self, QStandardItem) [signal] """
        pass

    def itemData(self, QModelIndex): # real signature unknown; restored from __doc__
        """ itemData(self, QModelIndex) -> Dict[int, Any] """
        return {}

    def itemFromIndex(self, QModelIndex): # real signature unknown; restored from __doc__
        """ itemFromIndex(self, QModelIndex) -> QStandardItem """
        return QStandardItem

    def itemPrototype(self): # real signature unknown; restored from __doc__
        """ itemPrototype(self) -> QStandardItem """
        return QStandardItem

    def mimeData(self, Iterable, QModelIndex=None): # real signature unknown; restored from __doc__
        """ mimeData(self, Iterable[QModelIndex]) -> QMimeData """
        pass

    def mimeTypes(self): # real signature unknown; restored from __doc__
        """ mimeTypes(self) -> List[str] """
        return []

    def parent(self, QModelIndex=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        parent(self, QModelIndex) -> QModelIndex
        parent(self) -> QObject
        """
        pass

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

    def setColumnCount(self, p_int): # real signature unknown; restored from __doc__
        """ setColumnCount(self, int) """
        pass

    def setData(self, QModelIndex, Any, role=None): # real signature unknown; restored from __doc__
        """ setData(self, QModelIndex, Any, role: int = Qt.EditRole) -> bool """
        return False

    def setHeaderData(self, p_int, Qt_Orientation, Any, role=None): # real signature unknown; restored from __doc__
        """ setHeaderData(self, int, Qt.Orientation, Any, role: int = Qt.EditRole) -> bool """
        return False

    def setHorizontalHeaderItem(self, p_int, QStandardItem): # real signature unknown; restored from __doc__
        """ setHorizontalHeaderItem(self, int, QStandardItem) """
        pass

    def setHorizontalHeaderLabels(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ setHorizontalHeaderLabels(self, Iterable[str]) """
        pass

    def setItem(self, p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setItem(self, int, int, QStandardItem)
        setItem(self, int, QStandardItem)
        """
        pass

    def setItemData(self, QModelIndex, Dict, p_int=None, Any=None): # real signature unknown; restored from __doc__
        """ setItemData(self, QModelIndex, Dict[int, Any]) -> bool """
        return False

    def setItemPrototype(self, QStandardItem): # real signature unknown; restored from __doc__
        """ setItemPrototype(self, QStandardItem) """
        pass

    def setItemRoleNames(self, Dict, p_int=None, Union=None, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setItemRoleNames(self, Dict[int, Union[QByteArray, bytes, bytearray]]) """
        pass

    def setRowCount(self, p_int): # real signature unknown; restored from __doc__
        """ setRowCount(self, int) """
        pass

    def setSortRole(self, p_int): # real signature unknown; restored from __doc__
        """ setSortRole(self, int) """
        pass

    def setVerticalHeaderItem(self, p_int, QStandardItem): # real signature unknown; restored from __doc__
        """ setVerticalHeaderItem(self, int, QStandardItem) """
        pass

    def setVerticalHeaderLabels(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ setVerticalHeaderLabels(self, Iterable[str]) """
        pass

    def sibling(self, p_int, p_int_1, QModelIndex): # real signature unknown; restored from __doc__
        """ sibling(self, int, int, QModelIndex) -> QModelIndex """
        pass

    def sort(self, p_int, order=None): # real signature unknown; restored from __doc__
        """ sort(self, int, order: Qt.SortOrder = Qt.AscendingOrder) """
        pass

    def sortRole(self): # real signature unknown; restored from __doc__
        """ sortRole(self) -> int """
        return 0

    def supportedDropActions(self): # real signature unknown; restored from __doc__
        """ supportedDropActions(self) -> Qt.DropActions """
        pass

    def takeColumn(self, p_int): # real signature unknown; restored from __doc__
        """ takeColumn(self, int) -> List[QStandardItem] """
        return []

    def takeHorizontalHeaderItem(self, p_int): # real signature unknown; restored from __doc__
        """ takeHorizontalHeaderItem(self, int) -> QStandardItem """
        return QStandardItem

    def takeItem(self, p_int, column=0): # real signature unknown; restored from __doc__
        """ takeItem(self, int, column: int = 0) -> QStandardItem """
        return QStandardItem

    def takeRow(self, p_int): # real signature unknown; restored from __doc__
        """ takeRow(self, int) -> List[QStandardItem] """
        return []

    def takeVerticalHeaderItem(self, p_int): # real signature unknown; restored from __doc__
        """ takeVerticalHeaderItem(self, int) -> QStandardItem """
        return QStandardItem

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def verticalHeaderItem(self, p_int): # real signature unknown; restored from __doc__
        """ verticalHeaderItem(self, int) -> QStandardItem """
        return QStandardItem

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


