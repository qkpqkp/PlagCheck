# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QStorageInfo(__sip.simplewrapper):
    """
    QStorageInfo()
    QStorageInfo(str)
    QStorageInfo(QDir)
    QStorageInfo(QStorageInfo)
    """
    def blockSize(self): # real signature unknown; restored from __doc__
        """ blockSize(self) -> int """
        return 0

    def bytesAvailable(self): # real signature unknown; restored from __doc__
        """ bytesAvailable(self) -> int """
        return 0

    def bytesFree(self): # real signature unknown; restored from __doc__
        """ bytesFree(self) -> int """
        return 0

    def bytesTotal(self): # real signature unknown; restored from __doc__
        """ bytesTotal(self) -> int """
        return 0

    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> QByteArray """
        return QByteArray

    def displayName(self): # real signature unknown; restored from __doc__
        """ displayName(self) -> str """
        return ""

    def fileSystemType(self): # real signature unknown; restored from __doc__
        """ fileSystemType(self) -> QByteArray """
        return QByteArray

    def isReadOnly(self): # real signature unknown; restored from __doc__
        """ isReadOnly(self) -> bool """
        return False

    def isReady(self): # real signature unknown; restored from __doc__
        """ isReady(self) -> bool """
        return False

    def isRoot(self): # real signature unknown; restored from __doc__
        """ isRoot(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def mountedVolumes(self): # real signature unknown; restored from __doc__
        """ mountedVolumes() -> List[QStorageInfo] """
        return []

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def refresh(self): # real signature unknown; restored from __doc__
        """ refresh(self) """
        pass

    def root(self): # real signature unknown; restored from __doc__
        """ root() -> QStorageInfo """
        return QStorageInfo

    def rootPath(self): # real signature unknown; restored from __doc__
        """ rootPath(self) -> str """
        return ""

    def setPath(self, p_str): # real signature unknown; restored from __doc__
        """ setPath(self, str) """
        pass

    def subvolume(self): # real signature unknown; restored from __doc__
        """ subvolume(self) -> QByteArray """
        return QByteArray

    def swap(self, QStorageInfo): # real signature unknown; restored from __doc__
        """ swap(self, QStorageInfo) """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __hash__ = None


