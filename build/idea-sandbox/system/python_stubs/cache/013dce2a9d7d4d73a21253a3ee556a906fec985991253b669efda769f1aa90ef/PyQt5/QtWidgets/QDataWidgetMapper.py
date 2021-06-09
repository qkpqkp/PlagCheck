# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QDataWidgetMapper(__PyQt5_QtCore.QObject):
    """ QDataWidgetMapper(parent: QObject = None) """
    def addMapping(self, QWidget, p_int, Union=None, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addMapping(self, QWidget, int)
        addMapping(self, QWidget, int, Union[QByteArray, bytes, bytearray])
        """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clearMapping(self): # real signature unknown; restored from __doc__
        """ clearMapping(self) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def currentIndex(self): # real signature unknown; restored from __doc__
        """ currentIndex(self) -> int """
        return 0

    def currentIndexChanged(self, p_int): # real signature unknown; restored from __doc__
        """ currentIndexChanged(self, int) [signal] """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def itemDelegate(self): # real signature unknown; restored from __doc__
        """ itemDelegate(self) -> QAbstractItemDelegate """
        return QAbstractItemDelegate

    def mappedPropertyName(self, QWidget): # real signature unknown; restored from __doc__
        """ mappedPropertyName(self, QWidget) -> QByteArray """
        pass

    def mappedSection(self, QWidget): # real signature unknown; restored from __doc__
        """ mappedSection(self, QWidget) -> int """
        return 0

    def mappedWidgetAt(self, p_int): # real signature unknown; restored from __doc__
        """ mappedWidgetAt(self, int) -> QWidget """
        return QWidget

    def model(self): # real signature unknown; restored from __doc__
        """ model(self) -> QAbstractItemModel """
        pass

    def orientation(self): # real signature unknown; restored from __doc__
        """ orientation(self) -> Qt.Orientation """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeMapping(self, QWidget): # real signature unknown; restored from __doc__
        """ removeMapping(self, QWidget) """
        pass

    def revert(self): # real signature unknown; restored from __doc__
        """ revert(self) """
        pass

    def rootIndex(self): # real signature unknown; restored from __doc__
        """ rootIndex(self) -> QModelIndex """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCurrentIndex(self, p_int): # real signature unknown; restored from __doc__
        """ setCurrentIndex(self, int) """
        pass

    def setCurrentModelIndex(self, QModelIndex): # real signature unknown; restored from __doc__
        """ setCurrentModelIndex(self, QModelIndex) """
        pass

    def setItemDelegate(self, QAbstractItemDelegate): # real signature unknown; restored from __doc__
        """ setItemDelegate(self, QAbstractItemDelegate) """
        pass

    def setModel(self, QAbstractItemModel): # real signature unknown; restored from __doc__
        """ setModel(self, QAbstractItemModel) """
        pass

    def setOrientation(self, Qt_Orientation): # real signature unknown; restored from __doc__
        """ setOrientation(self, Qt.Orientation) """
        pass

    def setRootIndex(self, QModelIndex): # real signature unknown; restored from __doc__
        """ setRootIndex(self, QModelIndex) """
        pass

    def setSubmitPolicy(self, QDataWidgetMapper_SubmitPolicy): # real signature unknown; restored from __doc__
        """ setSubmitPolicy(self, QDataWidgetMapper.SubmitPolicy) """
        pass

    def submit(self): # real signature unknown; restored from __doc__
        """ submit(self) -> bool """
        return False

    def submitPolicy(self): # real signature unknown; restored from __doc__
        """ submitPolicy(self) -> QDataWidgetMapper.SubmitPolicy """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def toFirst(self): # real signature unknown; restored from __doc__
        """ toFirst(self) """
        pass

    def toLast(self): # real signature unknown; restored from __doc__
        """ toLast(self) """
        pass

    def toNext(self): # real signature unknown; restored from __doc__
        """ toNext(self) """
        pass

    def toPrevious(self): # real signature unknown; restored from __doc__
        """ toPrevious(self) """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    AutoSubmit = 0
    ManualSubmit = 1


