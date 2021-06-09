# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QIconEngine(__sip.wrapper):
    """
    QIconEngine()
    QIconEngine(QIconEngine)
    """
    def actualSize(self, QSize, QIcon_Mode, QIcon_State): # real signature unknown; restored from __doc__
        """ actualSize(self, QSize, QIcon.Mode, QIcon.State) -> QSize """
        pass

    def addFile(self, p_str, QSize, QIcon_Mode, QIcon_State): # real signature unknown; restored from __doc__
        """ addFile(self, str, QSize, QIcon.Mode, QIcon.State) """
        pass

    def addPixmap(self, QPixmap, QIcon_Mode, QIcon_State): # real signature unknown; restored from __doc__
        """ addPixmap(self, QPixmap, QIcon.Mode, QIcon.State) """
        pass

    def availableSizes(self, mode=None, state=None): # real signature unknown; restored from __doc__
        """ availableSizes(self, mode: QIcon.Mode = QIcon.Normal, state: QIcon.State = QIcon.Off) -> List[QSize] """
        return []

    def clone(self): # real signature unknown; restored from __doc__
        """ clone(self) -> QIconEngine """
        return QIconEngine

    def iconName(self): # real signature unknown; restored from __doc__
        """ iconName(self) -> str """
        return ""

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def key(self): # real signature unknown; restored from __doc__
        """ key(self) -> str """
        return ""

    def paint(self, QPainter, QRect, QIcon_Mode, QIcon_State): # real signature unknown; restored from __doc__
        """ paint(self, QPainter, QRect, QIcon.Mode, QIcon.State) """
        pass

    def pixmap(self, QSize, QIcon_Mode, QIcon_State): # real signature unknown; restored from __doc__
        """ pixmap(self, QSize, QIcon.Mode, QIcon.State) -> QPixmap """
        return QPixmap

    def read(self, QDataStream): # real signature unknown; restored from __doc__
        """ read(self, QDataStream) -> bool """
        return False

    def scaledPixmap(self, QSize, QIcon_Mode, QIcon_State, p_float): # real signature unknown; restored from __doc__
        """ scaledPixmap(self, QSize, QIcon.Mode, QIcon.State, float) -> QPixmap """
        return QPixmap

    def write(self, QDataStream): # real signature unknown; restored from __doc__
        """ write(self, QDataStream) -> bool """
        return False

    def __init__(self, QIconEngine=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AvailableSizesHook = 1
    IconNameHook = 2
    IsNullHook = 3
    ScaledPixmapHook = 4


