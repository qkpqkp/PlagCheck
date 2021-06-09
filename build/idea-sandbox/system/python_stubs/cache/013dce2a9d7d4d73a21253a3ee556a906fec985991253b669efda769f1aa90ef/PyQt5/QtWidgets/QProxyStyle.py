# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QCommonStyle import QCommonStyle

class QProxyStyle(QCommonStyle):
    """
    QProxyStyle(style: QStyle = None)
    QProxyStyle(str)
    """
    def baseStyle(self): # real signature unknown; restored from __doc__
        """ baseStyle(self) -> QStyle """
        return QStyle

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def drawComplexControl(self, QStyle_ComplexControl, QStyleOptionComplex, QPainter, widget=None): # real signature unknown; restored from __doc__
        """ drawComplexControl(self, QStyle.ComplexControl, QStyleOptionComplex, QPainter, widget: QWidget = None) """
        pass

    def drawControl(self, QStyle_ControlElement, QStyleOption, QPainter, widget=None): # real signature unknown; restored from __doc__
        """ drawControl(self, QStyle.ControlElement, QStyleOption, QPainter, widget: QWidget = None) """
        pass

    def drawItemPixmap(self, QPainter, QRect, p_int, QPixmap): # real signature unknown; restored from __doc__
        """ drawItemPixmap(self, QPainter, QRect, int, QPixmap) """
        pass

    def drawItemText(self, QPainter, QRect, p_int, QPalette, bool, p_str, textRole=None): # real signature unknown; restored from __doc__
        """ drawItemText(self, QPainter, QRect, int, QPalette, bool, str, textRole: QPalette.ColorRole = QPalette.NoRole) """
        pass

    def drawPrimitive(self, QStyle_PrimitiveElement, QStyleOption, QPainter, widget=None): # real signature unknown; restored from __doc__
        """ drawPrimitive(self, QStyle.PrimitiveElement, QStyleOption, QPainter, widget: QWidget = None) """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def generatedIconPixmap(self, QIcon_Mode, QPixmap, QStyleOption): # real signature unknown; restored from __doc__
        """ generatedIconPixmap(self, QIcon.Mode, QPixmap, QStyleOption) -> QPixmap """
        pass

    def hitTestComplexControl(self, QStyle_ComplexControl, QStyleOptionComplex, QPoint, widget=None): # real signature unknown; restored from __doc__
        """ hitTestComplexControl(self, QStyle.ComplexControl, QStyleOptionComplex, QPoint, widget: QWidget = None) -> QStyle.SubControl """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def itemPixmapRect(self, QRect, p_int, QPixmap): # real signature unknown; restored from __doc__
        """ itemPixmapRect(self, QRect, int, QPixmap) -> QRect """
        pass

    def itemTextRect(self, QFontMetrics, QRect, p_int, bool, p_str): # real signature unknown; restored from __doc__
        """ itemTextRect(self, QFontMetrics, QRect, int, bool, str) -> QRect """
        pass

    def layoutSpacing(self, QSizePolicy_ControlType, QSizePolicy_ControlType_1, Qt_Orientation, option=None, widget=None): # real signature unknown; restored from __doc__
        """ layoutSpacing(self, QSizePolicy.ControlType, QSizePolicy.ControlType, Qt.Orientation, option: QStyleOption = None, widget: QWidget = None) -> int """
        return 0

    def pixelMetric(self, QStyle_PixelMetric, option=None, widget=None): # real signature unknown; restored from __doc__
        """ pixelMetric(self, QStyle.PixelMetric, option: QStyleOption = None, widget: QWidget = None) -> int """
        return 0

    def polish(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        polish(self, QWidget)
        polish(self, QPalette) -> QPalette
        polish(self, QApplication)
        """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setBaseStyle(self, QStyle): # real signature unknown; restored from __doc__
        """ setBaseStyle(self, QStyle) """
        pass

    def sizeFromContents(self, QStyle_ContentsType, QStyleOption, QSize, QWidget): # real signature unknown; restored from __doc__
        """ sizeFromContents(self, QStyle.ContentsType, QStyleOption, QSize, QWidget) -> QSize """
        pass

    def standardIcon(self, QStyle_StandardPixmap, option=None, widget=None): # real signature unknown; restored from __doc__
        """ standardIcon(self, QStyle.StandardPixmap, option: QStyleOption = None, widget: QWidget = None) -> QIcon """
        pass

    def standardPalette(self): # real signature unknown; restored from __doc__
        """ standardPalette(self) -> QPalette """
        pass

    def standardPixmap(self, QStyle_StandardPixmap, QStyleOption, widget=None): # real signature unknown; restored from __doc__
        """ standardPixmap(self, QStyle.StandardPixmap, QStyleOption, widget: QWidget = None) -> QPixmap """
        pass

    def styleHint(self, QStyle_StyleHint, option=None, widget=None, returnData=None): # real signature unknown; restored from __doc__
        """ styleHint(self, QStyle.StyleHint, option: QStyleOption = None, widget: QWidget = None, returnData: QStyleHintReturn = None) -> int """
        return 0

    def subControlRect(self, QStyle_ComplexControl, QStyleOptionComplex, QStyle_SubControl, QWidget): # real signature unknown; restored from __doc__
        """ subControlRect(self, QStyle.ComplexControl, QStyleOptionComplex, QStyle.SubControl, QWidget) -> QRect """
        pass

    def subElementRect(self, QStyle_SubElement, QStyleOption, QWidget): # real signature unknown; restored from __doc__
        """ subElementRect(self, QStyle.SubElement, QStyleOption, QWidget) -> QRect """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def unpolish(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        unpolish(self, QWidget)
        unpolish(self, QApplication)
        """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


