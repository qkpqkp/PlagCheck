# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QObject import QObject

class QItemSelectionModel(QObject):
    """
    QItemSelectionModel(model: QAbstractItemModel = None)
    QItemSelectionModel(QAbstractItemModel, QObject)
    """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def clearCurrentIndex(self): # real signature unknown; restored from __doc__
        """ clearCurrentIndex(self) """
        pass

    def clearSelection(self): # real signature unknown; restored from __doc__
        """ clearSelection(self) """
        pass

    def columnIntersectsSelection(self, p_int, QModelIndex): # real signature unknown; restored from __doc__
        """ columnIntersectsSelection(self, int, QModelIndex) -> bool """
        return False

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def currentChanged(self, QModelIndex, QModelIndex_1): # real signature unknown; restored from __doc__
        """ currentChanged(self, QModelIndex, QModelIndex) [signal] """
        pass

    def currentColumnChanged(self, QModelIndex, QModelIndex_1): # real signature unknown; restored from __doc__
        """ currentColumnChanged(self, QModelIndex, QModelIndex) [signal] """
        pass

    def currentIndex(self): # real signature unknown; restored from __doc__
        """ currentIndex(self) -> QModelIndex """
        return QModelIndex

    def currentRowChanged(self, QModelIndex, QModelIndex_1): # real signature unknown; restored from __doc__
        """ currentRowChanged(self, QModelIndex, QModelIndex) [signal] """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def emitSelectionChanged(self, QItemSelection, QItemSelection_1): # real signature unknown; restored from __doc__
        """ emitSelectionChanged(self, QItemSelection, QItemSelection) """
        pass

    def hasSelection(self): # real signature unknown; restored from __doc__
        """ hasSelection(self) -> bool """
        return False

    def isColumnSelected(self, p_int, QModelIndex): # real signature unknown; restored from __doc__
        """ isColumnSelected(self, int, QModelIndex) -> bool """
        return False

    def isRowSelected(self, p_int, QModelIndex): # real signature unknown; restored from __doc__
        """ isRowSelected(self, int, QModelIndex) -> bool """
        return False

    def isSelected(self, QModelIndex): # real signature unknown; restored from __doc__
        """ isSelected(self, QModelIndex) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def model(self): # real signature unknown; restored from __doc__
        """ model(self) -> QAbstractItemModel """
        return QAbstractItemModel

    def modelChanged(self, QAbstractItemModel): # real signature unknown; restored from __doc__
        """ modelChanged(self, QAbstractItemModel) [signal] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) """
        pass

    def rowIntersectsSelection(self, p_int, QModelIndex): # real signature unknown; restored from __doc__
        """ rowIntersectsSelection(self, int, QModelIndex) -> bool """
        return False

    def select(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        select(self, QModelIndex, Union[QItemSelectionModel.SelectionFlags, QItemSelectionModel.SelectionFlag])
        select(self, QItemSelection, Union[QItemSelectionModel.SelectionFlags, QItemSelectionModel.SelectionFlag])
        """
        pass

    def selectedColumns(self, row=0): # real signature unknown; restored from __doc__
        """ selectedColumns(self, row: int = 0) -> List[QModelIndex] """
        return []

    def selectedIndexes(self): # real signature unknown; restored from __doc__
        """ selectedIndexes(self) -> List[QModelIndex] """
        return []

    def selectedRows(self, column=0): # real signature unknown; restored from __doc__
        """ selectedRows(self, column: int = 0) -> List[QModelIndex] """
        return []

    def selection(self): # real signature unknown; restored from __doc__
        """ selection(self) -> QItemSelection """
        return QItemSelection

    def selectionChanged(self, QItemSelection, QItemSelection_1): # real signature unknown; restored from __doc__
        """ selectionChanged(self, QItemSelection, QItemSelection) [signal] """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCurrentIndex(self, QModelIndex, Union, QItemSelectionModel_SelectionFlags=None, QItemSelectionModel_SelectionFlag=None): # real signature unknown; restored from __doc__
        """ setCurrentIndex(self, QModelIndex, Union[QItemSelectionModel.SelectionFlags, QItemSelectionModel.SelectionFlag]) """
        pass

    def setModel(self, QAbstractItemModel): # real signature unknown; restored from __doc__
        """ setModel(self, QAbstractItemModel) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    Clear = 1
    ClearAndSelect = 3
    Columns = 64
    Current = 16
    Deselect = 4
    NoUpdate = 0
    Rows = 32
    Select = 2
    SelectCurrent = 18
    Toggle = 8
    ToggleCurrent = 24


