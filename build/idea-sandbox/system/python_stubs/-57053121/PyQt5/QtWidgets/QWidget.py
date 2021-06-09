# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QWidget(__PyQt5_QtCore.QObject, __PyQt5_QtGui.QPaintDevice):
    """ QWidget(parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()) """
    def acceptDrops(self): # real signature unknown; restored from __doc__
        """ acceptDrops(self) -> bool """
        return False

    def accessibleDescription(self): # real signature unknown; restored from __doc__
        """ accessibleDescription(self) -> str """
        return ""

    def accessibleName(self): # real signature unknown; restored from __doc__
        """ accessibleName(self) -> str """
        return ""

    def actionEvent(self, QActionEvent): # real signature unknown; restored from __doc__
        """ actionEvent(self, QActionEvent) """
        pass

    def actions(self): # real signature unknown; restored from __doc__
        """ actions(self) -> List[QAction] """
        return []

    def activateWindow(self): # real signature unknown; restored from __doc__
        """ activateWindow(self) """
        pass

    def addAction(self, QAction): # real signature unknown; restored from __doc__
        """ addAction(self, QAction) """
        pass

    def addActions(self, Iterable, QAction=None): # real signature unknown; restored from __doc__
        """ addActions(self, Iterable[QAction]) """
        pass

    def adjustSize(self): # real signature unknown; restored from __doc__
        """ adjustSize(self) """
        pass

    def autoFillBackground(self): # real signature unknown; restored from __doc__
        """ autoFillBackground(self) -> bool """
        return False

    def backgroundRole(self): # real signature unknown; restored from __doc__
        """ backgroundRole(self) -> QPalette.ColorRole """
        pass

    def baseSize(self): # real signature unknown; restored from __doc__
        """ baseSize(self) -> QSize """
        pass

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ changeEvent(self, QEvent) """
        pass

    def childAt(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        childAt(self, QPoint) -> QWidget
        childAt(self, int, int) -> QWidget
        """
        return QWidget

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childrenRect(self): # real signature unknown; restored from __doc__
        """ childrenRect(self) -> QRect """
        pass

    def childrenRegion(self): # real signature unknown; restored from __doc__
        """ childrenRegion(self) -> QRegion """
        pass

    def clearFocus(self): # real signature unknown; restored from __doc__
        """ clearFocus(self) """
        pass

    def clearMask(self): # real signature unknown; restored from __doc__
        """ clearMask(self) """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) -> bool """
        return False

    def closeEvent(self, QCloseEvent): # real signature unknown; restored from __doc__
        """ closeEvent(self, QCloseEvent) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contentsMargins(self): # real signature unknown; restored from __doc__
        """ contentsMargins(self) -> QMargins """
        pass

    def contentsRect(self): # real signature unknown; restored from __doc__
        """ contentsRect(self) -> QRect """
        pass

    def contextMenuEvent(self, QContextMenuEvent): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, QContextMenuEvent) """
        pass

    def contextMenuPolicy(self): # real signature unknown; restored from __doc__
        """ contextMenuPolicy(self) -> Qt.ContextMenuPolicy """
        pass

    def create(self, window=0, initializeWindow=True, destroyOldWindow=True): # real signature unknown; restored from __doc__
        """ create(self, window: sip.voidptr = 0, initializeWindow: bool = True, destroyOldWindow: bool = True) """
        pass

    def createWindowContainer(self, QWindow, parent=None, flags, Qt_WindowFlags=None, Qt_WindowType=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ createWindowContainer(QWindow, parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = 0) -> QWidget """
        pass

    def cursor(self): # real signature unknown; restored from __doc__
        """ cursor(self) -> QCursor """
        pass

    def customContextMenuRequested(self, QPoint): # real signature unknown; restored from __doc__
        """ customContextMenuRequested(self, QPoint) [signal] """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, destroyWindow=True, destroySubWindows=True): # real signature unknown; restored from __doc__
        """ destroy(self, destroyWindow: bool = True, destroySubWindows: bool = True) """
        pass

    def devType(self): # real signature unknown; restored from __doc__
        """ devType(self) -> int """
        return 0

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dragEnterEvent(self, QDragEnterEvent): # real signature unknown; restored from __doc__
        """ dragEnterEvent(self, QDragEnterEvent) """
        pass

    def dragLeaveEvent(self, QDragLeaveEvent): # real signature unknown; restored from __doc__
        """ dragLeaveEvent(self, QDragLeaveEvent) """
        pass

    def dragMoveEvent(self, QDragMoveEvent): # real signature unknown; restored from __doc__
        """ dragMoveEvent(self, QDragMoveEvent) """
        pass

    def dropEvent(self, QDropEvent): # real signature unknown; restored from __doc__
        """ dropEvent(self, QDropEvent) """
        pass

    def effectiveWinId(self): # real signature unknown; restored from __doc__
        """ effectiveWinId(self) -> sip.voidptr """
        pass

    def ensurePolished(self): # real signature unknown; restored from __doc__
        """ ensurePolished(self) """
        pass

    def enterEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ enterEvent(self, QEvent) """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def find(self, sip_voidptr): # real signature unknown; restored from __doc__
        """ find(sip.voidptr) -> QWidget """
        return QWidget

    def focusInEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ focusInEvent(self, QFocusEvent) """
        pass

    def focusNextChild(self): # real signature unknown; restored from __doc__
        """ focusNextChild(self) -> bool """
        return False

    def focusNextPrevChild(self, bool): # real signature unknown; restored from __doc__
        """ focusNextPrevChild(self, bool) -> bool """
        return False

    def focusOutEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, QFocusEvent) """
        pass

    def focusPolicy(self): # real signature unknown; restored from __doc__
        """ focusPolicy(self) -> Qt.FocusPolicy """
        pass

    def focusPreviousChild(self): # real signature unknown; restored from __doc__
        """ focusPreviousChild(self) -> bool """
        return False

    def focusProxy(self): # real signature unknown; restored from __doc__
        """ focusProxy(self) -> QWidget """
        return QWidget

    def focusWidget(self): # real signature unknown; restored from __doc__
        """ focusWidget(self) -> QWidget """
        return QWidget

    def font(self): # real signature unknown; restored from __doc__
        """ font(self) -> QFont """
        pass

    def fontInfo(self): # real signature unknown; restored from __doc__
        """ fontInfo(self) -> QFontInfo """
        pass

    def fontMetrics(self): # real signature unknown; restored from __doc__
        """ fontMetrics(self) -> QFontMetrics """
        pass

    def foregroundRole(self): # real signature unknown; restored from __doc__
        """ foregroundRole(self) -> QPalette.ColorRole """
        pass

    def frameGeometry(self): # real signature unknown; restored from __doc__
        """ frameGeometry(self) -> QRect """
        pass

    def frameSize(self): # real signature unknown; restored from __doc__
        """ frameSize(self) -> QSize """
        pass

    def geometry(self): # real signature unknown; restored from __doc__
        """ geometry(self) -> QRect """
        pass

    def getContentsMargins(self): # real signature unknown; restored from __doc__
        """ getContentsMargins(self) -> Tuple[int, int, int, int] """
        pass

    def grab(self, rectangle=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ grab(self, rectangle: QRect = QRect(QPoint(0,0),QSize(-1,-1))) -> QPixmap """
        pass

    def grabGesture(self, Qt_GestureType, flags, Qt_GestureFlags=None, Qt_GestureFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ grabGesture(self, Qt.GestureType, flags: Union[Qt.GestureFlags, Qt.GestureFlag] = Qt.GestureFlags()) """
        pass

    def grabKeyboard(self): # real signature unknown; restored from __doc__
        """ grabKeyboard(self) """
        pass

    def grabMouse(self, Union=None, QCursor=None, Qt_CursorShape=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        grabMouse(self)
        grabMouse(self, Union[QCursor, Qt.CursorShape])
        """
        pass

    def grabShortcut(self, Union, QKeySequence=None, QKeySequence_StandardKey=None, p_str=None, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ grabShortcut(self, Union[QKeySequence, QKeySequence.StandardKey, str, int], context: Qt.ShortcutContext = Qt.WindowShortcut) -> int """
        pass

    def graphicsEffect(self): # real signature unknown; restored from __doc__
        """ graphicsEffect(self) -> QGraphicsEffect """
        return QGraphicsEffect

    def graphicsProxyWidget(self): # real signature unknown; restored from __doc__
        """ graphicsProxyWidget(self) -> QGraphicsProxyWidget """
        return QGraphicsProxyWidget

    def hasFocus(self): # real signature unknown; restored from __doc__
        """ hasFocus(self) -> bool """
        return False

    def hasHeightForWidth(self): # real signature unknown; restored from __doc__
        """ hasHeightForWidth(self) -> bool """
        return False

    def hasMouseTracking(self): # real signature unknown; restored from __doc__
        """ hasMouseTracking(self) -> bool """
        return False

    def hasTabletTracking(self): # real signature unknown; restored from __doc__
        """ hasTabletTracking(self) -> bool """
        return False

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> int """
        return 0

    def heightForWidth(self, p_int): # real signature unknown; restored from __doc__
        """ heightForWidth(self, int) -> int """
        return 0

    def hide(self): # real signature unknown; restored from __doc__
        """ hide(self) """
        pass

    def hideEvent(self, QHideEvent): # real signature unknown; restored from __doc__
        """ hideEvent(self, QHideEvent) """
        pass

    def initPainter(self, QPainter): # real signature unknown; restored from __doc__
        """ initPainter(self, QPainter) """
        pass

    def inputMethodEvent(self, QInputMethodEvent): # real signature unknown; restored from __doc__
        """ inputMethodEvent(self, QInputMethodEvent) """
        pass

    def inputMethodHints(self): # real signature unknown; restored from __doc__
        """ inputMethodHints(self) -> Qt.InputMethodHints """
        pass

    def inputMethodQuery(self, Qt_InputMethodQuery): # real signature unknown; restored from __doc__
        """ inputMethodQuery(self, Qt.InputMethodQuery) -> Any """
        pass

    def insertAction(self, QAction, QAction_1): # real signature unknown; restored from __doc__
        """ insertAction(self, QAction, QAction) """
        pass

    def insertActions(self, QAction, Iterable, QAction=None): # real signature unknown; restored from __doc__
        """ insertActions(self, QAction, Iterable[QAction]) """
        pass

    def isActiveWindow(self): # real signature unknown; restored from __doc__
        """ isActiveWindow(self) -> bool """
        return False

    def isAncestorOf(self, QWidget): # real signature unknown; restored from __doc__
        """ isAncestorOf(self, QWidget) -> bool """
        return False

    def isEnabled(self): # real signature unknown; restored from __doc__
        """ isEnabled(self) -> bool """
        return False

    def isEnabledTo(self, QWidget): # real signature unknown; restored from __doc__
        """ isEnabledTo(self, QWidget) -> bool """
        return False

    def isFullScreen(self): # real signature unknown; restored from __doc__
        """ isFullScreen(self) -> bool """
        return False

    def isHidden(self): # real signature unknown; restored from __doc__
        """ isHidden(self) -> bool """
        return False

    def isLeftToRight(self): # real signature unknown; restored from __doc__
        """ isLeftToRight(self) -> bool """
        return False

    def isMaximized(self): # real signature unknown; restored from __doc__
        """ isMaximized(self) -> bool """
        return False

    def isMinimized(self): # real signature unknown; restored from __doc__
        """ isMinimized(self) -> bool """
        return False

    def isModal(self): # real signature unknown; restored from __doc__
        """ isModal(self) -> bool """
        return False

    def isRightToLeft(self): # real signature unknown; restored from __doc__
        """ isRightToLeft(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isVisible(self): # real signature unknown; restored from __doc__
        """ isVisible(self) -> bool """
        return False

    def isVisibleTo(self, QWidget): # real signature unknown; restored from __doc__
        """ isVisibleTo(self, QWidget) -> bool """
        return False

    def isWindow(self): # real signature unknown; restored from __doc__
        """ isWindow(self) -> bool """
        return False

    def isWindowModified(self): # real signature unknown; restored from __doc__
        """ isWindowModified(self) -> bool """
        return False

    def keyboardGrabber(self): # real signature unknown; restored from __doc__
        """ keyboardGrabber() -> QWidget """
        return QWidget

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, QKeyEvent) """
        pass

    def keyReleaseEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, QKeyEvent) """
        pass

    def layout(self): # real signature unknown; restored from __doc__
        """ layout(self) -> QLayout """
        return QLayout

    def layoutDirection(self): # real signature unknown; restored from __doc__
        """ layoutDirection(self) -> Qt.LayoutDirection """
        pass

    def leaveEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ leaveEvent(self, QEvent) """
        pass

    def locale(self): # real signature unknown; restored from __doc__
        """ locale(self) -> QLocale """
        pass

    def lower(self): # real signature unknown; restored from __doc__
        """ lower(self) """
        pass

    def mapFrom(self, QWidget, QPoint): # real signature unknown; restored from __doc__
        """ mapFrom(self, QWidget, QPoint) -> QPoint """
        pass

    def mapFromGlobal(self, QPoint): # real signature unknown; restored from __doc__
        """ mapFromGlobal(self, QPoint) -> QPoint """
        pass

    def mapFromParent(self, QPoint): # real signature unknown; restored from __doc__
        """ mapFromParent(self, QPoint) -> QPoint """
        pass

    def mapTo(self, QWidget, QPoint): # real signature unknown; restored from __doc__
        """ mapTo(self, QWidget, QPoint) -> QPoint """
        pass

    def mapToGlobal(self, QPoint): # real signature unknown; restored from __doc__
        """ mapToGlobal(self, QPoint) -> QPoint """
        pass

    def mapToParent(self, QPoint): # real signature unknown; restored from __doc__
        """ mapToParent(self, QPoint) -> QPoint """
        pass

    def mask(self): # real signature unknown; restored from __doc__
        """ mask(self) -> QRegion """
        pass

    def maximumHeight(self): # real signature unknown; restored from __doc__
        """ maximumHeight(self) -> int """
        return 0

    def maximumSize(self): # real signature unknown; restored from __doc__
        """ maximumSize(self) -> QSize """
        pass

    def maximumWidth(self): # real signature unknown; restored from __doc__
        """ maximumWidth(self) -> int """
        return 0

    def metric(self, QPaintDevice_PaintDeviceMetric): # real signature unknown; restored from __doc__
        """ metric(self, QPaintDevice.PaintDeviceMetric) -> int """
        return 0

    def minimumHeight(self): # real signature unknown; restored from __doc__
        """ minimumHeight(self) -> int """
        return 0

    def minimumSize(self): # real signature unknown; restored from __doc__
        """ minimumSize(self) -> QSize """
        pass

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> QSize """
        pass

    def minimumWidth(self): # real signature unknown; restored from __doc__
        """ minimumWidth(self) -> int """
        return 0

    def mouseDoubleClickEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mouseDoubleClickEvent(self, QMouseEvent) """
        pass

    def mouseGrabber(self): # real signature unknown; restored from __doc__
        """ mouseGrabber() -> QWidget """
        return QWidget

    def mouseMoveEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mouseMoveEvent(self, QMouseEvent) """
        pass

    def mousePressEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, QMouseEvent) """
        pass

    def mouseReleaseEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, QMouseEvent) """
        pass

    def move(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        move(self, QPoint)
        move(self, int, int)
        """
        pass

    def moveEvent(self, QMoveEvent): # real signature unknown; restored from __doc__
        """ moveEvent(self, QMoveEvent) """
        pass

    def nativeEvent(self, Union, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ nativeEvent(self, Union[QByteArray, bytes, bytearray], sip.voidptr) -> Tuple[bool, int] """
        pass

    def nativeParentWidget(self): # real signature unknown; restored from __doc__
        """ nativeParentWidget(self) -> QWidget """
        return QWidget

    def nextInFocusChain(self): # real signature unknown; restored from __doc__
        """ nextInFocusChain(self) -> QWidget """
        return QWidget

    def normalGeometry(self): # real signature unknown; restored from __doc__
        """ normalGeometry(self) -> QRect """
        pass

    def overrideWindowFlags(self, Union, Qt_WindowFlags=None, Qt_WindowType=None): # real signature unknown; restored from __doc__
        """ overrideWindowFlags(self, Union[Qt.WindowFlags, Qt.WindowType]) """
        pass

    def overrideWindowState(self, Union, Qt_WindowStates=None, Qt_WindowState=None): # real signature unknown; restored from __doc__
        """ overrideWindowState(self, Union[Qt.WindowStates, Qt.WindowState]) """
        pass

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ paintEngine(self) -> QPaintEngine """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ paintEvent(self, QPaintEvent) """
        pass

    def palette(self): # real signature unknown; restored from __doc__
        """ palette(self) -> QPalette """
        pass

    def parentWidget(self): # real signature unknown; restored from __doc__
        """ parentWidget(self) -> QWidget """
        return QWidget

    def pos(self): # real signature unknown; restored from __doc__
        """ pos(self) -> QPoint """
        pass

    def previousInFocusChain(self): # real signature unknown; restored from __doc__
        """ previousInFocusChain(self) -> QWidget """
        return QWidget

    def raise_(self): # real signature unknown; restored from __doc__
        """ raise_(self) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def rect(self): # real signature unknown; restored from __doc__
        """ rect(self) -> QRect """
        pass

    def releaseKeyboard(self): # real signature unknown; restored from __doc__
        """ releaseKeyboard(self) """
        pass

    def releaseMouse(self): # real signature unknown; restored from __doc__
        """ releaseMouse(self) """
        pass

    def releaseShortcut(self, p_int): # real signature unknown; restored from __doc__
        """ releaseShortcut(self, int) """
        pass

    def removeAction(self, QAction): # real signature unknown; restored from __doc__
        """ removeAction(self, QAction) """
        pass

    def render(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        render(self, QPaintDevice, targetOffset: QPoint = QPoint(), sourceRegion: QRegion = QRegion(), flags: Union[QWidget.RenderFlags, QWidget.RenderFlag] = QWidget.RenderFlags(QWidget.DrawWindowBackground|QWidget.DrawChildren))
        render(self, QPainter, targetOffset: QPoint = QPoint(), sourceRegion: QRegion = QRegion(), flags: Union[QWidget.RenderFlags, QWidget.RenderFlag] = QWidget.RenderFlags(QWidget.DrawWindowBackground|QWidget.DrawChildren))
        """
        pass

    def repaint(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        repaint(self)
        repaint(self, int, int, int, int)
        repaint(self, QRect)
        repaint(self, QRegion)
        """
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

    def restoreGeometry(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ restoreGeometry(self, Union[QByteArray, bytes, bytearray]) -> bool """
        return False

    def saveGeometry(self): # real signature unknown; restored from __doc__
        """ saveGeometry(self) -> QByteArray """
        pass

    def scroll(self, p_int, p_int_1, QRect=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        scroll(self, int, int)
        scroll(self, int, int, QRect)
        """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAcceptDrops(self, bool): # real signature unknown; restored from __doc__
        """ setAcceptDrops(self, bool) """
        pass

    def setAccessibleDescription(self, p_str): # real signature unknown; restored from __doc__
        """ setAccessibleDescription(self, str) """
        pass

    def setAccessibleName(self, p_str): # real signature unknown; restored from __doc__
        """ setAccessibleName(self, str) """
        pass

    def setAttribute(self, Qt_WidgetAttribute, on=True): # real signature unknown; restored from __doc__
        """ setAttribute(self, Qt.WidgetAttribute, on: bool = True) """
        pass

    def setAutoFillBackground(self, bool): # real signature unknown; restored from __doc__
        """ setAutoFillBackground(self, bool) """
        pass

    def setBackgroundRole(self, QPalette_ColorRole): # real signature unknown; restored from __doc__
        """ setBackgroundRole(self, QPalette.ColorRole) """
        pass

    def setBaseSize(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setBaseSize(self, int, int)
        setBaseSize(self, QSize)
        """
        pass

    def setContentsMargins(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setContentsMargins(self, int, int, int, int)
        setContentsMargins(self, QMargins)
        """
        pass

    def setContextMenuPolicy(self, Qt_ContextMenuPolicy): # real signature unknown; restored from __doc__
        """ setContextMenuPolicy(self, Qt.ContextMenuPolicy) """
        pass

    def setCursor(self, Union, QCursor=None, Qt_CursorShape=None): # real signature unknown; restored from __doc__
        """ setCursor(self, Union[QCursor, Qt.CursorShape]) """
        pass

    def setDisabled(self, bool): # real signature unknown; restored from __doc__
        """ setDisabled(self, bool) """
        pass

    def setEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setEnabled(self, bool) """
        pass

    def setFixedHeight(self, p_int): # real signature unknown; restored from __doc__
        """ setFixedHeight(self, int) """
        pass

    def setFixedSize(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setFixedSize(self, QSize)
        setFixedSize(self, int, int)
        """
        pass

    def setFixedWidth(self, p_int): # real signature unknown; restored from __doc__
        """ setFixedWidth(self, int) """
        pass

    def setFocus(self, Qt_FocusReason=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setFocus(self)
        setFocus(self, Qt.FocusReason)
        """
        pass

    def setFocusPolicy(self, Qt_FocusPolicy): # real signature unknown; restored from __doc__
        """ setFocusPolicy(self, Qt.FocusPolicy) """
        pass

    def setFocusProxy(self, QWidget): # real signature unknown; restored from __doc__
        """ setFocusProxy(self, QWidget) """
        pass

    def setFont(self, QFont): # real signature unknown; restored from __doc__
        """ setFont(self, QFont) """
        pass

    def setForegroundRole(self, QPalette_ColorRole): # real signature unknown; restored from __doc__
        """ setForegroundRole(self, QPalette.ColorRole) """
        pass

    def setGeometry(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setGeometry(self, QRect)
        setGeometry(self, int, int, int, int)
        """
        pass

    def setGraphicsEffect(self, QGraphicsEffect): # real signature unknown; restored from __doc__
        """ setGraphicsEffect(self, QGraphicsEffect) """
        pass

    def setHidden(self, bool): # real signature unknown; restored from __doc__
        """ setHidden(self, bool) """
        pass

    def setInputMethodHints(self, Union, Qt_InputMethodHints=None, Qt_InputMethodHint=None): # real signature unknown; restored from __doc__
        """ setInputMethodHints(self, Union[Qt.InputMethodHints, Qt.InputMethodHint]) """
        pass

    def setLayout(self, QLayout): # real signature unknown; restored from __doc__
        """ setLayout(self, QLayout) """
        pass

    def setLayoutDirection(self, Qt_LayoutDirection): # real signature unknown; restored from __doc__
        """ setLayoutDirection(self, Qt.LayoutDirection) """
        pass

    def setLocale(self, QLocale): # real signature unknown; restored from __doc__
        """ setLocale(self, QLocale) """
        pass

    def setMask(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setMask(self, QBitmap)
        setMask(self, QRegion)
        """
        pass

    def setMaximumHeight(self, p_int): # real signature unknown; restored from __doc__
        """ setMaximumHeight(self, int) """
        pass

    def setMaximumSize(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setMaximumSize(self, int, int)
        setMaximumSize(self, QSize)
        """
        pass

    def setMaximumWidth(self, p_int): # real signature unknown; restored from __doc__
        """ setMaximumWidth(self, int) """
        pass

    def setMinimumHeight(self, p_int): # real signature unknown; restored from __doc__
        """ setMinimumHeight(self, int) """
        pass

    def setMinimumSize(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setMinimumSize(self, int, int)
        setMinimumSize(self, QSize)
        """
        pass

    def setMinimumWidth(self, p_int): # real signature unknown; restored from __doc__
        """ setMinimumWidth(self, int) """
        pass

    def setMouseTracking(self, bool): # real signature unknown; restored from __doc__
        """ setMouseTracking(self, bool) """
        pass

    def setPalette(self, QPalette): # real signature unknown; restored from __doc__
        """ setPalette(self, QPalette) """
        pass

    def setParent(self, QWidget, Union=None, Qt_WindowFlags=None, Qt_WindowType=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setParent(self, QWidget)
        setParent(self, QWidget, Union[Qt.WindowFlags, Qt.WindowType])
        """
        pass

    def setShortcutAutoRepeat(self, p_int, enabled=True): # real signature unknown; restored from __doc__
        """ setShortcutAutoRepeat(self, int, enabled: bool = True) """
        pass

    def setShortcutEnabled(self, p_int, enabled=True): # real signature unknown; restored from __doc__
        """ setShortcutEnabled(self, int, enabled: bool = True) """
        pass

    def setSizeIncrement(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setSizeIncrement(self, int, int)
        setSizeIncrement(self, QSize)
        """
        pass

    def setSizePolicy(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setSizePolicy(self, QSizePolicy)
        setSizePolicy(self, QSizePolicy.Policy, QSizePolicy.Policy)
        """
        pass

    def setStatusTip(self, p_str): # real signature unknown; restored from __doc__
        """ setStatusTip(self, str) """
        pass

    def setStyle(self, QStyle): # real signature unknown; restored from __doc__
        """ setStyle(self, QStyle) """
        pass

    def setStyleSheet(self, p_str): # real signature unknown; restored from __doc__
        """ setStyleSheet(self, str) """
        pass

    def setTabletTracking(self, bool): # real signature unknown; restored from __doc__
        """ setTabletTracking(self, bool) """
        pass

    def setTabOrder(self, QWidget, QWidget_1): # real signature unknown; restored from __doc__
        """ setTabOrder(QWidget, QWidget) """
        pass

    def setToolTip(self, p_str): # real signature unknown; restored from __doc__
        """ setToolTip(self, str) """
        pass

    def setToolTipDuration(self, p_int): # real signature unknown; restored from __doc__
        """ setToolTipDuration(self, int) """
        pass

    def setUpdatesEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setUpdatesEnabled(self, bool) """
        pass

    def setVisible(self, bool): # real signature unknown; restored from __doc__
        """ setVisible(self, bool) """
        pass

    def setWhatsThis(self, p_str): # real signature unknown; restored from __doc__
        """ setWhatsThis(self, str) """
        pass

    def setWindowFilePath(self, p_str): # real signature unknown; restored from __doc__
        """ setWindowFilePath(self, str) """
        pass

    def setWindowFlag(self, Qt_WindowType, on=True): # real signature unknown; restored from __doc__
        """ setWindowFlag(self, Qt.WindowType, on: bool = True) """
        pass

    def setWindowFlags(self, Union, Qt_WindowFlags=None, Qt_WindowType=None): # real signature unknown; restored from __doc__
        """ setWindowFlags(self, Union[Qt.WindowFlags, Qt.WindowType]) """
        pass

    def setWindowIcon(self, QIcon): # real signature unknown; restored from __doc__
        """ setWindowIcon(self, QIcon) """
        pass

    def setWindowIconText(self, p_str): # real signature unknown; restored from __doc__
        """ setWindowIconText(self, str) """
        pass

    def setWindowModality(self, Qt_WindowModality): # real signature unknown; restored from __doc__
        """ setWindowModality(self, Qt.WindowModality) """
        pass

    def setWindowModified(self, bool): # real signature unknown; restored from __doc__
        """ setWindowModified(self, bool) """
        pass

    def setWindowOpacity(self, p_float): # real signature unknown; restored from __doc__
        """ setWindowOpacity(self, float) """
        pass

    def setWindowRole(self, p_str): # real signature unknown; restored from __doc__
        """ setWindowRole(self, str) """
        pass

    def setWindowState(self, Union, Qt_WindowStates=None, Qt_WindowState=None): # real signature unknown; restored from __doc__
        """ setWindowState(self, Union[Qt.WindowStates, Qt.WindowState]) """
        pass

    def setWindowTitle(self, p_str): # real signature unknown; restored from __doc__
        """ setWindowTitle(self, str) """
        pass

    def sharedPainter(self): # real signature unknown; restored from __doc__
        """ sharedPainter(self) -> QPainter """
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

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def sizeIncrement(self): # real signature unknown; restored from __doc__
        """ sizeIncrement(self) -> QSize """
        pass

    def sizePolicy(self): # real signature unknown; restored from __doc__
        """ sizePolicy(self) -> QSizePolicy """
        return QSizePolicy

    def stackUnder(self, QWidget): # real signature unknown; restored from __doc__
        """ stackUnder(self, QWidget) """
        pass

    def statusTip(self): # real signature unknown; restored from __doc__
        """ statusTip(self) -> str """
        return ""

    def style(self): # real signature unknown; restored from __doc__
        """ style(self) -> QStyle """
        return QStyle

    def styleSheet(self): # real signature unknown; restored from __doc__
        """ styleSheet(self) -> str """
        return ""

    def tabletEvent(self, QTabletEvent): # real signature unknown; restored from __doc__
        """ tabletEvent(self, QTabletEvent) """
        pass

    def testAttribute(self, Qt_WidgetAttribute): # real signature unknown; restored from __doc__
        """ testAttribute(self, Qt.WidgetAttribute) -> bool """
        return False

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def toolTip(self): # real signature unknown; restored from __doc__
        """ toolTip(self) -> str """
        return ""

    def toolTipDuration(self): # real signature unknown; restored from __doc__
        """ toolTipDuration(self) -> int """
        return 0

    def underMouse(self): # real signature unknown; restored from __doc__
        """ underMouse(self) -> bool """
        return False

    def ungrabGesture(self, Qt_GestureType): # real signature unknown; restored from __doc__
        """ ungrabGesture(self, Qt.GestureType) """
        pass

    def unsetCursor(self): # real signature unknown; restored from __doc__
        """ unsetCursor(self) """
        pass

    def unsetLayoutDirection(self): # real signature unknown; restored from __doc__
        """ unsetLayoutDirection(self) """
        pass

    def unsetLocale(self): # real signature unknown; restored from __doc__
        """ unsetLocale(self) """
        pass

    def update(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        update(self)
        update(self, QRect)
        update(self, QRegion)
        update(self, int, int, int, int)
        """
        pass

    def updateGeometry(self): # real signature unknown; restored from __doc__
        """ updateGeometry(self) """
        pass

    def updateMicroFocus(self): # real signature unknown; restored from __doc__
        """ updateMicroFocus(self) """
        pass

    def updatesEnabled(self): # real signature unknown; restored from __doc__
        """ updatesEnabled(self) -> bool """
        return False

    def visibleRegion(self): # real signature unknown; restored from __doc__
        """ visibleRegion(self) -> QRegion """
        pass

    def whatsThis(self): # real signature unknown; restored from __doc__
        """ whatsThis(self) -> str """
        return ""

    def wheelEvent(self, QWheelEvent): # real signature unknown; restored from __doc__
        """ wheelEvent(self, QWheelEvent) """
        pass

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> int """
        return 0

    def window(self): # real signature unknown; restored from __doc__
        """ window(self) -> QWidget """
        return QWidget

    def windowFilePath(self): # real signature unknown; restored from __doc__
        """ windowFilePath(self) -> str """
        return ""

    def windowFlags(self): # real signature unknown; restored from __doc__
        """ windowFlags(self) -> Qt.WindowFlags """
        pass

    def windowHandle(self): # real signature unknown; restored from __doc__
        """ windowHandle(self) -> QWindow """
        pass

    def windowIcon(self): # real signature unknown; restored from __doc__
        """ windowIcon(self) -> QIcon """
        pass

    def windowIconChanged(self, QIcon): # real signature unknown; restored from __doc__
        """ windowIconChanged(self, QIcon) [signal] """
        pass

    def windowIconText(self): # real signature unknown; restored from __doc__
        """ windowIconText(self) -> str """
        return ""

    def windowIconTextChanged(self, p_str): # real signature unknown; restored from __doc__
        """ windowIconTextChanged(self, str) [signal] """
        pass

    def windowModality(self): # real signature unknown; restored from __doc__
        """ windowModality(self) -> Qt.WindowModality """
        pass

    def windowOpacity(self): # real signature unknown; restored from __doc__
        """ windowOpacity(self) -> float """
        return 0.0

    def windowRole(self): # real signature unknown; restored from __doc__
        """ windowRole(self) -> str """
        return ""

    def windowState(self): # real signature unknown; restored from __doc__
        """ windowState(self) -> Qt.WindowStates """
        pass

    def windowTitle(self): # real signature unknown; restored from __doc__
        """ windowTitle(self) -> str """
        return ""

    def windowTitleChanged(self, p_str): # real signature unknown; restored from __doc__
        """ windowTitleChanged(self, str) [signal] """
        pass

    def windowType(self): # real signature unknown; restored from __doc__
        """ windowType(self) -> Qt.WindowType """
        pass

    def winId(self): # real signature unknown; restored from __doc__
        """ winId(self) -> sip.voidptr """
        pass

    def x(self): # real signature unknown; restored from __doc__
        """ x(self) -> int """
        return 0

    def y(self): # real signature unknown; restored from __doc__
        """ y(self) -> int """
        return 0

    def __init__(self, parent=None, flags, Qt_WindowFlags=None, Qt_WindowType=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    DrawChildren = 2
    DrawWindowBackground = 1
    IgnoreMask = 4


