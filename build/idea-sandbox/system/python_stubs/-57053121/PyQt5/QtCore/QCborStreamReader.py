# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QCborStreamReader(__sip.simplewrapper):
    """
    QCborStreamReader()
    QCborStreamReader(Union[QByteArray, bytes, bytearray])
    QCborStreamReader(QIODevice)
    """
    def addData(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ addData(self, Union[QByteArray, bytes, bytearray]) """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def containerDepth(self): # real signature unknown; restored from __doc__
        """ containerDepth(self) -> int """
        return 0

    def currentOffset(self): # real signature unknown; restored from __doc__
        """ currentOffset(self) -> int """
        return 0

    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> QIODevice """
        return QIODevice

    def enterContainer(self): # real signature unknown; restored from __doc__
        """ enterContainer(self) -> bool """
        return False

    def hasNext(self): # real signature unknown; restored from __doc__
        """ hasNext(self) -> bool """
        return False

    def isArray(self): # real signature unknown; restored from __doc__
        """ isArray(self) -> bool """
        return False

    def isBool(self): # real signature unknown; restored from __doc__
        """ isBool(self) -> bool """
        return False

    def isByteArray(self): # real signature unknown; restored from __doc__
        """ isByteArray(self) -> bool """
        return False

    def isContainer(self): # real signature unknown; restored from __doc__
        """ isContainer(self) -> bool """
        return False

    def isDouble(self): # real signature unknown; restored from __doc__
        """ isDouble(self) -> bool """
        return False

    def isFalse(self): # real signature unknown; restored from __doc__
        """ isFalse(self) -> bool """
        return False

    def isFloat(self): # real signature unknown; restored from __doc__
        """ isFloat(self) -> bool """
        return False

    def isFloat16(self): # real signature unknown; restored from __doc__
        """ isFloat16(self) -> bool """
        return False

    def isInteger(self): # real signature unknown; restored from __doc__
        """ isInteger(self) -> bool """
        return False

    def isInvalid(self): # real signature unknown; restored from __doc__
        """ isInvalid(self) -> bool """
        return False

    def isLengthKnown(self): # real signature unknown; restored from __doc__
        """ isLengthKnown(self) -> bool """
        return False

    def isMap(self): # real signature unknown; restored from __doc__
        """ isMap(self) -> bool """
        return False

    def isNegativeInteger(self): # real signature unknown; restored from __doc__
        """ isNegativeInteger(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isSimpleType(self, QCborSimpleType=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        isSimpleType(self) -> bool
        isSimpleType(self, QCborSimpleType) -> bool
        """
        return False

    def isString(self): # real signature unknown; restored from __doc__
        """ isString(self) -> bool """
        return False

    def isTag(self): # real signature unknown; restored from __doc__
        """ isTag(self) -> bool """
        return False

    def isTrue(self): # real signature unknown; restored from __doc__
        """ isTrue(self) -> bool """
        return False

    def isUndefined(self): # real signature unknown; restored from __doc__
        """ isUndefined(self) -> bool """
        return False

    def isUnsignedInteger(self): # real signature unknown; restored from __doc__
        """ isUnsignedInteger(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def lastError(self): # real signature unknown; restored from __doc__
        """ lastError(self) -> QCborError """
        return QCborError

    def leaveContainer(self): # real signature unknown; restored from __doc__
        """ leaveContainer(self) -> bool """
        return False

    def length(self): # real signature unknown; restored from __doc__
        """ length(self) -> int """
        return 0

    def next(self, maxRecursion=10000): # real signature unknown; restored from __doc__
        """ next(self, maxRecursion: int = 10000) -> bool """
        return False

    def parentContainerType(self): # real signature unknown; restored from __doc__
        """ parentContainerType(self) -> QCborStreamReader.Type """
        pass

    def readByteArray(self): # real signature unknown; restored from __doc__
        """ readByteArray(self) -> Tuple[QByteArray, QCborStreamReader.StringResultCode] """
        pass

    def readString(self): # real signature unknown; restored from __doc__
        """ readString(self) -> Tuple[str, QCborStreamReader.StringResultCode] """
        pass

    def reparse(self): # real signature unknown; restored from __doc__
        """ reparse(self) """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) """
        pass

    def setDevice(self, QIODevice): # real signature unknown; restored from __doc__
        """ setDevice(self, QIODevice) """
        pass

    def toBool(self): # real signature unknown; restored from __doc__
        """ toBool(self) -> bool """
        return False

    def toDouble(self): # real signature unknown; restored from __doc__
        """ toDouble(self) -> float """
        return 0.0

    def toInteger(self): # real signature unknown; restored from __doc__
        """ toInteger(self) -> int """
        return 0

    def toSimpleType(self): # real signature unknown; restored from __doc__
        """ toSimpleType(self) -> QCborSimpleType """
        return QCborSimpleType

    def toUnsignedInteger(self): # real signature unknown; restored from __doc__
        """ toUnsignedInteger(self) -> int """
        return 0

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QCborStreamReader.Type """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Array = 128
    ByteArray = 64
    ByteString = 64
    Double = 251
    EndOfString = 0
    Error = -1
    Float = 250
    Float16 = 249
    HalfFloat = 249
    Invalid = 255
    Map = 160
    NegativeInteger = 32
    Ok = 1
    SimpleType = 224
    String = 96
    Tag = 192
    TextString = 96
    UnsignedInteger = 0


