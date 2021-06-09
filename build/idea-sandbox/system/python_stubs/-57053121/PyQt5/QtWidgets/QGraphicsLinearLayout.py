# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QGraphicsLayout import QGraphicsLayout

class QGraphicsLinearLayout(QGraphicsLayout):
    """
    QGraphicsLinearLayout(parent: QGraphicsLayoutItem = None)
    QGraphicsLinearLayout(Qt.Orientation, parent: QGraphicsLayoutItem = None)
    """
    def addChildLayoutItem(self, *args, **kwargs): # real signature unknown
        pass

    def addItem(self, QGraphicsLayoutItem): # real signature unknown; restored from __doc__
        """ addItem(self, QGraphicsLayoutItem) """
        pass

    def addStretch(self, stretch=1): # real signature unknown; restored from __doc__
        """ addStretch(self, stretch: int = 1) """
        pass

    def alignment(self, QGraphicsLayoutItem): # real signature unknown; restored from __doc__
        """ alignment(self, QGraphicsLayoutItem) -> Qt.Alignment """
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def insertItem(self, p_int, QGraphicsLayoutItem): # real signature unknown; restored from __doc__
        """ insertItem(self, int, QGraphicsLayoutItem) """
        pass

    def insertStretch(self, p_int, stretch=1): # real signature unknown; restored from __doc__
        """ insertStretch(self, int, stretch: int = 1) """
        pass

    def invalidate(self): # real signature unknown; restored from __doc__
        """ invalidate(self) """
        pass

    def itemAt(self, p_int): # real signature unknown; restored from __doc__
        """ itemAt(self, int) -> QGraphicsLayoutItem """
        return QGraphicsLayoutItem

    def itemSpacing(self, p_int): # real signature unknown; restored from __doc__
        """ itemSpacing(self, int) -> float """
        return 0.0

    def orientation(self): # real signature unknown; restored from __doc__
        """ orientation(self) -> Qt.Orientation """
        pass

    def removeAt(self, p_int): # real signature unknown; restored from __doc__
        """ removeAt(self, int) """
        pass

    def removeItem(self, QGraphicsLayoutItem): # real signature unknown; restored from __doc__
        """ removeItem(self, QGraphicsLayoutItem) """
        pass

    def setAlignment(self, QGraphicsLayoutItem, Union, Qt_Alignment=None, Qt_AlignmentFlag=None): # real signature unknown; restored from __doc__
        """ setAlignment(self, QGraphicsLayoutItem, Union[Qt.Alignment, Qt.AlignmentFlag]) """
        pass

    def setGeometry(self, QRectF): # real signature unknown; restored from __doc__
        """ setGeometry(self, QRectF) """
        pass

    def setGraphicsItem(self, *args, **kwargs): # real signature unknown
        pass

    def setItemSpacing(self, p_int, p_float): # real signature unknown; restored from __doc__
        """ setItemSpacing(self, int, float) """
        pass

    def setOrientation(self, Qt_Orientation): # real signature unknown; restored from __doc__
        """ setOrientation(self, Qt.Orientation) """
        pass

    def setOwnedByLayout(self, *args, **kwargs): # real signature unknown
        pass

    def setSpacing(self, p_float): # real signature unknown; restored from __doc__
        """ setSpacing(self, float) """
        pass

    def setStretchFactor(self, QGraphicsLayoutItem, p_int): # real signature unknown; restored from __doc__
        """ setStretchFactor(self, QGraphicsLayoutItem, int) """
        pass

    def sizeHint(self, Qt_SizeHint, constraint=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ sizeHint(self, Qt.SizeHint, constraint: QSizeF = QSizeF()) -> QSizeF """
        pass

    def spacing(self): # real signature unknown; restored from __doc__
        """ spacing(self) -> float """
        return 0.0

    def stretchFactor(self, QGraphicsLayoutItem): # real signature unknown; restored from __doc__
        """ stretchFactor(self, QGraphicsLayoutItem) -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


