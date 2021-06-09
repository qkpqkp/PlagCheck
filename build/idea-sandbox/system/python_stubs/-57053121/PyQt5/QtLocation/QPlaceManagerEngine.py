# encoding: utf-8
# module PyQt5.QtLocation
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtLocation.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QPlaceManagerEngine(__PyQt5_QtCore.QObject):
    """ QPlaceManagerEngine(Dict[str, Any], parent: QObject = None) """
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

    def childCategories(self, p_str): # real signature unknown; restored from __doc__
        """ childCategories(self, str) -> List[QPlaceCategory] """
        return []

    def childCategoryIds(self, p_str): # real signature unknown; restored from __doc__
        """ childCategoryIds(self, str) -> List[str] """
        return []

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def compatiblePlace(self, QPlace): # real signature unknown; restored from __doc__
        """ compatiblePlace(self, QPlace) -> QPlace """
        return QPlace

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def constructIconUrl(self, QPlaceIcon, QSize): # real signature unknown; restored from __doc__
        """ constructIconUrl(self, QPlaceIcon, QSize) -> QUrl """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dataChanged(self): # real signature unknown; restored from __doc__
        """ dataChanged(self) [signal] """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
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

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def locales(self): # real signature unknown; restored from __doc__
        """ locales(self) -> List[QLocale] """
        return []

    def manager(self): # real signature unknown; restored from __doc__
        """ manager(self) -> QPlaceManager """
        return QPlaceManager

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

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeCategory(self, p_str): # real signature unknown; restored from __doc__
        """ removeCategory(self, str) -> QPlaceIdReply """
        return QPlaceIdReply

    def removePlace(self, p_str): # real signature unknown; restored from __doc__
        """ removePlace(self, str) -> QPlaceIdReply """
        return QPlaceIdReply

    def saveCategory(self, QPlaceCategory, p_str): # real signature unknown; restored from __doc__
        """ saveCategory(self, QPlaceCategory, str) -> QPlaceIdReply """
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

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setLocales(self, Iterable, QLocale=None): # real signature unknown; restored from __doc__
        """ setLocales(self, Iterable[QLocale]) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, Dict, p_str=None, Any=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


