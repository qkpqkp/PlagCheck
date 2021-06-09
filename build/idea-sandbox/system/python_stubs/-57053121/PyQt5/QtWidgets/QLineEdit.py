# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QWidget import QWidget

class QLineEdit(QWidget):
    """
    QLineEdit(parent: QWidget = None)
    QLineEdit(str, parent: QWidget = None)
    """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def addAction(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addAction(self, QAction)
        addAction(self, QAction, QLineEdit.ActionPosition)
        addAction(self, QIcon, QLineEdit.ActionPosition) -> QAction
        """
        return QAction

    def alignment(self): # real signature unknown; restored from __doc__
        """ alignment(self) -> Qt.Alignment """
        pass

    def backspace(self): # real signature unknown; restored from __doc__
        """ backspace(self) """
        pass

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

    def completer(self): # real signature unknown; restored from __doc__
        """ completer(self) -> QCompleter """
        return QCompleter

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, QContextMenuEvent): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, QContextMenuEvent) """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) """
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def createStandardContextMenu(self): # real signature unknown; restored from __doc__
        """ createStandardContextMenu(self) -> QMenu """
        return QMenu

    def cursorBackward(self, bool, steps=1): # real signature unknown; restored from __doc__
        """ cursorBackward(self, bool, steps: int = 1) """
        pass

    def cursorForward(self, bool, steps=1): # real signature unknown; restored from __doc__
        """ cursorForward(self, bool, steps: int = 1) """
        pass

    def cursorMoveStyle(self): # real signature unknown; restored from __doc__
        """ cursorMoveStyle(self) -> Qt.CursorMoveStyle """
        pass

    def cursorPosition(self): # real signature unknown; restored from __doc__
        """ cursorPosition(self) -> int """
        return 0

    def cursorPositionAt(self, QPoint): # real signature unknown; restored from __doc__
        """ cursorPositionAt(self, QPoint) -> int """
        return 0

    def cursorPositionChanged(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ cursorPositionChanged(self, int, int) [signal] """
        pass

    def cursorRect(self): # real signature unknown; restored from __doc__
        """ cursorRect(self) -> QRect """
        pass

    def cursorWordBackward(self, bool): # real signature unknown; restored from __doc__
        """ cursorWordBackward(self, bool) """
        pass

    def cursorWordForward(self, bool): # real signature unknown; restored from __doc__
        """ cursorWordForward(self, bool) """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def cut(self): # real signature unknown; restored from __doc__
        """ cut(self) """
        pass

    def del_(self): # real signature unknown; restored from __doc__
        """ del_(self) """
        pass

    def deselect(self): # real signature unknown; restored from __doc__
        """ deselect(self) """
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def displayText(self): # real signature unknown; restored from __doc__
        """ displayText(self) -> str """
        return ""

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

    def dropEvent(self, QDropEvent): # real signature unknown; restored from __doc__
        """ dropEvent(self, QDropEvent) """
        pass

    def echoMode(self): # real signature unknown; restored from __doc__
        """ echoMode(self) -> QLineEdit.EchoMode """
        pass

    def editingFinished(self): # real signature unknown; restored from __doc__
        """ editingFinished(self) [signal] """
        pass

    def end(self, bool): # real signature unknown; restored from __doc__
        """ end(self, bool) """
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def focusInEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ focusInEvent(self, QFocusEvent) """
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, QFocusEvent) """
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def getTextMargins(self): # real signature unknown; restored from __doc__
        """ getTextMargins(self) -> Tuple[int, int, int, int] """
        pass

    def hasAcceptableInput(self): # real signature unknown; restored from __doc__
        """ hasAcceptableInput(self) -> bool """
        return False

    def hasFrame(self): # real signature unknown; restored from __doc__
        """ hasFrame(self) -> bool """
        return False

    def hasSelectedText(self): # real signature unknown; restored from __doc__
        """ hasSelectedText(self) -> bool """
        return False

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def home(self, bool): # real signature unknown; restored from __doc__
        """ home(self, bool) """
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def initStyleOption(self, QStyleOptionFrame): # real signature unknown; restored from __doc__
        """ initStyleOption(self, QStyleOptionFrame) """
        pass

    def inputMask(self): # real signature unknown; restored from __doc__
        """ inputMask(self) -> str """
        return ""

    def inputMethodEvent(self, QInputMethodEvent): # real signature unknown; restored from __doc__
        """ inputMethodEvent(self, QInputMethodEvent) """
        pass

    def inputMethodQuery(self, Qt_InputMethodQuery, Any=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        inputMethodQuery(self, Qt.InputMethodQuery) -> Any
        inputMethodQuery(self, Qt.InputMethodQuery, Any) -> Any
        """
        pass

    def inputRejected(self): # real signature unknown; restored from __doc__
        """ inputRejected(self) [signal] """
        pass

    def insert(self, p_str): # real signature unknown; restored from __doc__
        """ insert(self, str) """
        pass

    def isClearButtonEnabled(self): # real signature unknown; restored from __doc__
        """ isClearButtonEnabled(self) -> bool """
        return False

    def isModified(self): # real signature unknown; restored from __doc__
        """ isModified(self) -> bool """
        return False

    def isReadOnly(self): # real signature unknown; restored from __doc__
        """ isReadOnly(self) -> bool """
        return False

    def isRedoAvailable(self): # real signature unknown; restored from __doc__
        """ isRedoAvailable(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isUndoAvailable(self): # real signature unknown; restored from __doc__
        """ isUndoAvailable(self) -> bool """
        return False

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, QKeyEvent) """
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def maxLength(self): # real signature unknown; restored from __doc__
        """ maxLength(self) -> int """
        return 0

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> QSize """
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

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ paintEvent(self, QPaintEvent) """
        pass

    def paste(self): # real signature unknown; restored from __doc__
        """ paste(self) """
        pass

    def placeholderText(self): # real signature unknown; restored from __doc__
        """ placeholderText(self) -> str """
        return ""

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def redo(self): # real signature unknown; restored from __doc__
        """ redo(self) """
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def returnPressed(self): # real signature unknown; restored from __doc__
        """ returnPressed(self) [signal] """
        pass

    def selectAll(self): # real signature unknown; restored from __doc__
        """ selectAll(self) """
        pass

    def selectedText(self): # real signature unknown; restored from __doc__
        """ selectedText(self) -> str """
        return ""

    def selectionChanged(self): # real signature unknown; restored from __doc__
        """ selectionChanged(self) [signal] """
        pass

    def selectionEnd(self): # real signature unknown; restored from __doc__
        """ selectionEnd(self) -> int """
        return 0

    def selectionLength(self): # real signature unknown; restored from __doc__
        """ selectionLength(self) -> int """
        return 0

    def selectionStart(self): # real signature unknown; restored from __doc__
        """ selectionStart(self) -> int """
        return 0

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAlignment(self, Union, Qt_Alignment=None, Qt_AlignmentFlag=None): # real signature unknown; restored from __doc__
        """ setAlignment(self, Union[Qt.Alignment, Qt.AlignmentFlag]) """
        pass

    def setClearButtonEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setClearButtonEnabled(self, bool) """
        pass

    def setCompleter(self, QCompleter): # real signature unknown; restored from __doc__
        """ setCompleter(self, QCompleter) """
        pass

    def setCursorMoveStyle(self, Qt_CursorMoveStyle): # real signature unknown; restored from __doc__
        """ setCursorMoveStyle(self, Qt.CursorMoveStyle) """
        pass

    def setCursorPosition(self, p_int): # real signature unknown; restored from __doc__
        """ setCursorPosition(self, int) """
        pass

    def setDragEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setDragEnabled(self, bool) """
        pass

    def setEchoMode(self, QLineEdit_EchoMode): # real signature unknown; restored from __doc__
        """ setEchoMode(self, QLineEdit.EchoMode) """
        pass

    def setFrame(self, bool): # real signature unknown; restored from __doc__
        """ setFrame(self, bool) """
        pass

    def setInputMask(self, p_str): # real signature unknown; restored from __doc__
        """ setInputMask(self, str) """
        pass

    def setMaxLength(self, p_int): # real signature unknown; restored from __doc__
        """ setMaxLength(self, int) """
        pass

    def setModified(self, bool): # real signature unknown; restored from __doc__
        """ setModified(self, bool) """
        pass

    def setPlaceholderText(self, p_str): # real signature unknown; restored from __doc__
        """ setPlaceholderText(self, str) """
        pass

    def setReadOnly(self, bool): # real signature unknown; restored from __doc__
        """ setReadOnly(self, bool) """
        pass

    def setSelection(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ setSelection(self, int, int) """
        pass

    def setText(self, p_str): # real signature unknown; restored from __doc__
        """ setText(self, str) """
        pass

    def setTextMargins(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setTextMargins(self, int, int, int, int)
        setTextMargins(self, QMargins)
        """
        pass

    def setValidator(self, QValidator): # real signature unknown; restored from __doc__
        """ setValidator(self, QValidator) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def textChanged(self, p_str): # real signature unknown; restored from __doc__
        """ textChanged(self, str) [signal] """
        pass

    def textEdited(self, p_str): # real signature unknown; restored from __doc__
        """ textEdited(self, str) [signal] """
        pass

    def textMargins(self): # real signature unknown; restored from __doc__
        """ textMargins(self) -> QMargins """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def undo(self): # real signature unknown; restored from __doc__
        """ undo(self) """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def validator(self): # real signature unknown; restored from __doc__
        """ validator(self) -> QValidator """
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    LeadingPosition = 0
    NoEcho = 1
    Normal = 0
    Password = 2
    PasswordEchoOnEdit = 3
    TrailingPosition = 1


