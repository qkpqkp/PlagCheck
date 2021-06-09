# encoding: utf-8
# module PyQt5.QtNetwork
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QSslKey(__sip.simplewrapper):
    """
    QSslKey()
    QSslKey(Union[QByteArray, bytes, bytearray], QSsl.KeyAlgorithm, encoding: QSsl.EncodingFormat = QSsl.Pem, type: QSsl.KeyType = QSsl.PrivateKey, passPhrase: Union[QByteArray, bytes, bytearray] = QByteArray())
    QSslKey(QIODevice, QSsl.KeyAlgorithm, encoding: QSsl.EncodingFormat = QSsl.Pem, type: QSsl.KeyType = QSsl.PrivateKey, passPhrase: Union[QByteArray, bytes, bytearray] = QByteArray())
    QSslKey(sip.voidptr, type: QSsl.KeyType = QSsl.PrivateKey)
    QSslKey(QSslKey)
    """
    def algorithm(self): # real signature unknown; restored from __doc__
        """ algorithm(self) -> QSsl.KeyAlgorithm """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def handle(self): # real signature unknown; restored from __doc__
        """ handle(self) -> sip.voidptr """
        pass

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def length(self): # real signature unknown; restored from __doc__
        """ length(self) -> int """
        return 0

    def swap(self, QSslKey): # real signature unknown; restored from __doc__
        """ swap(self, QSslKey) """
        pass

    def toDer(self, passPhrase, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ toDer(self, passPhrase: Union[QByteArray, bytes, bytearray] = QByteArray()) -> QByteArray """
        pass

    def toPem(self, passPhrase, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ toPem(self, passPhrase: Union[QByteArray, bytes, bytearray] = QByteArray()) -> QByteArray """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QSsl.KeyType """
        pass

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

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __hash__ = None


