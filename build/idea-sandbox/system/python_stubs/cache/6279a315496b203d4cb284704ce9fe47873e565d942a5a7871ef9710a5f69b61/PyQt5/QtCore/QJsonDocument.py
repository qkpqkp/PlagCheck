# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QJsonDocument(__sip.simplewrapper):
    """
    QJsonDocument()
    QJsonDocument(Dict[str, QJsonValue])
    QJsonDocument(Iterable[Union[QJsonValue, QJsonValue.Type, Dict[str, QJsonValue], bool, int, float, str]])
    QJsonDocument(QJsonDocument)
    """
    def array(self): # real signature unknown; restored from __doc__
        """ array(self) -> List[QJsonValue] """
        return []

    def fromBinaryData(self, Union, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ fromBinaryData(Union[QByteArray, bytes, bytearray], validation: QJsonDocument.DataValidation = QJsonDocument.Validate) -> QJsonDocument """
        pass

    def fromJson(self, Union, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ fromJson(Union[QByteArray, bytes, bytearray], error: QJsonParseError = None) -> QJsonDocument """
        pass

    def fromRawData(self, p_str, p_int, validation=None): # real signature unknown; restored from __doc__
        """ fromRawData(str, int, validation: QJsonDocument.DataValidation = QJsonDocument.Validate) -> QJsonDocument """
        return QJsonDocument

    def fromVariant(self, Any): # real signature unknown; restored from __doc__
        """ fromVariant(Any) -> QJsonDocument """
        return QJsonDocument

    def isArray(self): # real signature unknown; restored from __doc__
        """ isArray(self) -> bool """
        return False

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isObject(self): # real signature unknown; restored from __doc__
        """ isObject(self) -> bool """
        return False

    def object(self): # real signature unknown; restored from __doc__
        """ object(self) -> Dict[str, QJsonValue] """
        return {}

    def rawData(self): # real signature unknown; restored from __doc__
        """ rawData(self) -> Tuple[str, int] """
        pass

    def setArray(self, Iterable, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setArray(self, Iterable[Union[QJsonValue, QJsonValue.Type, Dict[str, QJsonValue], bool, int, float, str]]) """
        pass

    def setObject(self, Dict, p_str=None, QJsonValue=None): # real signature unknown; restored from __doc__
        """ setObject(self, Dict[str, QJsonValue]) """
        pass

    def swap(self, QJsonDocument): # real signature unknown; restored from __doc__
        """ swap(self, QJsonDocument) """
        pass

    def toBinaryData(self): # real signature unknown; restored from __doc__
        """ toBinaryData(self) -> QByteArray """
        return QByteArray

    def toJson(self, QJsonDocument_JsonFormat=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        toJson(self) -> QByteArray
        toJson(self, QJsonDocument.JsonFormat) -> QByteArray
        """
        return QByteArray

    def toVariant(self): # real signature unknown; restored from __doc__
        """ toVariant(self) -> Any """
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


    BypassValidation = 1
    Compact = 1
    Indented = 0
    Validate = 0
    __hash__ = None


