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


from .QSGGeometryNode import QSGGeometryNode

class QSGSimpleTextureNode(QSGGeometryNode):
    """ QSGSimpleTextureNode() """
    def filtering(self): # real signature unknown; restored from __doc__
        """ filtering(self) -> QSGTexture.Filtering """
        pass

    def ownsTexture(self): # real signature unknown; restored from __doc__
        """ ownsTexture(self) -> bool """
        return False

    def rect(self): # real signature unknown; restored from __doc__
        """ rect(self) -> QRectF """
        pass

    def setFiltering(self, QSGTexture_Filtering): # real signature unknown; restored from __doc__
        """ setFiltering(self, QSGTexture.Filtering) """
        pass

    def setOwnsTexture(self, bool): # real signature unknown; restored from __doc__
        """ setOwnsTexture(self, bool) """
        pass

    def setRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setRect(self, QRectF)
        setRect(self, float, float, float, float)
        """
        pass

    def setSourceRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setSourceRect(self, QRectF)
        setSourceRect(self, float, float, float, float)
        """
        pass

    def setTexture(self, QSGTexture): # real signature unknown; restored from __doc__
        """ setTexture(self, QSGTexture) """
        pass

    def setTextureCoordinatesTransform(self, Union, QSGSimpleTextureNode_TextureCoordinatesTransformMode=None, QSGSimpleTextureNode_TextureCoordinatesTransformFlag=None): # real signature unknown; restored from __doc__
        """ setTextureCoordinatesTransform(self, Union[QSGSimpleTextureNode.TextureCoordinatesTransformMode, QSGSimpleTextureNode.TextureCoordinatesTransformFlag]) """
        pass

    def sourceRect(self): # real signature unknown; restored from __doc__
        """ sourceRect(self) -> QRectF """
        pass

    def texture(self): # real signature unknown; restored from __doc__
        """ texture(self) -> QSGTexture """
        return QSGTexture

    def textureCoordinatesTransform(self): # real signature unknown; restored from __doc__
        """ textureCoordinatesTransform(self) -> QSGSimpleTextureNode.TextureCoordinatesTransformMode """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    MirrorHorizontally = 1
    MirrorVertically = 2
    NoTransform = 0


