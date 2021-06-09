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

class QTabWidget(QWidget):
    """ QTabWidget(parent: QWidget = None) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def addTab(self, QWidget, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addTab(self, QWidget, str) -> int
        addTab(self, QWidget, QIcon, str) -> int
        """
        return 0

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

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def currentChanged(self, p_int): # real signature unknown; restored from __doc__
        """ currentChanged(self, int) [signal] """
        pass

    def currentIndex(self): # real signature unknown; restored from __doc__
        """ currentIndex(self) -> int """
        return 0

    def currentWidget(self): # real signature unknown; restored from __doc__
        """ currentWidget(self) -> QWidget """
        return QWidget

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def documentMode(self): # real signature unknown; restored from __doc__
        """ documentMode(self) -> bool """
        return False

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def elideMode(self): # real signature unknown; restored from __doc__
        """ elideMode(self) -> Qt.TextElideMode """
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def focusInEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def hasHeightForWidth(self): # real signature unknown; restored from __doc__
        """ hasHeightForWidth(self) -> bool """
        return False

    def heightForWidth(self, p_int): # real signature unknown; restored from __doc__
        """ heightForWidth(self, int) -> int """
        return 0

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def iconSize(self): # real signature unknown; restored from __doc__
        """ iconSize(self) -> QSize """
        pass

    def indexOf(self, QWidget): # real signature unknown; restored from __doc__
        """ indexOf(self, QWidget) -> int """
        return 0

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def initStyleOption(self, QStyleOptionTabWidgetFrame): # real signature unknown; restored from __doc__
        """ initStyleOption(self, QStyleOptionTabWidgetFrame) """
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def insertTab(self, p_int, QWidget, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        insertTab(self, int, QWidget, str) -> int
        insertTab(self, int, QWidget, QIcon, str) -> int
        """
        return 0

    def isMovable(self): # real signature unknown; restored from __doc__
        """ isMovable(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isTabEnabled(self, p_int): # real signature unknown; restored from __doc__
        """ isTabEnabled(self, int) -> bool """
        return False

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, QKeyEvent) """
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> QSize """
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseReleaseEvent(self, *args, **kwargs): # real signature unknown
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

    def removeTab(self, p_int): # real signature unknown; restored from __doc__
        """ removeTab(self, int) """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ resizeEvent(self, QResizeEvent) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCornerWidget(self, QWidget, corner=None): # real signature unknown; restored from __doc__
        """ setCornerWidget(self, QWidget, corner: Qt.Corner = Qt.TopRightCorner) """
        pass

    def setCurrentIndex(self, p_int): # real signature unknown; restored from __doc__
        """ setCurrentIndex(self, int) """
        pass

    def setCurrentWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ setCurrentWidget(self, QWidget) """
        pass

    def setDocumentMode(self, bool): # real signature unknown; restored from __doc__
        """ setDocumentMode(self, bool) """
        pass

    def setElideMode(self, Qt_TextElideMode): # real signature unknown; restored from __doc__
        """ setElideMode(self, Qt.TextElideMode) """
        pass

    def setIconSize(self, QSize): # real signature unknown; restored from __doc__
        """ setIconSize(self, QSize) """
        pass

    def setMovable(self, bool): # real signature unknown; restored from __doc__
        """ setMovable(self, bool) """
        pass

    def setTabBar(self, QTabBar): # real signature unknown; restored from __doc__
        """ setTabBar(self, QTabBar) """
        pass

    def setTabBarAutoHide(self, bool): # real signature unknown; restored from __doc__
        """ setTabBarAutoHide(self, bool) """
        pass

    def setTabEnabled(self, p_int, bool): # real signature unknown; restored from __doc__
        """ setTabEnabled(self, int, bool) """
        pass

    def setTabIcon(self, p_int, QIcon): # real signature unknown; restored from __doc__
        """ setTabIcon(self, int, QIcon) """
        pass

    def setTabPosition(self, QTabWidget_TabPosition): # real signature unknown; restored from __doc__
        """ setTabPosition(self, QTabWidget.TabPosition) """
        pass

    def setTabsClosable(self, bool): # real signature unknown; restored from __doc__
        """ setTabsClosable(self, bool) """
        pass

    def setTabShape(self, QTabWidget_TabShape): # real signature unknown; restored from __doc__
        """ setTabShape(self, QTabWidget.TabShape) """
        pass

    def setTabText(self, p_int, p_str): # real signature unknown; restored from __doc__
        """ setTabText(self, int, str) """
        pass

    def setTabToolTip(self, p_int, p_str): # real signature unknown; restored from __doc__
        """ setTabToolTip(self, int, str) """
        pass

    def setTabWhatsThis(self, p_int, p_str): # real signature unknown; restored from __doc__
        """ setTabWhatsThis(self, int, str) """
        pass

    def setUsesScrollButtons(self, bool): # real signature unknown; restored from __doc__
        """ setUsesScrollButtons(self, bool) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, QShowEvent): # real signature unknown; restored from __doc__
        """ showEvent(self, QShowEvent) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def tabBar(self): # real signature unknown; restored from __doc__
        """ tabBar(self) -> QTabBar """
        return QTabBar

    def tabBarAutoHide(self): # real signature unknown; restored from __doc__
        """ tabBarAutoHide(self) -> bool """
        return False

    def tabBarClicked(self, p_int): # real signature unknown; restored from __doc__
        """ tabBarClicked(self, int) [signal] """
        pass

    def tabBarDoubleClicked(self, p_int): # real signature unknown; restored from __doc__
        """ tabBarDoubleClicked(self, int) [signal] """
        pass

    def tabCloseRequested(self, p_int): # real signature unknown; restored from __doc__
        """ tabCloseRequested(self, int) [signal] """
        pass

    def tabIcon(self, p_int): # real signature unknown; restored from __doc__
        """ tabIcon(self, int) -> QIcon """
        pass

    def tabInserted(self, p_int): # real signature unknown; restored from __doc__
        """ tabInserted(self, int) """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def tabPosition(self): # real signature unknown; restored from __doc__
        """ tabPosition(self) -> QTabWidget.TabPosition """
        pass

    def tabRemoved(self, p_int): # real signature unknown; restored from __doc__
        """ tabRemoved(self, int) """
        pass

    def tabsClosable(self): # real signature unknown; restored from __doc__
        """ tabsClosable(self) -> bool """
        return False

    def tabShape(self): # real signature unknown; restored from __doc__
        """ tabShape(self) -> QTabWidget.TabShape """
        pass

    def tabText(self, p_int): # real signature unknown; restored from __doc__
        """ tabText(self, int) -> str """
        return ""

    def tabToolTip(self, p_int): # real signature unknown; restored from __doc__
        """ tabToolTip(self, int) -> str """
        return ""

    def tabWhatsThis(self, p_int): # real signature unknown; restored from __doc__
        """ tabWhatsThis(self, int) -> str """
        return ""

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def usesScrollButtons(self): # real signature unknown; restored from __doc__
        """ usesScrollButtons(self) -> bool """
        return False

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def widget(self, p_int): # real signature unknown; restored from __doc__
        """ widget(self, int) -> QWidget """
        return QWidget

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    East = 3
    North = 0
    Rounded = 0
    South = 1
    Triangular = 1
    West = 2


