# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QTreeWidgetItem(__sip.wrapper):
    """
    QTreeWidgetItem(type: int = QTreeWidgetItem.Type)
    QTreeWidgetItem(Iterable[str], type: int = QTreeWidgetItem.Type)
    QTreeWidgetItem(QTreeWidget, type: int = QTreeWidgetItem.Type)
    QTreeWidgetItem(QTreeWidget, Iterable[str], type: int = QTreeWidgetItem.Type)
    QTreeWidgetItem(QTreeWidget, QTreeWidgetItem, type: int = QTreeWidgetItem.Type)
    QTreeWidgetItem(QTreeWidgetItem, type: int = QTreeWidgetItem.Type)
    QTreeWidgetItem(QTreeWidgetItem, Iterable[str], type: int = QTreeWidgetItem.Type)
    QTreeWidgetItem(QTreeWidgetItem, QTreeWidgetItem, type: int = QTreeWidgetItem.Type)
    QTreeWidgetItem(QTreeWidgetItem)
    """
    def addChild(self, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ addChild(self, QTreeWidgetItem) """
        pass

    def addChildren(self, Iterable, QTreeWidgetItem=None): # real signature unknown; restored from __doc__
        """ addChildren(self, Iterable[QTreeWidgetItem]) """
        pass

    def background(self, p_int): # real signature unknown; restored from __doc__
        """ background(self, int) -> QBrush """
        pass

    def checkState(self, p_int): # real signature unknown; restored from __doc__
        """ checkState(self, int) -> Qt.CheckState """
        pass

    def child(self, p_int): # real signature unknown; restored from __doc__
        """ child(self, int) -> QTreeWidgetItem """
        return QTreeWidgetItem

    def childCount(self): # real signature unknown; restored from __doc__
        """ childCount(self) -> int """
        return 0

    def childIndicatorPolicy(self): # real signature unknown; restored from __doc__
        """ childIndicatorPolicy(self) -> QTreeWidgetItem.ChildIndicatorPolicy """
        pass

    def clone(self): # real signature unknown; restored from __doc__
        """ clone(self) -> QTreeWidgetItem """
        return QTreeWidgetItem

    def columnCount(self): # real signature unknown; restored from __doc__
        """ columnCount(self) -> int """
        return 0

    def data(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ data(self, int, int) -> Any """
        pass

    def emitDataChanged(self): # real signature unknown; restored from __doc__
        """ emitDataChanged(self) """
        pass

    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> Qt.ItemFlags """
        pass

    def font(self, p_int): # real signature unknown; restored from __doc__
        """ font(self, int) -> QFont """
        pass

    def foreground(self, p_int): # real signature unknown; restored from __doc__
        """ foreground(self, int) -> QBrush """
        pass

    def icon(self, p_int): # real signature unknown; restored from __doc__
        """ icon(self, int) -> QIcon """
        pass

    def indexOfChild(self, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ indexOfChild(self, QTreeWidgetItem) -> int """
        return 0

    def insertChild(self, p_int, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ insertChild(self, int, QTreeWidgetItem) """
        pass

    def insertChildren(self, p_int, Iterable, QTreeWidgetItem=None): # real signature unknown; restored from __doc__
        """ insertChildren(self, int, Iterable[QTreeWidgetItem]) """
        pass

    def isDisabled(self): # real signature unknown; restored from __doc__
        """ isDisabled(self) -> bool """
        return False

    def isExpanded(self): # real signature unknown; restored from __doc__
        """ isExpanded(self) -> bool """
        return False

    def isFirstColumnSpanned(self): # real signature unknown; restored from __doc__
        """ isFirstColumnSpanned(self) -> bool """
        return False

    def isHidden(self): # real signature unknown; restored from __doc__
        """ isHidden(self) -> bool """
        return False

    def isSelected(self): # real signature unknown; restored from __doc__
        """ isSelected(self) -> bool """
        return False

    def parent(self): # real signature unknown; restored from __doc__
        """ parent(self) -> QTreeWidgetItem """
        return QTreeWidgetItem

    def read(self, QDataStream): # real signature unknown; restored from __doc__
        """ read(self, QDataStream) """
        pass

    def removeChild(self, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ removeChild(self, QTreeWidgetItem) """
        pass

    def setBackground(self, p_int, Union, QBrush=None, QColor=None, Qt_GlobalColor=None, QGradient=None): # real signature unknown; restored from __doc__
        """ setBackground(self, int, Union[QBrush, QColor, Qt.GlobalColor, QGradient]) """
        pass

    def setCheckState(self, p_int, Qt_CheckState): # real signature unknown; restored from __doc__
        """ setCheckState(self, int, Qt.CheckState) """
        pass

    def setChildIndicatorPolicy(self, QTreeWidgetItem_ChildIndicatorPolicy): # real signature unknown; restored from __doc__
        """ setChildIndicatorPolicy(self, QTreeWidgetItem.ChildIndicatorPolicy) """
        pass

    def setData(self, p_int, p_int_1, Any): # real signature unknown; restored from __doc__
        """ setData(self, int, int, Any) """
        pass

    def setDisabled(self, bool): # real signature unknown; restored from __doc__
        """ setDisabled(self, bool) """
        pass

    def setExpanded(self, bool): # real signature unknown; restored from __doc__
        """ setExpanded(self, bool) """
        pass

    def setFirstColumnSpanned(self, bool): # real signature unknown; restored from __doc__
        """ setFirstColumnSpanned(self, bool) """
        pass

    def setFlags(self, Union, Qt_ItemFlags=None, Qt_ItemFlag=None): # real signature unknown; restored from __doc__
        """ setFlags(self, Union[Qt.ItemFlags, Qt.ItemFlag]) """
        pass

    def setFont(self, p_int, QFont): # real signature unknown; restored from __doc__
        """ setFont(self, int, QFont) """
        pass

    def setForeground(self, p_int, Union, QBrush=None, QColor=None, Qt_GlobalColor=None, QGradient=None): # real signature unknown; restored from __doc__
        """ setForeground(self, int, Union[QBrush, QColor, Qt.GlobalColor, QGradient]) """
        pass

    def setHidden(self, bool): # real signature unknown; restored from __doc__
        """ setHidden(self, bool) """
        pass

    def setIcon(self, p_int, QIcon): # real signature unknown; restored from __doc__
        """ setIcon(self, int, QIcon) """
        pass

    def setSelected(self, bool): # real signature unknown; restored from __doc__
        """ setSelected(self, bool) """
        pass

    def setSizeHint(self, p_int, QSize): # real signature unknown; restored from __doc__
        """ setSizeHint(self, int, QSize) """
        pass

    def setStatusTip(self, p_int, p_str): # real signature unknown; restored from __doc__
        """ setStatusTip(self, int, str) """
        pass

    def setText(self, p_int, p_str): # real signature unknown; restored from __doc__
        """ setText(self, int, str) """
        pass

    def setTextAlignment(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ setTextAlignment(self, int, int) """
        pass

    def setToolTip(self, p_int, p_str): # real signature unknown; restored from __doc__
        """ setToolTip(self, int, str) """
        pass

    def setWhatsThis(self, p_int, p_str): # real signature unknown; restored from __doc__
        """ setWhatsThis(self, int, str) """
        pass

    def sizeHint(self, p_int): # real signature unknown; restored from __doc__
        """ sizeHint(self, int) -> QSize """
        pass

    def sortChildren(self, p_int, Qt_SortOrder): # real signature unknown; restored from __doc__
        """ sortChildren(self, int, Qt.SortOrder) """
        pass

    def statusTip(self, p_int): # real signature unknown; restored from __doc__
        """ statusTip(self, int) -> str """
        return ""

    def takeChild(self, p_int): # real signature unknown; restored from __doc__
        """ takeChild(self, int) -> QTreeWidgetItem """
        return QTreeWidgetItem

    def takeChildren(self): # real signature unknown; restored from __doc__
        """ takeChildren(self) -> List[QTreeWidgetItem] """
        return []

    def text(self, p_int): # real signature unknown; restored from __doc__
        """ text(self, int) -> str """
        return ""

    def textAlignment(self, p_int): # real signature unknown; restored from __doc__
        """ textAlignment(self, int) -> int """
        return 0

    def toolTip(self, p_int): # real signature unknown; restored from __doc__
        """ toolTip(self, int) -> str """
        return ""

    def treeWidget(self): # real signature unknown; restored from __doc__
        """ treeWidget(self) -> QTreeWidget """
        return QTreeWidget

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> int """
        return 0

    def whatsThis(self, p_int): # real signature unknown; restored from __doc__
        """ whatsThis(self, int) -> str """
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


    DontShowIndicator = 1
    DontShowIndicatorWhenChildless = 2
    ShowIndicator = 0
    Type = 0
    UserType = 1000
    __hash__ = None


