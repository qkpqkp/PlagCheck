# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QFileSystemModel(__PyQt5_QtCore.QAbstractItemModel):
    """ QFileSystemModel(parent: QObject = None) """
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

    def directoryLoaded(self, p_str): # real signature unknown; restored from __doc__
        """ directoryLoaded(self, str) [signal] """
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

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def fetchMore(self, QModelIndex): # real signature unknown; restored from __doc__
        """ fetchMore(self, QModelIndex) """
        pass

    def fileIcon(self, QModelIndex): # real signature unknown; restored from __doc__
        """ fileIcon(self, QModelIndex) -> QIcon """
        pass

    def fileInfo(self, QModelIndex): # real signature unknown; restored from __doc__
        """ fileInfo(self, QModelIndex) -> QFileInfo """
        pass

    def fileName(self, QModelIndex): # real signature unknown; restored from __doc__
        """ fileName(self, QModelIndex) -> str """
        return ""

    def filePath(self, QModelIndex): # real signature unknown; restored from __doc__
        """ filePath(self, QModelIndex) -> str """
        return ""

    def fileRenamed(self, p_str, p_str_1, p_str_2): # real signature unknown; restored from __doc__
        """ fileRenamed(self, str, str, str) [signal] """
        pass

    def filter(self): # real signature unknown; restored from __doc__
        """ filter(self) -> QDir.Filters """
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

    def iconProvider(self): # real signature unknown; restored from __doc__
        """ iconProvider(self) -> QFileIconProvider """
        return QFileIconProvider

    def index(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        index(self, int, int, parent: QModelIndex = QModelIndex()) -> QModelIndex
        index(self, str, column: int = 0) -> QModelIndex
        """
        pass

    def isDir(self, QModelIndex): # real signature unknown; restored from __doc__
        """ isDir(self, QModelIndex) -> bool """
        return False

    def isReadOnly(self): # real signature unknown; restored from __doc__
        """ isReadOnly(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def lastModified(self, QModelIndex): # real signature unknown; restored from __doc__
        """ lastModified(self, QModelIndex) -> QDateTime """
        pass

    def mimeData(self, Iterable, QModelIndex=None): # real signature unknown; restored from __doc__
        """ mimeData(self, Iterable[QModelIndex]) -> QMimeData """
        pass

    def mimeTypes(self): # real signature unknown; restored from __doc__
        """ mimeTypes(self) -> List[str] """
        return []

    def mkdir(self, QModelIndex, p_str): # real signature unknown; restored from __doc__
        """ mkdir(self, QModelIndex, str) -> QModelIndex """
        pass

    def myComputer(self, role=None): # real signature unknown; restored from __doc__
        """ myComputer(self, role: int = Qt.DisplayRole) -> Any """
        pass

    def nameFilterDisables(self): # real signature unknown; restored from __doc__
        """ nameFilterDisables(self) -> bool """
        return False

    def nameFilters(self): # real signature unknown; restored from __doc__
        """ nameFilters(self) -> List[str] """
        return []

    def parent(self, QModelIndex): # real signature unknown; restored from __doc__
        """ parent(self, QModelIndex) -> QModelIndex """
        pass

    def permissions(self, QModelIndex): # real signature unknown; restored from __doc__
        """ permissions(self, QModelIndex) -> QFileDevice.Permissions """
        pass

    def persistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def remove(self, QModelIndex): # real signature unknown; restored from __doc__
        """ remove(self, QModelIndex) -> bool """
        return False

    def resetInternalData(self, *args, **kwargs): # real signature unknown
        pass

    def resolveSymlinks(self): # real signature unknown; restored from __doc__
        """ resolveSymlinks(self) -> bool """
        return False

    def rmdir(self, QModelIndex): # real signature unknown; restored from __doc__
        """ rmdir(self, QModelIndex) -> bool """
        return False

    def rootDirectory(self): # real signature unknown; restored from __doc__
        """ rootDirectory(self) -> QDir """
        pass

    def rootPath(self): # real signature unknown; restored from __doc__
        """ rootPath(self) -> str """
        return ""

    def rootPathChanged(self, p_str): # real signature unknown; restored from __doc__
        """ rootPathChanged(self, str) [signal] """
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

    def setFilter(self, Union, QDir_Filters=None, QDir_Filter=None): # real signature unknown; restored from __doc__
        """ setFilter(self, Union[QDir.Filters, QDir.Filter]) """
        pass

    def setIconProvider(self, QFileIconProvider): # real signature unknown; restored from __doc__
        """ setIconProvider(self, QFileIconProvider) """
        pass

    def setNameFilterDisables(self, bool): # real signature unknown; restored from __doc__
        """ setNameFilterDisables(self, bool) """
        pass

    def setNameFilters(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ setNameFilters(self, Iterable[str]) """
        pass

    def setReadOnly(self, bool): # real signature unknown; restored from __doc__
        """ setReadOnly(self, bool) """
        pass

    def setResolveSymlinks(self, bool): # real signature unknown; restored from __doc__
        """ setResolveSymlinks(self, bool) """
        pass

    def setRootPath(self, p_str): # real signature unknown; restored from __doc__
        """ setRootPath(self, str) -> QModelIndex """
        pass

    def sibling(self, p_int, p_int_1, QModelIndex): # real signature unknown; restored from __doc__
        """ sibling(self, int, int, QModelIndex) -> QModelIndex """
        pass

    def size(self, QModelIndex): # real signature unknown; restored from __doc__
        """ size(self, QModelIndex) -> int """
        return 0

    def sort(self, p_int, order=None): # real signature unknown; restored from __doc__
        """ sort(self, int, order: Qt.SortOrder = Qt.AscendingOrder) """
        pass

    def supportedDropActions(self): # real signature unknown; restored from __doc__
        """ supportedDropActions(self) -> Qt.DropActions """
        pass

    def timerEvent(self, QTimerEvent): # real signature unknown; restored from __doc__
        """ timerEvent(self, QTimerEvent) """
        pass

    def type(self, QModelIndex): # real signature unknown; restored from __doc__
        """ type(self, QModelIndex) -> str """
        return ""

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    FileIconRole = 1
    FileNameRole = 258
    FilePathRole = 257
    FilePermissions = 259


