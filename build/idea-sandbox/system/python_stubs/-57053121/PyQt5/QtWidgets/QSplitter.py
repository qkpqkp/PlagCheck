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

class QSplitter(QFrame):
    """
    QSplitter(parent: QWidget = None)
    QSplitter(Qt.Orientation, parent: QWidget = None)
    """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def addWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ addWidget(self, QWidget) """
        pass

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ changeEvent(self, QEvent) """
        pass

    def childEvent(self, QChildEvent): # real signature unknown; restored from __doc__
        """ childEvent(self, QChildEvent) """
        pass

    def childrenCollapsible(self): # real signature unknown; restored from __doc__
        """ childrenCollapsible(self) -> bool """
        return False

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closestLegalPosition(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ closestLegalPosition(self, int, int) -> int """
        return 0

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def createHandle(self): # real signature unknown; restored from __doc__
        """ createHandle(self) -> QSplitterHandle """
        return QSplitterHandle

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

    def getRange(self, p_int): # real signature unknown; restored from __doc__
        """ getRange(self, int) -> Tuple[int, int] """
        pass

    def handle(self, p_int): # real signature unknown; restored from __doc__
        """ handle(self, int) -> QSplitterHandle """
        return QSplitterHandle

    def handleWidth(self): # real signature unknown; restored from __doc__
        """ handleWidth(self) -> int """
        return 0

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def indexOf(self, QWidget): # real signature unknown; restored from __doc__
        """ indexOf(self, QWidget) -> int """
        return 0

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def initStyleOption(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def insertWidget(self, p_int, QWidget): # real signature unknown; restored from __doc__
        """ insertWidget(self, int, QWidget) """
        pass

    def isCollapsible(self, p_int): # real signature unknown; restored from __doc__
        """ isCollapsible(self, int) -> bool """
        return False

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

    def moveSplitter(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ moveSplitter(self, int, int) """
        pass

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def opaqueResize(self): # real signature unknown; restored from __doc__
        """ opaqueResize(self) -> bool """
        return False

    def orientation(self): # real signature unknown; restored from __doc__
        """ orientation(self) -> Qt.Orientation """
        pass

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def refresh(self): # real signature unknown; restored from __doc__
        """ refresh(self) """
        pass

    def replaceWidget(self, p_int, QWidget): # real signature unknown; restored from __doc__
        """ replaceWidget(self, int, QWidget) -> QWidget """
        return QWidget

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ resizeEvent(self, QResizeEvent) """
        pass

    def restoreState(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ restoreState(self, Union[QByteArray, bytes, bytearray]) -> bool """
        return False

    def saveState(self): # real signature unknown; restored from __doc__
        """ saveState(self) -> QByteArray """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setChildrenCollapsible(self, bool): # real signature unknown; restored from __doc__
        """ setChildrenCollapsible(self, bool) """
        pass

    def setCollapsible(self, p_int, bool): # real signature unknown; restored from __doc__
        """ setCollapsible(self, int, bool) """
        pass

    def setHandleWidth(self, p_int): # real signature unknown; restored from __doc__
        """ setHandleWidth(self, int) """
        pass

    def setOpaqueResize(self, opaque=True): # real signature unknown; restored from __doc__
        """ setOpaqueResize(self, opaque: bool = True) """
        pass

    def setOrientation(self, Qt_Orientation): # real signature unknown; restored from __doc__
        """ setOrientation(self, Qt.Orientation) """
        pass

    def setRubberBand(self, p_int): # real signature unknown; restored from __doc__
        """ setRubberBand(self, int) """
        pass

    def setSizes(self, Iterable, p_int=None): # real signature unknown; restored from __doc__
        """ setSizes(self, Iterable[int]) """
        pass

    def setStretchFactor(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ setStretchFactor(self, int, int) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def sizes(self): # real signature unknown; restored from __doc__
        """ sizes(self) -> List[int] """
        return []

    def splitterMoved(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ splitterMoved(self, int, int) [signal] """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def widget(self, p_int): # real signature unknown; restored from __doc__
        """ widget(self, int) -> QWidget """
        return QWidget

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass


