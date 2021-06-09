# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QAbstractItemModel import QAbstractItemModel

class QAbstractListModel(QAbstractItemModel):
    """ QAbstractListModel(parent: QObject = None) """
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

    def columnCount(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createIndex(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
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

    def flags(self, QModelIndex): # real signature unknown; restored from __doc__
        """ flags(self, QModelIndex) -> Qt.ItemFlags """
        pass

    def hasChildren(self, *args, **kwargs): # real signature unknown
        pass

    def index(self, p_int, column=0, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ index(self, int, column: int = 0, parent: QModelIndex = QModelIndex()) -> QModelIndex """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def parent(self): # real signature unknown; restored from __doc__
        """ parent(self) -> QObject """
        return QObject

    def persistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resetInternalData(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def sibling(self, p_int, p_int_1, QModelIndex): # real signature unknown; restored from __doc__
        """ sibling(self, int, int, QModelIndex) -> QModelIndex """
        return QModelIndex

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


