# encoding: utf-8
# module PyQt5.QtLocation
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtLocation.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QGeoManeuver(__sip.simplewrapper):
    """
    QGeoManeuver()
    QGeoManeuver(QGeoManeuver)
    """
    def direction(self): # real signature unknown; restored from __doc__
        """ direction(self) -> QGeoManeuver.InstructionDirection """
        pass

    def distanceToNextInstruction(self): # real signature unknown; restored from __doc__
        """ distanceToNextInstruction(self) -> float """
        return 0.0

    def extendedAttributes(self): # real signature unknown; restored from __doc__
        """ extendedAttributes(self) -> Dict[str, Any] """
        return {}

    def instructionText(self): # real signature unknown; restored from __doc__
        """ instructionText(self) -> str """
        return ""

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def position(self): # real signature unknown; restored from __doc__
        """ position(self) -> QGeoCoordinate """
        pass

    def setDirection(self, QGeoManeuver_InstructionDirection): # real signature unknown; restored from __doc__
        """ setDirection(self, QGeoManeuver.InstructionDirection) """
        pass

    def setDistanceToNextInstruction(self, p_float): # real signature unknown; restored from __doc__
        """ setDistanceToNextInstruction(self, float) """
        pass

    def setExtendedAttributes(self, Dict, p_str=None, Any=None): # real signature unknown; restored from __doc__
        """ setExtendedAttributes(self, Dict[str, Any]) """
        pass

    def setInstructionText(self, p_str): # real signature unknown; restored from __doc__
        """ setInstructionText(self, str) """
        pass

    def setPosition(self, QGeoCoordinate): # real signature unknown; restored from __doc__
        """ setPosition(self, QGeoCoordinate) """
        pass

    def setTimeToNextInstruction(self, p_int): # real signature unknown; restored from __doc__
        """ setTimeToNextInstruction(self, int) """
        pass

    def setWaypoint(self, QGeoCoordinate): # real signature unknown; restored from __doc__
        """ setWaypoint(self, QGeoCoordinate) """
        pass

    def timeToNextInstruction(self): # real signature unknown; restored from __doc__
        """ timeToNextInstruction(self) -> int """
        return 0

    def waypoint(self): # real signature unknown; restored from __doc__
        """ waypoint(self) -> QGeoCoordinate """
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

    def __init__(self, QGeoManeuver=None): # real signature unknown; restored from __doc__ with multiple overloads
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


    DirectionBearLeft = 11
    DirectionBearRight = 2
    DirectionForward = 1
    DirectionHardLeft = 8
    DirectionHardRight = 5
    DirectionLeft = 9
    DirectionLightLeft = 10
    DirectionLightRight = 3
    DirectionRight = 4
    DirectionUTurnLeft = 7
    DirectionUTurnRight = 6
    NoDirection = 0
    __hash__ = None


