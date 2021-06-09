# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QAction import QAction

class QWidgetAction(QAction):
    """ QWidgetAction(QObject) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createdWidgets(self): # real signature unknown; restored from __doc__
        """ createdWidgets(self) -> List[QWidget] """
        return []

    def createWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ createWidget(self, QWidget) -> QWidget """
        return QWidget

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultWidget(self): # real signature unknown; restored from __doc__
        """ defaultWidget(self) -> QWidget """
        return QWidget

    def deleteWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ deleteWidget(self, QWidget) """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def eventFilter(self, QObject, QEvent): # real signature unknown; restored from __doc__
        """ eventFilter(self, QObject, QEvent) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def releaseWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ releaseWidget(self, QWidget) """
        pass

    def requestWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ requestWidget(self, QWidget) -> QWidget """
        return QWidget

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setDefaultWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ setDefaultWidget(self, QWidget) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, QObject): # real signature unknown; restored from __doc__
        pass


