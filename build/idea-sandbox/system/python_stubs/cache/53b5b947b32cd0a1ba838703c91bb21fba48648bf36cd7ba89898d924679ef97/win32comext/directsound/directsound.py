# encoding: utf-8
# module win32comext.directsound.directsound
# from C:\Users\Doly\Anaconda3\lib\site-packages\win32comext\directsound\directsound.pyd
# by generator 1.147
""" A module encapsulating the DirectSound interfaces. """
# no imports

# Variables with simple values

DS3DMODE_DISABLE = 2
DS3DMODE_HEADRELATIVE = 1
DS3DMODE_NORMAL = 0

DSBCAPS_CTRL3D = 16
DSBCAPS_CTRLFREQUENCY = 32
DSBCAPS_CTRLPAN = 64
DSBCAPS_CTRLPOSITIONNOTIFY = 256
DSBCAPS_CTRLVOLUME = 128
DSBCAPS_GETCURRENTPOSITION2 = 65536
DSBCAPS_GLOBALFOCUS = 32768
DSBCAPS_LOCHARDWARE = 4
DSBCAPS_LOCSOFTWARE = 8
DSBCAPS_MUTE3DATMAXDISTANCE = 131072
DSBCAPS_PRIMARYBUFFER = 1
DSBCAPS_STATIC = 2
DSBCAPS_STICKYFOCUS = 16384

DSBFREQUENCY_MAX = 200000
DSBFREQUENCY_MIN = 100
DSBFREQUENCY_ORIGINAL = 0

DSBLOCK_ENTIREBUFFER = 2
DSBLOCK_FROMWRITECURSOR = 1

DSBPAN_CENTER = 0
DSBPAN_LEFT = -10000
DSBPAN_RIGHT = 10000

DSBPLAY_LOOPING = 1

DSBPN_OFFSETSTOP = -1

DSBSIZE_MAX = 268435455
DSBSIZE_MIN = 4

DSBSTATUS_BUFFERLOST = 2
DSBSTATUS_LOOPING = 4
DSBSTATUS_PLAYING = 1

DSBVOLUME_MAX = 0
DSBVOLUME_MIN = -10000

DSCAPS_CERTIFIED = 64
DSCAPS_CONTINUOUSRATE = 16
DSCAPS_EMULDRIVER = 32
DSCAPS_PRIMARY16BIT = 8
DSCAPS_PRIMARY8BIT = 4
DSCAPS_PRIMARYMONO = 1
DSCAPS_PRIMARYSTEREO = 2
DSCAPS_SECONDARY16BIT = 2048
DSCAPS_SECONDARY8BIT = 1024
DSCAPS_SECONDARYMONO = 256
DSCAPS_SECONDARYSTEREO = 512

DSCBCAPS_WAVEMAPPED = -2147483648

DSCBLOCK_ENTIREBUFFER = 1

DSCBSTART_LOOPING = 1

DSCBSTATUS_CAPTURING = 1
DSCBSTATUS_LOOPING = 2

DSCCAPS_EMULDRIVER = 32

DSSCL_EXCLUSIVE = 3
DSSCL_NORMAL = 1
DSSCL_PRIORITY = 2
DSSCL_WRITEPRIMARY = 4

DSSPEAKER_GEOMETRY_MAX = 180
DSSPEAKER_GEOMETRY_MIN = 5
DSSPEAKER_GEOMETRY_NARROW = 10
DSSPEAKER_GEOMETRY_WIDE = 20

DSSPEAKER_HEADPHONE = 1
DSSPEAKER_MONO = 2
DSSPEAKER_QUAD = 3
DSSPEAKER_STEREO = 4
DSSPEAKER_SURROUND = 5

# functions

def DirectSoundCaptureCreate(*args, **kwargs): # real signature unknown
    pass

def DirectSoundCaptureEnumerate(*args, **kwargs): # real signature unknown
    pass

def DirectSoundCreate(*args, **kwargs): # real signature unknown
    pass

def DirectSoundEnumerate(*args, **kwargs): # real signature unknown
    pass

def DSBCAPS(*args, **kwargs): # real signature unknown
    pass

def DSBUFFERDESC(*args, **kwargs): # real signature unknown
    pass

def DSCAPS(*args, **kwargs): # real signature unknown
    pass

def DSCBCAPS(*args, **kwargs): # real signature unknown
    pass

def DSCBUFFERDESC(*args, **kwargs): # real signature unknown
    pass

def DSCCAPS(*args, **kwargs): # real signature unknown
    pass

# classes

class DSBCAPSType(object):
    # no doc
    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    dwBufferBytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Size of the buffer, in bytes"""

    dwFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Flags that specify buffer-object capabilities."""

    dwPlayCpuOverhead = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dwUnlockTransferRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies the rate, in kilobytes per second, at which data is transferred to the buffer memory when IDirectSoundBuffer::Update is called. High-performance applications can use this value to determine the time required for IDirectSoundBuffer::Update to execute. For software buffers located in system memory, the rate will be very high because no processing is required. For hardware buffers, the rate might be slower because the buffer might have to be downloaded to the sound card, which might have a limited transfer rate."""



class DSBUFFERDESCType(object):
    # no doc
    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    dwBufferBytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Size of the new buffer, in bytes. This value must be 0 when creating primary buffers. For secondary buffers, the minimum and maximum sizes allowed are specified by DSBSIZE_MIN and DSBSIZE_MAX"""

    dwFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the capabilities to include when creating a new DirectSoundBuffer object"""

    lpwfxFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Structure specifying the waveform format for the buffer. This value must be None for primary buffers. The application can use IDirectSoundBuffer::SetFormat to set the format of the primary buffer."""



