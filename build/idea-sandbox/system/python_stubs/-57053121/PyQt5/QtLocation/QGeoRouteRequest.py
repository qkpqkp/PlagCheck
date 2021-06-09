# encoding: utf-8
# module PyQt5.QtLocation
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtLocation.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QGeoRouteRequest(__sip.simplewrapper):
    """
    QGeoRouteRequest(waypoints: Iterable[QGeoCoordinate] = [])
    QGeoRouteRequest(QGeoCoordinate, QGeoCoordinate)
    QGeoRouteRequest(QGeoRouteRequest)
    """
    def excludeAreas(self): # real signature unknown; restored from __doc__
        """ excludeAreas(self) -> List[QGeoRectangle] """
        return []

    def extraParameters(self): # real signature unknown; restored from __doc__
        """ extraParameters(self) -> Dict[str, Any] """
        return {}

    def featureTypes(self): # real signature unknown; restored from __doc__
        """ featureTypes(self) -> List[QGeoRouteRequest.FeatureType] """
        return []

    def featureWeight(self, QGeoRouteRequest_FeatureType): # real signature unknown; restored from __doc__
        """ featureWeight(self, QGeoRouteRequest.FeatureType) -> QGeoRouteRequest.FeatureWeight """
        pass

    def maneuverDetail(self): # real signature unknown; restored from __doc__
        """ maneuverDetail(self) -> QGeoRouteRequest.ManeuverDetail """
        pass

    def numberAlternativeRoutes(self): # real signature unknown; restored from __doc__
        """ numberAlternativeRoutes(self) -> int """
        return 0

    def routeOptimization(self): # real signature unknown; restored from __doc__
        """ routeOptimization(self) -> QGeoRouteRequest.RouteOptimizations """
        pass

    def segmentDetail(self): # real signature unknown; restored from __doc__
        """ segmentDetail(self) -> QGeoRouteRequest.SegmentDetail """
        pass

    def setExcludeAreas(self, Iterable, QGeoRectangle=None): # real signature unknown; restored from __doc__
        """ setExcludeAreas(self, Iterable[QGeoRectangle]) """
        pass

    def setExtraParameters(self, Dict, p_str=None, Any=None): # real signature unknown; restored from __doc__
        """ setExtraParameters(self, Dict[str, Any]) """
        pass

    def setFeatureWeight(self, QGeoRouteRequest_FeatureType, QGeoRouteRequest_FeatureWeight): # real signature unknown; restored from __doc__
        """ setFeatureWeight(self, QGeoRouteRequest.FeatureType, QGeoRouteRequest.FeatureWeight) """
        pass

    def setManeuverDetail(self, QGeoRouteRequest_ManeuverDetail): # real signature unknown; restored from __doc__
        """ setManeuverDetail(self, QGeoRouteRequest.ManeuverDetail) """
        pass

    def setNumberAlternativeRoutes(self, p_int): # real signature unknown; restored from __doc__
        """ setNumberAlternativeRoutes(self, int) """
        pass

    def setRouteOptimization(self, Union, QGeoRouteRequest_RouteOptimizations=None, QGeoRouteRequest_RouteOptimization=None): # real signature unknown; restored from __doc__
        """ setRouteOptimization(self, Union[QGeoRouteRequest.RouteOptimizations, QGeoRouteRequest.RouteOptimization]) """
        pass

    def setSegmentDetail(self, QGeoRouteRequest_SegmentDetail): # real signature unknown; restored from __doc__
        """ setSegmentDetail(self, QGeoRouteRequest.SegmentDetail) """
        pass

    def setTravelModes(self, Union, QGeoRouteRequest_TravelModes=None, QGeoRouteRequest_TravelMode=None): # real signature unknown; restored from __doc__
        """ setTravelModes(self, Union[QGeoRouteRequest.TravelModes, QGeoRouteRequest.TravelMode]) """
        pass

    def setWaypoints(self, Iterable, QGeoCoordinate=None): # real signature unknown; restored from __doc__
        """ setWaypoints(self, Iterable[QGeoCoordinate]) """
        pass

    def setWaypointsMetadata(self, Iterable, Dict=None, p_str=None, Any=None): # real signature unknown; restored from __doc__
        """ setWaypointsMetadata(self, Iterable[Dict[str, Any]]) """
        pass

    def travelModes(self): # real signature unknown; restored from __doc__
        """ travelModes(self) -> QGeoRouteRequest.TravelModes """
        pass

    def waypoints(self): # real signature unknown; restored from __doc__
        """ waypoints(self) -> List[QGeoCoordinate] """
        return []

    def waypointsMetadata(self): # real signature unknown; restored from __doc__
        """ waypointsMetadata(self) -> List[Dict[str, Any]] """
        return []

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


    AvoidFeatureWeight = 4
    BasicManeuvers = 1
    BasicSegmentData = 1
    BicycleTravel = 4
    CarTravel = 1
    DirtRoadFeature = 32
    DisallowFeatureWeight = 8
    FastestRoute = 2
    FerryFeature = 8
    HighwayFeature = 2
    MostEconomicRoute = 4
    MostScenicRoute = 8
    MotorPoolLaneFeature = 128
    NeutralFeatureWeight = 0
    NoFeature = 0
    NoManeuvers = 0
    NoSegmentData = 0
    ParksFeature = 64
    PedestrianTravel = 2
    PreferFeatureWeight = 1
    PublicTransitFeature = 4
    PublicTransitTravel = 8
    RequireFeatureWeight = 2
    ShortestRoute = 1
    TollFeature = 1
    TrafficFeature = 256
    TruckTravel = 16
    TunnelFeature = 16
    __hash__ = None


