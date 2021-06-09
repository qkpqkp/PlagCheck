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

class QGraphicsGridLayout(QGraphicsLayout):
    """ QGraphicsGridLayout(parent: QGraphicsLayoutItem = None) """
    def addChildLayoutItem(self, *args, **kwargs): # real signature unknown
        pass

    def addItem(self, QGraphicsLayoutItem, p_int, p_int_1, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addItem(self, QGraphicsLayoutItem, int, int, int, int, alignment: Union[Qt.Alignment, Qt.AlignmentFlag] = Qt.Alignment())
        addItem(self, QGraphicsLayoutItem, int, int, alignment: Union[Qt.Alignment, Qt.AlignmentFlag] = Qt.Alignment())
        """
        pass

    def alignment(self, QGraphicsLayoutItem): # real signature unknown; restored from __doc__
        """ alignment(self, QGraphicsLayoutItem) -> Qt.Alignment """
        pass

    def columnAlignment(self, p_int): # real signature unknown; restored from __doc__
        """ columnAlignment(self, int) -> Qt.Alignment """
        pass

    def columnCount(self): # real signature unknown; restored from __doc__
        """ columnCount(self) -> int """
        return 0

    def columnMaximumWidth(self, p_int): # real signature unknown; restored from __doc__
        """ columnMaximumWidth(self, int) -> float """
        return 0.0

    def columnMinimumWidth(self, p_int): # real signature unknown; restored from __doc__
        """ columnMinimumWidth(self, int) -> float """
        return 0.0

    def columnPreferredWidth(self, p_int): # real signature unknown; restored from __doc__
        """ columnPreferredWidth(self, int) -> float """
        return 0.0

    def columnSpacing(self, p_int): # real signature unknown; restored from __doc__
        """ columnSpacing(self, int) -> float """
        return 0.0

    def columnStretchFactor(self, p_int): # real signature unknown; restored from __doc__
        """ columnStretchFactor(self, int) -> int """
        return 0

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def horizontalSpacing(self): # real signature unknown; restored from __doc__
        """ horizontalSpacing(self) -> float """
        return 0.0

    def invalidate(self): # real signature unknown; restored from __doc__
        """ invalidate(self) """
        pass

    def itemAt(self, p_int, p_int_1=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        itemAt(self, int, int) -> QGraphicsLayoutItem
        itemAt(self, int) -> QGraphicsLayoutItem
        """
        return QGraphicsLayoutItem

    def removeAt(self, p_int): # real signature unknown; restored from __doc__
        """ removeAt(self, int) """
        pass

    def removeItem(self, QGraphicsLayoutItem): # real signature unknown; restored from __doc__
        """ removeItem(self, QGraphicsLayoutItem) """
        pass

    def rowAlignment(self, p_int): # real signature unknown; restored from __doc__
        """ rowAlignment(self, int) -> Qt.Alignment """
        pass

    def rowCount(self): # real signature unknown; restored from __doc__
        """ rowCount(self) -> int """
        return 0

    def rowMaximumHeight(self, p_int): # real signature unknown; restored from __doc__
        """ rowMaximumHeight(self, int) -> float """
        return 0.0

    def rowMinimumHeight(self, p_int): # real signature unknown; restored from __doc__
        """ rowMinimumHeight(self, int) -> float """
        return 0.0

    def rowPreferredHeight(self, p_int): # real signature unknown; restored from __doc__
        """ rowPreferredHeight(self, int) -> float """
        return 0.0

    def rowSpacing(self, p_int): # real signature unknown; restored from __doc__
        """ rowSpacing(self, int) -> float """
        return 0.0

    def rowStretchFactor(self, p_int): # real signature unknown; restored from __doc__
        """ rowStretchFactor(self, int) -> int """
        return 0

    def setAlignment(self, QGraphicsLayoutItem, Union, Qt_Alignment=None, Qt_AlignmentFlag=None): # real signature unknown; restored from __doc__
        """ setAlignment(self, QGraphicsLayoutItem, Union[Qt.Alignment, Qt.AlignmentFlag]) """
        pass

    def setColumnAlignment(self, p_int, Union, Qt_Alignment=None, Qt_AlignmentFlag=None): # real signature unknown; restored from __doc__
        """ setColumnAlignment(self, int, Union[Qt.Alignment, Qt.AlignmentFlag]) """
        pass

    def setColumnFixedWidth(self, p_int, p_float): # real signature unknown; restored from __doc__
        """ setColumnFixedWidth(self, int, float) """
        pass

    def setColumnMaximumWidth(self, p_int, p_float): # real signature unknown; restored from __doc__
        """ setColumnMaximumWidth(self, int, float) """
        pass

    def setColumnMinimumWidth(self, p_int, p_float): # real signature unknown; restored from __doc__
        """ setColumnMinimumWidth(self, int, float) """
        pass

    def setColumnPreferredWidth(self, p_int, p_float): # real signature unknown; restored from __doc__
        """ setColumnPreferredWidth(self, int, float) """
        pass

    def setColumnSpacing(self, p_int, p_float): # real signature unknown; restored from __doc__
        """ setColumnSpacing(self, int, float) """
        pass

    def setColumnStretchFactor(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ setColumnStretchFactor(self, int, int) """
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

    def setRowAlignment(self, p_int, Union, Qt_Alignment=None, Qt_AlignmentFlag=None): # real signature unknown; restored from __doc__
        """ setRowAlignment(self, int, Union[Qt.Alignment, Qt.AlignmentFlag]) """
        pass

    def setRowFixedHeight(self, p_int, p_float): # real signature unknown; restored from __doc__
        """ setRowFixedHeight(self, int, float) """
        pass

    def setRowMaximumHeight(self, p_int, p_float): # real signature unknown; restored from __doc__
        """ setRowMaximumHeight(self, int, float) """
        pass

    def setRowMinimumHeight(self, p_int, p_float): # real signature unknown; restored from __doc__
        """ setRowMinimumHeight(self, int, float) """
        pass

    def setRowPreferredHeight(self, p_int, p_float): # real signature unknown; restored from __doc__
        """ setRowPreferredHeight(self, int, float) """
        pass

    def setRowSpacing(self, p_int, p_float): # real signature unknown; restored from __doc__
        """ setRowSpacing(self, int, float) """
        pass

    def setRowStretchFactor(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ setRowStretchFactor(self, int, int) """
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


