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

class QBoxLayout(QLayout):
    """ QBoxLayout(QBoxLayout.Direction, parent: QWidget = None) """
    def addChildLayout(self, *args, **kwargs): # real signature unknown
        pass

    def addChildWidget(self, *args, **kwargs): # real signature unknown
        pass

    def addItem(self, QLayoutItem): # real signature unknown; restored from __doc__
        """ addItem(self, QLayoutItem) """
        pass

    def addLayout(self, QLayout, stretch=0): # real signature unknown; restored from __doc__
        """ addLayout(self, QLayout, stretch: int = 0) """
        pass

    def addSpacerItem(self, QSpacerItem): # real signature unknown; restored from __doc__
        """ addSpacerItem(self, QSpacerItem) """
        pass

    def addSpacing(self, p_int): # real signature unknown; restored from __doc__
        """ addSpacing(self, int) """
        pass

    def addStretch(self, stretch=0): # real signature unknown; restored from __doc__
        """ addStretch(self, stretch: int = 0) """
        pass

    def addStrut(self, p_int): # real signature unknown; restored from __doc__
        """ addStrut(self, int) """
        pass

    def addWidget(self, QWidget, stretch=0, alignment, Qt_Alignment=None, Qt_AlignmentFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ addWidget(self, QWidget, stretch: int = 0, alignment: Union[Qt.Alignment, Qt.AlignmentFlag] = Qt.Alignment()) """
        pass

    def alignmentRect(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def direction(self): # real signature unknown; restored from __doc__
        """ direction(self) -> QBoxLayout.Direction """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def expandingDirections(self): # real signature unknown; restored from __doc__
        """ expandingDirections(self) -> Qt.Orientations """
        pass

    def hasHeightForWidth(self): # real signature unknown; restored from __doc__
        """ hasHeightForWidth(self) -> bool """
        return False

    def heightForWidth(self, p_int): # real signature unknown; restored from __doc__
        """ heightForWidth(self, int) -> int """
        return 0

    def insertItem(self, p_int, QLayoutItem): # real signature unknown; restored from __doc__
        """ insertItem(self, int, QLayoutItem) """
        pass

    def insertLayout(self, p_int, QLayout, stretch=0): # real signature unknown; restored from __doc__
        """ insertLayout(self, int, QLayout, stretch: int = 0) """
        pass

    def insertSpacerItem(self, p_int, QSpacerItem): # real signature unknown; restored from __doc__
        """ insertSpacerItem(self, int, QSpacerItem) """
        pass

    def insertSpacing(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ insertSpacing(self, int, int) """
        pass

    def insertStretch(self, p_int, stretch=0): # real signature unknown; restored from __doc__
        """ insertStretch(self, int, stretch: int = 0) """
        pass

    def insertWidget(self, p_int, QWidget, stretch=0, alignment, Qt_Alignment=None, Qt_AlignmentFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ insertWidget(self, int, QWidget, stretch: int = 0, alignment: Union[Qt.Alignment, Qt.AlignmentFlag] = Qt.Alignment()) """
        pass

    def invalidate(self): # real signature unknown; restored from __doc__
        """ invalidate(self) """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def itemAt(self, p_int): # real signature unknown; restored from __doc__
        """ itemAt(self, int) -> QLayoutItem """
        return QLayoutItem

    def maximumSize(self): # real signature unknown; restored from __doc__
        """ maximumSize(self) -> QSize """
        pass

    def minimumHeightForWidth(self, p_int): # real signature unknown; restored from __doc__
        """ minimumHeightForWidth(self, int) -> int """
        return 0

    def minimumSize(self): # real signature unknown; restored from __doc__
        """ minimumSize(self) -> QSize """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setDirection(self, QBoxLayout_Direction): # real signature unknown; restored from __doc__
        """ setDirection(self, QBoxLayout.Direction) """
        pass

    def setGeometry(self, QRect): # real signature unknown; restored from __doc__
        """ setGeometry(self, QRect) """
        pass

    def setSpacing(self, p_int): # real signature unknown; restored from __doc__
        """ setSpacing(self, int) """
        pass

    def setStretch(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ setStretch(self, int, int) """
        pass

    def setStretchFactor(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setStretchFactor(self, QWidget, int) -> bool
        setStretchFactor(self, QLayout, int) -> bool
        """
        return False

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def spacing(self): # real signature unknown; restored from __doc__
        """ spacing(self) -> int """
        return 0

    def stretch(self, p_int): # real signature unknown; restored from __doc__
        """ stretch(self, int) -> int """
        return 0

    def takeAt(self, p_int): # real signature unknown; restored from __doc__
        """ takeAt(self, int) -> QLayoutItem """
        return QLayoutItem

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def widgetEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, QBoxLayout_Direction, parent=None): # real signature unknown; restored from __doc__
        pass

    BottomToTop = 3
    Down = 2
    LeftToRight = 0
    RightToLeft = 1
    TopToBottom = 2
    Up = 3


