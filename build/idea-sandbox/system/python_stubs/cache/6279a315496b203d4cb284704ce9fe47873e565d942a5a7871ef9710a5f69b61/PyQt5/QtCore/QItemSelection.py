# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QItemSelection(__sip.simplewrapper):
    """
    QItemSelection()
    QItemSelection(QModelIndex, QModelIndex)
    QItemSelection(QItemSelection)
    """
    def append(self, QItemSelectionRange): # real signature unknown; restored from __doc__
        """ append(self, QItemSelectionRange) """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def contains(self, QModelIndex): # real signature unknown; restored from __doc__
        """ contains(self, QModelIndex) -> bool """
        return False

    def count(self, QItemSelectionRange=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        count(self, QItemSelectionRange) -> int
        count(self) -> int
        """
        return 0

    def first(self): # real signature unknown; restored from __doc__
        """ first(self) -> QItemSelectionRange """
        return QItemSelectionRange

    def indexes(self): # real signature unknown; restored from __doc__
        """ indexes(self) -> List[QModelIndex] """
        return []

    def indexOf(self, QItemSelectionRange, from_=0): # real signature unknown; restored from __doc__
        """ indexOf(self, QItemSelectionRange, from_: int = 0) -> int """
        return 0

    def insert(self, p_int, QItemSelectionRange): # real signature unknown; restored from __doc__
        """ insert(self, int, QItemSelectionRange) """
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def last(self): # real signature unknown; restored from __doc__
        """ last(self) -> QItemSelectionRange """
        return QItemSelectionRange

    def lastIndexOf(self, QItemSelectionRange, from_=-1): # real signature unknown; restored from __doc__
        """ lastIndexOf(self, QItemSelectionRange, from_: int = -1) -> int """
        return 0

    def merge(self, QItemSelection, Union, QItemSelectionModel_SelectionFlags=None, QItemSelectionModel_SelectionFlag=None): # real signature unknown; restored from __doc__
        """ merge(self, QItemSelection, Union[QItemSelectionModel.SelectionFlags, QItemSelectionModel.SelectionFlag]) """
        pass

    def move(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ move(self, int, int) """
        pass

    def prepend(self, QItemSelectionRange): # real signature unknown; restored from __doc__
        """ prepend(self, QItemSelectionRange) """
        pass

    def removeAll(self, QItemSelectionRange): # real signature unknown; restored from __doc__
        """ removeAll(self, QItemSelectionRange) -> int """
        return 0

    def removeAt(self, p_int): # real signature unknown; restored from __doc__
        """ removeAt(self, int) """
        pass

    def replace(self, p_int, QItemSelectionRange): # real signature unknown; restored from __doc__
        """ replace(self, int, QItemSelectionRange) """
        pass

    def select(self, QModelIndex, QModelIndex_1): # real signature unknown; restored from __doc__
        """ select(self, QModelIndex, QModelIndex) """
        pass

    def split(self, QItemSelectionRange, QItemSelectionRange_1, QItemSelection): # real signature unknown; restored from __doc__
        """ split(QItemSelectionRange, QItemSelectionRange, QItemSelection) """
        pass

    def swap(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ swap(self, int, int) """
        pass

    def takeAt(self, p_int): # real signature unknown; restored from __doc__
        """ takeAt(self, int) -> QItemSelectionRange """
        return QItemSelectionRange

    def takeFirst(self): # real signature unknown; restored from __doc__
        """ takeFirst(self) -> QItemSelectionRange """
        return QItemSelectionRange

    def takeLast(self): # real signature unknown; restored from __doc__
        """ takeLast(self) -> QItemSelectionRange """
        return QItemSelectionRange

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __iadd__(self, *args, **kwargs): # real signature unknown
        """ Implement self+=value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
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

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __hash__ = None


