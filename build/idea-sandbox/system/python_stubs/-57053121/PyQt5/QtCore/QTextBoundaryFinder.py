# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QTextBoundaryFinder(__sip.simplewrapper):
    """
    QTextBoundaryFinder()
    QTextBoundaryFinder(QTextBoundaryFinder)
    QTextBoundaryFinder(QTextBoundaryFinder.BoundaryType, str)
    """
    def boundaryReasons(self): # real signature unknown; restored from __doc__
        """ boundaryReasons(self) -> QTextBoundaryFinder.BoundaryReasons """
        pass

    def isAtBoundary(self): # real signature unknown; restored from __doc__
        """ isAtBoundary(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def position(self): # real signature unknown; restored from __doc__
        """ position(self) -> int """
        return 0

    def setPosition(self, p_int): # real signature unknown; restored from __doc__
        """ setPosition(self, int) """
        pass

    def string(self): # real signature unknown; restored from __doc__
        """ string(self) -> str """
        return ""

    def toEnd(self): # real signature unknown; restored from __doc__
        """ toEnd(self) """
        pass

    def toNextBoundary(self): # real signature unknown; restored from __doc__
        """ toNextBoundary(self) -> int """
        return 0

    def toPreviousBoundary(self): # real signature unknown; restored from __doc__
        """ toPreviousBoundary(self) -> int """
        return 0

    def toStart(self): # real signature unknown; restored from __doc__
        """ toStart(self) """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QTextBoundaryFinder.BoundaryType """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    BreakOpportunity = 31
    EndOfItem = 64
    Grapheme = 0
    Line = 3
    MandatoryBreak = 128
    NotAtBoundary = 0
    Sentence = 2
    SoftHyphen = 256
    StartOfItem = 32
    Word = 1


