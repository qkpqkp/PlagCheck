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

class QTabBar(QWidget):
    """ QTabBar(parent: QWidget = None) """
    def accessibleTabName(self, p_int): # real signature unknown; restored from __doc__
        """ accessibleTabName(self, int) -> str """
        return ""

    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def addTab(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addTab(self, str) -> int
        addTab(self, QIcon, str) -> int
        """
        return 0

    def autoHide(self): # real signature unknown; restored from __doc__
        """ autoHide(self) -> bool """
        return False

    def changeCurrentOnDrag(self): # real signature unknown; restored from __doc__
        """ changeCurrentOnDrag(self) -> bool """
        return False

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ changeEvent(self, QEvent) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

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

    def drawBase(self): # real signature unknown; restored from __doc__
        """ drawBase(self) -> bool """
        return False

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

    def expanding(self): # real signature unknown; restored from __doc__
        """ expanding(self) -> bool """
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

    def hideEvent(self, QHideEvent): # real signature unknown; restored from __doc__
        """ hideEvent(self, QHideEvent) """
        pass

    def iconSize(self): # real signature unknown; restored from __doc__
        """ iconSize(self) -> QSize """
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def initStyleOption(self, QStyleOptionTab, p_int): # real signature unknown; restored from __doc__
        """ initStyleOption(self, QStyleOptionTab, int) """
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def insertTab(self, p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        insertTab(self, int, str) -> int
        insertTab(self, int, QIcon, str) -> int
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

    def minimumTabSizeHint(self, p_int): # real signature unknown; restored from __doc__
        """ minimumTabSizeHint(self, int) -> QSize """
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

    def moveTab(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ moveTab(self, int, int) """
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

    def selectionBehaviorOnRemove(self): # real signature unknown; restored from __doc__
        """ selectionBehaviorOnRemove(self) -> QTabBar.SelectionBehavior """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAccessibleTabName(self, p_int, p_str): # real signature unknown; restored from __doc__
        """ setAccessibleTabName(self, int, str) """
        pass

    def setAutoHide(self, bool): # real signature unknown; restored from __doc__
        """ setAutoHide(self, bool) """
        pass

    def setChangeCurrentOnDrag(self, bool): # real signature unknown; restored from __doc__
        """ setChangeCurrentOnDrag(self, bool) """
        pass

    def setCurrentIndex(self, p_int): # real signature unknown; restored from __doc__
        """ setCurrentIndex(self, int) """
        pass

    def setDocumentMode(self, bool): # real signature unknown; restored from __doc__
        """ setDocumentMode(self, bool) """
        pass

    def setDrawBase(self, bool): # real signature unknown; restored from __doc__
        """ setDrawBase(self, bool) """
        pass

    def setElideMode(self, Qt_TextElideMode): # real signature unknown; restored from __doc__
        """ setElideMode(self, Qt.TextElideMode) """
        pass

    def setExpanding(self, bool): # real signature unknown; restored from __doc__
        """ setExpanding(self, bool) """
        pass

    def setIconSize(self, QSize): # real signature unknown; restored from __doc__
        """ setIconSize(self, QSize) """
        pass

    def setMovable(self, bool): # real signature unknown; restored from __doc__
        """ setMovable(self, bool) """
        pass

    def setSelectionBehaviorOnRemove(self, QTabBar_SelectionBehavior): # real signature unknown; restored from __doc__
        """ setSelectionBehaviorOnRemove(self, QTabBar.SelectionBehavior) """
        pass

    def setShape(self, QTabBar_Shape): # real signature unknown; restored from __doc__
        """ setShape(self, QTabBar.Shape) """
        pass

    def setTabButton(self, p_int, QTabBar_ButtonPosition, QWidget): # real signature unknown; restored from __doc__
        """ setTabButton(self, int, QTabBar.ButtonPosition, QWidget) """
        pass

    def setTabData(self, p_int, Any): # real signature unknown; restored from __doc__
        """ setTabData(self, int, Any) """
        pass

    def setTabEnabled(self, p_int, bool): # real signature unknown; restored from __doc__
        """ setTabEnabled(self, int, bool) """
        pass

    def setTabIcon(self, p_int, QIcon): # real signature unknown; restored from __doc__
        """ setTabIcon(self, int, QIcon) """
        pass

    def setTabsClosable(self, bool): # real signature unknown; restored from __doc__
        """ setTabsClosable(self, bool) """
        pass

    def setTabText(self, p_int, p_str): # real signature unknown; restored from __doc__
        """ setTabText(self, int, str) """
        pass

    def setTabTextColor(self, p_int, Union, QColor=None, Qt_GlobalColor=None, QGradient=None): # real signature unknown; restored from __doc__
        """ setTabTextColor(self, int, Union[QColor, Qt.GlobalColor, QGradient]) """
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

    def shape(self): # real signature unknown; restored from __doc__
        """ shape(self) -> QTabBar.Shape """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, QShowEvent): # real signature unknown; restored from __doc__
        """ showEvent(self, QShowEvent) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def tabAt(self, QPoint): # real signature unknown; restored from __doc__
        """ tabAt(self, QPoint) -> int """
        return 0

    def tabBarClicked(self, p_int): # real signature unknown; restored from __doc__
        """ tabBarClicked(self, int) [signal] """
        pass

    def tabBarDoubleClicked(self, p_int): # real signature unknown; restored from __doc__
        """ tabBarDoubleClicked(self, int) [signal] """
        pass

    def tabButton(self, p_int, QTabBar_ButtonPosition): # real signature unknown; restored from __doc__
        """ tabButton(self, int, QTabBar.ButtonPosition) -> QWidget """
        return QWidget

    def tabCloseRequested(self, p_int): # real signature unknown; restored from __doc__
        """ tabCloseRequested(self, int) [signal] """
        pass

    def tabData(self, p_int): # real signature unknown; restored from __doc__
        """ tabData(self, int) -> Any """
        pass

    def tabIcon(self, p_int): # real signature unknown; restored from __doc__
        """ tabIcon(self, int) -> QIcon """
        pass

    def tabInserted(self, p_int): # real signature unknown; restored from __doc__
        """ tabInserted(self, int) """
        pass

    def tabLayoutChange(self): # real signature unknown; restored from __doc__
        """ tabLayoutChange(self) """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def tabMoved(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ tabMoved(self, int, int) [signal] """
        pass

    def tabRect(self, p_int): # real signature unknown; restored from __doc__
        """ tabRect(self, int) -> QRect """
        pass

    def tabRemoved(self, p_int): # real signature unknown; restored from __doc__
        """ tabRemoved(self, int) """
        pass

    def tabsClosable(self): # real signature unknown; restored from __doc__
        """ tabsClosable(self) -> bool """
        return False

    def tabSizeHint(self, p_int): # real signature unknown; restored from __doc__
        """ tabSizeHint(self, int) -> QSize """
        pass

    def tabText(self, p_int): # real signature unknown; restored from __doc__
        """ tabText(self, int) -> str """
        return ""

    def tabTextColor(self, p_int): # real signature unknown; restored from __doc__
        """ tabTextColor(self, int) -> QColor """
        pass

    def tabToolTip(self, p_int): # real signature unknown; restored from __doc__
        """ tabToolTip(self, int) -> str """
        return ""

    def tabWhatsThis(self, p_int): # real signature unknown; restored from __doc__
        """ tabWhatsThis(self, int) -> str """
        return ""

    def timerEvent(self, QTimerEvent): # real signature unknown; restored from __doc__
        """ timerEvent(self, QTimerEvent) """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def usesScrollButtons(self): # real signature unknown; restored from __doc__
        """ usesScrollButtons(self) -> bool """
        return False

    def wheelEvent(self, QWheelEvent): # real signature unknown; restored from __doc__
        """ wheelEvent(self, QWheelEvent) """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    LeftSide = 0
    RightSide = 1
    RoundedEast = 3
    RoundedNorth = 0
    RoundedSouth = 1
    RoundedWest = 2
    SelectLeftTab = 0
    SelectPreviousTab = 2
    SelectRightTab = 1
    TriangularEast = 7
    TriangularNorth = 4
    TriangularSouth = 5
    TriangularWest = 6


