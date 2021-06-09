# encoding: utf-8
# module PyQt5.QtLocation
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtLocation.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QGeoRoutingManager(__PyQt5_QtCore.QObject):
    # no doc
    def calculateRoute(self, QGeoRouteRequest): # real signature unknown; restored from __doc__
        """ calculateRoute(self, QGeoRouteRequest) -> QGeoRouteReply """
        return QGeoRouteReply

    def error(self, QGeoRouteReply, QGeoRouteReply_Error, errorString=''): # real signature unknown; restored from __doc__
        """ error(self, QGeoRouteReply, QGeoRouteReply.Error, errorString: str = '') [signal] """
        pass

    def finished(self, QGeoRouteReply): # real signature unknown; restored from __doc__
        """ finished(self, QGeoRouteReply) [signal] """
        pass

    def locale(self): # real signature unknown; restored from __doc__
        """ locale(self) -> QLocale """
        pass

    def managerName(self): # real signature unknown; restored from __doc__
        """ managerName(self) -> str """
        return ""

    def managerVersion(self): # real signature unknown; restored from __doc__
        """ managerVersion(self) -> int """
        return 0

    def measurementSystem(self): # real signature unknown; restored from __doc__
        """ measurementSystem(self) -> QLocale.MeasurementSystem """
        pass

    def setLocale(self, QLocale): # real signature unknown; restored from __doc__
        """ setLocale(self, QLocale) """
        pass

    def setMeasurementSystem(self, QLocale_MeasurementSystem): # real signature unknown; restored from __doc__
        """ setMeasurementSystem(self, QLocale.MeasurementSystem) """
        pass

    def supportedFeatureTypes(self): # real signature unknown; restored from __doc__
        """ supportedFeatureTypes(self) -> QGeoRouteRequest.FeatureTypes """
        pass

    def supportedFeatureWeights(self): # real signature unknown; restored from __doc__
        """ supportedFeatureWeights(self) -> QGeoRouteRequest.FeatureWeights """
        pass

    def supportedManeuverDetails(self): # real signature unknown; restored from __doc__
        """ supportedManeuverDetails(self) -> QGeoRouteRequest.ManeuverDetails """
        pass

    def supportedRouteOptimizations(self): # real signature unknown; restored from __doc__
        """ supportedRouteOptimizations(self) -> QGeoRouteRequest.RouteOptimizations """
        pass

    def supportedSegmentDetails(self): # real signature unknown; restored from __doc__
        """ supportedSegmentDetails(self) -> QGeoRouteRequest.SegmentDetails """
        pass

    def supportedTravelModes(self): # real signature unknown; restored from __doc__
        """ supportedTravelModes(self) -> QGeoRouteRequest.TravelModes """
        pass

    def updateRoute(self, QGeoRoute, QGeoCoordinate): # real signature unknown; restored from __doc__
        """ updateRoute(self, QGeoRoute, QGeoCoordinate) -> QGeoRouteReply """
        return QGeoRouteReply

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


