# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QTextDocumentWriter(__sip.simplewrapper):
    """
    QTextDocumentWriter()
    QTextDocumentWriter(QIODevice, Union[QByteArray, bytes, bytearray])
    QTextDocumentWriter(str, format: Union[QByteArray, bytes, bytearray] = QByteArray())
    """
    def codec(self): # real signature unknown; restored from __doc__
        """ codec(self) -> QTextCodec """
        pass

    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> QIODevice """
        pass

    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> QByteArray """
        pass

    def setCodec(self, QTextCodec): # real signature unknown; restored from __doc__
        """ setCodec(self, QTextCodec) """
        pass

    def setDevice(self, QIODevice): # real signature unknown; restored from __doc__
        """ setDevice(self, QIODevice) """
        pass

    def setFileName(self, p_str): # real signature unknown; restored from __doc__
        """ setFileName(self, str) """
        pass

    def setFormat(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setFormat(self, Union[QByteArray, bytes, bytearray]) """
        pass

    def supportedDocumentFormats(self): # real signature unknown; restored from __doc__
        """ supportedDocumentFormats() -> List[QByteArray] """
        return []

    def write(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        write(self, QTextDocument) -> bool
        write(self, QTextDocumentFragment) -> bool
        """
        return False

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



