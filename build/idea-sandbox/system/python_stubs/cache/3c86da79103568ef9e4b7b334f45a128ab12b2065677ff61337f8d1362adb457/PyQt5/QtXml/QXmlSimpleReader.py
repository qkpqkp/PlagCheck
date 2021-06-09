# encoding: utf-8
# module PyQt5.QtXml
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtXml.pyd
# by generator 1.147
# no doc

# imports
import sip as __sip


from .QXmlReader import QXmlReader

class QXmlSimpleReader(QXmlReader):
    """ QXmlSimpleReader() """
    def contentHandler(self): # real signature unknown; restored from __doc__
        """ contentHandler(self) -> QXmlContentHandler """
        return QXmlContentHandler

    def declHandler(self): # real signature unknown; restored from __doc__
        """ declHandler(self) -> QXmlDeclHandler """
        return QXmlDeclHandler

    def DTDHandler(self): # real signature unknown; restored from __doc__
        """ DTDHandler(self) -> QXmlDTDHandler """
        return QXmlDTDHandler

    def entityResolver(self): # real signature unknown; restored from __doc__
        """ entityResolver(self) -> QXmlEntityResolver """
        return QXmlEntityResolver

    def errorHandler(self): # real signature unknown; restored from __doc__
        """ errorHandler(self) -> QXmlErrorHandler """
        return QXmlErrorHandler

    def feature(self, p_str): # real signature unknown; restored from __doc__
        """ feature(self, str) -> Tuple[bool, bool] """
        pass

    def hasFeature(self, p_str): # real signature unknown; restored from __doc__
        """ hasFeature(self, str) -> bool """
        return False

    def hasProperty(self, p_str): # real signature unknown; restored from __doc__
        """ hasProperty(self, str) -> bool """
        return False

    def lexicalHandler(self): # real signature unknown; restored from __doc__
        """ lexicalHandler(self) -> QXmlLexicalHandler """
        return QXmlLexicalHandler

    def parse(self, QXmlInputSource, bool=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        parse(self, QXmlInputSource) -> bool
        parse(self, QXmlInputSource, bool) -> bool
        """
        return False

    def parseContinue(self): # real signature unknown; restored from __doc__
        """ parseContinue(self) -> bool """
        return False

    def property(self, p_str): # real signature unknown; restored from __doc__
        """ property(self, str) -> Tuple[sip.voidptr, bool] """
        pass

    def setContentHandler(self, QXmlContentHandler): # real signature unknown; restored from __doc__
        """ setContentHandler(self, QXmlContentHandler) """
        pass

    def setDeclHandler(self, QXmlDeclHandler): # real signature unknown; restored from __doc__
        """ setDeclHandler(self, QXmlDeclHandler) """
        pass

    def setDTDHandler(self, QXmlDTDHandler): # real signature unknown; restored from __doc__
        """ setDTDHandler(self, QXmlDTDHandler) """
        pass

    def setEntityResolver(self, QXmlEntityResolver): # real signature unknown; restored from __doc__
        """ setEntityResolver(self, QXmlEntityResolver) """
        pass

    def setErrorHandler(self, QXmlErrorHandler): # real signature unknown; restored from __doc__
        """ setErrorHandler(self, QXmlErrorHandler) """
        pass

    def setFeature(self, p_str, bool): # real signature unknown; restored from __doc__
        """ setFeature(self, str, bool) """
        pass

    def setLexicalHandler(self, QXmlLexicalHandler): # real signature unknown; restored from __doc__
        """ setLexicalHandler(self, QXmlLexicalHandler) """
        pass

    def setProperty(self, p_str, sip_voidptr): # real signature unknown; restored from __doc__
        """ setProperty(self, str, sip.voidptr) """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass


