# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QSyntaxHighlighter(__PyQt5_QtCore.QObject):
    """
    QSyntaxHighlighter(QTextDocument)
    QSyntaxHighlighter(QObject)
    """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def currentBlock(self): # real signature unknown; restored from __doc__
        """ currentBlock(self) -> QTextBlock """
        return QTextBlock

    def currentBlockState(self): # real signature unknown; restored from __doc__
        """ currentBlockState(self) -> int """
        return 0

    def currentBlockUserData(self): # real signature unknown; restored from __doc__
        """ currentBlockUserData(self) -> QTextBlockUserData """
        return QTextBlockUserData

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def document(self): # real signature unknown; restored from __doc__
        """ document(self) -> QTextDocument """
        return QTextDocument

    def format(self, p_int): # real signature unknown; restored from __doc__
        """ format(self, int) -> QTextCharFormat """
        return QTextCharFormat

    def highlightBlock(self, p_str): # real signature unknown; restored from __doc__
        """ highlightBlock(self, str) """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def previousBlockState(self): # real signature unknown; restored from __doc__
        """ previousBlockState(self) -> int """
        return 0

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def rehighlight(self): # real signature unknown; restored from __doc__
        """ rehighlight(self) """
        pass

    def rehighlightBlock(self, QTextBlock): # real signature unknown; restored from __doc__
        """ rehighlightBlock(self, QTextBlock) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCurrentBlockState(self, p_int): # real signature unknown; restored from __doc__
        """ setCurrentBlockState(self, int) """
        pass

    def setCurrentBlockUserData(self, QTextBlockUserData): # real signature unknown; restored from __doc__
        """ setCurrentBlockUserData(self, QTextBlockUserData) """
        pass

    def setDocument(self, QTextDocument): # real signature unknown; restored from __doc__
        """ setDocument(self, QTextDocument) """
        pass

    def setFormat(self, p_int, p_int_1, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setFormat(self, int, int, QTextCharFormat)
        setFormat(self, int, int, Union[QColor, Qt.GlobalColor, QGradient])
        setFormat(self, int, int, QFont)
        """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


