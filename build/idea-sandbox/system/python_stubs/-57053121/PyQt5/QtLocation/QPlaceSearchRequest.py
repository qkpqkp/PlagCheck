# encoding: utf-8
# module PyQt5.QtLocation
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtLocation.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QPlaceSearchRequest(__sip.simplewrapper):
    """
    QPlaceSearchRequest()
    QPlaceSearchRequest(QPlaceSearchRequest)
    """
    def categories(self): # real signature unknown; restored from __doc__
        """ categories(self) -> List[QPlaceCategory] """
        return []

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def limit(self): # real signature unknown; restored from __doc__
        """ limit(self) -> int """
        return 0

    def recommendationId(self): # real signature unknown; restored from __doc__
        """ recommendationId(self) -> str """
        return ""

    def relevanceHint(self): # real signature unknown; restored from __doc__
        """ relevanceHint(self) -> QPlaceSearchRequest.RelevanceHint """
        pass

    def searchArea(self): # real signature unknown; restored from __doc__
        """ searchArea(self) -> QGeoShape """
        pass

    def searchContext(self): # real signature unknown; restored from __doc__
        """ searchContext(self) -> Any """
        pass

    def searchTerm(self): # real signature unknown; restored from __doc__
        """ searchTerm(self) -> str """
        return ""

    def setCategories(self, Iterable, QPlaceCategory=None): # real signature unknown; restored from __doc__
        """ setCategories(self, Iterable[QPlaceCategory]) """
        pass

    def setCategory(self, QPlaceCategory): # real signature unknown; restored from __doc__
        """ setCategory(self, QPlaceCategory) """
        pass

    def setLimit(self, p_int): # real signature unknown; restored from __doc__
        """ setLimit(self, int) """
        pass

    def setRecommendationId(self, p_str): # real signature unknown; restored from __doc__
        """ setRecommendationId(self, str) """
        pass

    def setRelevanceHint(self, QPlaceSearchRequest_RelevanceHint): # real signature unknown; restored from __doc__
        """ setRelevanceHint(self, QPlaceSearchRequest.RelevanceHint) """
        pass

    def setSearchArea(self, QGeoShape): # real signature unknown; restored from __doc__
        """ setSearchArea(self, QGeoShape) """
        pass

    def setSearchContext(self, Any): # real signature unknown; restored from __doc__
        """ setSearchContext(self, Any) """
        pass

    def setSearchTerm(self, p_str): # real signature unknown; restored from __doc__
        """ setSearchTerm(self, str) """
        pass

    def setVisibilityScope(self, Union, QLocation_VisibilityScope=None, QLocation_Visibility=None): # real signature unknown; restored from __doc__
        """ setVisibilityScope(self, Union[QLocation.VisibilityScope, QLocation.Visibility]) """
        pass

    def visibilityScope(self): # real signature unknown; restored from __doc__
        """ visibilityScope(self) -> QLocation.VisibilityScope """
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

    def __init__(self, QPlaceSearchRequest=None): # real signature unknown; restored from __doc__ with multiple overloads
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


    DistanceHint = 1
    LexicalPlaceNameHint = 2
    UnspecifiedHint = 0
    __hash__ = None


