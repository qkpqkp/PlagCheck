# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QWidget import QWidget

class QMenuBar(QWidget):
    """ QMenuBar(parent: QWidget = None) """
    def actionAt(self, QPoint): # real signature unknown; restored from __doc__
        """ actionAt(self, QPoint) -> QAction """
        return QAction

    def actionEvent(self, QActionEvent): # real signature unknown; restored from __doc__
        """ actionEvent(self, QActionEvent) """
        pass

    def actionGeometry(self, QAction): # real signature unknown; restored from __doc__
        """ actionGeometry(self, QAction) -> QRect """
        pass

    def activeAction(self): # real signature unknown; restored from __doc__
        """ activeAction(self) -> QAction """
        return QAction

    def addAction(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addAction(self, QAction)
        addAction(self, str) -> QAction
        addAction(self, str, PYQT_SLOT) -> QAction
        """
        return QAction

    def addMenu(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addMenu(self, QMenu) -> QAction
        addMenu(self, str) -> QMenu
        addMenu(self, QIcon, str) -> QMenu
        """
        return QAction or QMenu

    def addSeparator(self): # real signature unknown; restored from __doc__
        """ addSeparator(self) -> QAction """
        return QAction

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

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def cornerWidget(self, corner=None): # real signature unknown; restored from __doc__
        """ cornerWidget(self, corner: Qt.Corner = Qt.TopRightCorner) -> QWidget """
        return QWidget

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

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def eventFilter(self, QObject, QEvent): # real signature unknown; restored from __doc__
        """ eventFilter(self, QObject, QEvent) -> bool """
        return False

    def focusInEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ focusInEvent(self, QFocusEvent) """
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, QFocusEvent) """
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def heightForWidth(self, p_int): # real signature unknown; restored from __doc__
        """ heightForWidth(self, int) -> int """
        return 0

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def hovered(self, QAction): # real signature unknown; restored from __doc__
        """ hovered(self, QAction) [signal] """
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def initStyleOption(self, QStyleOptionMenuItem, QAction): # real signature unknown; restored from __doc__
        """ initStyleOption(self, QStyleOptionMenuItem, QAction) """
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def insertMenu(self, QAction, QMenu): # real signature unknown; restored from __doc__
        """ insertMenu(self, QAction, QMenu) -> QAction """
        return QAction

    def insertSeparator(self, QAction): # real signature unknown; restored from __doc__
        """ insertSeparator(self, QAction) -> QAction """
        return QAction

    def isDefaultUp(self): # real signature unknown; restored from __doc__
        """ isDefaultUp(self) -> bool """
        return False

    def isNativeMenuBar(self): # real signature unknown; restored from __doc__
        """ isNativeMenuBar(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, QKeyEvent) """
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ leaveEvent(self, QEvent) """
        pass

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

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ paintEvent(self, QPaintEvent) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ resizeEvent(self, QResizeEvent) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setActiveAction(self, QAction): # real signature unknown; restored from __doc__
        """ setActiveAction(self, QAction) """
        pass

    def setCornerWidget(self, QWidget, corner=None): # real signature unknown; restored from __doc__
        """ setCornerWidget(self, QWidget, corner: Qt.Corner = Qt.TopRightCorner) """
        pass

    def setDefaultUp(self, bool): # real signature unknown; restored from __doc__
        """ setDefaultUp(self, bool) """
        pass

    def setNativeMenuBar(self, bool): # real signature unknown; restored from __doc__
        """ setNativeMenuBar(self, bool) """
        pass

    def setVisible(self, bool): # real signature unknown; restored from __doc__
        """ setVisible(self, bool) """
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

    def timerEvent(self, QTimerEvent): # real signature unknown; restored from __doc__
        """ timerEvent(self, QTimerEvent) """
        pass

    def triggered(self, QAction): # real signature unknown; restored from __doc__
        """ triggered(self, QAction) [signal] """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


