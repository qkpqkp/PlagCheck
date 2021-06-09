# encoding: utf-8
# module PyQt5.QtNetwork
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QNetworkDatagram(__sip.simplewrapper):
    """
    QNetworkDatagram()
    QNetworkDatagram(Union[QByteArray, bytes, bytearray], destinationAddress: Union[QHostAddress, QHostAddress.SpecialAddress] = QHostAddress(), port: int = 0)
    QNetworkDatagram(QNetworkDatagram)
    """
    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def data(self): # real signature unknown; restored from __doc__
        """ data(self) -> QByteArray """
        pass

    def destinationAddress(self): # real signature unknown; restored from __doc__
        """ destinationAddress(self) -> QHostAddress """
        return QHostAddress

    def destinationPort(self): # real signature unknown; restored from __doc__
        """ destinationPort(self) -> int """
        return 0

    def hopLimit(self): # real signature unknown; restored from __doc__
        """ hopLimit(self) -> int """
        return 0

    def interfaceIndex(self): # real signature unknown; restored from __doc__
        """ interfaceIndex(self) -> int """
        return 0

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def makeReply(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ makeReply(self, Union[QByteArray, bytes, bytearray]) -> QNetworkDatagram """
        return QNetworkDatagram

    def senderAddress(self): # real signature unknown; restored from __doc__
        """ senderAddress(self) -> QHostAddress """
        return QHostAddress

    def senderPort(self): # real signature unknown; restored from __doc__
        """ senderPort(self) -> int """
        return 0

    def setData(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setData(self, Union[QByteArray, bytes, bytearray]) """
        pass

    def setDestination(self, Union, QHostAddress=None, QHostAddress_SpecialAddress=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setDestination(self, Union[QHostAddress, QHostAddress.SpecialAddress], int) """
        pass

    def setHopLimit(self, p_int): # real signature unknown; restored from __doc__
        """ setHopLimit(self, int) """
        pass

    def setInterfaceIndex(self, p_int): # real signature unknown; restored from __doc__
        """ setInterfaceIndex(self, int) """
        pass

    def setSender(self, Union, QHostAddress=None, QHostAddress_SpecialAddress=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setSender(self, Union[QHostAddress, QHostAddress.SpecialAddress], port: int = 0) """
        pass

    def swap(self, QNetworkDatagram): # real signature unknown; restored from __doc__
        """ swap(self, QNetworkDatagram) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



