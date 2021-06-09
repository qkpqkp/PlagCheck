# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QTextCursor(__sip.simplewrapper):
    """
    QTextCursor()
    QTextCursor(QTextDocument)
    QTextCursor(QTextFrame)
    QTextCursor(QTextBlock)
    QTextCursor(QTextCursor)
    """
    def anchor(self): # real signature unknown; restored from __doc__
        """ anchor(self) -> int """
        return 0

    def atBlockEnd(self): # real signature unknown; restored from __doc__
        """ atBlockEnd(self) -> bool """
        return False

    def atBlockStart(self): # real signature unknown; restored from __doc__
        """ atBlockStart(self) -> bool """
        return False

    def atEnd(self): # real signature unknown; restored from __doc__
        """ atEnd(self) -> bool """
        return False

    def atStart(self): # real signature unknown; restored from __doc__
        """ atStart(self) -> bool """
        return False

    def beginEditBlock(self): # real signature unknown; restored from __doc__
        """ beginEditBlock(self) """
        pass

    def block(self): # real signature unknown; restored from __doc__
        """ block(self) -> QTextBlock """
        return QTextBlock

    def blockCharFormat(self): # real signature unknown; restored from __doc__
        """ blockCharFormat(self) -> QTextCharFormat """
        return QTextCharFormat

    def blockFormat(self): # real signature unknown; restored from __doc__
        """ blockFormat(self) -> QTextBlockFormat """
        return QTextBlockFormat

    def blockNumber(self): # real signature unknown; restored from __doc__
        """ blockNumber(self) -> int """
        return 0

    def charFormat(self): # real signature unknown; restored from __doc__
        """ charFormat(self) -> QTextCharFormat """
        return QTextCharFormat

    def clearSelection(self): # real signature unknown; restored from __doc__
        """ clearSelection(self) """
        pass

    def columnNumber(self): # real signature unknown; restored from __doc__
        """ columnNumber(self) -> int """
        return 0

    def createList(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        createList(self, QTextListFormat) -> QTextList
        createList(self, QTextListFormat.Style) -> QTextList
        """
        return QTextList

    def currentFrame(self): # real signature unknown; restored from __doc__
        """ currentFrame(self) -> QTextFrame """
        return QTextFrame

    def currentList(self): # real signature unknown; restored from __doc__
        """ currentList(self) -> QTextList """
        return QTextList

    def currentTable(self): # real signature unknown; restored from __doc__
        """ currentTable(self) -> QTextTable """
        return QTextTable

    def deleteChar(self): # real signature unknown; restored from __doc__
        """ deleteChar(self) """
        pass

    def deletePreviousChar(self): # real signature unknown; restored from __doc__
        """ deletePreviousChar(self) """
        pass

    def document(self): # real signature unknown; restored from __doc__
        """ document(self) -> QTextDocument """
        return QTextDocument

    def endEditBlock(self): # real signature unknown; restored from __doc__
        """ endEditBlock(self) """
        pass

    def hasComplexSelection(self): # real signature unknown; restored from __doc__
        """ hasComplexSelection(self) -> bool """
        return False

    def hasSelection(self): # real signature unknown; restored from __doc__
        """ hasSelection(self) -> bool """
        return False

    def insertBlock(self, QTextBlockFormat=None, QTextCharFormat=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        insertBlock(self)
        insertBlock(self, QTextBlockFormat)
        insertBlock(self, QTextBlockFormat, QTextCharFormat)
        """
        pass

    def insertFragment(self, QTextDocumentFragment): # real signature unknown; restored from __doc__
        """ insertFragment(self, QTextDocumentFragment) """
        pass

    def insertFrame(self, QTextFrameFormat): # real signature unknown; restored from __doc__
        """ insertFrame(self, QTextFrameFormat) -> QTextFrame """
        return QTextFrame

    def insertHtml(self, p_str): # real signature unknown; restored from __doc__
        """ insertHtml(self, str) """
        pass

    def insertImage(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        insertImage(self, QTextImageFormat)
        insertImage(self, QTextImageFormat, QTextFrameFormat.Position)
        insertImage(self, str)
        insertImage(self, QImage, name: str = '')
        """
        pass

    def insertList(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        insertList(self, QTextListFormat) -> QTextList
        insertList(self, QTextListFormat.Style) -> QTextList
        """
        return QTextList

    def insertTable(self, p_int, p_int_1, QTextTableFormat=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        insertTable(self, int, int, QTextTableFormat) -> QTextTable
        insertTable(self, int, int) -> QTextTable
        """
        return QTextTable

    def insertText(self, p_str, QTextCharFormat=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        insertText(self, str)
        insertText(self, str, QTextCharFormat)
        """
        pass

    def isCopyOf(self, QTextCursor): # real signature unknown; restored from __doc__
        """ isCopyOf(self, QTextCursor) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def joinPreviousEditBlock(self): # real signature unknown; restored from __doc__
        """ joinPreviousEditBlock(self) """
        pass

    def keepPositionOnInsert(self): # real signature unknown; restored from __doc__
        """ keepPositionOnInsert(self) -> bool """
        return False

    def mergeBlockCharFormat(self, QTextCharFormat): # real signature unknown; restored from __doc__
        """ mergeBlockCharFormat(self, QTextCharFormat) """
        pass

    def mergeBlockFormat(self, QTextBlockFormat): # real signature unknown; restored from __doc__
        """ mergeBlockFormat(self, QTextBlockFormat) """
        pass

    def mergeCharFormat(self, QTextCharFormat): # real signature unknown; restored from __doc__
        """ mergeCharFormat(self, QTextCharFormat) """
        pass

    def movePosition(self, QTextCursor_MoveOperation, mode=None, n=1): # real signature unknown; restored from __doc__
        """ movePosition(self, QTextCursor.MoveOperation, mode: QTextCursor.MoveMode = QTextCursor.MoveAnchor, n: int = 1) -> bool """
        return False

    def position(self): # real signature unknown; restored from __doc__
        """ position(self) -> int """
        return 0

    def positionInBlock(self): # real signature unknown; restored from __doc__
        """ positionInBlock(self) -> int """
        return 0

    def removeSelectedText(self): # real signature unknown; restored from __doc__
        """ removeSelectedText(self) """
        pass

    def select(self, QTextCursor_SelectionType): # real signature unknown; restored from __doc__
        """ select(self, QTextCursor.SelectionType) """
        pass

    def selectedTableCells(self): # real signature unknown; restored from __doc__
        """ selectedTableCells(self) -> Tuple[int, int, int, int] """
        pass

    def selectedText(self): # real signature unknown; restored from __doc__
        """ selectedText(self) -> str """
        return ""

    def selection(self): # real signature unknown; restored from __doc__
        """ selection(self) -> QTextDocumentFragment """
        return QTextDocumentFragment

    def selectionEnd(self): # real signature unknown; restored from __doc__
        """ selectionEnd(self) -> int """
        return 0

    def selectionStart(self): # real signature unknown; restored from __doc__
        """ selectionStart(self) -> int """
        return 0

    def setBlockCharFormat(self, QTextCharFormat): # real signature unknown; restored from __doc__
        """ setBlockCharFormat(self, QTextCharFormat) """
        pass

    def setBlockFormat(self, QTextBlockFormat): # real signature unknown; restored from __doc__
        """ setBlockFormat(self, QTextBlockFormat) """
        pass

    def setCharFormat(self, QTextCharFormat): # real signature unknown; restored from __doc__
        """ setCharFormat(self, QTextCharFormat) """
        pass

    def setKeepPositionOnInsert(self, bool): # real signature unknown; restored from __doc__
        """ setKeepPositionOnInsert(self, bool) """
        pass

    def setPosition(self, p_int, mode=None): # real signature unknown; restored from __doc__
        """ setPosition(self, int, mode: QTextCursor.MoveMode = QTextCursor.MoveAnchor) """
        pass

    def setVerticalMovementX(self, p_int): # real signature unknown; restored from __doc__
        """ setVerticalMovementX(self, int) """
        pass

    def setVisualNavigation(self, bool): # real signature unknown; restored from __doc__
        """ setVisualNavigation(self, bool) """
        pass

    def swap(self, QTextCursor): # real signature unknown; restored from __doc__
        """ swap(self, QTextCursor) """
        pass

    def verticalMovementX(self): # real signature unknown; restored from __doc__
        """ verticalMovementX(self) -> int """
        return 0

    def visualNavigation(self): # real signature unknown; restored from __doc__
        """ visualNavigation(self) -> bool """
        return False

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    BlockUnderCursor = 2
    Document = 3
    Down = 12
    End = 11
    EndOfBlock = 15
    EndOfLine = 13
    EndOfWord = 14
    KeepAnchor = 1
    Left = 9
    LineUnderCursor = 1
    MoveAnchor = 0
    NextBlock = 16
    NextCell = 21
    NextCharacter = 17
    NextRow = 23
    NextWord = 18
    NoMove = 0
    PreviousBlock = 6
    PreviousCell = 22
    PreviousCharacter = 7
    PreviousRow = 24
    PreviousWord = 8
    Right = 19
    Start = 1
    StartOfBlock = 4
    StartOfLine = 3
    StartOfWord = 5
    Up = 2
    WordLeft = 10
    WordRight = 20
    WordUnderCursor = 0
    __hash__ = None


