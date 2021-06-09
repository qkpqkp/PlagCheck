# encoding: utf-8
# module PyQt5.QtNetwork
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QHostInfo(__sip.simplewrapper):
    """
    QHostInfo(id: int = -1)
    QHostInfo(QHostInfo)
    """
    def abortHostLookup(self, p_int): # real signature unknown; restored from __doc__
        """ abortHostLookup(int) """
        pass

    def addresses(self): # real signature unknown; restored from __doc__
        """ addresses(self) -> List[QHostAddress] """
        return []

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> QHostInfo.HostInfoError """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def fromName(self, p_str): # real signature unknown; restored from __doc__
        """ fromName(str) -> QHostInfo """
        return QHostInfo

    def hostName(self): # real signature unknown; restored from __doc__
        """ hostName(self) -> str """
        return ""

    def localDomainName(self): # real signature unknown; restored from __doc__
        """ localDomainName() -> str """
        return ""

    def localHostName(self): # real signature unknown; restored from __doc__
        """ localHostName() -> str """
        return ""

    def lookupHost(self, p_str, PYQT_SLOT): # real signature unknown; restored from __doc__
        """ lookupHost(str, PYQT_SLOT) -> int """
        return 0

    def lookupId(self): # real signature unknown; restored from __doc__
        """ lookupId(self) -> int """
        return 0

    def setAddresses(self, Iterable, Union=None, QHostAddress=None, QHostAddress_SpecialAddress=None): # real signature unknown; restored from __doc__
        """ setAddresses(self, Iterable[Union[QHostAddress, QHostAddress.SpecialAddress]]) """
        pass

    def setError(self, QHostInfo_HostInfoError): # real signature unknown; restored from __doc__
        """ setError(self, QHostInfo.HostInfoError) """
        pass

    def setErrorString(self, p_str): # real signature unknown; restored from __doc__
        """ setErrorString(self, str) """
        pass

    def setHostName(self, p_str): # real signature unknown; restored from __doc__
        """ setHostName(self, str) """
        pass

    def setLookupId(self, p_int): # real signature unknown; restored from __doc__
        """ setLookupId(self, int) """
        pass

    def swap(self, QHostInfo): # real signature unknown; restored from __doc__
        """ swap(self, QHostInfo) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    HostNotFound = 1
    NoError = 0
    UnknownError = 2


