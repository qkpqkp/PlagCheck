# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QColor(__sip.simplewrapper):
    """
    QColor(Qt.GlobalColor)
    QColor(int)
    QColor(QRgba64)
    QColor(Any)
    QColor()
    QColor(int, int, int, alpha: int = 255)
    QColor(str)
    QColor(Union[QColor, Qt.GlobalColor, QGradient])
    """
    def alpha(self): # real signature unknown; restored from __doc__
        """ alpha(self) -> int """
        return 0

    def alphaF(self): # real signature unknown; restored from __doc__
        """ alphaF(self) -> float """
        return 0.0

    def black(self): # real signature unknown; restored from __doc__
        """ black(self) -> int """
        return 0

    def blackF(self): # real signature unknown; restored from __doc__
        """ blackF(self) -> float """
        return 0.0

    def blue(self): # real signature unknown; restored from __doc__
        """ blue(self) -> int """
        return 0

    def blueF(self): # real signature unknown; restored from __doc__
        """ blueF(self) -> float """
        return 0.0

    def colorNames(self): # real signature unknown; restored from __doc__
        """ colorNames() -> List[str] """
        return []

    def convertTo(self, QColor_Spec): # real signature unknown; restored from __doc__
        """ convertTo(self, QColor.Spec) -> QColor """
        return QColor

    def cyan(self): # real signature unknown; restored from __doc__
        """ cyan(self) -> int """
        return 0

    def cyanF(self): # real signature unknown; restored from __doc__
        """ cyanF(self) -> float """
        return 0.0

    def darker(self, factor=200): # real signature unknown; restored from __doc__
        """ darker(self, factor: int = 200) -> QColor """
        return QColor

    def fromCmyk(self, p_int, p_int_1, p_int_2, p_int_3, alpha=255): # real signature unknown; restored from __doc__
        """ fromCmyk(int, int, int, int, alpha: int = 255) -> QColor """
        return QColor

    def fromCmykF(self, p_float, p_float_1, p_float_2, p_float_3, alpha=1): # real signature unknown; restored from __doc__
        """ fromCmykF(float, float, float, float, alpha: float = 1) -> QColor """
        return QColor

    def fromHsl(self, p_int, p_int_1, p_int_2, alpha=255): # real signature unknown; restored from __doc__
        """ fromHsl(int, int, int, alpha: int = 255) -> QColor """
        return QColor

    def fromHslF(self, p_float, p_float_1, p_float_2, alpha=1): # real signature unknown; restored from __doc__
        """ fromHslF(float, float, float, alpha: float = 1) -> QColor """
        return QColor

    def fromHsv(self, p_int, p_int_1, p_int_2, alpha=255): # real signature unknown; restored from __doc__
        """ fromHsv(int, int, int, alpha: int = 255) -> QColor """
        return QColor

    def fromHsvF(self, p_float, p_float_1, p_float_2, alpha=1): # real signature unknown; restored from __doc__
        """ fromHsvF(float, float, float, alpha: float = 1) -> QColor """
        return QColor

    def fromRgb(self, p_int, p_int_1=None, p_int_2=None, alpha=255): # real signature unknown; restored from __doc__ with multiple overloads
        """
        fromRgb(int) -> QColor
        fromRgb(int, int, int, alpha: int = 255) -> QColor
        """
        return QColor

    def fromRgba(self, p_int): # real signature unknown; restored from __doc__
        """ fromRgba(int) -> QColor """
        return QColor

    def fromRgba64(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        fromRgba64(int, int, int, alpha: int = 65535) -> QColor
        fromRgba64(QRgba64) -> QColor
        """
        return QColor

    def fromRgbF(self, p_float, p_float_1, p_float_2, alpha=1): # real signature unknown; restored from __doc__
        """ fromRgbF(float, float, float, alpha: float = 1) -> QColor """
        return QColor

    def getCmyk(self): # real signature unknown; restored from __doc__
        """ getCmyk(self) -> Tuple[int, int, int, int, int] """
        pass

    def getCmykF(self): # real signature unknown; restored from __doc__
        """ getCmykF(self) -> Tuple[float, float, float, float, float] """
        pass

    def getHsl(self): # real signature unknown; restored from __doc__
        """ getHsl(self) -> Tuple[int, int, int, int] """
        pass

    def getHslF(self): # real signature unknown; restored from __doc__
        """ getHslF(self) -> Tuple[float, float, float, float] """
        pass

    def getHsv(self): # real signature unknown; restored from __doc__
        """ getHsv(self) -> Tuple[int, int, int, int] """
        pass

    def getHsvF(self): # real signature unknown; restored from __doc__
        """ getHsvF(self) -> Tuple[float, float, float, float] """
        pass

    def getRgb(self): # real signature unknown; restored from __doc__
        """ getRgb(self) -> Tuple[int, int, int, int] """
        pass

    def getRgbF(self): # real signature unknown; restored from __doc__
        """ getRgbF(self) -> Tuple[float, float, float, float] """
        pass

    def green(self): # real signature unknown; restored from __doc__
        """ green(self) -> int """
        return 0

    def greenF(self): # real signature unknown; restored from __doc__
        """ greenF(self) -> float """
        return 0.0

    def hslHue(self): # real signature unknown; restored from __doc__
        """ hslHue(self) -> int """
        return 0

    def hslHueF(self): # real signature unknown; restored from __doc__
        """ hslHueF(self) -> float """
        return 0.0

    def hslSaturation(self): # real signature unknown; restored from __doc__
        """ hslSaturation(self) -> int """
        return 0

    def hslSaturationF(self): # real signature unknown; restored from __doc__
        """ hslSaturationF(self) -> float """
        return 0.0

    def hsvHue(self): # real signature unknown; restored from __doc__
        """ hsvHue(self) -> int """
        return 0

    def hsvHueF(self): # real signature unknown; restored from __doc__
        """ hsvHueF(self) -> float """
        return 0.0

    def hsvSaturation(self): # real signature unknown; restored from __doc__
        """ hsvSaturation(self) -> int """
        return 0

    def hsvSaturationF(self): # real signature unknown; restored from __doc__
        """ hsvSaturationF(self) -> float """
        return 0.0

    def hue(self): # real signature unknown; restored from __doc__
        """ hue(self) -> int """
        return 0

    def hueF(self): # real signature unknown; restored from __doc__
        """ hueF(self) -> float """
        return 0.0

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def isValidColor(self, p_str): # real signature unknown; restored from __doc__
        """ isValidColor(str) -> bool """
        return False

    def lighter(self, factor=150): # real signature unknown; restored from __doc__
        """ lighter(self, factor: int = 150) -> QColor """
        return QColor

    def lightness(self): # real signature unknown; restored from __doc__
        """ lightness(self) -> int """
        return 0

    def lightnessF(self): # real signature unknown; restored from __doc__
        """ lightnessF(self) -> float """
        return 0.0

    def magenta(self): # real signature unknown; restored from __doc__
        """ magenta(self) -> int """
        return 0

    def magentaF(self): # real signature unknown; restored from __doc__
        """ magentaF(self) -> float """
        return 0.0

    def name(self, QColor_NameFormat=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        name(self) -> str
        name(self, QColor.NameFormat) -> str
        """
        return ""

    def red(self): # real signature unknown; restored from __doc__
        """ red(self) -> int """
        return 0

    def redF(self): # real signature unknown; restored from __doc__
        """ redF(self) -> float """
        return 0.0

    def rgb(self): # real signature unknown; restored from __doc__
        """ rgb(self) -> int """
        return 0

    def rgba(self): # real signature unknown; restored from __doc__
        """ rgba(self) -> int """
        return 0

    def rgba64(self): # real signature unknown; restored from __doc__
        """ rgba64(self) -> QRgba64 """
        return QRgba64

    def saturation(self): # real signature unknown; restored from __doc__
        """ saturation(self) -> int """
        return 0

    def saturationF(self): # real signature unknown; restored from __doc__
        """ saturationF(self) -> float """
        return 0.0

    def setAlpha(self, p_int): # real signature unknown; restored from __doc__
        """ setAlpha(self, int) """
        pass

    def setAlphaF(self, p_float): # real signature unknown; restored from __doc__
        """ setAlphaF(self, float) """
        pass

    def setBlue(self, p_int): # real signature unknown; restored from __doc__
        """ setBlue(self, int) """
        pass

    def setBlueF(self, p_float): # real signature unknown; restored from __doc__
        """ setBlueF(self, float) """
        pass

    def setCmyk(self, p_int, p_int_1, p_int_2, p_int_3, alpha=255): # real signature unknown; restored from __doc__
        """ setCmyk(self, int, int, int, int, alpha: int = 255) """
        pass

    def setCmykF(self, p_float, p_float_1, p_float_2, p_float_3, alpha=1): # real signature unknown; restored from __doc__
        """ setCmykF(self, float, float, float, float, alpha: float = 1) """
        pass

    def setGreen(self, p_int): # real signature unknown; restored from __doc__
        """ setGreen(self, int) """
        pass

    def setGreenF(self, p_float): # real signature unknown; restored from __doc__
        """ setGreenF(self, float) """
        pass

    def setHsl(self, p_int, p_int_1, p_int_2, alpha=255): # real signature unknown; restored from __doc__
        """ setHsl(self, int, int, int, alpha: int = 255) """
        pass

    def setHslF(self, p_float, p_float_1, p_float_2, alpha=1): # real signature unknown; restored from __doc__
        """ setHslF(self, float, float, float, alpha: float = 1) """
        pass

    def setHsv(self, p_int, p_int_1, p_int_2, alpha=255): # real signature unknown; restored from __doc__
        """ setHsv(self, int, int, int, alpha: int = 255) """
        pass

    def setHsvF(self, p_float, p_float_1, p_float_2, alpha=1): # real signature unknown; restored from __doc__
        """ setHsvF(self, float, float, float, alpha: float = 1) """
        pass

    def setNamedColor(self, p_str): # real signature unknown; restored from __doc__
        """ setNamedColor(self, str) """
        pass

    def setRed(self, p_int): # real signature unknown; restored from __doc__
        """ setRed(self, int) """
        pass

    def setRedF(self, p_float): # real signature unknown; restored from __doc__
        """ setRedF(self, float) """
        pass

    def setRgb(self, p_int, p_int_1=None, p_int_2=None, alpha=255): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setRgb(self, int, int, int, alpha: int = 255)
        setRgb(self, int)
        """
        pass

    def setRgba(self, p_int): # real signature unknown; restored from __doc__
        """ setRgba(self, int) """
        pass

    def setRgba64(self, QRgba64): # real signature unknown; restored from __doc__
        """ setRgba64(self, QRgba64) """
        pass

    def setRgbF(self, p_float, p_float_1, p_float_2, alpha=1): # real signature unknown; restored from __doc__
        """ setRgbF(self, float, float, float, alpha: float = 1) """
        pass

    def spec(self): # real signature unknown; restored from __doc__
        """ spec(self) -> QColor.Spec """
        pass

    def toCmyk(self): # real signature unknown; restored from __doc__
        """ toCmyk(self) -> QColor """
        return QColor

    def toHsl(self): # real signature unknown; restored from __doc__
        """ toHsl(self) -> QColor """
        return QColor

    def toHsv(self): # real signature unknown; restored from __doc__
        """ toHsv(self) -> QColor """
        return QColor

    def toRgb(self): # real signature unknown; restored from __doc__
        """ toRgb(self) -> QColor """
        return QColor

    def value(self): # real signature unknown; restored from __doc__
        """ value(self) -> int """
        return 0

    def valueF(self): # real signature unknown; restored from __doc__
        """ valueF(self) -> float """
        return 0.0

    def yellow(self): # real signature unknown; restored from __doc__
        """ yellow(self) -> int """
        return 0

    def yellowF(self): # real signature unknown; restored from __doc__
        """ yellowF(self) -> float """
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

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Cmyk = 3
    HexArgb = 1
    HexRgb = 0
    Hsl = 4
    Hsv = 2
    Invalid = 0
    Rgb = 1
    __hash__ = None


