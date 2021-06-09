# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QFrame import QFrame

class QLabel(QFrame):
    """
    QLabel(parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags())
    QLabel(str, parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags())
    """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def alignment(self): # real signature unknown; restored from __doc__
        """ alignment(self) -> Qt.Alignment """
        pass

    def buddy(self): # real signature unknown; restored from __doc__
        """ buddy(self) -> QWidget """
        return QWidget

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ changeEvent(self, QEvent) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, QContextMenuEvent): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, QContextMenuEvent) """
        pass

    def create(self, *args, **kwargs): # real signature unknown
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

    def focusInEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ focusInEvent(self, QFocusEvent) """
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

    def hasScaledContents(self): # real signature unknown; restored from __doc__
        """ hasScaledContents(self) -> bool """
        return False

    def hasSelectedText(self): # real signature unknown; restored from __doc__
        """ hasSelectedText(self) -> bool """
        return False

    def heightForWidth(self, p_int): # real signature unknown; restored from __doc__
        """ heightForWidth(self, int) -> int """
        return 0

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def indent(self): # real signature unknown; restored from __doc__
        """ indent(self) -> int """
        return 0

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def initStyleOption(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, QKeyEvent) """
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def linkActivated(self, p_str): # real signature unknown; restored from __doc__
        """ linkActivated(self, str) [signal] """
        pass

    def linkHovered(self, p_str): # real signature unknown; restored from __doc__
        """ linkHovered(self, str) [signal] """
        pass

    def margin(self): # real signature unknown; restored from __doc__
        """ margin(self) -> int """
        return 0

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> QSize """
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

    def movie(self): # real signature unknown; restored from __doc__
        """ movie(self) -> QMovie """
        pass

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def openExternalLinks(self): # real signature unknown; restored from __doc__
        """ openExternalLinks(self) -> bool """
        return False

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ paintEvent(self, QPaintEvent) """
        pass

    def picture(self): # real signature unknown; restored from __doc__
        """ picture(self) -> QPicture """
        pass

    def pixmap(self): # real signature unknown; restored from __doc__
        """ pixmap(self) -> QPixmap """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def selectedText(self): # real signature unknown; restored from __doc__
        """ selectedText(self) -> str """
        return ""

    def selectionStart(self): # real signature unknown; restored from __doc__
        """ selectionStart(self) -> int """
        return 0

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAlignment(self, Union, Qt_Alignment=None, Qt_AlignmentFlag=None): # real signature unknown; restored from __doc__
        """ setAlignment(self, Union[Qt.Alignment, Qt.AlignmentFlag]) """
        pass

    def setBuddy(self, QWidget): # real signature unknown; restored from __doc__
        """ setBuddy(self, QWidget) """
        pass

    def setIndent(self, p_int): # real signature unknown; restored from __doc__
        """ setIndent(self, int) """
        pass

    def setMargin(self, p_int): # real signature unknown; restored from __doc__
        """ setMargin(self, int) """
        pass

    def setMovie(self, QMovie): # real signature unknown; restored from __doc__
        """ setMovie(self, QMovie) """
        pass

    def setNum(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setNum(self, float)
        setNum(self, int)
        """
        pass

    def setOpenExternalLinks(self, bool): # real signature unknown; restored from __doc__
        """ setOpenExternalLinks(self, bool) """
        pass

    def setPicture(self, QPicture): # real signature unknown; restored from __doc__
        """ setPicture(self, QPicture) """
        pass

    def setPixmap(self, QPixmap): # real signature unknown; restored from __doc__
        """ setPixmap(self, QPixmap) """
        pass

    def setScaledContents(self, bool): # real signature unknown; restored from __doc__
        """ setScaledContents(self, bool) """
        pass

    def setSelection(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ setSelection(self, int, int) """
        pass

    def setText(self, p_str): # real signature unknown; restored from __doc__
        """ setText(self, str) """
        pass

    def setTextFormat(self, Qt_TextFormat): # real signature unknown; restored from __doc__
        """ setTextFormat(self, Qt.TextFormat) """
        pass

    def setTextInteractionFlags(self, Union, Qt_TextInteractionFlags=None, Qt_TextInteractionFlag=None): # real signature unknown; restored from __doc__
        """ setTextInteractionFlags(self, Union[Qt.TextInteractionFlags, Qt.TextInteractionFlag]) """
        pass

    def setWordWrap(self, bool): # real signature unknown; restored from __doc__
        """ setWordWrap(self, bool) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def textFormat(self): # real signature unknown; restored from __doc__
        """ textFormat(self) -> Qt.TextFormat """
        pass

    def textInteractionFlags(self): # real signature unknown; restored from __doc__
        """ textInteractionFlags(self) -> Qt.TextInteractionFlags """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def wordWrap(self): # real signature unknown; restored from __doc__
        """ wordWrap(self) -> bool """
        return False

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


