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

class QMenu(QWidget):
    """
    QMenu(parent: QWidget = None)
    QMenu(str, parent: QWidget = None)
    """
    def aboutToHide(self): # real signature unknown; restored from __doc__
        """ aboutToHide(self) [signal] """
        pass

    def aboutToShow(self): # real signature unknown; restored from __doc__
        """ aboutToShow(self) [signal] """
        pass

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
        addAction(self, QIcon, str) -> QAction
        addAction(self, str, PYQT_SLOT, shortcut: Union[QKeySequence, QKeySequence.StandardKey, str, int] = 0) -> QAction
        addAction(self, QIcon, str, PYQT_SLOT, shortcut: Union[QKeySequence, QKeySequence.StandardKey, str, int] = 0) -> QAction
        """
        return QAction

    def addMenu(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addMenu(self, QMenu) -> QAction
        addMenu(self, str) -> QMenu
        addMenu(self, QIcon, str) -> QMenu
        """
        return QAction or QMenu

    def addSection(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addSection(self, str) -> QAction
        addSection(self, QIcon, str) -> QAction
        """
        return QAction

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

    def columnCount(self): # real signature unknown; restored from __doc__
        """ columnCount(self) -> int """
        return 0

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultAction(self): # real signature unknown; restored from __doc__
        """ defaultAction(self) -> QAction """
        return QAction

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

    def enterEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ enterEvent(self, QEvent) """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def exec(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        exec(self) -> QAction
        exec(self, QPoint, action: QAction = None) -> QAction
        exec(Iterable[QAction], QPoint, at: QAction = None, parent: QWidget = None) -> QAction
        """
        return QAction

    def exec_(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        exec_(self) -> QAction
        exec_(self, QPoint, action: QAction = None) -> QAction
        exec_(Iterable[QAction], QPoint, at: QAction = None, parent: QWidget = None) -> QAction
        """
        return QAction

    def focusInEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, bool): # real signature unknown; restored from __doc__
        """ focusNextPrevChild(self, bool) -> bool """
        return False

    def focusOutEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def hideEvent(self, QHideEvent): # real signature unknown; restored from __doc__
        """ hideEvent(self, QHideEvent) """
        pass

    def hideTearOffMenu(self): # real signature unknown; restored from __doc__
        """ hideTearOffMenu(self) """
        pass

    def hovered(self, QAction): # real signature unknown; restored from __doc__
        """ hovered(self, QAction) [signal] """
        pass

    def icon(self): # real signature unknown; restored from __doc__
        """ icon(self) -> QIcon """
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

    def insertSection(self, QAction, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        insertSection(self, QAction, str) -> QAction
        insertSection(self, QAction, QIcon, str) -> QAction
        """
        return QAction

    def insertSeparator(self, QAction): # real signature unknown; restored from __doc__
        """ insertSeparator(self, QAction) -> QAction """
        return QAction

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isTearOffEnabled(self): # real signature unknown; restored from __doc__
        """ isTearOffEnabled(self) -> bool """
        return False

    def isTearOffMenuVisible(self): # real signature unknown; restored from __doc__
        """ isTearOffMenuVisible(self) -> bool """
        return False

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, QKeyEvent) """
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ leaveEvent(self, QEvent) """
        pass

    def menuAction(self): # real signature unknown; restored from __doc__
        """ menuAction(self) -> QAction """
        return QAction

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

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ paintEvent(self, QPaintEvent) """
        pass

    def popup(self, QPoint, action=None): # real signature unknown; restored from __doc__
        """ popup(self, QPoint, action: QAction = None) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def separatorsCollapsible(self): # real signature unknown; restored from __doc__
        """ separatorsCollapsible(self) -> bool """
        return False

    def setActiveAction(self, QAction): # real signature unknown; restored from __doc__
        """ setActiveAction(self, QAction) """
        pass

    def setDefaultAction(self, QAction): # real signature unknown; restored from __doc__
        """ setDefaultAction(self, QAction) """
        pass

    def setIcon(self, QIcon): # real signature unknown; restored from __doc__
        """ setIcon(self, QIcon) """
        pass

    def setNoReplayFor(self, QWidget): # real signature unknown; restored from __doc__
        """ setNoReplayFor(self, QWidget) """
        pass

    def setSeparatorsCollapsible(self, bool): # real signature unknown; restored from __doc__
        """ setSeparatorsCollapsible(self, bool) """
        pass

    def setTearOffEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setTearOffEnabled(self, bool) """
        pass

    def setTitle(self, p_str): # real signature unknown; restored from __doc__
        """ setTitle(self, str) """
        pass

    def setToolTipsVisible(self, bool): # real signature unknown; restored from __doc__
        """ setToolTipsVisible(self, bool) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def showTearOffMenu(self, QPoint=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        showTearOffMenu(self)
        showTearOffMenu(self, QPoint)
        """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, QTimerEvent): # real signature unknown; restored from __doc__
        """ timerEvent(self, QTimerEvent) """
        pass

    def title(self): # real signature unknown; restored from __doc__
        """ title(self) -> str """
        return ""

    def toolTipsVisible(self): # real signature unknown; restored from __doc__
        """ toolTipsVisible(self) -> bool """
        return False

    def triggered(self, QAction): # real signature unknown; restored from __doc__
        """ triggered(self, QAction) [signal] """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, QWheelEvent): # real signature unknown; restored from __doc__
        """ wheelEvent(self, QWheelEvent) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


