# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QAbstractScrollArea import QAbstractScrollArea

class QAbstractItemView(QAbstractScrollArea):
    """ QAbstractItemView(parent: QWidget = None) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def activated(self, QModelIndex): # real signature unknown; restored from __doc__
        """ activated(self, QModelIndex) [signal] """
        pass

    def alternatingRowColors(self): # real signature unknown; restored from __doc__
        """ alternatingRowColors(self) -> bool """
        return False

    def autoScrollMargin(self): # real signature unknown; restored from __doc__
        """ autoScrollMargin(self) -> int """
        return 0

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clearSelection(self): # real signature unknown; restored from __doc__
        """ clearSelection(self) """
        pass

    def clicked(self, QModelIndex): # real signature unknown; restored from __doc__
        """ clicked(self, QModelIndex) [signal] """
        pass

    def closeEditor(self, QWidget, QAbstractItemDelegate_EndEditHint): # real signature unknown; restored from __doc__
        """ closeEditor(self, QWidget, QAbstractItemDelegate.EndEditHint) """
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closePersistentEditor(self, QModelIndex): # real signature unknown; restored from __doc__
        """ closePersistentEditor(self, QModelIndex) """
        pass

    def commitData(self, QWidget): # real signature unknown; restored from __doc__
        """ commitData(self, QWidget) """
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

    def currentIndex(self): # real signature unknown; restored from __doc__
        """ currentIndex(self) -> QModelIndex """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dataChanged(self, QModelIndex, QModelIndex_1, roles, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ dataChanged(self, QModelIndex, QModelIndex, roles: Iterable[int] = []) """
        pass

    def defaultDropAction(self): # real signature unknown; restored from __doc__
        """ defaultDropAction(self) -> Qt.DropAction """
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def dirtyRegionOffset(self): # real signature unknown; restored from __doc__
        """ dirtyRegionOffset(self) -> QPoint """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def doubleClicked(self, QModelIndex): # real signature unknown; restored from __doc__
        """ doubleClicked(self, QModelIndex) [signal] """
        pass

    def dragDropMode(self): # real signature unknown; restored from __doc__
        """ dragDropMode(self) -> QAbstractItemView.DragDropMode """
        pass

    def dragDropOverwriteMode(self): # real signature unknown; restored from __doc__
        """ dragDropOverwriteMode(self) -> bool """
        return False

    def dragEnabled(self): # real signature unknown; restored from __doc__
        """ dragEnabled(self) -> bool """
        return False

    def dragEnterEvent(self, QDragEnterEvent): # real signature unknown; restored from __doc__
        """ dragEnterEvent(self, QDragEnterEvent) """
        pass

    def dragLeaveEvent(self, QDragLeaveEvent): # real signature unknown; restored from __doc__
        """ dragLeaveEvent(self, QDragLeaveEvent) """
        pass

    def dragMoveEvent(self, QDragMoveEvent): # real signature unknown; restored from __doc__
        """ dragMoveEvent(self, QDragMoveEvent) """
        pass

    def drawFrame(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, QDropEvent): # real signature unknown; restored from __doc__
        """ dropEvent(self, QDropEvent) """
        pass

    def dropIndicatorPosition(self): # real signature unknown; restored from __doc__
        """ dropIndicatorPosition(self) -> QAbstractItemView.DropIndicatorPosition """
        pass

    def edit(self, QModelIndex, QAbstractItemView_EditTrigger=None, QEvent=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        edit(self, QModelIndex)
        edit(self, QModelIndex, QAbstractItemView.EditTrigger, QEvent) -> bool
        """
        return False

    def editorDestroyed(self, QObject): # real signature unknown; restored from __doc__
        """ editorDestroyed(self, QObject) """
        pass

    def editTriggers(self): # real signature unknown; restored from __doc__
        """ editTriggers(self) -> QAbstractItemView.EditTriggers """
        pass

    def entered(self, QModelIndex): # real signature unknown; restored from __doc__
        """ entered(self, QModelIndex) [signal] """
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def eventFilter(self, QObject, QEvent): # real signature unknown; restored from __doc__
        """ eventFilter(self, QObject, QEvent) -> bool """
        return False

    def executeDelayedItemsLayout(self): # real signature unknown; restored from __doc__
        """ executeDelayedItemsLayout(self) """
        pass

    def focusInEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ focusInEvent(self, QFocusEvent) """
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, bool): # real signature unknown; restored from __doc__
        """ focusNextPrevChild(self, bool) -> bool """
        return False

    def focusOutEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, QFocusEvent) """
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def hasAutoScroll(self): # real signature unknown; restored from __doc__
        """ hasAutoScroll(self) -> bool """
        return False

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def horizontalOffset(self): # real signature unknown; restored from __doc__
        """ horizontalOffset(self) -> int """
        return 0

    def horizontalScrollbarAction(self, p_int): # real signature unknown; restored from __doc__
        """ horizontalScrollbarAction(self, int) """
        pass

    def horizontalScrollbarValueChanged(self, p_int): # real signature unknown; restored from __doc__
        """ horizontalScrollbarValueChanged(self, int) """
        pass

    def horizontalScrollMode(self): # real signature unknown; restored from __doc__
        """ horizontalScrollMode(self) -> QAbstractItemView.ScrollMode """
        pass

    def iconSize(self): # real signature unknown; restored from __doc__
        """ iconSize(self) -> QSize """
        pass

    def iconSizeChanged(self, QSize): # real signature unknown; restored from __doc__
        """ iconSizeChanged(self, QSize) [signal] """
        pass

    def indexAt(self, QPoint): # real signature unknown; restored from __doc__
        """ indexAt(self, QPoint) -> QModelIndex """
        pass

    def indexWidget(self, QModelIndex): # real signature unknown; restored from __doc__
        """ indexWidget(self, QModelIndex) -> QWidget """
        return QWidget

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def initStyleOption(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, QInputMethodEvent): # real signature unknown; restored from __doc__
        """ inputMethodEvent(self, QInputMethodEvent) """
        pass

    def inputMethodQuery(self, Qt_InputMethodQuery): # real signature unknown; restored from __doc__
        """ inputMethodQuery(self, Qt.InputMethodQuery) -> Any """
        pass

    def isIndexHidden(self, QModelIndex): # real signature unknown; restored from __doc__
        """ isIndexHidden(self, QModelIndex) -> bool """
        return False

    def isPersistentEditorOpen(self, QModelIndex): # real signature unknown; restored from __doc__
        """ isPersistentEditorOpen(self, QModelIndex) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def itemDelegate(self, QModelIndex=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        itemDelegate(self) -> QAbstractItemDelegate
        itemDelegate(self, QModelIndex) -> QAbstractItemDelegate
        """
        return QAbstractItemDelegate

    def itemDelegateForColumn(self, p_int): # real signature unknown; restored from __doc__
        """ itemDelegateForColumn(self, int) -> QAbstractItemDelegate """
        return QAbstractItemDelegate

    def itemDelegateForRow(self, p_int): # real signature unknown; restored from __doc__
        """ itemDelegateForRow(self, int) -> QAbstractItemDelegate """
        return QAbstractItemDelegate

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

    def model(self): # real signature unknown; restored from __doc__
        """ model(self) -> QAbstractItemModel """
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

    def openPersistentEditor(self, QModelIndex): # real signature unknown; restored from __doc__
        """ openPersistentEditor(self, QModelIndex) """
        pass

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def pressed(self, QModelIndex): # real signature unknown; restored from __doc__
        """ pressed(self, QModelIndex) [signal] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) """
        pass

    def resetHorizontalScrollMode(self): # real signature unknown; restored from __doc__
        """ resetHorizontalScrollMode(self) """
        pass

    def resetVerticalScrollMode(self): # real signature unknown; restored from __doc__
        """ resetVerticalScrollMode(self) """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ resizeEvent(self, QResizeEvent) """
        pass

    def rootIndex(self): # real signature unknown; restored from __doc__
        """ rootIndex(self) -> QModelIndex """
        pass

    def rowsAboutToBeRemoved(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ rowsAboutToBeRemoved(self, QModelIndex, int, int) """
        pass

    def rowsInserted(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ rowsInserted(self, QModelIndex, int, int) """
        pass

    def scheduleDelayedItemsLayout(self): # real signature unknown; restored from __doc__
        """ scheduleDelayedItemsLayout(self) """
        pass

    def scrollContentsBy(self, *args, **kwargs): # real signature unknown
        pass

    def scrollDirtyRegion(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ scrollDirtyRegion(self, int, int) """
        pass

    def scrollTo(self, QModelIndex, hint=None): # real signature unknown; restored from __doc__
        """ scrollTo(self, QModelIndex, hint: QAbstractItemView.ScrollHint = QAbstractItemView.EnsureVisible) """
        pass

    def scrollToBottom(self): # real signature unknown; restored from __doc__
        """ scrollToBottom(self) """
        pass

    def scrollToTop(self): # real signature unknown; restored from __doc__
        """ scrollToTop(self) """
        pass

    def selectAll(self): # real signature unknown; restored from __doc__
        """ selectAll(self) """
        pass

    def selectedIndexes(self): # real signature unknown; restored from __doc__
        """ selectedIndexes(self) -> List[QModelIndex] """
        return []

    def selectionBehavior(self): # real signature unknown; restored from __doc__
        """ selectionBehavior(self) -> QAbstractItemView.SelectionBehavior """
        pass

    def selectionChanged(self, QItemSelection, QItemSelection_1): # real signature unknown; restored from __doc__
        """ selectionChanged(self, QItemSelection, QItemSelection) """
        pass

    def selectionCommand(self, QModelIndex, event=None): # real signature unknown; restored from __doc__
        """ selectionCommand(self, QModelIndex, event: QEvent = None) -> QItemSelectionModel.SelectionFlags """
        pass

    def selectionMode(self): # real signature unknown; restored from __doc__
        """ selectionMode(self) -> QAbstractItemView.SelectionMode """
        pass

    def selectionModel(self): # real signature unknown; restored from __doc__
        """ selectionModel(self) -> QItemSelectionModel """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAlternatingRowColors(self, bool): # real signature unknown; restored from __doc__
        """ setAlternatingRowColors(self, bool) """
        pass

    def setAutoScroll(self, bool): # real signature unknown; restored from __doc__
        """ setAutoScroll(self, bool) """
        pass

    def setAutoScrollMargin(self, p_int): # real signature unknown; restored from __doc__
        """ setAutoScrollMargin(self, int) """
        pass

    def setCurrentIndex(self, QModelIndex): # real signature unknown; restored from __doc__
        """ setCurrentIndex(self, QModelIndex) """
        pass

    def setDefaultDropAction(self, Qt_DropAction): # real signature unknown; restored from __doc__
        """ setDefaultDropAction(self, Qt.DropAction) """
        pass

    def setDirtyRegion(self, QRegion): # real signature unknown; restored from __doc__
        """ setDirtyRegion(self, QRegion) """
        pass

    def setDragDropMode(self, QAbstractItemView_DragDropMode): # real signature unknown; restored from __doc__
        """ setDragDropMode(self, QAbstractItemView.DragDropMode) """
        pass

    def setDragDropOverwriteMode(self, bool): # real signature unknown; restored from __doc__
        """ setDragDropOverwriteMode(self, bool) """
        pass

    def setDragEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setDragEnabled(self, bool) """
        pass

    def setDropIndicatorShown(self, bool): # real signature unknown; restored from __doc__
        """ setDropIndicatorShown(self, bool) """
        pass

    def setEditTriggers(self, Union, QAbstractItemView_EditTriggers=None, QAbstractItemView_EditTrigger=None): # real signature unknown; restored from __doc__
        """ setEditTriggers(self, Union[QAbstractItemView.EditTriggers, QAbstractItemView.EditTrigger]) """
        pass

    def setHorizontalScrollMode(self, QAbstractItemView_ScrollMode): # real signature unknown; restored from __doc__
        """ setHorizontalScrollMode(self, QAbstractItemView.ScrollMode) """
        pass

    def setIconSize(self, QSize): # real signature unknown; restored from __doc__
        """ setIconSize(self, QSize) """
        pass

    def setIndexWidget(self, QModelIndex, QWidget): # real signature unknown; restored from __doc__
        """ setIndexWidget(self, QModelIndex, QWidget) """
        pass

    def setItemDelegate(self, QAbstractItemDelegate): # real signature unknown; restored from __doc__
        """ setItemDelegate(self, QAbstractItemDelegate) """
        pass

    def setItemDelegateForColumn(self, p_int, QAbstractItemDelegate): # real signature unknown; restored from __doc__
        """ setItemDelegateForColumn(self, int, QAbstractItemDelegate) """
        pass

    def setItemDelegateForRow(self, p_int, QAbstractItemDelegate): # real signature unknown; restored from __doc__
        """ setItemDelegateForRow(self, int, QAbstractItemDelegate) """
        pass

    def setModel(self, QAbstractItemModel): # real signature unknown; restored from __doc__
        """ setModel(self, QAbstractItemModel) """
        pass

    def setRootIndex(self, QModelIndex): # real signature unknown; restored from __doc__
        """ setRootIndex(self, QModelIndex) """
        pass

    def setSelection(self, QRect, Union, QItemSelectionModel_SelectionFlags=None, QItemSelectionModel_SelectionFlag=None): # real signature unknown; restored from __doc__
        """ setSelection(self, QRect, Union[QItemSelectionModel.SelectionFlags, QItemSelectionModel.SelectionFlag]) """
        pass

    def setSelectionBehavior(self, QAbstractItemView_SelectionBehavior): # real signature unknown; restored from __doc__
        """ setSelectionBehavior(self, QAbstractItemView.SelectionBehavior) """
        pass

    def setSelectionMode(self, QAbstractItemView_SelectionMode): # real signature unknown; restored from __doc__
        """ setSelectionMode(self, QAbstractItemView.SelectionMode) """
        pass

    def setSelectionModel(self, QItemSelectionModel): # real signature unknown; restored from __doc__
        """ setSelectionModel(self, QItemSelectionModel) """
        pass

    def setState(self, QAbstractItemView_State): # real signature unknown; restored from __doc__
        """ setState(self, QAbstractItemView.State) """
        pass

    def setTabKeyNavigation(self, bool): # real signature unknown; restored from __doc__
        """ setTabKeyNavigation(self, bool) """
        pass

    def setTextElideMode(self, Qt_TextElideMode): # real signature unknown; restored from __doc__
        """ setTextElideMode(self, Qt.TextElideMode) """
        pass

    def setVerticalScrollMode(self, QAbstractItemView_ScrollMode): # real signature unknown; restored from __doc__
        """ setVerticalScrollMode(self, QAbstractItemView.ScrollMode) """
        pass

    def setViewportMargins(self, *args, **kwargs): # real signature unknown
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showDropIndicator(self): # real signature unknown; restored from __doc__
        """ showDropIndicator(self) -> bool """
        return False

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHintForColumn(self, p_int): # real signature unknown; restored from __doc__
        """ sizeHintForColumn(self, int) -> int """
        return 0

    def sizeHintForIndex(self, QModelIndex): # real signature unknown; restored from __doc__
        """ sizeHintForIndex(self, QModelIndex) -> QSize """
        pass

    def sizeHintForRow(self, p_int): # real signature unknown; restored from __doc__
        """ sizeHintForRow(self, int) -> int """
        return 0

    def startDrag(self, Union, Qt_DropActions=None, Qt_DropAction=None): # real signature unknown; restored from __doc__
        """ startDrag(self, Union[Qt.DropActions, Qt.DropAction]) """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QAbstractItemView.State """
        pass

    def tabKeyNavigation(self): # real signature unknown; restored from __doc__
        """ tabKeyNavigation(self) -> bool """
        return False

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def textElideMode(self): # real signature unknown; restored from __doc__
        """ textElideMode(self) -> Qt.TextElideMode """
        pass

    def timerEvent(self, QTimerEvent): # real signature unknown; restored from __doc__
        """ timerEvent(self, QTimerEvent) """
        pass

    def update(self, QModelIndex=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        update(self)
        update(self, QModelIndex)
        """
        pass

    def updateEditorData(self): # real signature unknown; restored from __doc__
        """ updateEditorData(self) """
        pass

    def updateEditorGeometries(self): # real signature unknown; restored from __doc__
        """ updateEditorGeometries(self) """
        pass

    def updateGeometries(self): # real signature unknown; restored from __doc__
        """ updateGeometries(self) """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def verticalOffset(self): # real signature unknown; restored from __doc__
        """ verticalOffset(self) -> int """
        return 0

    def verticalScrollbarAction(self, p_int): # real signature unknown; restored from __doc__
        """ verticalScrollbarAction(self, int) """
        pass

    def verticalScrollbarValueChanged(self, p_int): # real signature unknown; restored from __doc__
        """ verticalScrollbarValueChanged(self, int) """
        pass

    def verticalScrollMode(self): # real signature unknown; restored from __doc__
        """ verticalScrollMode(self) -> QAbstractItemView.ScrollMode """
        pass

    def viewOptions(self): # real signature unknown; restored from __doc__
        """ viewOptions(self) -> QStyleOptionViewItem """
        return QStyleOptionViewItem

    def viewportEntered(self): # real signature unknown; restored from __doc__
        """ viewportEntered(self) [signal] """
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

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    AboveItem = 1
    AllEditTriggers = 31
    AnimatingState = 6
    AnyKeyPressed = 16
    BelowItem = 2
    CollapsingState = 5
    ContiguousSelection = 4
    CurrentChanged = 1
    DoubleClicked = 2
    DragDrop = 3
    DraggingState = 1
    DragOnly = 1
    DragSelectingState = 2
    DropOnly = 2
    EditingState = 3
    EditKeyPressed = 8
    EnsureVisible = 0
    ExpandingState = 4
    ExtendedSelection = 3
    InternalMove = 4
    MoveDown = 1
    MoveEnd = 5
    MoveHome = 4
    MoveLeft = 2
    MoveNext = 8
    MovePageDown = 7
    MovePageUp = 6
    MovePrevious = 9
    MoveRight = 3
    MoveUp = 0
    MultiSelection = 2
    NoDragDrop = 0
    NoEditTriggers = 0
    NoSelection = 0
    NoState = 0
    OnItem = 0
    OnViewport = 3
    PositionAtBottom = 2
    PositionAtCenter = 3
    PositionAtTop = 1
    ScrollPerItem = 0
    ScrollPerPixel = 1
    SelectColumns = 2
    SelectedClicked = 4
    SelectItems = 0
    SelectRows = 1
    SingleSelection = 1


