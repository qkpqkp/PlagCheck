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


from .QSGNode import QSGNode

class QSGRenderNode(QSGNode):
    # no doc
    def changedStates(self): # real signature unknown; restored from __doc__
        """ changedStates(self) -> QSGRenderNode.StateFlags """
        pass

    def clipList(self): # real signature unknown; restored from __doc__
        """ clipList(self) -> QSGClipNode """
        return QSGClipNode

    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> QSGRenderNode.RenderingFlags """
        pass

    def inheritedOpacity(self): # real signature unknown; restored from __doc__
        """ inheritedOpacity(self) -> float """
        return 0.0

    def matrix(self): # real signature unknown; restored from __doc__
        """ matrix(self) -> QMatrix4x4 """
        pass

    def rect(self): # real signature unknown; restored from __doc__
        """ rect(self) -> QRectF """
        pass

    def releaseResources(self): # real signature unknown; restored from __doc__
        """ releaseResources(self) """
        pass

    def render(self, QSGRenderNode_RenderState): # real signature unknown; restored from __doc__
        """ render(self, QSGRenderNode.RenderState) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    BlendState = 16
    BoundedRectRendering = 1
    ColorState = 8
    CullState = 32
    DepthAwareRendering = 2
    DepthState = 1
    OpaqueRendering = 4
    RenderTargetState = 128
    ScissorState = 4
    StencilState = 2
    ViewportState = 64


