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

class QGraphicsAnchorLayout(QGraphicsLayout):
    """ QGraphicsAnchorLayout(parent: QGraphicsLayoutItem = None) """
    def addAnchor(self, QGraphicsLayoutItem, Qt_AnchorPoint, QGraphicsLayoutItem_1, Qt_AnchorPoint_1): # real signature unknown; restored from __doc__
        """ addAnchor(self, QGraphicsLayoutItem, Qt.AnchorPoint, QGraphicsLayoutItem, Qt.AnchorPoint) -> QGraphicsAnchor """
        return QGraphicsAnchor

    def addAnchors(self, QGraphicsLayoutItem, QGraphicsLayoutItem_1, orientations, Qt_Orientations=None, Qt_Orientation=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ addAnchors(self, QGraphicsLayoutItem, QGraphicsLayoutItem, orientations: Union[Qt.Orientations, Qt.Orientation] = Qt.Horizontal|Qt.Vertical) """
        pass

    def addChildLayoutItem(self, *args, **kwargs): # real signature unknown
        pass

    def addCornerAnchors(self, QGraphicsLayoutItem, Qt_Corner, QGraphicsLayoutItem_1, Qt_Corner_1): # real signature unknown; restored from __doc__
        """ addCornerAnchors(self, QGraphicsLayoutItem, Qt.Corner, QGraphicsLayoutItem, Qt.Corner) """
        pass

    def anchor(self, QGraphicsLayoutItem, Qt_AnchorPoint, QGraphicsLayoutItem_1, Qt_AnchorPoint_1): # real signature unknown; restored from __doc__
        """ anchor(self, QGraphicsLayoutItem, Qt.AnchorPoint, QGraphicsLayoutItem, Qt.AnchorPoint) -> QGraphicsAnchor """
        return QGraphicsAnchor

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def horizontalSpacing(self): # real signature unknown; restored from __doc__
        """ horizontalSpacing(self) -> float """
        return 0.0

    def invalidate(self): # real signature unknown; restored from __doc__
        """ invalidate(self) """
        pass

    def itemAt(self, p_int): # real signature unknown; restored from __doc__
        """ itemAt(self, int) -> QGraphicsLayoutItem """
        return QGraphicsLayoutItem

    def removeAt(self, p_int): # real signature unknown; restored from __doc__
        """ removeAt(self, int) """
        pass

    def setGeometry(self, QRectF): # real signature unknown; restored from __doc__
        """ setGeometry(self, QRectF) """
        pass

    def setGraphicsItem(self, *args, **kwargs): # real signature unknown
        pass

    def setHorizontalSpacing(self, p_float): # real signature unknown; restored from __doc__
        """ setHorizontalSpacing(self, float) """
        pass

    def setOwnedByLayout(self, *args, **kwargs): # real signature unknown
        pass

    def setSpacing(self, p_float): # real signature unknown; restored from __doc__
        """ setSpacing(self, float) """
        pass

    def setVerticalSpacing(self, p_float): # real signature unknown; restored from __doc__
        """ setVerticalSpacing(self, float) """
        pass

    def sizeHint(self, Qt_SizeHint, constraint=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ sizeHint(self, Qt.SizeHint, constraint: QSizeF = QSizeF()) -> QSizeF """
        pass

    def verticalSpacing(self): # real signature unknown; restored from __doc__
        """ verticalSpacing(self) -> float """
        return 0.0

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


