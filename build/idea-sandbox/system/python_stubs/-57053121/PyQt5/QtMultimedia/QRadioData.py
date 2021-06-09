# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QMediaBindableInterface import QMediaBindableInterface

class QRadioData(__PyQt5_QtCore.QObject, QMediaBindableInterface):
    """ QRadioData(QMediaObject, parent: QObject = None) """
    def alternativeFrequenciesEnabledChanged(self, bool): # real signature unknown; restored from __doc__
        """ alternativeFrequenciesEnabledChanged(self, bool) [signal] """
        pass

    def availability(self): # real signature unknown; restored from __doc__
        """ availability(self) -> QMultimedia.AvailabilityStatus """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, QRadioData_Error=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        error(self) -> QRadioData.Error
        error(self, QRadioData.Error) [signal]
        """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def isAlternativeFrequenciesEnabled(self): # real signature unknown; restored from __doc__
        """ isAlternativeFrequenciesEnabled(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def mediaObject(self): # real signature unknown; restored from __doc__
        """ mediaObject(self) -> QMediaObject """
        return QMediaObject

    def programType(self): # real signature unknown; restored from __doc__
        """ programType(self) -> QRadioData.ProgramType """
        pass

    def programTypeChanged(self, QRadioData_ProgramType): # real signature unknown; restored from __doc__
        """ programTypeChanged(self, QRadioData.ProgramType) [signal] """
        pass

    def programTypeName(self): # real signature unknown; restored from __doc__
        """ programTypeName(self) -> str """
        return ""

    def programTypeNameChanged(self, p_str): # real signature unknown; restored from __doc__
        """ programTypeNameChanged(self, str) [signal] """
        pass

    def radioText(self): # real signature unknown; restored from __doc__
        """ radioText(self) -> str """
        return ""

    def radioTextChanged(self, p_str): # real signature unknown; restored from __doc__
        """ radioTextChanged(self, str) [signal] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAlternativeFrequenciesEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setAlternativeFrequenciesEnabled(self, bool) """
        pass

    def setMediaObject(self, QMediaObject): # real signature unknown; restored from __doc__
        """ setMediaObject(self, QMediaObject) -> bool """
        return False

    def stationId(self): # real signature unknown; restored from __doc__
        """ stationId(self) -> str """
        return ""

    def stationIdChanged(self, p_str): # real signature unknown; restored from __doc__
        """ stationIdChanged(self, str) [signal] """
        pass

    def stationName(self): # real signature unknown; restored from __doc__
        """ stationName(self) -> str """
        return ""

    def stationNameChanged(self, p_str): # real signature unknown; restored from __doc__
        """ stationNameChanged(self, str) [signal] """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, QMediaObject, parent=None): # real signature unknown; restored from __doc__
        pass

    AdultHits = 34
    Alarm = 31
    AlarmTest = 30
    ChildrensProgrammes = 18
    Classical = 39
    ClassicRock = 33
    College = 47
    CountryMusic = 25
    Culture = 7
    CurrentAffairs = 2
    Documentary = 29
    Drama = 6
    EasyListening = 12
    Education = 5
    Finance = 17
    FolkMusic = 28
    Information = 3
    JazzMusic = 24
    Language = 42
    Leisure = 23
    LightClassical = 13
    NationalMusic = 26
    News = 1
    NoError = 0
    Nostalgia = 38
    OldiesMusic = 27
    OpenError = 2
    OtherMusic = 15
    OutOfRangeError = 3
    Personality = 45
    PhoneIn = 21
    PopMusic = 10
    Public = 46
    Religion = 20
    ReligiousMusic = 43
    ReligiousTalk = 44
    ResourceError = 1
    RhythmAndBlues = 40
    RockMusic = 11
    Science = 8
    SeriousClassical = 14
    SocialAffairs = 19
    Soft = 37
    SoftRhythmAndBlues = 41
    SoftRock = 35
    Sport = 4
    Talk = 32
    Top40 = 36
    Travel = 22
    Undefined = 0
    Varied = 9
    Weather = 16


