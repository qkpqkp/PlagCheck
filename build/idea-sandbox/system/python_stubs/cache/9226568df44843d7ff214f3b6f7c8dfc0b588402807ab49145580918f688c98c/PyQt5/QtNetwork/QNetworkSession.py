# encoding: utf-8
# module PyQt5.QtNetwork
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QNetworkSession(__PyQt5_QtCore.QObject):
    """ QNetworkSession(QNetworkConfiguration, parent: QObject = None) """
    def accept(self): # real signature unknown; restored from __doc__
        """ accept(self) """
        pass

    def activeTime(self): # real signature unknown; restored from __doc__
        """ activeTime(self) -> int """
        return 0

    def bytesReceived(self): # real signature unknown; restored from __doc__
        """ bytesReceived(self) -> int """
        return 0

    def bytesWritten(self): # real signature unknown; restored from __doc__
        """ bytesWritten(self) -> int """
        return 0

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) """
        pass

    def closed(self): # real signature unknown; restored from __doc__
        """ closed(self) [signal] """
        pass

    def configuration(self): # real signature unknown; restored from __doc__
        """ configuration(self) -> QNetworkConfiguration """
        return QNetworkConfiguration

    def connectNotify(self, QMetaMethod): # real signature unknown; restored from __doc__
        """ connectNotify(self, QMetaMethod) """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, QMetaMethod): # real signature unknown; restored from __doc__
        """ disconnectNotify(self, QMetaMethod) """
        pass

    def error(self, QNetworkSession_SessionError=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        error(self) -> QNetworkSession.SessionError
        error(self, QNetworkSession.SessionError) [signal]
        """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def ignore(self): # real signature unknown; restored from __doc__
        """ ignore(self) """
        pass

    def interface(self): # real signature unknown; restored from __doc__
        """ interface(self) -> QNetworkInterface """
        return QNetworkInterface

    def isOpen(self): # real signature unknown; restored from __doc__
        """ isOpen(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def migrate(self): # real signature unknown; restored from __doc__
        """ migrate(self) """
        pass

    def newConfigurationActivated(self): # real signature unknown; restored from __doc__
        """ newConfigurationActivated(self) [signal] """
        pass

    def open(self): # real signature unknown; restored from __doc__
        """ open(self) """
        pass

    def opened(self): # real signature unknown; restored from __doc__
        """ opened(self) [signal] """
        pass

    def preferredConfigurationChanged(self, QNetworkConfiguration, bool): # real signature unknown; restored from __doc__
        """ preferredConfigurationChanged(self, QNetworkConfiguration, bool) [signal] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def reject(self): # real signature unknown; restored from __doc__
        """ reject(self) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def sessionProperty(self, p_str): # real signature unknown; restored from __doc__
        """ sessionProperty(self, str) -> Any """
        pass

    def setSessionProperty(self, p_str, Any): # real signature unknown; restored from __doc__
        """ setSessionProperty(self, str, Any) """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QNetworkSession.State """
        pass

    def stateChanged(self, QNetworkSession_State): # real signature unknown; restored from __doc__
        """ stateChanged(self, QNetworkSession.State) [signal] """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def usagePolicies(self): # real signature unknown; restored from __doc__
        """ usagePolicies(self) -> QNetworkSession.UsagePolicies """
        pass

    def usagePoliciesChanged(self, Union, QNetworkSession_UsagePolicies=None, QNetworkSession_UsagePolicy=None): # real signature unknown; restored from __doc__
        """ usagePoliciesChanged(self, Union[QNetworkSession.UsagePolicies, QNetworkSession.UsagePolicy]) [signal] """
        pass

    def waitForOpened(self, msecs=30000): # real signature unknown; restored from __doc__
        """ waitForOpened(self, msecs: int = 30000) -> bool """
        return False

    def __init__(self, QNetworkConfiguration, parent=None): # real signature unknown; restored from __doc__
        pass

    Closing = 4
    Connected = 3
    Connecting = 2
    Disconnected = 5
    Invalid = 0
    InvalidConfigurationError = 4
    NoBackgroundTrafficPolicy = 1
    NoPolicy = 0
    NotAvailable = 1
    OperationNotSupportedError = 3
    Roaming = 6
    RoamingError = 2
    SessionAbortedError = 1
    UnknownSessionError = 0


