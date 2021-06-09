# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QTextStream(__sip.simplewrapper):
    """
    QTextStream()
    QTextStream(QIODevice)
    QTextStream(QByteArray, mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.ReadWrite)
    """
    def atEnd(self): # real signature unknown; restored from __doc__
        """ atEnd(self) -> bool """
        return False

    def autoDetectUnicode(self): # real signature unknown; restored from __doc__
        """ autoDetectUnicode(self) -> bool """
        return False

    def codec(self): # real signature unknown; restored from __doc__
        """ codec(self) -> QTextCodec """
        return QTextCodec

    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> QIODevice """
        return QIODevice

    def fieldAlignment(self): # real signature unknown; restored from __doc__
        """ fieldAlignment(self) -> QTextStream.FieldAlignment """
        pass

    def fieldWidth(self): # real signature unknown; restored from __doc__
        """ fieldWidth(self) -> int """
        return 0

    def flush(self): # real signature unknown; restored from __doc__
        """ flush(self) """
        pass

    def generateByteOrderMark(self): # real signature unknown; restored from __doc__
        """ generateByteOrderMark(self) -> bool """
        return False

    def integerBase(self): # real signature unknown; restored from __doc__
        """ integerBase(self) -> int """
        return 0

    def locale(self): # real signature unknown; restored from __doc__
        """ locale(self) -> QLocale """
        return QLocale

    def numberFlags(self): # real signature unknown; restored from __doc__
        """ numberFlags(self) -> QTextStream.NumberFlags """
        pass

    def padChar(self): # real signature unknown; restored from __doc__
        """ padChar(self) -> str """
        return ""

    def pos(self): # real signature unknown; restored from __doc__
        """ pos(self) -> int """
        return 0

    def read(self, p_int): # real signature unknown; restored from __doc__
        """ read(self, int) -> str """
        return ""

    def readAll(self): # real signature unknown; restored from __doc__
        """ readAll(self) -> str """
        return ""

    def readLine(self, maxLength=0): # real signature unknown; restored from __doc__
        """ readLine(self, maxLength: int = 0) -> str """
        return ""

    def realNumberNotation(self): # real signature unknown; restored from __doc__
        """ realNumberNotation(self) -> QTextStream.RealNumberNotation """
        pass

    def realNumberPrecision(self): # real signature unknown; restored from __doc__
        """ realNumberPrecision(self) -> int """
        return 0

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) """
        pass

    def resetStatus(self): # real signature unknown; restored from __doc__
        """ resetStatus(self) """
        pass

    def seek(self, p_int): # real signature unknown; restored from __doc__
        """ seek(self, int) -> bool """
        return False

    def setAutoDetectUnicode(self, bool): # real signature unknown; restored from __doc__
        """ setAutoDetectUnicode(self, bool) """
        pass

    def setCodec(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setCodec(self, QTextCodec)
        setCodec(self, str)
        """
        pass

    def setDevice(self, QIODevice): # real signature unknown; restored from __doc__
        """ setDevice(self, QIODevice) """
        pass

    def setFieldAlignment(self, QTextStream_FieldAlignment): # real signature unknown; restored from __doc__
        """ setFieldAlignment(self, QTextStream.FieldAlignment) """
        pass

    def setFieldWidth(self, p_int): # real signature unknown; restored from __doc__
        """ setFieldWidth(self, int) """
        pass

    def setGenerateByteOrderMark(self, bool): # real signature unknown; restored from __doc__
        """ setGenerateByteOrderMark(self, bool) """
        pass

    def setIntegerBase(self, p_int): # real signature unknown; restored from __doc__
        """ setIntegerBase(self, int) """
        pass

    def setLocale(self, QLocale): # real signature unknown; restored from __doc__
        """ setLocale(self, QLocale) """
        pass

    def setNumberFlags(self, Union, QTextStream_NumberFlags=None, QTextStream_NumberFlag=None): # real signature unknown; restored from __doc__
        """ setNumberFlags(self, Union[QTextStream.NumberFlags, QTextStream.NumberFlag]) """
        pass

    def setPadChar(self, p_str): # real signature unknown; restored from __doc__
        """ setPadChar(self, str) """
        pass

    def setRealNumberNotation(self, QTextStream_RealNumberNotation): # real signature unknown; restored from __doc__
        """ setRealNumberNotation(self, QTextStream.RealNumberNotation) """
        pass

    def setRealNumberPrecision(self, p_int): # real signature unknown; restored from __doc__
        """ setRealNumberPrecision(self, int) """
        pass

    def setStatus(self, QTextStream_Status): # real signature unknown; restored from __doc__
        """ setStatus(self, QTextStream.Status) """
        pass

    def skipWhiteSpace(self): # real signature unknown; restored from __doc__
        """ skipWhiteSpace(self) """
        pass

    def status(self): # real signature unknown; restored from __doc__
        """ status(self) -> QTextStream.Status """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AlignAccountingStyle = 3
    AlignCenter = 2
    AlignLeft = 0
    AlignRight = 1
    FixedNotation = 1
    ForcePoint = 2
    ForceSign = 4
    Ok = 0
    ReadCorruptData = 2
    ReadPastEnd = 1
    ScientificNotation = 2
    ShowBase = 1
    SmartNotation = 0
    UppercaseBase = 8
    UppercaseDigits = 16
    WriteFailed = 3


