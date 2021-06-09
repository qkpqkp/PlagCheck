# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QObject import QObject

class QEventLoop(QObject):
    """ QEventLoop(parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def exec(self, flags=None): # real signature unknown; restored from __doc__
        """ exec(self, flags: QEventLoop.ProcessEventsFlags = QEventLoop.AllEvents) -> int """
        return 0

    def exec_(self, flags=None): # real signature unknown; restored from __doc__
        """ exec_(self, flags: QEventLoop.ProcessEventsFlags = QEventLoop.AllEvents) -> int """
        return 0

    def exit(self, returnCode=0): # real signature unknown; restored from __doc__
        """ exit(self, returnCode: int = 0) """
        pass

    def isRunning(self): # real signature unknown; restored from __doc__
        """ isRunning(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def processEvents(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        processEvents(self, flags: Union[QEventLoop.ProcessEventsFlags, QEventLoop.ProcessEventsFlag] = QEventLoop.AllEvents) -> bool
        processEvents(self, Union[QEventLoop.ProcessEventsFlags, QEventLoop.ProcessEventsFlag], int)
        """
        pass

    def quit(self): # real signature unknown; restored from __doc__
        """ quit(self) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def wakeUp(self): # real signature unknown; restored from __doc__
        """ wakeUp(self) """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    AllEvents = 0
    ExcludeSocketNotifiers = 2
    ExcludeUserInputEvents = 1
    WaitForMoreEvents = 4
    X11ExcludeTimers = 8


