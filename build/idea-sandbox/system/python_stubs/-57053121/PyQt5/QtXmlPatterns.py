# encoding: utf-8
# module PyQt5.QtXmlPatterns
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtXmlPatterns.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


# no functions
# classes

class QAbstractMessageHandler(__PyQt5_QtCore.QObject):
    """ QAbstractMessageHandler(parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def handleMessage(self, QtMsgType, p_str, QUrl, QSourceLocation): # real signature unknown; restored from __doc__
        """ handleMessage(self, QtMsgType, str, QUrl, QSourceLocation) """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def message(self, QtMsgType, p_str, identifier=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ message(self, QtMsgType, str, identifier: QUrl = QUrl(), sourceLocation: QSourceLocation = QSourceLocation()) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


class QAbstractUriResolver(__PyQt5_QtCore.QObject):
    """ QAbstractUriResolver(parent: QObject = None) """
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

    def resolve(self, QUrl, QUrl_1): # real signature unknown; restored from __doc__
        """ resolve(self, QUrl, QUrl) -> QUrl """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


class QAbstractXmlNodeModel(__sip.simplewrapper):
    """ QAbstractXmlNodeModel() """
    def attributes(self, QXmlNodeModelIndex): # real signature unknown; restored from __doc__
        """ attributes(self, QXmlNodeModelIndex) -> List[QXmlNodeModelIndex] """
        return []

    def baseUri(self, QXmlNodeModelIndex): # real signature unknown; restored from __doc__
        """ baseUri(self, QXmlNodeModelIndex) -> QUrl """
        pass

    def compareOrder(self, QXmlNodeModelIndex, QXmlNodeModelIndex_1): # real signature unknown; restored from __doc__
        """ compareOrder(self, QXmlNodeModelIndex, QXmlNodeModelIndex) -> QXmlNodeModelIndex.DocumentOrder """
        pass

    def createIndex(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        createIndex(self, int) -> QXmlNodeModelIndex
        createIndex(self, int, int) -> QXmlNodeModelIndex
        createIndex(self, object, additionalData: int = 0) -> QXmlNodeModelIndex
        """
        return QXmlNodeModelIndex

    def documentUri(self, QXmlNodeModelIndex): # real signature unknown; restored from __doc__
        """ documentUri(self, QXmlNodeModelIndex) -> QUrl """
        pass

    def elementById(self, QXmlName): # real signature unknown; restored from __doc__
        """ elementById(self, QXmlName) -> QXmlNodeModelIndex """
        return QXmlNodeModelIndex

    def kind(self, QXmlNodeModelIndex): # real signature unknown; restored from __doc__
        """ kind(self, QXmlNodeModelIndex) -> QXmlNodeModelIndex.NodeKind """
        pass

    def name(self, QXmlNodeModelIndex): # real signature unknown; restored from __doc__
        """ name(self, QXmlNodeModelIndex) -> QXmlName """
        return QXmlName

    def namespaceBindings(self, QXmlNodeModelIndex): # real signature unknown; restored from __doc__
        """ namespaceBindings(self, QXmlNodeModelIndex) -> List[QXmlName] """
        return []

    def nextFromSimpleAxis(self, QAbstractXmlNodeModel_SimpleAxis, QXmlNodeModelIndex): # real signature unknown; restored from __doc__
        """ nextFromSimpleAxis(self, QAbstractXmlNodeModel.SimpleAxis, QXmlNodeModelIndex) -> QXmlNodeModelIndex """
        return QXmlNodeModelIndex

    def nodesByIdref(self, QXmlName): # real signature unknown; restored from __doc__
        """ nodesByIdref(self, QXmlName) -> List[QXmlNodeModelIndex] """
        return []

    def root(self, QXmlNodeModelIndex): # real signature unknown; restored from __doc__
        """ root(self, QXmlNodeModelIndex) -> QXmlNodeModelIndex """
        return QXmlNodeModelIndex

    def sourceLocation(self, QXmlNodeModelIndex): # real signature unknown; restored from __doc__
        """ sourceLocation(self, QXmlNodeModelIndex) -> QSourceLocation """
        return QSourceLocation

    def stringValue(self, QXmlNodeModelIndex): # real signature unknown; restored from __doc__
        """ stringValue(self, QXmlNodeModelIndex) -> str """
        return ""

    def typedValue(self, QXmlNodeModelIndex): # real signature unknown; restored from __doc__
        """ typedValue(self, QXmlNodeModelIndex) -> Any """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    FirstChild = 1
    NextSibling = 3
    Parent = 0
    PreviousSibling = 2


