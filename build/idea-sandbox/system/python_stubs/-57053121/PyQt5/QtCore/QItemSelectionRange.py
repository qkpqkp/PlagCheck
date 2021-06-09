# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QItemSelectionRange(__sip.simplewrapper):
    """
    QItemSelectionRange()
    QItemSelectionRange(QItemSelectionRange)
    QItemSelectionRange(QModelIndex, QModelIndex)
    QItemSelectionRange(QModelIndex)
    """
    def bottom(self): # real signature unknown; restored from __doc__
        """ bottom(self) -> int """
        return 0

    def bottomRight(self): # real signature unknown; restored from __doc__
        """ bottomRight(self) -> QPersistentModelIndex """
        return QPersistentModelIndex

    def contains(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        contains(self, QModelIndex) -> bool
        contains(self, int, int, QModelIndex) -> bool
        """
        return False

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> int """
        return 0

    def indexes(self): # real signature unknown; restored from __doc__
        """ indexes(self) -> List[QModelIndex] """
        return []

    def intersected(self, QItemSelectionRange): # real signature unknown; restored from __doc__
        """ intersected(self, QItemSelectionRange) -> QItemSelectionRange """
        return QItemSelectionRange

    def intersects(self, QItemSelectionRange): # real signature unknown; restored from __doc__
        """ intersects(self, QItemSelectionRange) -> bool """
        return False

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def left(self): # real signature unknown; restored from __doc__
        """ left(self) -> int """
        return 0

    def model(self): # real signature unknown; restored from __doc__
        """ model(self) -> QAbstractItemModel """
        return QAbstractItemModel

    def parent(self): # real signature unknown; restored from __doc__
        """ parent(self) -> QModelIndex """
        return QModelIndex

    def right(self): # real signature unknown; restored from __doc__
        """ right(self) -> int """
        return 0

    def swap(self, QItemSelectionRange): # real signature unknown; restored from __doc__
        """ swap(self, QItemSelectionRange) """
        pass

    def top(self): # real signature unknown; restored from __doc__
        """ top(self) -> int """
        return 0

    def topLeft(self): # real signature unknown; restored from __doc__
        """ topLeft(self) -> QPersistentModelIndex """
        return QPersistentModelIndex

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> int """
        return 0

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
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



