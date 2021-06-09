# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QObject import QObject

class QFileSelector(QObject):
    """ QFileSelector(parent: QObject = None) """
    def allSelectors(self): # real signature unknown; restored from __doc__
        """ allSelectors(self) -> List[str] """
        return []

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def extraSelectors(self): # real signature unknown; restored from __doc__
        """ extraSelectors(self) -> List[str] """
        return []

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def select(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        select(self, str) -> str
        select(self, QUrl) -> QUrl
        """
        return "" or QUrl

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setExtraSelectors(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ setExtraSelectors(self, Iterable[str]) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


