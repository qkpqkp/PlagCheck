# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QResource(__sip.simplewrapper):
    """ QResource(fileName: str = '', locale: QLocale = QLocale()) """
    def absoluteFilePath(self): # real signature unknown; restored from __doc__
        """ absoluteFilePath(self) -> str """
        return ""

    def children(self): # real signature unknown; restored from __doc__
        """ children(self) -> List[str] """
        return []

    def data(self): # real signature unknown; restored from __doc__
        """ data(self) -> bytes """
        return b""

    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def isCompressed(self): # real signature unknown; restored from __doc__
        """ isCompressed(self) -> bool """
        return False

    def isDir(self): # real signature unknown; restored from __doc__
        """ isDir(self) -> bool """
        return False

    def isFile(self): # real signature unknown; restored from __doc__
        """ isFile(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def lastModified(self): # real signature unknown; restored from __doc__
        """ lastModified(self) -> QDateTime """
        return QDateTime

    def locale(self): # real signature unknown; restored from __doc__
        """ locale(self) -> QLocale """
        return QLocale

    def registerResource(self, p_str, mapRoot=''): # real signature unknown; restored from __doc__
        """ registerResource(str, mapRoot: str = '') -> bool """
        return False

    def registerResourceData(self, bytes, mapRoot=''): # real signature unknown; restored from __doc__
        """ registerResourceData(bytes, mapRoot: str = '') -> bool """
        return False

    def setFileName(self, p_str): # real signature unknown; restored from __doc__
        """ setFileName(self, str) """
        pass

    def setLocale(self, QLocale): # real signature unknown; restored from __doc__
        """ setLocale(self, QLocale) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def unregisterResource(self, p_str, mapRoot=''): # real signature unknown; restored from __doc__
        """ unregisterResource(str, mapRoot: str = '') -> bool """
        return False

    def unregisterResourceData(self, bytes, mapRoot=''): # real signature unknown; restored from __doc__
        """ unregisterResourceData(bytes, mapRoot: str = '') -> bool """
        return False

    def __init__(self, fileName='', locale=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



