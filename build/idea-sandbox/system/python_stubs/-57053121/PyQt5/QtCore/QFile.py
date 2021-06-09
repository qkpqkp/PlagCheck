# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QFileDevice import QFileDevice

class QFile(QFileDevice):
    """
    QFile()
    QFile(str)
    QFile(QObject)
    QFile(str, QObject)
    """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def copy(self, p_str, p_str_1=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        copy(self, str) -> bool
        copy(str, str) -> bool
        """
        return False

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def decodeName(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        decodeName(Union[QByteArray, bytes, bytearray]) -> str
        decodeName(str) -> str
        """
        return ""

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def encodeName(self, p_str): # real signature unknown; restored from __doc__
        """ encodeName(str) -> QByteArray """
        return QByteArray

    def exists(self, p_str=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        exists(self) -> bool
        exists(str) -> bool
        """
        return False

    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def link(self, p_str, p_str_1=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        link(self, str) -> bool
        link(str, str) -> bool
        """
        return False

    def open(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        open(self, Union[QIODevice.OpenMode, QIODevice.OpenModeFlag]) -> bool
        open(self, int, Union[QIODevice.OpenMode, QIODevice.OpenModeFlag], handleFlags: Union[QFileDevice.FileHandleFlags, QFileDevice.FileHandleFlag] = QFileDevice.DontCloseHandle) -> bool
        """
        return False

    def permissions(self, p_str=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        permissions(self) -> QFileDevice.Permissions
        permissions(str) -> QFileDevice.Permissions
        """
        pass

    def readData(self, *args, **kwargs): # real signature unknown
        pass

    def readLineData(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def remove(self, p_str=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        remove(self) -> bool
        remove(str) -> bool
        """
        return False

    def rename(self, p_str, p_str_1=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        rename(self, str) -> bool
        rename(str, str) -> bool
        """
        return False

    def resize(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        resize(self, int) -> bool
        resize(str, int) -> bool
        """
        return False

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setErrorString(self, *args, **kwargs): # real signature unknown
        pass

    def setFileName(self, p_str): # real signature unknown; restored from __doc__
        """ setFileName(self, str) """
        pass

    def setOpenMode(self, *args, **kwargs): # real signature unknown
        pass

    def setPermissions(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setPermissions(self, Union[QFileDevice.Permissions, QFileDevice.Permission]) -> bool
        setPermissions(str, Union[QFileDevice.Permissions, QFileDevice.Permission]) -> bool
        """
        return False

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def symLinkTarget(self, p_str=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        symLinkTarget(self) -> str
        symLinkTarget(str) -> str
        """
        return ""

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def writeData(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


