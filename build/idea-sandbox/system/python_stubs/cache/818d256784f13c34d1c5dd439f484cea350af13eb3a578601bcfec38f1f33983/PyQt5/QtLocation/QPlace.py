# encoding: utf-8
# module PyQt5.QtLocation
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtLocation.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QPlace(__sip.simplewrapper):
    """
    QPlace()
    QPlace(QPlace)
    """
    def appendContactDetail(self, p_str, QPlaceContactDetail): # real signature unknown; restored from __doc__
        """ appendContactDetail(self, str, QPlaceContactDetail) """
        pass

    def attribution(self): # real signature unknown; restored from __doc__
        """ attribution(self) -> str """
        return ""

    def categories(self): # real signature unknown; restored from __doc__
        """ categories(self) -> List[QPlaceCategory] """
        return []

    def contactDetails(self, p_str): # real signature unknown; restored from __doc__
        """ contactDetails(self, str) -> List[QPlaceContactDetail] """
        return []

    def contactTypes(self): # real signature unknown; restored from __doc__
        """ contactTypes(self) -> List[str] """
        return []

    def content(self, QPlaceContent_Type): # real signature unknown; restored from __doc__
        """ content(self, QPlaceContent.Type) -> Dict[int, QPlaceContent] """
        return {}

    def detailsFetched(self): # real signature unknown; restored from __doc__
        """ detailsFetched(self) -> bool """
        return False

    def extendedAttribute(self, p_str): # real signature unknown; restored from __doc__
        """ extendedAttribute(self, str) -> QPlaceAttribute """
        return QPlaceAttribute

    def extendedAttributeTypes(self): # real signature unknown; restored from __doc__
        """ extendedAttributeTypes(self) -> List[str] """
        return []

    def icon(self): # real signature unknown; restored from __doc__
        """ icon(self) -> QPlaceIcon """
        return QPlaceIcon

    def insertContent(self, QPlaceContent_Type, Dict, p_int=None, QPlaceContent=None): # real signature unknown; restored from __doc__
        """ insertContent(self, QPlaceContent.Type, Dict[int, QPlaceContent]) """
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def location(self): # real signature unknown; restored from __doc__
        """ location(self) -> QGeoLocation """
        pass

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def placeId(self): # real signature unknown; restored from __doc__
        """ placeId(self) -> str """
        return ""

    def primaryEmail(self): # real signature unknown; restored from __doc__
        """ primaryEmail(self) -> str """
        return ""

    def primaryFax(self): # real signature unknown; restored from __doc__
        """ primaryFax(self) -> str """
        return ""

    def primaryPhone(self): # real signature unknown; restored from __doc__
        """ primaryPhone(self) -> str """
        return ""

    def primaryWebsite(self): # real signature unknown; restored from __doc__
        """ primaryWebsite(self) -> QUrl """
        pass

    def ratings(self): # real signature unknown; restored from __doc__
        """ ratings(self) -> QPlaceRatings """
        return QPlaceRatings

    def removeContactDetails(self, p_str): # real signature unknown; restored from __doc__
        """ removeContactDetails(self, str) """
        pass

    def removeExtendedAttribute(self, p_str): # real signature unknown; restored from __doc__
        """ removeExtendedAttribute(self, str) """
        pass

    def setAttribution(self, p_str): # real signature unknown; restored from __doc__
        """ setAttribution(self, str) """
        pass

    def setCategories(self, Iterable, QPlaceCategory=None): # real signature unknown; restored from __doc__
        """ setCategories(self, Iterable[QPlaceCategory]) """
        pass

    def setCategory(self, QPlaceCategory): # real signature unknown; restored from __doc__
        """ setCategory(self, QPlaceCategory) """
        pass

    def setContactDetails(self, p_str, Iterable, QPlaceContactDetail=None): # real signature unknown; restored from __doc__
        """ setContactDetails(self, str, Iterable[QPlaceContactDetail]) """
        pass

    def setContent(self, QPlaceContent_Type, Dict, p_int=None, QPlaceContent=None): # real signature unknown; restored from __doc__
        """ setContent(self, QPlaceContent.Type, Dict[int, QPlaceContent]) """
        pass

    def setDetailsFetched(self, bool): # real signature unknown; restored from __doc__
        """ setDetailsFetched(self, bool) """
        pass

    def setExtendedAttribute(self, p_str, QPlaceAttribute): # real signature unknown; restored from __doc__
        """ setExtendedAttribute(self, str, QPlaceAttribute) """
        pass

    def setIcon(self, QPlaceIcon): # real signature unknown; restored from __doc__
        """ setIcon(self, QPlaceIcon) """
        pass

    def setLocation(self, QGeoLocation): # real signature unknown; restored from __doc__
        """ setLocation(self, QGeoLocation) """
        pass

    def setName(self, p_str): # real signature unknown; restored from __doc__
        """ setName(self, str) """
        pass

    def setPlaceId(self, p_str): # real signature unknown; restored from __doc__
        """ setPlaceId(self, str) """
        pass

    def setRatings(self, QPlaceRatings): # real signature unknown; restored from __doc__
        """ setRatings(self, QPlaceRatings) """
        pass

    def setSupplier(self, QPlaceSupplier): # real signature unknown; restored from __doc__
        """ setSupplier(self, QPlaceSupplier) """
        pass

    def setTotalContentCount(self, QPlaceContent_Type, p_int): # real signature unknown; restored from __doc__
        """ setTotalContentCount(self, QPlaceContent.Type, int) """
        pass

    def setVisibility(self, QLocation_Visibility): # real signature unknown; restored from __doc__
        """ setVisibility(self, QLocation.Visibility) """
        pass

    def supplier(self): # real signature unknown; restored from __doc__
        """ supplier(self) -> QPlaceSupplier """
        return QPlaceSupplier

    def totalContentCount(self, QPlaceContent_Type): # real signature unknown; restored from __doc__
        """ totalContentCount(self, QPlaceContent.Type) -> int """
        return 0

    def visibility(self): # real signature unknown; restored from __doc__
        """ visibility(self) -> QLocation.Visibility """
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

    def __init__(self, QPlace=None): # real signature unknown; restored from __doc__ with multiple overloads
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


