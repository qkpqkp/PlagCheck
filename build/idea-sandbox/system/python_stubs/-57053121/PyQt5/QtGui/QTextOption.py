# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QTextOption(__sip.simplewrapper):
    """
    QTextOption()
    QTextOption(Union[Qt.Alignment, Qt.AlignmentFlag])
    QTextOption(QTextOption)
    """
    def alignment(self): # real signature unknown; restored from __doc__
        """ alignment(self) -> Qt.Alignment """
        pass

    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> QTextOption.Flags """
        pass

    def setAlignment(self, Union, Qt_Alignment=None, Qt_AlignmentFlag=None): # real signature unknown; restored from __doc__
        """ setAlignment(self, Union[Qt.Alignment, Qt.AlignmentFlag]) """
        pass

    def setFlags(self, Union, QTextOption_Flags=None, QTextOption_Flag=None): # real signature unknown; restored from __doc__
        """ setFlags(self, Union[QTextOption.Flags, QTextOption.Flag]) """
        pass

    def setTabArray(self, Iterable, p_float=None): # real signature unknown; restored from __doc__
        """ setTabArray(self, Iterable[float]) """
        pass

    def setTabs(self, Iterable, QTextOption_Tab=None): # real signature unknown; restored from __doc__
        """ setTabs(self, Iterable[QTextOption.Tab]) """
        pass

    def setTabStop(self, p_float): # real signature unknown; restored from __doc__
        """ setTabStop(self, float) """
        pass

    def setTabStopDistance(self, p_float): # real signature unknown; restored from __doc__
        """ setTabStopDistance(self, float) """
        pass

    def setTextDirection(self, Qt_LayoutDirection): # real signature unknown; restored from __doc__
        """ setTextDirection(self, Qt.LayoutDirection) """
        pass

    def setUseDesignMetrics(self, bool): # real signature unknown; restored from __doc__
        """ setUseDesignMetrics(self, bool) """
        pass

    def setWrapMode(self, QTextOption_WrapMode): # real signature unknown; restored from __doc__
        """ setWrapMode(self, QTextOption.WrapMode) """
        pass

    def tabArray(self): # real signature unknown; restored from __doc__
        """ tabArray(self) -> List[float] """
        return []

    def tabs(self): # real signature unknown; restored from __doc__
        """ tabs(self) -> List[QTextOption.Tab] """
        return []

    def tabStop(self): # real signature unknown; restored from __doc__
        """ tabStop(self) -> float """
        return 0.0

    def tabStopDistance(self): # real signature unknown; restored from __doc__
        """ tabStopDistance(self) -> float """
        return 0.0

    def textDirection(self): # real signature unknown; restored from __doc__
        """ textDirection(self) -> Qt.LayoutDirection """
        pass

    def useDesignMetrics(self): # real signature unknown; restored from __doc__
        """ useDesignMetrics(self) -> bool """
        return False

    def wrapMode(self): # real signature unknown; restored from __doc__
        """ wrapMode(self) -> QTextOption.WrapMode """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AddSpaceForLineAndParagraphSeparators = 4
    CenterTab = 2
    DelimiterTab = 3
    IncludeTrailingSpaces = -2147483648
    LeftTab = 0
    ManualWrap = 2
    NoWrap = 0
    RightTab = 1
    ShowDocumentTerminator = 16
    ShowLineAndParagraphSeparators = 2
    ShowTabsAndSpaces = 1
    SuppressColors = 8
    WordWrap = 1
    WrapAnywhere = 3
    WrapAtWordBoundaryOrAnywhere = 4


