# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QTextFormat import QTextFormat

class QTextBlockFormat(QTextFormat):
    """
    QTextBlockFormat()
    QTextBlockFormat(QTextBlockFormat)
    """
    def alignment(self): # real signature unknown; restored from __doc__
        """ alignment(self) -> Qt.Alignment """
        pass

    def bottomMargin(self): # real signature unknown; restored from __doc__
        """ bottomMargin(self) -> float """
        return 0.0

    def headingLevel(self): # real signature unknown; restored from __doc__
        """ headingLevel(self) -> int """
        return 0

    def indent(self): # real signature unknown; restored from __doc__
        """ indent(self) -> int """
        return 0

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def leftMargin(self): # real signature unknown; restored from __doc__
        """ leftMargin(self) -> float """
        return 0.0

    def lineHeight(self, p_float=None, scaling=1): # real signature unknown; restored from __doc__ with multiple overloads
        """
        lineHeight(self) -> float
        lineHeight(self, float, scaling: float = 1) -> float
        """
        return 0.0

    def lineHeightType(self): # real signature unknown; restored from __doc__
        """ lineHeightType(self) -> int """
        return 0

    def nonBreakableLines(self): # real signature unknown; restored from __doc__
        """ nonBreakableLines(self) -> bool """
        return False

    def pageBreakPolicy(self): # real signature unknown; restored from __doc__
        """ pageBreakPolicy(self) -> QTextFormat.PageBreakFlags """
        pass

    def rightMargin(self): # real signature unknown; restored from __doc__
        """ rightMargin(self) -> float """
        return 0.0

    def setAlignment(self, Union, Qt_Alignment=None, Qt_AlignmentFlag=None): # real signature unknown; restored from __doc__
        """ setAlignment(self, Union[Qt.Alignment, Qt.AlignmentFlag]) """
        pass

    def setBottomMargin(self, p_float): # real signature unknown; restored from __doc__
        """ setBottomMargin(self, float) """
        pass

    def setHeadingLevel(self, p_int): # real signature unknown; restored from __doc__
        """ setHeadingLevel(self, int) """
        pass

    def setIndent(self, p_int): # real signature unknown; restored from __doc__
        """ setIndent(self, int) """
        pass

    def setLeftMargin(self, p_float): # real signature unknown; restored from __doc__
        """ setLeftMargin(self, float) """
        pass

    def setLineHeight(self, p_float, p_int): # real signature unknown; restored from __doc__
        """ setLineHeight(self, float, int) """
        pass

    def setNonBreakableLines(self, bool): # real signature unknown; restored from __doc__
        """ setNonBreakableLines(self, bool) """
        pass

    def setPageBreakPolicy(self, Union, QTextFormat_PageBreakFlags=None, QTextFormat_PageBreakFlag=None): # real signature unknown; restored from __doc__
        """ setPageBreakPolicy(self, Union[QTextFormat.PageBreakFlags, QTextFormat.PageBreakFlag]) """
        pass

    def setRightMargin(self, p_float): # real signature unknown; restored from __doc__
        """ setRightMargin(self, float) """
        pass

    def setTabPositions(self, Iterable, QTextOption_Tab=None): # real signature unknown; restored from __doc__
        """ setTabPositions(self, Iterable[QTextOption.Tab]) """
        pass

    def setTextIndent(self, p_float): # real signature unknown; restored from __doc__
        """ setTextIndent(self, float) """
        pass

    def setTopMargin(self, p_float): # real signature unknown; restored from __doc__
        """ setTopMargin(self, float) """
        pass

    def tabPositions(self): # real signature unknown; restored from __doc__
        """ tabPositions(self) -> List[QTextOption.Tab] """
        return []

    def textIndent(self): # real signature unknown; restored from __doc__
        """ textIndent(self) -> float """
        return 0.0

    def topMargin(self): # real signature unknown; restored from __doc__
        """ topMargin(self) -> float """
        return 0.0

    def __init__(self, QTextBlockFormat=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    FixedHeight = 2
    LineDistanceHeight = 4
    MinimumHeight = 3
    ProportionalHeight = 1
    SingleHeight = 0


