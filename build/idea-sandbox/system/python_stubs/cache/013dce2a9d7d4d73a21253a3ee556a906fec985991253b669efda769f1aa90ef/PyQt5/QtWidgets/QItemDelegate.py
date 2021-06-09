# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QAbstractItemDelegate import QAbstractItemDelegate

class QItemDelegate(QAbstractItemDelegate):
    """ QItemDelegate(parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createEditor(self, QWidget, QStyleOptionViewItem, QModelIndex): # real signature unknown; restored from __doc__
        """ createEditor(self, QWidget, QStyleOptionViewItem, QModelIndex) -> QWidget """
        return QWidget

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def drawBackground(self, QPainter, QStyleOptionViewItem, QModelIndex): # real signature unknown; restored from __doc__
        """ drawBackground(self, QPainter, QStyleOptionViewItem, QModelIndex) """
        pass

    def drawCheck(self, QPainter, QStyleOptionViewItem, QRect, Qt_CheckState): # real signature unknown; restored from __doc__
        """ drawCheck(self, QPainter, QStyleOptionViewItem, QRect, Qt.CheckState) """
        pass

    def drawDecoration(self, QPainter, QStyleOptionViewItem, QRect, QPixmap): # real signature unknown; restored from __doc__
        """ drawDecoration(self, QPainter, QStyleOptionViewItem, QRect, QPixmap) """
        pass

    def drawDisplay(self, QPainter, QStyleOptionViewItem, QRect, p_str): # real signature unknown; restored from __doc__
        """ drawDisplay(self, QPainter, QStyleOptionViewItem, QRect, str) """
        pass

    def drawFocus(self, QPainter, QStyleOptionViewItem, QRect): # real signature unknown; restored from __doc__
        """ drawFocus(self, QPainter, QStyleOptionViewItem, QRect) """
        pass

    def editorEvent(self, QEvent, QAbstractItemModel, QStyleOptionViewItem, QModelIndex): # real signature unknown; restored from __doc__
        """ editorEvent(self, QEvent, QAbstractItemModel, QStyleOptionViewItem, QModelIndex) -> bool """
        return False

    def eventFilter(self, QObject, QEvent): # real signature unknown; restored from __doc__
        """ eventFilter(self, QObject, QEvent) -> bool """
        return False

    def hasClipping(self): # real signature unknown; restored from __doc__
        """ hasClipping(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def itemEditorFactory(self): # real signature unknown; restored from __doc__
        """ itemEditorFactory(self) -> QItemEditorFactory """
        return QItemEditorFactory

    def paint(self, QPainter, QStyleOptionViewItem, QModelIndex): # real signature unknown; restored from __doc__
        """ paint(self, QPainter, QStyleOptionViewItem, QModelIndex) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setClipping(self, bool): # real signature unknown; restored from __doc__
        """ setClipping(self, bool) """
        pass

    def setEditorData(self, QWidget, QModelIndex): # real signature unknown; restored from __doc__
        """ setEditorData(self, QWidget, QModelIndex) """
        pass

    def setItemEditorFactory(self, QItemEditorFactory): # real signature unknown; restored from __doc__
        """ setItemEditorFactory(self, QItemEditorFactory) """
        pass

    def setModelData(self, QWidget, QAbstractItemModel, QModelIndex): # real signature unknown; restored from __doc__
        """ setModelData(self, QWidget, QAbstractItemModel, QModelIndex) """
        pass

    def sizeHint(self, QStyleOptionViewItem, QModelIndex): # real signature unknown; restored from __doc__
        """ sizeHint(self, QStyleOptionViewItem, QModelIndex) -> QSize """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateEditorGeometry(self, QWidget, QStyleOptionViewItem, QModelIndex): # real signature unknown; restored from __doc__
        """ updateEditorGeometry(self, QWidget, QStyleOptionViewItem, QModelIndex) """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


