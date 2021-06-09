# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QTextDocumentFragment(__sip.simplewrapper):
    """
    QTextDocumentFragment()
    QTextDocumentFragment(QTextDocument)
    QTextDocumentFragment(QTextCursor)
    QTextDocumentFragment(QTextDocumentFragment)
    """
    def fromHtml(self, p_str, QTextDocument=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        fromHtml(str) -> QTextDocumentFragment
        fromHtml(str, QTextDocument) -> QTextDocumentFragment
        """
        return QTextDocumentFragment

    def fromPlainText(self, p_str): # real signature unknown; restored from __doc__
        """ fromPlainText(str) -> QTextDocumentFragment """
        return QTextDocumentFragment

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def toHtml(self, encoding, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ toHtml(self, encoding: Union[QByteArray, bytes, bytearray] = QByteArray()) -> str """
        pass

    def toPlainText(self): # real signature unknown; restored from __doc__
        """ toPlainText(self) -> str """
        return ""

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



