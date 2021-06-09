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

class QDockWidget(QWidget):
    """
    QDockWidget(str, parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags())
    QDockWidget(parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags())
    """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def allowedAreas(self): # real signature unknown; restored from __doc__
        """ allowedAreas(self) -> Qt.DockWidgetAreas """
        pass

    def allowedAreasChanged(self, Union, Qt_DockWidgetAreas=None, Qt_DockWidgetArea=None): # real signature unknown; restored from __doc__
        """ allowedAreasChanged(self, Union[Qt.DockWidgetAreas, Qt.DockWidgetArea]) [signal] """
        pass

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ changeEvent(self, QEvent) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, QCloseEvent): # real signature unknown; restored from __doc__
        """ closeEvent(self, QCloseEvent) """
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

    def dockLocationChanged(self, Qt_DockWidgetArea): # real signature unknown; restored from __doc__
        """ dockLocationChanged(self, Qt.DockWidgetArea) [signal] """
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

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def features(self): # real signature unknown; restored from __doc__
        """ features(self) -> QDockWidget.DockWidgetFeatures """
        pass

    def featuresChanged(self, Union, QDockWidget_DockWidgetFeatures=None, QDockWidget_DockWidgetFeature=None): # real signature unknown; restored from __doc__
        """ featuresChanged(self, Union[QDockWidget.DockWidgetFeatures, QDockWidget.DockWidgetFeature]) [signal] """
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

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def initStyleOption(self, QStyleOptionDockWidget): # real signature unknown; restored from __doc__
        """ initStyleOption(self, QStyleOptionDockWidget) """
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isAreaAllowed(self, Qt_DockWidgetArea): # real signature unknown; restored from __doc__
        """ isAreaAllowed(self, Qt.DockWidgetArea) -> bool """
        return False

    def isFloating(self): # real signature unknown; restored from __doc__
        """ isFloating(self) -> bool """
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

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ paintEvent(self, QPaintEvent) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAllowedAreas(self, Union, Qt_DockWidgetAreas=None, Qt_DockWidgetArea=None): # real signature unknown; restored from __doc__
        """ setAllowedAreas(self, Union[Qt.DockWidgetAreas, Qt.DockWidgetArea]) """
        pass

    def setFeatures(self, Union, QDockWidget_DockWidgetFeatures=None, QDockWidget_DockWidgetFeature=None): # real signature unknown; restored from __doc__
        """ setFeatures(self, Union[QDockWidget.DockWidgetFeatures, QDockWidget.DockWidgetFeature]) """
        pass

    def setFloating(self, bool): # real signature unknown; restored from __doc__
        """ setFloating(self, bool) """
        pass

    def setTitleBarWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ setTitleBarWidget(self, QWidget) """
        pass

    def setWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ setWidget(self, QWidget) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def titleBarWidget(self): # real signature unknown; restored from __doc__
        """ titleBarWidget(self) -> QWidget """
        return QWidget

    def toggleViewAction(self): # real signature unknown; restored from __doc__
        """ toggleViewAction(self) -> QAction """
        return QAction

    def topLevelChanged(self, bool): # real signature unknown; restored from __doc__
        """ topLevelChanged(self, bool) [signal] """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def visibilityChanged(self, bool): # real signature unknown; restored from __doc__
        """ visibilityChanged(self, bool) [signal] """
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def widget(self): # real signature unknown; restored from __doc__
        """ widget(self) -> QWidget """
        return QWidget

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AllDockWidgetFeatures = 7
    DockWidgetClosable = 1
    DockWidgetFloatable = 4
    DockWidgetMovable = 2
    DockWidgetVerticalTitleBar = 8
    NoDockWidgetFeatures = 0


