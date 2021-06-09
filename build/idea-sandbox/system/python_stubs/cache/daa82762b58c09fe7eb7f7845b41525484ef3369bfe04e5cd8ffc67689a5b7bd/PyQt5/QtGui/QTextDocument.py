# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QTextDocument(__PyQt5_QtCore.QObject):
    """
    QTextDocument(parent: QObject = None)
    QTextDocument(str, parent: QObject = None)
    """
    def addResource(self, p_int, QUrl, Any): # real signature unknown; restored from __doc__
        """ addResource(self, int, QUrl, Any) """
        pass

    def adjustSize(self): # real signature unknown; restored from __doc__
        """ adjustSize(self) """
        pass

    def allFormats(self): # real signature unknown; restored from __doc__
        """ allFormats(self) -> List[QTextFormat] """
        return []

    def availableRedoSteps(self): # real signature unknown; restored from __doc__
        """ availableRedoSteps(self) -> int """
        return 0

    def availableUndoSteps(self): # real signature unknown; restored from __doc__
        """ availableUndoSteps(self) -> int """
        return 0

    def baseUrl(self): # real signature unknown; restored from __doc__
        """ baseUrl(self) -> QUrl """
        pass

    def baseUrlChanged(self, QUrl): # real signature unknown; restored from __doc__
        """ baseUrlChanged(self, QUrl) [signal] """
        pass

    def begin(self): # real signature unknown; restored from __doc__
        """ begin(self) -> QTextBlock """
        return QTextBlock

    def blockCount(self): # real signature unknown; restored from __doc__
        """ blockCount(self) -> int """
        return 0

    def blockCountChanged(self, p_int): # real signature unknown; restored from __doc__
        """ blockCountChanged(self, int) [signal] """
        pass

    def characterAt(self, p_int): # real signature unknown; restored from __doc__
        """ characterAt(self, int) -> str """
        return ""

    def characterCount(self): # real signature unknown; restored from __doc__
        """ characterCount(self) -> int """
        return 0

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def clearUndoRedoStacks(self, stacks=None): # real signature unknown; restored from __doc__
        """ clearUndoRedoStacks(self, stacks: QTextDocument.Stacks = QTextDocument.UndoAndRedoStacks) """
        pass

    def clone(self, parent=None): # real signature unknown; restored from __doc__
        """ clone(self, parent: QObject = None) -> QTextDocument """
        return QTextDocument

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contentsChange(self, p_int, p_int_1, p_int_2): # real signature unknown; restored from __doc__
        """ contentsChange(self, int, int, int) [signal] """
        pass

    def contentsChanged(self): # real signature unknown; restored from __doc__
        """ contentsChanged(self) [signal] """
        pass

    def createObject(self, QTextFormat): # real signature unknown; restored from __doc__
        """ createObject(self, QTextFormat) -> QTextObject """
        return QTextObject

    def cursorPositionChanged(self, QTextCursor): # real signature unknown; restored from __doc__
        """ cursorPositionChanged(self, QTextCursor) [signal] """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultCursorMoveStyle(self): # real signature unknown; restored from __doc__
        """ defaultCursorMoveStyle(self) -> Qt.CursorMoveStyle """
        pass

    def defaultFont(self): # real signature unknown; restored from __doc__
        """ defaultFont(self) -> QFont """
        return QFont

    def defaultStyleSheet(self): # real signature unknown; restored from __doc__
        """ defaultStyleSheet(self) -> str """
        return ""

    def defaultTextOption(self): # real signature unknown; restored from __doc__
        """ defaultTextOption(self) -> QTextOption """
        return QTextOption

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def documentLayout(self): # real signature unknown; restored from __doc__
        """ documentLayout(self) -> QAbstractTextDocumentLayout """
        return QAbstractTextDocumentLayout

    def documentLayoutChanged(self): # real signature unknown; restored from __doc__
        """ documentLayoutChanged(self) [signal] """
        pass

    def documentMargin(self): # real signature unknown; restored from __doc__
        """ documentMargin(self) -> float """
        return 0.0

    def drawContents(self, QPainter, rect=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ drawContents(self, QPainter, rect: QRectF = QRectF()) """
        pass

    def end(self): # real signature unknown; restored from __doc__
        """ end(self) -> QTextBlock """
        return QTextBlock

    def find(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        find(self, str, position: int = 0, options: QTextDocument.FindFlags = 0) -> QTextCursor
        find(self, QRegExp, position: int = 0, options: QTextDocument.FindFlags = 0) -> QTextCursor
        find(self, QRegularExpression, position: int = 0, options: QTextDocument.FindFlags = 0) -> QTextCursor
        find(self, str, QTextCursor, options: QTextDocument.FindFlags = 0) -> QTextCursor
        find(self, QRegExp, QTextCursor, options: QTextDocument.FindFlags = 0) -> QTextCursor
        find(self, QRegularExpression, QTextCursor, options: QTextDocument.FindFlags = 0) -> QTextCursor
        """
        return QTextCursor

    def findBlock(self, p_int): # real signature unknown; restored from __doc__
        """ findBlock(self, int) -> QTextBlock """
        return QTextBlock

    def findBlockByLineNumber(self, p_int): # real signature unknown; restored from __doc__
        """ findBlockByLineNumber(self, int) -> QTextBlock """
        return QTextBlock

    def findBlockByNumber(self, p_int): # real signature unknown; restored from __doc__
        """ findBlockByNumber(self, int) -> QTextBlock """
        return QTextBlock

    def firstBlock(self): # real signature unknown; restored from __doc__
        """ firstBlock(self) -> QTextBlock """
        return QTextBlock

    def idealWidth(self): # real signature unknown; restored from __doc__
        """ idealWidth(self) -> float """
        return 0.0

    def indentWidth(self): # real signature unknown; restored from __doc__
        """ indentWidth(self) -> float """
        return 0.0

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isModified(self): # real signature unknown; restored from __doc__
        """ isModified(self) -> bool """
        return False

    def isRedoAvailable(self): # real signature unknown; restored from __doc__
        """ isRedoAvailable(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isUndoAvailable(self): # real signature unknown; restored from __doc__
        """ isUndoAvailable(self) -> bool """
        return False

    def isUndoRedoEnabled(self): # real signature unknown; restored from __doc__
        """ isUndoRedoEnabled(self) -> bool """
        return False

    def lastBlock(self): # real signature unknown; restored from __doc__
        """ lastBlock(self) -> QTextBlock """
        return QTextBlock

    def lineCount(self): # real signature unknown; restored from __doc__
        """ lineCount(self) -> int """
        return 0

    def loadResource(self, p_int, QUrl): # real signature unknown; restored from __doc__
        """ loadResource(self, int, QUrl) -> Any """
        pass

    def markContentsDirty(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ markContentsDirty(self, int, int) """
        pass

    def maximumBlockCount(self): # real signature unknown; restored from __doc__
        """ maximumBlockCount(self) -> int """
        return 0

    def metaInformation(self, QTextDocument_MetaInformation): # real signature unknown; restored from __doc__
        """ metaInformation(self, QTextDocument.MetaInformation) -> str """
        return ""

    def modificationChanged(self, bool): # real signature unknown; restored from __doc__
        """ modificationChanged(self, bool) [signal] """
        pass

    def object(self, p_int): # real signature unknown; restored from __doc__
        """ object(self, int) -> QTextObject """
        return QTextObject

    def objectForFormat(self, QTextFormat): # real signature unknown; restored from __doc__
        """ objectForFormat(self, QTextFormat) -> QTextObject """
        return QTextObject

    def pageCount(self): # real signature unknown; restored from __doc__
        """ pageCount(self) -> int """
        return 0

    def pageSize(self): # real signature unknown; restored from __doc__
        """ pageSize(self) -> QSizeF """
        pass

    def print(self, QPagedPaintDevice): # real signature unknown; restored from __doc__
        """ print(self, QPagedPaintDevice) """
        pass

    def print_(self, QPagedPaintDevice): # real signature unknown; restored from __doc__
        """ print_(self, QPagedPaintDevice) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def redo(self, QTextCursor=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        redo(self)
        redo(self, QTextCursor)
        """
        pass

    def redoAvailable(self, bool): # real signature unknown; restored from __doc__
        """ redoAvailable(self, bool) [signal] """
        pass

    def resource(self, p_int, QUrl): # real signature unknown; restored from __doc__
        """ resource(self, int, QUrl) -> Any """
        pass

    def revision(self): # real signature unknown; restored from __doc__
        """ revision(self) -> int """
        return 0

    def rootFrame(self): # real signature unknown; restored from __doc__
        """ rootFrame(self) -> QTextFrame """
        return QTextFrame

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setBaseUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ setBaseUrl(self, QUrl) """
        pass

    def setDefaultCursorMoveStyle(self, Qt_CursorMoveStyle): # real signature unknown; restored from __doc__
        """ setDefaultCursorMoveStyle(self, Qt.CursorMoveStyle) """
        pass

    def setDefaultFont(self, QFont): # real signature unknown; restored from __doc__
        """ setDefaultFont(self, QFont) """
        pass

    def setDefaultStyleSheet(self, p_str): # real signature unknown; restored from __doc__
        """ setDefaultStyleSheet(self, str) """
        pass

    def setDefaultTextOption(self, QTextOption): # real signature unknown; restored from __doc__
        """ setDefaultTextOption(self, QTextOption) """
        pass

    def setDocumentLayout(self, QAbstractTextDocumentLayout): # real signature unknown; restored from __doc__
        """ setDocumentLayout(self, QAbstractTextDocumentLayout) """
        pass

    def setDocumentMargin(self, p_float): # real signature unknown; restored from __doc__
        """ setDocumentMargin(self, float) """
        pass

    def setHtml(self, p_str): # real signature unknown; restored from __doc__
        """ setHtml(self, str) """
        pass

    def setIndentWidth(self, p_float): # real signature unknown; restored from __doc__
        """ setIndentWidth(self, float) """
        pass

    def setMaximumBlockCount(self, p_int): # real signature unknown; restored from __doc__
        """ setMaximumBlockCount(self, int) """
        pass

    def setMetaInformation(self, QTextDocument_MetaInformation, p_str): # real signature unknown; restored from __doc__
        """ setMetaInformation(self, QTextDocument.MetaInformation, str) """
        pass

    def setModified(self, on=True): # real signature unknown; restored from __doc__
        """ setModified(self, on: bool = True) """
        pass

    def setPageSize(self, QSizeF): # real signature unknown; restored from __doc__
        """ setPageSize(self, QSizeF) """
        pass

    def setPlainText(self, p_str): # real signature unknown; restored from __doc__
        """ setPlainText(self, str) """
        pass

    def setTextWidth(self, p_float): # real signature unknown; restored from __doc__
        """ setTextWidth(self, float) """
        pass

    def setUndoRedoEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setUndoRedoEnabled(self, bool) """
        pass

    def setUseDesignMetrics(self, bool): # real signature unknown; restored from __doc__
        """ setUseDesignMetrics(self, bool) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> QSizeF """
        pass

    def textWidth(self): # real signature unknown; restored from __doc__
        """ textWidth(self) -> float """
        return 0.0

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def toHtml(self, encoding, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ toHtml(self, encoding: Union[QByteArray, bytes, bytearray] = QByteArray()) -> str """
        pass

    def toPlainText(self): # real signature unknown; restored from __doc__
        """ toPlainText(self) -> str """
        return ""

    def toRawText(self): # real signature unknown; restored from __doc__
        """ toRawText(self) -> str """
        return ""

    def undo(self, QTextCursor=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        undo(self)
        undo(self, QTextCursor)
        """
        pass

    def undoAvailable(self, bool): # real signature unknown; restored from __doc__
        """ undoAvailable(self, bool) [signal] """
        pass

    def undoCommandAdded(self): # real signature unknown; restored from __doc__
        """ undoCommandAdded(self) [signal] """
        pass

    def useDesignMetrics(self): # real signature unknown; restored from __doc__
        """ useDesignMetrics(self) -> bool """
        return False

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    DocumentTitle = 0
    DocumentUrl = 1
    FindBackward = 1
    FindCaseSensitively = 2
    FindWholeWords = 4
    HtmlResource = 1
    ImageResource = 2
    RedoStack = 2
    StyleSheetResource = 3
    UndoAndRedoStacks = 3
    UndoStack = 1
    UserResource = 100


