# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QStyle(__PyQt5_QtCore.QObject):
    """ QStyle() """
    def alignedRect(self, Qt_LayoutDirection, Union, Qt_Alignment=None, Qt_AlignmentFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ alignedRect(Qt.LayoutDirection, Union[Qt.Alignment, Qt.AlignmentFlag], QSize, QRect) -> QRect """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def combinedLayoutSpacing(self, Union, QSizePolicy_ControlTypes=None, QSizePolicy_ControlType=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ combinedLayoutSpacing(self, Union[QSizePolicy.ControlTypes, QSizePolicy.ControlType], Union[QSizePolicy.ControlTypes, QSizePolicy.ControlType], Qt.Orientation, option: QStyleOption = None, widget: QWidget = None) -> int """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def drawComplexControl(self, QStyle_ComplexControl, QStyleOptionComplex, QPainter, widget=None): # real signature unknown; restored from __doc__
        """ drawComplexControl(self, QStyle.ComplexControl, QStyleOptionComplex, QPainter, widget: QWidget = None) """
        pass

    def drawControl(self, QStyle_ControlElement, QStyleOption, QPainter, widget=None): # real signature unknown; restored from __doc__
        """ drawControl(self, QStyle.ControlElement, QStyleOption, QPainter, widget: QWidget = None) """
        pass

    def drawItemPixmap(self, QPainter, QRect, p_int, QPixmap): # real signature unknown; restored from __doc__
        """ drawItemPixmap(self, QPainter, QRect, int, QPixmap) """
        pass

    def drawItemText(self, QPainter, QRect, p_int, QPalette, bool, p_str, textRole=None): # real signature unknown; restored from __doc__
        """ drawItemText(self, QPainter, QRect, int, QPalette, bool, str, textRole: QPalette.ColorRole = QPalette.NoRole) """
        pass

    def drawPrimitive(self, QStyle_PrimitiveElement, QStyleOption, QPainter, widget=None): # real signature unknown; restored from __doc__
        """ drawPrimitive(self, QStyle.PrimitiveElement, QStyleOption, QPainter, widget: QWidget = None) """
        pass

    def generatedIconPixmap(self, QIcon_Mode, QPixmap, QStyleOption): # real signature unknown; restored from __doc__
        """ generatedIconPixmap(self, QIcon.Mode, QPixmap, QStyleOption) -> QPixmap """
        pass

    def hitTestComplexControl(self, QStyle_ComplexControl, QStyleOptionComplex, QPoint, widget=None): # real signature unknown; restored from __doc__
        """ hitTestComplexControl(self, QStyle.ComplexControl, QStyleOptionComplex, QPoint, widget: QWidget = None) -> QStyle.SubControl """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def itemPixmapRect(self, QRect, p_int, QPixmap): # real signature unknown; restored from __doc__
        """ itemPixmapRect(self, QRect, int, QPixmap) -> QRect """
        pass

    def itemTextRect(self, QFontMetrics, QRect, p_int, bool, p_str): # real signature unknown; restored from __doc__
        """ itemTextRect(self, QFontMetrics, QRect, int, bool, str) -> QRect """
        pass

    def layoutSpacing(self, QSizePolicy_ControlType, QSizePolicy_ControlType_1, Qt_Orientation, option=None, widget=None): # real signature unknown; restored from __doc__
        """ layoutSpacing(self, QSizePolicy.ControlType, QSizePolicy.ControlType, Qt.Orientation, option: QStyleOption = None, widget: QWidget = None) -> int """
        return 0

    def pixelMetric(self, QStyle_PixelMetric, option=None, widget=None): # real signature unknown; restored from __doc__
        """ pixelMetric(self, QStyle.PixelMetric, option: QStyleOption = None, widget: QWidget = None) -> int """
        return 0

    def polish(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        polish(self, QWidget)
        polish(self, QApplication)
        polish(self, QPalette) -> QPalette
        """
        pass

    def proxy(self): # real signature unknown; restored from __doc__
        """ proxy(self) -> QStyle """
        return QStyle

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def sizeFromContents(self, QStyle_ContentsType, QStyleOption, QSize, widget=None): # real signature unknown; restored from __doc__
        """ sizeFromContents(self, QStyle.ContentsType, QStyleOption, QSize, widget: QWidget = None) -> QSize """
        pass

    def sliderPositionFromValue(self, p_int, p_int_1, p_int_2, p_int_3, upsideDown=False): # real signature unknown; restored from __doc__
        """ sliderPositionFromValue(int, int, int, int, upsideDown: bool = False) -> int """
        return 0

    def sliderValueFromPosition(self, p_int, p_int_1, p_int_2, p_int_3, upsideDown=False): # real signature unknown; restored from __doc__
        """ sliderValueFromPosition(int, int, int, int, upsideDown: bool = False) -> int """
        return 0

    def standardIcon(self, QStyle_StandardPixmap, option=None, widget=None): # real signature unknown; restored from __doc__
        """ standardIcon(self, QStyle.StandardPixmap, option: QStyleOption = None, widget: QWidget = None) -> QIcon """
        pass

    def standardPalette(self): # real signature unknown; restored from __doc__
        """ standardPalette(self) -> QPalette """
        pass

    def standardPixmap(self, QStyle_StandardPixmap, option=None, widget=None): # real signature unknown; restored from __doc__
        """ standardPixmap(self, QStyle.StandardPixmap, option: QStyleOption = None, widget: QWidget = None) -> QPixmap """
        pass

    def styleHint(self, QStyle_StyleHint, option=None, widget=None, returnData=None): # real signature unknown; restored from __doc__
        """ styleHint(self, QStyle.StyleHint, option: QStyleOption = None, widget: QWidget = None, returnData: QStyleHintReturn = None) -> int """
        return 0

    def subControlRect(self, QStyle_ComplexControl, QStyleOptionComplex, QStyle_SubControl, widget=None): # real signature unknown; restored from __doc__
        """ subControlRect(self, QStyle.ComplexControl, QStyleOptionComplex, QStyle.SubControl, widget: QWidget = None) -> QRect """
        pass

    def subElementRect(self, QStyle_SubElement, QStyleOption, widget=None): # real signature unknown; restored from __doc__
        """ subElementRect(self, QStyle.SubElement, QStyleOption, widget: QWidget = None) -> QRect """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def unpolish(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        unpolish(self, QWidget)
        unpolish(self, QApplication)
        """
        pass

    def visualAlignment(self, Qt_LayoutDirection, Union, Qt_Alignment=None, Qt_AlignmentFlag=None): # real signature unknown; restored from __doc__
        """ visualAlignment(Qt.LayoutDirection, Union[Qt.Alignment, Qt.AlignmentFlag]) -> Qt.Alignment """
        pass

    def visualPos(self, Qt_LayoutDirection, QRect, QPoint): # real signature unknown; restored from __doc__
        """ visualPos(Qt.LayoutDirection, QRect, QPoint) -> QPoint """
        pass

    def visualRect(self, Qt_LayoutDirection, QRect, QRect_1): # real signature unknown; restored from __doc__
        """ visualRect(Qt.LayoutDirection, QRect, QRect) -> QRect """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    CC_ComboBox = 1
    CC_CustomBase = -268435456
    CC_Dial = 6
    CC_GroupBox = 7
    CC_MdiControls = 8
    CC_ScrollBar = 2
    CC_Slider = 3
    CC_SpinBox = 0
    CC_TitleBar = 5
    CC_ToolButton = 4
    CE_CheckBox = 3
    CE_CheckBoxLabel = 4
    CE_ColumnViewGrip = 44
    CE_ComboBoxLabel = 39
    CE_CustomBase = -268435456
    CE_DockWidgetTitle = 30
    CE_FocusFrame = 38
    CE_Header = 23
    CE_HeaderEmptyArea = 43
    CE_HeaderLabel = 25
    CE_HeaderSection = 24
    CE_ItemViewItem = 45
    CE_MenuBarEmptyArea = 21
    CE_MenuBarItem = 20
    CE_MenuEmptyArea = 19
    CE_MenuHMargin = 17
    CE_MenuItem = 14
    CE_MenuScroller = 15
    CE_MenuTearoff = 18
    CE_MenuVMargin = 16
    CE_ProgressBar = 10
    CE_ProgressBarContents = 12
    CE_ProgressBarGroove = 11
    CE_ProgressBarLabel = 13
    CE_PushButton = 0
    CE_PushButtonBevel = 1
    CE_PushButtonLabel = 2
    CE_RadioButton = 5
    CE_RadioButtonLabel = 6
    CE_RubberBand = 29
    CE_ScrollBarAddLine = 31
    CE_ScrollBarAddPage = 33
    CE_ScrollBarFirst = 36
    CE_ScrollBarLast = 37
    CE_ScrollBarSlider = 35
    CE_ScrollBarSubLine = 32
    CE_ScrollBarSubPage = 34
    CE_ShapedFrame = 46
    CE_SizeGrip = 27
    CE_Splitter = 28
    CE_TabBarTab = 7
    CE_TabBarTabLabel = 9
    CE_TabBarTabShape = 8
    CE_ToolBar = 40
    CE_ToolBoxTab = 26
    CE_ToolBoxTabLabel = 42
    CE_ToolBoxTabShape = 41
    CE_ToolButtonLabel = 22
    CT_CheckBox = 1
    CT_ComboBox = 4
    CT_CustomBase = -268435456
    CT_DialogButtons = 18
    CT_GroupBox = 20
    CT_HeaderSection = 19
    CT_ItemViewItem = 22
    CT_LineEdit = 14
    CT_MdiControls = 21
    CT_Menu = 10
    CT_MenuBar = 9
    CT_MenuBarItem = 8
    CT_MenuItem = 7
    CT_ProgressBar = 6
    CT_PushButton = 0
    CT_RadioButton = 2
    CT_ScrollBar = 13
    CT_SizeGrip = 16
    CT_Slider = 12
    CT_SpinBox = 15
    CT_Splitter = 5
    CT_TabBarTab = 11
    CT_TabWidget = 17
    CT_ToolButton = 3
    PE_CustomBase = 251658240
    PE_Frame = 0
    PE_FrameButtonBevel = 10
    PE_FrameButtonTool = 11
    PE_FrameDefaultButton = 1
    PE_FrameDockWidget = 2
    PE_FrameFocusRect = 3
    PE_FrameGroupBox = 4
    PE_FrameLineEdit = 5
    PE_FrameMenu = 6
    PE_FrameStatusBar = 7
    PE_FrameStatusBarItem = 7
    PE_FrameTabBarBase = 12
    PE_FrameTabWidget = 8
    PE_FrameWindow = 9
    PE_IndicatorArrowDown = 19
    PE_IndicatorArrowLeft = 20
    PE_IndicatorArrowRight = 21
    PE_IndicatorArrowUp = 22
    PE_IndicatorBranch = 23
    PE_IndicatorButtonDropDown = 24
    PE_IndicatorCheckBox = 26
    PE_IndicatorColumnViewArrow = 42
    PE_IndicatorDockWidgetResizeHandle = 27
    PE_IndicatorHeaderArrow = 28
    PE_IndicatorItemViewItemCheck = 25
    PE_IndicatorItemViewItemDrop = 43
    PE_IndicatorMenuCheckMark = 29
    PE_IndicatorProgressChunk = 30
    PE_IndicatorRadioButton = 31
    PE_IndicatorSpinDown = 32
    PE_IndicatorSpinMinus = 33
    PE_IndicatorSpinPlus = 34
    PE_IndicatorSpinUp = 35
    PE_IndicatorTabClose = 47
    PE_IndicatorTabTear = 39
    PE_IndicatorTabTearLeft = 39
    PE_IndicatorTabTearRight = 49
    PE_IndicatorToolBarHandle = 36
    PE_IndicatorToolBarSeparator = 37
    PE_IndicatorViewItemCheck = 25
    PE_PanelButtonBevel = 14
    PE_PanelButtonCommand = 13
    PE_PanelButtonTool = 15
    PE_PanelItemViewItem = 44
    PE_PanelItemViewRow = 45
    PE_PanelLineEdit = 18
    PE_PanelMenu = 48
    PE_PanelMenuBar = 16
    PE_PanelScrollAreaCorner = 40
    PE_PanelStatusBar = 46
    PE_PanelTipLabel = 38
    PE_PanelToolBar = 17
    PE_Widget = 41
    PM_ButtonDefaultIndicator = 1
    PM_ButtonIconSize = 75
    PM_ButtonMargin = 0
    PM_ButtonShiftHorizontal = 3
    PM_ButtonShiftVertical = 4
    PM_CheckBoxLabelSpacing = 70
    PM_ComboBoxFrameWidth = 7
    PM_CustomBase = -268435456
    PM_DefaultChildMargin = 60
    PM_DefaultFrameWidth = 5
    PM_DefaultLayoutSpacing = 61
    PM_DefaultTopLevelMargin = 59
    PM_DialogButtonsButtonHeight = 43
    PM_DialogButtonsButtonWidth = 42
    PM_DialogButtonsSeparator = 41
    PM_DockWidgetFrameWidth = 18
    PM_DockWidgetHandleExtent = 17
    PM_DockWidgetSeparatorExtent = 16
    PM_DockWidgetTitleBarButtonMargin = 76
    PM_DockWidgetTitleMargin = 73
    PM_ExclusiveIndicatorHeight = 40
    PM_ExclusiveIndicatorWidth = 39
    PM_FocusFrameHMargin = 68
    PM_FocusFrameVMargin = 67
    PM_HeaderDefaultSectionSizeHorizontal = 92
    PM_HeaderDefaultSectionSizeVertical = 93
    PM_HeaderGripMargin = 48
    PM_HeaderMargin = 46
    PM_HeaderMarkSize = 47
    PM_IconViewIconSize = 64
    PM_IndicatorHeight = 38
    PM_IndicatorWidth = 37
    PM_LargeIconSize = 66
    PM_LayoutBottomMargin = 81
    PM_LayoutHorizontalSpacing = 82
    PM_LayoutLeftMargin = 78
    PM_LayoutRightMargin = 80
    PM_LayoutTopMargin = 79
    PM_LayoutVerticalSpacing = 83
    PM_ListViewIconSize = 63
    PM_MaximumDragDistance = 8
    PM_MDIFrameWidth = 44
    PM_MDIMinimizedWidth = 45
    PM_MdiSubWindowFrameWidth = 44
    PM_MdiSubWindowMinimizedWidth = 45
    PM_MenuBarHMargin = 36
    PM_MenuBarItemSpacing = 34
    PM_MenuBarPanelWidth = 33
    PM_MenuBarVMargin = 35
    PM_MenuButtonIndicator = 2
    PM_MenuDesktopFrameWidth = 32
    PM_MenuHMargin = 28
    PM_MenuPanelWidth = 30
    PM_MenuScrollerHeight = 27
    PM_MenuTearoffHeight = 31
    PM_MenuVMargin = 29
    PM_MessageBoxIconSize = 74
    PM_ProgressBarChunkWidth = 24
    PM_RadioButtonLabelSpacing = 77
    PM_ScrollBarExtent = 9
    PM_ScrollBarSliderMin = 10
    PM_ScrollView_ScrollBarOverlap = 89
    PM_ScrollView_ScrollBarSpacing = 88
    PM_SizeGripSize = 72
    PM_SliderControlThickness = 12
    PM_SliderLength = 13
    PM_SliderSpaceAvailable = 15
    PM_SliderThickness = 11
    PM_SliderTickmarkOffset = 14
    PM_SmallIconSize = 65
    PM_SpinBoxFrameWidth = 6
    PM_SpinBoxSliderHeight = 58
    PM_SplitterWidth = 25
    PM_SubMenuOverlap = 90
    PM_TabBarBaseHeight = 22
    PM_TabBarBaseOverlap = 23
    PM_TabBarIconSize = 71
    PM_TabBarScrollButtonWidth = 51
    PM_TabBarTabHSpace = 20
    PM_TabBarTabOverlap = 19
    PM_TabBarTabShiftHorizontal = 49
    PM_TabBarTabShiftVertical = 50
    PM_TabBarTabVSpace = 21
    PM_TabBar_ScrollButtonOverlap = 84
    PM_TabCloseIndicatorHeight = 87
    PM_TabCloseIndicatorWidth = 86
    PM_TextCursorWidth = 85
    PM_TitleBarButtonIconSize = 94
    PM_TitleBarButtonSize = 95
    PM_TitleBarHeight = 26
    PM_ToolBarExtensionExtent = 57
    PM_ToolBarFrameWidth = 52
    PM_ToolBarHandleExtent = 53
    PM_ToolBarIconSize = 62
    PM_ToolBarItemMargin = 55
    PM_ToolBarItemSpacing = 54
    PM_ToolBarSeparatorExtent = 56
    PM_ToolTipLabelFrameWidth = 69
    PM_TreeViewIndentation = 91
    RSIP_OnMouseClick = 1
    RSIP_OnMouseClickAndAlreadyFocused = 0
    SC_All = -1
    SC_ComboBoxArrow = 4
    SC_ComboBoxEditField = 2
    SC_ComboBoxFrame = 1
    SC_ComboBoxListBoxPopup = 8
    SC_CustomBase = -268435456
    SC_DialGroove = 1
    SC_DialHandle = 2
    SC_DialTickmarks = 4
    SC_GroupBoxCheckBox = 1
    SC_GroupBoxContents = 4
    SC_GroupBoxFrame = 8
    SC_GroupBoxLabel = 2
    SC_MdiCloseButton = 4
    SC_MdiMinButton = 1
    SC_MdiNormalButton = 2
    SC_None = 0
    SC_ScrollBarAddLine = 1
    SC_ScrollBarAddPage = 4
    SC_ScrollBarFirst = 16
    SC_ScrollBarGroove = 128
    SC_ScrollBarLast = 32
    SC_ScrollBarSlider = 64
    SC_ScrollBarSubLine = 2
    SC_ScrollBarSubPage = 8
    SC_SliderGroove = 1
    SC_SliderHandle = 2
    SC_SliderTickmarks = 4
    SC_SpinBoxDown = 2
    SC_SpinBoxEditField = 8
    SC_SpinBoxFrame = 4
    SC_SpinBoxUp = 1
    SC_TitleBarCloseButton = 8
    SC_TitleBarContextHelpButton = 128
    SC_TitleBarLabel = 256
    SC_TitleBarMaxButton = 4
    SC_TitleBarMinButton = 2
    SC_TitleBarNormalButton = 16
    SC_TitleBarShadeButton = 32
    SC_TitleBarSysMenu = 1
    SC_TitleBarUnshadeButton = 64
    SC_ToolButton = 1
    SC_ToolButtonMenu = 2
    SE_CheckBoxClickRect = 5
    SE_CheckBoxContents = 3
    SE_CheckBoxFocusRect = 4
    SE_CheckBoxIndicator = 2
    SE_CheckBoxLayoutItem = 32
    SE_ComboBoxFocusRect = 10
    SE_ComboBoxLayoutItem = 33
    SE_CustomBase = -268435456
    SE_DateTimeEditLayoutItem = 34
    SE_DialogButtonBoxLayoutItem = 35
    SE_DockWidgetCloseButton = 28
    SE_DockWidgetFloatButton = 29
    SE_DockWidgetIcon = 31
    SE_DockWidgetTitleBarText = 30
    SE_FrameContents = 27
    SE_FrameLayoutItem = 43
    SE_GroupBoxLayoutItem = 44
    SE_HeaderArrow = 17
    SE_HeaderLabel = 16
    SE_ItemViewItemCheckIndicator = 23
    SE_ItemViewItemDecoration = 46
    SE_ItemViewItemFocusRect = 48
    SE_ItemViewItemText = 47
    SE_LabelLayoutItem = 36
    SE_LineEditContents = 26
    SE_ProgressBarContents = 13
    SE_ProgressBarGroove = 12
    SE_ProgressBarLabel = 14
    SE_ProgressBarLayoutItem = 37
    SE_PushButtonContents = 0
    SE_PushButtonFocusRect = 1
    SE_PushButtonLayoutItem = 38
    SE_RadioButtonClickRect = 9
    SE_RadioButtonContents = 7
    SE_RadioButtonFocusRect = 8
    SE_RadioButtonIndicator = 6
    SE_RadioButtonLayoutItem = 39
    SE_ShapedFrameContents = 52
    SE_SliderFocusRect = 11
    SE_SliderLayoutItem = 40
    SE_SpinBoxLayoutItem = 41
    SE_TabBarScrollLeftButton = 54
    SE_TabBarScrollRightButton = 55
    SE_TabBarTabLeftButton = 49
    SE_TabBarTabRightButton = 50
    SE_TabBarTabText = 51
    SE_TabBarTearIndicator = 24
    SE_TabBarTearIndicatorLeft = 24
    SE_TabBarTearIndicatorRight = 56
    SE_TabWidgetLayoutItem = 45
    SE_TabWidgetLeftCorner = 21
    SE_TabWidgetRightCorner = 22
    SE_TabWidgetTabBar = 18
    SE_TabWidgetTabContents = 20
    SE_TabWidgetTabPane = 19
    SE_ToolBarHandle = 53
    SE_ToolBoxTabContents = 15
    SE_ToolButtonLayoutItem = 42
    SE_TreeViewDisclosureItem = 25
    SE_ViewItemCheckIndicator = 23
    SH_BlinkCursorWhenTextSelected = 28
    SH_Button_FocusPolicy = 49
    SH_ComboBox_AllowWheelScrolling = 115
    SH_ComboBox_LayoutDirection = 58
    SH_ComboBox_ListMouseTracking = 19
    SH_ComboBox_Popup = 25
    SH_ComboBox_PopupFrameStyle = 69
    SH_CustomBase = -268435456
    SH_DialogButtonBox_ButtonsHaveIcons = 71
    SH_DialogButtonLayout = 68
    SH_DialogButtons_DefaultButton = 36
    SH_Dial_BackgroundRole = 57
    SH_DitherDisabledText = 1
    SH_DockWidget_ButtonsHaveFrame = 94
    SH_DrawMenuBarSeparator = 47
    SH_EtchDisabledText = 0
    SH_FocusFrame_AboveWidget = 77
    SH_FocusFrame_Mask = 53
    SH_FontDialog_SelectAssociatedText = 13
    SH_FormLayoutFieldGrowthPolicy = 89
    SH_FormLayoutFormAlignment = 90
    SH_FormLayoutLabelAlignment = 91
    SH_FormLayoutWrapPolicy = 86
    SH_GroupBox_TextLabelColor = 32
    SH_GroupBox_TextLabelVerticalAlignment = 31
    SH_Header_ArrowAlignment = 6
    SH_ItemView_ActivateItemOnSingleClick = 61
    SH_ItemView_ArrowKeysNavigateIntoChildren = 80
    SH_ItemView_ChangeHighlightOnFocus = 22
    SH_ItemView_DrawDelegateFrame = 92
    SH_ItemView_EllipsisLocation = 59
    SH_ItemView_MovementWithoutUpdatingSelection = 75
    SH_ItemView_PaintAlternatingRowColorsForEmptyArea = 85
    SH_ItemView_ScrollMode = 112
    SH_ItemView_ShowDecorationSelected = 60
    SH_LineEdit_PasswordCharacter = 35
    SH_LineEdit_PasswordMaskDelay = 104
    SH_ListViewExpand_SelectMouseType = 40
    SH_MainWindow_SpaceBelowMenuBar = 12
    SH_MenuBar_AltKeyNavigation = 18
    SH_MenuBar_MouseTracking = 21
    SH_Menu_AllowActiveAndDisabled = 14
    SH_Menu_FadeOutOnHide = 83
    SH_Menu_FillScreenWithScroll = 45
    SH_Menu_FlashTriggeredItem = 82
    SH_Menu_KeyboardSearch = 66
    SH_Menu_Mask = 81
    SH_Menu_MouseTracking = 20
    SH_Menu_Scrollable = 30
    SH_Menu_SelectionWrap = 74
    SH_Menu_SloppySubMenus = 33
    SH_Menu_SpaceActivatesItem = 15
    SH_Menu_SubMenuDontStartSloppyOnLeave = 111
    SH_Menu_SubMenuPopupDelay = 16
    SH_Menu_SubMenuResetWhenReenteringParent = 110
    SH_Menu_SubMenuSloppyCloseTimeout = 109
    SH_Menu_SubMenuSloppySelectOtherActions = 108
    SH_Menu_SubMenuUniDirection = 106
    SH_Menu_SubMenuUniDirectionFailCount = 107
    SH_Menu_SupportsSections = 98
    SH_MessageBox_CenterButtons = 73
    SH_MessageBox_TextInteractionFlags = 70
    SH_MessageBox_UseBorderForButtonSpacing = 50
    SH_PrintDialog_RightAlignButtons = 11
    SH_ProgressDialog_CenterCancelButton = 9
    SH_ProgressDialog_TextLabelAlignment = 10
    SH_RequestSoftwareInputPanel = 96
    SH_RichText_FullWidthSelection = 29
    SH_RubberBand_Mask = 54
    SH_ScrollBar_ContextMenu = 62
    SH_ScrollBar_LeftClickAbsolutePosition = 39
    SH_ScrollBar_MiddleClickAbsolutePosition = 2
    SH_ScrollBar_RollBetweenButtons = 63
    SH_ScrollBar_ScrollWhenPointerLeavesControl = 3
    SH_ScrollBar_StopMouseOverSlider = 27
    SH_ScrollBar_Transient = 97
    SH_ScrollView_FrameOnlyAroundContents = 17
    SH_Slider_AbsoluteSetButtons = 64
    SH_Slider_PageSetButtons = 65
    SH_Slider_SloppyKeyEvents = 8
    SH_Slider_SnapToValue = 7
    SH_Slider_StopMouseOverSlider = 27
    SH_SpellCheckUnderlineStyle = 72
    SH_SpinBox_AnimateButton = 42
    SH_SpinBox_ButtonsInsideFrame = 116
    SH_SpinBox_ClickAutoRepeatRate = 44
    SH_SpinBox_ClickAutoRepeatThreshold = 84
    SH_SpinBox_KeyPressAutoRepeatRate = 43
    SH_SpinBox_StepModifier = 117
    SH_SpinControls_DisableOnBounds = 56
    SH_Splitter_OpaqueResize = 102
    SH_TabBar_Alignment = 5
    SH_TabBar_ChangeCurrentDelay = 105
    SH_TabBar_CloseButtonPosition = 93
    SH_TabBar_ElideMode = 67
    SH_TabBar_PreferNoArrows = 38
    SH_TabBar_SelectMouseType = 4
    SH_Table_GridLineColor = 34
    SH_TabWidget_DefaultTabPosition = 87
    SH_TextControl_FocusIndicatorTextCharFormat = 78
    SH_TitleBar_AutoRaise = 51
    SH_TitleBar_ModifyNotification = 48
    SH_TitleBar_NoBorder = 26
    SH_TitleBar_ShowToolTipsOnButtons = 113
    SH_ToolBar_Movable = 88
    SH_ToolBox_SelectedPageTitleBold = 37
    SH_ToolButtonStyle = 95
    SH_ToolButton_PopupDelay = 52
    SH_ToolTipLabel_Opacity = 46
    SH_ToolTip_FallAsleepDelay = 100
    SH_ToolTip_Mask = 76
    SH_ToolTip_WakeUpDelay = 99
    SH_UnderlineShortcut = 41
    SH_Widget_Animate = 101
    SH_Widget_Animation_Duration = 114
    SH_Widget_ShareActivation = 23
    SH_WindowFrame_Mask = 55
    SH_WizardStyle = 79
    SH_Workspace_FillSpaceOnMaximize = 24
    SP_ArrowBack = 54
    SP_ArrowDown = 51
    SP_ArrowForward = 55
    SP_ArrowLeft = 52
    SP_ArrowRight = 53
    SP_ArrowUp = 50
    SP_BrowserReload = 59
    SP_BrowserStop = 60
    SP_CommandLink = 57
    SP_ComputerIcon = 15
    SP_CustomBase = -268435456
    SP_DesktopIcon = 13
    SP_DialogApplyButton = 45
    SP_DialogCancelButton = 40
    SP_DialogCloseButton = 44
    SP_DialogDiscardButton = 47
    SP_DialogHelpButton = 41
    SP_DialogNoButton = 49
    SP_DialogOkButton = 39
    SP_DialogOpenButton = 42
    SP_DialogResetButton = 46
    SP_DialogSaveButton = 43
    SP_DialogYesButton = 48
    SP_DirClosedIcon = 22
    SP_DirHomeIcon = 56
    SP_DirIcon = 38
    SP_DirLinkIcon = 23
    SP_DirLinkOpenIcon = 24
    SP_DirOpenIcon = 21
    SP_DockWidgetCloseButton = 8
    SP_DriveCDIcon = 18
    SP_DriveDVDIcon = 19
    SP_DriveFDIcon = 16
    SP_DriveHDIcon = 17
    SP_DriveNetIcon = 20
    SP_FileDialogBack = 37
    SP_FileDialogContentsView = 35
    SP_FileDialogDetailedView = 33
    SP_FileDialogEnd = 30
    SP_FileDialogInfoView = 34
    SP_FileDialogListView = 36
    SP_FileDialogNewFolder = 32
    SP_FileDialogStart = 29
    SP_FileDialogToParent = 31
    SP_FileIcon = 25
    SP_FileLinkIcon = 26
    SP_LineEditClearButton = 70
    SP_MediaPause = 63
    SP_MediaPlay = 61
    SP_MediaSeekBackward = 67
    SP_MediaSeekForward = 66
    SP_MediaSkipBackward = 65
    SP_MediaSkipForward = 64
    SP_MediaStop = 62
    SP_MediaVolume = 68
    SP_MediaVolumeMuted = 69
    SP_MessageBoxCritical = 11
    SP_MessageBoxInformation = 9
    SP_MessageBoxQuestion = 12
    SP_MessageBoxWarning = 10
    SP_TitleBarCloseButton = 3
    SP_TitleBarContextHelpButton = 7
    SP_TitleBarMaxButton = 2
    SP_TitleBarMenuButton = 0
    SP_TitleBarMinButton = 1
    SP_TitleBarNormalButton = 4
    SP_TitleBarShadeButton = 5
    SP_TitleBarUnshadeButton = 6
    SP_ToolBarHorizontalExtensionButton = 27
    SP_ToolBarVerticalExtensionButton = 28
    SP_TrashIcon = 14
    SP_VistaShield = 58
    State_Active = 65536
    State_AutoRaise = 4096
    State_Bottom = 1024
    State_Children = 524288
    State_DownArrow = 64
    State_Editing = 4194304
    State_Enabled = 1
    State_FocusAtBorder = 2048
    State_HasFocus = 256
    State_Horizontal = 128
    State_Item = 1048576
    State_KeyboardFocusChange = 8388608
    State_Mini = 134217728
    State_MouseOver = 8192
    State_NoChange = 16
    State_None = 0
    State_Off = 8
    State_On = 32
    State_Open = 262144
    State_Raised = 2
    State_ReadOnly = 33554432
    State_Selected = 32768
    State_Sibling = 2097152
    State_Small = 67108864
    State_Sunken = 4
    State_Top = 512
    State_UpArrow = 16384
    State_Window = 131072


