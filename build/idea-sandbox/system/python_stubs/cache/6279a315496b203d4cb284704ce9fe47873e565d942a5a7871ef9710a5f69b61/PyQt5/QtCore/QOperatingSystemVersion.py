# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QOperatingSystemVersion(__sip.simplewrapper):
    """
    QOperatingSystemVersion(QOperatingSystemVersion.OSType, int, vminor: int = -1, vmicro: int = -1)
    QOperatingSystemVersion(QOperatingSystemVersion)
    """
    def current(self): # real signature unknown; restored from __doc__
        """ current() -> QOperatingSystemVersion """
        return QOperatingSystemVersion

    def currentType(self): # real signature unknown; restored from __doc__
        """ currentType() -> QOperatingSystemVersion.OSType """
        pass

    def majorVersion(self): # real signature unknown; restored from __doc__
        """ majorVersion(self) -> int """
        return 0

    def microVersion(self): # real signature unknown; restored from __doc__
        """ microVersion(self) -> int """
        return 0

    def minorVersion(self): # real signature unknown; restored from __doc__
        """ minorVersion(self) -> int """
        return 0

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def segmentCount(self): # real signature unknown; restored from __doc__
        """ segmentCount(self) -> int """
        return 0

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QOperatingSystemVersion.OSType """
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


    Android = 6
    IOS = 3
    MacOS = 2
    TvOS = 4
    Unknown = 0
    WatchOS = 5
    Windows = 1
    __hash__ = None


