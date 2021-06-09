# encoding: utf-8
# module PyQt5.QtLocation
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtLocation.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QPlaceSearchResult(__sip.simplewrapper):
    """
    QPlaceSearchResult()
    QPlaceSearchResult(QPlaceSearchResult)
    """
    def icon(self): # real signature unknown; restored from __doc__
        """ icon(self) -> QPlaceIcon """
        return QPlaceIcon

    def setIcon(self, QPlaceIcon): # real signature unknown; restored from __doc__
        """ setIcon(self, QPlaceIcon) """
        pass

    def setTitle(self, p_str): # real signature unknown; restored from __doc__
        """ setTitle(self, str) """
        pass

    def title(self): # real signature unknown; restored from __doc__
        """ title(self) -> str """
        return ""

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QPlaceSearchResult.SearchResultType """
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

    def __init__(self, QPlaceSearchResult=None): # real signature unknown; restored from __doc__ with multiple overloads
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


    PlaceResult = 1
    ProposedSearchResult = 2
    UnknownSearchResult = 0
    __hash__ = None


