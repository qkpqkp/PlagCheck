# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QAbstractItemView import QAbstractItemView

class QTableView(QAbstractItemView):
    """ QTableView(parent: QWidget = None) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clearSpans(self): # real signature unknown; restored from __doc__
        """ clearSpans(self) """
        pass

    def closeEditor(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def columnAt(self, p_int): # real signature unknown; restored from __doc__
        """ columnAt(self, int) -> int """
        return 0

    def columnCountChanged(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ columnCountChanged(self, int, int) """
        pass

    def columnMoved(self, p_int, p_int_1, p_int_2): # real signature unknown; restored from __doc__
        """ columnMoved(self, int, int, int) """
        pass

    def columnResized(self, p_int, p_int_1, p_int_2): # real signature unknown; restored from __doc__
        """ columnResized(self, int, int, int) """
        pass

    def columnSpan(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ columnSpan(self, int, int) -> int """
        return 0

    def columnViewportPosition(self, p_int): # real signature unknown; restored from __doc__
        """ columnViewportPosition(self, int) -> int """
        return 0

    def columnWidth(self, p_int): # real signature unknown; restored from __doc__
        """ columnWidth(self, int) -> int """
        return 0

    def commitData(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def currentChanged(self, QModelIndex, QModelIndex_1): # real signature unknown; restored from __doc__
        """ currentChanged(self, QModelIndex, QModelIndex) """
        pass

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

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dropIndicatorPosition(self, *args, **kwargs): # real signature unknown
        pass

    def edit(self, *args, **kwargs): # real signature unknown
        pass

    def editorDestroyed(self, *args, **kwargs): # real signature unknown
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def eventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def executeDelayedItemsLayout(self, *args, **kwargs): # real signature unknown
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

    def gridStyle(self): # real signature unknown; restored from __doc__
        """ gridStyle(self) -> Qt.PenStyle """
        pass

    def hideColumn(self, p_int): # real signature unknown; restored from __doc__
        """ hideColumn(self, int) """
        pass

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def hideRow(self, p_int): # real signature unknown; restored from __doc__
        """ hideRow(self, int) """
        pass

    def horizontalHeader(self): # real signature unknown; restored from __doc__
        """ horizontalHeader(self) -> QHeaderView """
        return QHeaderView

    def horizontalOffset(self): # real signature unknown; restored from __doc__
        """ horizontalOffset(self) -> int """
        return 0

    def horizontalScrollbarAction(self, p_int): # real signature unknown; restored from __doc__
        """ horizontalScrollbarAction(self, int) """
        pass

    def horizontalScrollbarValueChanged(self, *args, **kwargs): # real signature unknown
        pass

    def indexAt(self, QPoint): # real signature unknown; restored from __doc__
        """ indexAt(self, QPoint) -> QModelIndex """
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def initStyleOption(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isColumnHidden(self, p_int): # real signature unknown; restored from __doc__
        """ isColumnHidden(self, int) -> bool """
        return False

    def isCornerButtonEnabled(self): # real signature unknown; restored from __doc__
        """ isCornerButtonEnabled(self) -> bool """
        return False

    def isIndexHidden(self, QModelIndex): # real signature unknown; restored from __doc__
        """ isIndexHidden(self, QModelIndex) -> bool """
        return False

    def isRowHidden(self, p_int): # real signature unknown; restored from __doc__
        """ isRowHidden(self, int) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isSortingEnabled(self): # real signature unknown; restored from __doc__
        """ isSortingEnabled(self) -> bool """
        return False

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

    def moveCursor(self, QAbstractItemView_CursorAction, Union, Qt_KeyboardModifiers=None, Qt_KeyboardModifier=None): # real signature unknown; restored from __doc__
        """ moveCursor(self, QAbstractItemView.CursorAction, Union[Qt.KeyboardModifiers, Qt.KeyboardModifier]) -> QModelIndex """
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ paintEvent(self, QPaintEvent) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resizeColumnsToContents(self): # real signature unknown; restored from __doc__
        """ resizeColumnsToContents(self) """
        pass

    def resizeColumnToContents(self, p_int): # real signature unknown; restored from __doc__
        """ resizeColumnToContents(self, int) """
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def resizeRowsToContents(self): # real signature unknown; restored from __doc__
        """ resizeRowsToContents(self) """
        pass

    def resizeRowToContents(self, p_int): # real signature unknown; restored from __doc__
        """ resizeRowToContents(self, int) """
        pass

    def rowAt(self, p_int): # real signature unknown; restored from __doc__
        """ rowAt(self, int) -> int """
        return 0

    def rowCountChanged(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ rowCountChanged(self, int, int) """
        pass

    def rowHeight(self, p_int): # real signature unknown; restored from __doc__
        """ rowHeight(self, int) -> int """
        return 0

    def rowMoved(self, p_int, p_int_1, p_int_2): # real signature unknown; restored from __doc__
        """ rowMoved(self, int, int, int) """
        pass

    def rowResized(self, p_int, p_int_1, p_int_2): # real signature unknown; restored from __doc__
        """ rowResized(self, int, int, int) """
        pass

    def rowsAboutToBeRemoved(self, *args, **kwargs): # real signature unknown
        pass

    def rowsInserted(self, *args, **kwargs): # real signature unknown
        pass

    def rowSpan(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ rowSpan(self, int, int) -> int """
        return 0

    def rowViewportPosition(self, p_int): # real signature unknown; restored from __doc__
        """ rowViewportPosition(self, int) -> int """
        return 0

    def scheduleDelayedItemsLayout(self, *args, **kwargs): # real signature unknown
        pass

    def scrollContentsBy(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ scrollContentsBy(self, int, int) """
        pass

    def scrollDirtyRegion(self, *args, **kwargs): # real signature unknown
        pass

    def scrollTo(self, QModelIndex, hint=None): # real signature unknown; restored from __doc__
        """ scrollTo(self, QModelIndex, hint: QAbstractItemView.ScrollHint = QAbstractItemView.EnsureVisible) """
        pass

    def selectColumn(self, p_int): # real signature unknown; restored from __doc__
        """ selectColumn(self, int) """
        pass

    def selectedIndexes(self): # real signature unknown; restored from __doc__
        """ selectedIndexes(self) -> List[QModelIndex] """
        return []

    def selectionChanged(self, QItemSelection, QItemSelection_1): # real signature unknown; restored from __doc__
        """ selectionChanged(self, QItemSelection, QItemSelection) """
        pass

    def selectionCommand(self, *args, **kwargs): # real signature unknown
        pass

    def selectRow(self, p_int): # real signature unknown; restored from __doc__
        """ selectRow(self, int) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setColumnHidden(self, p_int, bool): # real signature unknown; restored from __doc__
        """ setColumnHidden(self, int, bool) """
        pass

    def setColumnWidth(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ setColumnWidth(self, int, int) """
        pass

    def setCornerButtonEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setCornerButtonEnabled(self, bool) """
        pass

    def setDirtyRegion(self, *args, **kwargs): # real signature unknown
        pass

    def setGridStyle(self, Qt_PenStyle): # real signature unknown; restored from __doc__
        """ setGridStyle(self, Qt.PenStyle) """
        pass

    def setHorizontalHeader(self, QHeaderView): # real signature unknown; restored from __doc__
        """ setHorizontalHeader(self, QHeaderView) """
        pass

    def setModel(self, QAbstractItemModel): # real signature unknown; restored from __doc__
        """ setModel(self, QAbstractItemModel) """
        pass

    def setRootIndex(self, QModelIndex): # real signature unknown; restored from __doc__
        """ setRootIndex(self, QModelIndex) """
        pass

    def setRowHeight(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ setRowHeight(self, int, int) """
        pass

    def setRowHidden(self, p_int, bool): # real signature unknown; restored from __doc__
        """ setRowHidden(self, int, bool) """
        pass

    def setSelection(self, QRect, Union, QItemSelectionModel_SelectionFlags=None, QItemSelectionModel_SelectionFlag=None): # real signature unknown; restored from __doc__
        """ setSelection(self, QRect, Union[QItemSelectionModel.SelectionFlags, QItemSelectionModel.SelectionFlag]) """
        pass

    def setSelectionModel(self, QItemSelectionModel): # real signature unknown; restored from __doc__
        """ setSelectionModel(self, QItemSelectionModel) """
        pass

    def setShowGrid(self, bool): # real signature unknown; restored from __doc__
        """ setShowGrid(self, bool) """
        pass

    def setSortingEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setSortingEnabled(self, bool) """
        pass

    def setSpan(self, p_int, p_int_1, p_int_2, p_int_3): # real signature unknown; restored from __doc__
        """ setSpan(self, int, int, int, int) """
        pass

    def setState(self, *args, **kwargs): # real signature unknown
        pass

    def setVerticalHeader(self, QHeaderView): # real signature unknown; restored from __doc__
        """ setVerticalHeader(self, QHeaderView) """
        pass

    def setViewportMargins(self, *args, **kwargs): # real signature unknown
        pass

    def setWordWrap(self, bool): # real signature unknown; restored from __doc__
        """ setWordWrap(self, bool) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showColumn(self, p_int): # real signature unknown; restored from __doc__
        """ showColumn(self, int) """
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def showGrid(self): # real signature unknown; restored from __doc__
        """ showGrid(self) -> bool """
        return False

    def showRow(self, p_int): # real signature unknown; restored from __doc__
        """ showRow(self, int) """
        pass

    def sizeHintForColumn(self, p_int): # real signature unknown; restored from __doc__
        """ sizeHintForColumn(self, int) -> int """
        return 0

    def sizeHintForRow(self, p_int): # real signature unknown; restored from __doc__
        """ sizeHintForRow(self, int) -> int """
        return 0

    def sortByColumn(self, p_int, Qt_SortOrder): # real signature unknown; restored from __doc__
        """ sortByColumn(self, int, Qt.SortOrder) """
        pass

    def startDrag(self, *args, **kwargs): # real signature unknown
        pass

    def state(self, *args, **kwargs): # real signature unknown
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, QTimerEvent): # real signature unknown; restored from __doc__
        """ timerEvent(self, QTimerEvent) """
        pass

    def updateEditorData(self, *args, **kwargs): # real signature unknown
        pass

    def updateEditorGeometries(self, *args, **kwargs): # real signature unknown
        pass

    def updateGeometries(self): # real signature unknown; restored from __doc__
        """ updateGeometries(self) """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def verticalHeader(self): # real signature unknown; restored from __doc__
        """ verticalHeader(self) -> QHeaderView """
        return QHeaderView

    def verticalOffset(self): # real signature unknown; restored from __doc__
        """ verticalOffset(self) -> int """
        return 0

    def verticalScrollbarAction(self, p_int): # real signature unknown; restored from __doc__
        """ verticalScrollbarAction(self, int) """
        pass

    def verticalScrollbarValueChanged(self, *args, **kwargs): # real signature unknown
        pass

    def viewOptions(self): # real signature unknown; restored from __doc__
        """ viewOptions(self) -> QStyleOptionViewItem """
        return QStyleOptionViewItem

    def viewportEvent(self, *args, **kwargs): # real signature unknown
        pass

    def viewportMargins(self, *args, **kwargs): # real signature unknown
        pass

    def viewportSizeHint(self): # real signature unknown; restored from __doc__
        """ viewportSizeHint(self) -> QSize """
        pass

    def visualRect(self, QModelIndex): # real signature unknown; restored from __doc__
        """ visualRect(self, QModelIndex) -> QRect """
        pass

    def visualRegionForSelection(self, QItemSelection): # real signature unknown; restored from __doc__
        """ visualRegionForSelection(self, QItemSelection) -> QRegion """
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def wordWrap(self): # real signature unknown; restored from __doc__
        """ wordWrap(self) -> bool """
        return False

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


