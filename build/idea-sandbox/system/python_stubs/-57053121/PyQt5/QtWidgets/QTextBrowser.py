# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QTextEdit import QTextEdit

class QTextBrowser(QTextEdit):
    """ QTextBrowser(parent: QWidget = None) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def anchorClicked(self, QUrl): # real signature unknown; restored from __doc__
        """ anchorClicked(self, QUrl) [signal] """
        pass

    def backward(self): # real signature unknown; restored from __doc__
        """ backward(self) """
        pass

    def backwardAvailable(self, bool): # real signature unknown; restored from __doc__
        """ backwardAvailable(self, bool) [signal] """
        pass

    def backwardHistoryCount(self): # real signature unknown; restored from __doc__
        """ backwardHistoryCount(self) -> int """
        return 0

    def canInsertFromMimeData(self, *args, **kwargs): # real signature unknown
        pass

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clearHistory(self): # real signature unknown; restored from __doc__
        """ clearHistory(self) """
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def createMimeDataFromSelection(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def drawFrame(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def eventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def focusInEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, bool): # real signature unknown; restored from __doc__
        """ focusNextPrevChild(self, bool) -> bool """
        return False

    def focusOutEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, QFocusEvent) """
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def forward(self): # real signature unknown; restored from __doc__
        """ forward(self) """
        pass

    def forwardAvailable(self, bool): # real signature unknown; restored from __doc__
        """ forwardAvailable(self, bool) [signal] """
        pass

    def forwardHistoryCount(self): # real signature unknown; restored from __doc__
        """ forwardHistoryCount(self) -> int """
        return 0

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def highlighted(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        highlighted(self, QUrl) [signal]
        highlighted(self, str) [signal]
        """
        pass

    def historyChanged(self): # real signature unknown; restored from __doc__
        """ historyChanged(self) [signal] """
        pass

    def historyTitle(self, p_int): # real signature unknown; restored from __doc__
        """ historyTitle(self, int) -> str """
        return ""

    def historyUrl(self, p_int): # real signature unknown; restored from __doc__
        """ historyUrl(self, int) -> QUrl """
        pass

    def home(self): # real signature unknown; restored from __doc__
        """ home(self) """
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def initStyleOption(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def insertFromMimeData(self, *args, **kwargs): # real signature unknown
        pass

    def isBackwardAvailable(self): # real signature unknown; restored from __doc__
        """ isBackwardAvailable(self) -> bool """
        return False

    def isForwardAvailable(self): # real signature unknown; restored from __doc__
        """ isForwardAvailable(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, QKeyEvent) """
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def loadResource(self, p_int, QUrl): # real signature unknown; restored from __doc__
        """ loadResource(self, int, QUrl) -> Any """
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mouseMoveEvent(self, QMouseEvent) """
        pass

    def mousePressEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, QMouseEvent) """
        pass

    def mouseReleaseEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, QMouseEvent) """
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def openExternalLinks(self): # real signature unknown; restored from __doc__
        """ openExternalLinks(self) -> bool """
        return False

    def openLinks(self): # real signature unknown; restored from __doc__
        """ openLinks(self) -> bool """
        return False

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ paintEvent(self, QPaintEvent) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def reload(self): # real signature unknown; restored from __doc__
        """ reload(self) """
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def scrollContentsBy(self, *args, **kwargs): # real signature unknown
        pass

    def searchPaths(self): # real signature unknown; restored from __doc__
        """ searchPaths(self) -> List[str] """
        return []

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setOpenExternalLinks(self, bool): # real signature unknown; restored from __doc__
        """ setOpenExternalLinks(self, bool) """
        pass

    def setOpenLinks(self, bool): # real signature unknown; restored from __doc__
        """ setOpenLinks(self, bool) """
        pass

    def setSearchPaths(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ setSearchPaths(self, Iterable[str]) """
        pass

    def setSource(self, QUrl): # real signature unknown; restored from __doc__
        """ setSource(self, QUrl) """
        pass

    def setViewportMargins(self, *args, **kwargs): # real signature unknown
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def source(self): # real signature unknown; restored from __doc__
        """ source(self) -> QUrl """
        pass

    def sourceChanged(self, QUrl): # real signature unknown; restored from __doc__
        """ sourceChanged(self, QUrl) [signal] """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def viewportEvent(self, *args, **kwargs): # real signature unknown
        pass

    def viewportMargins(self, *args, **kwargs): # real signature unknown
        pass

    def viewportSizeHint(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


