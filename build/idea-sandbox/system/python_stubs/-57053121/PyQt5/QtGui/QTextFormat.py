# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QTextFormat(__sip.simplewrapper):
    """
    QTextFormat()
    QTextFormat(int)
    QTextFormat(QTextFormat)
    QTextFormat(Any)
    """
    def background(self): # real signature unknown; restored from __doc__
        """ background(self) -> QBrush """
        return QBrush

    def boolProperty(self, p_int): # real signature unknown; restored from __doc__
        """ boolProperty(self, int) -> bool """
        return False

    def brushProperty(self, p_int): # real signature unknown; restored from __doc__
        """ brushProperty(self, int) -> QBrush """
        return QBrush

    def clearBackground(self): # real signature unknown; restored from __doc__
        """ clearBackground(self) """
        pass

    def clearForeground(self): # real signature unknown; restored from __doc__
        """ clearForeground(self) """
        pass

    def clearProperty(self, p_int): # real signature unknown; restored from __doc__
        """ clearProperty(self, int) """
        pass

    def colorProperty(self, p_int): # real signature unknown; restored from __doc__
        """ colorProperty(self, int) -> QColor """
        return QColor

    def doubleProperty(self, p_int): # real signature unknown; restored from __doc__
        """ doubleProperty(self, int) -> float """
        return 0.0

    def foreground(self): # real signature unknown; restored from __doc__
        """ foreground(self) -> QBrush """
        return QBrush

    def hasProperty(self, p_int): # real signature unknown; restored from __doc__
        """ hasProperty(self, int) -> bool """
        return False

    def intProperty(self, p_int): # real signature unknown; restored from __doc__
        """ intProperty(self, int) -> int """
        return 0

    def isBlockFormat(self): # real signature unknown; restored from __doc__
        """ isBlockFormat(self) -> bool """
        return False

    def isCharFormat(self): # real signature unknown; restored from __doc__
        """ isCharFormat(self) -> bool """
        return False

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isFrameFormat(self): # real signature unknown; restored from __doc__
        """ isFrameFormat(self) -> bool """
        return False

    def isImageFormat(self): # real signature unknown; restored from __doc__
        """ isImageFormat(self) -> bool """
        return False

    def isListFormat(self): # real signature unknown; restored from __doc__
        """ isListFormat(self) -> bool """
        return False

    def isTableCellFormat(self): # real signature unknown; restored from __doc__
        """ isTableCellFormat(self) -> bool """
        return False

    def isTableFormat(self): # real signature unknown; restored from __doc__
        """ isTableFormat(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def layoutDirection(self): # real signature unknown; restored from __doc__
        """ layoutDirection(self) -> Qt.LayoutDirection """
        pass

    def lengthProperty(self, p_int): # real signature unknown; restored from __doc__
        """ lengthProperty(self, int) -> QTextLength """
        return QTextLength

    def lengthVectorProperty(self, p_int): # real signature unknown; restored from __doc__
        """ lengthVectorProperty(self, int) -> List[QTextLength] """
        return []

    def merge(self, QTextFormat): # real signature unknown; restored from __doc__
        """ merge(self, QTextFormat) """
        pass

    def objectIndex(self): # real signature unknown; restored from __doc__
        """ objectIndex(self) -> int """
        return 0

    def objectType(self): # real signature unknown; restored from __doc__
        """ objectType(self) -> int """
        return 0

    def penProperty(self, p_int): # real signature unknown; restored from __doc__
        """ penProperty(self, int) -> QPen """
        return QPen

    def properties(self): # real signature unknown; restored from __doc__
        """ properties(self) -> Dict[int, Any] """
        return {}

    def property(self, p_int): # real signature unknown; restored from __doc__
        """ property(self, int) -> Any """
        pass

    def propertyCount(self): # real signature unknown; restored from __doc__
        """ propertyCount(self) -> int """
        return 0

    def setBackground(self, Union, QBrush=None, QColor=None, Qt_GlobalColor=None, QGradient=None): # real signature unknown; restored from __doc__
        """ setBackground(self, Union[QBrush, QColor, Qt.GlobalColor, QGradient]) """
        pass

    def setForeground(self, Union, QBrush=None, QColor=None, Qt_GlobalColor=None, QGradient=None): # real signature unknown; restored from __doc__
        """ setForeground(self, Union[QBrush, QColor, Qt.GlobalColor, QGradient]) """
        pass

    def setLayoutDirection(self, Qt_LayoutDirection): # real signature unknown; restored from __doc__
        """ setLayoutDirection(self, Qt.LayoutDirection) """
        pass

    def setObjectIndex(self, p_int): # real signature unknown; restored from __doc__
        """ setObjectIndex(self, int) """
        pass

    def setObjectType(self, p_int): # real signature unknown; restored from __doc__
        """ setObjectType(self, int) """
        pass

    def setProperty(self, p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setProperty(self, int, Any)
        setProperty(self, int, Iterable[QTextLength])
        """
        pass

    def stringProperty(self, p_int): # real signature unknown; restored from __doc__
        """ stringProperty(self, int) -> str """
        return ""

    def swap(self, QTextFormat): # real signature unknown; restored from __doc__
        """ swap(self, QTextFormat) """
        pass

    def toBlockFormat(self): # real signature unknown; restored from __doc__
        """ toBlockFormat(self) -> QTextBlockFormat """
        return QTextBlockFormat

    def toCharFormat(self): # real signature unknown; restored from __doc__
        """ toCharFormat(self) -> QTextCharFormat """
        return QTextCharFormat

    def toFrameFormat(self): # real signature unknown; restored from __doc__
        """ toFrameFormat(self) -> QTextFrameFormat """
        return QTextFrameFormat

    def toImageFormat(self): # real signature unknown; restored from __doc__
        """ toImageFormat(self) -> QTextImageFormat """
        return QTextImageFormat

    def toListFormat(self): # real signature unknown; restored from __doc__
        """ toListFormat(self) -> QTextListFormat """
        return QTextListFormat

    def toTableCellFormat(self): # real signature unknown; restored from __doc__
        """ toTableCellFormat(self) -> QTextTableCellFormat """
        return QTextTableCellFormat

    def toTableFormat(self): # real signature unknown; restored from __doc__
        """ toTableFormat(self) -> QTextTableFormat """
        return QTextTableFormat

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> int """
        return 0

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


    AnchorHref = 8241
    AnchorName = 8242
    BackgroundBrush = 2080
    BackgroundImageUrl = 2083
    BlockAlignment = 4112
    BlockBottomMargin = 4145
    BlockFormat = 1
    BlockIndent = 4160
    BlockLeftMargin = 4146
    BlockNonBreakableLines = 4176
    BlockRightMargin = 4147
    BlockTopMargin = 4144
    BlockTrailingHorizontalRulerWidth = 4192
    CharFormat = 2
    CssFloat = 2048
    FirstFontProperty = 8160
    FontCapitalization = 8160
    FontFamily = 8192
    FontFixedPitch = 8200
    FontHintingPreference = 8166
    FontItalic = 8196
    FontKerning = 8165
    FontLetterSpacing = 8161
    FontLetterSpacingType = 8243
    FontOverline = 8198
    FontPixelSize = 8201
    FontPointSize = 8193
    FontSizeAdjustment = 8194
    FontSizeIncrement = 8194
    FontStretch = 8244
    FontStrikeOut = 8199
    FontStyleHint = 8163
    FontStyleStrategy = 8164
    FontUnderline = 8197
    FontWeight = 8195
    FontWordSpacing = 8162
    ForegroundBrush = 2081
    FrameBorder = 16384
    FrameBorderBrush = 16393
    FrameBorderStyle = 16400
    FrameBottomMargin = 16390
    FrameFormat = 5
    FrameHeight = 16388
    FrameLeftMargin = 16391
    FrameMargin = 16385
    FramePadding = 16386
    FrameRightMargin = 16392
    FrameTopMargin = 16389
    FrameWidth = 16387
    FullWidthSelection = 24576
    HeadingLevel = 4208
    ImageHeight = 20497
    ImageName = 20480
    ImageObject = 1
    ImageQuality = 20500
    ImageWidth = 20496
    InvalidFormat = -1
    IsAnchor = 8240
    LastFontProperty = 8201
    LayoutDirection = 2049
    LineHeight = 4168
    LineHeightType = 4169
    ListFormat = 3
    ListIndent = 12289
    ListNumberPrefix = 12290
    ListNumberSuffix = 12291
    ListStyle = 12288
    NoObject = 0
    ObjectIndex = 0
    ObjectType = 12032
    OutlinePen = 2064
    PageBreakPolicy = 28672
    PageBreak_AlwaysAfter = 16
    PageBreak_AlwaysBefore = 1
    PageBreak_Auto = 0
    TableCellBottomPadding = 18451
    TableCellColumnSpan = 18449
    TableCellLeftPadding = 18452
    TableCellObject = 3
    TableCellPadding = 16643
    TableCellRightPadding = 18453
    TableCellRowSpan = 18448
    TableCellSpacing = 16642
    TableCellTopPadding = 18450
    TableColumns = 16640
    TableColumnWidthConstraints = 16641
    TableFormat = 4
    TableHeaderRowCount = 16644
    TableObject = 2
    TabPositions = 4149
    TextIndent = 4148
    TextOutline = 8226
    TextToolTip = 8228
    TextUnderlineColor = 8208
    TextUnderlineStyle = 8227
    TextVerticalAlignment = 8225
    UserFormat = 100
    UserObject = 4096
    UserProperty = 1048576
    __hash__ = None


