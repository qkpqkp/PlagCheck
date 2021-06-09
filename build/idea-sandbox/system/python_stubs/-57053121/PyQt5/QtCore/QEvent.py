# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QEvent(__sip.wrapper):
    """
    QEvent(QEvent.Type)
    QEvent(QEvent)
    """
    def accept(self): # real signature unknown; restored from __doc__
        """ accept(self) """
        pass

    def ignore(self): # real signature unknown; restored from __doc__
        """ ignore(self) """
        pass

    def isAccepted(self): # real signature unknown; restored from __doc__
        """ isAccepted(self) -> bool """
        return False

    def registerEventType(self, hint=-1): # real signature unknown; restored from __doc__
        """ registerEventType(hint: int = -1) -> int """
        return 0

    def setAccepted(self, bool): # real signature unknown; restored from __doc__
        """ setAccepted(self, bool) """
        pass

    def spontaneous(self): # real signature unknown; restored from __doc__
        """ spontaneous(self) -> bool """
        return False

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QEvent.Type """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    ActionAdded = 114
    ActionChanged = 113
    ActionRemoved = 115
    ActivationChange = 99
    ApplicationActivate = 121
    ApplicationActivated = 121
    ApplicationDeactivate = 122
    ApplicationDeactivated = 122
    ApplicationFontChange = 36
    ApplicationLayoutDirectionChange = 37
    ApplicationPaletteChange = 38
    ApplicationStateChange = 214
    ApplicationWindowIconChange = 35
    ChildAdded = 68
    ChildPolished = 69
    ChildRemoved = 71
    Clipboard = 40
    Close = 19
    CloseSoftwareInputPanel = 200
    ContentsRectChange = 178
    ContextMenu = 82
    CursorChange = 183
    DeferredDelete = 52
    DragEnter = 60
    DragLeave = 62
    DragMove = 61
    Drop = 63
    DynamicPropertyChange = 170
    EnabledChange = 98
    Enter = 10
    EnterWhatsThisMode = 124
    Expose = 206
    FileOpen = 116
    FocusAboutToChange = 23
    FocusIn = 8
    FocusOut = 9
    FontChange = 97
    Gesture = 198
    GestureOverride = 202
    GrabKeyboard = 188
    GrabMouse = 186
    GraphicsSceneContextMenu = 159
    GraphicsSceneDragEnter = 164
    GraphicsSceneDragLeave = 166
    GraphicsSceneDragMove = 165
    GraphicsSceneDrop = 167
    GraphicsSceneHelp = 163
    GraphicsSceneHoverEnter = 160
    GraphicsSceneHoverLeave = 162
    GraphicsSceneHoverMove = 161
    GraphicsSceneMouseDoubleClick = 158
    GraphicsSceneMouseMove = 155
    GraphicsSceneMousePress = 156
    GraphicsSceneMouseRelease = 157
    GraphicsSceneMove = 182
    GraphicsSceneResize = 181
    GraphicsSceneWheel = 168
    Hide = 18
    HideToParent = 27
    HoverEnter = 127
    HoverLeave = 128
    HoverMove = 129
    IconDrag = 96
    IconTextChange = 101
    InputMethod = 83
    InputMethodQuery = 207
    KeyboardLayoutChange = 169
    KeyPress = 6
    KeyRelease = 7
    LanguageChange = 89
    LayoutDirectionChange = 90
    LayoutRequest = 76
    Leave = 11
    LeaveWhatsThisMode = 125
    LocaleChange = 88
    MacSizeChange = 177
    MaxUser = 65535
    MetaCall = 43
    ModifiedChange = 102
    MouseButtonDblClick = 4
    MouseButtonPress = 2
    MouseButtonRelease = 3
    MouseMove = 5
    MouseTrackingChange = 109
    Move = 13
    NonClientAreaMouseButtonDblClick = 176
    NonClientAreaMouseButtonPress = 174
    NonClientAreaMouseButtonRelease = 175
    NonClientAreaMouseMove = 173
    None_ = 0
    OkRequest = 94
    OrientationChange = 208
    Paint = 12
    PaletteChange = 39
    ParentAboutToChange = 131
    ParentChange = 21
    PlatformPanel = 212
    PlatformSurface = 217
    Polish = 75
    PolishRequest = 74
    QueryWhatsThis = 123
    ReadOnlyChange = 106
    RequestSoftwareInputPanel = 199
    Resize = 14
    Scroll = 205
    ScrollPrepare = 204
    Shortcut = 117
    ShortcutOverride = 51
    Show = 17
    ShowToParent = 26
    SockAct = 50
    StateMachineSignal = 192
    StateMachineWrapped = 193
    StatusTip = 112
    StyleChange = 100
    TabletEnterProximity = 171
    TabletLeaveProximity = 172
    TabletMove = 87
    TabletPress = 92
    TabletRelease = 93
    TabletTrackingChange = 219
    ThreadChange = 22
    Timer = 1
    ToolBarChange = 120
    ToolTip = 110
    ToolTipChange = 184
    TouchBegin = 194
    TouchCancel = 209
    TouchEnd = 196
    TouchUpdate = 195
    UngrabKeyboard = 189
    UngrabMouse = 187
    UpdateLater = 78
    UpdateRequest = 77
    User = 1000
    WhatsThis = 111
    WhatsThisClicked = 118
    Wheel = 31
    WindowActivate = 24
    WindowBlocked = 103
    WindowDeactivate = 25
    WindowIconChange = 34
    WindowStateChange = 105
    WindowTitleChange = 33
    WindowUnblocked = 104
    WinEventAct = 132
    WinIdChange = 203
    ZOrderChange = 126


