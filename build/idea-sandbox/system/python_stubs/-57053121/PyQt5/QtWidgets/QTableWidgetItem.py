# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QTableWidgetItem(__sip.wrapper):
    """
    QTableWidgetItem(type: int = QTableWidgetItem.Type)
    QTableWidgetItem(str, type: int = QTableWidgetItem.Type)
    QTableWidgetItem(QIcon, str, type: int = QTableWidgetItem.Type)
    QTableWidgetItem(QTableWidgetItem)
    """
    def background(self): # real signature unknown; restored from __doc__
        """ background(self) -> QBrush """
        pass

    def checkState(self): # real signature unknown; restored from __doc__
        """ checkState(self) -> Qt.CheckState """
        pass

    def clone(self): # real signature unknown; restored from __doc__
        """ clone(self) -> QTableWidgetItem """
        return QTableWidgetItem

    def column(self): # real signature unknown; restored from __doc__
        """ column(self) -> int """
        return 0

    def data(self, p_int): # real signature unknown; restored from __doc__
        """ data(self, int) -> Any """
        pass

    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> Qt.ItemFlags """
        pass

    def font(self): # real signature unknown; restored from __doc__
        """ font(self) -> QFont """
        pass

    def foreground(self): # real signature unknown; restored from __doc__
        """ foreground(self) -> QBrush """
        pass

    def icon(self): # real signature unknown; restored from __doc__
        """ icon(self) -> QIcon """
        pass

    def isSelected(self): # real signature unknown; restored from __doc__
        """ isSelected(self) -> bool """
        return False

    def read(self, QDataStream): # real signature unknown; restored from __doc__
        """ read(self, QDataStream) """
        pass

    def row(self): # real signature unknown; restored from __doc__
        """ row(self) -> int """
        return 0

    def setBackground(self, Union, QBrush=None, QColor=None, Qt_GlobalColor=None, QGradient=None): # real signature unknown; restored from __doc__
        """ setBackground(self, Union[QBrush, QColor, Qt.GlobalColor, QGradient]) """
        pass

    def setCheckState(self, Qt_CheckState): # real signature unknown; restored from __doc__
        """ setCheckState(self, Qt.CheckState) """
        pass

    def setData(self, p_int, Any): # real signature unknown; restored from __doc__
        """ setData(self, int, Any) """
        pass

    def setFlags(self, Union, Qt_ItemFlags=None, Qt_ItemFlag=None): # real signature unknown; restored from __doc__
        """ setFlags(self, Union[Qt.ItemFlags, Qt.ItemFlag]) """
        pass

    def setFont(self, QFont): # real signature unknown; restored from __doc__
        """ setFont(self, QFont) """
        pass

    def setForeground(self, Union, QBrush=None, QColor=None, Qt_GlobalColor=None, QGradient=None): # real signature unknown; restored from __doc__
        """ setForeground(self, Union[QBrush, QColor, Qt.GlobalColor, QGradient]) """
        pass

    def setIcon(self, QIcon): # real signature unknown; restored from __doc__
        """ setIcon(self, QIcon) """
        pass

    def setSelected(self, bool): # real signature unknown; restored from __doc__
        """ setSelected(self, bool) """
        pass

    def setSizeHint(self, QSize): # real signature unknown; restored from __doc__
        """ setSizeHint(self, QSize) """
        pass

    def setStatusTip(self, p_str): # real signature unknown; restored from __doc__
        """ setStatusTip(self, str) """
        pass

    def setText(self, p_str): # real signature unknown; restored from __doc__
        """ setText(self, str) """
        pass

    def setTextAlignment(self, p_int): # real signature unknown; restored from __doc__
        """ setTextAlignment(self, int) """
        pass

    def setToolTip(self, p_str): # real signature unknown; restored from __doc__
        """ setToolTip(self, str) """
        pass

    def setWhatsThis(self, p_str): # real signature unknown; restored from __doc__
        """ setWhatsThis(self, str) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def statusTip(self): # real signature unknown; restored from __doc__
        """ statusTip(self) -> str """
        return ""

    def tableWidget(self): # real signature unknown; restored from __doc__
        """ tableWidget(self) -> QTableWidget """
        return QTableWidget

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def textAlignment(self): # real signature unknown; restored from __doc__
        """ textAlignment(self) -> int """
        return 0

    def toolTip(self): # real signature unknown; restored from __doc__
        """ toolTip(self) -> str """
        return ""

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> int """
        return 0

    def whatsThis(self): # real signature unknown; restored from __doc__
        """ whatsThis(self) -> str """
        return ""

    def write(self, QDataStream): # real signature unknown; restored from __doc__
        """ write(self, QDataStream) """
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


    Type = 0
    UserType = 1000
    __hash__ = None


