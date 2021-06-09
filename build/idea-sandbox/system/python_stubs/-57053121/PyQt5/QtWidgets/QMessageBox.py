# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QDialog import QDialog

class QMessageBox(QDialog):
    """
    QMessageBox(parent: QWidget = None)
    QMessageBox(QMessageBox.Icon, str, str, buttons: Union[QMessageBox.StandardButtons, QMessageBox.StandardButton] = QMessageBox.NoButton, parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.Dialog|Qt.MSWindowsFixedSizeDialogHint)
    """
    def about(self, QWidget, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ about(QWidget, str, str) """
        pass

    def aboutQt(self, QWidget, title=''): # real signature unknown; restored from __doc__
        """ aboutQt(QWidget, title: str = '') """
        pass

    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def addButton(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addButton(self, QAbstractButton, QMessageBox.ButtonRole)
        addButton(self, str, QMessageBox.ButtonRole) -> QPushButton
        addButton(self, QMessageBox.StandardButton) -> QPushButton
        """
        return QPushButton

    def button(self, QMessageBox_StandardButton): # real signature unknown; restored from __doc__
        """ button(self, QMessageBox.StandardButton) -> QAbstractButton """
        return QAbstractButton

    def buttonClicked(self, QAbstractButton): # real signature unknown; restored from __doc__
        """ buttonClicked(self, QAbstractButton) [signal] """
        pass

    def buttonRole(self, QAbstractButton): # real signature unknown; restored from __doc__
        """ buttonRole(self, QAbstractButton) -> QMessageBox.ButtonRole """
        pass

    def buttons(self): # real signature unknown; restored from __doc__
        """ buttons(self) -> List[QAbstractButton] """
        return []

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ changeEvent(self, QEvent) """
        pass

    def checkBox(self): # real signature unknown; restored from __doc__
        """ checkBox(self) -> QCheckBox """
        return QCheckBox

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clickedButton(self): # real signature unknown; restored from __doc__
        """ clickedButton(self) -> QAbstractButton """
        return QAbstractButton

    def closeEvent(self, QCloseEvent): # real signature unknown; restored from __doc__
        """ closeEvent(self, QCloseEvent) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def critical(self, QWidget, p_str, p_str_1, buttons, QMessageBox_StandardButtons=None, QMessageBox_StandardButton=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ critical(QWidget, str, str, buttons: Union[QMessageBox.StandardButtons, QMessageBox.StandardButton] = QMessageBox.Ok, defaultButton: QMessageBox.StandardButton = QMessageBox.NoButton) -> QMessageBox.StandardButton """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultButton(self): # real signature unknown; restored from __doc__
        """ defaultButton(self) -> QPushButton """
        return QPushButton

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def detailedText(self): # real signature unknown; restored from __doc__
        """ detailedText(self) -> str """
        return ""

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def escapeButton(self): # real signature unknown; restored from __doc__
        """ escapeButton(self) -> QAbstractButton """
        return QAbstractButton

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def eventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def focusInEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def icon(self): # real signature unknown; restored from __doc__
        """ icon(self) -> QMessageBox.Icon """
        pass

    def iconPixmap(self): # real signature unknown; restored from __doc__
        """ iconPixmap(self) -> QPixmap """
        pass

    def information(self, QWidget, p_str, p_str_1, buttons, QMessageBox_StandardButtons=None, QMessageBox_StandardButton=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ information(QWidget, str, str, buttons: Union[QMessageBox.StandardButtons, QMessageBox.StandardButton] = QMessageBox.Ok, defaultButton: QMessageBox.StandardButton = QMessageBox.NoButton) -> QMessageBox.StandardButton """
        pass

    def informativeText(self): # real signature unknown; restored from __doc__
        """ informativeText(self) -> str """
        return ""

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, QKeyEvent) """
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def open(self, PYQT_SLOT=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        open(self)
        open(self, PYQT_SLOT)
        """
        pass

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def question(self, QWidget, p_str, p_str_1, buttons, QMessageBox_StandardButtons=None, QMessageBox_StandardButton=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ question(QWidget, str, str, buttons: Union[QMessageBox.StandardButtons, QMessageBox.StandardButton] = QMessageBox.StandardButtons(QMessageBox.Yes|QMessageBox.No), defaultButton: QMessageBox.StandardButton = QMessageBox.NoButton) -> QMessageBox.StandardButton """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeButton(self, QAbstractButton): # real signature unknown; restored from __doc__
        """ removeButton(self, QAbstractButton) """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ resizeEvent(self, QResizeEvent) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCheckBox(self, QCheckBox): # real signature unknown; restored from __doc__
        """ setCheckBox(self, QCheckBox) """
        pass

    def setDefaultButton(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setDefaultButton(self, QPushButton)
        setDefaultButton(self, QMessageBox.StandardButton)
        """
        pass

    def setDetailedText(self, p_str): # real signature unknown; restored from __doc__
        """ setDetailedText(self, str) """
        pass

    def setEscapeButton(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setEscapeButton(self, QAbstractButton)
        setEscapeButton(self, QMessageBox.StandardButton)
        """
        pass

    def setIcon(self, QMessageBox_Icon): # real signature unknown; restored from __doc__
        """ setIcon(self, QMessageBox.Icon) """
        pass

    def setIconPixmap(self, QPixmap): # real signature unknown; restored from __doc__
        """ setIconPixmap(self, QPixmap) """
        pass

    def setInformativeText(self, p_str): # real signature unknown; restored from __doc__
        """ setInformativeText(self, str) """
        pass

    def setStandardButtons(self, Union, QMessageBox_StandardButtons=None, QMessageBox_StandardButton=None): # real signature unknown; restored from __doc__
        """ setStandardButtons(self, Union[QMessageBox.StandardButtons, QMessageBox.StandardButton]) """
        pass

    def setText(self, p_str): # real signature unknown; restored from __doc__
        """ setText(self, str) """
        pass

    def setTextFormat(self, Qt_TextFormat): # real signature unknown; restored from __doc__
        """ setTextFormat(self, Qt.TextFormat) """
        pass

    def setTextInteractionFlags(self, Union, Qt_TextInteractionFlags=None, Qt_TextInteractionFlag=None): # real signature unknown; restored from __doc__
        """ setTextInteractionFlags(self, Union[Qt.TextInteractionFlags, Qt.TextInteractionFlag]) """
        pass

    def setWindowModality(self, Qt_WindowModality): # real signature unknown; restored from __doc__
        """ setWindowModality(self, Qt.WindowModality) """
        pass

    def setWindowTitle(self, p_str): # real signature unknown; restored from __doc__
        """ setWindowTitle(self, str) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, QShowEvent): # real signature unknown; restored from __doc__
        """ showEvent(self, QShowEvent) """
        pass

    def standardButton(self, QAbstractButton): # real signature unknown; restored from __doc__
        """ standardButton(self, QAbstractButton) -> QMessageBox.StandardButton """
        pass

    def standardButtons(self): # real signature unknown; restored from __doc__
        """ standardButtons(self) -> QMessageBox.StandardButtons """
        pass

    def standardIcon(self, QMessageBox_Icon): # real signature unknown; restored from __doc__
        """ standardIcon(QMessageBox.Icon) -> QPixmap """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def textFormat(self): # real signature unknown; restored from __doc__
        """ textFormat(self) -> Qt.TextFormat """
        pass

    def textInteractionFlags(self): # real signature unknown; restored from __doc__
        """ textInteractionFlags(self) -> Qt.TextInteractionFlags """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def warning(self, QWidget, p_str, p_str_1, buttons, QMessageBox_StandardButtons=None, QMessageBox_StandardButton=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ warning(QWidget, str, str, buttons: Union[QMessageBox.StandardButtons, QMessageBox.StandardButton] = QMessageBox.Ok, defaultButton: QMessageBox.StandardButton = QMessageBox.NoButton) -> QMessageBox.StandardButton """
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    Abort = 262144
    AcceptRole = 0
    ActionRole = 3
    Apply = 33554432
    ApplyRole = 8
    ButtonMask = -769
    Cancel = 4194304
    Close = 2097152
    Critical = 3
    Default = 256
    DestructiveRole = 2
    Discard = 8388608
    Escape = 512
    FirstButton = 1024
    FlagMask = 768
    Help = 16777216
    HelpRole = 4
    Ignore = 1048576
    Information = 1
    InvalidRole = -1
    LastButton = 134217728
    No = 65536
    NoAll = 131072
    NoButton = 0
    NoIcon = 0
    NoRole = 6
    NoToAll = 131072
    Ok = 1024
    Open = 8192
    Question = 4
    RejectRole = 1
    Reset = 67108864
    ResetRole = 7
    RestoreDefaults = 134217728
    Retry = 524288
    Save = 2048
    SaveAll = 4096
    Warning = 2
    Yes = 16384
    YesAll = 32768
    YesRole = 5
    YesToAll = 32768


