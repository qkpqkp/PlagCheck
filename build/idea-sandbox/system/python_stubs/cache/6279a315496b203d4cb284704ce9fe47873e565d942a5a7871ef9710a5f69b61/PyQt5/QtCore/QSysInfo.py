# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QSysInfo(__sip.simplewrapper):
    """
    QSysInfo()
    QSysInfo(QSysInfo)
    """
    def buildAbi(self): # real signature unknown; restored from __doc__
        """ buildAbi() -> str """
        return ""

    def buildCpuArchitecture(self): # real signature unknown; restored from __doc__
        """ buildCpuArchitecture() -> str """
        return ""

    def currentCpuArchitecture(self): # real signature unknown; restored from __doc__
        """ currentCpuArchitecture() -> str """
        return ""

    def kernelType(self): # real signature unknown; restored from __doc__
        """ kernelType() -> str """
        return ""

    def kernelVersion(self): # real signature unknown; restored from __doc__
        """ kernelVersion() -> str """
        return ""

    def machineHostName(self): # real signature unknown; restored from __doc__
        """ machineHostName() -> str """
        return ""

    def prettyProductName(self): # real signature unknown; restored from __doc__
        """ prettyProductName() -> str """
        return ""

    def productType(self): # real signature unknown; restored from __doc__
        """ productType() -> str """
        return ""

    def productVersion(self): # real signature unknown; restored from __doc__
        """ productVersion() -> str """
        return ""

    def windowsVersion(self): # real signature unknown; restored from __doc__
        """ windowsVersion() -> QSysInfo.WinVersion """
        pass

    def __init__(self, QSysInfo=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    BigEndian = 0
    ByteOrder = 1
    LittleEndian = 1
    WindowsVersion = 192
    WordSize = 64
    WV_10_0 = 192
    WV_2000 = 32
    WV_2003 = 64
    WV_32s = 1
    WV_4_0 = 16
    WV_5_0 = 32
    WV_5_1 = 48
    WV_5_2 = 64
    WV_6_0 = 128
    WV_6_1 = 144
    WV_6_2 = 160
    WV_6_3 = 176
    WV_95 = 2
    WV_98 = 3
    WV_CE = 256
    WV_CENET = 512
    WV_CE_5 = 768
    WV_CE_6 = 1024
    WV_CE_based = 3840
    WV_DOS_based = 15
    WV_Me = 4
    WV_NT = 16
    WV_NT_based = 240
    WV_VISTA = 128
    WV_WINDOWS10 = 192
    WV_WINDOWS7 = 144
    WV_WINDOWS8 = 160
    WV_WINDOWS8_1 = 176
    WV_XP = 48


