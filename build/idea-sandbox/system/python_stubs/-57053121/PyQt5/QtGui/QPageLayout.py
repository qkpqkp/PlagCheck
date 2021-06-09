# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QPageLayout(__sip.simplewrapper):
    """
    QPageLayout()
    QPageLayout(QPageSize, QPageLayout.Orientation, QMarginsF, units: QPageLayout.Unit = QPageLayout.Point, minMargins: QMarginsF = QMarginsF(0,0,0,0))
    QPageLayout(QPageLayout)
    """
    def fullRect(self, QPageLayout_Unit=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        fullRect(self) -> QRectF
        fullRect(self, QPageLayout.Unit) -> QRectF
        """
        pass

    def fullRectPixels(self, p_int): # real signature unknown; restored from __doc__
        """ fullRectPixels(self, int) -> QRect """
        pass

    def fullRectPoints(self): # real signature unknown; restored from __doc__
        """ fullRectPoints(self) -> QRect """
        pass

    def isEquivalentTo(self, QPageLayout): # real signature unknown; restored from __doc__
        """ isEquivalentTo(self, QPageLayout) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def margins(self, QPageLayout_Unit=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        margins(self) -> QMarginsF
        margins(self, QPageLayout.Unit) -> QMarginsF
        """
        pass

    def marginsPixels(self, p_int): # real signature unknown; restored from __doc__
        """ marginsPixels(self, int) -> QMargins """
        pass

    def marginsPoints(self): # real signature unknown; restored from __doc__
        """ marginsPoints(self) -> QMargins """
        pass

    def maximumMargins(self): # real signature unknown; restored from __doc__
        """ maximumMargins(self) -> QMarginsF """
        pass

    def minimumMargins(self): # real signature unknown; restored from __doc__
        """ minimumMargins(self) -> QMarginsF """
        pass

    def mode(self): # real signature unknown; restored from __doc__
        """ mode(self) -> QPageLayout.Mode """
        pass

    def orientation(self): # real signature unknown; restored from __doc__
        """ orientation(self) -> QPageLayout.Orientation """
        pass

    def pageSize(self): # real signature unknown; restored from __doc__
        """ pageSize(self) -> QPageSize """
        return QPageSize

    def paintRect(self, QPageLayout_Unit=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        paintRect(self) -> QRectF
        paintRect(self, QPageLayout.Unit) -> QRectF
        """
        pass

    def paintRectPixels(self, p_int): # real signature unknown; restored from __doc__
        """ paintRectPixels(self, int) -> QRect """
        pass

    def paintRectPoints(self): # real signature unknown; restored from __doc__
        """ paintRectPoints(self) -> QRect """
        pass

    def setBottomMargin(self, p_float): # real signature unknown; restored from __doc__
        """ setBottomMargin(self, float) -> bool """
        return False

    def setLeftMargin(self, p_float): # real signature unknown; restored from __doc__
        """ setLeftMargin(self, float) -> bool """
        return False

    def setMargins(self, QMarginsF): # real signature unknown; restored from __doc__
        """ setMargins(self, QMarginsF) -> bool """
        return False

    def setMinimumMargins(self, QMarginsF): # real signature unknown; restored from __doc__
        """ setMinimumMargins(self, QMarginsF) """
        pass

    def setMode(self, QPageLayout_Mode): # real signature unknown; restored from __doc__
        """ setMode(self, QPageLayout.Mode) """
        pass

    def setOrientation(self, QPageLayout_Orientation): # real signature unknown; restored from __doc__
        """ setOrientation(self, QPageLayout.Orientation) """
        pass

    def setPageSize(self, QPageSize, minMargins=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setPageSize(self, QPageSize, minMargins: QMarginsF = QMarginsF(0,0,0,0)) """
        pass

    def setRightMargin(self, p_float): # real signature unknown; restored from __doc__
        """ setRightMargin(self, float) -> bool """
        return False

    def setTopMargin(self, p_float): # real signature unknown; restored from __doc__
        """ setTopMargin(self, float) -> bool """
        return False

    def setUnits(self, QPageLayout_Unit): # real signature unknown; restored from __doc__
        """ setUnits(self, QPageLayout.Unit) """
        pass

    def swap(self, QPageLayout): # real signature unknown; restored from __doc__
        """ swap(self, QPageLayout) """
        pass

    def units(self): # real signature unknown; restored from __doc__
        """ units(self) -> QPageLayout.Unit """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Cicero = 5
    Didot = 4
    FullPageMode = 1
    Inch = 2
    Landscape = 1
    Millimeter = 0
    Pica = 3
    Point = 1
    Portrait = 0
    StandardMode = 0
    __hash__ = None


