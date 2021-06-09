# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QClipboard(__PyQt5_QtCore.QObject):
    # no doc
    def changed(self, QClipboard_Mode): # real signature unknown; restored from __doc__
        """ changed(self, QClipboard.Mode) [signal] """
        pass

    def clear(self, mode=None): # real signature unknown; restored from __doc__
        """ clear(self, mode: QClipboard.Mode = QClipboard.Clipboard) """
        pass

    def dataChanged(self): # real signature unknown; restored from __doc__
        """ dataChanged(self) [signal] """
        pass

    def findBufferChanged(self): # real signature unknown; restored from __doc__
        """ findBufferChanged(self) [signal] """
        pass

    def image(self, mode=None): # real signature unknown; restored from __doc__
        """ image(self, mode: QClipboard.Mode = QClipboard.Clipboard) -> QImage """
        return QImage

    def mimeData(self, mode=None): # real signature unknown; restored from __doc__
        """ mimeData(self, mode: QClipboard.Mode = QClipboard.Clipboard) -> QMimeData """
        pass

    def ownsClipboard(self): # real signature unknown; restored from __doc__
        """ ownsClipboard(self) -> bool """
        return False

    def ownsFindBuffer(self): # real signature unknown; restored from __doc__
        """ ownsFindBuffer(self) -> bool """
        return False

    def ownsSelection(self): # real signature unknown; restored from __doc__
        """ ownsSelection(self) -> bool """
        return False

    def pixmap(self, mode=None): # real signature unknown; restored from __doc__
        """ pixmap(self, mode: QClipboard.Mode = QClipboard.Clipboard) -> QPixmap """
        return QPixmap

    def selectionChanged(self): # real signature unknown; restored from __doc__
        """ selectionChanged(self) [signal] """
        pass

    def setImage(self, QImage, mode=None): # real signature unknown; restored from __doc__
        """ setImage(self, QImage, mode: QClipboard.Mode = QClipboard.Clipboard) """
        pass

    def setMimeData(self, QMimeData, mode=None): # real signature unknown; restored from __doc__
        """ setMimeData(self, QMimeData, mode: QClipboard.Mode = QClipboard.Clipboard) """
        pass

    def setPixmap(self, QPixmap, mode=None): # real signature unknown; restored from __doc__
        """ setPixmap(self, QPixmap, mode: QClipboard.Mode = QClipboard.Clipboard) """
        pass

    def setText(self, p_str, mode=None): # real signature unknown; restored from __doc__
        """ setText(self, str, mode: QClipboard.Mode = QClipboard.Clipboard) """
        pass

    def supportsFindBuffer(self): # real signature unknown; restored from __doc__
        """ supportsFindBuffer(self) -> bool """
        return False

    def supportsSelection(self): # real signature unknown; restored from __doc__
        """ supportsSelection(self) -> bool """
        return False

    def text(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        text(self, mode: QClipboard.Mode = QClipboard.Clipboard) -> str
        text(self, str, mode: QClipboard.Mode = QClipboard.Clipboard) -> Tuple[str, str]
        """
        return ""

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    Clipboard = 0
    FindBuffer = 2
    Selection = 1


