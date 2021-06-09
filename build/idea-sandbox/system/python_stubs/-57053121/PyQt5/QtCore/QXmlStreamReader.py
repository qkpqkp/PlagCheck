# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QXmlStreamReader(__sip.simplewrapper):
    """
    QXmlStreamReader()
    QXmlStreamReader(QIODevice)
    QXmlStreamReader(Union[QByteArray, bytes, bytearray])
    QXmlStreamReader(str)
    """
    def addData(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addData(self, Union[QByteArray, bytes, bytearray])
        addData(self, str)
        """
        pass

    def addExtraNamespaceDeclaration(self, QXmlStreamNamespaceDeclaration): # real signature unknown; restored from __doc__
        """ addExtraNamespaceDeclaration(self, QXmlStreamNamespaceDeclaration) """
        pass

    def addExtraNamespaceDeclarations(self, Iterable, QXmlStreamNamespaceDeclaration=None): # real signature unknown; restored from __doc__
        """ addExtraNamespaceDeclarations(self, Iterable[QXmlStreamNamespaceDeclaration]) """
        pass

    def atEnd(self): # real signature unknown; restored from __doc__
        """ atEnd(self) -> bool """
        return False

    def attributes(self): # real signature unknown; restored from __doc__
        """ attributes(self) -> QXmlStreamAttributes """
        return QXmlStreamAttributes

    def characterOffset(self): # real signature unknown; restored from __doc__
        """ characterOffset(self) -> int """
        return 0

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def columnNumber(self): # real signature unknown; restored from __doc__
        """ columnNumber(self) -> int """
        return 0

    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> QIODevice """
        return QIODevice

    def documentEncoding(self): # real signature unknown; restored from __doc__
        """ documentEncoding(self) -> str """
        return ""

    def documentVersion(self): # real signature unknown; restored from __doc__
        """ documentVersion(self) -> str """
        return ""

    def dtdName(self): # real signature unknown; restored from __doc__
        """ dtdName(self) -> str """
        return ""

    def dtdPublicId(self): # real signature unknown; restored from __doc__
        """ dtdPublicId(self) -> str """
        return ""

    def dtdSystemId(self): # real signature unknown; restored from __doc__
        """ dtdSystemId(self) -> str """
        return ""

    def entityDeclarations(self): # real signature unknown; restored from __doc__
        """ entityDeclarations(self) -> List[QXmlStreamEntityDeclaration] """
        return []

    def entityResolver(self): # real signature unknown; restored from __doc__
        """ entityResolver(self) -> QXmlStreamEntityResolver """
        return QXmlStreamEntityResolver

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> QXmlStreamReader.Error """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def hasError(self): # real signature unknown; restored from __doc__
        """ hasError(self) -> bool """
        return False

    def isCDATA(self): # real signature unknown; restored from __doc__
        """ isCDATA(self) -> bool """
        return False

    def isCharacters(self): # real signature unknown; restored from __doc__
        """ isCharacters(self) -> bool """
        return False

    def isComment(self): # real signature unknown; restored from __doc__
        """ isComment(self) -> bool """
        return False

    def isDTD(self): # real signature unknown; restored from __doc__
        """ isDTD(self) -> bool """
        return False

    def isEndDocument(self): # real signature unknown; restored from __doc__
        """ isEndDocument(self) -> bool """
        return False

    def isEndElement(self): # real signature unknown; restored from __doc__
        """ isEndElement(self) -> bool """
        return False

    def isEntityReference(self): # real signature unknown; restored from __doc__
        """ isEntityReference(self) -> bool """
        return False

    def isProcessingInstruction(self): # real signature unknown; restored from __doc__
        """ isProcessingInstruction(self) -> bool """
        return False

    def isStandaloneDocument(self): # real signature unknown; restored from __doc__
        """ isStandaloneDocument(self) -> bool """
        return False

    def isStartDocument(self): # real signature unknown; restored from __doc__
        """ isStartDocument(self) -> bool """
        return False

    def isStartElement(self): # real signature unknown; restored from __doc__
        """ isStartElement(self) -> bool """
        return False

    def isWhitespace(self): # real signature unknown; restored from __doc__
        """ isWhitespace(self) -> bool """
        return False

    def lineNumber(self): # real signature unknown; restored from __doc__
        """ lineNumber(self) -> int """
        return 0

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def namespaceDeclarations(self): # real signature unknown; restored from __doc__
        """ namespaceDeclarations(self) -> List[QXmlStreamNamespaceDeclaration] """
        return []

    def namespaceProcessing(self): # real signature unknown; restored from __doc__
        """ namespaceProcessing(self) -> bool """
        return False

    def namespaceUri(self): # real signature unknown; restored from __doc__
        """ namespaceUri(self) -> str """
        return ""

    def notationDeclarations(self): # real signature unknown; restored from __doc__
        """ notationDeclarations(self) -> List[QXmlStreamNotationDeclaration] """
        return []

    def prefix(self): # real signature unknown; restored from __doc__
        """ prefix(self) -> str """
        return ""

    def processingInstructionData(self): # real signature unknown; restored from __doc__
        """ processingInstructionData(self) -> str """
        return ""

    def processingInstructionTarget(self): # real signature unknown; restored from __doc__
        """ processingInstructionTarget(self) -> str """
        return ""

    def qualifiedName(self): # real signature unknown; restored from __doc__
        """ qualifiedName(self) -> str """
        return ""

    def raiseError(self, message=''): # real signature unknown; restored from __doc__
        """ raiseError(self, message: str = '') """
        pass

    def readElementText(self, behaviour=None): # real signature unknown; restored from __doc__
        """ readElementText(self, behaviour: QXmlStreamReader.ReadElementTextBehaviour = QXmlStreamReader.ErrorOnUnexpectedElement) -> str """
        return ""

    def readNext(self): # real signature unknown; restored from __doc__
        """ readNext(self) -> QXmlStreamReader.TokenType """
        pass

    def readNextStartElement(self): # real signature unknown; restored from __doc__
        """ readNextStartElement(self) -> bool """
        return False

    def setDevice(self, QIODevice): # real signature unknown; restored from __doc__
        """ setDevice(self, QIODevice) """
        pass

    def setEntityResolver(self, QXmlStreamEntityResolver): # real signature unknown; restored from __doc__
        """ setEntityResolver(self, QXmlStreamEntityResolver) """
        pass

    def setNamespaceProcessing(self, bool): # real signature unknown; restored from __doc__
        """ setNamespaceProcessing(self, bool) """
        pass

    def skipCurrentElement(self): # real signature unknown; restored from __doc__
        """ skipCurrentElement(self) """
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def tokenString(self): # real signature unknown; restored from __doc__
        """ tokenString(self) -> str """
        return ""

    def tokenType(self): # real signature unknown; restored from __doc__
        """ tokenType(self) -> QXmlStreamReader.TokenType """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Characters = 6
    Comment = 7
    CustomError = 2
    DTD = 8
    EndDocument = 3
    EndElement = 5
    EntityReference = 9
    ErrorOnUnexpectedElement = 0
    IncludeChildElements = 1
    Invalid = 1
    NoError = 0
    NoToken = 0
    NotWellFormedError = 3
    PrematureEndOfDocumentError = 4
    ProcessingInstruction = 10
    SkipChildElements = 2
    StartDocument = 2
    StartElement = 4
    UnexpectedElementError = 1


