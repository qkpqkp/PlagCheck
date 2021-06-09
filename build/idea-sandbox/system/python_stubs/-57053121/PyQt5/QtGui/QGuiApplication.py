# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QGuiApplication(__PyQt5_QtCore.QCoreApplication):
    """ QGuiApplication(List[str]) """
    def allWindows(self): # real signature unknown; restored from __doc__
        """ allWindows() -> List[QWindow] """
        return []

    def applicationDisplayName(self): # real signature unknown; restored from __doc__
        """ applicationDisplayName() -> str """
        return ""

    def applicationDisplayNameChanged(self): # real signature unknown; restored from __doc__
        """ applicationDisplayNameChanged(self) [signal] """
        pass

    def applicationState(self): # real signature unknown; restored from __doc__
        """ applicationState() -> Qt.ApplicationState """
        pass

    def applicationStateChanged(self, Qt_ApplicationState): # real signature unknown; restored from __doc__
        """ applicationStateChanged(self, Qt.ApplicationState) [signal] """
        pass

    def changeOverrideCursor(self, Union, QCursor=None, Qt_CursorShape=None): # real signature unknown; restored from __doc__
        """ changeOverrideCursor(Union[QCursor, Qt.CursorShape]) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clipboard(self): # real signature unknown; restored from __doc__
        """ clipboard() -> QClipboard """
        return QClipboard

    def commitDataRequest(self, QSessionManager): # real signature unknown; restored from __doc__
        """ commitDataRequest(self, QSessionManager) [signal] """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def desktopFileName(self): # real signature unknown; restored from __doc__
        """ desktopFileName() -> str """
        return ""

    def desktopSettingsAware(self): # real signature unknown; restored from __doc__
        """ desktopSettingsAware() -> bool """
        return False

    def devicePixelRatio(self): # real signature unknown; restored from __doc__
        """ devicePixelRatio(self) -> float """
        return 0.0

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def exec(self): # real signature unknown; restored from __doc__
        """ exec() -> int """
        return 0

    def exec_(self): # real signature unknown; restored from __doc__
        """ exec_() -> int """
        return 0

    def focusObject(self): # real signature unknown; restored from __doc__
        """ focusObject() -> QObject """
        pass

    def focusObjectChanged(self, QObject): # real signature unknown; restored from __doc__
        """ focusObjectChanged(self, QObject) [signal] """
        pass

    def focusWindow(self): # real signature unknown; restored from __doc__
        """ focusWindow() -> QWindow """
        return QWindow

    def focusWindowChanged(self, QWindow): # real signature unknown; restored from __doc__
        """ focusWindowChanged(self, QWindow) [signal] """
        pass

    def font(self): # real signature unknown; restored from __doc__
        """ font() -> QFont """
        return QFont

    def fontChanged(self, QFont): # real signature unknown; restored from __doc__
        """ fontChanged(self, QFont) [signal] """
        pass

    def fontDatabaseChanged(self): # real signature unknown; restored from __doc__
        """ fontDatabaseChanged(self) [signal] """
        pass

    def inputMethod(self): # real signature unknown; restored from __doc__
        """ inputMethod() -> QInputMethod """
        return QInputMethod

    def isFallbackSessionManagementEnabled(self): # real signature unknown; restored from __doc__
        """ isFallbackSessionManagementEnabled() -> bool """
        return False

    def isLeftToRight(self): # real signature unknown; restored from __doc__
        """ isLeftToRight() -> bool """
        return False

    def isRightToLeft(self): # real signature unknown; restored from __doc__
        """ isRightToLeft() -> bool """
        return False

    def isSavingSession(self): # real signature unknown; restored from __doc__
        """ isSavingSession(self) -> bool """
        return False

    def isSessionRestored(self): # real signature unknown; restored from __doc__
        """ isSessionRestored(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyboardModifiers(self): # real signature unknown; restored from __doc__
        """ keyboardModifiers() -> Qt.KeyboardModifiers """
        pass

    def lastWindowClosed(self): # real signature unknown; restored from __doc__
        """ lastWindowClosed(self) [signal] """
        pass

    def layoutDirection(self): # real signature unknown; restored from __doc__
        """ layoutDirection() -> Qt.LayoutDirection """
        pass

    def layoutDirectionChanged(self, Qt_LayoutDirection): # real signature unknown; restored from __doc__
        """ layoutDirectionChanged(self, Qt.LayoutDirection) [signal] """
        pass

    def modalWindow(self): # real signature unknown; restored from __doc__
        """ modalWindow() -> QWindow """
        return QWindow

    def mouseButtons(self): # real signature unknown; restored from __doc__
        """ mouseButtons() -> Qt.MouseButtons """
        pass

    def notify(self, QObject, QEvent): # real signature unknown; restored from __doc__
        """ notify(self, QObject, QEvent) -> bool """
        return False

    def overrideCursor(self): # real signature unknown; restored from __doc__
        """ overrideCursor() -> QCursor """
        return QCursor

    def palette(self): # real signature unknown; restored from __doc__
        """ palette() -> QPalette """
        return QPalette

    def paletteChanged(self, QPalette): # real signature unknown; restored from __doc__
        """ paletteChanged(self, QPalette) [signal] """
        pass

    def platformName(self): # real signature unknown; restored from __doc__
        """ platformName() -> str """
        return ""

    def primaryScreen(self): # real signature unknown; restored from __doc__
        """ primaryScreen() -> QScreen """
        return QScreen

    def primaryScreenChanged(self, QScreen): # real signature unknown; restored from __doc__
        """ primaryScreenChanged(self, QScreen) [signal] """
        pass

    def queryKeyboardModifiers(self): # real signature unknown; restored from __doc__
        """ queryKeyboardModifiers() -> Qt.KeyboardModifiers """
        pass

    def quitOnLastWindowClosed(self): # real signature unknown; restored from __doc__
        """ quitOnLastWindowClosed() -> bool """
        return False

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def restoreOverrideCursor(self): # real signature unknown; restored from __doc__
        """ restoreOverrideCursor() """
        pass

    def saveStateRequest(self, QSessionManager): # real signature unknown; restored from __doc__
        """ saveStateRequest(self, QSessionManager) [signal] """
        pass

    def screenAdded(self, QScreen): # real signature unknown; restored from __doc__
        """ screenAdded(self, QScreen) [signal] """
        pass

    def screenAt(self, QPoint): # real signature unknown; restored from __doc__
        """ screenAt(QPoint) -> QScreen """
        return QScreen

    def screenRemoved(self, QScreen): # real signature unknown; restored from __doc__
        """ screenRemoved(self, QScreen) [signal] """
        pass

    def screens(self): # real signature unknown; restored from __doc__
        """ screens() -> List[QScreen] """
        return []

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def sessionId(self): # real signature unknown; restored from __doc__
        """ sessionId(self) -> str """
        return ""

    def sessionKey(self): # real signature unknown; restored from __doc__
        """ sessionKey(self) -> str """
        return ""

    def setApplicationDisplayName(self, p_str): # real signature unknown; restored from __doc__
        """ setApplicationDisplayName(str) """
        pass

    def setDesktopFileName(self, p_str): # real signature unknown; restored from __doc__
        """ setDesktopFileName(str) """
        pass

    def setDesktopSettingsAware(self, bool): # real signature unknown; restored from __doc__
        """ setDesktopSettingsAware(bool) """
        pass

    def setFallbackSessionManagementEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setFallbackSessionManagementEnabled(bool) """
        pass

    def setFont(self, QFont): # real signature unknown; restored from __doc__
        """ setFont(QFont) """
        pass

    def setLayoutDirection(self, Qt_LayoutDirection): # real signature unknown; restored from __doc__
        """ setLayoutDirection(Qt.LayoutDirection) """
        pass

    def setOverrideCursor(self, Union, QCursor=None, Qt_CursorShape=None): # real signature unknown; restored from __doc__
        """ setOverrideCursor(Union[QCursor, Qt.CursorShape]) """
        pass

    def setPalette(self, QPalette): # real signature unknown; restored from __doc__
        """ setPalette(QPalette) """
        pass

    def setQuitOnLastWindowClosed(self, bool): # real signature unknown; restored from __doc__
        """ setQuitOnLastWindowClosed(bool) """
        pass

    def setWindowIcon(self, QIcon): # real signature unknown; restored from __doc__
        """ setWindowIcon(QIcon) """
        pass

    def styleHints(self): # real signature unknown; restored from __doc__
        """ styleHints() -> QStyleHints """
        return QStyleHints

    def sync(self): # real signature unknown; restored from __doc__
        """ sync() """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def topLevelAt(self, QPoint): # real signature unknown; restored from __doc__
        """ topLevelAt(QPoint) -> QWindow """
        return QWindow

    def topLevelWindows(self): # real signature unknown; restored from __doc__
        """ topLevelWindows() -> List[QWindow] """
        return []

    def windowIcon(self): # real signature unknown; restored from __doc__
        """ windowIcon() -> QIcon """
        return QIcon

    def __init__(self, List, p_str=None): # real signature unknown; restored from __doc__
        pass


