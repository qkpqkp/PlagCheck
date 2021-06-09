# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QTreeWidgetItemIterator(__sip.simplewrapper):
    """
    QTreeWidgetItemIterator(QTreeWidgetItemIterator)
    QTreeWidgetItemIterator(QTreeWidget, flags: QTreeWidgetItemIterator.IteratorFlags = QTreeWidgetItemIterator.All)
    QTreeWidgetItemIterator(QTreeWidgetItem, flags: QTreeWidgetItemIterator.IteratorFlags = QTreeWidgetItemIterator.All)
    """
    def value(self): # real signature unknown; restored from __doc__
        """ value(self) -> QTreeWidgetItem """
        return QTreeWidgetItem

    def __iadd__(self, *args, **kwargs): # real signature unknown
        """ Return self+=value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __isub__(self, *args, **kwargs): # real signature unknown
        """ Return self-=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    All = 0
    Checked = 4096
    Disabled = 32768
    DragDisabled = 128
    DragEnabled = 64
    DropDisabled = 512
    DropEnabled = 256
    Editable = 65536
    Enabled = 16384
    HasChildren = 1024
    Hidden = 1
    NoChildren = 2048
    NotChecked = 8192
    NotEditable = 131072
    NotHidden = 2
    NotSelectable = 32
    Selectable = 16
    Selected = 4
    Unselected = 8
    UserFlag = 16777216


