# encoding: utf-8
# module PyQt5.QtWinExtras
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWinExtras.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


# no functions
# classes

class QtWin(__sip.simplewrapper):
    # no doc
    def colorizationColor(self): # real signature unknown; restored from __doc__
        """ colorizationColor() -> Tuple[QColor, bool] """
        pass

    def createMask(self, QBitmap): # real signature unknown; restored from __doc__
        """ createMask(QBitmap) -> sip.voidptr """
        pass

    def disableBlurBehindWindow(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        disableBlurBehindWindow(QWindow)
        disableBlurBehindWindow(QWidget)
        """
        pass

    def enableBlurBehindWindow(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        enableBlurBehindWindow(QWindow, QRegion)
        enableBlurBehindWindow(QWindow)
        enableBlurBehindWindow(QWidget, QRegion)
        enableBlurBehindWindow(QWidget)
        """
        pass

    def errorStringFromHresult(self, p_int): # real signature unknown; restored from __doc__
        """ errorStringFromHresult(int) -> str """
        return ""

    def extendFrameIntoClientArea(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        extendFrameIntoClientArea(QWindow, int, int, int, int)
        extendFrameIntoClientArea(QWindow, QMargins)
        extendFrameIntoClientArea(QWidget, QMargins)
        extendFrameIntoClientArea(QWidget, int, int, int, int)
        """
        pass

    def fromHBITMAP(self, sip_voidptr, format=None): # real signature unknown; restored from __doc__
        """ fromHBITMAP(sip.voidptr, format: QtWin.HBitmapFormat = QtWin.HBitmapNoAlpha) -> QPixmap """
        pass

    def fromHICON(self, sip_voidptr): # real signature unknown; restored from __doc__
        """ fromHICON(sip.voidptr) -> QPixmap """
        pass

    def fromHRGN(self, sip_voidptr): # real signature unknown; restored from __doc__
        """ fromHRGN(sip.voidptr) -> QRegion """
        pass

    def imageFromHBITMAP(self, sip_voidptr, sip_voidptr_1, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ imageFromHBITMAP(sip.voidptr, sip.voidptr, int, int) -> QImage """
        pass

    def isCompositionEnabled(self): # real signature unknown; restored from __doc__
        """ isCompositionEnabled() -> bool """
        return False

    def isCompositionOpaque(self): # real signature unknown; restored from __doc__
        """ isCompositionOpaque() -> bool """
        return False

    def isWindowExcludedFromPeek(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        isWindowExcludedFromPeek(QWindow) -> bool
        isWindowExcludedFromPeek(QWidget) -> bool
        """
        return False

    def isWindowPeekDisallowed(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        isWindowPeekDisallowed(QWindow) -> bool
        isWindowPeekDisallowed(QWidget) -> bool
        """
        return False

    def markFullscreenWindow(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        markFullscreenWindow(QWindow, fullscreen: bool = True)
        markFullscreenWindow(QWidget, fullscreen: bool = True)
        """
        pass

    def realColorizationColor(self): # real signature unknown; restored from __doc__
        """ realColorizationColor() -> QColor """
        pass

    def resetExtendedFrame(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        resetExtendedFrame(QWindow)
        resetExtendedFrame(QWidget)
        """
        pass

    def setCompositionEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setCompositionEnabled(bool) """
        pass

    def setCurrentProcessExplicitAppUserModelID(self, p_str): # real signature unknown; restored from __doc__
        """ setCurrentProcessExplicitAppUserModelID(str) """
        pass

    def setWindowDisallowPeek(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setWindowDisallowPeek(QWindow, bool)
        setWindowDisallowPeek(QWidget, bool)
        """
        pass

    def setWindowExcludedFromPeek(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setWindowExcludedFromPeek(QWindow, bool)
        setWindowExcludedFromPeek(QWidget, bool)
        """
        pass

    def setWindowFlip3DPolicy(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setWindowFlip3DPolicy(QWindow, QtWin.WindowFlip3DPolicy)
        setWindowFlip3DPolicy(QWidget, QtWin.WindowFlip3DPolicy)
        """
        pass

    def stringFromHresult(self, p_int): # real signature unknown; restored from __doc__
        """ stringFromHresult(int) -> str """
        return ""

    def taskbarActivateTab(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        taskbarActivateTab(QWindow)
        taskbarActivateTab(QWidget)
        """
        pass

    def taskbarActivateTabAlt(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        taskbarActivateTabAlt(QWindow)
        taskbarActivateTabAlt(QWidget)
        """
        pass

    def taskbarAddTab(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        taskbarAddTab(QWindow)
        taskbarAddTab(QWidget)
        """
        pass

    def taskbarDeleteTab(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        taskbarDeleteTab(QWindow)
        taskbarDeleteTab(QWidget)
        """
        pass

    def toHBITMAP(self, QPixmap, format=None): # real signature unknown; restored from __doc__
        """ toHBITMAP(QPixmap, format: QtWin.HBitmapFormat = QtWin.HBitmapNoAlpha) -> sip.voidptr """
        pass

    def toHICON(self, QPixmap): # real signature unknown; restored from __doc__
        """ toHICON(QPixmap) -> sip.voidptr """
        pass

    def toHRGN(self, QRegion): # real signature unknown; restored from __doc__
        """ toHRGN(QRegion) -> sip.voidptr """
        pass

    def windowFlip3DPolicy(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        windowFlip3DPolicy(QWindow) -> QtWin.WindowFlip3DPolicy
        windowFlip3DPolicy(QWidget) -> QtWin.WindowFlip3DPolicy
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    FlipDefault = 0
    FlipExcludeAbove = 2
    FlipExcludeBelow = 1
    HBitmapAlpha = 2
    HBitmapNoAlpha = 0
    HBitmapPremultipliedAlpha = 1


class QWinJumpList(__PyQt5_QtCore.QObject):
    """ QWinJumpList(parent: QObject = None) """
    def addCategory(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addCategory(self, QWinJumpListCategory)
        addCategory(self, str, items: Iterable[QWinJumpListItem] = []) -> QWinJumpListCategory
        """
        pass

    def categories(self): # real signature unknown; restored from __doc__
        """ categories(self) -> List[QWinJumpListCategory] """
        return []

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def frequent(self): # real signature unknown; restored from __doc__
        """ frequent(self) -> QWinJumpListCategory """
        return QWinJumpListCategory

    def identifier(self): # real signature unknown; restored from __doc__
        """ identifier(self) -> str """
        return ""

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def recent(self): # real signature unknown; restored from __doc__
        """ recent(self) -> QWinJumpListCategory """
        return QWinJumpListCategory

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setIdentifier(self, p_str): # real signature unknown; restored from __doc__
        """ setIdentifier(self, str) """
        pass

    def tasks(self): # real signature unknown; restored from __doc__
        """ tasks(self) -> QWinJumpListCategory """
        return QWinJumpListCategory

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


class QWinJumpListCategory(__sip.wrapper):
    """ QWinJumpListCategory(title: str = '') """
    def addDestination(self, p_str): # real signature unknown; restored from __doc__
        """ addDestination(self, str) -> QWinJumpListItem """
        return QWinJumpListItem

    def addItem(self, QWinJumpListItem): # real signature unknown; restored from __doc__
        """ addItem(self, QWinJumpListItem) """
        pass

    def addLink(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addLink(self, str, str, arguments: Iterable[str] = []) -> QWinJumpListItem
        addLink(self, QIcon, str, str, arguments: Iterable[str] = []) -> QWinJumpListItem
        """
        pass

    def addSeparator(self): # real signature unknown; restored from __doc__
        """ addSeparator(self) -> QWinJumpListItem """
        return QWinJumpListItem

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isVisible(self): # real signature unknown; restored from __doc__
        """ isVisible(self) -> bool """
        return False

    def items(self): # real signature unknown; restored from __doc__
        """ items(self) -> List[QWinJumpListItem] """
        return []

    def setTitle(self, p_str): # real signature unknown; restored from __doc__
        """ setTitle(self, str) """
        pass

    def setVisible(self, bool): # real signature unknown; restored from __doc__
        """ setVisible(self, bool) """
        pass

    def title(self): # real signature unknown; restored from __doc__
        """ title(self) -> str """
        return ""

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QWinJumpListCategory.Type """
        pass

    def __init__(self, title=''): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Custom = 0
    Frequent = 2
    Recent = 1
    Tasks = 3


class QWinJumpListItem(__sip.wrapper):
    """ QWinJumpListItem(QWinJumpListItem.Type) """
    def arguments(self): # real signature unknown; restored from __doc__
        """ arguments(self) -> List[str] """
        return []

    def description(self): # real signature unknown; restored from __doc__
        """ description(self) -> str """
        return ""

    def filePath(self): # real signature unknown; restored from __doc__
        """ filePath(self) -> str """
        return ""

    def icon(self): # real signature unknown; restored from __doc__
        """ icon(self) -> QIcon """
        pass

    def setArguments(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ setArguments(self, Iterable[str]) """
        pass

    def setDescription(self, p_str): # real signature unknown; restored from __doc__
        """ setDescription(self, str) """
        pass

    def setFilePath(self, p_str): # real signature unknown; restored from __doc__
        """ setFilePath(self, str) """
        pass

    def setIcon(self, QIcon): # real signature unknown; restored from __doc__
        """ setIcon(self, QIcon) """
        pass

    def setTitle(self, p_str): # real signature unknown; restored from __doc__
        """ setTitle(self, str) """
        pass

    def setType(self, QWinJumpListItem_Type): # real signature unknown; restored from __doc__
        """ setType(self, QWinJumpListItem.Type) """
        pass

    def setWorkingDirectory(self, p_str): # real signature unknown; restored from __doc__
        """ setWorkingDirectory(self, str) """
        pass

    def title(self): # real signature unknown; restored from __doc__
        """ title(self) -> str """
        return ""

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QWinJumpListItem.Type """
        pass

    def workingDirectory(self): # real signature unknown; restored from __doc__
        """ workingDirectory(self) -> str """
        return ""

    def __init__(self, QWinJumpListItem_Type): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Destination = 0
    Link = 1
    Separator = 2


class QWinTaskbarButton(__PyQt5_QtCore.QObject):
    """ QWinTaskbarButton(parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clearOverlayIcon(self): # real signature unknown; restored from __doc__
        """ clearOverlayIcon(self) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def eventFilter(self, QObject, QEvent): # real signature unknown; restored from __doc__
        """ eventFilter(self, QObject, QEvent) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def overlayAccessibleDescription(self): # real signature unknown; restored from __doc__
        """ overlayAccessibleDescription(self) -> str """
        return ""

    def overlayIcon(self): # real signature unknown; restored from __doc__
        """ overlayIcon(self) -> QIcon """
        pass

    def progress(self): # real signature unknown; restored from __doc__
        """ progress(self) -> QWinTaskbarProgress """
        return QWinTaskbarProgress

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setOverlayAccessibleDescription(self, p_str): # real signature unknown; restored from __doc__
        """ setOverlayAccessibleDescription(self, str) """
        pass

    def setOverlayIcon(self, QIcon): # real signature unknown; restored from __doc__
        """ setOverlayIcon(self, QIcon) """
        pass

    def setWindow(self, QWindow): # real signature unknown; restored from __doc__
        """ setWindow(self, QWindow) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def window(self): # real signature unknown; restored from __doc__
        """ window(self) -> QWindow """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


class QWinTaskbarProgress(__PyQt5_QtCore.QObject):
    """ QWinTaskbarProgress(parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def hide(self): # real signature unknown; restored from __doc__
        """ hide(self) """
        pass

    def isPaused(self): # real signature unknown; restored from __doc__
        """ isPaused(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isStopped(self): # real signature unknown; restored from __doc__
        """ isStopped(self) -> bool """
        return False

    def isVisible(self): # real signature unknown; restored from __doc__
        """ isVisible(self) -> bool """
        return False

    def maximum(self): # real signature unknown; restored from __doc__
        """ maximum(self) -> int """
        return 0

    def maximumChanged(self, p_int): # real signature unknown; restored from __doc__
        """ maximumChanged(self, int) [signal] """
        pass

    def minimum(self): # real signature unknown; restored from __doc__
        """ minimum(self) -> int """
        return 0

    def minimumChanged(self, p_int): # real signature unknown; restored from __doc__
        """ minimumChanged(self, int) [signal] """
        pass

    def pause(self): # real signature unknown; restored from __doc__
        """ pause(self) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) """
        pass

    def resume(self): # real signature unknown; restored from __doc__
        """ resume(self) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setMaximum(self, p_int): # real signature unknown; restored from __doc__
        """ setMaximum(self, int) """
        pass

    def setMinimum(self, p_int): # real signature unknown; restored from __doc__
        """ setMinimum(self, int) """
        pass

    def setPaused(self, bool): # real signature unknown; restored from __doc__
        """ setPaused(self, bool) """
        pass

    def setRange(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ setRange(self, int, int) """
        pass

    def setValue(self, p_int): # real signature unknown; restored from __doc__
        """ setValue(self, int) """
        pass

    def setVisible(self, bool): # real signature unknown; restored from __doc__
        """ setVisible(self, bool) """
        pass

    def show(self): # real signature unknown; restored from __doc__
        """ show(self) """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def value(self): # real signature unknown; restored from __doc__
        """ value(self) -> int """
        return 0

    def valueChanged(self, p_int): # real signature unknown; restored from __doc__
        """ valueChanged(self, int) [signal] """
        pass

    def visibilityChanged(self, bool): # real signature unknown; restored from __doc__
        """ visibilityChanged(self, bool) [signal] """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


class QWinThumbnailToolBar(__PyQt5_QtCore.QObject):
    """ QWinThumbnailToolBar(parent: QObject = None) """
    def addButton(self, QWinThumbnailToolButton): # real signature unknown; restored from __doc__
        """ addButton(self, QWinThumbnailToolButton) """
        pass

    def buttons(self): # real signature unknown; restored from __doc__
        """ buttons(self) -> List[QWinThumbnailToolButton] """
        return []

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def iconicLivePreviewPixmap(self): # real signature unknown; restored from __doc__
        """ iconicLivePreviewPixmap(self) -> QPixmap """
        pass

    def iconicLivePreviewPixmapRequested(self): # real signature unknown; restored from __doc__
        """ iconicLivePreviewPixmapRequested(self) [signal] """
        pass

    def iconicPixmapNotificationsEnabled(self): # real signature unknown; restored from __doc__
        """ iconicPixmapNotificationsEnabled(self) -> bool """
        return False

    def iconicThumbnailPixmap(self): # real signature unknown; restored from __doc__
        """ iconicThumbnailPixmap(self) -> QPixmap """
        pass

    def iconicThumbnailPixmapRequested(self): # real signature unknown; restored from __doc__
        """ iconicThumbnailPixmapRequested(self) [signal] """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeButton(self, QWinThumbnailToolButton): # real signature unknown; restored from __doc__
        """ removeButton(self, QWinThumbnailToolButton) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setButtons(self, Iterable, QWinThumbnailToolButton=None): # real signature unknown; restored from __doc__
        """ setButtons(self, Iterable[QWinThumbnailToolButton]) """
        pass

    def setIconicLivePreviewPixmap(self, QPixmap): # real signature unknown; restored from __doc__
        """ setIconicLivePreviewPixmap(self, QPixmap) """
        pass

    def setIconicPixmapNotificationsEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setIconicPixmapNotificationsEnabled(self, bool) """
        pass

    def setIconicThumbnailPixmap(self, QPixmap): # real signature unknown; restored from __doc__
        """ setIconicThumbnailPixmap(self, QPixmap) """
        pass

    def setWindow(self, QWindow): # real signature unknown; restored from __doc__
        """ setWindow(self, QWindow) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def window(self): # real signature unknown; restored from __doc__
        """ window(self) -> QWindow """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


class QWinThumbnailToolButton(__PyQt5_QtCore.QObject):
    """ QWinThumbnailToolButton(parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def click(self): # real signature unknown; restored from __doc__
        """ click(self) """
        pass

    def clicked(self): # real signature unknown; restored from __doc__
        """ clicked(self) [signal] """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dismissOnClick(self): # real signature unknown; restored from __doc__
        """ dismissOnClick(self) -> bool """
        return False

    def icon(self): # real signature unknown; restored from __doc__
        """ icon(self) -> QIcon """
        pass

    def isEnabled(self): # real signature unknown; restored from __doc__
        """ isEnabled(self) -> bool """
        return False

    def isFlat(self): # real signature unknown; restored from __doc__
        """ isFlat(self) -> bool """
        return False

    def isInteractive(self): # real signature unknown; restored from __doc__
        """ isInteractive(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isVisible(self): # real signature unknown; restored from __doc__
        """ isVisible(self) -> bool """
        return False

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setDismissOnClick(self, bool): # real signature unknown; restored from __doc__
        """ setDismissOnClick(self, bool) """
        pass

    def setEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setEnabled(self, bool) """
        pass

    def setFlat(self, bool): # real signature unknown; restored from __doc__
        """ setFlat(self, bool) """
        pass

    def setIcon(self, QIcon): # real signature unknown; restored from __doc__
        """ setIcon(self, QIcon) """
        pass

    def setInteractive(self, bool): # real signature unknown; restored from __doc__
        """ setInteractive(self, bool) """
        pass

    def setToolTip(self, p_str): # real signature unknown; restored from __doc__
        """ setToolTip(self, str) """
        pass

    def setVisible(self, bool): # real signature unknown; restored from __doc__
        """ setVisible(self, bool) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def toolTip(self): # real signature unknown; restored from __doc__
        """ toolTip(self) -> str """
        return ""

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


# variables with complex values



