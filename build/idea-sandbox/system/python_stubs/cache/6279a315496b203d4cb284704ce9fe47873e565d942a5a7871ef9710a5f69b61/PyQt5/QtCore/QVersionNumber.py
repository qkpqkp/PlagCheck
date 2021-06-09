# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QVersionNumber(__sip.simplewrapper):
    """
    QVersionNumber()
    QVersionNumber(Iterable[int])
    QVersionNumber(int)
    QVersionNumber(int, int)
    QVersionNumber(int, int, int)
    QVersionNumber(QVersionNumber)
    """
    def commonPrefix(self, QVersionNumber, QVersionNumber_1): # real signature unknown; restored from __doc__
        """ commonPrefix(QVersionNumber, QVersionNumber) -> QVersionNumber """
        return QVersionNumber

    def compare(self, QVersionNumber, QVersionNumber_1): # real signature unknown; restored from __doc__
        """ compare(QVersionNumber, QVersionNumber) -> int """
        return 0

    def fromString(self, p_str): # real signature unknown; restored from __doc__
        """ fromString(str) -> Tuple[QVersionNumber, int] """
        pass

    def isNormalized(self): # real signature unknown; restored from __doc__
        """ isNormalized(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isPrefixOf(self, QVersionNumber): # real signature unknown; restored from __doc__
        """ isPrefixOf(self, QVersionNumber) -> bool """
        return False

    def majorVersion(self): # real signature unknown; restored from __doc__
        """ majorVersion(self) -> int """
        return 0

    def microVersion(self): # real signature unknown; restored from __doc__
        """ microVersion(self) -> int """
        return 0

    def minorVersion(self): # real signature unknown; restored from __doc__
        """ minorVersion(self) -> int """
        return 0

    def normalized(self): # real signature unknown; restored from __doc__
        """ normalized(self) -> QVersionNumber """
        return QVersionNumber

    def segmentAt(self, p_int): # real signature unknown; restored from __doc__
        """ segmentAt(self, int) -> int """
        return 0

    def segmentCount(self): # real signature unknown; restored from __doc__
        """ segmentCount(self) -> int """
        return 0

    def segments(self): # real signature unknown; restored from __doc__
        """ segments(self) -> List[int] """
        return []

    def toString(self): # real signature unknown; restored from __doc__
        """ toString(self) -> str """
        return ""

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



