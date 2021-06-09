# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QObject import QObject

class QAbstractState(QObject):
    """ QAbstractState(parent: QState = None) """
    def active(self): # real signature unknown; restored from __doc__
        """ active(self) -> bool """
        return False

    def activeChanged(self, bool): # real signature unknown; restored from __doc__
        """ activeChanged(self, bool) [signal] """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def entered(self): # real signature unknown; restored from __doc__
        """ entered(self) [signal] """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def exited(self): # real signature unknown; restored from __doc__
        """ exited(self) [signal] """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def machine(self): # real signature unknown; restored from __doc__
        """ machine(self) -> QStateMachine """
        return QStateMachine

    def onEntry(self, QEvent): # real signature unknown; restored from __doc__
        """ onEntry(self, QEvent) """
        pass

    def onExit(self, QEvent): # real signature unknown; restored from __doc__
        """ onExit(self, QEvent) """
        pass

    def parentState(self): # real signature unknown; restored from __doc__
        """ parentState(self) -> QState """
        return QState

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


