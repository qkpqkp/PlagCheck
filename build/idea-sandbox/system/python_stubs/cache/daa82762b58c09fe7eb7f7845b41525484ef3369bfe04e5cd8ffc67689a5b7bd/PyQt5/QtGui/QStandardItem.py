# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QStandardItem(__sip.wrapper):
    """
    QStandardItem()
    QStandardItem(str)
    QStandardItem(QIcon, str)
    QStandardItem(int, columns: int = 1)
    QStandardItem(QStandardItem)
    """
    def accessibleDescription(self): # real signature unknown; restored from __doc__
        """ accessibleDescription(self) -> str """
        return ""

    def accessibleText(self): # real signature unknown; restored from __doc__
        """ accessibleText(self) -> str """
        return ""

    def appendColumn(self, Iterable, QStandardItem=None): # real signature unknown; restored from __doc__
        """ appendColumn(self, Iterable[QStandardItem]) """
        pass

    def appendRow(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        appendRow(self, Iterable[QStandardItem])
        appendRow(self, QStandardItem)
        """
        pass

    def appendRows(self, Iterable, QStandardItem=None): # real signature unknown; restored from __doc__
        """ appendRows(self, Iterable[QStandardItem]) """
        pass

    def background(self): # real signature unknown; restored from __doc__
        """ background(self) -> QBrush """
        return QBrush

    def checkState(self): # real signature unknown; restored from __doc__
        """ checkState(self) -> Qt.CheckState """
        pass

    def child(self, p_int, column=0): # real signature unknown; restored from __doc__
        """ child(self, int, column: int = 0) -> QStandardItem """
        return QStandardItem

    def clearData(self): # real signature unknown; restored from __doc__
        """ clearData(self) """
        pass

    def clone(self): # real signature unknown; restored from __doc__
        """ clone(self) -> QStandardItem """
        return QStandardItem

    def column(self): # real signature unknown; restored from __doc__
        """ column(self) -> int """
        return 0

    def columnCount(self): # real signature unknown; restored from __doc__
        """ columnCount(self) -> int """
        return 0

    def data(self, role=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ data(self, role: int = Qt.UserRole+1) -> Any """
        pass

    def emitDataChanged(self): # real signature unknown; restored from __doc__
        """ emitDataChanged(self) """
        pass

    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> Qt.ItemFlags """
        pass

    def font(self): # real signature unknown; restored from __doc__
        """ font(self) -> QFont """
        return QFont

    def foreground(self): # real signature unknown; restored from __doc__
        """ foreground(self) -> QBrush """
        return QBrush

    def hasChildren(self): # real signature unknown; restored from __doc__
        """ hasChildren(self) -> bool """
        return False

    def icon(self): # real signature unknown; restored from __doc__
        """ icon(self) -> QIcon """
        return QIcon

    def index(self): # real signature unknown; restored from __doc__
        """ index(self) -> QModelIndex """
        pass

    def insertColumn(self, p_int, Iterable, QStandardItem=None): # real signature unknown; restored from __doc__
        """ insertColumn(self, int, Iterable[QStandardItem]) """
        pass

    def insertColumns(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ insertColumns(self, int, int) """
        pass

    def insertRow(self, p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        insertRow(self, int, Iterable[QStandardItem])
        insertRow(self, int, QStandardItem)
        """
        pass

    def insertRows(self, p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        insertRows(self, int, int)
        insertRows(self, int, Iterable[QStandardItem])
        """
        pass

    def isAutoTristate(self): # real signature unknown; restored from __doc__
        """ isAutoTristate(self) -> bool """
        return False

    def isCheckable(self): # real signature unknown; restored from __doc__
        """ isCheckable(self) -> bool """
        return False

    def isDragEnabled(self): # real signature unknown; restored from __doc__
        """ isDragEnabled(self) -> bool """
        return False

    def isDropEnabled(self): # real signature unknown; restored from __doc__
        """ isDropEnabled(self) -> bool """
        return False

    def isEditable(self): # real signature unknown; restored from __doc__
        """ isEditable(self) -> bool """
        return False

    def isEnabled(self): # real signature unknown; restored from __doc__
        """ isEnabled(self) -> bool """
        return False

    def isSelectable(self): # real signature unknown; restored from __doc__
        """ isSelectable(self) -> bool """
        return False

    def isTristate(self): # real signature unknown; restored from __doc__
        """ isTristate(self) -> bool """
        return False

    def isUserTristate(self): # real signature unknown; restored from __doc__
        """ isUserTristate(self) -> bool """
        return False

    def model(self): # real signature unknown; restored from __doc__
        """ model(self) -> QStandardItemModel """
        return QStandardItemModel

    def parent(self): # real signature unknown; restored from __doc__
        """ parent(self) -> QStandardItem """
        return QStandardItem

    def read(self, QDataStream): # real signature unknown; restored from __doc__
        """ read(self, QDataStream) """
        pass

    def removeColumn(self, p_int): # real signature unknown; restored from __doc__
        """ removeColumn(self, int) """
        pass

    def removeColumns(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ removeColumns(self, int, int) """
        pass

    def removeRow(self, p_int): # real signature unknown; restored from __doc__
        """ removeRow(self, int) """
        pass

    def removeRows(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ removeRows(self, int, int) """
        pass

    def row(self): # real signature unknown; restored from __doc__
        """ row(self) -> int """
        return 0

    def rowCount(self): # real signature unknown; restored from __doc__
        """ rowCount(self) -> int """
        return 0

    def setAccessibleDescription(self, p_str): # real signature unknown; restored from __doc__
        """ setAccessibleDescription(self, str) """
        pass

    def setAccessibleText(self, p_str): # real signature unknown; restored from __doc__
        """ setAccessibleText(self, str) """
        pass

    def setAutoTristate(self, bool): # real signature unknown; restored from __doc__
        """ setAutoTristate(self, bool) """
        pass

    def setBackground(self, Union, QBrush=None, QColor=None, Qt_GlobalColor=None, QGradient=None): # real signature unknown; restored from __doc__
        """ setBackground(self, Union[QBrush, QColor, Qt.GlobalColor, QGradient]) """
        pass

    def setCheckable(self, bool): # real signature unknown; restored from __doc__
        """ setCheckable(self, bool) """
        pass

    def setCheckState(self, Qt_CheckState): # real signature unknown; restored from __doc__
        """ setCheckState(self, Qt.CheckState) """
        pass

    def setChild(self, p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setChild(self, int, int, QStandardItem)
        setChild(self, int, QStandardItem)
        """
        pass

    def setColumnCount(self, p_int): # real signature unknown; restored from __doc__
        """ setColumnCount(self, int) """
        pass

    def setData(self, Any, role=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setData(self, Any, role: int = Qt.UserRole+1) """
        pass

    def setDragEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setDragEnabled(self, bool) """
        pass

    def setDropEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setDropEnabled(self, bool) """
        pass

    def setEditable(self, bool): # real signature unknown; restored from __doc__
        """ setEditable(self, bool) """
        pass

    def setEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setEnabled(self, bool) """
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

    def setRowCount(self, p_int): # real signature unknown; restored from __doc__
        """ setRowCount(self, int) """
        pass

    def setSelectable(self, bool): # real signature unknown; restored from __doc__
        """ setSelectable(self, bool) """
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

    def setTextAlignment(self, Union, Qt_Alignment=None, Qt_AlignmentFlag=None): # real signature unknown; restored from __doc__
        """ setTextAlignment(self, Union[Qt.Alignment, Qt.AlignmentFlag]) """
        pass

    def setToolTip(self, p_str): # real signature unknown; restored from __doc__
        """ setToolTip(self, str) """
        pass

    def setTristate(self, bool): # real signature unknown; restored from __doc__
        """ setTristate(self, bool) """
        pass

    def setUserTristate(self, bool): # real signature unknown; restored from __doc__
        """ setUserTristate(self, bool) """
        pass

    def setWhatsThis(self, p_str): # real signature unknown; restored from __doc__
        """ setWhatsThis(self, str) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def sortChildren(self, p_int, order=None): # real signature unknown; restored from __doc__
        """ sortChildren(self, int, order: Qt.SortOrder = Qt.AscendingOrder) """
        pass

    def statusTip(self): # real signature unknown; restored from __doc__
        """ statusTip(self) -> str """
        return ""

    def takeChild(self, p_int, column=0): # real signature unknown; restored from __doc__
        """ takeChild(self, int, column: int = 0) -> QStandardItem """
        return QStandardItem

    def takeColumn(self, p_int): # real signature unknown; restored from __doc__
        """ takeColumn(self, int) -> List[QStandardItem] """
        return []

    def takeRow(self, p_int): # real signature unknown; restored from __doc__
        """ takeRow(self, int) -> List[QStandardItem] """
        return []

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def textAlignment(self): # real signature unknown; restored from __doc__
        """ textAlignment(self) -> Qt.Alignment """
        pass

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