class QAbstractXmlReceiver(__sip.simplewrapper):
    """ QAbstractXmlReceiver() """
    def atomicValue(self, Any): # real signature unknown; restored from __doc__
        """ atomicValue(self, Any) """
        pass

    def attribute(self, QXmlName, p_str): # real signature unknown; restored from __doc__
        """ attribute(self, QXmlName, str) """
        pass

    def characters(self, p_str): # real signature unknown; restored from __doc__
        """ characters(self, str) """
        pass

    def comment(self, p_str): # real signature unknown; restored from __doc__
        """ comment(self, str) """
        pass

    def endDocument(self): # real signature unknown; restored from __doc__
        """ endDocument(self) """
        pass

    def endElement(self): # real signature unknown; restored from __doc__
        """ endElement(self) """
        pass

    def endOfSequence(self): # real signature unknown; restored from __doc__
        """ endOfSequence(self) """
        pass

    def namespaceBinding(self, QXmlName): # real signature unknown; restored from __doc__
        """ namespaceBinding(self, QXmlName) """
        pass

    def processingInstruction(self, QXmlName, p_str): # real signature unknown; restored from __doc__
        """ processingInstruction(self, QXmlName, str) """
        pass

    def startDocument(self): # real signature unknown; restored from __doc__
        """ startDocument(self) """
        pass

    def startElement(self, QXmlName): # real signature unknown; restored from __doc__
        """ startElement(self, QXmlName) """
        pass

    def startOfSequence(self): # real signature unknown; restored from __doc__
        """ startOfSequence(self) """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QSimpleXmlNodeModel(QAbstractXmlNodeModel):
    """ QSimpleXmlNodeModel(QXmlNamePool) """
    def attributes(self, *args, **kwargs): # real signature unknown
        pass

    def baseUri(self, QXmlNodeModelIndex): # real signature unknown; restored from __doc__
        """ baseUri(self, QXmlNodeModelIndex) -> QUrl """
        pass

    def createIndex(self, *args, **kwargs): # real signature unknown
        pass

    def elementById(self, QXmlName): # real signature unknown; restored from __doc__
        """ elementById(self, QXmlName) -> QXmlNodeModelIndex """
        return QXmlNodeModelIndex

    def namePool(self): # real signature unknown; restored from __doc__
        """ namePool(self) -> QXmlNamePool """
        return QXmlNamePool

    def namespaceBindings(self, QXmlNodeModelIndex): # real signature unknown; restored from __doc__
        """ namespaceBindings(self, QXmlNodeModelIndex) -> List[QXmlName] """
        return []

    def nextFromSimpleAxis(self, *args, **kwargs): # real signature unknown
        pass

    def nodesByIdref(self, QXmlName): # real signature unknown; restored from __doc__
        """ nodesByIdref(self, QXmlName) -> List[QXmlNodeModelIndex] """
        return []

    def stringValue(self, QXmlNodeModelIndex): # real signature unknown; restored from __doc__
        """ stringValue(self, QXmlNodeModelIndex) -> str """
        return ""

    def __init__(self, QXmlNamePool): # real signature unknown; restored from __doc__
        pass


class QSourceLocation(__sip.simplewrapper):
    """
    QSourceLocation()
    QSourceLocation(QSourceLocation)
    QSourceLocation(QUrl, line: int = -1, column: int = -1)
    """
    def column(self): # real signature unknown; restored from __doc__
        """ column(self) -> int """
        return 0

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def line(self): # real signature unknown; restored from __doc__
        """ line(self) -> int """
        return 0

    def setColumn(self, p_int): # real signature unknown; restored from __doc__
        """ setColumn(self, int) """
        pass

    def setLine(self, p_int): # real signature unknown; restored from __doc__
        """ setLine(self, int) """
        pass

    def setUri(self, QUrl): # real signature unknown; restored from __doc__
        """ setUri(self, QUrl) """
        pass

    def uri(self): # real signature unknown; restored from __doc__
        """ uri(self) -> QUrl """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
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



