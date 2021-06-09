# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QPixmapCache(__sip.simplewrapper):
    """
    QPixmapCache()
    QPixmapCache(QPixmapCache)
    """
    def cacheLimit(self): # real signature unknown; restored from __doc__
        """ cacheLimit() -> int """
        return 0

    def clear(self): # real signature unknown; restored from __doc__
        """ clear() """
        pass

    def find(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        find(str) -> QPixmap
        find(QPixmapCache.Key) -> QPixmap
        """
        return QPixmap

    def insert(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        insert(str, QPixmap) -> bool
        insert(QPixmap) -> QPixmapCache.Key
        """
        return False

    def remove(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        remove(str)
        remove(QPixmapCache.Key)
        """
        pass

    def replace(self, QPixmapCache_Key, QPixmap): # real signature unknown; restored from __doc__
        """ replace(QPixmapCache.Key, QPixmap) -> bool """
        return False

    def setCacheLimit(self, p_int): # real signature unknown; restored from __doc__
        """ setCacheLimit(int) """
        pass

    def __init__(self, QPixmapCache=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""




