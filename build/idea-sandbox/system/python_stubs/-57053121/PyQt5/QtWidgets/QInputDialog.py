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

class QInputDialog(QDialog):
    """ QInputDialog(parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def cancelButtonText(self): # real signature unknown; restored from __doc__
        """ cancelButtonText(self) -> str """
        return ""

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def comboBoxItems(self): # real signature unknown; restored from __doc__
        """ comboBoxItems(self) -> List[str] """
        return []

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def done(self, p_int): # real signature unknown; restored from __doc__
        """ done(self, int) """
        pass

    def doubleDecimals(self): # real signature unknown; restored from __doc__
        """ doubleDecimals(self) -> int """
        return 0

    def doubleMaximum(self): # real signature unknown; restored from __doc__
        """ doubleMaximum(self) -> float """
        return 0.0

    def doubleMinimum(self): # real signature unknown; restored from __doc__
        """ doubleMinimum(self) -> float """
        return 0.0

    def doubleStep(self): # real signature unknown; restored from __doc__
        """ doubleStep(self) -> float """
        return 0.0

    def doubleValue(self): # real signature unknown; restored from __doc__
        """ doubleValue(self) -> float """
        return 0.0

    def doubleValueChanged(self, p_float): # real signature unknown; restored from __doc__
        """ doubleValueChanged(self, float) [signal] """
        pass

    def doubleValueSelected(self, p_float): # real signature unknown; restored from __doc__
        """ doubleValueSelected(self, float) [signal] """
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

    def event(self, *args, **kwargs): # real signature unknown
        pass

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

    def getDouble(self, QWidget, p_str, p_str_1, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        getDouble(QWidget, str, str, value: float = 0, min: float = -2147483647, max: float = 2147483647, decimals: int = 1, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()) -> Tuple[float, bool]
        getDouble(QWidget, str, str, float, float, float, int, Union[Qt.WindowFlags, Qt.WindowType], float) -> Tuple[float, bool]
        """
        pass

    def getInt(self, QWidget, p_str, p_str_1, value=0, min=-2147483647, max=2147483647, step=1, flags, Qt_WindowFlags=None, Qt_WindowType=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ getInt(QWidget, str, str, value: int = 0, min: int = -2147483647, max: int = 2147483647, step: int = 1, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()) -> Tuple[int, bool] """
        pass

    def getItem(self, QWidget, p_str, p_str_1, Iterable, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ getItem(QWidget, str, str, Iterable[str], current: int = 0, editable: bool = True, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags(), inputMethodHints: Union[Qt.InputMethodHints, Qt.InputMethodHint] = Qt.ImhNone) -> Tuple[str, bool] """
        pass

    def getMultiLineText(self, QWidget, p_str, p_str_1, text='', flags, Qt_WindowFlags=None, Qt_WindowType=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ getMultiLineText(QWidget, str, str, text: str = '', flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags(), inputMethodHints: Union[Qt.InputMethodHints, Qt.InputMethodHint] = Qt.ImhNone) -> Tuple[str, bool] """
        pass

    def getText(self, QWidget, p_str, p_str_1, echo=None, text='', flags, Qt_WindowFlags=None, Qt_WindowType=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ getText(QWidget, str, str, echo: QLineEdit.EchoMode = QLineEdit.Normal, text: str = '', flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags(), inputMethodHints: Union[Qt.InputMethodHints, Qt.InputMethodHint] = Qt.ImhNone) -> Tuple[str, bool] """
        pass

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def inputMode(self): # real signature unknown; restored from __doc__
        """ inputMode(self) -> QInputDialog.InputMode """
        pass

    def intMaximum(self): # real signature unknown; restored from __doc__
        """ intMaximum(self) -> int """
        return 0

    def intMinimum(self): # real signature unknown; restored from __doc__
        """ intMinimum(self) -> int """
        return 0

    def intStep(self): # real signature unknown; restored from __doc__
        """ intStep(self) -> int """
        return 0

    def intValue(self): # real signature unknown; restored from __doc__
        """ intValue(self) -> int """
        return 0

    def intValueChanged(self, p_int): # real signature unknown; restored from __doc__
        """ intValueChanged(self, int) [signal] """
        pass

    def intValueSelected(self, p_int): # real signature unknown; restored from __doc__
        """ intValueSelected(self, int) [signal] """
        pass

    def isComboBoxEditable(self): # real signature unknown; restored from __doc__
        """ isComboBoxEditable(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def labelText(self): # real signature unknown; restored from __doc__
        """ labelText(self) -> str """
        return ""

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> QSize """
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

    def okButtonText(self): # real signature unknown; restored from __doc__
        """ okButtonText(self) -> str """
        return ""

    def open(self, PYQT_SLOT=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        open(self)
        open(self, PYQT_SLOT)
        """
        pass

    def options(self): # real signature unknown; restored from __doc__
        """ options(self) -> QInputDialog.InputDialogOptions """
        pass

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCancelButtonText(self, p_str): # real signature unknown; restored from __doc__
        """ setCancelButtonText(self, str) """
        pass

    def setComboBoxEditable(self, bool): # real signature unknown; restored from __doc__
        """ setComboBoxEditable(self, bool) """
        pass

    def setComboBoxItems(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ setComboBoxItems(self, Iterable[str]) """
        pass

    def setDoubleDecimals(self, p_int): # real signature unknown; restored from __doc__
        """ setDoubleDecimals(self, int) """
        pass

    def setDoubleMaximum(self, p_float): # real signature unknown; restored from __doc__
        """ setDoubleMaximum(self, float) """
        pass

    def setDoubleMinimum(self, p_float): # real signature unknown; restored from __doc__
        """ setDoubleMinimum(self, float) """
        pass

    def setDoubleRange(self, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ setDoubleRange(self, float, float) """
        pass

    def setDoubleStep(self, p_float): # real signature unknown; restored from __doc__
        """ setDoubleStep(self, float) """
        pass

    def setDoubleValue(self, p_float): # real signature unknown; restored from __doc__
        """ setDoubleValue(self, float) """
        pass

    def setInputMode(self, QInputDialog_InputMode): # real signature unknown; restored from __doc__
        """ setInputMode(self, QInputDialog.InputMode) """
        pass

    def setIntMaximum(self, p_int): # real signature unknown; restored from __doc__
        """ setIntMaximum(self, int) """
        pass

    def setIntMinimum(self, p_int): # real signature unknown; restored from __doc__
        """ setIntMinimum(self, int) """
        pass

    def setIntRange(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ setIntRange(self, int, int) """
        pass

    def setIntStep(self, p_int): # real signature unknown; restored from __doc__
        """ setIntStep(self, int) """
        pass

    def setIntValue(self, p_int): # real signature unknown; restored from __doc__
        """ setIntValue(self, int) """
        pass

    def setLabelText(self, p_str): # real signature unknown; restored from __doc__
        """ setLabelText(self, str) """
        pass

    def setOkButtonText(self, p_str): # real signature unknown; restored from __doc__
        """ setOkButtonText(self, str) """
        pass

    def setOption(self, QInputDialog_InputDialogOption, on=True): # real signature unknown; restored from __doc__
        """ setOption(self, QInputDialog.InputDialogOption, on: bool = True) """
        pass

    def setOptions(self, Union, QInputDialog_InputDialogOptions=None, QInputDialog_InputDialogOption=None): # real signature unknown; restored from __doc__
        """ setOptions(self, Union[QInputDialog.InputDialogOptions, QInputDialog.InputDialogOption]) """
        pass

    def setTextEchoMode(self, QLineEdit_EchoMode): # real signature unknown; restored from __doc__
        """ setTextEchoMode(self, QLineEdit.EchoMode) """
        pass

    def setTextValue(self, p_str): # real signature unknown; restored from __doc__
        """ setTextValue(self, str) """
        pass

    def setVisible(self, bool): # real signature unknown; restored from __doc__
        """ setVisible(self, bool) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def testOption(self, QInputDialog_InputDialogOption): # real signature unknown; restored from __doc__
        """ testOption(self, QInputDialog.InputDialogOption) -> bool """
        return False

    def textEchoMode(self): # real signature unknown; restored from __doc__
        """ textEchoMode(self) -> QLineEdit.EchoMode """
        pass

    def textValue(self): # real signature unknown; restored from __doc__
        """ textValue(self) -> str """
        return ""

    def textValueChanged(self, p_str): # real signature unknown; restored from __doc__
        """ textValueChanged(self, str) [signal] """
        pass

    def textValueSelected(self, p_str): # real signature unknown; restored from __doc__
        """ textValueSelected(self, str) [signal] """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None, flags, Qt_WindowFlags=None, Qt_WindowType=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    DoubleInput = 2
    IntInput = 1
    NoButtons = 1
    TextInput = 0
    UseListViewForComboBoxItems = 2
    UsePlainTextEditForTextInput = 4


