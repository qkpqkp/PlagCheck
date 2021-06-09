# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QDirIterator(__sip.simplewrapper):
    """
    QDirIterator(QDir, flags: QDirIterator.IteratorFlags = QDirIterator.NoIteratorFlags)
    QDirIterator(str, flags: QDirIterator.IteratorFlags = QDirIterator.NoIteratorFlags)
    QDirIterator(str, QDir.Filters, flags: QDirIterator.IteratorFlags = QDirIterator.NoIteratorFlags)
    QDirIterator(str, Iterable[str], filters: QDir.Filters = QDir.NoFilter, flags: QDirIterator.IteratorFlags = QDirIterator.NoIteratorFlags)
    """
    def fileInfo(self): # real signature unknown; restored from __doc__
        """ fileInfo(self) -> QFileInfo """
        return QFileInfo

    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def filePath(self): # real signature unknown; restored from __doc__
        """ filePath(self) -> str """
        return ""

    def hasNext(self): # real signature unknown; restored from __doc__
        """ hasNext(self) -> bool """
        return False

    def next(self): # real signature unknown; restored from __doc__
        """ next(self) -> str """
        return ""

    def path(self): # real signature unknown; restored from __doc__
        """ path(self) -> str """
        return ""

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    FollowSymlinks = 1
    NoIteratorFlags = 0
    Subdirectories = 2


