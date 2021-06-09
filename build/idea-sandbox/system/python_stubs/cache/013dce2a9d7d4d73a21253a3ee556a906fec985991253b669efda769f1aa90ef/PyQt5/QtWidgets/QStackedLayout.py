# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QLayout import QLayout

class QStackedLayout(QLayout):
    """
    QStackedLayout()
    QStackedLayout(QWidget)
    QStackedLayout(QLayout)
    """
    def addChildLayout(self, *args, **kwargs): # real signature unknown
        pass

    def addChildWidget(self, *args, **kwargs): # real signature unknown
        pass

    def addItem(self, QLayoutItem): # real signature unknown; restored from __doc__
        """ addItem(self, QLayoutItem) """
        pass

    def addWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ addWidget(self, QWidget) -> int """
        return 0

    def alignmentRect(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

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

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def hasHeightForWidth(self): # real signature unknown; restored from __doc__
        """ hasHeightForWidth(self) -> bool """
        return False

    def heightForWidth(self, p_int): # real signature unknown; restored from __doc__
        """ heightForWidth(self, int) -> int """
        return 0

    def insertWidget(self, p_int, QWidget): # real signature unknown; restored from __doc__
        """ insertWidget(self, int, QWidget) -> int """
        return 0

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def itemAt(self, p_int): # real signature unknown; restored from __doc__
        """ itemAt(self, int) -> QLayoutItem """
        return QLayoutItem

    def minimumSize(self): # real signature unknown; restored from __doc__
        """ minimumSize(self) -> QSize """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
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

    def setGeometry(self, QRect): # real signature unknown; restored from __doc__
        """ setGeometry(self, QRect) """
        pass

    def setStackingMode(self, QStackedLayout_StackingMode): # real signature unknown; restored from __doc__
        """ setStackingMode(self, QStackedLayout.StackingMode) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def stackingMode(self): # real signature unknown; restored from __doc__
        """ stackingMode(self) -> QStackedLayout.StackingMode """
        pass

    def takeAt(self, p_int): # real signature unknown; restored from __doc__
        """ takeAt(self, int) -> QLayoutItem """
        return QLayoutItem

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def widget(self, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        widget(self, int) -> QWidget
        widget(self) -> QWidget
        """
        return QWidget

    def widgetEvent(self, *args, **kwargs): # real signature unknown
        pass

    def widgetRemoved(self, p_int): # real signature unknown; restored from __doc__
        """ widgetRemoved(self, int) [signal] """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    StackAll = 1
    StackOne = 0