class QXmlSerializer(QAbstractXmlReceiver):
    """ QXmlSerializer(QXmlQuery, QIODevice) """
    def atomicValue(self, Any): # real signature unknown; restored from __doc__
        """ atomicValue(self, Any) """
        pass

    def attribute(self, QXmlName, p_str): # real signature unknown; restored from __doc__
        """ attribute(self, QXmlName, str) """
        pass

    def characters(self, p_str): # real signature unknown; restored from __doc__
        """ characters(self, str) """
        pass

    def codec(self): # real signature unknown; restored from __doc__
        """ codec(self) -> QTextCodec """
        pass

    def comment(self, p_str): # real signature unknown; restored from __doc__
        """ comment(self, str) """
        pass

    def endDocument(self): # real signature unknown; restored from __doc__
        """ endDocument(self) """
        pass

    def endElement(self): # real signature unknown; restored from __doc__
        """ endElement(self) """
        pass

    def endOfSequence(self): # real signature unknown; restored from __doc__
        """ endOfSequence(self) """
        pass

    def namespaceBinding(self, QXmlName): # real signature unknown; restored from __doc__
        """ namespaceBinding(self, QXmlName) """
        pass

    def outputDevice(self): # real signature unknown; restored from __doc__
        """ outputDevice(self) -> QIODevice """
        pass

    def processingInstruction(self, QXmlName, p_str): # real signature unknown; restored from __doc__
        """ processingInstruction(self, QXmlName, str) """
        pass

    def setCodec(self, QTextCodec): # real signature unknown; restored from __doc__
        """ setCodec(self, QTextCodec) """
        pass

    def startDocument(self): # real signature unknown; restored from __doc__
        """ startDocument(self) """
        pass

    def startElement(self, QXmlName): # real signature unknown; restored from __doc__
        """ startElement(self, QXmlName) """
        pass

    def startOfSequence(self): # real signature unknown; restored from __doc__
        """ startOfSequence(self) """
        pass

    def __init__(self, QXmlQuery, QIODevice): # real signature unknown; restored from __doc__
        pass


class QXmlFormatter(QXmlSerializer):
    """ QXmlFormatter(QXmlQuery, QIODevice) """
    def atomicValue(self, Any): # real signature unknown; restored from __doc__
        """ atomicValue(self, Any) """
        pass

    def attribute(self, QXmlName, p_str): # real signature unknown; restored from __doc__
        """ attribute(self, QXmlName, str) """
        pass

    def characters(self, p_str): # real signature unknown; restored from __doc__
        """ characters(self, str) """
        pass

    def comment(self, p_str): # real signature unknown; restored from __doc__
        """ comment(self, str) """
        pass

    def endDocument(self): # real signature unknown; restored from __doc__
        """ endDocument(self) """
        pass

    def endElement(self): # real signature unknown; restored from __doc__
        """ endElement(self) """
        pass

    def endOfSequence(self): # real signature unknown; restored from __doc__
        """ endOfSequence(self) """
        pass

    def indentationDepth(self): # real signature unknown; restored from __doc__
        """ indentationDepth(self) -> int """
        return 0

    def processingInstruction(self, QXmlName, p_str): # real signature unknown; restored from __doc__
        """ processingInstruction(self, QXmlName, str) """
        pass

    def setIndentationDepth(self, p_int): # real signature unknown; restored from __doc__
        """ setIndentationDepth(self, int) """
        pass

    def startDocument(self): # real signature unknown; restored from __doc__
        """ startDocument(self) """
        pass

    def startElement(self, QXmlName): # real signature unknown; restored from __doc__
        """ startElement(self, QXmlName) """
        pass

    def startOfSequence(self): # real signature unknown; restored from __doc__
        """ startOfSequence(self) """
        pass

    def __init__(self, QXmlQuery, QIODevice): # real signature unknown; restored from __doc__
        pass


class QXmlItem(__sip.simplewrapper):
    """
    QXmlItem()
    QXmlItem(QXmlItem)
    QXmlItem(QXmlNodeModelIndex)
    QXmlItem(Any)
    """
    def isAtomicValue(self): # real signature unknown; restored from __doc__
        """ isAtomicValue(self) -> bool """
        return False

    def isNode(self): # real signature unknown; restored from __doc__
        """ isNode(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def toAtomicValue(self): # real signature unknown; restored from __doc__
        """ toAtomicValue(self) -> Any """
        pass

    def toNodeModelIndex(self): # real signature unknown; restored from __doc__
        """ toNodeModelIndex(self) -> QXmlNodeModelIndex """
        return QXmlNodeModelIndex

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QXmlName(__sip.simplewrapper):
    """
    QXmlName()
    QXmlName(QXmlNamePool, str, namespaceUri: str = '', prefix: str = '')
    QXmlName(QXmlName)
    """
    def fromClarkName(self, p_str, QXmlNamePool): # real signature unknown; restored from __doc__
        """ fromClarkName(str, QXmlNamePool) -> QXmlName """
        return QXmlName

    def isNCName(self, p_str): # real signature unknown; restored from __doc__
        """ isNCName(str) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def localName(self, QXmlNamePool): # real signature unknown; restored from __doc__
        """ localName(self, QXmlNamePool) -> str """
        return ""

    def namespaceUri(self, QXmlNamePool): # real signature unknown; restored from __doc__
        """ namespaceUri(self, QXmlNamePool) -> str """
        return ""

    def prefix(self, QXmlNamePool): # real signature unknown; restored from __doc__
        """ prefix(self, QXmlNamePool) -> str """
        return ""

    def toClarkName(self, QXmlNamePool): # real signature unknown; restored from __doc__
        """ toClarkName(self, QXmlNamePool) -> str """
        return ""

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
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



