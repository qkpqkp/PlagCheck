# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QTextObject import QTextObject

class QTextFrame(QTextObject):
    """ QTextFrame(QTextDocument) """
    def begin(self): # real signature unknown; restored from __doc__
        """ begin(self) -> QTextFrame.iterator """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childFrames(self): # real signature unknown; restored from __doc__
        """ childFrames(self) -> List[QTextFrame] """
        return []

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def end(self): # real signature unknown; restored from __doc__
        """ end(self) -> QTextFrame.iterator """
        pass

    def firstCursorPosition(self): # real signature unknown; restored from __doc__
        """ firstCursorPosition(self) -> QTextCursor """
        return QTextCursor

    def firstPosition(self): # real signature unknown; restored from __doc__
        """ firstPosition(self) -> int """
        return 0

    def frameFormat(self): # real signature unknown; restored from __doc__
        """ frameFormat(self) -> QTextFrameFormat """
        return QTextFrameFormat

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def lastCursorPosition(self): # real signature unknown; restored from __doc__
        """ lastCursorPosition(self) -> QTextCursor """
        return QTextCursor

    def lastPosition(self): # real signature unknown; restored from __doc__
        """ lastPosition(self) -> int """
        return 0

    def parentFrame(self): # real signature unknown; restored from __doc__
        """ parentFrame(self) -> QTextFrame """
        return QTextFrame

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setFormat(self, *args, **kwargs): # real signature unknown
        pass

    def setFrameFormat(self, QTextFrameFormat): # real signature unknown; restored from __doc__
        """ setFrameFormat(self, QTextFrameFormat) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, QTextDocument): # real signature unknown; restored from __doc__
        pass



