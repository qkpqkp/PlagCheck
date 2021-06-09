# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QIODevice import QIODevice

class QBuffer(QIODevice):
    """
    QBuffer(parent: QObject = None)
    QBuffer(QByteArray, parent: QObject = None)
    """
    def atEnd(self): # real signature unknown; restored from __doc__
        """ atEnd(self) -> bool """
        return False

    def buffer(self): # real signature unknown; restored from __doc__
        """ buffer(self) -> QByteArray """
        return QByteArray

    def canReadLine(self): # real signature unknown; restored from __doc__
        """ canReadLine(self) -> bool """
        return False

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) """
        pass

    def connectNotify(self, QMetaMethod): # real signature unknown; restored from __doc__
        """ connectNotify(self, QMetaMethod) """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def data(self): # real signature unknown; restored from __doc__
        """ data(self) -> QByteArray """
        return QByteArray

    def disconnectNotify(self, QMetaMethod): # real signature unknown; restored from __doc__
        """ disconnectNotify(self, QMetaMethod) """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def open(self, Union, QIODevice_OpenMode=None, QIODevice_OpenModeFlag=None): # real signature unknown; restored from __doc__
        """ open(self, Union[QIODevice.OpenMode, QIODevice.OpenModeFlag]) -> bool """
        return False

    def pos(self): # real signature unknown; restored from __doc__
        """ pos(self) -> int """
        return 0

    def readData(self, p_int): # real signature unknown; restored from __doc__
        """ readData(self, int) -> bytes """
        return b""

    def readLineData(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def seek(self, p_int): # real signature unknown; restored from __doc__
        """ seek(self, int) -> bool """
        return False

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setBuffer(self, QByteArray): # real signature unknown; restored from __doc__
        """ setBuffer(self, QByteArray) """
        pass

    def setData(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setData(self, Union[QByteArray, bytes, bytearray])
        setData(self, bytes)
        """
        pass

    def setErrorString(self, *args, **kwargs): # real signature unknown
        pass

    def setOpenMode(self, *args, **kwargs): # real signature unknown
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def writeData(self, bytes): # real signature unknown; restored from __doc__
        """ writeData(self, bytes) -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


