# encoding: utf-8
# module PyQt5.QtQuick
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtQuick.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import PyQt5.QtQml as __PyQt5_QtQml
import sip as __sip


class QQuickWindow(__PyQt5_QtGui.QWindow):
    """ QQuickWindow(parent: QWindow = None) """
    def activeFocusItem(self): # real signature unknown; restored from __doc__
        """ activeFocusItem(self) -> QQuickItem """
        return QQuickItem

    def activeFocusItemChanged(self): # real signature unknown; restored from __doc__
        """ activeFocusItemChanged(self) [signal] """
        pass

    def afterAnimating(self): # real signature unknown; restored from __doc__
        """ afterAnimating(self) [signal] """
        pass

    def afterRendering(self): # real signature unknown; restored from __doc__
        """ afterRendering(self) [signal] """
        pass

    def afterSynchronizing(self): # real signature unknown; restored from __doc__
        """ afterSynchronizing(self) [signal] """
        pass

    def beforeRendering(self): # real signature unknown; restored from __doc__
        """ beforeRendering(self) [signal] """
        pass

    def beforeSynchronizing(self): # real signature unknown; restored from __doc__
        """ beforeSynchronizing(self) [signal] """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clearBeforeRendering(self): # real signature unknown; restored from __doc__
        """ clearBeforeRendering(self) -> bool """
        return False

    def closing(self, QQuickCloseEvent): # real signature unknown; restored from __doc__
        """ closing(self, QQuickCloseEvent) [signal] """
        pass

    def color(self): # real signature unknown; restored from __doc__
        """ color(self) -> QColor """
        pass

    def colorChanged(self, Union, QColor=None, Qt_GlobalColor=None): # real signature unknown; restored from __doc__
        """ colorChanged(self, Union[QColor, Qt.GlobalColor]) [signal] """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contentItem(self): # real signature unknown; restored from __doc__
        """ contentItem(self) -> QQuickItem """
        return QQuickItem

    def createImageNode(self): # real signature unknown; restored from __doc__
        """ createImageNode(self) -> QSGImageNode """
        return QSGImageNode

    def createRectangleNode(self): # real signature unknown; restored from __doc__
        """ createRectangleNode(self) -> QSGRectangleNode """
        return QSGRectangleNode

    def createTextureFromId(self, p_int, QSize, options, QQuickWindow_CreateTextureOptions=None, QQuickWindow_CreateTextureOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ createTextureFromId(self, int, QSize, options: Union[QQuickWindow.CreateTextureOptions, QQuickWindow.CreateTextureOption] = QQuickWindow.CreateTextureOption()) -> QSGTexture """
        pass

    def createTextureFromImage(self, QImage, Union=None, QQuickWindow_CreateTextureOptions=None, QQuickWindow_CreateTextureOption=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        createTextureFromImage(self, QImage) -> QSGTexture
        createTextureFromImage(self, QImage, Union[QQuickWindow.CreateTextureOptions, QQuickWindow.CreateTextureOption]) -> QSGTexture
        """
        return QSGTexture

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def effectiveDevicePixelRatio(self): # real signature unknown; restored from __doc__
        """ effectiveDevicePixelRatio(self) -> float """
        return 0.0

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def exposeEvent(self, QExposeEvent): # real signature unknown; restored from __doc__
        """ exposeEvent(self, QExposeEvent) """
        pass

    def focusInEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ focusInEvent(self, QFocusEvent) """
        pass

    def focusObject(self): # real signature unknown; restored from __doc__
        """ focusObject(self) -> QObject """
        pass

    def focusOutEvent(self, QFocusEvent): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, QFocusEvent) """
        pass

    def frameSwapped(self): # real signature unknown; restored from __doc__
        """ frameSwapped(self) [signal] """
        pass

    def grabWindow(self): # real signature unknown; restored from __doc__
        """ grabWindow(self) -> QImage """
        pass

    def hasDefaultAlphaBuffer(self): # real signature unknown; restored from __doc__
        """ hasDefaultAlphaBuffer() -> bool """
        return False

    def hideEvent(self, QHideEvent): # real signature unknown; restored from __doc__
        """ hideEvent(self, QHideEvent) """
        pass

    def incubationController(self): # real signature unknown; restored from __doc__
        """ incubationController(self) -> QQmlIncubationController """
        pass

    def isPersistentOpenGLContext(self): # real signature unknown; restored from __doc__
        """ isPersistentOpenGLContext(self) -> bool """
        return False

    def isPersistentSceneGraph(self): # real signature unknown; restored from __doc__
        """ isPersistentSceneGraph(self) -> bool """
        return False

    def isSceneGraphInitialized(self): # real signature unknown; restored from __doc__
        """ isSceneGraphInitialized(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, QKeyEvent) """
        pass

    def keyReleaseEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, QKeyEvent) """
        pass

    def mouseDoubleClickEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mouseDoubleClickEvent(self, QMouseEvent) """
        pass

    def mouseGrabberItem(self): # real signature unknown; restored from __doc__
        """ mouseGrabberItem(self) -> QQuickItem """
        return QQuickItem

    def mouseMoveEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mouseMoveEvent(self, QMouseEvent) """
        pass

    def mousePressEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, QMouseEvent) """
        pass

    def mouseReleaseEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, QMouseEvent) """
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def openglContext(self): # real signature unknown; restored from __doc__
        """ openglContext(self) -> QOpenGLContext """
        pass

    def openglContextCreated(self, QOpenGLContext): # real signature unknown; restored from __doc__
        """ openglContextCreated(self, QOpenGLContext) [signal] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def releaseResources(self): # real signature unknown; restored from __doc__
        """ releaseResources(self) """
        pass

    def rendererInterface(self): # real signature unknown; restored from __doc__
        """ rendererInterface(self) -> QSGRendererInterface """
        return QSGRendererInterface

    def renderTarget(self): # real signature unknown; restored from __doc__
        """ renderTarget(self) -> QOpenGLFramebufferObject """
        pass

    def renderTargetId(self): # real signature unknown; restored from __doc__
        """ renderTargetId(self) -> int """
        return 0

    def renderTargetSize(self): # real signature unknown; restored from __doc__
        """ renderTargetSize(self) -> QSize """
        pass

    def resetOpenGLState(self): # real signature unknown; restored from __doc__
        """ resetOpenGLState(self) """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ resizeEvent(self, QResizeEvent) """
        pass

    def sceneGraphAboutToStop(self): # real signature unknown; restored from __doc__
        """ sceneGraphAboutToStop(self) [signal] """
        pass

    def sceneGraphBackend(self): # real signature unknown; restored from __doc__
        """ sceneGraphBackend() -> str """
        return ""

    def sceneGraphError(self, QQuickWindow_SceneGraphError, p_str): # real signature unknown; restored from __doc__
        """ sceneGraphError(self, QQuickWindow.SceneGraphError, str) [signal] """
        pass

    def sceneGraphInitialized(self): # real signature unknown; restored from __doc__
        """ sceneGraphInitialized(self) [signal] """
        pass

    def sceneGraphInvalidated(self): # real signature unknown; restored from __doc__
        """ sceneGraphInvalidated(self) [signal] """
        pass

    def scheduleRenderJob(self, QRunnable, QQuickWindow_RenderStage): # real signature unknown; restored from __doc__
        """ scheduleRenderJob(self, QRunnable, QQuickWindow.RenderStage) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def sendEvent(self, QQuickItem, QEvent): # real signature unknown; restored from __doc__
        """ sendEvent(self, QQuickItem, QEvent) -> bool """
        return False

    def setClearBeforeRendering(self, bool): # real signature unknown; restored from __doc__
        """ setClearBeforeRendering(self, bool) """
        pass

    def setColor(self, Union, QColor=None, Qt_GlobalColor=None): # real signature unknown; restored from __doc__
        """ setColor(self, Union[QColor, Qt.GlobalColor]) """
        pass

    def setDefaultAlphaBuffer(self, bool): # real signature unknown; restored from __doc__
        """ setDefaultAlphaBuffer(bool) """
        pass

    def setPersistentOpenGLContext(self, bool): # real signature unknown; restored from __doc__
        """ setPersistentOpenGLContext(self, bool) """
        pass

    def setPersistentSceneGraph(self, bool): # real signature unknown; restored from __doc__
        """ setPersistentSceneGraph(self, bool) """
        pass

    def setRenderTarget(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setRenderTarget(self, QOpenGLFramebufferObject)
        setRenderTarget(self, int, QSize)
        """
        pass

    def setSceneGraphBackend(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setSceneGraphBackend(QSGRendererInterface.GraphicsApi)
        setSceneGraphBackend(str)
        """
        pass

    def setTextRenderType(self, QQuickWindow_TextRenderType): # real signature unknown; restored from __doc__
        """ setTextRenderType(QQuickWindow.TextRenderType) """
        pass

    def showEvent(self, QShowEvent): # real signature unknown; restored from __doc__
        """ showEvent(self, QShowEvent) """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def textRenderType(self): # real signature unknown; restored from __doc__
        """ textRenderType() -> QQuickWindow.TextRenderType """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def touchEvent(self, *args, **kwargs): # real signature unknown
        pass

    def update(self): # real signature unknown; restored from __doc__
        """ update(self) """
        pass

    def wheelEvent(self, QWheelEvent): # real signature unknown; restored from __doc__
        """ wheelEvent(self, QWheelEvent) """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    AfterRenderingStage = 3
    AfterSwapStage = 4
    AfterSynchronizingStage = 1
    BeforeRenderingStage = 2
    BeforeSynchronizingStage = 0
    ContextNotAvailable = 1
    NativeTextRendering = 1
    NoStage = 5
    QtTextRendering = 0
    TextureCanUseAtlas = 8
    TextureHasAlphaChannel = 1
    TextureHasMipmaps = 2
    TextureIsOpaque = 16
    TextureOwnsGLTexture = 4


