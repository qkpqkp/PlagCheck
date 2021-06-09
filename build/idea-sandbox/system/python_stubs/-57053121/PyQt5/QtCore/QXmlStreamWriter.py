# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QXmlStreamWriter(__sip.simplewrapper):
    """
    QXmlStreamWriter()
    QXmlStreamWriter(QIODevice)
    QXmlStreamWriter(Union[QByteArray, bytes, bytearray])
    """
    def autoFormatting(self): # real signature unknown; restored from __doc__
        """ autoFormatting(self) -> bool """
        return False

    def autoFormattingIndent(self): # real signature unknown; restored from __doc__
        """ autoFormattingIndent(self) -> int """
        return 0

    def codec(self): # real signature unknown; restored from __doc__
        """ codec(self) -> QTextCodec """
        return QTextCodec

    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> QIODevice """
        return QIODevice

    def hasError(self): # real signature unknown; restored from __doc__
        """ hasError(self) -> bool """
        return False

    def setAutoFormatting(self, bool): # real signature unknown; restored from __doc__
        """ setAutoFormatting(self, bool) """
        pass

    def setAutoFormattingIndent(self, p_int): # real signature unknown; restored from __doc__
        """ setAutoFormattingIndent(self, int) """
        pass

    def setCodec(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setCodec(self, QTextCodec)
        setCodec(self, str)
        """
        pass

    def setDevice(self, QIODevice): # real signature unknown; restored from __doc__
        """ setDevice(self, QIODevice) """
        pass

    def writeAttribute(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        writeAttribute(self, str, str)
        writeAttribute(self, str, str, str)
        writeAttribute(self, QXmlStreamAttribute)
        """
        pass

    def writeAttributes(self, QXmlStreamAttributes): # real signature unknown; restored from __doc__
        """ writeAttributes(self, QXmlStreamAttributes) """
        pass

    def writeCDATA(self, p_str): # real signature unknown; restored from __doc__
        """ writeCDATA(self, str) """
        pass

    def writeCharacters(self, p_str): # real signature unknown; restored from __doc__
        """ writeCharacters(self, str) """
        pass

    def writeComment(self, p_str): # real signature unknown; restored from __doc__
        """ writeComment(self, str) """
        pass

    def writeCurrentToken(self, QXmlStreamReader): # real signature unknown; restored from __doc__
        """ writeCurrentToken(self, QXmlStreamReader) """
        pass

    def writeDefaultNamespace(self, p_str): # real signature unknown; restored from __doc__
        """ writeDefaultNamespace(self, str) """
        pass

    def writeDTD(self, p_str): # real signature unknown; restored from __doc__
        """ writeDTD(self, str) """
        pass

    def writeEmptyElement(self, p_str, p_str_1=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        writeEmptyElement(self, str)
        writeEmptyElement(self, str, str)
        """
        pass

    def writeEndDocument(self): # real signature unknown; restored from __doc__
        """ writeEndDocument(self) """
        pass

    def writeEndElement(self): # real signature unknown; restored from __doc__
        """ writeEndElement(self) """
        pass

    def writeEntityReference(self, p_str): # real signature unknown; restored from __doc__
        """ writeEntityReference(self, str) """
        pass

    def writeNamespace(self, p_str, prefix=''): # real signature unknown; restored from __doc__
        """ writeNamespace(self, str, prefix: str = '') """
        pass

    def writeProcessingInstruction(self, p_str, data=''): # real signature unknown; restored from __doc__
        """ writeProcessingInstruction(self, str, data: str = '') """
        pass

    def writeStartDocument(self, p_str=None, bool=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        writeStartDocument(self)
        writeStartDocument(self, str)
        writeStartDocument(self, str, bool)
        """
        pass

    def writeStartElement(self, p_str, p_str_1=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        writeStartElement(self, str)
        writeStartElement(self, str, str)
        """
        pass

    def writeTextElement(self, p_str, p_str_1, p_str_2=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        writeTextElement(self, str, str)
        writeTextElement(self, str, str, str)
        """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



