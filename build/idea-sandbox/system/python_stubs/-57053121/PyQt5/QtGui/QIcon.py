# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QIcon(__sip.wrapper):
    """
    QIcon()
    QIcon(QPixmap)
    QIcon(QIcon)
    QIcon(str)
    QIcon(QIconEngine)
    QIcon(Any)
    """
    def actualSize(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        actualSize(self, QSize, mode: QIcon.Mode = QIcon.Normal, state: QIcon.State = QIcon.Off) -> QSize
        actualSize(self, QWindow, QSize, mode: QIcon.Mode = QIcon.Normal, state: QIcon.State = QIcon.Off) -> QSize
        """
        pass

    def addFile(self, p_str, size=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ addFile(self, str, size: QSize = QSize(), mode: QIcon.Mode = QIcon.Normal, state: QIcon.State = QIcon.Off) """
        pass

    def addPixmap(self, QPixmap, mode=None, state=None): # real signature unknown; restored from __doc__
        """ addPixmap(self, QPixmap, mode: QIcon.Mode = QIcon.Normal, state: QIcon.State = QIcon.Off) """
        pass

    def availableSizes(self, mode=None, state=None): # real signature unknown; restored from __doc__
        """ availableSizes(self, mode: QIcon.Mode = QIcon.Normal, state: QIcon.State = QIcon.Off) -> List[QSize] """
        return []

    def cacheKey(self): # real signature unknown; restored from __doc__
        """ cacheKey(self) -> int """
        return 0

    def fallbackSearchPaths(self): # real signature unknown; restored from __doc__
        """ fallbackSearchPaths() -> List[str] """
        return []

    def fallbackThemeName(self): # real signature unknown; restored from __doc__
        """ fallbackThemeName() -> str """
        return ""

    def fromTheme(self, p_str, QIcon=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        fromTheme(str) -> QIcon
        fromTheme(str, QIcon) -> QIcon
        """
        return QIcon

    def hasThemeIcon(self, p_str): # real signature unknown; restored from __doc__
        """ hasThemeIcon(str) -> bool """
        return False

    def isDetached(self): # real signature unknown; restored from __doc__
        """ isDetached(self) -> bool """
        return False

    def isMask(self): # real signature unknown; restored from __doc__
        """ isMask(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def paint(self, QPainter, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        paint(self, QPainter, QRect, alignment: Union[Qt.Alignment, Qt.AlignmentFlag] = Qt.AlignCenter, mode: QIcon.Mode = QIcon.Normal, state: QIcon.State = QIcon.Off)
        paint(self, QPainter, int, int, int, int, alignment: Union[Qt.Alignment, Qt.AlignmentFlag] = Qt.AlignCenter, mode: QIcon.Mode = QIcon.Normal, state: QIcon.State = QIcon.Off)
        """
        pass

    def pixmap(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        pixmap(self, QSize, mode: QIcon.Mode = QIcon.Normal, state: QIcon.State = QIcon.Off) -> QPixmap
        pixmap(self, int, int, mode: QIcon.Mode = QIcon.Normal, state: QIcon.State = QIcon.Off) -> QPixmap
        pixmap(self, int, mode: QIcon.Mode = QIcon.Normal, state: QIcon.State = QIcon.Off) -> QPixmap
        pixmap(self, QWindow, QSize, mode: QIcon.Mode = QIcon.Normal, state: QIcon.State = QIcon.Off) -> QPixmap
        """
        return QPixmap

    def setFallbackSearchPaths(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ setFallbackSearchPaths(Iterable[str]) """
        pass

    def setFallbackThemeName(self, p_str): # real signature unknown; restored from __doc__
        """ setFallbackThemeName(str) """
        pass

    def setIsMask(self, bool): # real signature unknown; restored from __doc__
        """ setIsMask(self, bool) """
        pass

    def setThemeName(self, p_str): # real signature unknown; restored from __doc__
        """ setThemeName(str) """
        pass

    def setThemeSearchPaths(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ setThemeSearchPaths(Iterable[str]) """
        pass

    def swap(self, QIcon): # real signature unknown; restored from __doc__
        """ swap(self, QIcon) """
        pass

    def themeName(self): # real signature unknown; restored from __doc__
        """ themeName() -> str """
        return ""

    def themeSearchPaths(self): # real signature unknown; restored from __doc__
        """ themeSearchPaths() -> List[str] """
        return []

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Active = 2
    Disabled = 1
    Normal = 0
    Off = 1
    On = 0
    Selected = 3


