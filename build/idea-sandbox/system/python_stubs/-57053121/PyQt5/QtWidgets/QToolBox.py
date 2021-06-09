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

class QToolBox(QFrame):
    """ QToolBox(parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def addItem(self, QWidget, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addItem(self, QWidget, str) -> int
        addItem(self, QWidget, QIcon, str) -> int
        """
        return 0

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

    def currentWidget(self): # real signature unknown; restored from __doc__
        """ currentWidget(self) -> QWidget """
        return QWidget

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

    def insertItem(self, p_int, QWidget, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        insertItem(self, int, QWidget, str) -> int
        insertItem(self, int, QWidget, QIcon, str) -> int
        """
        return 0

    def isItemEnabled(self, p_int): # real signature unknown; restored from __doc__
        """ isItemEnabled(self, int) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def itemIcon(self, p_int): # real signature unknown; restored from __doc__
        """ itemIcon(self, int) -> QIcon """
        pass

    def itemInserted(self, p_int): # real signature unknown; restored from __doc__
        """ itemInserted(self, int) """
        pass

    def itemRemoved(self, p_int): # real signature unknown; restored from __doc__
        """ itemRemoved(self, int) """
        pass

    def itemText(self, p_int): # real signature unknown; restored from __doc__
        """ itemText(self, int) -> str """
        return ""

    def itemToolTip(self, p_int): # real signature unknown; restored from __doc__
        """ itemToolTip(self, int) -> str """
        return ""

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
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

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeItem(self, p_int): # real signature unknown; restored from __doc__
        """ removeItem(self, int) """
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCurrentIndex(self, p_int): # real signature unknown; restored from __doc__
        """ setCurrentIndex(self, int) """
        pass

    def setCurrentWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ setCurrentWidget(self, QWidget) """
        pass

    def setItemEnabled(self, p_int, bool): # real signature unknown; restored from __doc__
        """ setItemEnabled(self, int, bool) """
        pass

    def setItemIcon(self, p_int, QIcon): # real signature unknown; restored from __doc__
        """ setItemIcon(self, int, QIcon) """
        pass

    def setItemText(self, p_int, p_str): # real signature unknown; restored from __doc__
        """ setItemText(self, int, str) """
        pass

    def setItemToolTip(self, p_int, p_str): # real signature unknown; restored from __doc__
        """ setItemToolTip(self, int, str) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, QShowEvent): # real signature unknown; restored from __doc__
        """ showEvent(self, QShowEvent) """
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

    def __init__(self, parent=None, flags, Qt_WindowFlags=None, Qt_WindowType=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass


