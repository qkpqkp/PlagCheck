# encoding: utf-8
# module PyQt5.QtNetwork
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QSslDiffieHellmanParameters(__sip.simplewrapper):
    """
    QSslDiffieHellmanParameters()
    QSslDiffieHellmanParameters(QSslDiffieHellmanParameters)
    """
    def defaultParameters(self): # real signature unknown; restored from __doc__
        """ defaultParameters() -> QSslDiffieHellmanParameters """
        return QSslDiffieHellmanParameters

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> QSslDiffieHellmanParameters.Error """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def fromEncoded(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        fromEncoded(Union[QByteArray, bytes, bytearray], encoding: QSsl.EncodingFormat = QSsl.EncodingFormat.Pem) -> QSslDiffieHellmanParameters
        fromEncoded(QIODevice, encoding: QSsl.EncodingFormat = QSsl.EncodingFormat.Pem) -> QSslDiffieHellmanParameters
        """
        return QSslDiffieHellmanParameters

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def swap(self, QSslDiffieHellmanParameters): # real signature unknown; restored from __doc__
        """ swap(self, QSslDiffieHellmanParameters) """
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

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, QSslDiffieHellmanParameters=None): # real signature unknown; restored from __doc__ with multiple overloads
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


    InvalidInputDataError = 1
    NoError = 0
    UnsafeParametersError = 2


