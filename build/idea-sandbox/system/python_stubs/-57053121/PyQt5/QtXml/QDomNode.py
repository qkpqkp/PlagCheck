# encoding: utf-8
# module PyQt5.QtXml
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtXml.pyd
# by generator 1.147
# no doc

# imports
import sip as __sip


class QDomNode(__sip.simplewrapper):
    """
    QDomNode()
    QDomNode(QDomNode)
    """
    def appendChild(self, QDomNode): # real signature unknown; restored from __doc__
        """ appendChild(self, QDomNode) -> QDomNode """
        return QDomNode

    def attributes(self): # real signature unknown; restored from __doc__
        """ attributes(self) -> QDomNamedNodeMap """
        return QDomNamedNodeMap

    def childNodes(self): # real signature unknown; restored from __doc__
        """ childNodes(self) -> QDomNodeList """
        return QDomNodeList

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def cloneNode(self, deep=True): # real signature unknown; restored from __doc__
        """ cloneNode(self, deep: bool = True) -> QDomNode """
        return QDomNode

    def columnNumber(self): # real signature unknown; restored from __doc__
        """ columnNumber(self) -> int """
        return 0

    def firstChild(self): # real signature unknown; restored from __doc__
        """ firstChild(self) -> QDomNode """
        return QDomNode

    def firstChildElement(self, tagName=''): # real signature unknown; restored from __doc__
        """ firstChildElement(self, tagName: str = '') -> QDomElement """
        return QDomElement

    def hasAttributes(self): # real signature unknown; restored from __doc__
        """ hasAttributes(self) -> bool """
        return False

    def hasChildNodes(self): # real signature unknown; restored from __doc__
        """ hasChildNodes(self) -> bool """
        return False

    def insertAfter(self, QDomNode, QDomNode_1): # real signature unknown; restored from __doc__
        """ insertAfter(self, QDomNode, QDomNode) -> QDomNode """
        return QDomNode

    def insertBefore(self, QDomNode, QDomNode_1): # real signature unknown; restored from __doc__
        """ insertBefore(self, QDomNode, QDomNode) -> QDomNode """
        return QDomNode

    def isAttr(self): # real signature unknown; restored from __doc__
        """ isAttr(self) -> bool """
        return False

    def isCDATASection(self): # real signature unknown; restored from __doc__
        """ isCDATASection(self) -> bool """
        return False

    def isCharacterData(self): # real signature unknown; restored from __doc__
        """ isCharacterData(self) -> bool """
        return False

    def isComment(self): # real signature unknown; restored from __doc__
        """ isComment(self) -> bool """
        return False

    def isDocument(self): # real signature unknown; restored from __doc__
        """ isDocument(self) -> bool """
        return False

    def isDocumentFragment(self): # real signature unknown; restored from __doc__
        """ isDocumentFragment(self) -> bool """
        return False

    def isDocumentType(self): # real signature unknown; restored from __doc__
        """ isDocumentType(self) -> bool """
        return False

    def isElement(self): # real signature unknown; restored from __doc__
        """ isElement(self) -> bool """
        return False

    def isEntity(self): # real signature unknown; restored from __doc__
        """ isEntity(self) -> bool """
        return False

    def isEntityReference(self): # real signature unknown; restored from __doc__
        """ isEntityReference(self) -> bool """
        return False

    def isNotation(self): # real signature unknown; restored from __doc__
        """ isNotation(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isProcessingInstruction(self): # real signature unknown; restored from __doc__
        """ isProcessingInstruction(self) -> bool """
        return False

    def isSupported(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ isSupported(self, str, str) -> bool """
        return False

    def isText(self): # real signature unknown; restored from __doc__
        """ isText(self) -> bool """
        return False

    def lastChild(self): # real signature unknown; restored from __doc__
        """ lastChild(self) -> QDomNode """
        return QDomNode

    def lastChildElement(self, tagName=''): # real signature unknown; restored from __doc__
        """ lastChildElement(self, tagName: str = '') -> QDomElement """
        return QDomElement

    def lineNumber(self): # real signature unknown; restored from __doc__
        """ lineNumber(self) -> int """
        return 0

    def localName(self): # real signature unknown; restored from __doc__
        """ localName(self) -> str """
        return ""

    def namedItem(self, p_str): # real signature unknown; restored from __doc__
        """ namedItem(self, str) -> QDomNode """
        return QDomNode

    def namespaceURI(self): # real signature unknown; restored from __doc__
        """ namespaceURI(self) -> str """
        return ""

    def nextSibling(self): # real signature unknown; restored from __doc__
        """ nextSibling(self) -> QDomNode """
        return QDomNode

    def nextSiblingElement(self, taName=''): # real signature unknown; restored from __doc__
        """ nextSiblingElement(self, taName: str = '') -> QDomElement """
        return QDomElement

    def nodeName(self): # real signature unknown; restored from __doc__
        """ nodeName(self) -> str """
        return ""

    def nodeType(self): # real signature unknown; restored from __doc__
        """ nodeType(self) -> QDomNode.NodeType """
        pass

    def nodeValue(self): # real signature unknown; restored from __doc__
        """ nodeValue(self) -> str """
        return ""

    def normalize(self): # real signature unknown; restored from __doc__
        """ normalize(self) """
        pass

    def ownerDocument(self): # real signature unknown; restored from __doc__
        """ ownerDocument(self) -> QDomDocument """
        return QDomDocument

    def parentNode(self): # real signature unknown; restored from __doc__
        """ parentNode(self) -> QDomNode """
        return QDomNode

    def prefix(self): # real signature unknown; restored from __doc__
        """ prefix(self) -> str """
        return ""

    def previousSibling(self): # real signature unknown; restored from __doc__
        """ previousSibling(self) -> QDomNode """
        return QDomNode

    def previousSiblingElement(self, tagName=''): # real signature unknown; restored from __doc__
        """ previousSiblingElement(self, tagName: str = '') -> QDomElement """
        return QDomElement

    def removeChild(self, QDomNode): # real signature unknown; restored from __doc__
        """ removeChild(self, QDomNode) -> QDomNode """
        return QDomNode

    def replaceChild(self, QDomNode, QDomNode_1): # real signature unknown; restored from __doc__
        """ replaceChild(self, QDomNode, QDomNode) -> QDomNode """
        return QDomNode

    def save(self, QTextStream, p_int, QDomNode_EncodingPolicy=None): # real signature unknown; restored from __doc__
        """ save(self, QTextStream, int, QDomNode.EncodingPolicy = QDomNode.EncodingFromDocument) """
        pass

    def setNodeValue(self, p_str): # real signature unknown; restored from __doc__
        """ setNodeValue(self, str) """
        pass

    def setPrefix(self, p_str): # real signature unknown; restored from __doc__
        """ setPrefix(self, str) """
        pass

    def toAttr(self): # real signature unknown; restored from __doc__
        """ toAttr(self) -> QDomAttr """
        return QDomAttr

    def toCDATASection(self): # real signature unknown; restored from __doc__
        """ toCDATASection(self) -> QDomCDATASection """
        return QDomCDATASection

    def toCharacterData(self): # real signature unknown; restored from __doc__
        """ toCharacterData(self) -> QDomCharacterData """
        return QDomCharacterData

    def toComment(self): # real signature unknown; restored from __doc__
        """ toComment(self) -> QDomComment """
        return QDomComment

    def toDocument(self): # real signature unknown; restored from __doc__
        """ toDocument(self) -> QDomDocument """
        return QDomDocument

    def toDocumentFragment(self): # real signature unknown; restored from __doc__
        """ toDocumentFragment(self) -> QDomDocumentFragment """
        return QDomDocumentFragment

    def toDocumentType(self): # real signature unknown; restored from __doc__
        """ toDocumentType(self) -> QDomDocumentType """
        return QDomDocumentType

    def toElement(self): # real signature unknown; restored from __doc__
        """ toElement(self) -> QDomElement """
        return QDomElement

    def toEntity(self): # real signature unknown; restored from __doc__
        """ toEntity(self) -> QDomEntity """
        return QDomEntity

    def toEntityReference(self): # real signature unknown; restored from __doc__
        """ toEntityReference(self) -> QDomEntityReference """
        return QDomEntityReference

    def toNotation(self): # real signature unknown; restored from __doc__
        """ toNotation(self) -> QDomNotation """
        return QDomNotation

    def toProcessingInstruction(self): # real signature unknown; restored from __doc__
        """ toProcessingInstruction(self) -> QDomProcessingInstruction """
        return QDomProcessingInstruction

    def toText(self): # real signature unknown; restored from __doc__
        """ toText(self) -> QDomText """
        return QDomText

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, QDomNode=None): # real signature unknown; restored from __doc__ with multiple overloads
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


    AttributeNode = 2
    BaseNode = 21
    CDATASectionNode = 4
    CharacterDataNode = 22
    CommentNode = 8
    DocumentFragmentNode = 11
    DocumentNode = 9
    DocumentTypeNode = 10
    ElementNode = 1
    EncodingFromDocument = 1
    EncodingFromTextStream = 2
    EntityNode = 6
    EntityReferenceNode = 5
    NotationNode = 12
    ProcessingInstructionNode = 7
    TextNode = 3
    __hash__ = None


