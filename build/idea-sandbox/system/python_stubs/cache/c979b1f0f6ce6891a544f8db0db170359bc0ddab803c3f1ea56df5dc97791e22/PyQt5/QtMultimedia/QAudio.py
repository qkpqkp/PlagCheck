# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QAudio(__sip.simplewrapper):
    # no doc
    def convertVolume(self, p_float, QAudio_VolumeScale, QAudio_VolumeScale_1): # real signature unknown; restored from __doc__
        """ convertVolume(float, QAudio.VolumeScale, QAudio.VolumeScale) -> float """
        return 0.0

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AccessibilityRole = 7
    ActiveState = 0
    AlarmRole = 4
    AudioInput = 0
    AudioOutput = 1
    CubicVolumeScale = 1
    CustomRole = 10
    DecibelVolumeScale = 3
    FatalError = 4
    GameRole = 9
    IdleState = 3
    InterruptedState = 4
    IOError = 2
    LinearVolumeScale = 0
    LogarithmicVolumeScale = 2
    MusicRole = 1
    NoError = 0
    NotificationRole = 5
    OpenError = 1
    RingtoneRole = 6
    SonificationRole = 8
    StoppedState = 2
    SuspendedState = 1
    UnderrunError = 3
    UnknownRole = 0
    VideoRole = 2
    VoiceCommunicationRole = 3


