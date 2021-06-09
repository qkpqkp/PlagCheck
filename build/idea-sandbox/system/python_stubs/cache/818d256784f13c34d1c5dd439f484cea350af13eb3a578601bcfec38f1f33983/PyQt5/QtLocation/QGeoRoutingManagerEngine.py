# encoding: utf-8
# module PyQt5.QtLocation
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtLocation.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QGeoRoutingManagerEngine(__PyQt5_QtCore.QObject):
    """ QGeoRoutingManagerEngine(Dict[str, Any], parent: QObject = None) """
    def calculateRoute(self, QGeoRouteRequest): # real signature unknown; restored from __doc__
        """ calculateRoute(self, QGeoRouteRequest) -> QGeoRouteReply """
        return QGeoRouteReply

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, QGeoRouteReply, QGeoRouteReply_Error, errorString=''): # real signature unknown; restored from __doc__
        """ error(self, QGeoRouteReply, QGeoRouteReply.Error, errorString: str = '') [signal] """
        pass

    def finished(self, QGeoRouteReply): # real signature unknown; restored from __doc__
        """ finished(self, QGeoRouteReply) [signal] """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
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

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setLocale(self, QLocale): # real signature unknown; restored from __doc__
        """ setLocale(self, QLocale) """
        pass

    def setMeasurementSystem(self, QLocale_MeasurementSystem): # real signature unknown; restored from __doc__
        """ setMeasurementSystem(self, QLocale.MeasurementSystem) """
        pass

    def setSupportedFeatureTypes(self, Union, QGeoRouteRequest_FeatureTypes=None, QGeoRouteRequest_FeatureType=None): # real signature unknown; restored from __doc__
        """ setSupportedFeatureTypes(self, Union[QGeoRouteRequest.FeatureTypes, QGeoRouteRequest.FeatureType]) """
        pass

    def setSupportedFeatureWeights(self, Union, QGeoRouteRequest_FeatureWeights=None, QGeoRouteRequest_FeatureWeight=None): # real signature unknown; restored from __doc__
        """ setSupportedFeatureWeights(self, Union[QGeoRouteRequest.FeatureWeights, QGeoRouteRequest.FeatureWeight]) """
        pass

    def setSupportedManeuverDetails(self, Union, QGeoRouteRequest_ManeuverDetails=None, QGeoRouteRequest_ManeuverDetail=None): # real signature unknown; restored from __doc__
        """ setSupportedManeuverDetails(self, Union[QGeoRouteRequest.ManeuverDetails, QGeoRouteRequest.ManeuverDetail]) """
        pass

    def setSupportedRouteOptimizations(self, Union, QGeoRouteRequest_RouteOptimizations=None, QGeoRouteRequest_RouteOptimization=None): # real signature unknown; restored from __doc__
        """ setSupportedRouteOptimizations(self, Union[QGeoRouteRequest.RouteOptimizations, QGeoRouteRequest.RouteOptimization]) """
        pass

    def setSupportedSegmentDetails(self, Union, QGeoRouteRequest_SegmentDetails=None, QGeoRouteRequest_SegmentDetail=None): # real signature unknown; restored from __doc__
        """ setSupportedSegmentDetails(self, Union[QGeoRouteRequest.SegmentDetails, QGeoRouteRequest.SegmentDetail]) """
        pass

    def setSupportedTravelModes(self, Union, QGeoRouteRequest_TravelModes=None, QGeoRouteRequest_TravelMode=None): # real signature unknown; restored from __doc__
        """ setSupportedTravelModes(self, Union[QGeoRouteRequest.TravelModes, QGeoRouteRequest.TravelMode]) """
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

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateRoute(self, QGeoRoute, QGeoCoordinate): # real signature unknown; restored from __doc__
        """ updateRoute(self, QGeoRoute, QGeoCoordinate) -> QGeoRouteReply """
        return QGeoRouteReply

    def __init__(self, Dict, p_str=None, Any=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


