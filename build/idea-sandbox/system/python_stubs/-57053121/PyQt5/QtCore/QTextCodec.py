# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QTextCodec(__sip.wrapper):
    # no doc
    def aliases(self): # real signature unknown; restored from __doc__
        """ aliases(self) -> List[QByteArray] """
        return []

    def availableCodecs(self): # real signature unknown; restored from __doc__
        """ availableCodecs() -> List[QByteArray] """
        return []

    def availableMibs(self): # real signature unknown; restored from __doc__
        """ availableMibs() -> List[int] """
        return []

    def canEncode(self, p_str): # real signature unknown; restored from __doc__
        """ canEncode(self, str) -> bool """
        return False

    def codecForHtml(self, Union, QByteArray=None, bytes=None, bytearray=None, *args=None, **kwargs=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        codecForHtml(Union[QByteArray, bytes, bytearray]) -> QTextCodec
        codecForHtml(Union[QByteArray, bytes, bytearray], QTextCodec) -> QTextCodec
        """
        return QTextCodec

    def codecForLocale(self): # real signature unknown; restored from __doc__
        """ codecForLocale() -> QTextCodec """
        return QTextCodec

    def codecForMib(self, p_int): # real signature unknown; restored from __doc__
        """ codecForMib(int) -> QTextCodec """
        return QTextCodec

    def codecForName(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        codecForName(Union[QByteArray, bytes, bytearray]) -> QTextCodec
        codecForName(str) -> QTextCodec
        """
        return QTextCodec

    def codecForUtfText(self, Union, QByteArray=None, bytes=None, bytearray=None, *args=None, **kwargs=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        codecForUtfText(Union[QByteArray, bytes, bytearray]) -> QTextCodec
        codecForUtfText(Union[QByteArray, bytes, bytearray], QTextCodec) -> QTextCodec
        """
        return QTextCodec

    def fromUnicode(self, p_str): # real signature unknown; restored from __doc__
        """ fromUnicode(self, str) -> QByteArray """
        return QByteArray

    def makeDecoder(self, flags, QTextCodec_ConversionFlags=None, QTextCodec_ConversionFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ makeDecoder(self, flags: Union[QTextCodec.ConversionFlags, QTextCodec.ConversionFlag] = QTextCodec.DefaultConversion) -> QTextDecoder """
        pass

    def makeEncoder(self, flags, QTextCodec_ConversionFlags=None, QTextCodec_ConversionFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ makeEncoder(self, flags: Union[QTextCodec.ConversionFlags, QTextCodec.ConversionFlag] = QTextCodec.DefaultConversion) -> QTextEncoder """
        pass

    def mibEnum(self): # real signature unknown; restored from __doc__
        """ mibEnum(self) -> int """
        return 0

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> QByteArray """
        return QByteArray

    def setCodecForLocale(self, QTextCodec): # real signature unknown; restored from __doc__
        """ setCodecForLocale(QTextCodec) """
        pass

    def toUnicode(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        toUnicode(self, Union[QByteArray, bytes, bytearray]) -> str
        toUnicode(self, str) -> str
        toUnicode(self, bytes, state: QTextCodec.ConverterState = None) -> str
        """
        return ""

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    ConvertInvalidToNull = -2147483648
    DefaultConversion = 0
    IgnoreHeader = 1


