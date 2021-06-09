# encoding: utf-8
# module PyQt5.QtPositioning
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtPositioning.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


# no functions
# classes

class QGeoAddress(__sip.wrapper):
    """
    QGeoAddress()
    QGeoAddress(QGeoAddress)
    """
    def city(self): # real signature unknown; restored from __doc__
        """ city(self) -> str """
        return ""

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def country(self): # real signature unknown; restored from __doc__
        """ country(self) -> str """
        return ""

    def countryCode(self): # real signature unknown; restored from __doc__
        """ countryCode(self) -> str """
        return ""

    def county(self): # real signature unknown; restored from __doc__
        """ county(self) -> str """
        return ""

    def district(self): # real signature unknown; restored from __doc__
        """ district(self) -> str """
        return ""

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isTextGenerated(self): # real signature unknown; restored from __doc__
        """ isTextGenerated(self) -> bool """
        return False

    def postalCode(self): # real signature unknown; restored from __doc__
        """ postalCode(self) -> str """
        return ""

    def setCity(self, p_str): # real signature unknown; restored from __doc__
        """ setCity(self, str) """
        pass

    def setCountry(self, p_str): # real signature unknown; restored from __doc__
        """ setCountry(self, str) """
        pass

    def setCountryCode(self, p_str): # real signature unknown; restored from __doc__
        """ setCountryCode(self, str) """
        pass

    def setCounty(self, p_str): # real signature unknown; restored from __doc__
        """ setCounty(self, str) """
        pass

    def setDistrict(self, p_str): # real signature unknown; restored from __doc__
        """ setDistrict(self, str) """
        pass

    def setPostalCode(self, p_str): # real signature unknown; restored from __doc__
        """ setPostalCode(self, str) """
        pass

    def setState(self, p_str): # real signature unknown; restored from __doc__
        """ setState(self, str) """
        pass

    def setStreet(self, p_str): # real signature unknown; restored from __doc__
        """ setStreet(self, str) """
        pass

    def setText(self, p_str): # real signature unknown; restored from __doc__
        """ setText(self, str) """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> str """
        return ""

    def street(self): # real signature unknown; restored from __doc__
        """ street(self) -> str """
        return ""

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, QGeoAddress=None): # real signature unknown; restored from __doc__ with multiple overloads
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


class QGeoAreaMonitorInfo(__sip.wrapper):
    """
    QGeoAreaMonitorInfo(name: str = '')
    QGeoAreaMonitorInfo(QGeoAreaMonitorInfo)
    """
    def area(self): # real signature unknown; restored from __doc__
        """ area(self) -> QGeoShape """
        return QGeoShape

    def expiration(self): # real signature unknown; restored from __doc__
        """ expiration(self) -> QDateTime """
        pass

    def identifier(self): # real signature unknown; restored from __doc__
        """ identifier(self) -> str """
        return ""

    def isPersistent(self): # real signature unknown; restored from __doc__
        """ isPersistent(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def notificationParameters(self): # real signature unknown; restored from __doc__
        """ notificationParameters(self) -> Dict[str, Any] """
        return {}

    def setArea(self, QGeoShape): # real signature unknown; restored from __doc__
        """ setArea(self, QGeoShape) """
        pass

    def setExpiration(self, Union, QDateTime=None, datetime_datetime=None): # real signature unknown; restored from __doc__
        """ setExpiration(self, Union[QDateTime, datetime.datetime]) """
        pass

    def setName(self, p_str): # real signature unknown; restored from __doc__
        """ setName(self, str) """
        pass

    def setNotificationParameters(self, Dict, p_str=None, Any=None): # real signature unknown; restored from __doc__
        """ setNotificationParameters(self, Dict[str, Any]) """
        pass

    def setPersistent(self, bool): # real signature unknown; restored from __doc__
        """ setPersistent(self, bool) """
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


    __hash__ = None


class QGeoAreaMonitorSource(__PyQt5_QtCore.QObject):
    """ QGeoAreaMonitorSource(QObject) """
    def activeMonitors(self, QGeoShape=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        activeMonitors(self) -> List[QGeoAreaMonitorInfo]
        activeMonitors(self, QGeoShape) -> List[QGeoAreaMonitorInfo]
        """
        return []

    def areaEntered(self, QGeoAreaMonitorInfo, QGeoPositionInfo): # real signature unknown; restored from __doc__
        """ areaEntered(self, QGeoAreaMonitorInfo, QGeoPositionInfo) [signal] """
        pass

    def areaExited(self, QGeoAreaMonitorInfo, QGeoPositionInfo): # real signature unknown; restored from __doc__
        """ areaExited(self, QGeoAreaMonitorInfo, QGeoPositionInfo) [signal] """
        pass

    def availableSources(self): # real signature unknown; restored from __doc__
        """ availableSources() -> List[str] """
        return []

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createDefaultSource(self, QObject): # real signature unknown; restored from __doc__
        """ createDefaultSource(QObject) -> QGeoAreaMonitorSource """
        return QGeoAreaMonitorSource

    def createSource(self, p_str, QObject): # real signature unknown; restored from __doc__
        """ createSource(str, QObject) -> QGeoAreaMonitorSource """
        return QGeoAreaMonitorSource

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, QGeoAreaMonitorSource_Error=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        error(self) -> QGeoAreaMonitorSource.Error
        error(self, QGeoAreaMonitorSource.Error) [signal]
        """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def monitorExpired(self, QGeoAreaMonitorInfo): # real signature unknown; restored from __doc__
        """ monitorExpired(self, QGeoAreaMonitorInfo) [signal] """
        pass

    def positionInfoSource(self): # real signature unknown; restored from __doc__
        """ positionInfoSource(self) -> QGeoPositionInfoSource """
        return QGeoPositionInfoSource

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def requestUpdate(self, QGeoAreaMonitorInfo, p_str): # real signature unknown; restored from __doc__
        """ requestUpdate(self, QGeoAreaMonitorInfo, str) -> bool """
        return False

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setPositionInfoSource(self, QGeoPositionInfoSource): # real signature unknown; restored from __doc__
        """ setPositionInfoSource(self, QGeoPositionInfoSource) """
        pass

    def sourceName(self): # real signature unknown; restored from __doc__
        """ sourceName(self) -> str """
        return ""

    def startMonitoring(self, QGeoAreaMonitorInfo): # real signature unknown; restored from __doc__
        """ startMonitoring(self, QGeoAreaMonitorInfo) -> bool """
        return False

    def stopMonitoring(self, QGeoAreaMonitorInfo): # real signature unknown; restored from __doc__
        """ stopMonitoring(self, QGeoAreaMonitorInfo) -> bool """
        return False

    def supportedAreaMonitorFeatures(self): # real signature unknown; restored from __doc__
        """ supportedAreaMonitorFeatures(self) -> QGeoAreaMonitorSource.AreaMonitorFeatures """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, QObject): # real signature unknown; restored from __doc__
        pass

    AccessError = 0
    AnyAreaMonitorFeature = -1
    InsufficientPositionInfo = 1
    NoError = 3
    PersistentAreaMonitorFeature = 1
    UnknownSourceError = 2


class QGeoShape(__sip.wrapper):
    """
    QGeoShape()
    QGeoShape(QGeoShape)
    """
    def boundingGeoRectangle(self): # real signature unknown; restored from __doc__
        """ boundingGeoRectangle(self) -> QGeoRectangle """
        return QGeoRectangle

    def center(self): # real signature unknown; restored from __doc__
        """ center(self) -> QGeoCoordinate """
        return QGeoCoordinate

    def contains(self, QGeoCoordinate): # real signature unknown; restored from __doc__
        """ contains(self, QGeoCoordinate) -> bool """
        return False

    def extendShape(self, QGeoCoordinate): # real signature unknown; restored from __doc__
        """ extendShape(self, QGeoCoordinate) """
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def toString(self): # real signature unknown; restored from __doc__
        """ toString(self) -> str """
        return ""

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QGeoShape.ShapeType """
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

    def __init__(self, QGeoShape=None): # real signature unknown; restored from __doc__ with multiple overloads
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


    CircleType = 2
    PathType = 3
    PolygonType = 4
    RectangleType = 1
    UnknownType = 0
    __hash__ = None


class QGeoCircle(QGeoShape):
    """
    QGeoCircle()
    QGeoCircle(QGeoCoordinate, radius: float = -1)
    QGeoCircle(QGeoCircle)
    QGeoCircle(QGeoShape)
    """
    def center(self): # real signature unknown; restored from __doc__
        """ center(self) -> QGeoCoordinate """
        return QGeoCoordinate

    def extendCircle(self, QGeoCoordinate): # real signature unknown; restored from __doc__
        """ extendCircle(self, QGeoCoordinate) """
        pass

    def radius(self): # real signature unknown; restored from __doc__
        """ radius(self) -> float """
        return 0.0

    def setCenter(self, QGeoCoordinate): # real signature unknown; restored from __doc__
        """ setCenter(self, QGeoCoordinate) """
        pass

    def setRadius(self, p_float): # real signature unknown; restored from __doc__
        """ setRadius(self, float) """
        pass

    def toString(self): # real signature unknown; restored from __doc__
        """ toString(self) -> str """
        return ""

    def translate(self, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ translate(self, float, float) """
        pass

    def translated(self, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ translated(self, float, float) -> QGeoCircle """
        return QGeoCircle

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

    __hash__ = None


class QGeoCoordinate(__sip.wrapper):
    """
    QGeoCoordinate()
    QGeoCoordinate(float, float)
    QGeoCoordinate(float, float, float)
    QGeoCoordinate(QGeoCoordinate)
    """
    def altitude(self): # real signature unknown; restored from __doc__
        """ altitude(self) -> float """
        return 0.0

    def atDistanceAndAzimuth(self, p_float, p_float_1, distanceUp=0): # real signature unknown; restored from __doc__
        """ atDistanceAndAzimuth(self, float, float, distanceUp: float = 0) -> QGeoCoordinate """
        return QGeoCoordinate

    def azimuthTo(self, QGeoCoordinate): # real signature unknown; restored from __doc__
        """ azimuthTo(self, QGeoCoordinate) -> float """
        return 0.0

    def distanceTo(self, QGeoCoordinate): # real signature unknown; restored from __doc__
        """ distanceTo(self, QGeoCoordinate) -> float """
        return 0.0

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def latitude(self): # real signature unknown; restored from __doc__
        """ latitude(self) -> float """
        return 0.0

    def longitude(self): # real signature unknown; restored from __doc__
        """ longitude(self) -> float """
        return 0.0

    def setAltitude(self, p_float): # real signature unknown; restored from __doc__
        """ setAltitude(self, float) """
        pass

    def setLatitude(self, p_float): # real signature unknown; restored from __doc__
        """ setLatitude(self, float) """
        pass

    def setLongitude(self, p_float): # real signature unknown; restored from __doc__
        """ setLongitude(self, float) """
        pass

    def toString(self, format=None): # real signature unknown; restored from __doc__
        """ toString(self, format: QGeoCoordinate.CoordinateFormat = QGeoCoordinate.DegreesMinutesSecondsWithHemisphere) -> str """
        return ""

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QGeoCoordinate.CoordinateType """
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

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
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


    Coordinate2D = 1
    Coordinate3D = 2
    Degrees = 0
    DegreesMinutes = 2
    DegreesMinutesSeconds = 4
    DegreesMinutesSecondsWithHemisphere = 5
    DegreesMinutesWithHemisphere = 3
    DegreesWithHemisphere = 1
    InvalidCoordinate = 0


class QGeoLocation(__sip.wrapper):
    """
    QGeoLocation()
    QGeoLocation(QGeoLocation)
    """
    def address(self): # real signature unknown; restored from __doc__
        """ address(self) -> QGeoAddress """
        return QGeoAddress

    def boundingBox(self): # real signature unknown; restored from __doc__
        """ boundingBox(self) -> QGeoRectangle """
        return QGeoRectangle

    def coordinate(self): # real signature unknown; restored from __doc__
        """ coordinate(self) -> QGeoCoordinate """
        return QGeoCoordinate

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def setAddress(self, QGeoAddress): # real signature unknown; restored from __doc__
        """ setAddress(self, QGeoAddress) """
        pass

    def setBoundingBox(self, QGeoRectangle): # real signature unknown; restored from __doc__
        """ setBoundingBox(self, QGeoRectangle) """
        pass

    def setCoordinate(self, QGeoCoordinate): # real signature unknown; restored from __doc__
        """ setCoordinate(self, QGeoCoordinate) """
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

    def __init__(self, QGeoLocation=None): # real signature unknown; restored from __doc__ with multiple overloads
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


class QGeoPath(QGeoShape):
    """
    QGeoPath()
    QGeoPath(Iterable[QGeoCoordinate], width: float = 0)
    QGeoPath(QGeoPath)
    QGeoPath(QGeoShape)
    """
    def addCoordinate(self, QGeoCoordinate): # real signature unknown; restored from __doc__
        """ addCoordinate(self, QGeoCoordinate) """
        pass

    def clearPath(self): # real signature unknown; restored from __doc__
        """ clearPath(self) """
        pass

    def containsCoordinate(self, QGeoCoordinate): # real signature unknown; restored from __doc__
        """ containsCoordinate(self, QGeoCoordinate) -> bool """
        return False

    def coordinateAt(self, p_int): # real signature unknown; restored from __doc__
        """ coordinateAt(self, int) -> QGeoCoordinate """
        return QGeoCoordinate

    def insertCoordinate(self, p_int, QGeoCoordinate): # real signature unknown; restored from __doc__
        """ insertCoordinate(self, int, QGeoCoordinate) """
        pass

    def length(self, indexFrom=0, indexTo=-1): # real signature unknown; restored from __doc__
        """ length(self, indexFrom: int = 0, indexTo: int = -1) -> float """
        return 0.0

    def path(self): # real signature unknown; restored from __doc__
        """ path(self) -> List[QGeoCoordinate] """
        return []

    def removeCoordinate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        removeCoordinate(self, QGeoCoordinate)
        removeCoordinate(self, int)
        """
        pass

    def replaceCoordinate(self, p_int, QGeoCoordinate): # real signature unknown; restored from __doc__
        """ replaceCoordinate(self, int, QGeoCoordinate) """
        pass

    def setPath(self, Iterable, QGeoCoordinate=None): # real signature unknown; restored from __doc__
        """ setPath(self, Iterable[QGeoCoordinate]) """
        pass

    def setWidth(self, p_float): # real signature unknown; restored from __doc__
        """ setWidth(self, float) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def toString(self): # real signature unknown; restored from __doc__
        """ toString(self) -> str """
        return ""

    def translate(self, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ translate(self, float, float) """
        pass

    def translated(self, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ translated(self, float, float) -> QGeoPath """
        return QGeoPath

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> float """
        return 0.0

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

    __hash__ = None


class QGeoPolygon(QGeoShape):
    """
    QGeoPolygon()
    QGeoPolygon(Iterable[QGeoCoordinate])
    QGeoPolygon(QGeoPolygon)
    QGeoPolygon(QGeoShape)
    """
    def addCoordinate(self, QGeoCoordinate): # real signature unknown; restored from __doc__
        """ addCoordinate(self, QGeoCoordinate) """
        pass

    def addHole(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addHole(self, Iterable[QGeoCoordinate])
        addHole(self, Any)
        """
        pass

    def containsCoordinate(self, QGeoCoordinate): # real signature unknown; restored from __doc__
        """ containsCoordinate(self, QGeoCoordinate) -> bool """
        return False

    def coordinateAt(self, p_int): # real signature unknown; restored from __doc__
        """ coordinateAt(self, int) -> QGeoCoordinate """
        return QGeoCoordinate

    def hole(self, p_int): # real signature unknown; restored from __doc__
        """ hole(self, int) -> List[Any] """
        return []

    def holePath(self, p_int): # real signature unknown; restored from __doc__
        """ holePath(self, int) -> List[QGeoCoordinate] """
        return []

    def holesCount(self): # real signature unknown; restored from __doc__
        """ holesCount(self) -> int """
        return 0

    def insertCoordinate(self, p_int, QGeoCoordinate): # real signature unknown; restored from __doc__
        """ insertCoordinate(self, int, QGeoCoordinate) """
        pass

    def length(self, indexFrom=0, indexTo=-1): # real signature unknown; restored from __doc__
        """ length(self, indexFrom: int = 0, indexTo: int = -1) -> float """
        return 0.0

    def path(self): # real signature unknown; restored from __doc__
        """ path(self) -> List[QGeoCoordinate] """
        return []

    def perimeter(self): # real signature unknown; restored from __doc__
        """ perimeter(self) -> List[Any] """
        return []

    def removeCoordinate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        removeCoordinate(self, QGeoCoordinate)
        removeCoordinate(self, int)
        """
        pass

    def removeHole(self, p_int): # real signature unknown; restored from __doc__
        """ removeHole(self, int) """
        pass

    def replaceCoordinate(self, p_int, QGeoCoordinate): # real signature unknown; restored from __doc__
        """ replaceCoordinate(self, int, QGeoCoordinate) """
        pass

    def setPath(self, Iterable, QGeoCoordinate=None): # real signature unknown; restored from __doc__
        """ setPath(self, Iterable[QGeoCoordinate]) """
        pass

    def setPerimeter(self, Iterable, Any=None): # real signature unknown; restored from __doc__
        """ setPerimeter(self, Iterable[Any]) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def toString(self): # real signature unknown; restored from __doc__
        """ toString(self) -> str """
        return ""

    def translate(self, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ translate(self, float, float) """
        pass

    def translated(self, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ translated(self, float, float) -> QGeoPolygon """
        return QGeoPolygon

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

    __hash__ = None


class QGeoPositionInfo(__sip.wrapper):
    """
    QGeoPositionInfo()
    QGeoPositionInfo(QGeoCoordinate, Union[QDateTime, datetime.datetime])
    QGeoPositionInfo(QGeoPositionInfo)
    """
    def attribute(self, QGeoPositionInfo_Attribute): # real signature unknown; restored from __doc__
        """ attribute(self, QGeoPositionInfo.Attribute) -> float """
        return 0.0

    def coordinate(self): # real signature unknown; restored from __doc__
        """ coordinate(self) -> QGeoCoordinate """
        return QGeoCoordinate

    def hasAttribute(self, QGeoPositionInfo_Attribute): # real signature unknown; restored from __doc__
        """ hasAttribute(self, QGeoPositionInfo.Attribute) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def removeAttribute(self, QGeoPositionInfo_Attribute): # real signature unknown; restored from __doc__
        """ removeAttribute(self, QGeoPositionInfo.Attribute) """
        pass

    def setAttribute(self, QGeoPositionInfo_Attribute, p_float): # real signature unknown; restored from __doc__
        """ setAttribute(self, QGeoPositionInfo.Attribute, float) """
        pass

    def setCoordinate(self, QGeoCoordinate): # real signature unknown; restored from __doc__
        """ setCoordinate(self, QGeoCoordinate) """
        pass

    def setTimestamp(self, Union, QDateTime=None, datetime_datetime=None): # real signature unknown; restored from __doc__
        """ setTimestamp(self, Union[QDateTime, datetime.datetime]) """
        pass

    def timestamp(self): # real signature unknown; restored from __doc__
        """ timestamp(self) -> QDateTime """
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


    Direction = 0
    GroundSpeed = 1
    HorizontalAccuracy = 4
    MagneticVariation = 3
    VerticalAccuracy = 5
    VerticalSpeed = 2
    __hash__ = None


class QGeoPositionInfoSource(__PyQt5_QtCore.QObject):
    """ QGeoPositionInfoSource(QObject) """
    def availableSources(self): # real signature unknown; restored from __doc__
        """ availableSources() -> List[str] """
        return []

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createDefaultSource(self, QObject): # real signature unknown; restored from __doc__
        """ createDefaultSource(QObject) -> QGeoPositionInfoSource """
        return QGeoPositionInfoSource

    def createSource(self, p_str, QObject): # real signature unknown; restored from __doc__
        """ createSource(str, QObject) -> QGeoPositionInfoSource """
        return QGeoPositionInfoSource

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, QGeoPositionInfoSource_Error=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        error(self) -> QGeoPositionInfoSource.Error
        error(self, QGeoPositionInfoSource.Error) [signal]
        """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def lastKnownPosition(self, fromSatellitePositioningMethodsOnly=False): # real signature unknown; restored from __doc__
        """ lastKnownPosition(self, fromSatellitePositioningMethodsOnly: bool = False) -> QGeoPositionInfo """
        return QGeoPositionInfo

    def minimumUpdateInterval(self): # real signature unknown; restored from __doc__
        """ minimumUpdateInterval(self) -> int """
        return 0

    def positionUpdated(self, QGeoPositionInfo): # real signature unknown; restored from __doc__
        """ positionUpdated(self, QGeoPositionInfo) [signal] """
        pass

    def preferredPositioningMethods(self): # real signature unknown; restored from __doc__
        """ preferredPositioningMethods(self) -> QGeoPositionInfoSource.PositioningMethods """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def requestUpdate(self, timeout=0): # real signature unknown; restored from __doc__
        """ requestUpdate(self, timeout: int = 0) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setPreferredPositioningMethods(self, Union, QGeoPositionInfoSource_PositioningMethods=None, QGeoPositionInfoSource_PositioningMethod=None): # real signature unknown; restored from __doc__
        """ setPreferredPositioningMethods(self, Union[QGeoPositionInfoSource.PositioningMethods, QGeoPositionInfoSource.PositioningMethod]) """
        pass

    def setUpdateInterval(self, p_int): # real signature unknown; restored from __doc__
        """ setUpdateInterval(self, int) """
        pass

    def sourceName(self): # real signature unknown; restored from __doc__
        """ sourceName(self) -> str """
        return ""

    def startUpdates(self): # real signature unknown; restored from __doc__
        """ startUpdates(self) """
        pass

    def stopUpdates(self): # real signature unknown; restored from __doc__
        """ stopUpdates(self) """
        pass

    def supportedPositioningMethods(self): # real signature unknown; restored from __doc__
        """ supportedPositioningMethods(self) -> QGeoPositionInfoSource.PositioningMethods """
        pass

    def supportedPositioningMethodsChanged(self): # real signature unknown; restored from __doc__
        """ supportedPositioningMethodsChanged(self) [signal] """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateInterval(self): # real signature unknown; restored from __doc__
        """ updateInterval(self) -> int """
        return 0

    def updateTimeout(self): # real signature unknown; restored from __doc__
        """ updateTimeout(self) [signal] """
        pass

    def __init__(self, QObject): # real signature unknown; restored from __doc__
        pass

    AccessError = 0
    AllPositioningMethods = -1
    ClosedError = 1
    NoError = 3
    NonSatellitePositioningMethods = -256
    NoPositioningMethods = 0
    SatellitePositioningMethods = 255
    UnknownSourceError = 2


class QGeoRectangle(QGeoShape):
    """
    QGeoRectangle()
    QGeoRectangle(QGeoCoordinate, float, float)
    QGeoRectangle(QGeoCoordinate, QGeoCoordinate)
    QGeoRectangle(Iterable[QGeoCoordinate])
    QGeoRectangle(QGeoRectangle)
    QGeoRectangle(QGeoShape)
    """
    def bottomLeft(self): # real signature unknown; restored from __doc__
        """ bottomLeft(self) -> QGeoCoordinate """
        return QGeoCoordinate

    def bottomRight(self): # real signature unknown; restored from __doc__
        """ bottomRight(self) -> QGeoCoordinate """
        return QGeoCoordinate

    def center(self): # real signature unknown; restored from __doc__
        """ center(self) -> QGeoCoordinate """
        return QGeoCoordinate

    def contains(self, QGeoRectangle): # real signature unknown; restored from __doc__
        """ contains(self, QGeoRectangle) -> bool """
        return False

    def extendRectangle(self, QGeoCoordinate): # real signature unknown; restored from __doc__
        """ extendRectangle(self, QGeoCoordinate) """
        pass

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> float """
        return 0.0

    def intersects(self, QGeoRectangle): # real signature unknown; restored from __doc__
        """ intersects(self, QGeoRectangle) -> bool """
        return False

    def setBottomLeft(self, QGeoCoordinate): # real signature unknown; restored from __doc__
        """ setBottomLeft(self, QGeoCoordinate) """
        pass

    def setBottomRight(self, QGeoCoordinate): # real signature unknown; restored from __doc__
        """ setBottomRight(self, QGeoCoordinate) """
        pass

    def setCenter(self, QGeoCoordinate): # real signature unknown; restored from __doc__
        """ setCenter(self, QGeoCoordinate) """
        pass

    def setHeight(self, p_float): # real signature unknown; restored from __doc__
        """ setHeight(self, float) """
        pass

    def setTopLeft(self, QGeoCoordinate): # real signature unknown; restored from __doc__
        """ setTopLeft(self, QGeoCoordinate) """
        pass

    def setTopRight(self, QGeoCoordinate): # real signature unknown; restored from __doc__
        """ setTopRight(self, QGeoCoordinate) """
        pass

    def setWidth(self, p_float): # real signature unknown; restored from __doc__
        """ setWidth(self, float) """
        pass

    def topLeft(self): # real signature unknown; restored from __doc__
        """ topLeft(self) -> QGeoCoordinate """
        return QGeoCoordinate

    def topRight(self): # real signature unknown; restored from __doc__
        """ topRight(self) -> QGeoCoordinate """
        return QGeoCoordinate

    def toString(self): # real signature unknown; restored from __doc__
        """ toString(self) -> str """
        return ""

    def translate(self, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ translate(self, float, float) """
        pass

    def translated(self, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ translated(self, float, float) -> QGeoRectangle """
        return QGeoRectangle

    def united(self, QGeoRectangle): # real signature unknown; restored from __doc__
        """ united(self, QGeoRectangle) -> QGeoRectangle """
        return QGeoRectangle

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> float """
        return 0.0

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

    def __ior__(self, *args, **kwargs): # real signature unknown
        """ Return self|=value. """
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

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    __hash__ = None


class QGeoSatelliteInfo(__sip.wrapper):
    """
    QGeoSatelliteInfo()
    QGeoSatelliteInfo(QGeoSatelliteInfo)
    """
    def attribute(self, QGeoSatelliteInfo_Attribute): # real signature unknown; restored from __doc__
        """ attribute(self, QGeoSatelliteInfo.Attribute) -> float """
        return 0.0

    def hasAttribute(self, QGeoSatelliteInfo_Attribute): # real signature unknown; restored from __doc__
        """ hasAttribute(self, QGeoSatelliteInfo.Attribute) -> bool """
        return False

    def removeAttribute(self, QGeoSatelliteInfo_Attribute): # real signature unknown; restored from __doc__
        """ removeAttribute(self, QGeoSatelliteInfo.Attribute) """
        pass

    def satelliteIdentifier(self): # real signature unknown; restored from __doc__
        """ satelliteIdentifier(self) -> int """
        return 0

    def satelliteSystem(self): # real signature unknown; restored from __doc__
        """ satelliteSystem(self) -> QGeoSatelliteInfo.SatelliteSystem """
        pass

    def setAttribute(self, QGeoSatelliteInfo_Attribute, p_float): # real signature unknown; restored from __doc__
        """ setAttribute(self, QGeoSatelliteInfo.Attribute, float) """
        pass

    def setSatelliteIdentifier(self, p_int): # real signature unknown; restored from __doc__
        """ setSatelliteIdentifier(self, int) """
        pass

    def setSatelliteSystem(self, QGeoSatelliteInfo_SatelliteSystem): # real signature unknown; restored from __doc__
        """ setSatelliteSystem(self, QGeoSatelliteInfo.SatelliteSystem) """
        pass

    def setSignalStrength(self, p_int): # real signature unknown; restored from __doc__
        """ setSignalStrength(self, int) """
        pass

    def signalStrength(self): # real signature unknown; restored from __doc__
        """ signalStrength(self) -> int """
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

    def __init__(self, QGeoSatelliteInfo=None): # real signature unknown; restored from __doc__ with multiple overloads
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


    Azimuth = 1
    Elevation = 0
    GLONASS = 2
    GPS = 1
    Undefined = 0
    __hash__ = None


class QGeoSatelliteInfoSource(__PyQt5_QtCore.QObject):
    """ QGeoSatelliteInfoSource(QObject) """
    def availableSources(self): # real signature unknown; restored from __doc__
        """ availableSources() -> List[str] """
        return []

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createDefaultSource(self, QObject): # real signature unknown; restored from __doc__
        """ createDefaultSource(QObject) -> QGeoSatelliteInfoSource """
        return QGeoSatelliteInfoSource

    def createSource(self, p_str, QObject): # real signature unknown; restored from __doc__
        """ createSource(str, QObject) -> QGeoSatelliteInfoSource """
        return QGeoSatelliteInfoSource

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, QGeoSatelliteInfoSource_Error=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        error(self) -> QGeoSatelliteInfoSource.Error
        error(self, QGeoSatelliteInfoSource.Error) [signal]
        """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def minimumUpdateInterval(self): # real signature unknown; restored from __doc__
        """ minimumUpdateInterval(self) -> int """
        return 0

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def requestTimeout(self): # real signature unknown; restored from __doc__
        """ requestTimeout(self) [signal] """
        pass

    def requestUpdate(self, timeout=0): # real signature unknown; restored from __doc__
        """ requestUpdate(self, timeout: int = 0) """
        pass

    def satellitesInUseUpdated(self, Iterable, QGeoSatelliteInfo=None): # real signature unknown; restored from __doc__
        """ satellitesInUseUpdated(self, Iterable[QGeoSatelliteInfo]) [signal] """
        pass

    def satellitesInViewUpdated(self, Iterable, QGeoSatelliteInfo=None): # real signature unknown; restored from __doc__
        """ satellitesInViewUpdated(self, Iterable[QGeoSatelliteInfo]) [signal] """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setUpdateInterval(self, p_int): # real signature unknown; restored from __doc__
        """ setUpdateInterval(self, int) """
        pass

    def sourceName(self): # real signature unknown; restored from __doc__
        """ sourceName(self) -> str """
        return ""

    def startUpdates(self): # real signature unknown; restored from __doc__
        """ startUpdates(self) """
        pass

    def stopUpdates(self): # real signature unknown; restored from __doc__
        """ stopUpdates(self) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateInterval(self): # real signature unknown; restored from __doc__
        """ updateInterval(self) -> int """
        return 0

    def __init__(self, QObject): # real signature unknown; restored from __doc__
        pass

    AccessError = 0
    ClosedError = 1
    NoError = 2
    UnknownSourceError = -1


class QNmeaPositionInfoSource(QGeoPositionInfoSource):
    """ QNmeaPositionInfoSource(QNmeaPositionInfoSource.UpdateMode, parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> QIODevice """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> QGeoPositionInfoSource.Error """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def lastKnownPosition(self, fromSatellitePositioningMethodsOnly=False): # real signature unknown; restored from __doc__
        """ lastKnownPosition(self, fromSatellitePositioningMethodsOnly: bool = False) -> QGeoPositionInfo """
        return QGeoPositionInfo

    def minimumUpdateInterval(self): # real signature unknown; restored from __doc__
        """ minimumUpdateInterval(self) -> int """
        return 0

    def parsePosInfoFromNmeaData(self, p_str, p_int, QGeoPositionInfo): # real signature unknown; restored from __doc__
        """ parsePosInfoFromNmeaData(self, str, int, QGeoPositionInfo) -> Tuple[bool, bool] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def requestUpdate(self, timeout=0): # real signature unknown; restored from __doc__
        """ requestUpdate(self, timeout: int = 0) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setDevice(self, QIODevice): # real signature unknown; restored from __doc__
        """ setDevice(self, QIODevice) """
        pass

    def setUpdateInterval(self, p_int): # real signature unknown; restored from __doc__
        """ setUpdateInterval(self, int) """
        pass

    def setUserEquivalentRangeError(self, p_float): # real signature unknown; restored from __doc__
        """ setUserEquivalentRangeError(self, float) """
        pass

    def startUpdates(self): # real signature unknown; restored from __doc__
        """ startUpdates(self) """
        pass

    def stopUpdates(self): # real signature unknown; restored from __doc__
        """ stopUpdates(self) """
        pass

    def supportedPositioningMethods(self): # real signature unknown; restored from __doc__
        """ supportedPositioningMethods(self) -> QGeoPositionInfoSource.PositioningMethods """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMode(self): # real signature unknown; restored from __doc__
        """ updateMode(self) -> QNmeaPositionInfoSource.UpdateMode """
        pass

    def userEquivalentRangeError(self): # real signature unknown; restored from __doc__
        """ userEquivalentRangeError(self) -> float """
        return 0.0

    def __init__(self, QNmeaPositionInfoSource_UpdateMode, parent=None): # real signature unknown; restored from __doc__
        pass

    RealTimeMode = 1
    SimulationMode = 2


# variables with complex values



