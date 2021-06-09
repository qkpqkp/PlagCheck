# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QIODevice import QIODevice

class QFileDevice(QIODevice):
    # no doc
    def atEnd(self): # real signature unknown; restored from __doc__
        """ atEnd(self) -> bool """
        return False

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) """
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> QFileDevice.FileError """
        pass

    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def fileTime(self, QFileDevice_FileTime): # real signature unknown; restored from __doc__
        """ fileTime(self, QFileDevice.FileTime) -> QDateTime """
        return QDateTime

    def flush(self): # real signature unknown; restored from __doc__
        """ flush(self) -> bool """
        return False

    def handle(self): # real signature unknown; restored from __doc__
        """ handle(self) -> int """
        return 0

    def isSequential(self): # real signature unknown; restored from __doc__
        """ isSequential(self) -> bool """
        return False

    def map(self, p_int, p_int_1, flags=None): # real signature unknown; restored from __doc__
        """ map(self, int, int, flags: QFileDevice.MemoryMapFlags = QFileDevice.NoOptions) -> sip.voidptr """
        pass

    def permissions(self): # real signature unknown; restored from __doc__
        """ permissions(self) -> QFileDevice.Permissions """
        pass

    def pos(self): # real signature unknown; restored from __doc__
        """ pos(self) -> int """
        return 0

    def resize(self, p_int): # real signature unknown; restored from __doc__
        """ resize(self, int) -> bool """
        return False

    def seek(self, p_int): # real signature unknown; restored from __doc__
        """ seek(self, int) -> bool """
        return False

    def setFileTime(self, Union, QDateTime=None, datetime_datetime=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setFileTime(self, Union[QDateTime, datetime.datetime], QFileDevice.FileTime) -> bool """
        pass

    def setPermissions(self, Union, QFileDevice_Permissions=None, QFileDevice_Permission=None): # real signature unknown; restored from __doc__
        """ setPermissions(self, Union[QFileDevice.Permissions, QFileDevice.Permission]) -> bool """
        return False

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def unmap(self, sip_voidptr): # real signature unknown; restored from __doc__
        """ unmap(self, sip.voidptr) -> bool """
        return False

    def unsetError(self): # real signature unknown; restored from __doc__
        """ unsetError(self) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    AbortError = 6
    AutoCloseHandle = 1
    CopyError = 14
    DontCloseHandle = 0
    ExeGroup = 16
    ExeOther = 1
    ExeOwner = 4096
    ExeUser = 256
    FatalError = 3
    FileAccessTime = 0
    FileBirthTime = 1
    FileMetadataChangeTime = 2
    FileModificationTime = 3
    MapPrivateOption = 1
    NoError = 0
    NoOptions = 0
    OpenError = 5
    PermissionsError = 13
    PositionError = 11
    ReadError = 1
    ReadGroup = 64
    ReadOther = 4
    ReadOwner = 16384
    ReadUser = 1024
    RemoveError = 9
    RenameError = 10
    ResizeError = 12
    ResourceError = 4
    TimeOutError = 7
    UnspecifiedError = 8
    WriteError = 2
    WriteGroup = 32
    WriteOther = 2
    WriteOwner = 8192
    WriteUser = 512


