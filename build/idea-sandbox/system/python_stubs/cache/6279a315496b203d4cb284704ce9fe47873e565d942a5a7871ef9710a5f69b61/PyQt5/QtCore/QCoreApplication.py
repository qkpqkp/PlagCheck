# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QObject import QObject

class QCoreApplication(QObject):
    """ QCoreApplication(List[str]) """
    def aboutToQuit(self): # real signature unknown; restored from __doc__
        """ aboutToQuit(self) [signal] """
        pass

    def addLibraryPath(self, p_str): # real signature unknown; restored from __doc__
        """ addLibraryPath(str) """
        pass

    def applicationDirPath(self): # real signature unknown; restored from __doc__
        """ applicationDirPath() -> str """
        return ""

    def applicationFilePath(self): # real signature unknown; restored from __doc__
        """ applicationFilePath() -> str """
        return ""

    def applicationName(self): # real signature unknown; restored from __doc__
        """ applicationName() -> str """
        return ""

    def applicationPid(self): # real signature unknown; restored from __doc__
        """ applicationPid() -> int """
        return 0

    def applicationVersion(self): # real signature unknown; restored from __doc__
        """ applicationVersion() -> str """
        return ""

    def arguments(self): # real signature unknown; restored from __doc__
        """ arguments() -> List[str] """
        return []

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closingDown(self): # real signature unknown; restored from __doc__
        """ closingDown() -> bool """
        return False

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def eventDispatcher(self): # real signature unknown; restored from __doc__
        """ eventDispatcher() -> QAbstractEventDispatcher """
        return QAbstractEventDispatcher

    def exec(self): # real signature unknown; restored from __doc__
        """ exec() -> int """
        return 0

    def exec_(self): # real signature unknown; restored from __doc__
        """ exec_() -> int """
        return 0

    def exit(self, returnCode=0): # real signature unknown; restored from __doc__
        """ exit(returnCode: int = 0) """
        pass

    def flush(self): # real signature unknown; restored from __doc__
        """ flush() """
        pass

    def hasPendingEvents(self): # real signature unknown; restored from __doc__
        """ hasPendingEvents() -> bool """
        return False

    def installNativeEventFilter(self, QAbstractNativeEventFilter): # real signature unknown; restored from __doc__
        """ installNativeEventFilter(self, QAbstractNativeEventFilter) """
        pass

    def installTranslator(self, QTranslator): # real signature unknown; restored from __doc__
        """ installTranslator(QTranslator) -> bool """
        return False

    def instance(self): # real signature unknown; restored from __doc__
        """ instance() -> QCoreApplication """
        return QCoreApplication

    def isQuitLockEnabled(self): # real signature unknown; restored from __doc__
        """ isQuitLockEnabled() -> bool """
        return False

    def isSetuidAllowed(self): # real signature unknown; restored from __doc__
        """ isSetuidAllowed() -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def libraryPaths(self): # real signature unknown; restored from __doc__
        """ libraryPaths() -> List[str] """
        return []

    def notify(self, QObject, QEvent): # real signature unknown; restored from __doc__
        """ notify(self, QObject, QEvent) -> bool """
        return False

    def organizationDomain(self): # real signature unknown; restored from __doc__
        """ organizationDomain() -> str """
        return ""

    def organizationName(self): # real signature unknown; restored from __doc__
        """ organizationName() -> str """
        return ""

    def postEvent(self, QObject, QEvent, priority=None): # real signature unknown; restored from __doc__
        """ postEvent(QObject, QEvent, priority: int = Qt.NormalEventPriority) """
        pass

    def processEvents(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        processEvents(flags: Union[QEventLoop.ProcessEventsFlags, QEventLoop.ProcessEventsFlag] = QEventLoop.AllEvents)
        processEvents(Union[QEventLoop.ProcessEventsFlags, QEventLoop.ProcessEventsFlag], int)
        """
        pass

    def quit(self): # real signature unknown; restored from __doc__
        """ quit() """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeLibraryPath(self, p_str): # real signature unknown; restored from __doc__
        """ removeLibraryPath(str) """
        pass

    def removeNativeEventFilter(self, QAbstractNativeEventFilter): # real signature unknown; restored from __doc__
        """ removeNativeEventFilter(self, QAbstractNativeEventFilter) """
        pass

    def removePostedEvents(self, QObject, eventType=0): # real signature unknown; restored from __doc__
        """ removePostedEvents(QObject, eventType: int = 0) """
        pass

    def removeTranslator(self, QTranslator): # real signature unknown; restored from __doc__
        """ removeTranslator(QTranslator) -> bool """
        return False

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def sendEvent(self, QObject, QEvent): # real signature unknown; restored from __doc__
        """ sendEvent(QObject, QEvent) -> bool """
        return False

    def sendPostedEvents(self, receiver=None, eventType=0): # real signature unknown; restored from __doc__
        """ sendPostedEvents(receiver: QObject = None, eventType: int = 0) """
        pass

    def setApplicationName(self, p_str): # real signature unknown; restored from __doc__
        """ setApplicationName(str) """
        pass

    def setApplicationVersion(self, p_str): # real signature unknown; restored from __doc__
        """ setApplicationVersion(str) """
        pass

    def setAttribute(self, Qt_ApplicationAttribute, on=True): # real signature unknown; restored from __doc__
        """ setAttribute(Qt.ApplicationAttribute, on: bool = True) """
        pass

    def setEventDispatcher(self, QAbstractEventDispatcher): # real signature unknown; restored from __doc__
        """ setEventDispatcher(QAbstractEventDispatcher) """
        pass

    def setLibraryPaths(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ setLibraryPaths(Iterable[str]) """
        pass

    def setOrganizationDomain(self, p_str): # real signature unknown; restored from __doc__
        """ setOrganizationDomain(str) """
        pass

    def setOrganizationName(self, p_str): # real signature unknown; restored from __doc__
        """ setOrganizationName(str) """
        pass

    def setQuitLockEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setQuitLockEnabled(bool) """
        pass

    def setSetuidAllowed(self, bool): # real signature unknown; restored from __doc__
        """ setSetuidAllowed(bool) """
        pass

    def startingUp(self): # real signature unknown; restored from __doc__
        """ startingUp() -> bool """
        return False

    def testAttribute(self, Qt_ApplicationAttribute): # real signature unknown; restored from __doc__
        """ testAttribute(Qt.ApplicationAttribute) -> bool """
        return False

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def translate(self, p_str, p_str_1, disambiguation=None, n=-1): # real signature unknown; restored from __doc__
        """ translate(str, str, disambiguation: str = None, n: int = -1) -> str """
        return ""

    def __enter__(self): # real signature unknown; restored from __doc__
        """ __enter__(self) -> object """
        return object()

    def __exit__(self, p_object, p_object_1, p_object_2): # real signature unknown; restored from __doc__
        """ __exit__(self, object, object, object) """
        pass

    def __init__(self, List, p_str=None): # real signature unknown; restored from __doc__
        pass


