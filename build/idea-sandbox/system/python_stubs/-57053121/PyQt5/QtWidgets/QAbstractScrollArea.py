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

class QAbstractScrollArea(QFrame):
    """ QAbstractScrollArea(parent: QWidget = None) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def addScrollBarWidget(self, QWidget, Union, Qt_Alignment=None, Qt_AlignmentFlag=None): # real signature unknown; restored from __doc__
        """ addScrollBarWidget(self, QWidget, Union[Qt.Alignment, Qt.AlignmentFlag]) """
        pass

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, QContextMenuEvent): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, QContextMenuEvent) """
        pass

    def cornerWidget(self): # real signature unknown; restored from __doc__
        """ cornerWidget(self) -> QWidget """
        return QWidget

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dragEnterEvent(self, QDragEnterEvent): # real signature unknown; restored from __doc__
        """ dragEnterEvent(self, QDragEnterEvent) """
        pass

    def dragLeaveEvent(self, QDragLeaveEvent): # real signature unknown; restored from __doc__
        """ dragLeaveEvent(self, QDragLeaveEvent) """
        pass

    def dragMoveEvent(self, QDragMoveEvent): # real signature unknown; restored from __doc__
        """ dragMoveEvent(self, QDragMoveEvent) """
        pass

    def drawFrame(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, QDropEvent): # real signature unknown; restored from __doc__
        """ dropEvent(self, QDropEvent) """
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

    def horizontalScrollBar(self): # real signature unknown; restored from __doc__
        """ horizontalScrollBar(self) -> QScrollBar """
        return QScrollBar

    def horizontalScrollBarPolicy(self): # real signature unknown; restored from __doc__
        """ horizontalScrollBarPolicy(self) -> Qt.ScrollBarPolicy """
        pass

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

    def maximumViewportSize(self): # real signature unknown; restored from __doc__
        """ maximumViewportSize(self) -> QSize """
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> QSize """
        pass

    def mouseDoubleClickEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mouseDoubleClickEvent(self, QMouseEvent) """
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

    def scrollBarWidgets(self, Union, Qt_Alignment=None, Qt_AlignmentFlag=None): # real signature unknown; restored from __doc__
        """ scrollBarWidgets(self, Union[Qt.Alignment, Qt.AlignmentFlag]) -> List[QWidget] """
        return []

    def scrollContentsBy(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ scrollContentsBy(self, int, int) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCornerWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ setCornerWidget(self, QWidget) """
        pass

    def setHorizontalScrollBar(self, QScrollBar): # real signature unknown; restored from __doc__
        """ setHorizontalScrollBar(self, QScrollBar) """
        pass

    def setHorizontalScrollBarPolicy(self, Qt_ScrollBarPolicy): # real signature unknown; restored from __doc__
        """ setHorizontalScrollBarPolicy(self, Qt.ScrollBarPolicy) """
        pass

    def setSizeAdjustPolicy(self, QAbstractScrollArea_SizeAdjustPolicy): # real signature unknown; restored from __doc__
        """ setSizeAdjustPolicy(self, QAbstractScrollArea.SizeAdjustPolicy) """
        pass

    def setupViewport(self, QWidget): # real signature unknown; restored from __doc__
        """ setupViewport(self, QWidget) """
        pass

    def setVerticalScrollBar(self, QScrollBar): # real signature unknown; restored from __doc__
        """ setVerticalScrollBar(self, QScrollBar) """
        pass

    def setVerticalScrollBarPolicy(self, Qt_ScrollBarPolicy): # real signature unknown; restored from __doc__
        """ setVerticalScrollBarPolicy(self, Qt.ScrollBarPolicy) """
        pass

    def setViewport(self, QWidget): # real signature unknown; restored from __doc__
        """ setViewport(self, QWidget) """
        pass

    def setViewportMargins(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setViewportMargins(self, int, int, int, int)
        setViewportMargins(self, QMargins)
        """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sizeAdjustPolicy(self): # real signature unknown; restored from __doc__
        """ sizeAdjustPolicy(self) -> QAbstractScrollArea.SizeAdjustPolicy """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def verticalScrollBar(self): # real signature unknown; restored from __doc__
        """ verticalScrollBar(self) -> QScrollBar """
        return QScrollBar

    def verticalScrollBarPolicy(self): # real signature unknown; restored from __doc__
        """ verticalScrollBarPolicy(self) -> Qt.ScrollBarPolicy """
        pass

    def viewport(self): # real signature unknown; restored from __doc__
        """ viewport(self) -> QWidget """
        return QWidget

    def viewportEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ viewportEvent(self, QEvent) -> bool """
        return False

    def viewportMargins(self): # real signature unknown; restored from __doc__
        """ viewportMargins(self) -> QMargins """
        pass

    def viewportSizeHint(self): # real signature unknown; restored from __doc__
        """ viewportSizeHint(self) -> QSize """
        pass

    def wheelEvent(self, QWheelEvent): # real signature unknown; restored from __doc__
        """ wheelEvent(self, QWheelEvent) """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    AdjustIgnored = 0
    AdjustToContents = 2
    AdjustToContentsOnFirstShow = 1


