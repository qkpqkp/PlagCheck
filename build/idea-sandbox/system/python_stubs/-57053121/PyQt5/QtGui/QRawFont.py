# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QRawFont(__sip.simplewrapper):
    """
    QRawFont()
    QRawFont(str, float, hintingPreference: QFont.HintingPreference = QFont.PreferDefaultHinting)
    QRawFont(Union[QByteArray, bytes, bytearray], float, hintingPreference: QFont.HintingPreference = QFont.PreferDefaultHinting)
    QRawFont(QRawFont)
    """
    def advancesForGlyphIndexes(self, Iterable, p_int=None, *args=None, **kwargs=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        advancesForGlyphIndexes(self, Iterable[int]) -> List[QPointF]
        advancesForGlyphIndexes(self, Iterable[int], Union[QRawFont.LayoutFlags, QRawFont.LayoutFlag]) -> List[QPointF]
        """
        return []

    def alphaMapForGlyph(self, p_int, antialiasingType=None, transform=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ alphaMapForGlyph(self, int, antialiasingType: QRawFont.AntialiasingType = QRawFont.SubPixelAntialiasing, transform: QTransform = QTransform()) -> QImage """
        pass

    def ascent(self): # real signature unknown; restored from __doc__
        """ ascent(self) -> float """
        return 0.0

    def averageCharWidth(self): # real signature unknown; restored from __doc__
        """ averageCharWidth(self) -> float """
        return 0.0

    def boundingRect(self, p_int): # real signature unknown; restored from __doc__
        """ boundingRect(self, int) -> QRectF """
        pass

    def capHeight(self): # real signature unknown; restored from __doc__
        """ capHeight(self) -> float """
        return 0.0

    def descent(self): # real signature unknown; restored from __doc__
        """ descent(self) -> float """
        return 0.0

    def familyName(self): # real signature unknown; restored from __doc__
        """ familyName(self) -> str """
        return ""

    def fontTable(self, p_str): # real signature unknown; restored from __doc__
        """ fontTable(self, str) -> QByteArray """
        pass

    def fromFont(self, QFont, writingSystem=None): # real signature unknown; restored from __doc__
        """ fromFont(QFont, writingSystem: QFontDatabase.WritingSystem = QFontDatabase.Any) -> QRawFont """
        return QRawFont

    def glyphIndexesForString(self, p_str): # real signature unknown; restored from __doc__
        """ glyphIndexesForString(self, str) -> List[int] """
        return []

    def hintingPreference(self): # real signature unknown; restored from __doc__
        """ hintingPreference(self) -> QFont.HintingPreference """
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def leading(self): # real signature unknown; restored from __doc__
        """ leading(self) -> float """
        return 0.0

    def lineThickness(self): # real signature unknown; restored from __doc__
        """ lineThickness(self) -> float """
        return 0.0

    def loadFromData(self, Union, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ loadFromData(self, Union[QByteArray, bytes, bytearray], float, QFont.HintingPreference) """
        pass

    def loadFromFile(self, p_str, p_float, QFont_HintingPreference): # real signature unknown; restored from __doc__
        """ loadFromFile(self, str, float, QFont.HintingPreference) """
        pass

    def maxCharWidth(self): # real signature unknown; restored from __doc__
        """ maxCharWidth(self) -> float """
        return 0.0

    def pathForGlyph(self, p_int): # real signature unknown; restored from __doc__
        """ pathForGlyph(self, int) -> QPainterPath """
        return QPainterPath

    def pixelSize(self): # real signature unknown; restored from __doc__
        """ pixelSize(self) -> float """
        return 0.0

    def setPixelSize(self, p_float): # real signature unknown; restored from __doc__
        """ setPixelSize(self, float) """
        pass

    def style(self): # real signature unknown; restored from __doc__
        """ style(self) -> QFont.Style """
        pass

    def styleName(self): # real signature unknown; restored from __doc__
        """ styleName(self) -> str """
        return ""

    def supportedWritingSystems(self): # real signature unknown; restored from __doc__
        """ supportedWritingSystems(self) -> List[QFontDatabase.WritingSystem] """
        return []

    def supportsCharacter(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        supportsCharacter(self, int) -> bool
        supportsCharacter(self, str) -> bool
        """
        return False

    def swap(self, QRawFont): # real signature unknown; restored from __doc__
        """ swap(self, QRawFont) """
        pass

    def underlinePosition(self): # real signature unknown; restored from __doc__
        """ underlinePosition(self) -> float """
        return 0.0

    def unitsPerEm(self): # real signature unknown; restored from __doc__
        """ unitsPerEm(self) -> float """
        return 0.0

    def weight(self): # real signature unknown; restored from __doc__
        """ weight(self) -> int """
        return 0

    def xHeight(self): # real signature unknown; restored from __doc__
        """ xHeight(self) -> float """
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


    KernedAdvances = 1
    PixelAntialiasing = 0
    SeparateAdvances = 0
    SubPixelAntialiasing = 1
    UseDesignMetrics = 2


