# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QAction(__PyQt5_QtCore.QObject):
    """
    QAction(parent: QObject = None)
    QAction(str, parent: QObject = None)
    QAction(QIcon, str, parent: QObject = None)
    """
    def actionGroup(self): # real signature unknown; restored from __doc__
        """ actionGroup(self) -> QActionGroup """
        return QActionGroup

    def activate(self, QAction_ActionEvent): # real signature unknown; restored from __doc__
        """ activate(self, QAction.ActionEvent) """
        pass

    def associatedGraphicsWidgets(self): # real signature unknown; restored from __doc__
        """ associatedGraphicsWidgets(self) -> List[QGraphicsWidget] """
        return []

    def associatedWidgets(self): # real signature unknown; restored from __doc__
        """ associatedWidgets(self) -> List[QWidget] """
        return []

    def autoRepeat(self): # real signature unknown; restored from __doc__
        """ autoRepeat(self) -> bool """
        return False

    def changed(self): # real signature unknown; restored from __doc__
        """ changed(self) [signal] """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def data(self): # real signature unknown; restored from __doc__
        """ data(self) -> Any """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def font(self): # real signature unknown; restored from __doc__
        """ font(self) -> QFont """
        pass

    def hover(self): # real signature unknown; restored from __doc__
        """ hover(self) """
        pass

    def hovered(self): # real signature unknown; restored from __doc__
        """ hovered(self) [signal] """
        pass

    def icon(self): # real signature unknown; restored from __doc__
        """ icon(self) -> QIcon """
        pass

    def iconText(self): # real signature unknown; restored from __doc__
        """ iconText(self) -> str """
        return ""

    def isCheckable(self): # real signature unknown; restored from __doc__
        """ isCheckable(self) -> bool """
        return False

    def isChecked(self): # real signature unknown; restored from __doc__
        """ isChecked(self) -> bool """
        return False

    def isEnabled(self): # real signature unknown; restored from __doc__
        """ isEnabled(self) -> bool """
        return False

    def isIconVisibleInMenu(self): # real signature unknown; restored from __doc__
        """ isIconVisibleInMenu(self) -> bool """
        return False

    def isSeparator(self): # real signature unknown; restored from __doc__
        """ isSeparator(self) -> bool """
        return False

    def isShortcutVisibleInContextMenu(self): # real signature unknown; restored from __doc__
        """ isShortcutVisibleInContextMenu(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isVisible(self): # real signature unknown; restored from __doc__
        """ isVisible(self) -> bool """
        return False

    def menu(self): # real signature unknown; restored from __doc__
        """ menu(self) -> QMenu """
        return QMenu

    def menuRole(self): # real signature unknown; restored from __doc__
        """ menuRole(self) -> QAction.MenuRole """
        pass

    def parentWidget(self): # real signature unknown; restored from __doc__
        """ parentWidget(self) -> QWidget """
        return QWidget

    def priority(self): # real signature unknown; restored from __doc__
        """ priority(self) -> QAction.Priority """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setActionGroup(self, QActionGroup): # real signature unknown; restored from __doc__
        """ setActionGroup(self, QActionGroup) """
        pass

    def setAutoRepeat(self, bool): # real signature unknown; restored from __doc__
        """ setAutoRepeat(self, bool) """
        pass

    def setCheckable(self, bool): # real signature unknown; restored from __doc__
        """ setCheckable(self, bool) """
        pass

    def setChecked(self, bool): # real signature unknown; restored from __doc__
        """ setChecked(self, bool) """
        pass

    def setData(self, Any): # real signature unknown; restored from __doc__
        """ setData(self, Any) """
        pass

    def setDisabled(self, bool): # real signature unknown; restored from __doc__
        """ setDisabled(self, bool) """
        pass

    def setEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setEnabled(self, bool) """
        pass

    def setFont(self, QFont): # real signature unknown; restored from __doc__
        """ setFont(self, QFont) """
        pass

    def setIcon(self, QIcon): # real signature unknown; restored from __doc__
        """ setIcon(self, QIcon) """
        pass

    def setIconText(self, p_str): # real signature unknown; restored from __doc__
        """ setIconText(self, str) """
        pass

    def setIconVisibleInMenu(self, bool): # real signature unknown; restored from __doc__
        """ setIconVisibleInMenu(self, bool) """
        pass

    def setMenu(self, QMenu): # real signature unknown; restored from __doc__
        """ setMenu(self, QMenu) """
        pass

    def setMenuRole(self, QAction_MenuRole): # real signature unknown; restored from __doc__
        """ setMenuRole(self, QAction.MenuRole) """
        pass

    def setPriority(self, QAction_Priority): # real signature unknown; restored from __doc__
        """ setPriority(self, QAction.Priority) """
        pass

    def setSeparator(self, bool): # real signature unknown; restored from __doc__
        """ setSeparator(self, bool) """
        pass

    def setShortcut(self, Union, QKeySequence=None, QKeySequence_StandardKey=None, p_str=None, p_int=None): # real signature unknown; restored from __doc__
        """ setShortcut(self, Union[QKeySequence, QKeySequence.StandardKey, str, int]) """
        pass

    def setShortcutContext(self, Qt_ShortcutContext): # real signature unknown; restored from __doc__
        """ setShortcutContext(self, Qt.ShortcutContext) """
        pass

    def setShortcuts(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setShortcuts(self, Iterable[Union[QKeySequence, QKeySequence.StandardKey, str, int]])
        setShortcuts(self, QKeySequence.StandardKey)
        """
        pass

    def setShortcutVisibleInContextMenu(self, bool): # real signature unknown; restored from __doc__
        """ setShortcutVisibleInContextMenu(self, bool) """
        pass

    def setStatusTip(self, p_str): # real signature unknown; restored from __doc__
        """ setStatusTip(self, str) """
        pass

    def setText(self, p_str): # real signature unknown; restored from __doc__
        """ setText(self, str) """
        pass

    def setToolTip(self, p_str): # real signature unknown; restored from __doc__
        """ setToolTip(self, str) """
        pass

    def setVisible(self, bool): # real signature unknown; restored from __doc__
        """ setVisible(self, bool) """
        pass

    def setWhatsThis(self, p_str): # real signature unknown; restored from __doc__
        """ setWhatsThis(self, str) """
        pass

    def shortcut(self): # real signature unknown; restored from __doc__
        """ shortcut(self) -> QKeySequence """
        pass

    def shortcutContext(self): # real signature unknown; restored from __doc__
        """ shortcutContext(self) -> Qt.ShortcutContext """
        pass

    def shortcuts(self): # real signature unknown; restored from __doc__
        """ shortcuts(self) -> List[QKeySequence] """
        return []

    def showStatusText(self, widget=None): # real signature unknown; restored from __doc__
        """ showStatusText(self, widget: QWidget = None) -> bool """
        return False

    def statusTip(self): # real signature unknown; restored from __doc__
        """ statusTip(self) -> str """
        return ""

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def toggle(self): # real signature unknown; restored from __doc__
        """ toggle(self) """
        pass

    def toggled(self, bool): # real signature unknown; restored from __doc__
        """ toggled(self, bool) [signal] """
        pass

    def toolTip(self): # real signature unknown; restored from __doc__
        """ toolTip(self) -> str """
        return ""

    def trigger(self): # real signature unknown; restored from __doc__
        """ trigger(self) """
        pass

    def triggered(self, checked=False): # real signature unknown; restored from __doc__
        """ triggered(self, checked: bool = False) [signal] """
        pass

    def whatsThis(self): # real signature unknown; restored from __doc__
        """ whatsThis(self) -> str """
        return ""

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AboutQtRole = 3
    AboutRole = 4
    ApplicationSpecificRole = 2
    HighPriority = 256
    Hover = 1
    LowPriority = 0
    NormalPriority = 128
    NoRole = 0
    PreferencesRole = 5
    QuitRole = 6
    TextHeuristicRole = 1
    Trigger = 0


