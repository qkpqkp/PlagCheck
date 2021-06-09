# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QTextLayout(__sip.simplewrapper):
    """
    QTextLayout()
    QTextLayout(str)
    QTextLayout(str, QFont, paintDevice: QPaintDevice = None)
    QTextLayout(QTextBlock)
    """
    def additionalFormats(self): # real signature unknown; restored from __doc__
        """ additionalFormats(self) -> List[QTextLayout.FormatRange] """
        return []

    def beginLayout(self): # real signature unknown; restored from __doc__
        """ beginLayout(self) """
        pass

    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> QRectF """
        pass

    def cacheEnabled(self): # real signature unknown; restored from __doc__
        """ cacheEnabled(self) -> bool """
        return False

    def clearAdditionalFormats(self): # real signature unknown; restored from __doc__
        """ clearAdditionalFormats(self) """
        pass

    def clearFormats(self): # real signature unknown; restored from __doc__
        """ clearFormats(self) """
        pass

    def clearLayout(self): # real signature unknown; restored from __doc__
        """ clearLayout(self) """
        pass

    def createLine(self): # real signature unknown; restored from __doc__
        """ createLine(self) -> QTextLine """
        return QTextLine

    def cursorMoveStyle(self): # real signature unknown; restored from __doc__
        """ cursorMoveStyle(self) -> Qt.CursorMoveStyle """
        pass

    def draw(self, QPainter, Union, QPointF=None, QPoint=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ draw(self, QPainter, Union[QPointF, QPoint], selections: Iterable[QTextLayout.FormatRange] = [], clip: QRectF = QRectF()) """
        pass

    def drawCursor(self, QPainter, Union, QPointF=None, QPoint=None, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawCursor(self, QPainter, Union[QPointF, QPoint], int)
        drawCursor(self, QPainter, Union[QPointF, QPoint], int, int)
        """
        pass

    def endLayout(self): # real signature unknown; restored from __doc__
        """ endLayout(self) """
        pass

    def font(self): # real signature unknown; restored from __doc__
        """ font(self) -> QFont """
        return QFont

    def formats(self): # real signature unknown; restored from __doc__
        """ formats(self) -> List[QTextLayout.FormatRange] """
        return []

    def glyphRuns(self, from_=-1, length=-1): # real signature unknown; restored from __doc__
        """ glyphRuns(self, from_: int = -1, length: int = -1) -> List[QGlyphRun] """
        return []

    def isValidCursorPosition(self, p_int): # real signature unknown; restored from __doc__
        """ isValidCursorPosition(self, int) -> bool """
        return False

    def leftCursorPosition(self, p_int): # real signature unknown; restored from __doc__
        """ leftCursorPosition(self, int) -> int """
        return 0

    def lineAt(self, p_int): # real signature unknown; restored from __doc__
        """ lineAt(self, int) -> QTextLine """
        return QTextLine

    def lineCount(self): # real signature unknown; restored from __doc__
        """ lineCount(self) -> int """
        return 0

    def lineForTextPosition(self, p_int): # real signature unknown; restored from __doc__
        """ lineForTextPosition(self, int) -> QTextLine """
        return QTextLine

    def maximumWidth(self): # real signature unknown; restored from __doc__
        """ maximumWidth(self) -> float """
        return 0.0

    def minimumWidth(self): # real signature unknown; restored from __doc__
        """ minimumWidth(self) -> float """
        return 0.0

    def nextCursorPosition(self, p_int, mode=None): # real signature unknown; restored from __doc__
        """ nextCursorPosition(self, int, mode: QTextLayout.CursorMode = QTextLayout.SkipCharacters) -> int """
        return 0

    def position(self): # real signature unknown; restored from __doc__
        """ position(self) -> QPointF """
        pass

    def preeditAreaPosition(self): # real signature unknown; restored from __doc__
        """ preeditAreaPosition(self) -> int """
        return 0

    def preeditAreaText(self): # real signature unknown; restored from __doc__
        """ preeditAreaText(self) -> str """
        return ""

    def previousCursorPosition(self, p_int, mode=None): # real signature unknown; restored from __doc__
        """ previousCursorPosition(self, int, mode: QTextLayout.CursorMode = QTextLayout.SkipCharacters) -> int """
        return 0

    def rightCursorPosition(self, p_int): # real signature unknown; restored from __doc__
        """ rightCursorPosition(self, int) -> int """
        return 0

    def setAdditionalFormats(self, Iterable, QTextLayout_FormatRange=None): # real signature unknown; restored from __doc__
        """ setAdditionalFormats(self, Iterable[QTextLayout.FormatRange]) """
        pass

    def setCacheEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setCacheEnabled(self, bool) """
        pass

    def setCursorMoveStyle(self, Qt_CursorMoveStyle): # real signature unknown; restored from __doc__
        """ setCursorMoveStyle(self, Qt.CursorMoveStyle) """
        pass

    def setFont(self, QFont): # real signature unknown; restored from __doc__
        """ setFont(self, QFont) """
        pass

    def setFormats(self, Iterable, QTextLayout_FormatRange=None): # real signature unknown; restored from __doc__
        """ setFormats(self, Iterable[QTextLayout.FormatRange]) """
        pass

    def setPosition(self, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ setPosition(self, Union[QPointF, QPoint]) """
        pass

    def setPreeditArea(self, p_int, p_str): # real signature unknown; restored from __doc__
        """ setPreeditArea(self, int, str) """
        pass

    def setText(self, p_str): # real signature unknown; restored from __doc__
        """ setText(self, str) """
        pass

    def setTextOption(self, QTextOption): # real signature unknown; restored from __doc__
        """ setTextOption(self, QTextOption) """
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def textOption(self): # real signature unknown; restored from __doc__
        """ textOption(self) -> QTextOption """
        return QTextOption

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    SkipCharacters = 0
    SkipWords = 1


