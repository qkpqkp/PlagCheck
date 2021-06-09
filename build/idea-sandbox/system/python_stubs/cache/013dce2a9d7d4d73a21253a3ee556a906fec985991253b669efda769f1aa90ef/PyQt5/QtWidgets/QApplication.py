# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QApplication(__PyQt5_QtGui.QGuiApplication):
    """ QApplication(List[str]) """
    def aboutQt(self): # real signature unknown; restored from __doc__
        """ aboutQt() """
        pass

    def activeModalWidget(self): # real signature unknown; restored from __doc__
        """ activeModalWidget() -> QWidget """
        return QWidget

    def activePopupWidget(self): # real signature unknown; restored from __doc__
        """ activePopupWidget() -> QWidget """
        return QWidget

    def activeWindow(self): # real signature unknown; restored from __doc__
        """ activeWindow() -> QWidget """
        return QWidget

    def alert(self, QWidget, msecs=0): # real signature unknown; restored from __doc__
        """ alert(QWidget, msecs: int = 0) """
        pass

    def allWidgets(self): # real signature unknown; restored from __doc__
        """ allWidgets() -> List[QWidget] """
        return []

    def autoSipEnabled(self): # real signature unknown; restored from __doc__
        """ autoSipEnabled(self) -> bool """
        return False

    def beep(self): # real signature unknown; restored from __doc__
        """ beep() """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeAllWindows(self): # real signature unknown; restored from __doc__
        """ closeAllWindows() """
        pass

    def colorSpec(self): # real signature unknown; restored from __doc__
        """ colorSpec() -> int """
        return 0

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def cursorFlashTime(self): # real signature unknown; restored from __doc__
        """ cursorFlashTime() -> int """
        return 0

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def desktop(self): # real signature unknown; restored from __doc__
        """ desktop() -> QDesktopWidget """
        return QDesktopWidget

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def doubleClickInterval(self): # real signature unknown; restored from __doc__
        """ doubleClickInterval() -> int """
        return 0

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def exec(self): # real signature unknown; restored from __doc__
        """ exec() -> int """
        return 0

    def exec_(self): # real signature unknown; restored from __doc__
        """ exec_() -> int """
        return 0

    def focusChanged(self, QWidget, QWidget_1): # real signature unknown; restored from __doc__
        """ focusChanged(self, QWidget, QWidget) [signal] """
        pass

    def focusWidget(self): # real signature unknown; restored from __doc__
        """ focusWidget() -> QWidget """
        return QWidget

    def font(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        font() -> QFont
        font(QWidget) -> QFont
        font(str) -> QFont
        """
        pass

    def fontMetrics(self): # real signature unknown; restored from __doc__
        """ fontMetrics() -> QFontMetrics """
        pass

    def globalStrut(self): # real signature unknown; restored from __doc__
        """ globalStrut() -> QSize """
        pass

    def isEffectEnabled(self, Qt_UIEffect): # real signature unknown; restored from __doc__
        """ isEffectEnabled(Qt.UIEffect) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyboardInputInterval(self): # real signature unknown; restored from __doc__
        """ keyboardInputInterval() -> int """
        return 0

    def notify(self, QObject, QEvent): # real signature unknown; restored from __doc__
        """ notify(self, QObject, QEvent) -> bool """
        return False

    def palette(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        palette() -> QPalette
        palette(QWidget) -> QPalette
        palette(str) -> QPalette
        """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setActiveWindow(self, QWidget): # real signature unknown; restored from __doc__
        """ setActiveWindow(QWidget) """
        pass

    def setAutoSipEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setAutoSipEnabled(self, bool) """
        pass

    def setColorSpec(self, p_int): # real signature unknown; restored from __doc__
        """ setColorSpec(int) """
        pass

    def setCursorFlashTime(self, p_int): # real signature unknown; restored from __doc__
        """ setCursorFlashTime(int) """
        pass

    def setDoubleClickInterval(self, p_int): # real signature unknown; restored from __doc__
        """ setDoubleClickInterval(int) """
        pass

    def setEffectEnabled(self, Qt_UIEffect, enabled=True): # real signature unknown; restored from __doc__
        """ setEffectEnabled(Qt.UIEffect, enabled: bool = True) """
        pass

    def setFont(self, QFont, className=None): # real signature unknown; restored from __doc__
        """ setFont(QFont, className: str = None) """
        pass

    def setGlobalStrut(self, QSize): # real signature unknown; restored from __doc__
        """ setGlobalStrut(QSize) """
        pass

    def setKeyboardInputInterval(self, p_int): # real signature unknown; restored from __doc__
        """ setKeyboardInputInterval(int) """
        pass

    def setPalette(self, QPalette, className=None): # real signature unknown; restored from __doc__
        """ setPalette(QPalette, className: str = None) """
        pass

    def setStartDragDistance(self, p_int): # real signature unknown; restored from __doc__
        """ setStartDragDistance(int) """
        pass

    def setStartDragTime(self, p_int): # real signature unknown; restored from __doc__
        """ setStartDragTime(int) """
        pass

    def setStyle(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setStyle(QStyle)
        setStyle(str) -> QStyle
        """
        return QStyle

    def setStyleSheet(self, p_str): # real signature unknown; restored from __doc__
        """ setStyleSheet(self, str) """
        pass

    def setWheelScrollLines(self, p_int): # real signature unknown; restored from __doc__
        """ setWheelScrollLines(int) """
        pass

    def setWindowIcon(self, QIcon): # real signature unknown; restored from __doc__
        """ setWindowIcon(QIcon) """
        pass

    def startDragDistance(self): # real signature unknown; restored from __doc__
        """ startDragDistance() -> int """
        return 0

    def startDragTime(self): # real signature unknown; restored from __doc__
        """ startDragTime() -> int """
        return 0

    def style(self): # real signature unknown; restored from __doc__
        """ style() -> QStyle """
        return QStyle

    def styleSheet(self): # real signature unknown; restored from __doc__
        """ styleSheet(self) -> str """
        return ""

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def topLevelAt(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        topLevelAt(QPoint) -> QWidget
        topLevelAt(int, int) -> QWidget
        """
        return QWidget

    def topLevelWidgets(self): # real signature unknown; restored from __doc__
        """ topLevelWidgets() -> List[QWidget] """
        return []

    def wheelScrollLines(self): # real signature unknown; restored from __doc__
        """ wheelScrollLines() -> int """
        return 0

    def widgetAt(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        widgetAt(QPoint) -> QWidget
        widgetAt(int, int) -> QWidget
        """
        return QWidget

    def windowIcon(self): # real signature unknown; restored from __doc__
        """ windowIcon() -> QIcon """
        pass

    def __init__(self, List, p_str=None): # real signature unknown; restored from __doc__
        pass

    CustomColor = 1
    ManyColor = 2
    NormalColor = 0


