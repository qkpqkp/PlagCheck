# encoding: utf-8
# module PyQt5.QtXml
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtXml.pyd
# by generator 1.147
# no doc

# imports
import sip as __sip


class QXmlErrorHandler(__sip.simplewrapper):
    """
    QXmlErrorHandler()
    QXmlErrorHandler(QXmlErrorHandler)
    """
    def error(self, QXmlParseException): # real signature unknown; restored from __doc__
        """ error(self, QXmlParseException) -> bool """
        return False

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def fatalError(self, QXmlParseException): # real signature unknown; restored from __doc__
        """ fatalError(self, QXmlParseException) -> bool """
        return False

    def warning(self, QXmlParseException): # real signature unknown; restored from __doc__
        """ warning(self, QXmlParseException) -> bool """
        return False

    def __init__(self, QXmlErrorHandler=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



