# encoding: utf-8
# module PyQt5.QtNetwork
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QNetworkProxyQuery(__sip.simplewrapper):
    """
    QNetworkProxyQuery()
    QNetworkProxyQuery(QUrl, type: QNetworkProxyQuery.QueryType = QNetworkProxyQuery.UrlRequest)
    QNetworkProxyQuery(str, int, protocolTag: str = '', type: QNetworkProxyQuery.QueryType = QNetworkProxyQuery.TcpSocket)
    QNetworkProxyQuery(int, protocolTag: str = '', type: QNetworkProxyQuery.QueryType = QNetworkProxyQuery.TcpServer)
    QNetworkProxyQuery(QNetworkConfiguration, QUrl, queryType: QNetworkProxyQuery.QueryType = QNetworkProxyQuery.UrlRequest)
    QNetworkProxyQuery(QNetworkConfiguration, str, int, protocolTag: str = '', type: QNetworkProxyQuery.QueryType = QNetworkProxyQuery.TcpSocket)
    QNetworkProxyQuery(QNetworkConfiguration, int, protocolTag: str = '', type: QNetworkProxyQuery.QueryType = QNetworkProxyQuery.TcpServer)
    QNetworkProxyQuery(QNetworkProxyQuery)
    """
    def localPort(self): # real signature unknown; restored from __doc__
        """ localPort(self) -> int """
        return 0

    def networkConfiguration(self): # real signature unknown; restored from __doc__
        """ networkConfiguration(self) -> QNetworkConfiguration """
        return QNetworkConfiguration

    def peerHostName(self): # real signature unknown; restored from __doc__
        """ peerHostName(self) -> str """
        return ""

    def peerPort(self): # real signature unknown; restored from __doc__
        """ peerPort(self) -> int """
        return 0

    def protocolTag(self): # real signature unknown; restored from __doc__
        """ protocolTag(self) -> str """
        return ""

    def queryType(self): # real signature unknown; restored from __doc__
        """ queryType(self) -> QNetworkProxyQuery.QueryType """
        pass

    def setLocalPort(self, p_int): # real signature unknown; restored from __doc__
        """ setLocalPort(self, int) """
        pass

    def setNetworkConfiguration(self, QNetworkConfiguration): # real signature unknown; restored from __doc__
        """ setNetworkConfiguration(self, QNetworkConfiguration) """
        pass

    def setPeerHostName(self, p_str): # real signature unknown; restored from __doc__
        """ setPeerHostName(self, str) """
        pass

    def setPeerPort(self, p_int): # real signature unknown; restored from __doc__
        """ setPeerPort(self, int) """
        pass

    def setProtocolTag(self, p_str): # real signature unknown; restored from __doc__
        """ setProtocolTag(self, str) """
        pass

    def setQueryType(self, QNetworkProxyQuery_QueryType): # real signature unknown; restored from __doc__
        """ setQueryType(self, QNetworkProxyQuery.QueryType) """
        pass

    def setUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ setUrl(self, QUrl) """
        pass

    def swap(self, QNetworkProxyQuery): # real signature unknown; restored from __doc__
        """ swap(self, QNetworkProxyQuery) """
        pass

    def url(self): # real signature unknown; restored from __doc__
        """ url(self) -> QUrl """
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


    SctpServer = 102
    SctpSocket = 2
    TcpServer = 100
    TcpSocket = 0
    UdpSocket = 1
    UrlRequest = 101
    __hash__ = None


