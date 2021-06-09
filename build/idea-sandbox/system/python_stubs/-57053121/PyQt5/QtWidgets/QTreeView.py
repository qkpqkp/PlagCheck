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

class QTreeView(QAbstractItemView):
    """ QTreeView(parent: QWidget = None) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def allColumnsShowFocus(self): # real signature unknown; restored from __doc__
        """ allColumnsShowFocus(self) -> bool """
        return False

    def autoExpandDelay(self): # real signature unknown; restored from __doc__
        """ autoExpandDelay(self) -> int """
        return 0

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEditor(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def collapse(self, QModelIndex): # real signature unknown; restored from __doc__
        """ collapse(self, QModelIndex) """
        pass

    def collapseAll(self): # real signature unknown; restored from __doc__
        """ collapseAll(self) """
        pass

    def collapsed(self, QModelIndex): # real signature unknown; restored from __doc__
        """ collapsed(self, QModelIndex) [signal] """
        pass

    def columnAt(self, p_int): # real signature unknown; restored from __doc__
        """ columnAt(self, int) -> int """
        return 0

    def columnCountChanged(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ columnCountChanged(self, int, int) """
        pass

    def columnMoved(self): # real signature unknown; restored from __doc__
        """ columnMoved(self) """
        pass

    def columnResized(self, p_int, p_int_1, p_int_2): # real signature unknown; restored from __doc__
        """ columnResized(self, int, int, int) """
        pass

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

    def dataChanged(self, QModelIndex, QModelIndex_1, roles, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ dataChanged(self, QModelIndex, QModelIndex, roles: Iterable[int] = []) """
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

    def dragMoveEvent(self, QDragMoveEvent): # real signature unknown; restored from __doc__
        """ dragMoveEvent(self, QDragMoveEvent) """
        pass

    def drawBranches(self, QPainter, QRect, QModelIndex): # real signature unknown; restored from __doc__
        """ drawBranches(self, QPainter, QRect, QModelIndex) """
        pass

    def drawFrame(self, *args, **kwargs): # real signature unknown
        pass

    def drawRow(self, QPainter, QStyleOptionViewItem, QModelIndex): # real signature unknown; restored from __doc__
        """ drawRow(self, QPainter, QStyleOptionViewItem, QModelIndex) """
        pass

    def drawTree(self, QPainter, QRegion): # real signature unknown; restored from __doc__
        """ drawTree(self, QPainter, QRegion) """
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

    def expand(self, QModelIndex): # real signature unknown; restored from __doc__
        """ expand(self, QModelIndex) """
        pass

    def expandAll(self): # real signature unknown; restored from __doc__
        """ expandAll(self) """
        pass

    def expanded(self, QModelIndex): # real signature unknown; restored from __doc__
        """ expanded(self, QModelIndex) [signal] """
        pass

    def expandsOnDoubleClick(self): # real signature unknown; restored from __doc__
        """ expandsOnDoubleClick(self) -> bool """
        return False

    def expandToDepth(self, p_int): # real signature unknown; restored from __doc__
        """ expandToDepth(self, int) """
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

    def header(self): # real signature unknown; restored from __doc__
        """ header(self) -> QHeaderView """
        return QHeaderView

    def hideColumn(self, p_int): # real signature unknown; restored from __doc__
        """ hideColumn(self, int) """
        pass

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def horizontalOffset(self): # real signature unknown; restored from __doc__
        """ horizontalOffset(self) -> int """
        return 0

    def horizontalScrollbarAction(self, p_int): # real signature unknown; restored from __doc__
        """ horizontalScrollbarAction(self, int) """
        pass

    def horizontalScrollbarValueChanged(self, *args, **kwargs): # real signature unknown
        pass

    def indentation(self): # real signature unknown; restored from __doc__
        """ indentation(self) -> int """
        return 0

    def indexAbove(self, QModelIndex): # real signature unknown; restored from __doc__
        """ indexAbove(self, QModelIndex) -> QModelIndex """
        pass

    def indexAt(self, QPoint): # real signature unknown; restored from __doc__
        """ indexAt(self, QPoint) -> QModelIndex """
        pass

    def indexBelow(self, QModelIndex): # real signature unknown; restored from __doc__
        """ indexBelow(self, QModelIndex) -> QModelIndex """
        pass

    def indexRowSizeHint(self, QModelIndex): # real signature unknown; restored from __doc__
        """ indexRowSizeHint(self, QModelIndex) -> int """
        return 0

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def initStyleOption(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isAnimated(self): # real signature unknown; restored from __doc__
        """ isAnimated(self) -> bool """
        return False

    def isColumnHidden(self, p_int): # real signature unknown; restored from __doc__
        """ isColumnHidden(self, int) -> bool """
        return False

    def isExpanded(self, QModelIndex): # real signature unknown; restored from __doc__
        """ isExpanded(self, QModelIndex) -> bool """
        return False

    def isFirstColumnSpanned(self, p_int, QModelIndex): # real signature unknown; restored from __doc__
        """ isFirstColumnSpanned(self, int, QModelIndex) -> bool """
        return False

    def isHeaderHidden(self): # real signature unknown; restored from __doc__
        """ isHeaderHidden(self) -> bool """
        return False

    def isIndexHidden(self, QModelIndex): # real signature unknown; restored from __doc__
        """ isIndexHidden(self, QModelIndex) -> bool """
        return False

    def isRowHidden(self, p_int, QModelIndex): # real signature unknown; restored from __doc__
        """ isRowHidden(self, int, QModelIndex) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isSortingEnabled(self): # real signature unknown; restored from __doc__
        """ isSortingEnabled(self) -> bool """
        return False

    def itemsExpandable(self): # real signature unknown; restored from __doc__
        """ itemsExpandable(self) -> bool """
        return False

    def keyboardSearch(self, p_str): # real signature unknown; restored from __doc__
        """ keyboardSearch(self, str) """
        pass

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, QKeyEvent) """
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def mouseDoubleClickEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mouseDoubleClickEvent(self, QMouseEvent) """
        pass

    def mouseMoveEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mouseMoveEvent(self, QMouseEvent) """
        pass

    def mousePressEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, QMouseEvent) """
        pass

    def mouseReleaseEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, QMouseEvent) """
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

    def reexpand(self): # real signature unknown; restored from __doc__
        """ reexpand(self) """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) """
        pass

    def resetIndentation(self): # real signature unknown; restored from __doc__
        """ resetIndentation(self) """
        pass

    def resizeColumnToContents(self, p_int): # real signature unknown; restored from __doc__
        """ resizeColumnToContents(self, int) """
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def rootIsDecorated(self): # real signature unknown; restored from __doc__
        """ rootIsDecorated(self) -> bool """
        return False

    def rowHeight(self, QModelIndex): # real signature unknown; restored from __doc__
        """ rowHeight(self, QModelIndex) -> int """
        return 0

    def rowsAboutToBeRemoved(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ rowsAboutToBeRemoved(self, QModelIndex, int, int) """
        pass

    def rowsInserted(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ rowsInserted(self, QModelIndex, int, int) """
        pass

    def rowsRemoved(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ rowsRemoved(self, QModelIndex, int, int) """
        pass

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

    def selectAll(self): # real signature unknown; restored from __doc__
        """ selectAll(self) """
        pass

    def selectedIndexes(self): # real signature unknown; restored from __doc__
        """ selectedIndexes(self) -> List[QModelIndex] """
        return []

    def selectionChanged(self, QItemSelection, QItemSelection_1): # real signature unknown; restored from __doc__
        """ selectionChanged(self, QItemSelection, QItemSelection) """
        pass

    def selectionCommand(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAllColumnsShowFocus(self, bool): # real signature unknown; restored from __doc__
        """ setAllColumnsShowFocus(self, bool) """
        pass

    def setAnimated(self, bool): # real signature unknown; restored from __doc__
        """ setAnimated(self, bool) """
        pass

    def setAutoExpandDelay(self, p_int): # real signature unknown; restored from __doc__
        """ setAutoExpandDelay(self, int) """
        pass

    def setColumnHidden(self, p_int, bool): # real signature unknown; restored from __doc__
        """ setColumnHidden(self, int, bool) """
        pass

    def setColumnWidth(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ setColumnWidth(self, int, int) """
        pass

    def setDirtyRegion(self, *args, **kwargs): # real signature unknown
        pass

    def setExpanded(self, QModelIndex, bool): # real signature unknown; restored from __doc__
        """ setExpanded(self, QModelIndex, bool) """
        pass

    def setExpandsOnDoubleClick(self, bool): # real signature unknown; restored from __doc__
        """ setExpandsOnDoubleClick(self, bool) """
        pass

    def setFirstColumnSpanned(self, p_int, QModelIndex, bool): # real signature unknown; restored from __doc__
        """ setFirstColumnSpanned(self, int, QModelIndex, bool) """
        pass

    def setHeader(self, QHeaderView): # real signature unknown; restored from __doc__
        """ setHeader(self, QHeaderView) """
        pass

    def setHeaderHidden(self, bool): # real signature unknown; restored from __doc__
        """ setHeaderHidden(self, bool) """
        pass

    def setIndentation(self, p_int): # real signature unknown; restored from __doc__
        """ setIndentation(self, int) """
        pass

    def setItemsExpandable(self, bool): # real signature unknown; restored from __doc__
        """ setItemsExpandable(self, bool) """
        pass

    def setModel(self, QAbstractItemModel): # real signature unknown; restored from __doc__
        """ setModel(self, QAbstractItemModel) """
        pass

    def setRootIndex(self, QModelIndex): # real signature unknown; restored from __doc__
        """ setRootIndex(self, QModelIndex) """
        pass

    def setRootIsDecorated(self, bool): # real signature unknown; restored from __doc__
        """ setRootIsDecorated(self, bool) """
        pass

    def setRowHidden(self, p_int, QModelIndex, bool): # real signature unknown; restored from __doc__
        """ setRowHidden(self, int, QModelIndex, bool) """
        pass

    def setSelection(self, QRect, Union, QItemSelectionModel_SelectionFlags=None, QItemSelectionModel_SelectionFlag=None): # real signature unknown; restored from __doc__
        """ setSelection(self, QRect, Union[QItemSelectionModel.SelectionFlags, QItemSelectionModel.SelectionFlag]) """
        pass

    def setSelectionModel(self, QItemSelectionModel): # real signature unknown; restored from __doc__
        """ setSelectionModel(self, QItemSelectionModel) """
        pass

    def setSortingEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setSortingEnabled(self, bool) """
        pass

    def setState(self, *args, **kwargs): # real signature unknown
        pass

    def setTreePosition(self, p_int): # real signature unknown; restored from __doc__
        """ setTreePosition(self, int) """
        pass

    def setUniformRowHeights(self, bool): # real signature unknown; restored from __doc__
        """ setUniformRowHeights(self, bool) """
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

    def sizeHintForColumn(self, p_int): # real signature unknown; restored from __doc__
        """ sizeHintForColumn(self, int) -> int """
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

    def treePosition(self): # real signature unknown; restored from __doc__
        """ treePosition(self) -> int """
        return 0

    def uniformRowHeights(self): # real signature unknown; restored from __doc__
        """ uniformRowHeights(self) -> bool """
        return False

    def updateEditorData(self, *args, **kwargs): # real signature unknown
        pass

    def updateEditorGeometries(self, *args, **kwargs): # real signature unknown
        pass

    def updateGeometries(self): # real signature unknown; restored from __doc__
        """ updateGeometries(self) """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def verticalOffset(self): # real signature unknown; restored from __doc__
        """ verticalOffset(self) -> int """
        return 0

    def verticalScrollbarAction(self, *args, **kwargs): # real signature unknown
        pass

    def verticalScrollbarValueChanged(self, *args, **kwargs): # real signature unknown
        pass

    def viewOptions(self, *args, **kwargs): # real signature unknown
        pass

    def viewportEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ viewportEvent(self, QEvent) -> bool """
        return False

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


