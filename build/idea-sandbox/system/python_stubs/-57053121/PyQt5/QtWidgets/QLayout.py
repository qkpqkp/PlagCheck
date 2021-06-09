# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QLayoutItem import QLayoutItem

class QLayout(__PyQt5_QtCore.QObject, QLayoutItem):
    """
    QLayout(QWidget)
    QLayout()
    """
    def activate(self): # real signature unknown; restored from __doc__
        """ activate(self) -> bool """
        return False

    def addChildLayout(self, QLayout): # real signature unknown; restored from __doc__
        """ addChildLayout(self, QLayout) """
        pass

    def addChildWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ addChildWidget(self, QWidget) """
        pass

    def addItem(self, QLayoutItem): # real signature unknown; restored from __doc__
        """ addItem(self, QLayoutItem) """
        pass

    def addWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ addWidget(self, QWidget) """
        pass

    def alignmentRect(self, QRect): # real signature unknown; restored from __doc__
        """ alignmentRect(self, QRect) -> QRect """
        pass

    def childEvent(self, QChildEvent): # real signature unknown; restored from __doc__
        """ childEvent(self, QChildEvent) """
        pass

    def closestAcceptableSize(self, QWidget, QSize): # real signature unknown; restored from __doc__
        """ closestAcceptableSize(QWidget, QSize) -> QSize """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contentsMargins(self): # real signature unknown; restored from __doc__
        """ contentsMargins(self) -> QMargins """
        pass

    def contentsRect(self): # real signature unknown; restored from __doc__
        """ contentsRect(self) -> QRect """
        pass

    def controlTypes(self): # real signature unknown; restored from __doc__
        """ controlTypes(self) -> QSizePolicy.ControlTypes """
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

    def geometry(self): # real signature unknown; restored from __doc__
        """ geometry(self) -> QRect """
        pass

    def getContentsMargins(self): # real signature unknown; restored from __doc__
        """ getContentsMargins(self) -> Tuple[int, int, int, int] """
        pass

    def indexOf(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        indexOf(self, QWidget) -> int
        indexOf(self, QLayoutItem) -> int
        """
        return 0

    def invalidate(self): # real signature unknown; restored from __doc__
        """ invalidate(self) """
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isEnabled(self): # real signature unknown; restored from __doc__
        """ isEnabled(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def itemAt(self, p_int): # real signature unknown; restored from __doc__
        """ itemAt(self, int) -> QLayoutItem """
        return QLayoutItem

    def layout(self): # real signature unknown; restored from __doc__
        """ layout(self) -> QLayout """
        return QLayout

    def maximumSize(self): # real signature unknown; restored from __doc__
        """ maximumSize(self) -> QSize """
        pass

    def menuBar(self): # real signature unknown; restored from __doc__
        """ menuBar(self) -> QWidget """
        return QWidget

    def minimumSize(self): # real signature unknown; restored from __doc__
        """ minimumSize(self) -> QSize """
        pass

    def parentWidget(self): # real signature unknown; restored from __doc__
        """ parentWidget(self) -> QWidget """
        return QWidget

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeItem(self, QLayoutItem): # real signature unknown; restored from __doc__
        """ removeItem(self, QLayoutItem) """
        pass

    def removeWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ removeWidget(self, QWidget) """
        pass

    def replaceWidget(self, QWidget, QWidget_1, options, Qt_FindChildOptions=None, Qt_FindChildOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ replaceWidget(self, QWidget, QWidget, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QLayoutItem """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAlignment(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setAlignment(self, QWidget, Union[Qt.Alignment, Qt.AlignmentFlag]) -> bool
        setAlignment(self, QLayout, Union[Qt.Alignment, Qt.AlignmentFlag]) -> bool
        setAlignment(self, Union[Qt.Alignment, Qt.AlignmentFlag])
        """
        return False

    def setContentsMargins(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setContentsMargins(self, int, int, int, int)
        setContentsMargins(self, QMargins)
        """
        pass

    def setEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setEnabled(self, bool) """
        pass

    def setGeometry(self, QRect): # real signature unknown; restored from __doc__
        """ setGeometry(self, QRect) """
        pass

    def setMenuBar(self, QWidget): # real signature unknown; restored from __doc__
        """ setMenuBar(self, QWidget) """
        pass

    def setSizeConstraint(self, QLayout_SizeConstraint): # real signature unknown; restored from __doc__
        """ setSizeConstraint(self, QLayout.SizeConstraint) """
        pass

    def setSpacing(self, p_int): # real signature unknown; restored from __doc__
        """ setSpacing(self, int) """
        pass

    def sizeConstraint(self): # real signature unknown; restored from __doc__
        """ sizeConstraint(self) -> QLayout.SizeConstraint """
        pass

    def spacing(self): # real signature unknown; restored from __doc__
        """ spacing(self) -> int """
        return 0

    def takeAt(self, p_int): # real signature unknown; restored from __doc__
        """ takeAt(self, int) -> QLayoutItem """
        return QLayoutItem

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def totalHeightForWidth(self, p_int): # real signature unknown; restored from __doc__
        """ totalHeightForWidth(self, int) -> int """
        return 0

    def totalMaximumSize(self): # real signature unknown; restored from __doc__
        """ totalMaximumSize(self) -> QSize """
        pass

    def totalMinimumSize(self): # real signature unknown; restored from __doc__
        """ totalMinimumSize(self) -> QSize """
        pass

    def totalSizeHint(self): # real signature unknown; restored from __doc__
        """ totalSizeHint(self) -> QSize """
        pass

    def update(self): # real signature unknown; restored from __doc__
        """ update(self) """
        pass

    def widgetEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ widgetEvent(self, QEvent) """
        pass

    def __init__(self, QWidget=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    SetDefaultConstraint = 0
    SetFixedSize = 3
    SetMaximumSize = 4
    SetMinAndMaxSize = 5
    SetMinimumSize = 2
    SetNoConstraint = 1


