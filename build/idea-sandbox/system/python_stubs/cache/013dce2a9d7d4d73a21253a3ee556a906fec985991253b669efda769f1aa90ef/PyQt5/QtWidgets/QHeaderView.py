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

class QHeaderView(QAbstractItemView):
    """ QHeaderView(Qt.Orientation, parent: QWidget = None) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def cascadingSectionResizes(self): # real signature unknown; restored from __doc__
        """ cascadingSectionResizes(self) -> bool """
        return False

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEditor(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def commitData(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

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

    def defaultAlignment(self): # real signature unknown; restored from __doc__
        """ defaultAlignment(self) -> Qt.Alignment """
        pass

    def defaultSectionSize(self): # real signature unknown; restored from __doc__
        """ defaultSectionSize(self) -> int """
        return 0

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

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

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

    def geometriesChanged(self): # real signature unknown; restored from __doc__
        """ geometriesChanged(self) [signal] """
        pass

    def headerDataChanged(self, Qt_Orientation, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ headerDataChanged(self, Qt.Orientation, int, int) """
        pass

    def hiddenSectionCount(self): # real signature unknown; restored from __doc__
        """ hiddenSectionCount(self) -> int """
        return 0

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def hideSection(self, p_int): # real signature unknown; restored from __doc__
        """ hideSection(self, int) """
        pass

    def highlightSections(self): # real signature unknown; restored from __doc__
        """ highlightSections(self) -> bool """
        return False

    def horizontalOffset(self): # real signature unknown; restored from __doc__
        """ horizontalOffset(self) -> int """
        return 0

    def horizontalScrollbarAction(self, *args, **kwargs): # real signature unknown
        pass

    def horizontalScrollbarValueChanged(self, *args, **kwargs): # real signature unknown
        pass

    def indexAt(self, QPoint): # real signature unknown; restored from __doc__
        """ indexAt(self, QPoint) -> QModelIndex """
        pass

    def initialize(self): # real signature unknown; restored from __doc__
        """ initialize(self) """
        pass

    def initializeSections(self, p_int=None, p_int_1=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        initializeSections(self)
        initializeSections(self, int, int)
        """
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def initStyleOption(self, QStyleOptionHeader): # real signature unknown; restored from __doc__
        """ initStyleOption(self, QStyleOptionHeader) """
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isFirstSectionMovable(self): # real signature unknown; restored from __doc__
        """ isFirstSectionMovable(self) -> bool """
        return False

    def isIndexHidden(self, QModelIndex): # real signature unknown; restored from __doc__
        """ isIndexHidden(self, QModelIndex) -> bool """
        return False

    def isSectionHidden(self, p_int): # real signature unknown; restored from __doc__
        """ isSectionHidden(self, int) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isSortIndicatorShown(self): # real signature unknown; restored from __doc__
        """ isSortIndicatorShown(self) -> bool """
        return False

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def length(self): # real signature unknown; restored from __doc__
        """ length(self) -> int """
        return 0

    def logicalIndex(self, p_int): # real signature unknown; restored from __doc__
        """ logicalIndex(self, int) -> int """
        return 0

    def logicalIndexAt(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        logicalIndexAt(self, int) -> int
        logicalIndexAt(self, int, int) -> int
        logicalIndexAt(self, QPoint) -> int
        """
        return 0

    def maximumSectionSize(self): # real signature unknown; restored from __doc__
        """ maximumSectionSize(self) -> int """
        return 0

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def minimumSectionSize(self): # real signature unknown; restored from __doc__
        """ minimumSectionSize(self) -> int """
        return 0

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

    def moveSection(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ moveSection(self, int, int) """
        pass

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def offset(self): # real signature unknown; restored from __doc__
        """ offset(self) -> int """
        return 0

    def orientation(self): # real signature unknown; restored from __doc__
        """ orientation(self) -> Qt.Orientation """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ paintEvent(self, QPaintEvent) """
        pass

    def paintSection(self, QPainter, QRect, p_int): # real signature unknown; restored from __doc__
        """ paintSection(self, QPainter, QRect, int) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) """
        pass

    def resetDefaultSectionSize(self): # real signature unknown; restored from __doc__
        """ resetDefaultSectionSize(self) """
        pass

    def resizeContentsPrecision(self): # real signature unknown; restored from __doc__
        """ resizeContentsPrecision(self) -> int """
        return 0

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def resizeSection(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ resizeSection(self, int, int) """
        pass

    def resizeSections(self, QHeaderView_ResizeMode=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        resizeSections(self)
        resizeSections(self, QHeaderView.ResizeMode)
        """
        pass

    def restoreState(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ restoreState(self, Union[QByteArray, bytes, bytearray]) -> bool """
        return False

    def rowsAboutToBeRemoved(self, *args, **kwargs): # real signature unknown
        pass

    def rowsInserted(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ rowsInserted(self, QModelIndex, int, int) """
        pass

    def saveState(self): # real signature unknown; restored from __doc__
        """ saveState(self) -> QByteArray """
        pass

    def scheduleDelayedItemsLayout(self, *args, **kwargs): # real signature unknown
        pass

    def scrollContentsBy(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ scrollContentsBy(self, int, int) """
        pass

    def scrollDirtyRegion(self, *args, **kwargs): # real signature unknown
        pass

    def scrollTo(self, QModelIndex, QAbstractItemView_ScrollHint): # real signature unknown; restored from __doc__
        """ scrollTo(self, QModelIndex, QAbstractItemView.ScrollHint) """
        pass

    def sectionClicked(self, p_int): # real signature unknown; restored from __doc__
        """ sectionClicked(self, int) [signal] """
        pass

    def sectionCountChanged(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ sectionCountChanged(self, int, int) [signal] """
        pass

    def sectionDoubleClicked(self, p_int): # real signature unknown; restored from __doc__
        """ sectionDoubleClicked(self, int) [signal] """
        pass

    def sectionEntered(self, p_int): # real signature unknown; restored from __doc__
        """ sectionEntered(self, int) [signal] """
        pass

    def sectionHandleDoubleClicked(self, p_int): # real signature unknown; restored from __doc__
        """ sectionHandleDoubleClicked(self, int) [signal] """
        pass

    def sectionMoved(self, p_int, p_int_1, p_int_2): # real signature unknown; restored from __doc__
        """ sectionMoved(self, int, int, int) [signal] """
        pass

    def sectionPosition(self, p_int): # real signature unknown; restored from __doc__
        """ sectionPosition(self, int) -> int """
        return 0

    def sectionPressed(self, p_int): # real signature unknown; restored from __doc__
        """ sectionPressed(self, int) [signal] """
        pass

    def sectionResized(self, p_int, p_int_1, p_int_2): # real signature unknown; restored from __doc__
        """ sectionResized(self, int, int, int) [signal] """
        pass

    def sectionResizeMode(self, p_int): # real signature unknown; restored from __doc__
        """ sectionResizeMode(self, int) -> QHeaderView.ResizeMode """
        pass

    def sectionsAboutToBeRemoved(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ sectionsAboutToBeRemoved(self, QModelIndex, int, int) """
        pass

    def sectionsClickable(self): # real signature unknown; restored from __doc__
        """ sectionsClickable(self) -> bool """
        return False

    def sectionsHidden(self): # real signature unknown; restored from __doc__
        """ sectionsHidden(self) -> bool """
        return False

    def sectionsInserted(self, QModelIndex, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ sectionsInserted(self, QModelIndex, int, int) """
        pass

    def sectionSize(self, p_int): # real signature unknown; restored from __doc__
        """ sectionSize(self, int) -> int """
        return 0

    def sectionSizeFromContents(self, p_int): # real signature unknown; restored from __doc__
        """ sectionSizeFromContents(self, int) -> QSize """
        pass

    def sectionSizeHint(self, p_int): # real signature unknown; restored from __doc__
        """ sectionSizeHint(self, int) -> int """
        return 0

    def sectionsMovable(self): # real signature unknown; restored from __doc__
        """ sectionsMovable(self) -> bool """
        return False

    def sectionsMoved(self): # real signature unknown; restored from __doc__
        """ sectionsMoved(self) -> bool """
        return False

    def sectionViewportPosition(self, p_int): # real signature unknown; restored from __doc__
        """ sectionViewportPosition(self, int) -> int """
        return 0

    def selectedIndexes(self, *args, **kwargs): # real signature unknown
        pass

    def selectionChanged(self, *args, **kwargs): # real signature unknown
        pass

    def selectionCommand(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCascadingSectionResizes(self, bool): # real signature unknown; restored from __doc__
        """ setCascadingSectionResizes(self, bool) """
        pass

    def setDefaultAlignment(self, Union, Qt_Alignment=None, Qt_AlignmentFlag=None): # real signature unknown; restored from __doc__
        """ setDefaultAlignment(self, Union[Qt.Alignment, Qt.AlignmentFlag]) """
        pass

    def setDefaultSectionSize(self, p_int): # real signature unknown; restored from __doc__
        """ setDefaultSectionSize(self, int) """
        pass

    def setDirtyRegion(self, *args, **kwargs): # real signature unknown
        pass

    def setFirstSectionMovable(self, bool): # real signature unknown; restored from __doc__
        """ setFirstSectionMovable(self, bool) """
        pass

    def setHighlightSections(self, bool): # real signature unknown; restored from __doc__
        """ setHighlightSections(self, bool) """
        pass

    def setMaximumSectionSize(self, p_int): # real signature unknown; restored from __doc__
        """ setMaximumSectionSize(self, int) """
        pass

    def setMinimumSectionSize(self, p_int): # real signature unknown; restored from __doc__
        """ setMinimumSectionSize(self, int) """
        pass

    def setModel(self, QAbstractItemModel): # real signature unknown; restored from __doc__
        """ setModel(self, QAbstractItemModel) """
        pass

    def setOffset(self, p_int): # real signature unknown; restored from __doc__
        """ setOffset(self, int) """
        pass

    def setOffsetToLastSection(self): # real signature unknown; restored from __doc__
        """ setOffsetToLastSection(self) """
        pass

    def setOffsetToSectionPosition(self, p_int): # real signature unknown; restored from __doc__
        """ setOffsetToSectionPosition(self, int) """
        pass

    def setResizeContentsPrecision(self, p_int): # real signature unknown; restored from __doc__
        """ setResizeContentsPrecision(self, int) """
        pass

    def setSectionHidden(self, p_int, bool): # real signature unknown; restored from __doc__
        """ setSectionHidden(self, int, bool) """
        pass

    def setSectionResizeMode(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setSectionResizeMode(self, int, QHeaderView.ResizeMode)
        setSectionResizeMode(self, QHeaderView.ResizeMode)
        """
        pass

    def setSectionsClickable(self, bool): # real signature unknown; restored from __doc__
        """ setSectionsClickable(self, bool) """
        pass

    def setSectionsMovable(self, bool): # real signature unknown; restored from __doc__
        """ setSectionsMovable(self, bool) """
        pass

    def setSelection(self, QRect, Union, QItemSelectionModel_SelectionFlags=None, QItemSelectionModel_SelectionFlag=None): # real signature unknown; restored from __doc__
        """ setSelection(self, QRect, Union[QItemSelectionModel.SelectionFlags, QItemSelectionModel.SelectionFlag]) """
        pass

    def setSortIndicator(self, p_int, Qt_SortOrder): # real signature unknown; restored from __doc__
        """ setSortIndicator(self, int, Qt.SortOrder) """
        pass

    def setSortIndicatorShown(self, bool): # real signature unknown; restored from __doc__
        """ setSortIndicatorShown(self, bool) """
        pass

    def setState(self, *args, **kwargs): # real signature unknown
        pass

    def setStretchLastSection(self, bool): # real signature unknown; restored from __doc__
        """ setStretchLastSection(self, bool) """
        pass

    def setViewportMargins(self, *args, **kwargs): # real signature unknown
        pass

    def setVisible(self, bool): # real signature unknown; restored from __doc__
        """ setVisible(self, bool) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def showSection(self, p_int): # real signature unknown; restored from __doc__
        """ showSection(self, int) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def sortIndicatorChanged(self, p_int, Qt_SortOrder): # real signature unknown; restored from __doc__
        """ sortIndicatorChanged(self, int, Qt.SortOrder) [signal] """
        pass

    def sortIndicatorOrder(self): # real signature unknown; restored from __doc__
        """ sortIndicatorOrder(self) -> Qt.SortOrder """
        pass

    def sortIndicatorSection(self): # real signature unknown; restored from __doc__
        """ sortIndicatorSection(self) -> int """
        return 0

    def startDrag(self, *args, **kwargs): # real signature unknown
        pass

    def state(self, *args, **kwargs): # real signature unknown
        pass

    def stretchLastSection(self): # real signature unknown; restored from __doc__
        """ stretchLastSection(self) -> bool """
        return False

    def stretchSectionCount(self): # real signature unknown; restored from __doc__
        """ stretchSectionCount(self) -> int """
        return 0

    def swapSections(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ swapSections(self, int, int) """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
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

    def updateSection(self, p_int): # real signature unknown; restored from __doc__
        """ updateSection(self, int) """
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

    def viewportSizeHint(self, *args, **kwargs): # real signature unknown
        pass

    def visualIndex(self, p_int): # real signature unknown; restored from __doc__
        """ visualIndex(self, int) -> int """
        return 0

    def visualIndexAt(self, p_int): # real signature unknown; restored from __doc__
        """ visualIndexAt(self, int) -> int """
        return 0

    def visualRect(self, QModelIndex): # real signature unknown; restored from __doc__
        """ visualRect(self, QModelIndex) -> QRect """
        pass

    def visualRegionForSelection(self, QItemSelection): # real signature unknown; restored from __doc__
        """ visualRegionForSelection(self, QItemSelection) -> QRegion """
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, Qt_Orientation, parent=None): # real signature unknown; restored from __doc__
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    Custom = 2
    Fixed = 2
    Interactive = 0
    ResizeToContents = 3
    Stretch = 1


