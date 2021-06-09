# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QFileInfo(__sip.simplewrapper):
    """
    QFileInfo()
    QFileInfo(str)
    QFileInfo(QFile)
    QFileInfo(QDir, str)
    QFileInfo(QFileInfo)
    """
    def absoluteDir(self): # real signature unknown; restored from __doc__
        """ absoluteDir(self) -> QDir """
        return QDir

    def absoluteFilePath(self): # real signature unknown; restored from __doc__
        """ absoluteFilePath(self) -> str """
        return ""

    def absolutePath(self): # real signature unknown; restored from __doc__
        """ absolutePath(self) -> str """
        return ""

    def baseName(self): # real signature unknown; restored from __doc__
        """ baseName(self) -> str """
        return ""

    def birthTime(self): # real signature unknown; restored from __doc__
        """ birthTime(self) -> QDateTime """
        return QDateTime

    def bundleName(self): # real signature unknown; restored from __doc__
        """ bundleName(self) -> str """
        return ""

    def caching(self): # real signature unknown; restored from __doc__
        """ caching(self) -> bool """
        return False

    def canonicalFilePath(self): # real signature unknown; restored from __doc__
        """ canonicalFilePath(self) -> str """
        return ""

    def canonicalPath(self): # real signature unknown; restored from __doc__
        """ canonicalPath(self) -> str """
        return ""

    def completeBaseName(self): # real signature unknown; restored from __doc__
        """ completeBaseName(self) -> str """
        return ""

    def completeSuffix(self): # real signature unknown; restored from __doc__
        """ completeSuffix(self) -> str """
        return ""

    def created(self): # real signature unknown; restored from __doc__
        """ created(self) -> QDateTime """
        return QDateTime

    def dir(self): # real signature unknown; restored from __doc__
        """ dir(self) -> QDir """
        return QDir

    def exists(self, p_str=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        exists(self) -> bool
        exists(str) -> bool
        """
        return False

    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def filePath(self): # real signature unknown; restored from __doc__
        """ filePath(self) -> str """
        return ""

    def fileTime(self, QFileDevice_FileTime): # real signature unknown; restored from __doc__
        """ fileTime(self, QFileDevice.FileTime) -> QDateTime """
        return QDateTime

    def group(self): # real signature unknown; restored from __doc__
        """ group(self) -> str """
        return ""

    def groupId(self): # real signature unknown; restored from __doc__
        """ groupId(self) -> int """
        return 0

    def isAbsolute(self): # real signature unknown; restored from __doc__
        """ isAbsolute(self) -> bool """
        return False

    def isBundle(self): # real signature unknown; restored from __doc__
        """ isBundle(self) -> bool """
        return False

    def isDir(self): # real signature unknown; restored from __doc__
        """ isDir(self) -> bool """
        return False

    def isExecutable(self): # real signature unknown; restored from __doc__
        """ isExecutable(self) -> bool """
        return False

    def isFile(self): # real signature unknown; restored from __doc__
        """ isFile(self) -> bool """
        return False

    def isHidden(self): # real signature unknown; restored from __doc__
        """ isHidden(self) -> bool """
        return False

    def isNativePath(self): # real signature unknown; restored from __doc__
        """ isNativePath(self) -> bool """
        return False

    def isReadable(self): # real signature unknown; restored from __doc__
        """ isReadable(self) -> bool """
        return False

    def isRelative(self): # real signature unknown; restored from __doc__
        """ isRelative(self) -> bool """
        return False

    def isRoot(self): # real signature unknown; restored from __doc__
        """ isRoot(self) -> bool """
        return False

    def isSymLink(self): # real signature unknown; restored from __doc__
        """ isSymLink(self) -> bool """
        return False

    def isWritable(self): # real signature unknown; restored from __doc__
        """ isWritable(self) -> bool """
        return False

    def lastModified(self): # real signature unknown; restored from __doc__
        """ lastModified(self) -> QDateTime """
        return QDateTime

    def lastRead(self): # real signature unknown; restored from __doc__
        """ lastRead(self) -> QDateTime """
        return QDateTime

    def makeAbsolute(self): # real signature unknown; restored from __doc__
        """ makeAbsolute(self) -> bool """
        return False

    def metadataChangeTime(self): # real signature unknown; restored from __doc__
        """ metadataChangeTime(self) -> QDateTime """
        return QDateTime

    def owner(self): # real signature unknown; restored from __doc__
        """ owner(self) -> str """
        return ""

    def ownerId(self): # real signature unknown; restored from __doc__
        """ ownerId(self) -> int """
        return 0

    def path(self): # real signature unknown; restored from __doc__
        """ path(self) -> str """
        return ""

    def permission(self, Union, QFileDevice_Permissions=None, QFileDevice_Permission=None): # real signature unknown; restored from __doc__
        """ permission(self, Union[QFileDevice.Permissions, QFileDevice.Permission]) -> bool """
        return False

    def permissions(self): # real signature unknown; restored from __doc__
        """ permissions(self) -> QFileDevice.Permissions """
        pass

    def refresh(self): # real signature unknown; restored from __doc__
        """ refresh(self) """
        pass

    def setCaching(self, bool): # real signature unknown; restored from __doc__
        """ setCaching(self, bool) """
        pass

    def setFile(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setFile(self, str)
        setFile(self, QFile)
        setFile(self, QDir, str)
        """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def suffix(self): # real signature unknown; restored from __doc__
        """ suffix(self) -> str """
        return ""

    def swap(self, QFileInfo): # real signature unknown; restored from __doc__
        """ swap(self, QFileInfo) """
        pass

    def symLinkTarget(self): # real signature unknown; restored from __doc__
        """ symLinkTarget(self) -> str """
        return ""

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __fspath__(self): # real signature unknown; restored from __doc__
        """ __fspath__(self) -> object """
        return object()

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


