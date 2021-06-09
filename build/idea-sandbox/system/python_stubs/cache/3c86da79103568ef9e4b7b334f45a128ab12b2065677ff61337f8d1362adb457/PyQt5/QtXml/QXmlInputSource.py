# encoding: utf-8
# module PyQt5.QtXml
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtXml.pyd
# by generator 1.147
# no doc

# imports
import sip as __sip


class QXmlInputSource(__sip.simplewrapper):
    """
    QXmlInputSource()
    QXmlInputSource(QIODevice)
    QXmlInputSource(QXmlInputSource)
    """
    def data(self): # real signature unknown; restored from __doc__
        """ data(self) -> str """
        return ""

    def fetchData(self): # real signature unknown; restored from __doc__
        """ fetchData(self) """
        pass

    def fromRawData(self, Union, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ fromRawData(self, Union[QByteArray, bytes, bytearray], beginning: bool = False) -> str """
        pass

    def next(self): # real signature unknown; restored from __doc__
        """ next(self) -> str """
        return ""

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) """
        pass

    def setData(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setData(self, str)
        setData(self, Union[QByteArray, bytes, bytearray])
        """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    EndOfData = 65534
    EndOfDocument = 65535


