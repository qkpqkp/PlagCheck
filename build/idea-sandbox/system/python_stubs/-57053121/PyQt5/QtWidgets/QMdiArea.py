# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QAbstractScrollArea import QAbstractScrollArea

class QMdiArea(QAbstractScrollArea):
    """ QMdiArea(parent: QWidget = None) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def activateNextSubWindow(self): # real signature unknown; restored from __doc__
        """ activateNextSubWindow(self) """
        pass

    def activatePreviousSubWindow(self): # real signature unknown; restored from __doc__
        """ activatePreviousSubWindow(self) """
        pass

    def activationOrder(self): # real signature unknown; restored from __doc__
        """ activationOrder(self) -> QMdiArea.WindowOrder """
        pass

    def activeSubWindow(self): # real signature unknown; restored from __doc__
        """ activeSubWindow(self) -> QMdiSubWindow """
        return QMdiSubWindow

    def addSubWindow(self, QWidget, flags, Qt_WindowFlags=None, Qt_WindowType=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ addSubWindow(self, QWidget, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()) -> QMdiSubWindow """
        pass

    def background(self): # real signature unknown; restored from __doc__
        """ background(self) -> QBrush """
        pass

    def cascadeSubWindows(self): # real signature unknown; restored from __doc__
        """ cascadeSubWindows(self) """
        pass

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, QChildEvent): # real signature unknown; restored from __doc__
        """ childEvent(self, QChildEvent) """
        pass

    def closeActiveSubWindow(self): # real signature unknown; restored from __doc__
        """ closeActiveSubWindow(self) """
        pass

    def closeAllSubWindows(self): # real signature unknown; restored from __doc__
        """ closeAllSubWindows(self) """
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def currentSubWindow(self): # real signature unknown; restored from __doc__
        """ currentSubWindow(self) -> QMdiSubWindow """
        return QMdiSubWindow

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

    def drawFrame(self, *args, **kwargs): # real signature unknown
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

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def initStyleOption(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
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

    def removeSubWindow(self, QWidget): # real signature unknown; restored from __doc__
        """ removeSubWindow(self, QWidget) """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ resizeEvent(self, QResizeEvent) """
        pass

    def scrollContentsBy(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ scrollContentsBy(self, int, int) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setActivationOrder(self, QMdiArea_WindowOrder): # real signature unknown; restored from __doc__
        """ setActivationOrder(self, QMdiArea.WindowOrder) """
        pass

    def setActiveSubWindow(self, QMdiSubWindow): # real signature unknown; restored from __doc__
        """ setActiveSubWindow(self, QMdiSubWindow) """
        pass

    def setBackground(self, Union, QBrush=None, QColor=None, Qt_GlobalColor=None, QGradient=None): # real signature unknown; restored from __doc__
        """ setBackground(self, Union[QBrush, QColor, Qt.GlobalColor, QGradient]) """
        pass

    def setDocumentMode(self, bool): # real signature unknown; restored from __doc__
        """ setDocumentMode(self, bool) """
        pass

    def setOption(self, QMdiArea_AreaOption, on=True): # real signature unknown; restored from __doc__
        """ setOption(self, QMdiArea.AreaOption, on: bool = True) """
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

    def setTabsMovable(self, bool): # real signature unknown; restored from __doc__
        """ setTabsMovable(self, bool) """
        pass

    def setupViewport(self, QWidget): # real signature unknown; restored from __doc__
        """ setupViewport(self, QWidget) """
        pass

    def setViewMode(self, QMdiArea_ViewMode): # real signature unknown; restored from __doc__
        """ setViewMode(self, QMdiArea.ViewMode) """
        pass

    def setViewportMargins(self, *args, **kwargs): # real signature unknown
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, QShowEvent): # real signature unknown; restored from __doc__
        """ showEvent(self, QShowEvent) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def subWindowActivated(self, QMdiSubWindow): # real signature unknown; restored from __doc__
        """ subWindowActivated(self, QMdiSubWindow) [signal] """
        pass

    def subWindowList(self, order=None): # real signature unknown; restored from __doc__
        """ subWindowList(self, order: QMdiArea.WindowOrder = QMdiArea.CreationOrder) -> List[QMdiSubWindow] """
        return []

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def tabPosition(self): # real signature unknown; restored from __doc__
        """ tabPosition(self) -> QTabWidget.TabPosition """
        pass

    def tabsClosable(self): # real signature unknown; restored from __doc__
        """ tabsClosable(self) -> bool """
        return False

    def tabShape(self): # real signature unknown; restored from __doc__
        """ tabShape(self) -> QTabWidget.TabShape """
        pass

    def tabsMovable(self): # real signature unknown; restored from __doc__
        """ tabsMovable(self) -> bool """
        return False

    def testOption(self, QMdiArea_AreaOption): # real signature unknown; restored from __doc__
        """ testOption(self, QMdiArea.AreaOption) -> bool """
        return False

    def tileSubWindows(self): # real signature unknown; restored from __doc__
        """ tileSubWindows(self) """
        pass

    def timerEvent(self, QTimerEvent): # real signature unknown; restored from __doc__
        """ timerEvent(self, QTimerEvent) """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def viewMode(self): # real signature unknown; restored from __doc__
        """ viewMode(self) -> QMdiArea.ViewMode """
        pass

    def viewportEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ viewportEvent(self, QEvent) -> bool """
        return False

    def viewportMargins(self, *args, **kwargs): # real signature unknown
        pass

    def viewportSizeHint(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    ActivationHistoryOrder = 2
    CreationOrder = 0
    DontMaximizeSubWindowOnActivation = 1
    StackingOrder = 1
    SubWindowView = 0
    TabbedView = 1


