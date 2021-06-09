# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QTreeView import QTreeView

class QTreeWidget(QTreeView):
    """ QTreeWidget(parent: QWidget = None) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def addTopLevelItem(self, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ addTopLevelItem(self, QTreeWidgetItem) """
        pass

    def addTopLevelItems(self, Iterable, QTreeWidgetItem=None): # real signature unknown; restored from __doc__
        """ addTopLevelItems(self, Iterable[QTreeWidgetItem]) """
        pass

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def closeEditor(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closePersistentEditor(self, QTreeWidgetItem, column=0): # real signature unknown; restored from __doc__
        """ closePersistentEditor(self, QTreeWidgetItem, column: int = 0) """
        pass

    def collapseItem(self, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ collapseItem(self, QTreeWidgetItem) """
        pass

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

    def currentChanged(self, *args, **kwargs): # real signature unknown
        pass

    def currentColumn(self): # real signature unknown; restored from __doc__
        """ currentColumn(self) -> int """
        return 0

    def currentItem(self): # real signature unknown; restored from __doc__
        """ currentItem(self) -> QTreeWidgetItem """
        return QTreeWidgetItem

    def currentItemChanged(self, QTreeWidgetItem, QTreeWidgetItem_1): # real signature unknown; restored from __doc__
        """ currentItemChanged(self, QTreeWidgetItem, QTreeWidgetItem) [signal] """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
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

    def drawBranches(self, *args, **kwargs): # real signature unknown
        pass

    def drawFrame(self, *args, **kwargs): # real signature unknown
        pass

    def drawRow(self, *args, **kwargs): # real signature unknown
        pass

    def drawTree(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, QDropEvent): # real signature unknown; restored from __doc__
        """ dropEvent(self, QDropEvent) """
        pass

    def dropIndicatorPosition(self, *args, **kwargs): # real signature unknown
        pass

    def dropMimeData(self, QTreeWidgetItem, p_int, QMimeData, Qt_DropAction): # real signature unknown; restored from __doc__
        """ dropMimeData(self, QTreeWidgetItem, int, QMimeData, Qt.DropAction) -> bool """
        return False

    def edit(self, *args, **kwargs): # real signature unknown
        pass

    def editItem(self, QTreeWidgetItem, column=0): # real signature unknown; restored from __doc__
        """ editItem(self, QTreeWidgetItem, column: int = 0) """
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

    def expandItem(self, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ expandItem(self, QTreeWidgetItem) """
        pass

    def findItems(self, p_str, Union, Qt_MatchFlags=None, Qt_MatchFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ findItems(self, str, Union[Qt.MatchFlags, Qt.MatchFlag], column: int = 0) -> List[QTreeWidgetItem] """
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

    def headerItem(self): # real signature unknown; restored from __doc__
        """ headerItem(self) -> QTreeWidgetItem """
        return QTreeWidgetItem

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def horizontalOffset(self, *args, **kwargs): # real signature unknown
        pass

    def horizontalScrollbarAction(self, *args, **kwargs): # real signature unknown
        pass

    def horizontalScrollbarValueChanged(self, *args, **kwargs): # real signature unknown
        pass

    def indexFromItem(self, QTreeWidgetItem, column=0): # real signature unknown; restored from __doc__
        """ indexFromItem(self, QTreeWidgetItem, column: int = 0) -> QModelIndex """
        pass

    def indexOfTopLevelItem(self, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ indexOfTopLevelItem(self, QTreeWidgetItem) -> int """
        return 0

    def indexRowSizeHint(self, *args, **kwargs): # real signature unknown
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def initStyleOption(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def insertTopLevelItem(self, p_int, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ insertTopLevelItem(self, int, QTreeWidgetItem) """
        pass

    def insertTopLevelItems(self, p_int, Iterable, QTreeWidgetItem=None): # real signature unknown; restored from __doc__
        """ insertTopLevelItems(self, int, Iterable[QTreeWidgetItem]) """
        pass

    def invisibleRootItem(self): # real signature unknown; restored from __doc__
        """ invisibleRootItem(self) -> QTreeWidgetItem """
        return QTreeWidgetItem

    def isFirstItemColumnSpanned(self, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ isFirstItemColumnSpanned(self, QTreeWidgetItem) -> bool """
        return False

    def isIndexHidden(self, *args, **kwargs): # real signature unknown
        pass

    def isPersistentEditorOpen(self, QTreeWidgetItem, column=0): # real signature unknown; restored from __doc__
        """ isPersistentEditorOpen(self, QTreeWidgetItem, column: int = 0) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def itemAbove(self, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ itemAbove(self, QTreeWidgetItem) -> QTreeWidgetItem """
        return QTreeWidgetItem

    def itemActivated(self, QTreeWidgetItem, p_int): # real signature unknown; restored from __doc__
        """ itemActivated(self, QTreeWidgetItem, int) [signal] """
        pass

    def itemAt(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        itemAt(self, QPoint) -> QTreeWidgetItem
        itemAt(self, int, int) -> QTreeWidgetItem
        """
        return QTreeWidgetItem

    def itemBelow(self, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ itemBelow(self, QTreeWidgetItem) -> QTreeWidgetItem """
        return QTreeWidgetItem

    def itemChanged(self, QTreeWidgetItem, p_int): # real signature unknown; restored from __doc__
        """ itemChanged(self, QTreeWidgetItem, int) [signal] """
        pass

    def itemClicked(self, QTreeWidgetItem, p_int): # real signature unknown; restored from __doc__
        """ itemClicked(self, QTreeWidgetItem, int) [signal] """
        pass

    def itemCollapsed(self, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ itemCollapsed(self, QTreeWidgetItem) [signal] """
        pass

    def itemDoubleClicked(self, QTreeWidgetItem, p_int): # real signature unknown; restored from __doc__
        """ itemDoubleClicked(self, QTreeWidgetItem, int) [signal] """
        pass

    def itemEntered(self, QTreeWidgetItem, p_int): # real signature unknown; restored from __doc__
        """ itemEntered(self, QTreeWidgetItem, int) [signal] """
        pass

    def itemExpanded(self, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ itemExpanded(self, QTreeWidgetItem) [signal] """
        pass

    def itemFromIndex(self, QModelIndex): # real signature unknown; restored from __doc__
        """ itemFromIndex(self, QModelIndex) -> QTreeWidgetItem """
        return QTreeWidgetItem

    def itemPressed(self, QTreeWidgetItem, p_int): # real signature unknown; restored from __doc__
        """ itemPressed(self, QTreeWidgetItem, int) [signal] """
        pass

    def itemSelectionChanged(self): # real signature unknown; restored from __doc__
        """ itemSelectionChanged(self) [signal] """
        pass

    def itemWidget(self, QTreeWidgetItem, p_int): # real signature unknown; restored from __doc__
        """ itemWidget(self, QTreeWidgetItem, int) -> QWidget """
        return QWidget

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def mimeData(self, Iterable, QTreeWidgetItem=None): # real signature unknown; restored from __doc__
        """ mimeData(self, Iterable[QTreeWidgetItem]) -> QMimeData """
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

    def openPersistentEditor(self, QTreeWidgetItem, column=0): # real signature unknown; restored from __doc__
        """ openPersistentEditor(self, QTreeWidgetItem, column: int = 0) """
        pass

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def reexpand(self, *args, **kwargs): # real signature unknown
        pass

    def removeItemWidget(self, QTreeWidgetItem, p_int): # real signature unknown; restored from __doc__
        """ removeItemWidget(self, QTreeWidgetItem, int) """
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def rowHeight(self, *args, **kwargs): # real signature unknown
        pass

    def rowsAboutToBeRemoved(self, *args, **kwargs): # real signature unknown
        pass

    def rowsInserted(self, *args, **kwargs): # real signature unknown
        pass

    def rowsRemoved(self, *args, **kwargs): # real signature unknown
        pass

    def scheduleDelayedItemsLayout(self, *args, **kwargs): # real signature unknown
        pass

    def scrollContentsBy(self, *args, **kwargs): # real signature unknown
        pass

    def scrollDirtyRegion(self, *args, **kwargs): # real signature unknown
        pass

    def scrollToItem(self, QTreeWidgetItem, hint=None): # real signature unknown; restored from __doc__
        """ scrollToItem(self, QTreeWidgetItem, hint: QAbstractItemView.ScrollHint = QAbstractItemView.EnsureVisible) """
        pass

    def selectedIndexes(self, *args, **kwargs): # real signature unknown
        pass

    def selectedItems(self): # real signature unknown; restored from __doc__
        """ selectedItems(self) -> List[QTreeWidgetItem] """
        return []

    def selectionChanged(self, *args, **kwargs): # real signature unknown
        pass

    def selectionCommand(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setColumnCount(self, p_int): # real signature unknown; restored from __doc__
        """ setColumnCount(self, int) """
        pass

    def setCurrentItem(self, QTreeWidgetItem, p_int=None, Union=None, QItemSelectionModel_SelectionFlags=None, QItemSelectionModel_SelectionFlag=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setCurrentItem(self, QTreeWidgetItem)
        setCurrentItem(self, QTreeWidgetItem, int)
        setCurrentItem(self, QTreeWidgetItem, int, Union[QItemSelectionModel.SelectionFlags, QItemSelectionModel.SelectionFlag])
        """
        pass

    def setDirtyRegion(self, *args, **kwargs): # real signature unknown
        pass

    def setFirstItemColumnSpanned(self, QTreeWidgetItem, bool): # real signature unknown; restored from __doc__
        """ setFirstItemColumnSpanned(self, QTreeWidgetItem, bool) """
        pass

    def setHeaderItem(self, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ setHeaderItem(self, QTreeWidgetItem) """
        pass

    def setHeaderLabel(self, p_str): # real signature unknown; restored from __doc__
        """ setHeaderLabel(self, str) """
        pass

    def setHeaderLabels(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ setHeaderLabels(self, Iterable[str]) """
        pass

    def setItemWidget(self, QTreeWidgetItem, p_int, QWidget): # real signature unknown; restored from __doc__
        """ setItemWidget(self, QTreeWidgetItem, int, QWidget) """
        pass

    def setModel(self, *args, **kwargs): # real signature unknown
        pass

    def setSelection(self, *args, **kwargs): # real signature unknown
        pass

    def setSelectionModel(self, QItemSelectionModel): # real signature unknown; restored from __doc__
        """ setSelectionModel(self, QItemSelectionModel) """
        pass

    def setState(self, *args, **kwargs): # real signature unknown
        pass

    def setViewportMargins(self, *args, **kwargs): # real signature unknown
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHintForColumn(self, *args, **kwargs): # real signature unknown
        pass

    def sortColumn(self): # real signature unknown; restored from __doc__
        """ sortColumn(self) -> int """
        return 0

    def sortItems(self, p_int, Qt_SortOrder): # real signature unknown; restored from __doc__
        """ sortItems(self, int, Qt.SortOrder) """
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

    def takeTopLevelItem(self, p_int): # real signature unknown; restored from __doc__
        """ takeTopLevelItem(self, int) -> QTreeWidgetItem """
        return QTreeWidgetItem

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def topLevelItem(self, p_int): # real signature unknown; restored from __doc__
        """ topLevelItem(self, int) -> QTreeWidgetItem """
        return QTreeWidgetItem

    def topLevelItemCount(self): # real signature unknown; restored from __doc__
        """ topLevelItemCount(self) -> int """
        return 0

    def updateEditorData(self, *args, **kwargs): # real signature unknown
        pass

    def updateEditorGeometries(self, *args, **kwargs): # real signature unknown
        pass

    def updateGeometries(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

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

    def visualItemRect(self, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ visualItemRect(self, QTreeWidgetItem) -> QRect """
        pass

    def visualRegionForSelection(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


