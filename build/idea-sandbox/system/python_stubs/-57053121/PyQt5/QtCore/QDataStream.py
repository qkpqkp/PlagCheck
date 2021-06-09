# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QDataStream(__sip.simplewrapper):
    """
    QDataStream()
    QDataStream(QIODevice)
    QDataStream(QByteArray, Union[QIODevice.OpenMode, QIODevice.OpenModeFlag])
    QDataStream(QByteArray)
    """
    def abortTransaction(self): # real signature unknown; restored from __doc__
        """ abortTransaction(self) """
        pass

    def atEnd(self): # real signature unknown; restored from __doc__
        """ atEnd(self) -> bool """
        return False

    def byteOrder(self): # real signature unknown; restored from __doc__
        """ byteOrder(self) -> QDataStream.ByteOrder """
        pass

    def commitTransaction(self): # real signature unknown; restored from __doc__
        """ commitTransaction(self) -> bool """
        return False

    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> QIODevice """
        return QIODevice

    def floatingPointPrecision(self): # real signature unknown; restored from __doc__
        """ floatingPointPrecision(self) -> QDataStream.FloatingPointPrecision """
        pass

    def readBool(self): # real signature unknown; restored from __doc__
        """ readBool(self) -> bool """
        return False

    def readBytes(self): # real signature unknown; restored from __doc__
        """ readBytes(self) -> bytes """
        return b""

    def readDouble(self): # real signature unknown; restored from __doc__
        """ readDouble(self) -> float """
        return 0.0

    def readFloat(self): # real signature unknown; restored from __doc__
        """ readFloat(self) -> float """
        return 0.0

    def readInt(self): # real signature unknown; restored from __doc__
        """ readInt(self) -> int """
        return 0

    def readInt16(self): # real signature unknown; restored from __doc__
        """ readInt16(self) -> int """
        return 0

    def readInt32(self): # real signature unknown; restored from __doc__
        """ readInt32(self) -> int """
        return 0

    def readInt64(self): # real signature unknown; restored from __doc__
        """ readInt64(self) -> int """
        return 0

    def readInt8(self): # real signature unknown; restored from __doc__
        """ readInt8(self) -> int """
        return 0

    def readQString(self): # real signature unknown; restored from __doc__
        """ readQString(self) -> str """
        return ""

    def readQStringList(self): # real signature unknown; restored from __doc__
        """ readQStringList(self) -> List[str] """
        return []

    def readQVariant(self): # real signature unknown; restored from __doc__
        """ readQVariant(self) -> Any """
        pass

    def readQVariantHash(self): # real signature unknown; restored from __doc__
        """ readQVariantHash(self) -> Dict[str, Any] """
        return {}

    def readQVariantList(self): # real signature unknown; restored from __doc__
        """ readQVariantList(self) -> List[Any] """
        return []

    def readQVariantMap(self): # real signature unknown; restored from __doc__
        """ readQVariantMap(self) -> Dict[str, Any] """
        return {}

    def readRawData(self, p_int): # real signature unknown; restored from __doc__
        """ readRawData(self, int) -> bytes """
        return b""

    def readString(self): # real signature unknown; restored from __doc__
        """ readString(self) -> bytes """
        return b""

    def readUInt16(self): # real signature unknown; restored from __doc__
        """ readUInt16(self) -> int """
        return 0

    def readUInt32(self): # real signature unknown; restored from __doc__
        """ readUInt32(self) -> int """
        return 0

    def readUInt64(self): # real signature unknown; restored from __doc__
        """ readUInt64(self) -> int """
        return 0

    def readUInt8(self): # real signature unknown; restored from __doc__
        """ readUInt8(self) -> int """
        return 0

    def resetStatus(self): # real signature unknown; restored from __doc__
        """ resetStatus(self) """
        pass

    def rollbackTransaction(self): # real signature unknown; restored from __doc__
        """ rollbackTransaction(self) """
        pass

    def setByteOrder(self, QDataStream_ByteOrder): # real signature unknown; restored from __doc__
        """ setByteOrder(self, QDataStream.ByteOrder) """
        pass

    def setDevice(self, QIODevice): # real signature unknown; restored from __doc__
        """ setDevice(self, QIODevice) """
        pass

    def setFloatingPointPrecision(self, QDataStream_FloatingPointPrecision): # real signature unknown; restored from __doc__
        """ setFloatingPointPrecision(self, QDataStream.FloatingPointPrecision) """
        pass

    def setStatus(self, QDataStream_Status): # real signature unknown; restored from __doc__
        """ setStatus(self, QDataStream.Status) """
        pass

    def setVersion(self, p_int): # real signature unknown; restored from __doc__
        """ setVersion(self, int) """
        pass

    def skipRawData(self, p_int): # real signature unknown; restored from __doc__
        """ skipRawData(self, int) -> int """
        return 0

    def startTransaction(self): # real signature unknown; restored from __doc__
        """ startTransaction(self) """
        pass

    def status(self): # real signature unknown; restored from __doc__
        """ status(self) -> QDataStream.Status """
        pass

    def version(self): # real signature unknown; restored from __doc__
        """ version(self) -> int """
        return 0

    def writeBool(self, bool): # real signature unknown; restored from __doc__
        """ writeBool(self, bool) """
        pass

    def writeBytes(self, bytes): # real signature unknown; restored from __doc__
        """ writeBytes(self, bytes) -> QDataStream """
        return QDataStream

    def writeDouble(self, p_float): # real signature unknown; restored from __doc__
        """ writeDouble(self, float) """
        pass

    def writeFloat(self, p_float): # real signature unknown; restored from __doc__
        """ writeFloat(self, float) """
        pass

    def writeInt(self, p_int): # real signature unknown; restored from __doc__
        """ writeInt(self, int) """
        pass

    def writeInt16(self, p_int): # real signature unknown; restored from __doc__
        """ writeInt16(self, int) """
        pass

    def writeInt32(self, p_int): # real signature unknown; restored from __doc__
        """ writeInt32(self, int) """
        pass

    def writeInt64(self, p_int): # real signature unknown; restored from __doc__
        """ writeInt64(self, int) """
        pass

    def writeInt8(self, p_int): # real signature unknown; restored from __doc__
        """ writeInt8(self, int) """
        pass

    def writeQString(self, p_str): # real signature unknown; restored from __doc__
        """ writeQString(self, str) """
        pass

    def writeQStringList(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ writeQStringList(self, Iterable[str]) """
        pass

    def writeQVariant(self, Any): # real signature unknown; restored from __doc__
        """ writeQVariant(self, Any) """
        pass

    def writeQVariantHash(self, Dict, p_str=None, Any=None): # real signature unknown; restored from __doc__
        """ writeQVariantHash(self, Dict[str, Any]) """
        pass

    def writeQVariantList(self, Iterable, Any=None): # real signature unknown; restored from __doc__
        """ writeQVariantList(self, Iterable[Any]) """
        pass

    def writeQVariantMap(self, Dict, p_str=None, Any=None): # real signature unknown; restored from __doc__
        """ writeQVariantMap(self, Dict[str, Any]) """
        pass

    def writeRawData(self, bytes): # real signature unknown; restored from __doc__
        """ writeRawData(self, bytes) -> int """
        return 0

    def writeString(self, p_str): # real signature unknown; restored from __doc__
        """ writeString(self, str) """
        pass

    def writeUInt16(self, p_int): # real signature unknown; restored from __doc__
        """ writeUInt16(self, int) """
        pass

    def writeUInt32(self, p_int): # real signature unknown; restored from __doc__
        """ writeUInt32(self, int) """
        pass

    def writeUInt64(self, p_int): # real signature unknown; restored from __doc__
        """ writeUInt64(self, int) """
        pass

    def writeUInt8(self, p_int): # real signature unknown; restored from __doc__
        """ writeUInt8(self, int) """
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


    BigEndian = 0
    DoublePrecision = 1
    LittleEndian = 1
    Ok = 0
    Qt_1_0 = 1
    Qt_2_0 = 2
    Qt_2_1 = 3
    Qt_3_0 = 4
    Qt_3_1 = 5
    Qt_3_3 = 6
    Qt_4_0 = 7
    Qt_4_1 = 7
    Qt_4_2 = 8
    Qt_4_3 = 9
    Qt_4_4 = 10
    Qt_4_5 = 11
    Qt_4_6 = 12
    Qt_4_7 = 12
    Qt_4_8 = 12
    Qt_4_9 = 12
    Qt_5_0 = 13
    Qt_5_1 = 14
    Qt_5_10 = 17
    Qt_5_11 = 17
    Qt_5_12 = 18
    Qt_5_2 = 15
    Qt_5_3 = 15
    Qt_5_4 = 16
    Qt_5_5 = 16
    Qt_5_6 = 17
    Qt_5_7 = 17
    Qt_5_8 = 17
    Qt_5_9 = 17
    ReadCorruptData = 2
    ReadPastEnd = 1
    SinglePrecision = 0
    WriteFailed = 3


