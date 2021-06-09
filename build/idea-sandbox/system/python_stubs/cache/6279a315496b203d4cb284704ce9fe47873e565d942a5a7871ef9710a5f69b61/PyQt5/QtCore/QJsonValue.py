# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QJsonValue(__sip.simplewrapper):
    """
    QJsonValue(type: QJsonValue.Type = QJsonValue.Null)
    QJsonValue(Union[QJsonValue, QJsonValue.Type, Dict[str, QJsonValue], bool, int, float, str])
    """
    def fromVariant(self, Any): # real signature unknown; restored from __doc__
        """ fromVariant(Any) -> QJsonValue """
        return QJsonValue

    def isArray(self): # real signature unknown; restored from __doc__
        """ isArray(self) -> bool """
        return False

    def isBool(self): # real signature unknown; restored from __doc__
        """ isBool(self) -> bool """
        return False

    def isDouble(self): # real signature unknown; restored from __doc__
        """ isDouble(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isObject(self): # real signature unknown; restored from __doc__
        """ isObject(self) -> bool """
        return False

    def isString(self): # real signature unknown; restored from __doc__
        """ isString(self) -> bool """
        return False

    def isUndefined(self): # real signature unknown; restored from __doc__
        """ isUndefined(self) -> bool """
        return False

    def swap(self, QJsonValue): # real signature unknown; restored from __doc__
        """ swap(self, QJsonValue) """
        pass

    def toArray(self, Iterable=None, *args=None, **kwargs=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        toArray(self) -> List[QJsonValue]
        toArray(self, Iterable[Union[QJsonValue, QJsonValue.Type, Dict[str, QJsonValue], bool, int, float, str]]) -> List[QJsonValue]
        """
        return []

    def toBool(self, defaultValue=False): # real signature unknown; restored from __doc__
        """ toBool(self, defaultValue: bool = False) -> bool """
        return False

    def toDouble(self, defaultValue=0): # real signature unknown; restored from __doc__
        """ toDouble(self, defaultValue: float = 0) -> float """
        return 0.0

    def toInt(self, defaultValue=0): # real signature unknown; restored from __doc__
        """ toInt(self, defaultValue: int = 0) -> int """
        return 0

    def toObject(self, Dict=None, p_str=None, QJsonValue=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        toObject(self) -> Dict[str, QJsonValue]
        toObject(self, Dict[str, QJsonValue]) -> Dict[str, QJsonValue]
        """
        return {}

    def toString(self, p_str=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        toString(self) -> str
        toString(self, str) -> str
        """
        return ""

    def toVariant(self): # real signature unknown; restored from __doc__
        """ toVariant(self) -> Any """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QJsonValue.Type """
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


    Array = 4
    Bool = 1
    Double = 2
    Null = 0
    Object = 5
    String = 3
    Undefined = 128


