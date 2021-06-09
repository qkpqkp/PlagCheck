# encoding: utf-8
# module PyQt5.QtLocation
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtLocation.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QPlaceManager(__PyQt5_QtCore.QObject):
    # no doc
    def category(self, p_str): # real signature unknown; restored from __doc__
        """ category(self, str) -> QPlaceCategory """
        return QPlaceCategory

    def categoryAdded(self, QPlaceCategory, p_str): # real signature unknown; restored from __doc__
        """ categoryAdded(self, QPlaceCategory, str) [signal] """
        pass

    def categoryRemoved(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ categoryRemoved(self, str, str) [signal] """
        pass

    def categoryUpdated(self, QPlaceCategory, p_str): # real signature unknown; restored from __doc__
        """ categoryUpdated(self, QPlaceCategory, str) [signal] """
        pass

    def childCategories(self, parentId=''): # real signature unknown; restored from __doc__
        """ childCategories(self, parentId: str = '') -> List[QPlaceCategory] """
        return []

    def childCategoryIds(self, parentId=''): # real signature unknown; restored from __doc__
        """ childCategoryIds(self, parentId: str = '') -> List[str] """
        return []

    def compatiblePlace(self, QPlace): # real signature unknown; restored from __doc__
        """ compatiblePlace(self, QPlace) -> QPlace """
        return QPlace

    def dataChanged(self): # real signature unknown; restored from __doc__
        """ dataChanged(self) [signal] """
        pass

    def error(self, QPlaceReply, QPlaceReply_Error, errorString=''): # real signature unknown; restored from __doc__
        """ error(self, QPlaceReply, QPlaceReply.Error, errorString: str = '') [signal] """
        pass

    def finished(self, QPlaceReply): # real signature unknown; restored from __doc__
        """ finished(self, QPlaceReply) [signal] """
        pass

    def getPlaceContent(self, QPlaceContentRequest): # real signature unknown; restored from __doc__
        """ getPlaceContent(self, QPlaceContentRequest) -> QPlaceContentReply """
        return QPlaceContentReply

    def getPlaceDetails(self, p_str): # real signature unknown; restored from __doc__
        """ getPlaceDetails(self, str) -> QPlaceDetailsReply """
        return QPlaceDetailsReply

    def initializeCategories(self): # real signature unknown; restored from __doc__
        """ initializeCategories(self) -> QPlaceReply """
        return QPlaceReply

    def locales(self): # real signature unknown; restored from __doc__
        """ locales(self) -> List[QLocale] """
        return []

    def managerName(self): # real signature unknown; restored from __doc__
        """ managerName(self) -> str """
        return ""

    def managerVersion(self): # real signature unknown; restored from __doc__
        """ managerVersion(self) -> int """
        return 0

    def matchingPlaces(self, QPlaceMatchRequest): # real signature unknown; restored from __doc__
        """ matchingPlaces(self, QPlaceMatchRequest) -> QPlaceMatchReply """
        return QPlaceMatchReply

    def parentCategoryId(self, p_str): # real signature unknown; restored from __doc__
        """ parentCategoryId(self, str) -> str """
        return ""

    def placeAdded(self, p_str): # real signature unknown; restored from __doc__
        """ placeAdded(self, str) [signal] """
        pass

    def placeRemoved(self, p_str): # real signature unknown; restored from __doc__
        """ placeRemoved(self, str) [signal] """
        pass

    def placeUpdated(self, p_str): # real signature unknown; restored from __doc__
        """ placeUpdated(self, str) [signal] """
        pass

    def removeCategory(self, p_str): # real signature unknown; restored from __doc__
        """ removeCategory(self, str) -> QPlaceIdReply """
        return QPlaceIdReply

    def removePlace(self, p_str): # real signature unknown; restored from __doc__
        """ removePlace(self, str) -> QPlaceIdReply """
        return QPlaceIdReply

    def saveCategory(self, QPlaceCategory, parentId=''): # real signature unknown; restored from __doc__
        """ saveCategory(self, QPlaceCategory, parentId: str = '') -> QPlaceIdReply """
        return QPlaceIdReply

    def savePlace(self, QPlace): # real signature unknown; restored from __doc__
        """ savePlace(self, QPlace) -> QPlaceIdReply """
        return QPlaceIdReply

    def search(self, QPlaceSearchRequest): # real signature unknown; restored from __doc__
        """ search(self, QPlaceSearchRequest) -> QPlaceSearchReply """
        return QPlaceSearchReply

    def searchSuggestions(self, QPlaceSearchRequest): # real signature unknown; restored from __doc__
        """ searchSuggestions(self, QPlaceSearchRequest) -> QPlaceSearchSuggestionReply """
        return QPlaceSearchSuggestionReply

    def setLocale(self, QLocale): # real signature unknown; restored from __doc__
        """ setLocale(self, QLocale) """
        pass

    def setLocales(self, Iterable, QLocale=None): # real signature unknown; restored from __doc__
        """ setLocales(self, Iterable[QLocale]) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


