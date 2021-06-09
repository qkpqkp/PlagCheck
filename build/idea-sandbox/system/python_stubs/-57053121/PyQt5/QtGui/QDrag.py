# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QDrag(__PyQt5_QtCore.QObject):
    """ QDrag(QObject) """
    def actionChanged(self, Qt_DropAction): # real signature unknown; restored from __doc__
        """ actionChanged(self, Qt.DropAction) [signal] """
        pass

    def cancel(self): # real signature unknown; restored from __doc__
        """ cancel() """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultAction(self): # real signature unknown; restored from __doc__
        """ defaultAction(self) -> Qt.DropAction """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dragCursor(self, Qt_DropAction): # real signature unknown; restored from __doc__
        """ dragCursor(self, Qt.DropAction) -> QPixmap """
        return QPixmap

    def exec(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        exec(self, supportedActions: Union[Qt.DropActions, Qt.DropAction] = Qt.MoveAction) -> Qt.DropAction
        exec(self, Union[Qt.DropActions, Qt.DropAction], Qt.DropAction) -> Qt.DropAction
        """
        pass

    def exec_(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        exec_(self, supportedActions: Union[Qt.DropActions, Qt.DropAction] = Qt.MoveAction) -> Qt.DropAction
        exec_(self, Union[Qt.DropActions, Qt.DropAction], Qt.DropAction) -> Qt.DropAction
        """
        pass

    def hotSpot(self): # real signature unknown; restored from __doc__
        """ hotSpot(self) -> QPoint """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def mimeData(self): # real signature unknown; restored from __doc__
        """ mimeData(self) -> QMimeData """
        pass

    def pixmap(self): # real signature unknown; restored from __doc__
        """ pixmap(self) -> QPixmap """
        return QPixmap

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setDragCursor(self, QPixmap, Qt_DropAction): # real signature unknown; restored from __doc__
        """ setDragCursor(self, QPixmap, Qt.DropAction) """
        pass

    def setHotSpot(self, QPoint): # real signature unknown; restored from __doc__
        """ setHotSpot(self, QPoint) """
        pass

    def setMimeData(self, QMimeData): # real signature unknown; restored from __doc__
        """ setMimeData(self, QMimeData) """
        pass

    def setPixmap(self, QPixmap): # real signature unknown; restored from __doc__
        """ setPixmap(self, QPixmap) """
        pass

    def source(self): # real signature unknown; restored from __doc__
        """ source(self) -> QObject """
        pass

    def supportedActions(self): # real signature unknown; restored from __doc__
        """ supportedActions(self) -> Qt.DropActions """
        pass

    def target(self): # real signature unknown; restored from __doc__
        """ target(self) -> QObject """
        pass

    def targetChanged(self, QObject): # real signature unknown; restored from __doc__
        """ targetChanged(self, QObject) [signal] """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, QObject): # real signature unknown; restored from __doc__
        pass


