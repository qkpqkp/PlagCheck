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

class QPlainTextEdit(QAbstractScrollArea):
    """
    QPlainTextEdit(parent: QWidget = None)
    QPlainTextEdit(str, parent: QWidget = None)
    """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def anchorAt(self, QPoint): # real signature unknown; restored from __doc__
        """ anchorAt(self, QPoint) -> str """
        return ""

    def appendHtml(self, p_str): # real signature unknown; restored from __doc__
        """ appendHtml(self, str) """
        pass

    def appendPlainText(self, p_str): # real signature unknown; restored from __doc__
        """ appendPlainText(self, str) """
        pass

    def backgroundVisible(self): # real signature unknown; restored from __doc__
        """ backgroundVisible(self) -> bool """
        return False

    def blockBoundingGeometry(self, QTextBlock): # real signature unknown; restored from __doc__
        """ blockBoundingGeometry(self, QTextBlock) -> QRectF """
        pass

    def blockBoundingRect(self, QTextBlock): # real signature unknown; restored from __doc__
        """ blockBoundingRect(self, QTextBlock) -> QRectF """
        pass

    def blockCount(self): # real signature unknown; restored from __doc__
        """ blockCount(self) -> int """
        return 0

    def blockCountChanged(self, p_int): # real signature unknown; restored from __doc__
        """ blockCountChanged(self, int) [signal] """
        pass

    def canInsertFromMimeData(self, QMimeData): # real signature unknown; restored from __doc__
        """ canInsertFromMimeData(self, QMimeData) -> bool """
        return False

    def canPaste(self): # real signature unknown; restored from __doc__
        """ canPaste(self) -> bool """
        return False

    def centerCursor(self): # real signature unknown; restored from __doc__
        """ centerCursor(self) """
        pass

    def centerOnScroll(self): # real signature unknown; restored from __doc__
        """ centerOnScroll(self) -> bool """
        return False

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ changeEvent(self, QEvent) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contentOffset(self): # real signature unknown; restored from __doc__
        """ contentOffset(self) -> QPointF """
        pass

    def contextMenuEvent(self, QContextMenuEvent): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, QContextMenuEvent) """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) """
        pass

    def copyAvailable(self, bool): # real signature unknown; restored from __doc__
        """ copyAvailable(self, bool) [signal] """
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def createMimeDataFromSelection(self): # real signature unknown; restored from __doc__
        """ createMimeDataFromSelection(self) -> QMimeData """
        pass

    def createStandardContextMenu(self, QPoint=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        createStandardContextMenu(self) -> QMenu
        createStandardContextMenu(self, QPoint) -> QMenu
        """
        return QMenu

    def currentCharFormat(self): # real signature unknown; restored from __doc__
        """ currentCharFormat(self) -> QTextCharFormat """
        pass

    def cursorForPosition(self, QPoint): # real signature unknown; restored from __doc__
        """ cursorForPosition(self, QPoint) -> QTextCursor """
        pass

    def cursorPositionChanged(self): # real signature unknown; restored from __doc__
        """ cursorPositionChanged(self) [signal] """
        pass

    def cursorRect(self, QTextCursor=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        cursorRect(self, QTextCursor) -> QRect
        cursorRect(self) -> QRect
        """
        pass

    def cursorWidth(self): # real signature unknown; restored from __doc__
        """ cursorWidth(self) -> int """
        return 0

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def cut(self): # real signature unknown; restored from __doc__
        """ cut(self) """
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def document(self): # real signature unknown; restored from __doc__
        """ document(self) -> QTextDocument """
        pass

    def documentTitle(self): # real signature unknown; restored from __doc__
        """ documentTitle(self) -> str """
        return ""

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

    def ensureCursorVisible(self): # real signature unknown; restored from __doc__
        """ ensureCursorVisible(self) """
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def eventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def extraSelections(self): # real signature unknown; restored from __doc__
        """ extraSelections(self) -> List[QTextEdit.ExtraSelection] """
        return []

    def find(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        find(self, str, options: Union[QTextDocument.FindFlags, QTextDocument.FindFlag] = QTextDocument.FindFlags()) -> bool
        find(self, QRegExp, options: Union[QTextDocument.FindFlags, QTextDocument.FindFlag] = QTextDocument.FindFlags()) -> bool
        """
        pass

    def firstVisibleBlock(self): # real signature unknown; restored from __doc__
        """ firstVisibleBlock(self) -> QTextBlock """
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

    def getPaintContext(self): # real signature unknown; restored from __doc__
        """ getPaintContext(self) -> QAbstractTextDocumentLayout.PaintContext """
        pass

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def initStyleOption(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, QInputMethodEvent): # real signature unknown; restored from __doc__
        """ inputMethodEvent(self, QInputMethodEvent) """
        pass

    def inputMethodQuery(self, Qt_InputMethodQuery, Any=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        inputMethodQuery(self, Qt.InputMethodQuery) -> Any
        inputMethodQuery(self, Qt.InputMethodQuery, Any) -> Any
        """
        pass

    def insertFromMimeData(self, QMimeData): # real signature unknown; restored from __doc__
        """ insertFromMimeData(self, QMimeData) """
        pass

    def insertPlainText(self, p_str): # real signature unknown; restored from __doc__
        """ insertPlainText(self, str) """
        pass

    def isReadOnly(self): # real signature unknown; restored from __doc__
        """ isReadOnly(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isUndoRedoEnabled(self): # real signature unknown; restored from __doc__
        """ isUndoRedoEnabled(self) -> bool """
        return False

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, QKeyEvent) """
        pass

    def keyReleaseEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, QKeyEvent) """
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def lineWrapMode(self): # real signature unknown; restored from __doc__
        """ lineWrapMode(self) -> QPlainTextEdit.LineWrapMode """
        pass

    def loadResource(self, p_int, QUrl): # real signature unknown; restored from __doc__
        """ loadResource(self, int, QUrl) -> Any """
        pass

    def maximumBlockCount(self): # real signature unknown; restored from __doc__
        """ maximumBlockCount(self) -> int """
        return 0

    def mergeCurrentCharFormat(self, QTextCharFormat): # real signature unknown; restored from __doc__
        """ mergeCurrentCharFormat(self, QTextCharFormat) """
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def modificationChanged(self, bool): # real signature unknown; restored from __doc__
        """ modificationChanged(self, bool) [signal] """
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

    def moveCursor(self, QTextCursor_MoveOperation, mode=None): # real signature unknown; restored from __doc__
        """ moveCursor(self, QTextCursor.MoveOperation, mode: QTextCursor.MoveMode = QTextCursor.MoveAnchor) """
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def overwriteMode(self): # real signature unknown; restored from __doc__
        """ overwriteMode(self) -> bool """
        return False

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ paintEvent(self, QPaintEvent) """
        pass

    def paste(self): # real signature unknown; restored from __doc__
        """ paste(self) """
        pass

    def placeholderText(self): # real signature unknown; restored from __doc__
        """ placeholderText(self) -> str """
        return ""

    def print(self, QPagedPaintDevice): # real signature unknown; restored from __doc__
        """ print(self, QPagedPaintDevice) """
        pass

    def print_(self, QPagedPaintDevice): # real signature unknown; restored from __doc__
        """ print_(self, QPagedPaintDevice) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def redo(self): # real signature unknown; restored from __doc__
        """ redo(self) """
        pass

    def redoAvailable(self, bool): # real signature unknown; restored from __doc__
        """ redoAvailable(self, bool) [signal] """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ resizeEvent(self, QResizeEvent) """
        pass

    def scrollContentsBy(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ scrollContentsBy(self, int, int) """
        pass

    def selectAll(self): # real signature unknown; restored from __doc__
        """ selectAll(self) """
        pass

    def selectionChanged(self): # real signature unknown; restored from __doc__
        """ selectionChanged(self) [signal] """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setBackgroundVisible(self, bool): # real signature unknown; restored from __doc__
        """ setBackgroundVisible(self, bool) """
        pass

    def setCenterOnScroll(self, bool): # real signature unknown; restored from __doc__
        """ setCenterOnScroll(self, bool) """
        pass

    def setCurrentCharFormat(self, QTextCharFormat): # real signature unknown; restored from __doc__
        """ setCurrentCharFormat(self, QTextCharFormat) """
        pass

    def setCursorWidth(self, p_int): # real signature unknown; restored from __doc__
        """ setCursorWidth(self, int) """
        pass

    def setDocument(self, QTextDocument): # real signature unknown; restored from __doc__
        """ setDocument(self, QTextDocument) """
        pass

    def setDocumentTitle(self, p_str): # real signature unknown; restored from __doc__
        """ setDocumentTitle(self, str) """
        pass

    def setExtraSelections(self, Iterable, QTextEdit_ExtraSelection=None): # real signature unknown; restored from __doc__
        """ setExtraSelections(self, Iterable[QTextEdit.ExtraSelection]) """
        pass

    def setLineWrapMode(self, QPlainTextEdit_LineWrapMode): # real signature unknown; restored from __doc__
        """ setLineWrapMode(self, QPlainTextEdit.LineWrapMode) """
        pass

    def setMaximumBlockCount(self, p_int): # real signature unknown; restored from __doc__
        """ setMaximumBlockCount(self, int) """
        pass

    def setOverwriteMode(self, bool): # real signature unknown; restored from __doc__
        """ setOverwriteMode(self, bool) """
        pass

    def setPlaceholderText(self, p_str): # real signature unknown; restored from __doc__
        """ setPlaceholderText(self, str) """
        pass

    def setPlainText(self, p_str): # real signature unknown; restored from __doc__
        """ setPlainText(self, str) """
        pass

    def setReadOnly(self, bool): # real signature unknown; restored from __doc__
        """ setReadOnly(self, bool) """
        pass

    def setTabChangesFocus(self, bool): # real signature unknown; restored from __doc__
        """ setTabChangesFocus(self, bool) """
        pass

    def setTabStopDistance(self, p_float): # real signature unknown; restored from __doc__
        """ setTabStopDistance(self, float) """
        pass

    def setTabStopWidth(self, p_int): # real signature unknown; restored from __doc__
        """ setTabStopWidth(self, int) """
        pass

    def setTextCursor(self, QTextCursor): # real signature unknown; restored from __doc__
        """ setTextCursor(self, QTextCursor) """
        pass

    def setTextInteractionFlags(self, Union, Qt_TextInteractionFlags=None, Qt_TextInteractionFlag=None): # real signature unknown; restored from __doc__
        """ setTextInteractionFlags(self, Union[Qt.TextInteractionFlags, Qt.TextInteractionFlag]) """
        pass

    def setUndoRedoEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setUndoRedoEnabled(self, bool) """
        pass

    def setViewportMargins(self, *args, **kwargs): # real signature unknown
        pass

    def setWordWrapMode(self, QTextOption_WrapMode): # real signature unknown; restored from __doc__
        """ setWordWrapMode(self, QTextOption.WrapMode) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, QShowEvent): # real signature unknown; restored from __doc__
        """ showEvent(self, QShowEvent) """
        pass

    def tabChangesFocus(self): # real signature unknown; restored from __doc__
        """ tabChangesFocus(self) -> bool """
        return False

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def tabStopDistance(self): # real signature unknown; restored from __doc__
        """ tabStopDistance(self) -> float """
        return 0.0

    def tabStopWidth(self): # real signature unknown; restored from __doc__
        """ tabStopWidth(self) -> int """
        return 0

    def textChanged(self): # real signature unknown; restored from __doc__
        """ textChanged(self) [signal] """
        pass

    def textCursor(self): # real signature unknown; restored from __doc__
        """ textCursor(self) -> QTextCursor """
        pass

    def textInteractionFlags(self): # real signature unknown; restored from __doc__
        """ textInteractionFlags(self) -> Qt.TextInteractionFlags """
        pass

    def timerEvent(self, QTimerEvent): # real signature unknown; restored from __doc__
        """ timerEvent(self, QTimerEvent) """
        pass

    def toPlainText(self): # real signature unknown; restored from __doc__
        """ toPlainText(self) -> str """
        return ""

    def undo(self): # real signature unknown; restored from __doc__
        """ undo(self) """
        pass

    def undoAvailable(self, bool): # real signature unknown; restored from __doc__
        """ undoAvailable(self, bool) [signal] """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def updateRequest(self, QRect, p_int): # real signature unknown; restored from __doc__
        """ updateRequest(self, QRect, int) [signal] """
        pass

    def viewportEvent(self, *args, **kwargs): # real signature unknown
        pass

    def viewportMargins(self, *args, **kwargs): # real signature unknown
        pass

    def viewportSizeHint(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, QWheelEvent): # real signature unknown; restored from __doc__
        """ wheelEvent(self, QWheelEvent) """
        pass

    def wordWrapMode(self): # real signature unknown; restored from __doc__
        """ wordWrapMode(self) -> QTextOption.WrapMode """
        pass

    def zoomIn(self, range=1): # real signature unknown; restored from __doc__
        """ zoomIn(self, range: int = 1) """
        pass

    def zoomOut(self, range=1): # real signature unknown; restored from __doc__
        """ zoomOut(self, range: int = 1) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    NoWrap = 0
    WidgetWidth = 1


