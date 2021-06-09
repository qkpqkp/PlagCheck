# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QWidget import QWidget

class QWizardPage(QWidget):
    """ QWizardPage(parent: QWidget = None) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def buttonText(self, QWizard_WizardButton): # real signature unknown; restored from __doc__
        """ buttonText(self, QWizard.WizardButton) -> str """
        return ""

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def cleanupPage(self): # real signature unknown; restored from __doc__
        """ cleanupPage(self) """
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def completeChanged(self): # real signature unknown; restored from __doc__
        """ completeChanged(self) [signal] """
        pass

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

    def field(self, p_str): # real signature unknown; restored from __doc__
        """ field(self, str) -> Any """
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

    def initializePage(self): # real signature unknown; restored from __doc__
        """ initializePage(self) """
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isCommitPage(self): # real signature unknown; restored from __doc__
        """ isCommitPage(self) -> bool """
        return False

    def isComplete(self): # real signature unknown; restored from __doc__
        """ isComplete(self) -> bool """
        return False

    def isFinalPage(self): # real signature unknown; restored from __doc__
        """ isFinalPage(self) -> bool """
        return False

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

    def nextId(self): # real signature unknown; restored from __doc__
        """ nextId(self) -> int """
        return 0

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def pixmap(self, QWizard_WizardPixmap): # real signature unknown; restored from __doc__
        """ pixmap(self, QWizard.WizardPixmap) -> QPixmap """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def registerField(self, p_str, QWidget, property=None, changedSignal=0): # real signature unknown; restored from __doc__
        """ registerField(self, str, QWidget, property: str = None, changedSignal: PYQT_SIGNAL = 0) """
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setButtonText(self, QWizard_WizardButton, p_str): # real signature unknown; restored from __doc__
        """ setButtonText(self, QWizard.WizardButton, str) """
        pass

    def setCommitPage(self, bool): # real signature unknown; restored from __doc__
        """ setCommitPage(self, bool) """
        pass

    def setField(self, p_str, Any): # real signature unknown; restored from __doc__
        """ setField(self, str, Any) """
        pass

    def setFinalPage(self, bool): # real signature unknown; restored from __doc__
        """ setFinalPage(self, bool) """
        pass

    def setPixmap(self, QWizard_WizardPixmap, QPixmap): # real signature unknown; restored from __doc__
        """ setPixmap(self, QWizard.WizardPixmap, QPixmap) """
        pass

    def setSubTitle(self, p_str): # real signature unknown; restored from __doc__
        """ setSubTitle(self, str) """
        pass

    def setTitle(self, p_str): # real signature unknown; restored from __doc__
        """ setTitle(self, str) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def subTitle(self): # real signature unknown; restored from __doc__
        """ subTitle(self) -> str """
        return ""

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def title(self): # real signature unknown; restored from __doc__
        """ title(self) -> str """
        return ""

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def validatePage(self): # real signature unknown; restored from __doc__
        """ validatePage(self) -> bool """
        return False

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def wizard(self): # real signature unknown; restored from __doc__
        """ wizard(self) -> QWizard """
        return QWizard

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


