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


class QSGAbstractRenderer(__PyQt5_QtCore.QObject):
    # no doc
    def clearColor(self): # real signature unknown; restored from __doc__
        """ clearColor(self) -> QColor """
        pass

    def clearMode(self): # real signature unknown; restored from __doc__
        """ clearMode(self) -> QSGAbstractRenderer.ClearMode """
        pass

    def deviceRect(self): # real signature unknown; restored from __doc__
        """ deviceRect(self) -> QRect """
        pass

    def projectionMatrix(self): # real signature unknown; restored from __doc__
        """ projectionMatrix(self) -> QMatrix4x4 """
        pass

    def renderScene(self, fboId=0): # real signature unknown; restored from __doc__
        """ renderScene(self, fboId: int = 0) """
        pass

    def sceneGraphChanged(self): # real signature unknown; restored from __doc__
        """ sceneGraphChanged(self) [signal] """
        pass

    def setClearColor(self, Union, QColor=None, Qt_GlobalColor=None): # real signature unknown; restored from __doc__
        """ setClearColor(self, Union[QColor, Qt.GlobalColor]) """
        pass

    def setClearMode(self, Union, QSGAbstractRenderer_ClearMode=None, QSGAbstractRenderer_ClearModeBit=None): # real signature unknown; restored from __doc__
        """ setClearMode(self, Union[QSGAbstractRenderer.ClearMode, QSGAbstractRenderer.ClearModeBit]) """
        pass

    def setDeviceRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setDeviceRect(self, QRect)
        setDeviceRect(self, QSize)
        """
        pass

    def setProjectionMatrix(self, QMatrix4x4): # real signature unknown; restored from __doc__
        """ setProjectionMatrix(self, QMatrix4x4) """
        pass

    def setProjectionMatrixToRect(self, QRectF): # real signature unknown; restored from __doc__
        """ setProjectionMatrixToRect(self, QRectF) """
        pass

    def setViewportRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setViewportRect(self, QRect)
        setViewportRect(self, QSize)
        """
        pass

    def viewportRect(self): # real signature unknown; restored from __doc__
        """ viewportRect(self) -> QRect """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    ClearColorBuffer = 1
    ClearDepthBuffer = 2
    ClearStencilBuffer = 4


