# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QMediaObject import QMediaObject

class QRadioTuner(QMediaObject):
    """ QRadioTuner(parent: QObject = None) """
    def addPropertyWatch(self, *args, **kwargs): # real signature unknown
        pass

    def antennaConnectedChanged(self, bool): # real signature unknown; restored from __doc__
        """ antennaConnectedChanged(self, bool) [signal] """
        pass

    def availability(self): # real signature unknown; restored from __doc__
        """ availability(self) -> QMultimedia.AvailabilityStatus """
        pass

    def band(self): # real signature unknown; restored from __doc__
        """ band(self) -> QRadioTuner.Band """
        pass

    def bandChanged(self, QRadioTuner_Band): # real signature unknown; restored from __doc__
        """ bandChanged(self, QRadioTuner.Band) [signal] """
        pass

    def cancelSearch(self): # real signature unknown; restored from __doc__
        """ cancelSearch(self) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, QRadioTuner_Error=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        error(self) -> QRadioTuner.Error
        error(self, QRadioTuner.Error) [signal]
        """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def frequency(self): # real signature unknown; restored from __doc__
        """ frequency(self) -> int """
        return 0

    def frequencyChanged(self, p_int): # real signature unknown; restored from __doc__
        """ frequencyChanged(self, int) [signal] """
        pass

    def frequencyRange(self, QRadioTuner_Band): # real signature unknown; restored from __doc__
        """ frequencyRange(self, QRadioTuner.Band) -> Tuple[int, int] """
        pass

    def frequencyStep(self, QRadioTuner_Band): # real signature unknown; restored from __doc__
        """ frequencyStep(self, QRadioTuner.Band) -> int """
        return 0

    def isAntennaConnected(self): # real signature unknown; restored from __doc__
        """ isAntennaConnected(self) -> bool """
        return False

    def isBandSupported(self, QRadioTuner_Band): # real signature unknown; restored from __doc__
        """ isBandSupported(self, QRadioTuner.Band) -> bool """
        return False

    def isMuted(self): # real signature unknown; restored from __doc__
        """ isMuted(self) -> bool """
        return False

    def isSearching(self): # real signature unknown; restored from __doc__
        """ isSearching(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isStereo(self): # real signature unknown; restored from __doc__
        """ isStereo(self) -> bool """
        return False

    def mutedChanged(self, bool): # real signature unknown; restored from __doc__
        """ mutedChanged(self, bool) [signal] """
        pass

    def radioData(self): # real signature unknown; restored from __doc__
        """ radioData(self) -> QRadioData """
        return QRadioData

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removePropertyWatch(self, *args, **kwargs): # real signature unknown
        pass

    def searchAllStations(self, searchMode=None): # real signature unknown; restored from __doc__
        """ searchAllStations(self, searchMode: QRadioTuner.SearchMode = QRadioTuner.SearchFast) """
        pass

    def searchBackward(self): # real signature unknown; restored from __doc__
        """ searchBackward(self) """
        pass

    def searchForward(self): # real signature unknown; restored from __doc__
        """ searchForward(self) """
        pass

    def searchingChanged(self, bool): # real signature unknown; restored from __doc__
        """ searchingChanged(self, bool) [signal] """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setBand(self, QRadioTuner_Band): # real signature unknown; restored from __doc__
        """ setBand(self, QRadioTuner.Band) """
        pass

    def setFrequency(self, p_int): # real signature unknown; restored from __doc__
        """ setFrequency(self, int) """
        pass

    def setMuted(self, bool): # real signature unknown; restored from __doc__
        """ setMuted(self, bool) """
        pass

    def setStereoMode(self, QRadioTuner_StereoMode): # real signature unknown; restored from __doc__
        """ setStereoMode(self, QRadioTuner.StereoMode) """
        pass

    def setVolume(self, p_int): # real signature unknown; restored from __doc__
        """ setVolume(self, int) """
        pass

    def signalStrength(self): # real signature unknown; restored from __doc__
        """ signalStrength(self) -> int """
        return 0

    def signalStrengthChanged(self, p_int): # real signature unknown; restored from __doc__
        """ signalStrengthChanged(self, int) [signal] """
        pass

    def start(self): # real signature unknown; restored from __doc__
        """ start(self) """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QRadioTuner.State """
        pass

    def stateChanged(self, QRadioTuner_State): # real signature unknown; restored from __doc__
        """ stateChanged(self, QRadioTuner.State) [signal] """
        pass

    def stationFound(self, p_int, p_str): # real signature unknown; restored from __doc__
        """ stationFound(self, int, str) [signal] """
        pass

    def stereoMode(self): # real signature unknown; restored from __doc__
        """ stereoMode(self) -> QRadioTuner.StereoMode """
        pass

    def stereoStatusChanged(self, bool): # real signature unknown; restored from __doc__
        """ stereoStatusChanged(self, bool) [signal] """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def volume(self): # real signature unknown; restored from __doc__
        """ volume(self) -> int """
        return 0

    def volumeChanged(self, p_int): # real signature unknown; restored from __doc__
        """ volumeChanged(self, int) [signal] """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    ActiveState = 0
    AM = 0
    Auto = 2
    FM = 1
    FM2 = 4
    ForceMono = 1
    ForceStereo = 0
    LW = 3
    NoError = 0
    OpenError = 2
    OutOfRangeError = 3
    ResourceError = 1
    SearchFast = 0
    SearchGetStationId = 1
    StoppedState = 1
    SW = 2


