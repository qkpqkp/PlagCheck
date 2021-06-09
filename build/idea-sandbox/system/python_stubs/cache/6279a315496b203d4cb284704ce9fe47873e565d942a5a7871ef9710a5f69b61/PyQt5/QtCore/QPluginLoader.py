# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QObject import QObject

class QPluginLoader(QObject):
    """
    QPluginLoader(parent: QObject = None)
    QPluginLoader(str, parent: QObject = None)
    """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def instance(self): # real signature unknown; restored from __doc__
        """ instance(self) -> QObject """
        return QObject

    def isLoaded(self): # real signature unknown; restored from __doc__
        """ isLoaded(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def load(self): # real signature unknown; restored from __doc__
        """ load(self) -> bool """
        return False

    def loadHints(self): # real signature unknown; restored from __doc__
        """ loadHints(self) -> QLibrary.LoadHints """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setFileName(self, p_str): # real signature unknown; restored from __doc__
        """ setFileName(self, str) """
        pass

    def setLoadHints(self, Union, QLibrary_LoadHints=None, QLibrary_LoadHint=None): # real signature unknown; restored from __doc__
        """ setLoadHints(self, Union[QLibrary.LoadHints, QLibrary.LoadHint]) """
        pass

    def staticInstances(self): # real signature unknown; restored from __doc__
        """ staticInstances() -> List[QObject] """
        return []

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def unload(self): # real signature unknown; restored from __doc__
        """ unload(self) -> bool """
        return False

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


