# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QAbstractItemDelegate(__PyQt5_QtCore.QObject):
    """ QAbstractItemDelegate(parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEditor(self, QWidget, hint=None): # real signature unknown; restored from __doc__
        """ closeEditor(self, QWidget, hint: QAbstractItemDelegate.EndEditHint = QAbstractItemDelegate.NoHint) [signal] """
        pass

    def commitData(self, QWidget): # real signature unknown; restored from __doc__
        """ commitData(self, QWidget) [signal] """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createEditor(self, QWidget, QStyleOptionViewItem, QModelIndex): # real signature unknown; restored from __doc__
        """ createEditor(self, QWidget, QStyleOptionViewItem, QModelIndex) -> QWidget """
        return QWidget

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def destroyEditor(self, QWidget, QModelIndex): # real signature unknown; restored from __doc__
        """ destroyEditor(self, QWidget, QModelIndex) """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def editorEvent(self, QEvent, QAbstractItemModel, QStyleOptionViewItem, QModelIndex): # real signature unknown; restored from __doc__
        """ editorEvent(self, QEvent, QAbstractItemModel, QStyleOptionViewItem, QModelIndex) -> bool """
        return False

    def helpEvent(self, QHelpEvent, QAbstractItemView, QStyleOptionViewItem, QModelIndex): # real signature unknown; restored from __doc__
        """ helpEvent(self, QHelpEvent, QAbstractItemView, QStyleOptionViewItem, QModelIndex) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def paint(self, QPainter, QStyleOptionViewItem, QModelIndex): # real signature unknown; restored from __doc__
        """ paint(self, QPainter, QStyleOptionViewItem, QModelIndex) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setEditorData(self, QWidget, QModelIndex): # real signature unknown; restored from __doc__
        """ setEditorData(self, QWidget, QModelIndex) """
        pass

    def setModelData(self, QWidget, QAbstractItemModel, QModelIndex): # real signature unknown; restored from __doc__
        """ setModelData(self, QWidget, QAbstractItemModel, QModelIndex) """
        pass

    def sizeHint(self, QStyleOptionViewItem, QModelIndex): # real signature unknown; restored from __doc__
        """ sizeHint(self, QStyleOptionViewItem, QModelIndex) -> QSize """
        pass

    def sizeHintChanged(self, QModelIndex): # real signature unknown; restored from __doc__
        """ sizeHintChanged(self, QModelIndex) [signal] """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateEditorGeometry(self, QWidget, QStyleOptionViewItem, QModelIndex): # real signature unknown; restored from __doc__
        """ updateEditorGeometry(self, QWidget, QStyleOptionViewItem, QModelIndex) """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    EditNextItem = 1
    EditPreviousItem = 2
    NoHint = 0
    RevertModelCache = 4
    SubmitModelCache = 3


