# encoding: utf-8
# module PyQt5.QtNetwork
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QAbstractNetworkCache(__PyQt5_QtCore.QObject):
    """ QAbstractNetworkCache(parent: QObject = None) """
    def cacheSize(self): # real signature unknown; restored from __doc__
        """ cacheSize(self) -> int """
        return 0

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def data(self, QUrl): # real signature unknown; restored from __doc__
        """ data(self, QUrl) -> QIODevice """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def insert(self, QIODevice): # real signature unknown; restored from __doc__
        """ insert(self, QIODevice) """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def metaData(self, QUrl): # real signature unknown; restored from __doc__
        """ metaData(self, QUrl) -> QNetworkCacheMetaData """
        return QNetworkCacheMetaData

    def prepare(self, QNetworkCacheMetaData): # real signature unknown; restored from __doc__
        """ prepare(self, QNetworkCacheMetaData) -> QIODevice """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def remove(self, QUrl): # real signature unknown; restored from __doc__
        """ remove(self, QUrl) -> bool """
        return False

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMetaData(self, QNetworkCacheMetaData): # real signature unknown; restored from __doc__
        """ updateMetaData(self, QNetworkCacheMetaData) """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


