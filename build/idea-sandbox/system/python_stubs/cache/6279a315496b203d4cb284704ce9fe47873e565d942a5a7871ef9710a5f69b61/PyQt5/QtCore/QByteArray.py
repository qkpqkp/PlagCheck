# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QByteArray(__sip.simplewrapper):
    """
    QByteArray()
    QByteArray(int, str)
    QByteArray(Union[QByteArray, bytes, bytearray])
    """
    def append(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        append(self, Union[QByteArray, bytes, bytearray]) -> QByteArray
        append(self, str) -> QByteArray
        append(self, int, str) -> QByteArray
        """
        return QByteArray

    def at(self, p_int): # real signature unknown; restored from __doc__
        """ at(self, int) -> str """
        return ""

    def capacity(self): # real signature unknown; restored from __doc__
        """ capacity(self) -> int """
        return 0

    def chop(self, p_int): # real signature unknown; restored from __doc__
        """ chop(self, int) """
        pass

    def chopped(self, p_int): # real signature unknown; restored from __doc__
        """ chopped(self, int) -> QByteArray """
        return QByteArray

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def compare(self, Union, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ compare(self, Union[QByteArray, bytes, bytearray], cs: Qt.CaseSensitivity = Qt.CaseSensitive) -> int """
        pass

    def contains(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ contains(self, Union[QByteArray, bytes, bytearray]) -> bool """
        return False

    def count(self, Union=None, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        count(self, Union[QByteArray, bytes, bytearray]) -> int
        count(self) -> int
        """
        return 0

    def data(self): # real signature unknown; restored from __doc__
        """ data(self) -> bytes """
        return b""

    def endsWith(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ endsWith(self, Union[QByteArray, bytes, bytearray]) -> bool """
        return False

    def fill(self, p_str, size=-1): # real signature unknown; restored from __doc__
        """ fill(self, str, size: int = -1) -> QByteArray """
        return QByteArray

    def fromBase64(self, Union, QByteArray=None, bytes=None, bytearray=None, *args=None, **kwargs=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        fromBase64(Union[QByteArray, bytes, bytearray]) -> QByteArray
        fromBase64(Union[QByteArray, bytes, bytearray], Union[QByteArray.Base64Options, QByteArray.Base64Option]) -> QByteArray
        """
        return QByteArray

    def fromHex(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ fromHex(Union[QByteArray, bytes, bytearray]) -> QByteArray """
        return QByteArray

    def fromPercentEncoding(self, Union, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ fromPercentEncoding(Union[QByteArray, bytes, bytearray], percent: str = '%') -> QByteArray """
        pass

    def fromRawData(self, bytes): # real signature unknown; restored from __doc__
        """ fromRawData(bytes) -> QByteArray """
        return QByteArray

    def indexOf(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        indexOf(self, Union[QByteArray, bytes, bytearray], from_: int = 0) -> int
        indexOf(self, str, from_: int = 0) -> int
        """
        return 0

    def insert(self, p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        insert(self, int, Union[QByteArray, bytes, bytearray]) -> QByteArray
        insert(self, int, str) -> QByteArray
        insert(self, int, int, str) -> QByteArray
        """
        return QByteArray

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isLower(self): # real signature unknown; restored from __doc__
        """ isLower(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isUpper(self): # real signature unknown; restored from __doc__
        """ isUpper(self) -> bool """
        return False

    def lastIndexOf(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        lastIndexOf(self, Union[QByteArray, bytes, bytearray], from_: int = -1) -> int
        lastIndexOf(self, str, from_: int = -1) -> int
        """
        return 0

    def left(self, p_int): # real signature unknown; restored from __doc__
        """ left(self, int) -> QByteArray """
        return QByteArray

    def leftJustified(self, p_int, fill=' ', truncate=False): # real signature unknown; restored from __doc__
        """ leftJustified(self, int, fill: str = ' ', truncate: bool = False) -> QByteArray """
        return QByteArray

    def length(self): # real signature unknown; restored from __doc__
        """ length(self) -> int """
        return 0

    def mid(self, p_int, length=-1): # real signature unknown; restored from __doc__
        """ mid(self, int, length: int = -1) -> QByteArray """
        return QByteArray

    def number(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        number(float, format: str = 'g', precision: int = 6) -> QByteArray
        number(int, base: int = 10) -> QByteArray
        """
        return QByteArray

    def prepend(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        prepend(self, Union[QByteArray, bytes, bytearray]) -> QByteArray
        prepend(self, int, str) -> QByteArray
        """
        return QByteArray

    def push_back(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ push_back(self, Union[QByteArray, bytes, bytearray]) """
        pass

    def push_front(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ push_front(self, Union[QByteArray, bytes, bytearray]) """
        pass

    def remove(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ remove(self, int, int) -> QByteArray """
        return QByteArray

    def repeated(self, p_int): # real signature unknown; restored from __doc__
        """ repeated(self, int) -> QByteArray """
        return QByteArray

    def replace(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        replace(self, int, int, Union[QByteArray, bytes, bytearray]) -> QByteArray
        replace(self, Union[QByteArray, bytes, bytearray], Union[QByteArray, bytes, bytearray]) -> QByteArray
        replace(self, str, Union[QByteArray, bytes, bytearray]) -> QByteArray
        """
        return QByteArray

    def reserve(self, p_int): # real signature unknown; restored from __doc__
        """ reserve(self, int) """
        pass

    def resize(self, p_int): # real signature unknown; restored from __doc__
        """ resize(self, int) """
        pass

    def right(self, p_int): # real signature unknown; restored from __doc__
        """ right(self, int) -> QByteArray """
        return QByteArray

    def rightJustified(self, p_int, fill=' ', truncate=False): # real signature unknown; restored from __doc__
        """ rightJustified(self, int, fill: str = ' ', truncate: bool = False) -> QByteArray """
        return QByteArray

    def setNum(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setNum(self, float, format: str = 'g', precision: int = 6) -> QByteArray
        setNum(self, int, base: int = 10) -> QByteArray
        """
        return QByteArray

    def simplified(self): # real signature unknown; restored from __doc__
        """ simplified(self) -> QByteArray """
        return QByteArray

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def split(self, p_str): # real signature unknown; restored from __doc__
        """ split(self, str) -> List[QByteArray] """
        return []

    def squeeze(self): # real signature unknown; restored from __doc__
        """ squeeze(self) """
        pass

    def startsWith(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ startsWith(self, Union[QByteArray, bytes, bytearray]) -> bool """
        return False

    def swap(self, QByteArray): # real signature unknown; restored from __doc__
        """ swap(self, QByteArray) """
        pass

    def toBase64(self, Union=None, QByteArray_Base64Options=None, QByteArray_Base64Option=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        toBase64(self) -> QByteArray
        toBase64(self, Union[QByteArray.Base64Options, QByteArray.Base64Option]) -> QByteArray
        """
        return QByteArray

    def toDouble(self): # real signature unknown; restored from __doc__
        """ toDouble(self) -> Tuple[float, bool] """
        pass

    def toFloat(self): # real signature unknown; restored from __doc__
        """ toFloat(self) -> Tuple[float, bool] """
        pass

    def toHex(self, p_str=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        toHex(self) -> QByteArray
        toHex(self, str) -> QByteArray
        """
        return QByteArray

    def toInt(self, base=10): # real signature unknown; restored from __doc__
        """ toInt(self, base: int = 10) -> Tuple[int, bool] """
        pass

    def toLong(self, base=10): # real signature unknown; restored from __doc__
        """ toLong(self, base: int = 10) -> Tuple[int, bool] """
        pass

    def toLongLong(self, base=10): # real signature unknown; restored from __doc__
        """ toLongLong(self, base: int = 10) -> Tuple[int, bool] """
        pass

    def toLower(self): # real signature unknown; restored from __doc__
        """ toLower(self) -> QByteArray """
        return QByteArray

    def toPercentEncoding(self, exclude, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ toPercentEncoding(self, exclude: Union[QByteArray, bytes, bytearray] = QByteArray(), include: Union[QByteArray, bytes, bytearray] = QByteArray(), percent: str = '%') -> QByteArray """
        pass

    def toShort(self, base=10): # real signature unknown; restored from __doc__
        """ toShort(self, base: int = 10) -> Tuple[int, bool] """
        pass

    def toUInt(self, base=10): # real signature unknown; restored from __doc__
        """ toUInt(self, base: int = 10) -> Tuple[int, bool] """
        pass

    def toULong(self, base=10): # real signature unknown; restored from __doc__
        """ toULong(self, base: int = 10) -> Tuple[int, bool] """
        pass

    def toULongLong(self, base=10): # real signature unknown; restored from __doc__
        """ toULongLong(self, base: int = 10) -> Tuple[int, bool] """
        pass

    def toUpper(self): # real signature unknown; restored from __doc__
        """ toUpper(self) -> QByteArray """
        return QByteArray

    def toUShort(self, base=10): # real signature unknown; restored from __doc__
        """ toUShort(self, base: int = 10) -> Tuple[int, bool] """
        pass

    def trimmed(self): # real signature unknown; restored from __doc__
        """ trimmed(self) -> QByteArray """
        return QByteArray

    def truncate(self, p_int): # real signature unknown; restored from __doc__
        """ truncate(self, int) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
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

    def __iadd__(self, *args, **kwargs): # real signature unknown
        """ Implement self+=value. """
        pass

    def __imul__(self, *args, **kwargs): # real signature unknown
        """ Implement self*=value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Base64Encoding = 0
    Base64UrlEncoding = 1
    KeepTrailingEquals = 0
    OmitTrailingEquals = 2


