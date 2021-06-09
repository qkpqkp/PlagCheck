# encoding: utf-8
# module PyQt5.QtOpenGL
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtOpenGL.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtWidgets as __PyQt5_QtWidgets
import sip as __sip


# no functions
# classes

class QGL(__sip.simplewrapper):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AccumBuffer = 16
    AlphaChannel = 8
    ColorIndex = 262144
    DeprecatedFunctions = 1024
    DepthBuffer = 2
    DirectRendering = 128
    DoubleBuffer = 1
    HasOverlay = 256
    IndirectRendering = 8388608
    NoAccumBuffer = 1048576
    NoAlphaChannel = 524288
    NoDeprecatedFunctions = 67108864
    NoDepthBuffer = 131072
    NoOverlay = 16777216
    NoSampleBuffers = 33554432
    NoStencilBuffer = 2097152
    NoStereoBuffers = 4194304
    Rgba = 4
    SampleBuffers = 512
    SingleBuffer = 65536
    StencilBuffer = 32
    StereoBuffers = 64


class QGLContext(__sip.wrapper):
    """ QGLContext(QGLFormat) """
    def areSharing(self, QGLContext, QGLContext_1): # real signature unknown; restored from __doc__
        """ areSharing(QGLContext, QGLContext) -> bool """
        return False

    def bindTexture(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        bindTexture(self, QImage, target: int = GL_TEXTURE_2D, format: int = GL_RGBA) -> int
        bindTexture(self, QPixmap, target: int = GL_TEXTURE_2D, format: int = GL_RGBA) -> int
        bindTexture(self, str) -> int
        bindTexture(self, QImage, int, int, Union[QGLContext.BindOptions, QGLContext.BindOption]) -> int
        bindTexture(self, QPixmap, int, int, Union[QGLContext.BindOptions, QGLContext.BindOption]) -> int
        """
        return 0

    def chooseContext(self, shareContext=None): # real signature unknown; restored from __doc__
        """ chooseContext(self, shareContext: QGLContext = None) -> bool """
        return False

    def create(self, shareContext=None): # real signature unknown; restored from __doc__
        """ create(self, shareContext: QGLContext = None) -> bool """
        return False

    def currentContext(self): # real signature unknown; restored from __doc__
        """ currentContext() -> QGLContext """
        return QGLContext

    def deleteTexture(self, p_int): # real signature unknown; restored from __doc__
        """ deleteTexture(self, int) """
        pass

    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> QPaintDevice """
        pass

    def deviceIsPixmap(self): # real signature unknown; restored from __doc__
        """ deviceIsPixmap(self) -> bool """
        return False

    def doneCurrent(self): # real signature unknown; restored from __doc__
        """ doneCurrent(self) """
        pass

    def drawTexture(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawTexture(self, QRectF, int, textureTarget: int = GL_TEXTURE_2D)
        drawTexture(self, Union[QPointF, QPoint], int, textureTarget: int = GL_TEXTURE_2D)
        """
        pass

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> QGLFormat """
        return QGLFormat

    def getProcAddress(self, p_str): # real signature unknown; restored from __doc__
        """ getProcAddress(self, str) -> sip.voidptr """
        pass

    def initialized(self): # real signature unknown; restored from __doc__
        """ initialized(self) -> bool """
        return False

    def isSharing(self): # real signature unknown; restored from __doc__
        """ isSharing(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def makeCurrent(self): # real signature unknown; restored from __doc__
        """ makeCurrent(self) """
        pass

    def moveToThread(self, QThread): # real signature unknown; restored from __doc__
        """ moveToThread(self, QThread) """
        pass

    def overlayTransparentColor(self): # real signature unknown; restored from __doc__
        """ overlayTransparentColor(self) -> QColor """
        pass

    def requestedFormat(self): # real signature unknown; restored from __doc__
        """ requestedFormat(self) -> QGLFormat """
        return QGLFormat

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) """
        pass

    def setFormat(self, QGLFormat): # real signature unknown; restored from __doc__
        """ setFormat(self, QGLFormat) """
        pass

    def setInitialized(self, bool): # real signature unknown; restored from __doc__
        """ setInitialized(self, bool) """
        pass

    def setTextureCacheLimit(self, p_int): # real signature unknown; restored from __doc__
        """ setTextureCacheLimit(int) """
        pass

    def setWindowCreated(self, bool): # real signature unknown; restored from __doc__
        """ setWindowCreated(self, bool) """
        pass

    def swapBuffers(self): # real signature unknown; restored from __doc__
        """ swapBuffers(self) """
        pass

    def textureCacheLimit(self): # real signature unknown; restored from __doc__
        """ textureCacheLimit() -> int """
        return 0

    def windowCreated(self): # real signature unknown; restored from __doc__
        """ windowCreated(self) -> bool """
        return False

    def __init__(self, QGLFormat): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    DefaultBindOption = 11
    InvertedYBindOption = 1
    LinearFilteringBindOption = 8
    MipmapBindOption = 2
    NoBindOption = 0
    PremultipliedAlphaBindOption = 4


class QGLFormat(__sip.simplewrapper):
    """
    QGLFormat()
    QGLFormat(Union[QGL.FormatOptions, QGL.FormatOption], plane: int = 0)
    QGLFormat(QGLFormat)
    """
    def accum(self): # real signature unknown; restored from __doc__
        """ accum(self) -> bool """
        return False

    def accumBufferSize(self): # real signature unknown; restored from __doc__
        """ accumBufferSize(self) -> int """
        return 0

    def alpha(self): # real signature unknown; restored from __doc__
        """ alpha(self) -> bool """
        return False

    def alphaBufferSize(self): # real signature unknown; restored from __doc__
        """ alphaBufferSize(self) -> int """
        return 0

    def blueBufferSize(self): # real signature unknown; restored from __doc__
        """ blueBufferSize(self) -> int """
        return 0

    def defaultFormat(self): # real signature unknown; restored from __doc__
        """ defaultFormat() -> QGLFormat """
        return QGLFormat

    def defaultOverlayFormat(self): # real signature unknown; restored from __doc__
        """ defaultOverlayFormat() -> QGLFormat """
        return QGLFormat

    def depth(self): # real signature unknown; restored from __doc__
        """ depth(self) -> bool """
        return False

    def depthBufferSize(self): # real signature unknown; restored from __doc__
        """ depthBufferSize(self) -> int """
        return 0

    def directRendering(self): # real signature unknown; restored from __doc__
        """ directRendering(self) -> bool """
        return False

    def doubleBuffer(self): # real signature unknown; restored from __doc__
        """ doubleBuffer(self) -> bool """
        return False

    def greenBufferSize(self): # real signature unknown; restored from __doc__
        """ greenBufferSize(self) -> int """
        return 0

    def hasOpenGL(self): # real signature unknown; restored from __doc__
        """ hasOpenGL() -> bool """
        return False

    def hasOpenGLOverlays(self): # real signature unknown; restored from __doc__
        """ hasOpenGLOverlays() -> bool """
        return False

    def hasOverlay(self): # real signature unknown; restored from __doc__
        """ hasOverlay(self) -> bool """
        return False

    def majorVersion(self): # real signature unknown; restored from __doc__
        """ majorVersion(self) -> int """
        return 0

    def minorVersion(self): # real signature unknown; restored from __doc__
        """ minorVersion(self) -> int """
        return 0

    def openGLVersionFlags(self): # real signature unknown; restored from __doc__
        """ openGLVersionFlags() -> QGLFormat.OpenGLVersionFlags """
        pass

    def plane(self): # real signature unknown; restored from __doc__
        """ plane(self) -> int """
        return 0

    def profile(self): # real signature unknown; restored from __doc__
        """ profile(self) -> QGLFormat.OpenGLContextProfile """
        pass

    def redBufferSize(self): # real signature unknown; restored from __doc__
        """ redBufferSize(self) -> int """
        return 0

    def rgba(self): # real signature unknown; restored from __doc__
        """ rgba(self) -> bool """
        return False

    def sampleBuffers(self): # real signature unknown; restored from __doc__
        """ sampleBuffers(self) -> bool """
        return False

    def samples(self): # real signature unknown; restored from __doc__
        """ samples(self) -> int """
        return 0

    def setAccum(self, bool): # real signature unknown; restored from __doc__
        """ setAccum(self, bool) """
        pass

    def setAccumBufferSize(self, p_int): # real signature unknown; restored from __doc__
        """ setAccumBufferSize(self, int) """
        pass

    def setAlpha(self, bool): # real signature unknown; restored from __doc__
        """ setAlpha(self, bool) """
        pass

    def setAlphaBufferSize(self, p_int): # real signature unknown; restored from __doc__
        """ setAlphaBufferSize(self, int) """
        pass

    def setBlueBufferSize(self, p_int): # real signature unknown; restored from __doc__
        """ setBlueBufferSize(self, int) """
        pass

    def setDefaultFormat(self, QGLFormat): # real signature unknown; restored from __doc__
        """ setDefaultFormat(QGLFormat) """
        pass

    def setDefaultOverlayFormat(self, QGLFormat): # real signature unknown; restored from __doc__
        """ setDefaultOverlayFormat(QGLFormat) """
        pass

    def setDepth(self, bool): # real signature unknown; restored from __doc__
        """ setDepth(self, bool) """
        pass

    def setDepthBufferSize(self, p_int): # real signature unknown; restored from __doc__
        """ setDepthBufferSize(self, int) """
        pass

    def setDirectRendering(self, bool): # real signature unknown; restored from __doc__
        """ setDirectRendering(self, bool) """
        pass

    def setDoubleBuffer(self, bool): # real signature unknown; restored from __doc__
        """ setDoubleBuffer(self, bool) """
        pass

    def setGreenBufferSize(self, p_int): # real signature unknown; restored from __doc__
        """ setGreenBufferSize(self, int) """
        pass

    def setOption(self, Union, QGL_FormatOptions=None, QGL_FormatOption=None): # real signature unknown; restored from __doc__
        """ setOption(self, Union[QGL.FormatOptions, QGL.FormatOption]) """
        pass

    def setOverlay(self, bool): # real signature unknown; restored from __doc__
        """ setOverlay(self, bool) """
        pass

    def setPlane(self, p_int): # real signature unknown; restored from __doc__
        """ setPlane(self, int) """
        pass

    def setProfile(self, QGLFormat_OpenGLContextProfile): # real signature unknown; restored from __doc__
        """ setProfile(self, QGLFormat.OpenGLContextProfile) """
        pass

    def setRedBufferSize(self, p_int): # real signature unknown; restored from __doc__
        """ setRedBufferSize(self, int) """
        pass

    def setRgba(self, bool): # real signature unknown; restored from __doc__
        """ setRgba(self, bool) """
        pass

    def setSampleBuffers(self, bool): # real signature unknown; restored from __doc__
        """ setSampleBuffers(self, bool) """
        pass

    def setSamples(self, p_int): # real signature unknown; restored from __doc__
        """ setSamples(self, int) """
        pass

    def setStencil(self, bool): # real signature unknown; restored from __doc__
        """ setStencil(self, bool) """
        pass

    def setStencilBufferSize(self, p_int): # real signature unknown; restored from __doc__
        """ setStencilBufferSize(self, int) """
        pass

    def setStereo(self, bool): # real signature unknown; restored from __doc__
        """ setStereo(self, bool) """
        pass

    def setSwapInterval(self, p_int): # real signature unknown; restored from __doc__
        """ setSwapInterval(self, int) """
        pass

    def setVersion(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ setVersion(self, int, int) """
        pass

    def stencil(self): # real signature unknown; restored from __doc__
        """ stencil(self) -> bool """
        return False

    def stencilBufferSize(self): # real signature unknown; restored from __doc__
        """ stencilBufferSize(self) -> int """
        return 0

    def stereo(self): # real signature unknown; restored from __doc__
        """ stereo(self) -> bool """
        return False

    def swapInterval(self): # real signature unknown; restored from __doc__
        """ swapInterval(self) -> int """
        return 0

    def testOption(self, Union, QGL_FormatOptions=None, QGL_FormatOption=None): # real signature unknown; restored from __doc__
        """ testOption(self, Union[QGL.FormatOptions, QGL.FormatOption]) -> bool """
        return False

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    CompatibilityProfile = 2
    CoreProfile = 1
    NoProfile = 0
    OpenGL_ES_CommonLite_Version_1_0 = 256
    OpenGL_ES_CommonLite_Version_1_1 = 1024
    OpenGL_ES_Common_Version_1_0 = 128
    OpenGL_ES_Common_Version_1_1 = 512
    OpenGL_ES_Version_2_0 = 2048
    OpenGL_Version_1_1 = 1
    OpenGL_Version_1_2 = 2
    OpenGL_Version_1_3 = 4
    OpenGL_Version_1_4 = 8
    OpenGL_Version_1_5 = 16
    OpenGL_Version_2_0 = 32
    OpenGL_Version_2_1 = 64
    OpenGL_Version_3_0 = 4096
    OpenGL_Version_3_1 = 8192
    OpenGL_Version_3_2 = 16384
    OpenGL_Version_3_3 = 32768
    OpenGL_Version_4_0 = 65536
    OpenGL_Version_4_1 = 131072
    OpenGL_Version_4_2 = 262144
    OpenGL_Version_4_3 = 524288
    OpenGL_Version_None = 0
    __hash__ = None


class QGLWidget(__PyQt5_QtWidgets.QWidget):
    """
    QGLWidget(parent: QWidget = None, shareWidget: QGLWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags())
    QGLWidget(QGLContext, parent: QWidget = None, shareWidget: QGLWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags())
    QGLWidget(QGLFormat, parent: QWidget = None, shareWidget: QGLWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags())
    """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def autoBufferSwap(self): # real signature unknown; restored from __doc__
        """ autoBufferSwap(self) -> bool """
        return False

    def bindTexture(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        bindTexture(self, QImage, target: int = GL_TEXTURE_2D, format: int = GL_RGBA) -> int
        bindTexture(self, QPixmap, target: int = GL_TEXTURE_2D, format: int = GL_RGBA) -> int
        bindTexture(self, str) -> int
        bindTexture(self, QImage, int, int, Union[QGLContext.BindOptions, QGLContext.BindOption]) -> int
        bindTexture(self, QPixmap, int, int, Union[QGLContext.BindOptions, QGLContext.BindOption]) -> int
        """
        return 0

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def context(self): # real signature unknown; restored from __doc__
        """ context(self) -> QGLContext """
        return QGLContext

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def convertToGLFormat(self, QImage): # real signature unknown; restored from __doc__
        """ convertToGLFormat(QImage) -> QImage """
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def deleteTexture(self, p_int): # real signature unknown; restored from __doc__
        """ deleteTexture(self, int) """
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def doneCurrent(self): # real signature unknown; restored from __doc__
        """ doneCurrent(self) """
        pass

    def doubleBuffer(self): # real signature unknown; restored from __doc__
        """ doubleBuffer(self) -> bool """
        return False

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def drawTexture(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        drawTexture(self, QRectF, int, textureTarget: int = GL_TEXTURE_2D)
        drawTexture(self, Union[QPointF, QPoint], int, textureTarget: int = GL_TEXTURE_2D)
        """
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

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

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> QGLFormat """
        return QGLFormat

    def glDraw(self): # real signature unknown; restored from __doc__
        """ glDraw(self) """
        pass

    def glInit(self): # real signature unknown; restored from __doc__
        """ glInit(self) """
        pass

    def grabFrameBuffer(self, withAlpha=False): # real signature unknown; restored from __doc__
        """ grabFrameBuffer(self, withAlpha: bool = False) -> QImage """
        pass

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def initializeGL(self): # real signature unknown; restored from __doc__
        """ initializeGL(self) """
        pass

    def initializeOverlayGL(self): # real signature unknown; restored from __doc__
        """ initializeOverlayGL(self) """
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isSharing(self): # real signature unknown; restored from __doc__
        """ isSharing(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def makeCurrent(self): # real signature unknown; restored from __doc__
        """ makeCurrent(self) """
        pass

    def makeOverlayCurrent(self): # real signature unknown; restored from __doc__
        """ makeOverlayCurrent(self) """
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

    def overlayContext(self): # real signature unknown; restored from __doc__
        """ overlayContext(self) -> QGLContext """
        return QGLContext

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ paintEngine(self) -> QPaintEngine """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ paintEvent(self, QPaintEvent) """
        pass

    def paintGL(self): # real signature unknown; restored from __doc__
        """ paintGL(self) """
        pass

    def paintOverlayGL(self): # real signature unknown; restored from __doc__
        """ paintOverlayGL(self) """
        pass

    def qglClearColor(self, Union, QColor=None, Qt_GlobalColor=None): # real signature unknown; restored from __doc__
        """ qglClearColor(self, Union[QColor, Qt.GlobalColor]) """
        pass

    def qglColor(self, Union, QColor=None, Qt_GlobalColor=None): # real signature unknown; restored from __doc__
        """ qglColor(self, Union[QColor, Qt.GlobalColor]) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def renderPixmap(self, width=0, height=0, useContext=False): # real signature unknown; restored from __doc__
        """ renderPixmap(self, width: int = 0, height: int = 0, useContext: bool = False) -> QPixmap """
        pass

    def renderText(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        renderText(self, int, int, str, font: QFont = QFont())
        renderText(self, float, float, float, str, font: QFont = QFont())
        """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ resizeEvent(self, QResizeEvent) """
        pass

    def resizeGL(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ resizeGL(self, int, int) """
        pass

    def resizeOverlayGL(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ resizeOverlayGL(self, int, int) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAutoBufferSwap(self, bool): # real signature unknown; restored from __doc__
        """ setAutoBufferSwap(self, bool) """
        pass

    def setContext(self, QGLContext, shareContext=None, deleteOldContext=True): # real signature unknown; restored from __doc__
        """ setContext(self, QGLContext, shareContext: QGLContext = None, deleteOldContext: bool = True) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def swapBuffers(self): # real signature unknown; restored from __doc__
        """ swapBuffers(self) """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateGL(self): # real signature unknown; restored from __doc__
        """ updateGL(self) """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def updateOverlayGL(self): # real signature unknown; restored from __doc__
        """ updateOverlayGL(self) """
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


# variables with complex values