class DSCAPSType(object):
    # no doc
    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    dwFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies device capabilities."""

    dwFreeHw3DAllBuffers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Description of the free, or unallocated, hardware 3-D positional capabilities of the device."""

    dwFreeHw3DStaticBuffers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Description of the free, or unallocated, hardware 3-D positional capabilities of the device."""

    dwFreeHw3DStreamingBuffers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Description of the free, or unallocated, hardware 3-D positional capabilities of the device."""

    dwFreeHwMemBytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Size, in bytes, of the free memory on the sound card."""

    dwFreeHwMixingAllBuffers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Description of the free mixing hardware capabilities of the device. An application can use these values to determine whether hardware resources are available for allocation to a secondary sound buffer. Also, by comparing this value to the members that specify maximum mixing capabilities, the resources that are already allocated can be determined. """

    dwFreeHwMixingStaticBuffers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Description of the free hardware mixing capabilities of the device. An application can use this value to determine whether hardware resources are available for allocation to a secondary sound buffer. Also, by comparing these values to the members that specify maximum mixing capabilities, the resources that are already allocated can be determined."""

    dwFreeHwMixingStreamingBuffers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Description of the free hardware mixing capabilities of the device. An application can use this value to determine whether hardware resources are available for allocation to a secondary sound buffer. Also, by comparing these values to the members that specify maximum mixing capabilities, the resources that are already allocated can be determined."""

    dwMaxContigFreeHwMemBytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Size, in bytes, of the largest contiguous block of free memory on the sound card."""

    dwMaxHw3DAllBuffers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Description of the hardware 3-D positional capabilities of the device."""

    dwMaxHw3DStaticBuffers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Description of the hardware 3-D positional capabilities of the device. """

    dwMaxHw3DStreamingBuffers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Description of the hardware 3-D positional capabilities of the device."""

    dwMaxHwMixingAllBuffers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies the total number of buffers that can be mixed in hardware. This member can be less than the sum of dwMaxHwMixingStaticBuffers and dwMaxHwMixingStreamingBuffers. Resource tradeoffs frequently occur."""

    dwMaxHwMixingStaticBuffers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies the maximum number of static sound buffers."""

    dwMaxHwMixingStreamingBuffers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies the maximum number of streaming sound buffers."""

    dwMaxSecondarySampleRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Maximum sample rate supported by this device's hardware secondary sound buffers."""

    dwMinSecondarySampleRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Minimum sample rate supported by this device's hardware secondary sound buffers."""

    dwPlayCpuOverheadSwBuffers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Description of the processing overhead, as a percentage of the central processing unit, needed to mix software buffers (those located in main system memory). This varies according to the bus type, the processor type, and the clock speed. The unlock transfer rate for software buffers is 0 because the data need not be transferred anywhere. Similarly, the play processing overhead for hardware buffers is 0 because the mixing is done by the sound device."""

    dwPrimaryBuffers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of primary buffers supported. This value will always be 1."""

    dwTotalHwMemBytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Size, in bytes, of the amount of memory on the sound card that stores static sound buffers."""

    dwUnlockTransferRateHwBuffers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Description of the rate, in kilobytes per second, at which data can be transferred to hardware static sound buffers. This and the number of bytes transferred determines the duration of a call to the IDirectSoundBuffer::Update method."""



class DSCBCAPSType(object):
    # no doc
    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    dwBufferBytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The size, in bytes, of the capture buffer."""

    dwFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies device capabilities. Can be 0 or DSCBCAPS_EMULDRIVER (indicates that no DirectSoundCapture device is available and standard wave audio functions are being used)"""



class DSCBUFFERDESCType(object):
    # no doc
    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    dwBufferBytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Size of the new buffer, in bytes. This value must be 0 when creating primary buffers. For secondary buffers, the minimum and maximum sizes allowed are specified by DSBSIZE_MIN and DSBSIZE_MAX"""

    dwFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies the capabilities to include when creating a new DirectSoundBuffer object"""

    lpwfxFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Structure specifying the waveform format for the buffer. This value must be None for primary buffers. The application can use IDirectSoundCaptureBuffer::SetFormat to set the format of the primary buffer."""



class DSCCAPSType(object):
    # no doc
    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    dwChannels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of channels supported by the device."""

    dwFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies device capabilities. Can be 0 or DSCCAPS_EMULDRIVER (indicates that no DirectSoundCapture device is available and standard wave audio functions are being used)"""

    dwFormats = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Supported WAVE_FORMAT formats."""



# variables with complex values

IID_IDirectSound = None # (!) real value is "IID('{279AFA83-4981-11CE-A521-0020AF0BE560}')"

IID_IDirectSoundBuffer = None # (!) real value is "IID('{279AFA85-4981-11CE-A521-0020AF0BE560}')"

IID_IDirectSoundCapture = None # (!) real value is "IID('{B0210781-89CD-11D0-AF08-00A0C925CD16}')"

IID_IDirectSoundCaptureBuffer = None # (!) real value is "IID('{B0210782-89CD-11D0-AF08-00A0C925CD16}')"

IID_IDirectSoundNotify = None # (!) real value is "IID('{B0210783-89CD-11D0-AF08-00A0C925CD16}')"

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000024E018D8160>'

__spec__ = None # (!) real value is "ModuleSpec(name='win32comext.directsound.directsound', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000024E018D8160>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\win32comext\\\\directsound\\\\directsound.pyd')"

