# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QActionGroup(__PyQt5_QtCore.QObject):
    """ QActionGroup(QObject) """
    def actions(self): # real signature unknown; restored from __doc__
        """ actions(self) -> List[QAction] """
        return []

    def addAction(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addAction(self, QAction) -> QAction
        addAction(self, str) -> QAction
        addAction(self, QIcon, str) -> QAction
        """
        return QAction

    def checkedAction(self): # real signature unknown; restored from __doc__
        """ checkedAction(self) -> QAction """
        return QAction

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def hovered(self, QAction): # real signature unknown; restored from __doc__
        """ hovered(self, QAction) [signal] """
        pass

    def isEnabled(self): # real signature unknown; restored from __doc__
        """ isEnabled(self) -> bool """
        return False

    def isExclusive(self): # real signature unknown; restored from __doc__
        """ isExclusive(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isVisible(self): # real signature unknown; restored from __doc__
        """ isVisible(self) -> bool """
        return False

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeAction(self, QAction): # real signature unknown; restored from __doc__
        """ removeAction(self, QAction) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setDisabled(self, bool): # real signature unknown; restored from __doc__
        """ setDisabled(self, bool) """
        pass

    def setEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setEnabled(self, bool) """
        pass

    def setExclusive(self, bool): # real signature unknown; restored from __doc__
        """ setExclusive(self, bool) """
        pass

    def setVisible(self, bool): # real signature unknown; restored from __doc__
        """ setVisible(self, bool) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def triggered(self, QAction): # real signature unknown; restored from __doc__
        """ triggered(self, QAction) [signal] """
        pass

    def __init__(self, QObject): # real signature unknown; restored from __doc__
        pass


