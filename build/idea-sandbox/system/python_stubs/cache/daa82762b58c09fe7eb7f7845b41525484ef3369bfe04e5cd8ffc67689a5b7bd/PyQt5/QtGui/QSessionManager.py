# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QSessionManager(__PyQt5_QtCore.QObject):
    # no doc
    def allowsErrorInteraction(self): # real signature unknown; restored from __doc__
        """ allowsErrorInteraction(self) -> bool """
        return False

    def allowsInteraction(self): # real signature unknown; restored from __doc__
        """ allowsInteraction(self) -> bool """
        return False

    def cancel(self): # real signature unknown; restored from __doc__
        """ cancel(self) """
        pass

    def discardCommand(self): # real signature unknown; restored from __doc__
        """ discardCommand(self) -> List[str] """
        return []

    def isPhase2(self): # real signature unknown; restored from __doc__
        """ isPhase2(self) -> bool """
        return False

    def release(self): # real signature unknown; restored from __doc__
        """ release(self) """
        pass

    def requestPhase2(self): # real signature unknown; restored from __doc__
        """ requestPhase2(self) """
        pass

    def restartCommand(self): # real signature unknown; restored from __doc__
        """ restartCommand(self) -> List[str] """
        return []

    def restartHint(self): # real signature unknown; restored from __doc__
        """ restartHint(self) -> QSessionManager.RestartHint """
        pass

    def sessionId(self): # real signature unknown; restored from __doc__
        """ sessionId(self) -> str """
        return ""

    def sessionKey(self): # real signature unknown; restored from __doc__
        """ sessionKey(self) -> str """
        return ""

    def setDiscardCommand(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ setDiscardCommand(self, Iterable[str]) """
        pass

    def setManagerProperty(self, p_str, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setManagerProperty(self, str, str)
        setManagerProperty(self, str, Iterable[str])
        """
        pass

    def setRestartCommand(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ setRestartCommand(self, Iterable[str]) """
        pass

    def setRestartHint(self, QSessionManager_RestartHint): # real signature unknown; restored from __doc__
        """ setRestartHint(self, QSessionManager.RestartHint) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    RestartAnyway = 1
    RestartIfRunning = 0
    RestartImmediately = 2
    RestartNever = 3


