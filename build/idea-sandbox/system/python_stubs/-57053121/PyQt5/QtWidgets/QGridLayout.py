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

class QGridLayout(QLayout):
    """
    QGridLayout(QWidget)
    QGridLayout()
    """
    def addChildLayout(self, *args, **kwargs): # real signature unknown
        pass

    def addChildWidget(self, *args, **kwargs): # real signature unknown
        pass

    def addItem(self, QLayoutItem, p_int=None, p_int_1=None, rowSpan=1, columnSpan=1, alignment=None, Qt_Alignment=None, Qt_AlignmentFlag=None, *args=None, **kwargs=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addItem(self, QLayoutItem, int, int, rowSpan: int = 1, columnSpan: int = 1, alignment: Union[Qt.Alignment, Qt.AlignmentFlag] = Qt.Alignment())
        addItem(self, QLayoutItem)
        """
        pass

    def addLayout(self, QLayout, p_int, p_int_1, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addLayout(self, QLayout, int, int, alignment: Union[Qt.Alignment, Qt.AlignmentFlag] = Qt.Alignment())
        addLayout(self, QLayout, int, int, int, int, alignment: Union[Qt.Alignment, Qt.AlignmentFlag] = Qt.Alignment())
        """
        pass

    def addWidget(self, QWidget, p_int=None, p_int_1=None, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addWidget(self, QWidget)
        addWidget(self, QWidget, int, int, alignment: Union[Qt.Alignment, Qt.AlignmentFlag] = Qt.Alignment())
        addWidget(self, QWidget, int, int, int, int, alignment: Union[Qt.Alignment, Qt.AlignmentFlag] = Qt.Alignment())
        """
        pass

    def alignmentRect(self, *args, **kwargs): # real signature unknown
        pass

    def cellRect(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ cellRect(self, int, int) -> QRect """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def columnCount(self): # real signature unknown; restored from __doc__
        """ columnCount(self) -> int """
        return 0

    def columnMinimumWidth(self, p_int): # real signature unknown; restored from __doc__
        """ columnMinimumWidth(self, int) -> int """
        return 0

    def columnStretch(self, p_int): # real signature unknown; restored from __doc__
        """ columnStretch(self, int) -> int """
        return 0

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def expandingDirections(self): # real signature unknown; restored from __doc__
        """ expandingDirections(self) -> Qt.Orientations """
        pass

    def getItemPosition(self, p_int): # real signature unknown; restored from __doc__
        """ getItemPosition(self, int) -> Tuple[int, int, int, int] """
        pass

    def hasHeightForWidth(self): # real signature unknown; restored from __doc__
        """ hasHeightForWidth(self) -> bool """
        return False

    def heightForWidth(self, p_int): # real signature unknown; restored from __doc__
        """ heightForWidth(self, int) -> int """
        return 0

    def horizontalSpacing(self): # real signature unknown; restored from __doc__
        """ horizontalSpacing(self) -> int """
        return 0

    def invalidate(self): # real signature unknown; restored from __doc__
        """ invalidate(self) """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def itemAt(self, p_int): # real signature unknown; restored from __doc__
        """ itemAt(self, int) -> QLayoutItem """
        return QLayoutItem

    def itemAtPosition(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ itemAtPosition(self, int, int) -> QLayoutItem """
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

    def originCorner(self): # real signature unknown; restored from __doc__
        """ originCorner(self) -> Qt.Corner """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def rowCount(self): # real signature unknown; restored from __doc__
        """ rowCount(self) -> int """
        return 0

    def rowMinimumHeight(self, p_int): # real signature unknown; restored from __doc__
        """ rowMinimumHeight(self, int) -> int """
        return 0

    def rowStretch(self, p_int): # real signature unknown; restored from __doc__
        """ rowStretch(self, int) -> int """
        return 0

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setColumnMinimumWidth(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ setColumnMinimumWidth(self, int, int) """
        pass

    def setColumnStretch(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ setColumnStretch(self, int, int) """
        pass

    def setDefaultPositioning(self, p_int, Qt_Orientation): # real signature unknown; restored from __doc__
        """ setDefaultPositioning(self, int, Qt.Orientation) """
        pass

    def setGeometry(self, QRect): # real signature unknown; restored from __doc__
        """ setGeometry(self, QRect) """
        pass

    def setHorizontalSpacing(self, p_int): # real signature unknown; restored from __doc__
        """ setHorizontalSpacing(self, int) """
        pass

    def setOriginCorner(self, Qt_Corner): # real signature unknown; restored from __doc__
        """ setOriginCorner(self, Qt.Corner) """
        pass

    def setRowMinimumHeight(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ setRowMinimumHeight(self, int, int) """
        pass

    def setRowStretch(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ setRowStretch(self, int, int) """
        pass

    def setSpacing(self, p_int): # real signature unknown; restored from __doc__
        """ setSpacing(self, int) """
        pass

    def setVerticalSpacing(self, p_int): # real signature unknown; restored from __doc__
        """ setVerticalSpacing(self, int) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def spacing(self): # real signature unknown; restored from __doc__
        """ spacing(self) -> int """
        return 0

    def takeAt(self, p_int): # real signature unknown; restored from __doc__
        """ takeAt(self, int) -> QLayoutItem """
        return QLayoutItem

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def verticalSpacing(self): # real signature unknown; restored from __doc__
        """ verticalSpacing(self) -> int """
        return 0

    def widgetEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, QWidget=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass


