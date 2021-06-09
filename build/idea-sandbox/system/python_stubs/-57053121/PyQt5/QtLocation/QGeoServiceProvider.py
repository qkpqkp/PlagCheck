# encoding: utf-8
# module PyQt5.QtLocation
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtLocation.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QGeoServiceProvider(__PyQt5_QtCore.QObject):
    """ QGeoServiceProvider(str, parameters: Dict[str, Any] = {}, allowExperimental: bool = False) """
    def availableServiceProviders(self): # real signature unknown; restored from __doc__
        """ availableServiceProviders() -> List[str] """
        return []

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> QGeoServiceProvider.Error """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def geocodingFeatures(self): # real signature unknown; restored from __doc__
        """ geocodingFeatures(self) -> QGeoServiceProvider.GeocodingFeatures """
        pass

    def geocodingManager(self): # real signature unknown; restored from __doc__
        """ geocodingManager(self) -> QGeoCodingManager """
        return QGeoCodingManager

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def mappingFeatures(self): # real signature unknown; restored from __doc__
        """ mappingFeatures(self) -> QGeoServiceProvider.MappingFeatures """
        pass

    def navigationFeatures(self): # real signature unknown; restored from __doc__
        """ navigationFeatures(self) -> QGeoServiceProvider.NavigationFeatures """
        pass

    def navigationManager(self): # real signature unknown; restored from __doc__
        """ navigationManager(self) -> QNavigationManager """
        return QNavigationManager

    def placeManager(self): # real signature unknown; restored from __doc__
        """ placeManager(self) -> QPlaceManager """
        return QPlaceManager

    def placesFeatures(self): # real signature unknown; restored from __doc__
        """ placesFeatures(self) -> QGeoServiceProvider.PlacesFeatures """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def routingFeatures(self): # real signature unknown; restored from __doc__
        """ routingFeatures(self) -> QGeoServiceProvider.RoutingFeatures """
        pass

    def routingManager(self): # real signature unknown; restored from __doc__
        """ routingManager(self) -> QGeoRoutingManager """
        return QGeoRoutingManager

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAllowExperimental(self, bool): # real signature unknown; restored from __doc__
        """ setAllowExperimental(self, bool) """
        pass

    def setLocale(self, QLocale): # real signature unknown; restored from __doc__
        """ setLocale(self, QLocale) """
        pass

    def setParameters(self, Dict, p_str=None, Any=None): # real signature unknown; restored from __doc__
        """ setParameters(self, Dict[str, Any]) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, p_str, parameters, p_str=None, Any=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    AlternativeRoutesFeature = 16
    AnyGeocodingFeatures = -1
    AnyMappingFeatures = -1
    AnyNavigationFeatures = -1
    AnyPlacesFeatures = -1
    AnyRoutingFeatures = -1
    ConnectionError = 4
    ExcludeAreasRoutingFeature = 32
    LoaderError = 5
    LocalizedGeocodingFeature = 8
    LocalizedMappingFeature = 4
    LocalizedPlacesFeature = 256
    LocalizedRoutingFeature = 4
    MissingRequiredParameterError = 3
    NoError = 0
    NoGeocodingFeatures = 0
    NoMappingFeatures = 0
    NoNavigationFeatures = 0
    NoPlacesFeatures = 0
    NoRoutingFeatures = 0
    NotificationsFeature = 512
    NotSupportedError = 1
    OfflineGeocodingFeature = 2
    OfflineMappingFeature = 2
    OfflineNavigationFeature = 2
    OfflinePlacesFeature = 2
    OfflineRoutingFeature = 2
    OnlineGeocodingFeature = 1
    OnlineMappingFeature = 1
    OnlineNavigationFeature = 1
    OnlinePlacesFeature = 1
    OnlineRoutingFeature = 1
    PlaceMatchingFeature = 1024
    PlaceRecommendationsFeature = 64
    RemoveCategoryFeature = 32
    RemovePlaceFeature = 8
    ReverseGeocodingFeature = 4
    RouteUpdatesFeature = 8
    SaveCategoryFeature = 16
    SavePlaceFeature = 4
    SearchSuggestionsFeature = 128
    UnknownParameterError = 2


