# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QOpenGLTextureBlitter(__sip.simplewrapper):
    """ QOpenGLTextureBlitter() """
    def bind(self, target=None): # real signature unknown; restored from __doc__
        """ bind(self, target: int = GL_TEXTURE_2D) """
        pass

    def blit(self, p_int, QMatrix4x4, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        blit(self, int, QMatrix4x4, QOpenGLTextureBlitter.Origin)
        blit(self, int, QMatrix4x4, QMatrix3x3)
        """
        pass

    def create(self): # real signature unknown; restored from __doc__
        """ create(self) -> bool """
        return False

    def destroy(self): # real signature unknown; restored from __doc__
        """ destroy(self) """
        pass

    def isCreated(self): # real signature unknown; restored from __doc__
        """ isCreated(self) -> bool """
        return False

    def release(self): # real signature unknown; restored from __doc__
        """ release(self) """
        pass

    def setOpacity(self, p_float): # real signature unknown; restored from __doc__
        """ setOpacity(self, float) """
        pass

    def setRedBlueSwizzle(self, bool): # real signature unknown; restored from __doc__
        """ setRedBlueSwizzle(self, bool) """
        pass

    def sourceTransform(self, QRectF, QSize, QOpenGLTextureBlitter_Origin): # real signature unknown; restored from __doc__
        """ sourceTransform(QRectF, QSize, QOpenGLTextureBlitter.Origin) -> QMatrix3x3 """
        return QMatrix3x3

    def supportsExternalOESTarget(self): # real signature unknown; restored from __doc__
        """ supportsExternalOESTarget(self) -> bool """
        return False

    def targetTransform(self, QRectF, QRect): # real signature unknown; restored from __doc__
        """ targetTransform(QRectF, QRect) -> QMatrix4x4 """
        return QMatrix4x4

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    OriginBottomLeft = 0
    OriginTopLeft = 1


