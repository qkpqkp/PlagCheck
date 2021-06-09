# encoding: utf-8
# module PyQt5.QtXml
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtXml.pyd
# by generator 1.147
# no doc

# imports
import sip as __sip


from .QDomNode import QDomNode

class QDomElement(QDomNode):
    """
    QDomElement()
    QDomElement(QDomElement)
    """
    def attribute(self, p_str, defaultValue=''): # real signature unknown; restored from __doc__
        """ attribute(self, str, defaultValue: str = '') -> str """
        return ""

    def attributeNode(self, p_str): # real signature unknown; restored from __doc__
        """ attributeNode(self, str) -> QDomAttr """
        return QDomAttr

    def attributeNodeNS(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ attributeNodeNS(self, str, str) -> QDomAttr """
        return QDomAttr

    def attributeNS(self, p_str, p_str_1, defaultValue=''): # real signature unknown; restored from __doc__
        """ attributeNS(self, str, str, defaultValue: str = '') -> str """
        return ""

    def attributes(self): # real signature unknown; restored from __doc__
        """ attributes(self) -> QDomNamedNodeMap """
        return QDomNamedNodeMap

    def elementsByTagName(self, p_str): # real signature unknown; restored from __doc__
        """ elementsByTagName(self, str) -> QDomNodeList """
        return QDomNodeList

    def elementsByTagNameNS(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ elementsByTagNameNS(self, str, str) -> QDomNodeList """
        return QDomNodeList

    def hasAttribute(self, p_str): # real signature unknown; restored from __doc__
        """ hasAttribute(self, str) -> bool """
        return False

    def hasAttributeNS(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ hasAttributeNS(self, str, str) -> bool """
        return False

    def nodeType(self): # real signature unknown; restored from __doc__
        """ nodeType(self) -> QDomNode.NodeType """
        pass

    def removeAttribute(self, p_str): # real signature unknown; restored from __doc__
        """ removeAttribute(self, str) """
        pass

    def removeAttributeNode(self, QDomAttr): # real signature unknown; restored from __doc__
        """ removeAttributeNode(self, QDomAttr) -> QDomAttr """
        return QDomAttr

    def removeAttributeNS(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ removeAttributeNS(self, str, str) """
        pass

    def setAttribute(self, p_str, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setAttribute(self, str, str)
        setAttribute(self, str, int)
        setAttribute(self, str, int)
        setAttribute(self, str, float)
        setAttribute(self, str, int)
        """
        pass

    def setAttributeNode(self, QDomAttr): # real signature unknown; restored from __doc__
        """ setAttributeNode(self, QDomAttr) -> QDomAttr """
        return QDomAttr

    def setAttributeNodeNS(self, QDomAttr): # real signature unknown; restored from __doc__
        """ setAttributeNodeNS(self, QDomAttr) -> QDomAttr """
        return QDomAttr

    def setAttributeNS(self, p_str, p_str_1, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setAttributeNS(self, str, str, str)
        setAttributeNS(self, str, str, int)
        setAttributeNS(self, str, str, int)
        setAttributeNS(self, str, str, float)
        setAttributeNS(self, str, str, int)
        """
        pass

    def setTagName(self, p_str): # real signature unknown; restored from __doc__
        """ setTagName(self, str) """
        pass

    def tagName(self): # real signature unknown; restored from __doc__
        """ tagName(self) -> str """
        return ""

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def __init__(self, QDomElement=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass


