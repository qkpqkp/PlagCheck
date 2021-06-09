# encoding: utf-8
# module PyQt5.QtDesigner
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtDesigner.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtWidgets as __PyQt5_QtWidgets
import sip as __sip


# no functions
# classes

class QAbstractExtensionFactory(__sip.simplewrapper):
    """
    QAbstractExtensionFactory()
    QAbstractExtensionFactory(QAbstractExtensionFactory)
    """
    def extension(self, QObject, p_str): # real signature unknown; restored from __doc__
        """ extension(self, QObject, str) -> QObject """
        pass

    def __init__(self, QAbstractExtensionFactory=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QAbstractExtensionManager(__sip.simplewrapper):
    """
    QAbstractExtensionManager()
    QAbstractExtensionManager(QAbstractExtensionManager)
    """
    def extension(self, QObject, p_str): # real signature unknown; restored from __doc__
        """ extension(self, QObject, str) -> QObject """
        pass

    def registerExtensions(self, QAbstractExtensionFactory, p_str): # real signature unknown; restored from __doc__
        """ registerExtensions(self, QAbstractExtensionFactory, str) """
        pass

    def unregisterExtensions(self, QAbstractExtensionFactory, p_str): # real signature unknown; restored from __doc__
        """ unregisterExtensions(self, QAbstractExtensionFactory, str) """
        pass

    def __init__(self, QAbstractExtensionManager=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QAbstractFormBuilder(__sip.simplewrapper):
    """ QAbstractFormBuilder() """
    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def load(self, QIODevice, parent=None): # real signature unknown; restored from __doc__
        """ load(self, QIODevice, parent: QWidget = None) -> QWidget """
        pass

    def save(self, QIODevice, QWidget): # real signature unknown; restored from __doc__
        """ save(self, QIODevice, QWidget) """
        pass

    def setWorkingDirectory(self, QDir): # real signature unknown; restored from __doc__
        """ setWorkingDirectory(self, QDir) """
        pass

    def workingDirectory(self): # real signature unknown; restored from __doc__
        """ workingDirectory(self) -> QDir """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QDesignerActionEditorInterface(__PyQt5_QtWidgets.QWidget):
    """ QDesignerActionEditorInterface(QWidget, flags: Union[Qt.WindowFlags, Qt.WindowType] = 0) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def core(self): # real signature unknown; restored from __doc__
        """ core(self) -> QDesignerFormEditorInterface """
        return QDesignerFormEditorInterface

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

    def manageAction(self, QAction): # real signature unknown; restored from __doc__
        """ manageAction(self, QAction) """
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

    def setFormWindow(self, QDesignerFormWindowInterface): # real signature unknown; restored from __doc__
        """ setFormWindow(self, QDesignerFormWindowInterface) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def unmanageAction(self, QAction): # real signature unknown; restored from __doc__
        """ unmanageAction(self, QAction) """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, QWidget, flags, Qt_WindowFlags=None, Qt_WindowType=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


class QDesignerContainerExtension(__sip.simplewrapper):
    """
    QDesignerContainerExtension()
    QDesignerContainerExtension(QDesignerContainerExtension)
    """
    def addWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ addWidget(self, QWidget) """
        pass

    def canAddWidget(self): # real signature unknown; restored from __doc__
        """ canAddWidget(self) -> bool """
        return False

    def canRemove(self, p_int): # real signature unknown; restored from __doc__
        """ canRemove(self, int) -> bool """
        return False

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def currentIndex(self): # real signature unknown; restored from __doc__
        """ currentIndex(self) -> int """
        return 0

    def insertWidget(self, p_int, QWidget): # real signature unknown; restored from __doc__
        """ insertWidget(self, int, QWidget) """
        pass

    def remove(self, p_int): # real signature unknown; restored from __doc__
        """ remove(self, int) """
        pass

    def setCurrentIndex(self, p_int): # real signature unknown; restored from __doc__
        """ setCurrentIndex(self, int) """
        pass

    def widget(self, p_int): # real signature unknown; restored from __doc__
        """ widget(self, int) -> QWidget """
        pass

    def __init__(self, QDesignerContainerExtension=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QDesignerCustomWidgetCollectionInterface(__sip.simplewrapper):
    """
    QDesignerCustomWidgetCollectionInterface()
    QDesignerCustomWidgetCollectionInterface(QDesignerCustomWidgetCollectionInterface)
    """
    def customWidgets(self): # real signature unknown; restored from __doc__
        """ customWidgets(self) -> List[QDesignerCustomWidgetInterface] """
        return []

    def __init__(self, QDesignerCustomWidgetCollectionInterface=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QDesignerCustomWidgetInterface(__sip.simplewrapper):
    """
    QDesignerCustomWidgetInterface()
    QDesignerCustomWidgetInterface(QDesignerCustomWidgetInterface)
    """
    def codeTemplate(self): # real signature unknown; restored from __doc__
        """ codeTemplate(self) -> str """
        return ""

    def createWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ createWidget(self, QWidget) -> QWidget """
        pass

    def domXml(self): # real signature unknown; restored from __doc__
        """ domXml(self) -> str """
        return ""

    def group(self): # real signature unknown; restored from __doc__
        """ group(self) -> str """
        return ""

    def icon(self): # real signature unknown; restored from __doc__
        """ icon(self) -> QIcon """
        pass

    def includeFile(self): # real signature unknown; restored from __doc__
        """ includeFile(self) -> str """
        return ""

    def initialize(self, QDesignerFormEditorInterface): # real signature unknown; restored from __doc__
        """ initialize(self, QDesignerFormEditorInterface) """
        pass

    def isContainer(self): # real signature unknown; restored from __doc__
        """ isContainer(self) -> bool """
        return False

    def isInitialized(self): # real signature unknown; restored from __doc__
        """ isInitialized(self) -> bool """
        return False

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def toolTip(self): # real signature unknown; restored from __doc__
        """ toolTip(self) -> str """
        return ""

    def whatsThis(self): # real signature unknown; restored from __doc__
        """ whatsThis(self) -> str """
        return ""

    def __init__(self, QDesignerCustomWidgetInterface=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QDesignerFormEditorInterface(__PyQt5_QtCore.QObject):
    """ QDesignerFormEditorInterface(parent: QObject = None) """
    def actionEditor(self): # real signature unknown; restored from __doc__
        """ actionEditor(self) -> QDesignerActionEditorInterface """
        return QDesignerActionEditorInterface

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def extensionManager(self): # real signature unknown; restored from __doc__
        """ extensionManager(self) -> QExtensionManager """
        return QExtensionManager

    def formWindowManager(self): # real signature unknown; restored from __doc__
        """ formWindowManager(self) -> QDesignerFormWindowManagerInterface """
        return QDesignerFormWindowManagerInterface

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def objectInspector(self): # real signature unknown; restored from __doc__
        """ objectInspector(self) -> QDesignerObjectInspectorInterface """
        return QDesignerObjectInspectorInterface

    def propertyEditor(self): # real signature unknown; restored from __doc__
        """ propertyEditor(self) -> QDesignerPropertyEditorInterface """
        return QDesignerPropertyEditorInterface

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setActionEditor(self, QDesignerActionEditorInterface): # real signature unknown; restored from __doc__
        """ setActionEditor(self, QDesignerActionEditorInterface) """
        pass

    def setObjectInspector(self, QDesignerObjectInspectorInterface): # real signature unknown; restored from __doc__
        """ setObjectInspector(self, QDesignerObjectInspectorInterface) """
        pass

    def setPropertyEditor(self, QDesignerPropertyEditorInterface): # real signature unknown; restored from __doc__
        """ setPropertyEditor(self, QDesignerPropertyEditorInterface) """
        pass

    def setWidgetBox(self, QDesignerWidgetBoxInterface): # real signature unknown; restored from __doc__
        """ setWidgetBox(self, QDesignerWidgetBoxInterface) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def topLevel(self): # real signature unknown; restored from __doc__
        """ topLevel(self) -> QWidget """
        pass

    def widgetBox(self): # real signature unknown; restored from __doc__
        """ widgetBox(self) -> QDesignerWidgetBoxInterface """
        return QDesignerWidgetBoxInterface

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


class QDesignerFormWindowCursorInterface(__sip.simplewrapper):
    """
    QDesignerFormWindowCursorInterface()
    QDesignerFormWindowCursorInterface(QDesignerFormWindowCursorInterface)
    """
    def current(self): # real signature unknown; restored from __doc__
        """ current(self) -> QWidget """
        pass

    def formWindow(self): # real signature unknown; restored from __doc__
        """ formWindow(self) -> QDesignerFormWindowInterface """
        return QDesignerFormWindowInterface

    def hasSelection(self): # real signature unknown; restored from __doc__
        """ hasSelection(self) -> bool """
        return False

    def isWidgetSelected(self, QWidget): # real signature unknown; restored from __doc__
        """ isWidgetSelected(self, QWidget) -> bool """
        return False

    def movePosition(self, QDesignerFormWindowCursorInterface_MoveOperation, mode=None): # real signature unknown; restored from __doc__
        """ movePosition(self, QDesignerFormWindowCursorInterface.MoveOperation, mode: QDesignerFormWindowCursorInterface.MoveMode = QDesignerFormWindowCursorInterface.MoveAnchor) -> bool """
        return False

    def position(self): # real signature unknown; restored from __doc__
        """ position(self) -> int """
        return 0

    def resetWidgetProperty(self, QWidget, p_str): # real signature unknown; restored from __doc__
        """ resetWidgetProperty(self, QWidget, str) """
        pass

    def selectedWidget(self, p_int): # real signature unknown; restored from __doc__
        """ selectedWidget(self, int) -> QWidget """
        pass

    def selectedWidgetCount(self): # real signature unknown; restored from __doc__
        """ selectedWidgetCount(self) -> int """
        return 0

    def setPosition(self, p_int, mode=None): # real signature unknown; restored from __doc__
        """ setPosition(self, int, mode: QDesignerFormWindowCursorInterface.MoveMode = QDesignerFormWindowCursorInterface.MoveAnchor) """
        pass

    def setProperty(self, p_str, Any): # real signature unknown; restored from __doc__
        """ setProperty(self, str, Any) """
        pass

    def setWidgetProperty(self, QWidget, p_str, Any): # real signature unknown; restored from __doc__
        """ setWidgetProperty(self, QWidget, str, Any) """
        pass

    def widget(self, p_int): # real signature unknown; restored from __doc__
        """ widget(self, int) -> QWidget """
        pass

    def widgetCount(self): # real signature unknown; restored from __doc__
        """ widgetCount(self) -> int """
        return 0

    def __init__(self, QDesignerFormWindowCursorInterface=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Down = 8
    End = 2
    KeepAnchor = 1
    Left = 5
    MoveAnchor = 0
    Next = 3
    NoMove = 0
    Prev = 4
    Right = 6
    Start = 1
    Up = 7


class QDesignerFormWindowInterface(__PyQt5_QtWidgets.QWidget):
    # no doc
    def aboutToUnmanageWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ aboutToUnmanageWidget(self, QWidget) [signal] """
        pass

    def absoluteDir(self): # real signature unknown; restored from __doc__
        """ absoluteDir(self) -> QDir """
        pass

    def activated(self, QWidget): # real signature unknown; restored from __doc__
        """ activated(self, QWidget) [signal] """
        pass

    def activateResourceFilePaths(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ activateResourceFilePaths(self, Iterable[str]) -> Tuple[int, str] """
        pass

    def activeResourceFilePaths(self): # real signature unknown; restored from __doc__
        """ activeResourceFilePaths(self) -> List[str] """
        return []

    def addResourceFile(self, p_str): # real signature unknown; restored from __doc__
        """ addResourceFile(self, str) """
        pass

    def author(self): # real signature unknown; restored from __doc__
        """ author(self) -> str """
        return ""

    def changed(self): # real signature unknown; restored from __doc__
        """ changed(self) [signal] """
        pass

    def checkContents(self): # real signature unknown; restored from __doc__
        """ checkContents(self) -> List[str] """
        return []

    def clearSelection(self, update=True): # real signature unknown; restored from __doc__
        """ clearSelection(self, update: bool = True) """
        pass

    def comment(self): # real signature unknown; restored from __doc__
        """ comment(self) -> str """
        return ""

    def contents(self): # real signature unknown; restored from __doc__
        """ contents(self) -> str """
        return ""

    def core(self): # real signature unknown; restored from __doc__
        """ core(self) -> QDesignerFormEditorInterface """
        return QDesignerFormEditorInterface

    def cursor(self): # real signature unknown; restored from __doc__
        """ cursor(self) -> QDesignerFormWindowCursorInterface """
        return QDesignerFormWindowCursorInterface

    def emitSelectionChanged(self): # real signature unknown; restored from __doc__
        """ emitSelectionChanged(self) """
        pass

    def exportMacro(self): # real signature unknown; restored from __doc__
        """ exportMacro(self) -> str """
        return ""

    def featureChanged(self, Union, QDesignerFormWindowInterface_Feature=None, QDesignerFormWindowInterface_FeatureFlag=None): # real signature unknown; restored from __doc__
        """ featureChanged(self, Union[QDesignerFormWindowInterface.Feature, QDesignerFormWindowInterface.FeatureFlag]) [signal] """
        pass

    def features(self): # real signature unknown; restored from __doc__
        """ features(self) -> QDesignerFormWindowInterface.Feature """
        pass

    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def fileNameChanged(self, p_str): # real signature unknown; restored from __doc__
        """ fileNameChanged(self, str) [signal] """
        pass

    def findFormWindow(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        findFormWindow(QWidget) -> QDesignerFormWindowInterface
        findFormWindow(QObject) -> QDesignerFormWindowInterface
        """
        return QDesignerFormWindowInterface

    def formContainer(self): # real signature unknown; restored from __doc__
        """ formContainer(self) -> QWidget """
        pass

    def geometryChanged(self): # real signature unknown; restored from __doc__
        """ geometryChanged(self) [signal] """
        pass

    def grid(self): # real signature unknown; restored from __doc__
        """ grid(self) -> QPoint """
        pass

    def hasFeature(self, Union, QDesignerFormWindowInterface_Feature=None, QDesignerFormWindowInterface_FeatureFlag=None): # real signature unknown; restored from __doc__
        """ hasFeature(self, Union[QDesignerFormWindowInterface.Feature, QDesignerFormWindowInterface.FeatureFlag]) -> bool """
        return False

    def includeHints(self): # real signature unknown; restored from __doc__
        """ includeHints(self) -> List[str] """
        return []

    def isDirty(self): # real signature unknown; restored from __doc__
        """ isDirty(self) -> bool """
        return False

    def isManaged(self, QWidget): # real signature unknown; restored from __doc__
        """ isManaged(self, QWidget) -> bool """
        return False

    def layoutDefault(self): # real signature unknown; restored from __doc__
        """ layoutDefault(self) -> Tuple[int, int] """
        pass

    def layoutFunction(self): # real signature unknown; restored from __doc__
        """ layoutFunction(self) -> Tuple[str, str] """
        pass

    def mainContainer(self): # real signature unknown; restored from __doc__
        """ mainContainer(self) -> QWidget """
        pass

    def mainContainerChanged(self, QWidget): # real signature unknown; restored from __doc__
        """ mainContainerChanged(self, QWidget) [signal] """
        pass

    def manageWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ manageWidget(self, QWidget) """
        pass

    def objectRemoved(self, QObject): # real signature unknown; restored from __doc__
        """ objectRemoved(self, QObject) [signal] """
        pass

    def pixmapFunction(self): # real signature unknown; restored from __doc__
        """ pixmapFunction(self) -> str """
        return ""

    def removeResourceFile(self, p_str): # real signature unknown; restored from __doc__
        """ removeResourceFile(self, str) """
        pass

    def resourceFiles(self): # real signature unknown; restored from __doc__
        """ resourceFiles(self) -> List[str] """
        return []

    def resourceFilesChanged(self): # real signature unknown; restored from __doc__
        """ resourceFilesChanged(self) [signal] """
        pass

    def selectionChanged(self): # real signature unknown; restored from __doc__
        """ selectionChanged(self) [signal] """
        pass

    def selectWidget(self, QWidget, select=True): # real signature unknown; restored from __doc__
        """ selectWidget(self, QWidget, select: bool = True) """
        pass

    def setAuthor(self, p_str): # real signature unknown; restored from __doc__
        """ setAuthor(self, str) """
        pass

    def setComment(self, p_str): # real signature unknown; restored from __doc__
        """ setComment(self, str) """
        pass

    def setContents(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setContents(self, QIODevice, errorMessage: str = '') -> bool
        setContents(self, str) -> bool
        """
        return False

    def setDirty(self, bool): # real signature unknown; restored from __doc__
        """ setDirty(self, bool) """
        pass

    def setExportMacro(self, p_str): # real signature unknown; restored from __doc__
        """ setExportMacro(self, str) """
        pass

    def setFeatures(self, Union, QDesignerFormWindowInterface_Feature=None, QDesignerFormWindowInterface_FeatureFlag=None): # real signature unknown; restored from __doc__
        """ setFeatures(self, Union[QDesignerFormWindowInterface.Feature, QDesignerFormWindowInterface.FeatureFlag]) """
        pass

    def setFileName(self, p_str): # real signature unknown; restored from __doc__
        """ setFileName(self, str) """
        pass

    def setGrid(self, QPoint): # real signature unknown; restored from __doc__
        """ setGrid(self, QPoint) """
        pass

    def setIncludeHints(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ setIncludeHints(self, Iterable[str]) """
        pass

    def setLayoutDefault(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ setLayoutDefault(self, int, int) """
        pass

    def setLayoutFunction(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ setLayoutFunction(self, str, str) """
        pass

    def setMainContainer(self, QWidget): # real signature unknown; restored from __doc__
        """ setMainContainer(self, QWidget) """
        pass

    def setPixmapFunction(self, p_str): # real signature unknown; restored from __doc__
        """ setPixmapFunction(self, str) """
        pass

    def unmanageWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ unmanageWidget(self, QWidget) """
        pass

    def widgetManaged(self, QWidget): # real signature unknown; restored from __doc__
        """ widgetManaged(self, QWidget) [signal] """
        pass

    def widgetRemoved(self, QWidget): # real signature unknown; restored from __doc__
        """ widgetRemoved(self, QWidget) [signal] """
        pass

    def widgetUnmanaged(self, QWidget): # real signature unknown; restored from __doc__
        """ widgetUnmanaged(self, QWidget) [signal] """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    DefaultFeature = 3
    EditFeature = 1
    GridFeature = 2
    TabOrderFeature = 4


class QDesignerFormWindowManagerInterface(__PyQt5_QtCore.QObject):
    # no doc
    def action(self, QDesignerFormWindowManagerInterface_Action): # real signature unknown; restored from __doc__
        """ action(self, QDesignerFormWindowManagerInterface.Action) -> QAction """
        pass

    def actionFormLayout(self): # real signature unknown; restored from __doc__
        """ actionFormLayout(self) -> QAction """
        pass

    def actionGroup(self, QDesignerFormWindowManagerInterface_ActionGroup): # real signature unknown; restored from __doc__
        """ actionGroup(self, QDesignerFormWindowManagerInterface.ActionGroup) -> QActionGroup """
        pass

    def actionSimplifyLayout(self): # real signature unknown; restored from __doc__
        """ actionSimplifyLayout(self) -> QAction """
        pass

    def activeFormWindow(self): # real signature unknown; restored from __doc__
        """ activeFormWindow(self) -> QDesignerFormWindowInterface """
        return QDesignerFormWindowInterface

    def activeFormWindowChanged(self, QDesignerFormWindowInterface): # real signature unknown; restored from __doc__
        """ activeFormWindowChanged(self, QDesignerFormWindowInterface) [signal] """
        pass

    def addFormWindow(self, QDesignerFormWindowInterface): # real signature unknown; restored from __doc__
        """ addFormWindow(self, QDesignerFormWindowInterface) """
        pass

    def closeAllPreviews(self): # real signature unknown; restored from __doc__
        """ closeAllPreviews(self) """
        pass

    def core(self): # real signature unknown; restored from __doc__
        """ core(self) -> QDesignerFormEditorInterface """
        return QDesignerFormEditorInterface

    def createFormWindow(self, parent=None, flags, Qt_WindowFlags=None, Qt_WindowType=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ createFormWindow(self, parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = 0) -> QDesignerFormWindowInterface """
        pass

    def formWindow(self, p_int): # real signature unknown; restored from __doc__
        """ formWindow(self, int) -> QDesignerFormWindowInterface """
        return QDesignerFormWindowInterface

    def formWindowAdded(self, QDesignerFormWindowInterface): # real signature unknown; restored from __doc__
        """ formWindowAdded(self, QDesignerFormWindowInterface) [signal] """
        pass

    def formWindowCount(self): # real signature unknown; restored from __doc__
        """ formWindowCount(self) -> int """
        return 0

    def formWindowRemoved(self, QDesignerFormWindowInterface): # real signature unknown; restored from __doc__
        """ formWindowRemoved(self, QDesignerFormWindowInterface) [signal] """
        pass

    def formWindowSettingsChanged(self, QDesignerFormWindowInterface): # real signature unknown; restored from __doc__
        """ formWindowSettingsChanged(self, QDesignerFormWindowInterface) [signal] """
        pass

    def removeFormWindow(self, QDesignerFormWindowInterface): # real signature unknown; restored from __doc__
        """ removeFormWindow(self, QDesignerFormWindowInterface) """
        pass

    def setActiveFormWindow(self, QDesignerFormWindowInterface): # real signature unknown; restored from __doc__
        """ setActiveFormWindow(self, QDesignerFormWindowInterface) """
        pass

    def showPluginDialog(self): # real signature unknown; restored from __doc__
        """ showPluginDialog(self) """
        pass

    def showPreview(self): # real signature unknown; restored from __doc__
        """ showPreview(self) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    AdjustSizeAction = 407
    BreakLayoutAction = 406
    CopyAction = 101
    CutAction = 100
    DefaultPreviewAction = 500
    DeleteAction = 103
    FormLayoutAction = 405
    FormWindowSettingsDialogAction = 600
    GridLayoutAction = 404
    HorizontalLayoutAction = 400
    LowerAction = 200
    PasteAction = 102
    RaiseAction = 201
    RedoAction = 301
    SelectAllAction = 104
    SimplifyLayoutAction = 408
    SplitHorizontalAction = 402
    SplitVerticalAction = 403
    StyledPreviewActionGroup = 100
    UndoAction = 300
    VerticalLayoutAction = 401


class QDesignerMemberSheetExtension(__sip.simplewrapper):
    """
    QDesignerMemberSheetExtension()
    QDesignerMemberSheetExtension(QDesignerMemberSheetExtension)
    """
    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def declaredInClass(self, p_int): # real signature unknown; restored from __doc__
        """ declaredInClass(self, int) -> str """
        return ""

    def indexOf(self, p_str): # real signature unknown; restored from __doc__
        """ indexOf(self, str) -> int """
        return 0

    def inheritedFromWidget(self, p_int): # real signature unknown; restored from __doc__
        """ inheritedFromWidget(self, int) -> bool """
        return False

    def isSignal(self, p_int): # real signature unknown; restored from __doc__
        """ isSignal(self, int) -> bool """
        return False

    def isSlot(self, p_int): # real signature unknown; restored from __doc__
        """ isSlot(self, int) -> bool """
        return False

    def isVisible(self, p_int): # real signature unknown; restored from __doc__
        """ isVisible(self, int) -> bool """
        return False

    def memberGroup(self, p_int): # real signature unknown; restored from __doc__
        """ memberGroup(self, int) -> str """
        return ""

    def memberName(self, p_int): # real signature unknown; restored from __doc__
        """ memberName(self, int) -> str """
        return ""

    def parameterNames(self, p_int): # real signature unknown; restored from __doc__
        """ parameterNames(self, int) -> List[QByteArray] """
        return []

    def parameterTypes(self, p_int): # real signature unknown; restored from __doc__
        """ parameterTypes(self, int) -> List[QByteArray] """
        return []

    def setMemberGroup(self, p_int, p_str): # real signature unknown; restored from __doc__
        """ setMemberGroup(self, int, str) """
        pass

    def setVisible(self, p_int, bool): # real signature unknown; restored from __doc__
        """ setVisible(self, int, bool) """
        pass

    def signature(self, p_int): # real signature unknown; restored from __doc__
        """ signature(self, int) -> str """
        return ""

    def __init__(self, QDesignerMemberSheetExtension=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QDesignerObjectInspectorInterface(__PyQt5_QtWidgets.QWidget):
    """ QDesignerObjectInspectorInterface(QWidget, flags: Union[Qt.WindowFlags, Qt.WindowType] = 0) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def core(self): # real signature unknown; restored from __doc__
        """ core(self) -> QDesignerFormEditorInterface """
        return QDesignerFormEditorInterface

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

    def setFormWindow(self, QDesignerFormWindowInterface): # real signature unknown; restored from __doc__
        """ setFormWindow(self, QDesignerFormWindowInterface) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, QWidget, flags, Qt_WindowFlags=None, Qt_WindowType=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


class QDesignerPropertyEditorInterface(__PyQt5_QtWidgets.QWidget):
    """ QDesignerPropertyEditorInterface(QWidget, flags: Union[Qt.WindowFlags, Qt.WindowType] = 0) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def core(self): # real signature unknown; restored from __doc__
        """ core(self) -> QDesignerFormEditorInterface """
        return QDesignerFormEditorInterface

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def currentPropertyName(self): # real signature unknown; restored from __doc__
        """ currentPropertyName(self) -> str """
        return ""

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

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isReadOnly(self): # real signature unknown; restored from __doc__
        """ isReadOnly(self) -> bool """
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

    def object(self): # real signature unknown; restored from __doc__
        """ object(self) -> QObject """
        pass

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def propertyChanged(self, p_str, Any): # real signature unknown; restored from __doc__
        """ propertyChanged(self, str, Any) [signal] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setObject(self, QObject): # real signature unknown; restored from __doc__
        """ setObject(self, QObject) """
        pass

    def setPropertyValue(self, p_str, Any, changed=True): # real signature unknown; restored from __doc__
        """ setPropertyValue(self, str, Any, changed: bool = True) """
        pass

    def setReadOnly(self, bool): # real signature unknown; restored from __doc__
        """ setReadOnly(self, bool) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, QWidget, flags, Qt_WindowFlags=None, Qt_WindowType=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


class QDesignerPropertySheetExtension(__sip.simplewrapper):
    """
    QDesignerPropertySheetExtension()
    QDesignerPropertySheetExtension(QDesignerPropertySheetExtension)
    """
    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def hasReset(self, p_int): # real signature unknown; restored from __doc__
        """ hasReset(self, int) -> bool """
        return False

    def indexOf(self, p_str): # real signature unknown; restored from __doc__
        """ indexOf(self, str) -> int """
        return 0

    def isAttribute(self, p_int): # real signature unknown; restored from __doc__
        """ isAttribute(self, int) -> bool """
        return False

    def isChanged(self, p_int): # real signature unknown; restored from __doc__
        """ isChanged(self, int) -> bool """
        return False

    def isEnabled(self, p_int): # real signature unknown; restored from __doc__
        """ isEnabled(self, int) -> bool """
        return False

    def isVisible(self, p_int): # real signature unknown; restored from __doc__
        """ isVisible(self, int) -> bool """
        return False

    def property(self, p_int): # real signature unknown; restored from __doc__
        """ property(self, int) -> Any """
        pass

    def propertyGroup(self, p_int): # real signature unknown; restored from __doc__
        """ propertyGroup(self, int) -> str """
        return ""

    def propertyName(self, p_int): # real signature unknown; restored from __doc__
        """ propertyName(self, int) -> str """
        return ""

    def reset(self, p_int): # real signature unknown; restored from __doc__
        """ reset(self, int) -> bool """
        return False

    def setAttribute(self, p_int, bool): # real signature unknown; restored from __doc__
        """ setAttribute(self, int, bool) """
        pass

    def setChanged(self, p_int, bool): # real signature unknown; restored from __doc__
        """ setChanged(self, int, bool) """
        pass

    def setProperty(self, p_int, Any): # real signature unknown; restored from __doc__
        """ setProperty(self, int, Any) """
        pass

    def setPropertyGroup(self, p_int, p_str): # real signature unknown; restored from __doc__
        """ setPropertyGroup(self, int, str) """
        pass

    def setVisible(self, p_int, bool): # real signature unknown; restored from __doc__
        """ setVisible(self, int, bool) """
        pass

    def __init__(self, QDesignerPropertySheetExtension=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QDesignerTaskMenuExtension(__sip.simplewrapper):
    """
    QDesignerTaskMenuExtension()
    QDesignerTaskMenuExtension(QDesignerTaskMenuExtension)
    """
    def preferredEditAction(self): # real signature unknown; restored from __doc__
        """ preferredEditAction(self) -> QAction """
        pass

    def taskActions(self): # real signature unknown; restored from __doc__
        """ taskActions(self) -> List[QAction] """
        return []

    def __init__(self, QDesignerTaskMenuExtension=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QDesignerWidgetBoxInterface(__PyQt5_QtWidgets.QWidget):
    # no doc
    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def load(self): # real signature unknown; restored from __doc__
        """ load(self) -> bool """
        return False

    def save(self): # real signature unknown; restored from __doc__
        """ save(self) -> bool """
        return False

    def setFileName(self, p_str): # real signature unknown; restored from __doc__
        """ setFileName(self, str) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QExtensionFactory(__PyQt5_QtCore.QObject, QAbstractExtensionFactory):
    """ QExtensionFactory(parent: QExtensionManager = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createExtension(self, QObject, p_str, QObject_1): # real signature unknown; restored from __doc__
        """ createExtension(self, QObject, str, QObject) -> QObject """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def extension(self, QObject, p_str): # real signature unknown; restored from __doc__
        """ extension(self, QObject, str) -> QObject """
        pass

    def extensionManager(self): # real signature unknown; restored from __doc__
        """ extensionManager(self) -> QExtensionManager """
        return QExtensionManager

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


class QExtensionManager(__PyQt5_QtCore.QObject, QAbstractExtensionManager):
    """ QExtensionManager(parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def extension(self, QObject, p_str): # real signature unknown; restored from __doc__
        """ extension(self, QObject, str) -> QObject """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def registerExtensions(self, QAbstractExtensionFactory, iid=''): # real signature unknown; restored from __doc__
        """ registerExtensions(self, QAbstractExtensionFactory, iid: str = '') """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def unregisterExtensions(self, QAbstractExtensionFactory, iid=''): # real signature unknown; restored from __doc__
        """ unregisterExtensions(self, QAbstractExtensionFactory, iid: str = '') """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


class QFormBuilder(QAbstractFormBuilder):
    """ QFormBuilder() """
    def addPluginPath(self, p_str): # real signature unknown; restored from __doc__
        """ addPluginPath(self, str) """
        pass

    def clearPluginPaths(self): # real signature unknown; restored from __doc__
        """ clearPluginPaths(self) """
        pass

    def customWidgets(self): # real signature unknown; restored from __doc__
        """ customWidgets(self) -> List[QDesignerCustomWidgetInterface] """
        return []

    def pluginPaths(self): # real signature unknown; restored from __doc__
        """ pluginPaths(self) -> List[str] """
        return []

    def setPluginPath(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ setPluginPath(self, Iterable[str]) """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass


class QPyDesignerContainerExtension(__PyQt5_QtCore.QObject, QDesignerContainerExtension):
    """ QPyDesignerContainerExtension(QObject) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, QObject): # real signature unknown; restored from __doc__
        pass


class QPyDesignerCustomWidgetCollectionPlugin(__PyQt5_QtCore.QObject, QDesignerCustomWidgetCollectionInterface):
    """ QPyDesignerCustomWidgetCollectionPlugin(parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


class QPyDesignerCustomWidgetPlugin(__PyQt5_QtCore.QObject, QDesignerCustomWidgetInterface):
    """ QPyDesignerCustomWidgetPlugin(parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


class QPyDesignerMemberSheetExtension(__PyQt5_QtCore.QObject, QDesignerMemberSheetExtension):
    """ QPyDesignerMemberSheetExtension(QObject) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, QObject): # real signature unknown; restored from __doc__
        pass


class QPyDesignerPropertySheetExtension(__PyQt5_QtCore.QObject, QDesignerPropertySheetExtension):
    """ QPyDesignerPropertySheetExtension(QObject) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, QObject): # real signature unknown; restored from __doc__
        pass


class QPyDesignerTaskMenuExtension(__PyQt5_QtCore.QObject, QDesignerTaskMenuExtension):
    """ QPyDesignerTaskMenuExtension(QObject) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, QObject): # real signature unknown; restored from __doc__
        pass


# variables with complex values



