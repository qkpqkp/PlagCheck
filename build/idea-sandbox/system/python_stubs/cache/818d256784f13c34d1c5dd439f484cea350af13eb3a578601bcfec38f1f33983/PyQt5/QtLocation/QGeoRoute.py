# encoding: utf-8
# module PyQt5.QtLocation
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtLocation.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QGeoRoute(__sip.simplewrapper):
    """
    QGeoRoute()
    QGeoRoute(QGeoRoute)
    """
    def bounds(self): # real signature unknown; restored from __doc__
        """ bounds(self) -> QGeoRectangle """
        pass

    def distance(self): # real signature unknown; restored from __doc__
        """ distance(self) -> float """
        return 0.0

    def firstRouteSegment(self): # real signature unknown; restored from __doc__
        """ firstRouteSegment(self) -> QGeoRouteSegment """
        return QGeoRouteSegment

    def path(self): # real signature unknown; restored from __doc__
        """ path(self) -> List[QGeoCoordinate] """
        return []

    def request(self): # real signature unknown; restored from __doc__
        """ request(self) -> QGeoRouteRequest """
        return QGeoRouteRequest

    def routeId(self): # real signature unknown; restored from __doc__
        """ routeId(self) -> str """
        return ""

    def routeLegs(self): # real signature unknown; restored from __doc__
        """ routeLegs(self) -> List[QGeoRouteLeg] """
        return []

    def setBounds(self, QGeoRectangle): # real signature unknown; restored from __doc__
        """ setBounds(self, QGeoRectangle) """
        pass

    def setDistance(self, p_float): # real signature unknown; restored from __doc__
        """ setDistance(self, float) """
        pass

    def setFirstRouteSegment(self, QGeoRouteSegment): # real signature unknown; restored from __doc__
        """ setFirstRouteSegment(self, QGeoRouteSegment) """
        pass

    def setPath(self, Iterable, QGeoCoordinate=None): # real signature unknown; restored from __doc__
        """ setPath(self, Iterable[QGeoCoordinate]) """
        pass

    def setRequest(self, QGeoRouteRequest): # real signature unknown; restored from __doc__
        """ setRequest(self, QGeoRouteRequest) """
        pass

    def setRouteId(self, p_str): # real signature unknown; restored from __doc__
        """ setRouteId(self, str) """
        pass

    def setRouteLegs(self, Iterable, QGeoRouteLeg=None): # real signature unknown; restored from __doc__
        """ setRouteLegs(self, Iterable[QGeoRouteLeg]) """
        pass

    def setTravelMode(self, QGeoRouteRequest_TravelMode): # real signature unknown; restored from __doc__
        """ setTravelMode(self, QGeoRouteRequest.TravelMode) """
        pass

    def setTravelTime(self, p_int): # real signature unknown; restored from __doc__
        """ setTravelTime(self, int) """
        pass

    def travelMode(self): # real signature unknown; restored from __doc__
        """ travelMode(self) -> QGeoRouteRequest.TravelMode """
        pass

    def travelTime(self): # real signature unknown; restored from __doc__
        """ travelTime(self) -> int """
        return 0

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, QGeoRoute=None): # real signature unknown; restored from __doc__ with multiple overloads
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


