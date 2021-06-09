# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QFontDatabase(__sip.simplewrapper):
    """
    QFontDatabase()
    QFontDatabase(QFontDatabase)
    """
    def addApplicationFont(self, p_str): # real signature unknown; restored from __doc__
        """ addApplicationFont(str) -> int """
        return 0

    def addApplicationFontFromData(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ addApplicationFontFromData(Union[QByteArray, bytes, bytearray]) -> int """
        return 0

    def applicationFontFamilies(self, p_int): # real signature unknown; restored from __doc__
        """ applicationFontFamilies(int) -> List[str] """
        return []

    def bold(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ bold(self, str, str) -> bool """
        return False

    def families(self, writingSystem=None): # real signature unknown; restored from __doc__
        """ families(self, writingSystem: QFontDatabase.WritingSystem = QFontDatabase.Any) -> List[str] """
        return []

    def font(self, p_str, p_str_1, p_int): # real signature unknown; restored from __doc__
        """ font(self, str, str, int) -> QFont """
        return QFont

    def isBitmapScalable(self, p_str, style=''): # real signature unknown; restored from __doc__
        """ isBitmapScalable(self, str, style: str = '') -> bool """
        return False

    def isFixedPitch(self, p_str, style=''): # real signature unknown; restored from __doc__
        """ isFixedPitch(self, str, style: str = '') -> bool """
        return False

    def isPrivateFamily(self, p_str): # real signature unknown; restored from __doc__
        """ isPrivateFamily(self, str) -> bool """
        return False

    def isScalable(self, p_str, style=''): # real signature unknown; restored from __doc__
        """ isScalable(self, str, style: str = '') -> bool """
        return False

    def isSmoothlyScalable(self, p_str, style=''): # real signature unknown; restored from __doc__
        """ isSmoothlyScalable(self, str, style: str = '') -> bool """
        return False

    def italic(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ italic(self, str, str) -> bool """
        return False

    def pointSizes(self, p_str, style=''): # real signature unknown; restored from __doc__
        """ pointSizes(self, str, style: str = '') -> List[int] """
        return []

    def removeAllApplicationFonts(self): # real signature unknown; restored from __doc__
        """ removeAllApplicationFonts() -> bool """
        return False

    def removeApplicationFont(self, p_int): # real signature unknown; restored from __doc__
        """ removeApplicationFont(int) -> bool """
        return False

    def smoothSizes(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ smoothSizes(self, str, str) -> List[int] """
        return []

    def standardSizes(self): # real signature unknown; restored from __doc__
        """ standardSizes() -> List[int] """
        return []

    def styles(self, p_str): # real signature unknown; restored from __doc__
        """ styles(self, str) -> List[str] """
        return []

    def styleString(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        styleString(self, QFont) -> str
        styleString(self, QFontInfo) -> str
        """
        return ""

    def supportsThreadedFontRendering(self): # real signature unknown; restored from __doc__
        """ supportsThreadedFontRendering() -> bool """
        return False

    def systemFont(self, QFontDatabase_SystemFont): # real signature unknown; restored from __doc__
        """ systemFont(QFontDatabase.SystemFont) -> QFont """
        return QFont

    def weight(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ weight(self, str, str) -> int """
        return 0

    def writingSystemName(self, QFontDatabase_WritingSystem): # real signature unknown; restored from __doc__
        """ writingSystemName(QFontDatabase.WritingSystem) -> str """
        return ""

    def writingSystems(self, p_str=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        writingSystems(self) -> List[QFontDatabase.WritingSystem]
        writingSystems(self, str) -> List[QFontDatabase.WritingSystem]
        """
        return []

    def writingSystemSample(self, QFontDatabase_WritingSystem): # real signature unknown; restored from __doc__
        """ writingSystemSample(QFontDatabase.WritingSystem) -> str """
        return ""

    def __init__(self, QFontDatabase=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Any = 0
    Arabic = 6
    Armenian = 4
    Bengali = 10
    Cyrillic = 3
    Devanagari = 9
    FixedFont = 1
    GeneralFont = 0
    Georgian = 23
    Greek = 2
    Gujarati = 12
    Gurmukhi = 11
    Hebrew = 5
    Japanese = 27
    Kannada = 16
    Khmer = 24
    Korean = 28
    Lao = 20
    Latin = 1
    Malayalam = 17
    Myanmar = 22
    Nko = 33
    Ogham = 31
    Oriya = 13
    Other = 30
    Runic = 32
    SimplifiedChinese = 25
    Sinhala = 18
    SmallestReadableFont = 3
    Symbol = 30
    Syriac = 7
    Tamil = 14
    Telugu = 15
    Thaana = 8
    Thai = 19
    Tibetan = 21
    TitleFont = 2
    TraditionalChinese = 26
    Vietnamese = 29


