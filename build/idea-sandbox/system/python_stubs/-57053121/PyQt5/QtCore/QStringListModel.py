# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QAbstractListModel import QAbstractListModel

class QStringListModel(QAbstractListModel):
    """
    QStringListModel(parent: QObject = None)
    QStringListModel(Iterable[str], parent: QObject = None)
    """
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

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createIndex(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def data(self, QModelIndex, p_int): # real signature unknown; restored from __doc__
        """ data(self, QModelIndex, int) -> Any """
        pass

    def decodeData(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

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

    def flags(self, QModelIndex): # real signature unknown; restored from __doc__
        """ flags(self, QModelIndex) -> Qt.ItemFlags """
        pass

    def insertRows(self, p_int, p_int_1, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ insertRows(self, int, int, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def persistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
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

    def setStringList(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ setStringList(self, Iterable[str]) """
        pass

    def sibling(self, p_int, p_int_1, QModelIndex): # real signature unknown; restored from __doc__
        """ sibling(self, int, int, QModelIndex) -> QModelIndex """
        return QModelIndex

    def sort(self, p_int, order=None): # real signature unknown; restored from __doc__
        """ sort(self, int, order: Qt.SortOrder = Qt.AscendingOrder) """
        pass

    def stringList(self): # real signature unknown; restored from __doc__
        """ stringList(self) -> List[str] """
        return []

    def supportedDropActions(self): # real signature unknown; restored from __doc__
        """ supportedDropActions(self) -> Qt.DropActions """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


