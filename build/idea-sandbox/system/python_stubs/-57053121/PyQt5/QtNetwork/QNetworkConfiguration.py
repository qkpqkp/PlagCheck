# encoding: utf-8
# module PyQt5.QtNetwork
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QNetworkConfiguration(__sip.simplewrapper):
    """
    QNetworkConfiguration()
    QNetworkConfiguration(QNetworkConfiguration)
    """
    def bearerType(self): # real signature unknown; restored from __doc__
        """ bearerType(self) -> QNetworkConfiguration.BearerType """
        pass

    def bearerTypeFamily(self): # real signature unknown; restored from __doc__
        """ bearerTypeFamily(self) -> QNetworkConfiguration.BearerType """
        pass

    def bearerTypeName(self): # real signature unknown; restored from __doc__
        """ bearerTypeName(self) -> str """
        return ""

    def children(self): # real signature unknown; restored from __doc__
        """ children(self) -> List[QNetworkConfiguration] """
        return []

    def connectTimeout(self): # real signature unknown; restored from __doc__
        """ connectTimeout(self) -> int """
        return 0

    def identifier(self): # real signature unknown; restored from __doc__
        """ identifier(self) -> str """
        return ""

    def isRoamingAvailable(self): # real signature unknown; restored from __doc__
        """ isRoamingAvailable(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def purpose(self): # real signature unknown; restored from __doc__
        """ purpose(self) -> QNetworkConfiguration.Purpose """
        pass

    def setConnectTimeout(self, p_int): # real signature unknown; restored from __doc__
        """ setConnectTimeout(self, int) -> bool """
        return False

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QNetworkConfiguration.StateFlags """
        pass

    def swap(self, QNetworkConfiguration): # real signature unknown; restored from __doc__
        """ swap(self, QNetworkConfiguration) """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QNetworkConfiguration.Type """
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

    def __init__(self, QNetworkConfiguration=None): # real signature unknown; restored from __doc__ with multiple overloads
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


    Active = 14
    Bearer2G = 3
    Bearer3G = 11
    Bearer4G = 12
    BearerBluetooth = 7
    BearerCDMA2000 = 4
    BearerEthernet = 1
    BearerEVDO = 9
    BearerHSPA = 6
    BearerLTE = 10
    BearerUnknown = 0
    BearerWCDMA = 5
    BearerWiMAX = 8
    BearerWLAN = 2
    Defined = 2
    Discovered = 6
    InternetAccessPoint = 0
    Invalid = 3
    PrivatePurpose = 2
    PublicPurpose = 1
    ServiceNetwork = 1
    ServiceSpecificPurpose = 3
    Undefined = 1
    UnknownPurpose = 0
    UserChoice = 2
    __hash__ = None


