# encoding: utf-8
# module PyQt5.QtXml
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtXml.pyd
# by generator 1.147
# no doc

# imports
import sip as __sip


from .QDomNode import QDomNode

class QDomDocument(QDomNode):
    """
    QDomDocument()
    QDomDocument(str)
    QDomDocument(QDomDocumentType)
    QDomDocument(QDomDocument)
    """
    def createAttribute(self, p_str): # real signature unknown; restored from __doc__
        """ createAttribute(self, str) -> QDomAttr """
        return QDomAttr

    def createAttributeNS(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ createAttributeNS(self, str, str) -> QDomAttr """
        return QDomAttr

    def createCDATASection(self, p_str): # real signature unknown; restored from __doc__
        """ createCDATASection(self, str) -> QDomCDATASection """
        return QDomCDATASection

    def createComment(self, p_str): # real signature unknown; restored from __doc__
        """ createComment(self, str) -> QDomComment """
        return QDomComment

    def createDocumentFragment(self): # real signature unknown; restored from __doc__
        """ createDocumentFragment(self) -> QDomDocumentFragment """
        return QDomDocumentFragment

    def createElement(self, p_str): # real signature unknown; restored from __doc__
        """ createElement(self, str) -> QDomElement """
        return QDomElement

    def createElementNS(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ createElementNS(self, str, str) -> QDomElement """
        return QDomElement

    def createEntityReference(self, p_str): # real signature unknown; restored from __doc__
        """ createEntityReference(self, str) -> QDomEntityReference """
        return QDomEntityReference

    def createProcessingInstruction(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ createProcessingInstruction(self, str, str) -> QDomProcessingInstruction """
        return QDomProcessingInstruction

    def createTextNode(self, p_str): # real signature unknown; restored from __doc__
        """ createTextNode(self, str) -> QDomText """
        return QDomText

    def doctype(self): # real signature unknown; restored from __doc__
        """ doctype(self) -> QDomDocumentType """
        return QDomDocumentType

    def documentElement(self): # real signature unknown; restored from __doc__
        """ documentElement(self) -> QDomElement """
        return QDomElement

    def elementById(self, p_str): # real signature unknown; restored from __doc__
        """ elementById(self, str) -> QDomElement """
        return QDomElement

    def elementsByTagName(self, p_str): # real signature unknown; restored from __doc__
        """ elementsByTagName(self, str) -> QDomNodeList """
        return QDomNodeList

    def elementsByTagNameNS(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ elementsByTagNameNS(self, str, str) -> QDomNodeList """
        return QDomNodeList

    def implementation(self): # real signature unknown; restored from __doc__
        """ implementation(self) -> QDomImplementation """
        return QDomImplementation

    def importNode(self, QDomNode, bool): # real signature unknown; restored from __doc__
        """ importNode(self, QDomNode, bool) -> QDomNode """
        return QDomNode

    def nodeType(self): # real signature unknown; restored from __doc__
        """ nodeType(self) -> QDomNode.NodeType """
        pass

    def setContent(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setContent(self, Union[QByteArray, bytes, bytearray], bool) -> Tuple[bool, str, int, int]
        setContent(self, str, bool) -> Tuple[bool, str, int, int]
        setContent(self, QIODevice, bool) -> Tuple[bool, str, int, int]
        setContent(self, QXmlInputSource, bool) -> Tuple[bool, str, int, int]
        setContent(self, Union[QByteArray, bytes, bytearray]) -> Tuple[bool, str, int, int]
        setContent(self, str) -> Tuple[bool, str, int, int]
        setContent(self, QIODevice) -> Tuple[bool, str, int, int]
        setContent(self, QXmlInputSource, QXmlReader) -> Tuple[bool, str, int, int]
        """
        pass

    def toByteArray(self, indent=1): # real signature unknown; restored from __doc__
        """ toByteArray(self, indent: int = 1) -> QByteArray """
        pass

    def toString(self, indent=1): # real signature unknown; restored from __doc__
        """ toString(self, indent: int = 1) -> str """
        return ""

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


