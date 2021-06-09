# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QTableView import QTableView

class QTableWidget(QTableView):
    """
    QTableWidget(parent: QWidget = None)
    QTableWidget(int, int, parent: QWidget = None)
    """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def cellActivated(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ cellActivated(self, int, int) [signal] """
        pass

    def cellChanged(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ cellChanged(self, int, int) [signal] """
        pass

    def cellClicked(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ cellClicked(self, int, int) [signal] """
        pass

    def cellDoubleClicked(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ cellDoubleClicked(self, int, int) [signal] """
        pass

    def cellEntered(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ cellEntered(self, int, int) [signal] """
        pass

    def cellPressed(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ cellPressed(self, int, int) [signal] """
        pass

    def cellWidget(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ cellWidget(self, int, int) -> QWidget """
        return QWidget

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def clearContents(self): # real signature unknown; restored from __doc__
        """ clearContents(self) """
        pass

    def closeEditor(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closePersistentEditor(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ closePersistentEditor(self, QTableWidgetItem) """
        pass

    def column(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ column(self, QTableWidgetItem) -> int """
        return 0

    def columnCount(self): # real signature unknown; restored from __doc__
        """ columnCount(self) -> int """
        return 0

    def columnCountChanged(self, *args, **kwargs): # real signature unknown
        pass

    def columnMoved(self, *args, **kwargs): # real signature unknown
        pass

    def columnResized(self, *args, **kwargs): # real signature unknown
        pass

    def commitData(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def currentCellChanged(self, p_int, p_int_1, p_int_2, p_int_3): # real signature unknown; restored from __doc__
        """ currentCellChanged(self, int, int, int, int) [signal] """
        pass

    def currentChanged(self, *args, **kwargs): # real signature unknown
        pass

    def currentColumn(self): # real signature unknown; restored from __doc__
        """ currentColumn(self) -> int """
        return 0

    def currentItem(self): # real signature unknown; restored from __doc__
        """ currentItem(self) -> QTableWidgetItem """
        return QTableWidgetItem

    def currentItemChanged(self, QTableWidgetItem, QTableWidgetItem_1): # real signature unknown; restored from __doc__
        """ currentItemChanged(self, QTableWidgetItem, QTableWidgetItem) [signal] """
        pass

    def currentRow(self): # real signature unknown; restored from __doc__
        """ currentRow(self) -> int """
        return 0

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dataChanged(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def dirtyRegionOffset(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def drawFrame(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, QDropEvent): # real signature unknown; restored from __doc__
        """ dropEvent(self, QDropEvent) """
        pass

    def dropIndicatorPosition(self, *args, **kwargs): # real signature unknown
        pass

    def dropMimeData(self, p_int, p_int_1, QMimeData, Qt_DropAction): # real signature unknown; restored from __doc__
        """ dropMimeData(self, int, int, QMimeData, Qt.DropAction) -> bool """
        return False

    def edit(self, *args, **kwargs): # real signature unknown
        pass

    def editItem(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ editItem(self, QTableWidgetItem) """
        pass

    def editorDestroyed(self, *args, **kwargs): # real signature unknown
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def eventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def executeDelayedItemsLayout(self, *args, **kwargs): # real signature unknown
        pass

    def findItems(self, p_str, Union, Qt_MatchFlags=None, Qt_MatchFlag=None): # real signature unknown; restored from __doc__
        """ findItems(self, str, Union[Qt.MatchFlags, Qt.MatchFlag]) -> List[QTableWidgetItem] """
        return []

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

    def horizontalHeaderItem(self, p_int): # real signature unknown; restored from __doc__
        """ horizontalHeaderItem(self, int) -> QTableWidgetItem """
        return QTableWidgetItem

    def horizontalOffset(self, *args, **kwargs): # real signature unknown
        pass

    def horizontalScrollbarAction(self, *args, **kwargs): # real signature unknown
        pass

    def horizontalScrollbarValueChanged(self, *args, **kwargs): # real signature unknown
        pass

    def indexFromItem(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ indexFromItem(self, QTableWidgetItem) -> QModelIndex """
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def initStyleOption(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def insertColumn(self, p_int): # real signature unknown; restored from __doc__
        """ insertColumn(self, int) """
        pass

    def insertRow(self, p_int): # real signature unknown; restored from __doc__
        """ insertRow(self, int) """
        pass

    def isIndexHidden(self, *args, **kwargs): # real signature unknown
        pass

    def isPersistentEditorOpen(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ isPersistentEditorOpen(self, QTableWidgetItem) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isSortingEnabled(self): # real signature unknown; restored from __doc__
        """ isSortingEnabled(self) -> bool """
        return False

    def item(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ item(self, int, int) -> QTableWidgetItem """
        return QTableWidgetItem

    def itemActivated(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ itemActivated(self, QTableWidgetItem) [signal] """
        pass

    def itemAt(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        itemAt(self, QPoint) -> QTableWidgetItem
        itemAt(self, int, int) -> QTableWidgetItem
        """
        return QTableWidgetItem

    def itemChanged(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ itemChanged(self, QTableWidgetItem) [signal] """
        pass

    def itemClicked(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ itemClicked(self, QTableWidgetItem) [signal] """
        pass

    def itemDoubleClicked(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ itemDoubleClicked(self, QTableWidgetItem) [signal] """
        pass

    def itemEntered(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ itemEntered(self, QTableWidgetItem) [signal] """
        pass

    def itemFromIndex(self, QModelIndex): # real signature unknown; restored from __doc__
        """ itemFromIndex(self, QModelIndex) -> QTableWidgetItem """
        return QTableWidgetItem

    def itemPressed(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ itemPressed(self, QTableWidgetItem) [signal] """
        pass

    def itemPrototype(self): # real signature unknown; restored from __doc__
        """ itemPrototype(self) -> QTableWidgetItem """
        return QTableWidgetItem

    def items(self, QMimeData): # real signature unknown; restored from __doc__
        """ items(self, QMimeData) -> List[QTableWidgetItem] """
        return []

    def itemSelectionChanged(self): # real signature unknown; restored from __doc__
        """ itemSelectionChanged(self) [signal] """
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def mimeData(self, Iterable, QTableWidgetItem=None): # real signature unknown; restored from __doc__
        """ mimeData(self, Iterable[QTableWidgetItem]) -> QMimeData """
        pass

    def mimeTypes(self): # real signature unknown; restored from __doc__
        """ mimeTypes(self) -> List[str] """
        return []

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def moveCursor(self, *args, **kwargs): # real signature unknown
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def openPersistentEditor(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ openPersistentEditor(self, QTableWidgetItem) """
        pass

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeCellWidget(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ removeCellWidget(self, int, int) """
        pass

    def removeColumn(self, p_int): # real signature unknown; restored from __doc__
        """ removeColumn(self, int) """
        pass

    def removeRow(self, p_int): # real signature unknown; restored from __doc__
        """ removeRow(self, int) """
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def row(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ row(self, QTableWidgetItem) -> int """
        return 0

    def rowCount(self): # real signature unknown; restored from __doc__
        """ rowCount(self) -> int """
        return 0

    def rowCountChanged(self, *args, **kwargs): # real signature unknown
        pass

    def rowMoved(self, *args, **kwargs): # real signature unknown
        pass

    def rowResized(self, *args, **kwargs): # real signature unknown
        pass

    def rowsAboutToBeRemoved(self, *args, **kwargs): # real signature unknown
        pass

    def rowsInserted(self, *args, **kwargs): # real signature unknown
        pass

    def scheduleDelayedItemsLayout(self, *args, **kwargs): # real signature unknown
        pass

    def scrollContentsBy(self, *args, **kwargs): # real signature unknown
        pass

    def scrollDirtyRegion(self, *args, **kwargs): # real signature unknown
        pass

    def scrollToItem(self, QTableWidgetItem, hint=None): # real signature unknown; restored from __doc__
        """ scrollToItem(self, QTableWidgetItem, hint: QAbstractItemView.ScrollHint = QAbstractItemView.EnsureVisible) """
        pass

    def selectedIndexes(self, *args, **kwargs): # real signature unknown
        pass

    def selectedItems(self): # real signature unknown; restored from __doc__
        """ selectedItems(self) -> List[QTableWidgetItem] """
        return []

    def selectedRanges(self): # real signature unknown; restored from __doc__
        """ selectedRanges(self) -> List[QTableWidgetSelectionRange] """
        return []

    def selectionChanged(self, *args, **kwargs): # real signature unknown
        pass

    def selectionCommand(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCellWidget(self, p_int, p_int_1, QWidget): # real signature unknown; restored from __doc__
        """ setCellWidget(self, int, int, QWidget) """
        pass

    def setColumnCount(self, p_int): # real signature unknown; restored from __doc__
        """ setColumnCount(self, int) """
        pass

    def setCurrentCell(self, p_int, p_int_1, Union=None, QItemSelectionModel_SelectionFlags=None, QItemSelectionModel_SelectionFlag=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setCurrentCell(self, int, int)
        setCurrentCell(self, int, int, Union[QItemSelectionModel.SelectionFlags, QItemSelectionModel.SelectionFlag])
        """
        pass

    def setCurrentItem(self, QTableWidgetItem, Union=None, QItemSelectionModel_SelectionFlags=None, QItemSelectionModel_SelectionFlag=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setCurrentItem(self, QTableWidgetItem)
        setCurrentItem(self, QTableWidgetItem, Union[QItemSelectionModel.SelectionFlags, QItemSelectionModel.SelectionFlag])
        """
        pass

    def setDirtyRegion(self, *args, **kwargs): # real signature unknown
        pass

    def setHorizontalHeaderItem(self, p_int, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ setHorizontalHeaderItem(self, int, QTableWidgetItem) """
        pass

    def setHorizontalHeaderLabels(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ setHorizontalHeaderLabels(self, Iterable[str]) """
        pass

    def setItem(self, p_int, p_int_1, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ setItem(self, int, int, QTableWidgetItem) """
        pass

    def setItemPrototype(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ setItemPrototype(self, QTableWidgetItem) """
        pass

    def setModel(self, *args, **kwargs): # real signature unknown
        pass

    def setRangeSelected(self, QTableWidgetSelectionRange, bool): # real signature unknown; restored from __doc__
        """ setRangeSelected(self, QTableWidgetSelectionRange, bool) """
        pass

    def setRowCount(self, p_int): # real signature unknown; restored from __doc__
        """ setRowCount(self, int) """
        pass

    def setSelection(self, *args, **kwargs): # real signature unknown
        pass

    def setSortingEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setSortingEnabled(self, bool) """
        pass

    def setState(self, *args, **kwargs): # real signature unknown
        pass

    def setVerticalHeaderItem(self, p_int, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ setVerticalHeaderItem(self, int, QTableWidgetItem) """
        pass

    def setVerticalHeaderLabels(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ setVerticalHeaderLabels(self, Iterable[str]) """
        pass

    def setViewportMargins(self, *args, **kwargs): # real signature unknown
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHintForColumn(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHintForRow(self, *args, **kwargs): # real signature unknown
        pass

    def sortItems(self, p_int, order=None): # real signature unknown; restored from __doc__
        """ sortItems(self, int, order: Qt.SortOrder = Qt.AscendingOrder) """
        pass

    def startDrag(self, *args, **kwargs): # real signature unknown
        pass

    def state(self, *args, **kwargs): # real signature unknown
        pass

    def supportedDropActions(self): # real signature unknown; restored from __doc__
        """ supportedDropActions(self) -> Qt.DropActions """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def takeHorizontalHeaderItem(self, p_int): # real signature unknown; restored from __doc__
        """ takeHorizontalHeaderItem(self, int) -> QTableWidgetItem """
        return QTableWidgetItem

    def takeItem(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ takeItem(self, int, int) -> QTableWidgetItem """
        return QTableWidgetItem

    def takeVerticalHeaderItem(self, p_int): # real signature unknown; restored from __doc__
        """ takeVerticalHeaderItem(self, int) -> QTableWidgetItem """
        return QTableWidgetItem

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateEditorData(self, *args, **kwargs): # real signature unknown
        pass

    def updateEditorGeometries(self, *args, **kwargs): # real signature unknown
        pass

    def updateGeometries(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def verticalHeaderItem(self, p_int): # real signature unknown; restored from __doc__
        """ verticalHeaderItem(self, int) -> QTableWidgetItem """
        return QTableWidgetItem

    def verticalOffset(self, *args, **kwargs): # real signature unknown
        pass

    def verticalScrollbarAction(self, *args, **kwargs): # real signature unknown
        pass

    def verticalScrollbarValueChanged(self, *args, **kwargs): # real signature unknown
        pass

    def viewOptions(self, *args, **kwargs): # real signature unknown
        pass

    def viewportEvent(self, *args, **kwargs): # real signature unknown
        pass

    def viewportMargins(self, *args, **kwargs): # real signature unknown
        pass

    def viewportSizeHint(self, *args, **kwargs): # real signature unknown
        pass

    def visualColumn(self, p_int): # real signature unknown; restored from __doc__
        """ visualColumn(self, int) -> int """
        return 0

    def visualItemRect(self, QTableWidgetItem): # real signature unknown; restored from __doc__
        """ visualItemRect(self, QTableWidgetItem) -> QRect """
        pass

    def visualRegionForSelection(self, *args, **kwargs): # real signature unknown
        pass

    def visualRow(self, p_int): # real signature unknown; restored from __doc__
        """ visualRow(self, int) -> int """
        return 0

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


