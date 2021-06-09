# encoding: utf-8
# module PyQt5.QtLocation
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtLocation.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QGeoRouteSegment(__sip.simplewrapper):
    """
    QGeoRouteSegment()
    QGeoRouteSegment(QGeoRouteSegment)
    """
    def distance(self): # real signature unknown; restored from __doc__
        """ distance(self) -> float """
        return 0.0

    def isLegLastSegment(self): # real signature unknown; restored from __doc__
        """ isLegLastSegment(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def maneuver(self): # real signature unknown; restored from __doc__
        """ maneuver(self) -> QGeoManeuver """
        return QGeoManeuver

    def nextRouteSegment(self): # real signature unknown; restored from __doc__
        """ nextRouteSegment(self) -> QGeoRouteSegment """
        return QGeoRouteSegment

    def path(self): # real signature unknown; restored from __doc__
        """ path(self) -> List[QGeoCoordinate] """
        return []

    def setDistance(self, p_float): # real signature unknown; restored from __doc__
        """ setDistance(self, float) """
        pass

    def setManeuver(self, QGeoManeuver): # real signature unknown; restored from __doc__
        """ setManeuver(self, QGeoManeuver) """
        pass

    def setNextRouteSegment(self, QGeoRouteSegment): # real signature unknown; restored from __doc__
        """ setNextRouteSegment(self, QGeoRouteSegment) """
        pass

    def setPath(self, Iterable, QGeoCoordinate=None): # real signature unknown; restored from __doc__
        """ setPath(self, Iterable[QGeoCoordinate]) """
        pass

    def setTravelTime(self, p_int): # real signature unknown; restored from __doc__
        """ setTravelTime(self, int) """
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

    def __init__(self, QGeoRouteSegment=None): # real signature unknown; restored from __doc__ with multiple overloads
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


