# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QSurface import QSurface

class QWindow(__PyQt5_QtCore.QObject, QSurface):
    """
    QWindow(screen: QScreen = None)
    QWindow(QWindow)
    """
    def activeChanged(self): # real signature unknown; restored from __doc__
        """ activeChanged(self) [signal] """
        pass

    def alert(self, p_int): # real signature unknown; restored from __doc__
        """ alert(self, int) """
        pass

    def baseSize(self): # real signature unknown; restored from __doc__
        """ baseSize(self) -> QSize """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) -> bool """
        return False

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contentOrientation(self): # real signature unknown; restored from __doc__
        """ contentOrientation(self) -> Qt.ScreenOrientation """
        pass

    def contentOrientationChanged(self, Qt_ScreenOrientation): # real signature unknown; restored from __doc__
        """ contentOrientationChanged(self, Qt.ScreenOrientation) [signal] """
        pass

    def create(self): # real signature unknown; restored from __doc__
        """ create(self) """
        pass

    def cursor(self): # real signature unknown; restored from __doc__
        """ cursor(self) -> QCursor """
        return QCursor

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self): # real signature unknown; restored from __doc__
        """ destroy(self) """
        pass

    def devicePixelRatio(self): # real signature unknown; restored from __doc__
        """ devicePixelRatio(self) -> float """
        return 0.0

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def exposeEvent(self, QExposeEvent): # real signature unknown; restored from __doc__
        """ exposeEvent(self, QExposeEvent) """
        pass

    def filePath(self): # real signature unknown; restored from __doc__
        """ filePath(self) -> str """
        return ""

    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> Qt.WindowFlags """
        pass

    def focusInEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ focusInEvent(self, QFocusEvent) """
        pass

    def focusObject(self): # real signature unknown; restored from __doc__
        """ focusObject(self) -> QObject """
        pass

    def focusObjectChanged(self, QObject): # real signature unknown; restored from __doc__
        """ focusObjectChanged(self, QObject) [signal] """
        pass

    def focusOutEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, QFocusEvent) """
        pass

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> QSurfaceFormat """
        return QSurfaceFormat

    def frameGeometry(self): # real signature unknown; restored from __doc__
        """ frameGeometry(self) -> QRect """
        pass

    def frameMargins(self): # real signature unknown; restored from __doc__
        """ frameMargins(self) -> QMargins """
        pass

    def framePosition(self): # real signature unknown; restored from __doc__
        """ framePosition(self) -> QPoint """
        pass

    def fromWinId(self, sip_voidptr): # real signature unknown; restored from __doc__
        """ fromWinId(sip.voidptr) -> QWindow """
        return QWindow

    def geometry(self): # real signature unknown; restored from __doc__
        """ geometry(self) -> QRect """
        pass

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> int """
        return 0

    def heightChanged(self, p_int): # real signature unknown; restored from __doc__
        """ heightChanged(self, int) [signal] """
        pass

    def hide(self): # real signature unknown; restored from __doc__
        """ hide(self) """
        pass

    def hideEvent(self, QHideEvent): # real signature unknown; restored from __doc__
        """ hideEvent(self, QHideEvent) """
        pass

    def icon(self): # real signature unknown; restored from __doc__
        """ icon(self) -> QIcon """
        return QIcon

    def isActive(self): # real signature unknown; restored from __doc__
        """ isActive(self) -> bool """
        return False

    def isAncestorOf(self, QWindow, mode=None): # real signature unknown; restored from __doc__
        """ isAncestorOf(self, QWindow, mode: QWindow.AncestorMode = QWindow.IncludeTransients) -> bool """
        return False

    def isExposed(self): # real signature unknown; restored from __doc__
        """ isExposed(self) -> bool """
        return False

    def isModal(self): # real signature unknown; restored from __doc__
        """ isModal(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isTopLevel(self): # real signature unknown; restored from __doc__
        """ isTopLevel(self) -> bool """
        return False

    def isVisible(self): # real signature unknown; restored from __doc__
        """ isVisible(self) -> bool """
        return False

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, QKeyEvent) """
        pass

    def keyReleaseEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, QKeyEvent) """
        pass

    def lower(self): # real signature unknown; restored from __doc__
        """ lower(self) """
        pass

    def mapFromGlobal(self, QPoint): # real signature unknown; restored from __doc__
        """ mapFromGlobal(self, QPoint) -> QPoint """
        pass

    def mapToGlobal(self, QPoint): # real signature unknown; restored from __doc__
        """ mapToGlobal(self, QPoint) -> QPoint """
        pass

    def mask(self): # real signature unknown; restored from __doc__
        """ mask(self) -> QRegion """
        return QRegion

    def maximumHeight(self): # real signature unknown; restored from __doc__
        """ maximumHeight(self) -> int """
        return 0

    def maximumHeightChanged(self, p_int): # real signature unknown; restored from __doc__
        """ maximumHeightChanged(self, int) [signal] """
        pass

    def maximumSize(self): # real signature unknown; restored from __doc__
        """ maximumSize(self) -> QSize """
        pass

    def maximumWidth(self): # real signature unknown; restored from __doc__
        """ maximumWidth(self) -> int """
        return 0

    def maximumWidthChanged(self, p_int): # real signature unknown; restored from __doc__
        """ maximumWidthChanged(self, int) [signal] """
        pass

    def minimumHeight(self): # real signature unknown; restored from __doc__
        """ minimumHeight(self) -> int """
        return 0

    def minimumHeightChanged(self, p_int): # real signature unknown; restored from __doc__
        """ minimumHeightChanged(self, int) [signal] """
        pass

    def minimumSize(self): # real signature unknown; restored from __doc__
        """ minimumSize(self) -> QSize """
        pass

    def minimumWidth(self): # real signature unknown; restored from __doc__
        """ minimumWidth(self) -> int """
        return 0

    def minimumWidthChanged(self, p_int): # real signature unknown; restored from __doc__
        """ minimumWidthChanged(self, int) [signal] """
        pass

    def modality(self): # real signature unknown; restored from __doc__
        """ modality(self) -> Qt.WindowModality """
        pass

    def modalityChanged(self, Qt_WindowModality): # real signature unknown; restored from __doc__
        """ modalityChanged(self, Qt.WindowModality) [signal] """
        pass

    def mouseDoubleClickEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mouseDoubleClickEvent(self, QMouseEvent) """
        pass

    def mouseMoveEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mouseMoveEvent(self, QMouseEvent) """
        pass

    def mousePressEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, QMouseEvent) """
        pass

    def mouseReleaseEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, QMouseEvent) """
        pass

    def moveEvent(self, QMoveEvent): # real signature unknown; restored from __doc__
        """ moveEvent(self, QMoveEvent) """
        pass

    def opacity(self): # real signature unknown; restored from __doc__
        """ opacity(self) -> float """
        return 0.0

    def opacityChanged(self, p_float): # real signature unknown; restored from __doc__
        """ opacityChanged(self, float) [signal] """
        pass

    def parent(self, QWindow_AncestorMode=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        parent(self) -> QWindow
        parent(self, QWindow.AncestorMode) -> QWindow
        """
        return QWindow

    def position(self): # real signature unknown; restored from __doc__
        """ position(self) -> QPoint """
        pass

    def raise_(self): # real signature unknown; restored from __doc__
        """ raise_(self) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def reportContentOrientationChange(self, Qt_ScreenOrientation): # real signature unknown; restored from __doc__
        """ reportContentOrientationChange(self, Qt.ScreenOrientation) """
        pass

    def requestActivate(self): # real signature unknown; restored from __doc__
        """ requestActivate(self) """
        pass

    def requestedFormat(self): # real signature unknown; restored from __doc__
        """ requestedFormat(self) -> QSurfaceFormat """
        return QSurfaceFormat

    def requestUpdate(self): # real signature unknown; restored from __doc__
        """ requestUpdate(self) """
        pass

    def resize(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        resize(self, QSize)
        resize(self, int, int)
        """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ resizeEvent(self, QResizeEvent) """
        pass

    def screen(self): # real signature unknown; restored from __doc__
        """ screen(self) -> QScreen """
        return QScreen

    def screenChanged(self, QScreen): # real signature unknown; restored from __doc__
        """ screenChanged(self, QScreen) [signal] """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setBaseSize(self, QSize): # real signature unknown; restored from __doc__
        """ setBaseSize(self, QSize) """
        pass

    def setCursor(self, Union, QCursor=None, Qt_CursorShape=None): # real signature unknown; restored from __doc__
        """ setCursor(self, Union[QCursor, Qt.CursorShape]) """
        pass

    def setFilePath(self, p_str): # real signature unknown; restored from __doc__
        """ setFilePath(self, str) """
        pass

    def setFlag(self, Qt_WindowType, on=True): # real signature unknown; restored from __doc__
        """ setFlag(self, Qt.WindowType, on: bool = True) """
        pass

    def setFlags(self, Union, Qt_WindowFlags=None, Qt_WindowType=None): # real signature unknown; restored from __doc__
        """ setFlags(self, Union[Qt.WindowFlags, Qt.WindowType]) """
        pass

    def setFormat(self, QSurfaceFormat): # real signature unknown; restored from __doc__
        """ setFormat(self, QSurfaceFormat) """
        pass

    def setFramePosition(self, QPoint): # real signature unknown; restored from __doc__
        """ setFramePosition(self, QPoint) """
        pass

    def setGeometry(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setGeometry(self, int, int, int, int)
        setGeometry(self, QRect)
        """
        pass

    def setHeight(self, p_int): # real signature unknown; restored from __doc__
        """ setHeight(self, int) """
        pass

    def setIcon(self, QIcon): # real signature unknown; restored from __doc__
        """ setIcon(self, QIcon) """
        pass

    def setKeyboardGrabEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setKeyboardGrabEnabled(self, bool) -> bool """
        return False

    def setMask(self, QRegion): # real signature unknown; restored from __doc__
        """ setMask(self, QRegion) """
        pass

    def setMaximumHeight(self, p_int): # real signature unknown; restored from __doc__
        """ setMaximumHeight(self, int) """
        pass

    def setMaximumSize(self, QSize): # real signature unknown; restored from __doc__
        """ setMaximumSize(self, QSize) """
        pass

    def setMaximumWidth(self, p_int): # real signature unknown; restored from __doc__
        """ setMaximumWidth(self, int) """
        pass

    def setMinimumHeight(self, p_int): # real signature unknown; restored from __doc__
        """ setMinimumHeight(self, int) """
        pass

    def setMinimumSize(self, QSize): # real signature unknown; restored from __doc__
        """ setMinimumSize(self, QSize) """
        pass

    def setMinimumWidth(self, p_int): # real signature unknown; restored from __doc__
        """ setMinimumWidth(self, int) """
        pass

    def setModality(self, Qt_WindowModality): # real signature unknown; restored from __doc__
        """ setModality(self, Qt.WindowModality) """
        pass

    def setMouseGrabEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setMouseGrabEnabled(self, bool) -> bool """
        return False

    def setOpacity(self, p_float): # real signature unknown; restored from __doc__
        """ setOpacity(self, float) """
        pass

    def setParent(self, QWindow): # real signature unknown; restored from __doc__
        """ setParent(self, QWindow) """
        pass

    def setPosition(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setPosition(self, QPoint)
        setPosition(self, int, int)
        """
        pass

    def setScreen(self, QScreen): # real signature unknown; restored from __doc__
        """ setScreen(self, QScreen) """
        pass

    def setSizeIncrement(self, QSize): # real signature unknown; restored from __doc__
        """ setSizeIncrement(self, QSize) """
        pass

    def setSurfaceType(self, QSurface_SurfaceType): # real signature unknown; restored from __doc__
        """ setSurfaceType(self, QSurface.SurfaceType) """
        pass

    def setTitle(self, p_str): # real signature unknown; restored from __doc__
        """ setTitle(self, str) """
        pass

    def setTransientParent(self, QWindow): # real signature unknown; restored from __doc__
        """ setTransientParent(self, QWindow) """
        pass

    def setVisibility(self, QWindow_Visibility): # real signature unknown; restored from __doc__
        """ setVisibility(self, QWindow.Visibility) """
        pass

    def setVisible(self, bool): # real signature unknown; restored from __doc__
        """ setVisible(self, bool) """
        pass

    def setWidth(self, p_int): # real signature unknown; restored from __doc__
        """ setWidth(self, int) """
        pass

    def setWindowState(self, Qt_WindowState): # real signature unknown; restored from __doc__
        """ setWindowState(self, Qt.WindowState) """
        pass

    def setWindowStates(self, Union, Qt_WindowStates=None, Qt_WindowState=None): # real signature unknown; restored from __doc__
        """ setWindowStates(self, Union[Qt.WindowStates, Qt.WindowState]) """
        pass

    def setX(self, p_int): # real signature unknown; restored from __doc__
        """ setX(self, int) """
        pass

    def setY(self, p_int): # real signature unknown; restored from __doc__
        """ setY(self, int) """
        pass

    def show(self): # real signature unknown; restored from __doc__
        """ show(self) """
        pass

    def showEvent(self, QShowEvent): # real signature unknown; restored from __doc__
        """ showEvent(self, QShowEvent) """
        pass

    def showFullScreen(self): # real signature unknown; restored from __doc__
        """ showFullScreen(self) """
        pass

    def showMaximized(self): # real signature unknown; restored from __doc__
        """ showMaximized(self) """
        pass

    def showMinimized(self): # real signature unknown; restored from __doc__
        """ showMinimized(self) """
        pass

    def showNormal(self): # real signature unknown; restored from __doc__
        """ showNormal(self) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> QSize """
        pass

    def sizeIncrement(self): # real signature unknown; restored from __doc__
        """ sizeIncrement(self) -> QSize """
        pass

    def surfaceType(self): # real signature unknown; restored from __doc__
        """ surfaceType(self) -> QSurface.SurfaceType """
        pass

    def tabletEvent(self, QTabletEvent): # real signature unknown; restored from __doc__
        """ tabletEvent(self, QTabletEvent) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def title(self): # real signature unknown; restored from __doc__
        """ title(self) -> str """
        return ""

    def touchEvent(self, QTouchEvent): # real signature unknown; restored from __doc__
        """ touchEvent(self, QTouchEvent) """
        pass

    def transientParent(self): # real signature unknown; restored from __doc__
        """ transientParent(self) -> QWindow """
        return QWindow

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> Qt.WindowType """
        pass

    def unsetCursor(self): # real signature unknown; restored from __doc__
        """ unsetCursor(self) """
        pass

    def visibility(self): # real signature unknown; restored from __doc__
        """ visibility(self) -> QWindow.Visibility """
        pass

    def visibilityChanged(self, QWindow_Visibility): # real signature unknown; restored from __doc__
        """ visibilityChanged(self, QWindow.Visibility) [signal] """
        pass

    def visibleChanged(self, bool): # real signature unknown; restored from __doc__
        """ visibleChanged(self, bool) [signal] """
        pass

    def wheelEvent(self, QWheelEvent): # real signature unknown; restored from __doc__
        """ wheelEvent(self, QWheelEvent) """
        pass

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> int """
        return 0

    def widthChanged(self, p_int): # real signature unknown; restored from __doc__
        """ widthChanged(self, int) [signal] """
        pass

    def windowState(self): # real signature unknown; restored from __doc__
        """ windowState(self) -> Qt.WindowState """
        pass

    def windowStateChanged(self, Qt_WindowState): # real signature unknown; restored from __doc__
        """ windowStateChanged(self, Qt.WindowState) [signal] """
        pass

    def windowStates(self): # real signature unknown; restored from __doc__
        """ windowStates(self) -> Qt.WindowStates """
        pass

    def windowTitleChanged(self, p_str): # real signature unknown; restored from __doc__
        """ windowTitleChanged(self, str) [signal] """
        pass

    def winId(self): # real signature unknown; restored from __doc__
        """ winId(self) -> sip.voidptr """
        pass

    def x(self): # real signature unknown; restored from __doc__
        """ x(self) -> int """
        return 0

    def xChanged(self, p_int): # real signature unknown; restored from __doc__
        """ xChanged(self, int) [signal] """
        pass

    def y(self): # real signature unknown; restored from __doc__
        """ y(self) -> int """
        return 0

    def yChanged(self, p_int): # real signature unknown; restored from __doc__
        """ yChanged(self, int) [signal] """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AutomaticVisibility = 1
    ExcludeTransients = 0
    FullScreen = 5
    Hidden = 0
    IncludeTransients = 1
    Maximized = 4
    Minimized = 3
    Windowed = 2


