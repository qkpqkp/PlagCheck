# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QStyle import QStyle

class QCommonStyle(QStyle):
    """ QCommonStyle() """
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

    def drawPrimitive(self, QStyle_PrimitiveElement, QStyleOption, QPainter, widget=None): # real signature unknown; restored from __doc__
        """ drawPrimitive(self, QStyle.PrimitiveElement, QStyleOption, QPainter, widget: QWidget = None) """
        pass

    def generatedIconPixmap(self, QIcon_Mode, QPixmap, QStyleOption): # real signature unknown; restored from __doc__
        """ generatedIconPixmap(self, QIcon.Mode, QPixmap, QStyleOption) -> QPixmap """
        pass

    def hitTestComplexControl(self, QStyle_ComplexControl, QStyleOptionComplex, QPoint, widget=None): # real signature unknown; restored from __doc__
        """ hitTestComplexControl(self, QStyle.ComplexControl, QStyleOptionComplex, QPoint, widget: QWidget = None) -> QStyle.SubControl """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
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
        polish(self, QApplication)
        polish(self, QPalette) -> QPalette
        """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def sizeFromContents(self, QStyle_ContentsType, QStyleOption, QSize, widget=None): # real signature unknown; restored from __doc__
        """ sizeFromContents(self, QStyle.ContentsType, QStyleOption, QSize, widget: QWidget = None) -> QSize """
        pass

    def standardIcon(self, QStyle_StandardPixmap, option=None, widget=None): # real signature unknown; restored from __doc__
        """ standardIcon(self, QStyle.StandardPixmap, option: QStyleOption = None, widget: QWidget = None) -> QIcon """
        pass

    def standardPixmap(self, QStyle_StandardPixmap, option=None, widget=None): # real signature unknown; restored from __doc__
        """ standardPixmap(self, QStyle.StandardPixmap, option: QStyleOption = None, widget: QWidget = None) -> QPixmap """
        pass

    def styleHint(self, QStyle_StyleHint, option=None, widget=None, returnData=None): # real signature unknown; restored from __doc__
        """ styleHint(self, QStyle.StyleHint, option: QStyleOption = None, widget: QWidget = None, returnData: QStyleHintReturn = None) -> int """
        return 0

    def subControlRect(self, QStyle_ComplexControl, QStyleOptionComplex, QStyle_SubControl, widget=None): # real signature unknown; restored from __doc__
        """ subControlRect(self, QStyle.ComplexControl, QStyleOptionComplex, QStyle.SubControl, widget: QWidget = None) -> QRect """
        pass

    def subElementRect(self, QStyle_SubElement, QStyleOption, widget=None): # real signature unknown; restored from __doc__
        """ subElementRect(self, QStyle.SubElement, QStyleOption, widget: QWidget = None) -> QRect """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def unpolish(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        unpolish(self, QWidget)
        unpolish(self, QApplication)
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass


