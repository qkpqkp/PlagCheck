# encoding: utf-8
# module PyQt5.QtXml
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtXml.pyd
# by generator 1.147
# no doc

# imports
import sip as __sip


from .QXmlContentHandler import QXmlContentHandler

from .QXmlErrorHandler import QXmlErrorHandler

from .QXmlDTDHandler import QXmlDTDHandler

from .QXmlEntityResolver import QXmlEntityResolver

from .QXmlLexicalHandler import QXmlLexicalHandler

from .QXmlDeclHandler import QXmlDeclHandler

class QXmlDefaultHandler(QXmlContentHandler, QXmlErrorHandler, QXmlDTDHandler, QXmlEntityResolver, QXmlLexicalHandler, QXmlDeclHandler):
    """ QXmlDefaultHandler() """
    def attributeDecl(self, p_str, p_str_1, p_str_2, p_str_3, p_str_4): # real signature unknown; restored from __doc__
        """ attributeDecl(self, str, str, str, str, str) -> bool """
        return False

    def characters(self, p_str): # real signature unknown; restored from __doc__
        """ characters(self, str) -> bool """
        return False

    def comment(self, p_str): # real signature unknown; restored from __doc__
        """ comment(self, str) -> bool """
        return False

    def endCDATA(self): # real signature unknown; restored from __doc__
        """ endCDATA(self) -> bool """
        return False

    def endDocument(self): # real signature unknown; restored from __doc__
        """ endDocument(self) -> bool """
        return False

    def endDTD(self): # real signature unknown; restored from __doc__
        """ endDTD(self) -> bool """
        return False

    def endElement(self, p_str, p_str_1, p_str_2): # real signature unknown; restored from __doc__
        """ endElement(self, str, str, str) -> bool """
        return False

    def endEntity(self, p_str): # real signature unknown; restored from __doc__
        """ endEntity(self, str) -> bool """
        return False

    def endPrefixMapping(self, p_str): # real signature unknown; restored from __doc__
        """ endPrefixMapping(self, str) -> bool """
        return False

    def error(self, QXmlParseException): # real signature unknown; restored from __doc__
        """ error(self, QXmlParseException) -> bool """
        return False

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def externalEntityDecl(self, p_str, p_str_1, p_str_2): # real signature unknown; restored from __doc__
        """ externalEntityDecl(self, str, str, str) -> bool """
        return False

    def fatalError(self, QXmlParseException): # real signature unknown; restored from __doc__
        """ fatalError(self, QXmlParseException) -> bool """
        return False

    def ignorableWhitespace(self, p_str): # real signature unknown; restored from __doc__
        """ ignorableWhitespace(self, str) -> bool """
        return False

    def internalEntityDecl(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ internalEntityDecl(self, str, str) -> bool """
        return False

    def notationDecl(self, p_str, p_str_1, p_str_2): # real signature unknown; restored from __doc__
        """ notationDecl(self, str, str, str) -> bool """
        return False

    def processingInstruction(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ processingInstruction(self, str, str) -> bool """
        return False

    def resolveEntity(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ resolveEntity(self, str, str) -> Tuple[bool, QXmlInputSource] """
        pass

    def setDocumentLocator(self, QXmlLocator): # real signature unknown; restored from __doc__
        """ setDocumentLocator(self, QXmlLocator) """
        pass

    def skippedEntity(self, p_str): # real signature unknown; restored from __doc__
        """ skippedEntity(self, str) -> bool """
        return False

    def startCDATA(self): # real signature unknown; restored from __doc__
        """ startCDATA(self) -> bool """
        return False

    def startDocument(self): # real signature unknown; restored from __doc__
        """ startDocument(self) -> bool """
        return False

    def startDTD(self, p_str, p_str_1, p_str_2): # real signature unknown; restored from __doc__
        """ startDTD(self, str, str, str) -> bool """
        return False

    def startElement(self, p_str, p_str_1, p_str_2, QXmlAttributes): # real signature unknown; restored from __doc__
        """ startElement(self, str, str, str, QXmlAttributes) -> bool """
        return False

    def startEntity(self, p_str): # real signature unknown; restored from __doc__
        """ startEntity(self, str) -> bool """
        return False

    def startPrefixMapping(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ startPrefixMapping(self, str, str) -> bool """
        return False

    def unparsedEntityDecl(self, p_str, p_str_1, p_str_2, p_str_3): # real signature unknown; restored from __doc__
        """ unparsedEntityDecl(self, str, str, str, str) -> bool """
        return False

    def warning(self, QXmlParseException): # real signature unknown; restored from __doc__
        """ warning(self, QXmlParseException) -> bool """
        return False

    def __init__(self): # real signature unknown; restored from __doc__
        pass


