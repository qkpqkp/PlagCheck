# encoding: utf-8
# module PyQt5.QtNetwork
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QNetworkCookie(__sip.simplewrapper):
    """
    QNetworkCookie(name: Union[QByteArray, bytes, bytearray] = QByteArray(), value: Union[QByteArray, bytes, bytearray] = QByteArray())
    QNetworkCookie(QNetworkCookie)
    """
    def domain(self): # real signature unknown; restored from __doc__
        """ domain(self) -> str """
        return ""

    def expirationDate(self): # real signature unknown; restored from __doc__
        """ expirationDate(self) -> QDateTime """
        pass

    def hasSameIdentifier(self, QNetworkCookie): # real signature unknown; restored from __doc__
        """ hasSameIdentifier(self, QNetworkCookie) -> bool """
        return False

    def isHttpOnly(self): # real signature unknown; restored from __doc__
        """ isHttpOnly(self) -> bool """
        return False

    def isSecure(self): # real signature unknown; restored from __doc__
        """ isSecure(self) -> bool """
        return False

    def isSessionCookie(self): # real signature unknown; restored from __doc__
        """ isSessionCookie(self) -> bool """
        return False

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> QByteArray """
        pass

    def normalize(self, QUrl): # real signature unknown; restored from __doc__
        """ normalize(self, QUrl) """
        pass

    def parseCookies(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ parseCookies(Union[QByteArray, bytes, bytearray]) -> List[QNetworkCookie] """
        return []

    def path(self): # real signature unknown; restored from __doc__
        """ path(self) -> str """
        return ""

    def setDomain(self, p_str): # real signature unknown; restored from __doc__
        """ setDomain(self, str) """
        pass

    def setExpirationDate(self, Union, QDateTime=None, datetime_datetime=None): # real signature unknown; restored from __doc__
        """ setExpirationDate(self, Union[QDateTime, datetime.datetime]) """
        pass

    def setHttpOnly(self, bool): # real signature unknown; restored from __doc__
        """ setHttpOnly(self, bool) """
        pass

    def setName(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setName(self, Union[QByteArray, bytes, bytearray]) """
        pass

    def setPath(self, p_str): # real signature unknown; restored from __doc__
        """ setPath(self, str) """
        pass

    def setSecure(self, bool): # real signature unknown; restored from __doc__
        """ setSecure(self, bool) """
        pass

    def setValue(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setValue(self, Union[QByteArray, bytes, bytearray]) """
        pass

    def swap(self, QNetworkCookie): # real signature unknown; restored from __doc__
        """ swap(self, QNetworkCookie) """
        pass

    def toRawForm(self, form=None): # real signature unknown; restored from __doc__
        """ toRawForm(self, form: QNetworkCookie.RawForm = QNetworkCookie.Full) -> QByteArray """
        pass

    def value(self): # real signature unknown; restored from __doc__
        """ value(self) -> QByteArray """
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


    Full = 1
    NameAndValueOnly = 0
    __hash__ = None


