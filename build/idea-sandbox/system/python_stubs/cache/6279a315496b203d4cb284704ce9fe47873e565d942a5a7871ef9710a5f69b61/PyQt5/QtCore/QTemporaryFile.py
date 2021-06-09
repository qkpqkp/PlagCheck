# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QFile import QFile

class QTemporaryFile(QFile):
    """
    QTemporaryFile()
    QTemporaryFile(str)
    QTemporaryFile(QObject)
    QTemporaryFile(str, QObject)
    """
    def autoRemove(self): # real signature unknown; restored from __doc__
        """ autoRemove(self) -> bool """
        return False

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createNativeFile(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        createNativeFile(str) -> QTemporaryFile
        createNativeFile(QFile) -> QTemporaryFile
        """
        return QTemporaryFile

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def fileTemplate(self): # real signature unknown; restored from __doc__
        """ fileTemplate(self) -> str """
        return ""

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def open(self, Union=None, QIODevice_OpenMode=None, QIODevice_OpenModeFlag=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        open(self) -> bool
        open(self, Union[QIODevice.OpenMode, QIODevice.OpenModeFlag]) -> bool
        """
        return False

    def readData(self, *args, **kwargs): # real signature unknown
        pass

    def readLineData(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def rename(self, p_str): # real signature unknown; restored from __doc__
        """ rename(self, str) -> bool """
        return False

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAutoRemove(self, bool): # real signature unknown; restored from __doc__
        """ setAutoRemove(self, bool) """
        pass

    def setErrorString(self, *args, **kwargs): # real signature unknown
        pass

    def setFileTemplate(self, p_str): # real signature unknown; restored from __doc__
        """ setFileTemplate(self, str) """
        pass

    def setOpenMode(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def writeData(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


