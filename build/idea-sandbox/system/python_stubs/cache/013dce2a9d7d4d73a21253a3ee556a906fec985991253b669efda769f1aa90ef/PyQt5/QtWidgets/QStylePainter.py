# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QStylePainter(__PyQt5_QtGui.QPainter):
    """
    QStylePainter()
    QStylePainter(QWidget)
    QStylePainter(QPaintDevice, QWidget)
    """
    def begin(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        begin(self, QWidget) -> bool
        begin(self, QPaintDevice, QWidget) -> bool
        """
        return False

    def drawComplexControl(self, QStyle_ComplexControl, QStyleOptionComplex): # real signature unknown; restored from __doc__
        """ drawComplexControl(self, QStyle.ComplexControl, QStyleOptionComplex) """
        pass

    def drawControl(self, QStyle_ControlElement, QStyleOption): # real signature unknown; restored from __doc__
        """ drawControl(self, QStyle.ControlElement, QStyleOption) """
        pass

    def drawItemPixmap(self, QRect, p_int, QPixmap): # real signature unknown; restored from __doc__
        """ drawItemPixmap(self, QRect, int, QPixmap) """
        pass

    def drawItemText(self, QRect, p_int, QPalette, bool, p_str, textRole=None): # real signature unknown; restored from __doc__
        """ drawItemText(self, QRect, int, QPalette, bool, str, textRole: QPalette.ColorRole = QPalette.NoRole) """
        pass

    def drawPrimitive(self, QStyle_PrimitiveElement, QStyleOption): # real signature unknown; restored from __doc__
        """ drawPrimitive(self, QStyle.PrimitiveElement, QStyleOption) """
        pass

    def style(self): # real signature unknown; restored from __doc__
        """ style(self) -> QStyle """
        return QStyle

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


