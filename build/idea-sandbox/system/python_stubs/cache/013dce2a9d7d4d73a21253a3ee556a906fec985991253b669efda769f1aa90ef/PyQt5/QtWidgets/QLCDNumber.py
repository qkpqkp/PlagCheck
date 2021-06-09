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

class QLCDNumber(QFrame):
    """
    QLCDNumber(parent: QWidget = None)
    QLCDNumber(int, parent: QWidget = None)
    """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def checkOverflow(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        checkOverflow(self, float) -> bool
        checkOverflow(self, int) -> bool
        """
        return False

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def digitCount(self): # real signature unknown; restored from __doc__
        """ digitCount(self) -> int """
        return 0

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def display(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        display(self, str)
        display(self, float)
        display(self, int)
        """
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

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def initStyleOption(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def intValue(self): # real signature unknown; restored from __doc__
        """ intValue(self) -> int """
        return 0

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

    def mode(self): # real signature unknown; restored from __doc__
        """ mode(self) -> QLCDNumber.Mode """
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

    def overflow(self): # real signature unknown; restored from __doc__
        """ overflow(self) [signal] """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ paintEvent(self, QPaintEvent) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def segmentStyle(self): # real signature unknown; restored from __doc__
        """ segmentStyle(self) -> QLCDNumber.SegmentStyle """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setBinMode(self): # real signature unknown; restored from __doc__
        """ setBinMode(self) """
        pass

    def setDecMode(self): # real signature unknown; restored from __doc__
        """ setDecMode(self) """
        pass

    def setDigitCount(self, p_int): # real signature unknown; restored from __doc__
        """ setDigitCount(self, int) """
        pass

    def setHexMode(self): # real signature unknown; restored from __doc__
        """ setHexMode(self) """
        pass

    def setMode(self, QLCDNumber_Mode): # real signature unknown; restored from __doc__
        """ setMode(self, QLCDNumber.Mode) """
        pass

    def setNumDigits(self, p_int): # real signature unknown; restored from __doc__
        """ setNumDigits(self, int) """
        pass

    def setOctMode(self): # real signature unknown; restored from __doc__
        """ setOctMode(self) """
        pass

    def setSegmentStyle(self, QLCDNumber_SegmentStyle): # real signature unknown; restored from __doc__
        """ setSegmentStyle(self, QLCDNumber.SegmentStyle) """
        pass

    def setSmallDecimalPoint(self, bool): # real signature unknown; restored from __doc__
        """ setSmallDecimalPoint(self, bool) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def smallDecimalPoint(self): # real signature unknown; restored from __doc__
        """ smallDecimalPoint(self) -> bool """
        return False

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def value(self): # real signature unknown; restored from __doc__
        """ value(self) -> float """
        return 0.0

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    Bin = 3
    Dec = 1
    Filled = 1
    Flat = 2
    Hex = 0
    Oct = 2
    Outline = 0


