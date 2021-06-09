# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QObject import QObject

class QSettings(QObject):
    """
    QSettings(str, application: str = '', parent: QObject = None)
    QSettings(QSettings.Scope, str, application: str = '', parent: QObject = None)
    QSettings(QSettings.Format, QSettings.Scope, str, application: str = '', parent: QObject = None)
    QSettings(str, QSettings.Format, parent: QObject = None)
    QSettings(parent: QObject = None)
    """
    def allKeys(self): # real signature unknown; restored from __doc__
        """ allKeys(self) -> List[str] """
        return []

    def applicationName(self): # real signature unknown; restored from __doc__
        """ applicationName(self) -> str """
        return ""

    def beginGroup(self, p_str): # real signature unknown; restored from __doc__
        """ beginGroup(self, str) """
        pass

    def beginReadArray(self, p_str): # real signature unknown; restored from __doc__
        """ beginReadArray(self, str) -> int """
        return 0

    def beginWriteArray(self, p_str, size=-1): # real signature unknown; restored from __doc__
        """ beginWriteArray(self, str, size: int = -1) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childGroups(self): # real signature unknown; restored from __doc__
        """ childGroups(self) -> List[str] """
        return []

    def childKeys(self): # real signature unknown; restored from __doc__
        """ childKeys(self) -> List[str] """
        return []

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contains(self, p_str): # real signature unknown; restored from __doc__
        """ contains(self, str) -> bool """
        return False

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultFormat(self): # real signature unknown; restored from __doc__
        """ defaultFormat() -> QSettings.Format """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def endArray(self): # real signature unknown; restored from __doc__
        """ endArray(self) """
        pass

    def endGroup(self): # real signature unknown; restored from __doc__
        """ endGroup(self) """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def fallbacksEnabled(self): # real signature unknown; restored from __doc__
        """ fallbacksEnabled(self) -> bool """
        return False

    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> QSettings.Format """
        pass

    def group(self): # real signature unknown; restored from __doc__
        """ group(self) -> str """
        return ""

    def iniCodec(self): # real signature unknown; restored from __doc__
        """ iniCodec(self) -> QTextCodec """
        return QTextCodec

    def isAtomicSyncRequired(self): # real signature unknown; restored from __doc__
        """ isAtomicSyncRequired(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isWritable(self): # real signature unknown; restored from __doc__
        """ isWritable(self) -> bool """
        return False

    def organizationName(self): # real signature unknown; restored from __doc__
        """ organizationName(self) -> str """
        return ""

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def remove(self, p_str): # real signature unknown; restored from __doc__
        """ remove(self, str) """
        pass

    def scope(self): # real signature unknown; restored from __doc__
        """ scope(self) -> QSettings.Scope """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setArrayIndex(self, p_int): # real signature unknown; restored from __doc__
        """ setArrayIndex(self, int) """
        pass

    def setAtomicSyncRequired(self, bool): # real signature unknown; restored from __doc__
        """ setAtomicSyncRequired(self, bool) """
        pass

    def setDefaultFormat(self, QSettings_Format): # real signature unknown; restored from __doc__
        """ setDefaultFormat(QSettings.Format) """
        pass

    def setFallbacksEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setFallbacksEnabled(self, bool) """
        pass

    def setIniCodec(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setIniCodec(self, QTextCodec)
        setIniCodec(self, str)
        """
        pass

    def setPath(self, QSettings_Format, QSettings_Scope, p_str): # real signature unknown; restored from __doc__
        """ setPath(QSettings.Format, QSettings.Scope, str) """
        pass

    def setValue(self, p_str, Any): # real signature unknown; restored from __doc__
        """ setValue(self, str, Any) """
        pass

    def status(self): # real signature unknown; restored from __doc__
        """ status(self) -> QSettings.Status """
        pass

    def sync(self): # real signature unknown; restored from __doc__
        """ sync(self) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def value(self, p_str, defaultValue=None, type=None): # real signature unknown; restored from __doc__
        """ value(self, str, defaultValue: Any = None, type: type = None) -> object """
        return object()

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AccessError = 1
    FormatError = 2
    IniFormat = 1
    InvalidFormat = 16
    NativeFormat = 0
    NoError = 0
    SystemScope = 1
    UserScope = 0


