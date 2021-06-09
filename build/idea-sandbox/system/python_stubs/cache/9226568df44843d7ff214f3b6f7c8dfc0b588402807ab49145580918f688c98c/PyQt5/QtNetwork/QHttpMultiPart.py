# encoding: utf-8
# module PyQt5.QtNetwork
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QHttpMultiPart(__PyQt5_QtCore.QObject):
    """
    QHttpMultiPart(parent: QObject = None)
    QHttpMultiPart(QHttpMultiPart.ContentType, parent: QObject = None)
    """
    def append(self, QHttpPart): # real signature unknown; restored from __doc__
        """ append(self, QHttpPart) """
        pass

    def boundary(self): # real signature unknown; restored from __doc__
        """ boundary(self) -> QByteArray """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setBoundary(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setBoundary(self, Union[QByteArray, bytes, bytearray]) """
        pass

    def setContentType(self, QHttpMultiPart_ContentType): # real signature unknown; restored from __doc__
        """ setContentType(self, QHttpMultiPart.ContentType) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AlternativeType = 3
    FormDataType = 2
    MixedType = 0
    RelatedType = 1