class QXmlNamePool(__sip.simplewrapper):
    """
    QXmlNamePool()
    QXmlNamePool(QXmlNamePool)
    """
    def __init__(self, QXmlNamePool=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QXmlNodeModelIndex(__sip.simplewrapper):
    """
    QXmlNodeModelIndex()
    QXmlNodeModelIndex(QXmlNodeModelIndex)
    """
    def additionalData(self): # real signature unknown; restored from __doc__
        """ additionalData(self) -> int """
        return 0

    def data(self): # real signature unknown; restored from __doc__
        """ data(self) -> int """
        return 0

    def internalPointer(self): # real signature unknown; restored from __doc__
        """ internalPointer(self) -> object """
        return object()

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def model(self): # real signature unknown; restored from __doc__
        """ model(self) -> QAbstractXmlNodeModel """
        return QAbstractXmlNodeModel

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, QXmlNodeModelIndex=None): # real signature unknown; restored from __doc__ with multiple overloads
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


    Attribute = 1
    Comment = 2
    Document = 4
    Element = 8
    Follows = 1
    Is = 0
    Namespace = 16
    Precedes = -1
    ProcessingInstruction = 32
    Text = 64


class QXmlQuery(__sip.simplewrapper):
    """
    QXmlQuery()
    QXmlQuery(QXmlQuery)
    QXmlQuery(QXmlNamePool)
    QXmlQuery(QXmlQuery.QueryLanguage, pool: QXmlNamePool = QXmlNamePool())
    """
    def bindVariable(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        bindVariable(self, QXmlName, QXmlItem)
        bindVariable(self, QXmlName, QIODevice)
        bindVariable(self, QXmlName, QXmlQuery)
        bindVariable(self, str, QXmlItem)
        bindVariable(self, str, QIODevice)
        bindVariable(self, str, QXmlQuery)
        """
        pass

    def evaluateTo(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        evaluateTo(self, QXmlResultItems)
        evaluateTo(self, QAbstractXmlReceiver) -> bool
        evaluateTo(self, QIODevice) -> bool
        """
        return False

    def evaluateToString(self): # real signature unknown; restored from __doc__
        """ evaluateToString(self) -> str """
        return ""

    def evaluateToStringList(self): # real signature unknown; restored from __doc__
        """ evaluateToStringList(self) -> List[str] """
        return []

    def initialTemplateName(self): # real signature unknown; restored from __doc__
        """ initialTemplateName(self) -> QXmlName """
        return QXmlName

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def messageHandler(self): # real signature unknown; restored from __doc__
        """ messageHandler(self) -> QAbstractMessageHandler """
        return QAbstractMessageHandler

    def namePool(self): # real signature unknown; restored from __doc__
        """ namePool(self) -> QXmlNamePool """
        return QXmlNamePool

    def networkAccessManager(self): # real signature unknown; restored from __doc__
        """ networkAccessManager(self) -> QNetworkAccessManager """
        pass

    def queryLanguage(self): # real signature unknown; restored from __doc__
        """ queryLanguage(self) -> QXmlQuery.QueryLanguage """
        pass

    def setFocus(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setFocus(self, QXmlItem)
        setFocus(self, QUrl) -> bool
        setFocus(self, QIODevice) -> bool
        setFocus(self, str) -> bool
        """
        return False

    def setInitialTemplateName(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setInitialTemplateName(self, QXmlName)
        setInitialTemplateName(self, str)
        """
        pass

    def setMessageHandler(self, QAbstractMessageHandler): # real signature unknown; restored from __doc__
        """ setMessageHandler(self, QAbstractMessageHandler) """
        pass

    def setNetworkAccessManager(self, QNetworkAccessManager): # real signature unknown; restored from __doc__
        """ setNetworkAccessManager(self, QNetworkAccessManager) """
        pass

    def setQuery(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setQuery(self, str, documentUri: QUrl = QUrl())
        setQuery(self, QIODevice, documentUri: QUrl = QUrl())
        setQuery(self, QUrl, baseUri: QUrl = QUrl())
        """
        pass

    def setUriResolver(self, QAbstractUriResolver): # real signature unknown; restored from __doc__
        """ setUriResolver(self, QAbstractUriResolver) """
        pass

    def uriResolver(self): # real signature unknown; restored from __doc__
        """ uriResolver(self) -> QAbstractUriResolver """
        return QAbstractUriResolver

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    XQuery10 = 1
    XSLT20 = 2


class QXmlResultItems(__sip.simplewrapper):
    """ QXmlResultItems() """
    def current(self): # real signature unknown; restored from __doc__
        """ current(self) -> QXmlItem """
        return QXmlItem

    def hasError(self): # real signature unknown; restored from __doc__
        """ hasError(self) -> bool """
        return False

    def next(self): # real signature unknown; restored from __doc__
        """ next(self) -> QXmlItem """
        return QXmlItem

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QXmlSchema(__sip.simplewrapper):
    """
    QXmlSchema()
    QXmlSchema(QXmlSchema)
    """
    def documentUri(self): # real signature unknown; restored from __doc__
        """ documentUri(self) -> QUrl """
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def load(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        load(self, QUrl) -> bool
        load(self, QIODevice, documentUri: QUrl = QUrl()) -> bool
        load(self, Union[QByteArray, bytes, bytearray], documentUri: QUrl = QUrl()) -> bool
        """
        return False

    def messageHandler(self): # real signature unknown; restored from __doc__
        """ messageHandler(self) -> QAbstractMessageHandler """
        return QAbstractMessageHandler

    def namePool(self): # real signature unknown; restored from __doc__
        """ namePool(self) -> QXmlNamePool """
        return QXmlNamePool

    def networkAccessManager(self): # real signature unknown; restored from __doc__
        """ networkAccessManager(self) -> QNetworkAccessManager """
        pass

    def setMessageHandler(self, QAbstractMessageHandler): # real signature unknown; restored from __doc__
        """ setMessageHandler(self, QAbstractMessageHandler) """
        pass

    def setNetworkAccessManager(self, QNetworkAccessManager): # real signature unknown; restored from __doc__
        """ setNetworkAccessManager(self, QNetworkAccessManager) """
        pass

    def setUriResolver(self, QAbstractUriResolver): # real signature unknown; restored from __doc__
        """ setUriResolver(self, QAbstractUriResolver) """
        pass

    def uriResolver(self): # real signature unknown; restored from __doc__
        """ uriResolver(self) -> QAbstractUriResolver """
        return QAbstractUriResolver

    def __init__(self, QXmlSchema=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QXmlSchemaValidator(__sip.simplewrapper):
    """
    QXmlSchemaValidator()
    QXmlSchemaValidator(QXmlSchema)
    """
    def messageHandler(self): # real signature unknown; restored from __doc__
        """ messageHandler(self) -> QAbstractMessageHandler """
        return QAbstractMessageHandler

    def namePool(self): # real signature unknown; restored from __doc__
        """ namePool(self) -> QXmlNamePool """
        return QXmlNamePool

    def networkAccessManager(self): # real signature unknown; restored from __doc__
        """ networkAccessManager(self) -> QNetworkAccessManager """
        pass

    def schema(self): # real signature unknown; restored from __doc__
        """ schema(self) -> QXmlSchema """
        return QXmlSchema

    def setMessageHandler(self, QAbstractMessageHandler): # real signature unknown; restored from __doc__
        """ setMessageHandler(self, QAbstractMessageHandler) """
        pass

    def setNetworkAccessManager(self, QNetworkAccessManager): # real signature unknown; restored from __doc__
        """ setNetworkAccessManager(self, QNetworkAccessManager) """
        pass

    def setSchema(self, QXmlSchema): # real signature unknown; restored from __doc__
        """ setSchema(self, QXmlSchema) """
        pass

    def setUriResolver(self, QAbstractUriResolver): # real signature unknown; restored from __doc__
        """ setUriResolver(self, QAbstractUriResolver) """
        pass

    def uriResolver(self): # real signature unknown; restored from __doc__
        """ uriResolver(self) -> QAbstractUriResolver """
        return QAbstractUriResolver

    def validate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        validate(self, QUrl) -> bool
        validate(self, QIODevice, documentUri: QUrl = QUrl()) -> bool
        validate(self, Union[QByteArray, bytes, bytearray], documentUri: QUrl = QUrl()) -> bool
        """
        return False

    def __init__(self, QXmlSchema=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values



