# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QFont(__sip.simplewrapper):
    """
    QFont()
    QFont(str, pointSize: int = -1, weight: int = -1, italic: bool = False)
    QFont(QFont, QPaintDevice)
    QFont(QFont)
    QFont(Any)
    """
    def bold(self): # real signature unknown; restored from __doc__
        """ bold(self) -> bool """
        return False

    def cacheStatistics(self): # real signature unknown; restored from __doc__
        """ cacheStatistics() """
        pass

    def capitalization(self): # real signature unknown; restored from __doc__
        """ capitalization(self) -> QFont.Capitalization """
        pass

    def cleanup(self): # real signature unknown; restored from __doc__
        """ cleanup() """
        pass

    def defaultFamily(self): # real signature unknown; restored from __doc__
        """ defaultFamily(self) -> str """
        return ""

    def exactMatch(self): # real signature unknown; restored from __doc__
        """ exactMatch(self) -> bool """
        return False

    def family(self): # real signature unknown; restored from __doc__
        """ family(self) -> str """
        return ""

    def fixedPitch(self): # real signature unknown; restored from __doc__
        """ fixedPitch(self) -> bool """
        return False

    def fromString(self, p_str): # real signature unknown; restored from __doc__
        """ fromString(self, str) -> bool """
        return False

    def hintingPreference(self): # real signature unknown; restored from __doc__
        """ hintingPreference(self) -> QFont.HintingPreference """
        pass

    def initialize(self): # real signature unknown; restored from __doc__
        """ initialize() """
        pass

    def insertSubstitution(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ insertSubstitution(str, str) """
        pass

    def insertSubstitutions(self, p_str, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ insertSubstitutions(str, Iterable[str]) """
        pass

    def isCopyOf(self, QFont): # real signature unknown; restored from __doc__
        """ isCopyOf(self, QFont) -> bool """
        return False

    def italic(self): # real signature unknown; restored from __doc__
        """ italic(self) -> bool """
        return False

    def kerning(self): # real signature unknown; restored from __doc__
        """ kerning(self) -> bool """
        return False

    def key(self): # real signature unknown; restored from __doc__
        """ key(self) -> str """
        return ""

    def lastResortFamily(self): # real signature unknown; restored from __doc__
        """ lastResortFamily(self) -> str """
        return ""

    def lastResortFont(self): # real signature unknown; restored from __doc__
        """ lastResortFont(self) -> str """
        return ""

    def letterSpacing(self): # real signature unknown; restored from __doc__
        """ letterSpacing(self) -> float """
        return 0.0

    def letterSpacingType(self): # real signature unknown; restored from __doc__
        """ letterSpacingType(self) -> QFont.SpacingType """
        pass

    def overline(self): # real signature unknown; restored from __doc__
        """ overline(self) -> bool """
        return False

    def pixelSize(self): # real signature unknown; restored from __doc__
        """ pixelSize(self) -> int """
        return 0

    def pointSize(self): # real signature unknown; restored from __doc__
        """ pointSize(self) -> int """
        return 0

    def pointSizeF(self): # real signature unknown; restored from __doc__
        """ pointSizeF(self) -> float """
        return 0.0

    def rawMode(self): # real signature unknown; restored from __doc__
        """ rawMode(self) -> bool """
        return False

    def rawName(self): # real signature unknown; restored from __doc__
        """ rawName(self) -> str """
        return ""

    def removeSubstitutions(self, p_str): # real signature unknown; restored from __doc__
        """ removeSubstitutions(str) """
        pass

    def resolve(self, QFont): # real signature unknown; restored from __doc__
        """ resolve(self, QFont) -> QFont """
        return QFont

    def setBold(self, bool): # real signature unknown; restored from __doc__
        """ setBold(self, bool) """
        pass

    def setCapitalization(self, QFont_Capitalization): # real signature unknown; restored from __doc__
        """ setCapitalization(self, QFont.Capitalization) """
        pass

    def setFamily(self, p_str): # real signature unknown; restored from __doc__
        """ setFamily(self, str) """
        pass

    def setFixedPitch(self, bool): # real signature unknown; restored from __doc__
        """ setFixedPitch(self, bool) """
        pass

    def setHintingPreference(self, QFont_HintingPreference): # real signature unknown; restored from __doc__
        """ setHintingPreference(self, QFont.HintingPreference) """
        pass

    def setItalic(self, bool): # real signature unknown; restored from __doc__
        """ setItalic(self, bool) """
        pass

    def setKerning(self, bool): # real signature unknown; restored from __doc__
        """ setKerning(self, bool) """
        pass

    def setLetterSpacing(self, QFont_SpacingType, p_float): # real signature unknown; restored from __doc__
        """ setLetterSpacing(self, QFont.SpacingType, float) """
        pass

    def setOverline(self, bool): # real signature unknown; restored from __doc__
        """ setOverline(self, bool) """
        pass

    def setPixelSize(self, p_int): # real signature unknown; restored from __doc__
        """ setPixelSize(self, int) """
        pass

    def setPointSize(self, p_int): # real signature unknown; restored from __doc__
        """ setPointSize(self, int) """
        pass

    def setPointSizeF(self, p_float): # real signature unknown; restored from __doc__
        """ setPointSizeF(self, float) """
        pass

    def setRawMode(self, bool): # real signature unknown; restored from __doc__
        """ setRawMode(self, bool) """
        pass

    def setRawName(self, p_str): # real signature unknown; restored from __doc__
        """ setRawName(self, str) """
        pass

    def setStretch(self, p_int): # real signature unknown; restored from __doc__
        """ setStretch(self, int) """
        pass

    def setStrikeOut(self, bool): # real signature unknown; restored from __doc__
        """ setStrikeOut(self, bool) """
        pass

    def setStyle(self, QFont_Style): # real signature unknown; restored from __doc__
        """ setStyle(self, QFont.Style) """
        pass

    def setStyleHint(self, QFont_StyleHint, strategy=None): # real signature unknown; restored from __doc__
        """ setStyleHint(self, QFont.StyleHint, strategy: QFont.StyleStrategy = QFont.PreferDefault) """
        pass

    def setStyleName(self, p_str): # real signature unknown; restored from __doc__
        """ setStyleName(self, str) """
        pass

    def setStyleStrategy(self, QFont_StyleStrategy): # real signature unknown; restored from __doc__
        """ setStyleStrategy(self, QFont.StyleStrategy) """
        pass

    def setUnderline(self, bool): # real signature unknown; restored from __doc__
        """ setUnderline(self, bool) """
        pass

    def setWeight(self, p_int): # real signature unknown; restored from __doc__
        """ setWeight(self, int) """
        pass

    def setWordSpacing(self, p_float): # real signature unknown; restored from __doc__
        """ setWordSpacing(self, float) """
        pass

    def stretch(self): # real signature unknown; restored from __doc__
        """ stretch(self) -> int """
        return 0

    def strikeOut(self): # real signature unknown; restored from __doc__
        """ strikeOut(self) -> bool """
        return False

    def style(self): # real signature unknown; restored from __doc__
        """ style(self) -> QFont.Style """
        pass

    def styleHint(self): # real signature unknown; restored from __doc__
        """ styleHint(self) -> QFont.StyleHint """
        pass

    def styleName(self): # real signature unknown; restored from __doc__
        """ styleName(self) -> str """
        return ""

    def styleStrategy(self): # real signature unknown; restored from __doc__
        """ styleStrategy(self) -> QFont.StyleStrategy """
        pass

    def substitute(self, p_str): # real signature unknown; restored from __doc__
        """ substitute(str) -> str """
        return ""

    def substitutes(self, p_str): # real signature unknown; restored from __doc__
        """ substitutes(str) -> List[str] """
        return []

    def substitutions(self): # real signature unknown; restored from __doc__
        """ substitutions() -> List[str] """
        return []

    def swap(self, QFont): # real signature unknown; restored from __doc__
        """ swap(self, QFont) """
        pass

    def toString(self): # real signature unknown; restored from __doc__
        """ toString(self) -> str """
        return ""

    def underline(self): # real signature unknown; restored from __doc__
        """ underline(self) -> bool """
        return False

    def weight(self): # real signature unknown; restored from __doc__
        """ weight(self) -> int """
        return 0

    def wordSpacing(self): # real signature unknown; restored from __doc__
        """ wordSpacing(self) -> float """
        return 0.0

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
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


    AbsoluteSpacing = 1
    AllLowercase = 2
    AllUppercase = 1
    AnyStretch = 0
    AnyStyle = 5
    Black = 87
    Bold = 75
    Capitalize = 4
    Condensed = 75
    Courier = 2
    Cursive = 6
    Decorative = 3
    DemiBold = 63
    Expanded = 125
    ExtraBold = 81
    ExtraCondensed = 62
    ExtraExpanded = 150
    ExtraLight = 12
    Fantasy = 8
    ForceIntegerMetrics = 1024
    ForceOutline = 16
    Helvetica = 0
    Light = 25
    Medium = 57
    MixedCase = 0
    Monospace = 7
    NoAntialias = 256
    NoFontMerging = 32768
    Normal = 50
    NoSubpixelAntialias = 2048
    OldEnglish = 3
    OpenGLCompatible = 512
    PercentageSpacing = 0
    PreferAntialias = 128
    PreferBitmap = 2
    PreferDefault = 1
    PreferDefaultHinting = 0
    PreferDevice = 4
    PreferFullHinting = 3
    PreferMatch = 32
    PreferNoHinting = 1
    PreferNoShaping = 4096
    PreferOutline = 8
    PreferQuality = 64
    PreferVerticalHinting = 2
    SansSerif = 0
    SemiCondensed = 87
    SemiExpanded = 112
    Serif = 1
    SmallCaps = 3
    StyleItalic = 1
    StyleNormal = 0
    StyleOblique = 2
    System = 4
    Thin = 0
    Times = 1
    TypeWriter = 2
    UltraCondensed = 50
    UltraExpanded = 200
    Unstretched = 100


