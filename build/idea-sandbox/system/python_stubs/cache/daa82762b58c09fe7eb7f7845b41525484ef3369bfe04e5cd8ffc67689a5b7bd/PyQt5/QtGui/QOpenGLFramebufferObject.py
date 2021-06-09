# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QOpenGLFramebufferObject(__sip.simplewrapper):
    """
    QOpenGLFramebufferObject(QSize, target: int = GL_TEXTURE_2D)
    QOpenGLFramebufferObject(int, int, target: int = GL_TEXTURE_2D)
    QOpenGLFramebufferObject(QSize, QOpenGLFramebufferObject.Attachment, target: int = GL_TEXTURE_2D, internal_format: int = GL_RGBA8)
    QOpenGLFramebufferObject(int, int, QOpenGLFramebufferObject.Attachment, target: int = GL_TEXTURE_2D, internal_format: int = GL_RGBA8)
    QOpenGLFramebufferObject(QSize, QOpenGLFramebufferObjectFormat)
    QOpenGLFramebufferObject(int, int, QOpenGLFramebufferObjectFormat)
    """
    def addColorAttachment(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addColorAttachment(self, QSize, internal_format: int = 0)
        addColorAttachment(self, int, int, internal_format: int = 0)
        """
        pass

    def attachment(self): # real signature unknown; restored from __doc__
        """ attachment(self) -> QOpenGLFramebufferObject.Attachment """
        pass

    def bind(self): # real signature unknown; restored from __doc__
        """ bind(self) -> bool """
        return False

    def bindDefault(self): # real signature unknown; restored from __doc__
        """ bindDefault() -> bool """
        return False

    def blitFramebuffer(self, QOpenGLFramebufferObject, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        blitFramebuffer(QOpenGLFramebufferObject, QRect, QOpenGLFramebufferObject, QRect, buffers: int = GL_COLOR_BUFFER_BIT, filter: int = GL_NEAREST)
        blitFramebuffer(QOpenGLFramebufferObject, QOpenGLFramebufferObject, buffers: int = GL_COLOR_BUFFER_BIT, filter: int = GL_NEAREST)
        blitFramebuffer(QOpenGLFramebufferObject, QRect, QOpenGLFramebufferObject, QRect, int, int, int, int)
        blitFramebuffer(QOpenGLFramebufferObject, QRect, QOpenGLFramebufferObject, QRect, int, int, int, int, QOpenGLFramebufferObject.FramebufferRestorePolicy)
        """
        pass

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> QOpenGLFramebufferObjectFormat """
        return QOpenGLFramebufferObjectFormat

    def handle(self): # real signature unknown; restored from __doc__
        """ handle(self) -> int """
        return 0

    def hasOpenGLFramebufferBlit(self): # real signature unknown; restored from __doc__
        """ hasOpenGLFramebufferBlit() -> bool """
        return False

    def hasOpenGLFramebufferObjects(self): # real signature unknown; restored from __doc__
        """ hasOpenGLFramebufferObjects() -> bool """
        return False

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> int """
        return 0

    def isBound(self): # real signature unknown; restored from __doc__
        """ isBound(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def release(self): # real signature unknown; restored from __doc__
        """ release(self) -> bool """
        return False

    def setAttachment(self, QOpenGLFramebufferObject_Attachment): # real signature unknown; restored from __doc__
        """ setAttachment(self, QOpenGLFramebufferObject.Attachment) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> QSize """
        pass

    def sizes(self): # real signature unknown; restored from __doc__
        """ sizes(self) -> List[QSize] """
        return []

    def takeTexture(self, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        takeTexture(self) -> int
        takeTexture(self, int) -> int
        """
        return 0

    def texture(self): # real signature unknown; restored from __doc__
        """ texture(self) -> int """
        return 0

    def textures(self): # real signature unknown; restored from __doc__
        """ textures(self) -> List[int] """
        return []

    def toImage(self, bool=None, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        toImage(self) -> QImage
        toImage(self, bool) -> QImage
        toImage(self, bool, int) -> QImage
        """
        return QImage

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    CombinedDepthStencil = 1
    Depth = 2
    DontRestoreFramebufferBinding = 0
    NoAttachment = 0
    RestoreFrameBufferBinding = 2
    RestoreFramebufferBindingToDefault = 1


