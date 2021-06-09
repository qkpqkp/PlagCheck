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

class QColorDialog(QDialog):
    """
    QColorDialog(parent: QWidget = None)
    QColorDialog(Union[QColor, Qt.GlobalColor, QGradient], parent: QWidget = None)
    """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ changeEvent(self, QEvent) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def colorSelected(self, Union, QColor=None, Qt_GlobalColor=None, QGradient=None): # real signature unknown; restored from __doc__
        """ colorSelected(self, Union[QColor, Qt.GlobalColor, QGradient]) [signal] """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def currentColor(self): # real signature unknown; restored from __doc__
        """ currentColor(self) -> QColor """
        pass

    def currentColorChanged(self, Union, QColor=None, Qt_GlobalColor=None, QGradient=None): # real signature unknown; restored from __doc__
        """ currentColorChanged(self, Union[QColor, Qt.GlobalColor, QGradient]) [signal] """
        pass

    def customColor(self, p_int): # real signature unknown; restored from __doc__
        """ customColor(int) -> QColor """
        pass

    def customCount(self): # real signature unknown; restored from __doc__
        """ customCount() -> int """
        return 0

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def done(self, p_int): # real signature unknown; restored from __doc__
        """ done(self, int) """
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

    def getColor(self, initial, QColor=None, Qt_GlobalColor=None, QGradient=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ getColor(initial: Union[QColor, Qt.GlobalColor, QGradient] = Qt.white, parent: QWidget = None, title: str = '', options: Union[QColorDialog.ColorDialogOptions, QColorDialog.ColorDialogOption] = QColorDialog.ColorDialogOptions()) -> QColor """
        pass

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
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

    def options(self): # real signature unknown; restored from __doc__
        """ options(self) -> QColorDialog.ColorDialogOptions """
        pass

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def selectedColor(self): # real signature unknown; restored from __doc__
        """ selectedColor(self) -> QColor """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCurrentColor(self, Union, QColor=None, Qt_GlobalColor=None, QGradient=None): # real signature unknown; restored from __doc__
        """ setCurrentColor(self, Union[QColor, Qt.GlobalColor, QGradient]) """
        pass

    def setCustomColor(self, p_int, Union, QColor=None, Qt_GlobalColor=None, QGradient=None): # real signature unknown; restored from __doc__
        """ setCustomColor(int, Union[QColor, Qt.GlobalColor, QGradient]) """
        pass

    def setOption(self, QColorDialog_ColorDialogOption, on=True): # real signature unknown; restored from __doc__
        """ setOption(self, QColorDialog.ColorDialogOption, on: bool = True) """
        pass

    def setOptions(self, Union, QColorDialog_ColorDialogOptions=None, QColorDialog_ColorDialogOption=None): # real signature unknown; restored from __doc__
        """ setOptions(self, Union[QColorDialog.ColorDialogOptions, QColorDialog.ColorDialogOption]) """
        pass

    def setStandardColor(self, p_int, Union, QColor=None, Qt_GlobalColor=None, QGradient=None): # real signature unknown; restored from __doc__
        """ setStandardColor(int, Union[QColor, Qt.GlobalColor, QGradient]) """
        pass

    def setVisible(self, bool): # real signature unknown; restored from __doc__
        """ setVisible(self, bool) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def standardColor(self, p_int): # real signature unknown; restored from __doc__
        """ standardColor(int) -> QColor """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def testOption(self, QColorDialog_ColorDialogOption): # real signature unknown; restored from __doc__
        """ testOption(self, QColorDialog.ColorDialogOption) -> bool """
        return False

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    DontUseNativeDialog = 4
    NoButtons = 2
    ShowAlphaChannel = 1


