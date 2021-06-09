# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QGraphicsEffect import QGraphicsEffect

class QGraphicsBlurEffect(QGraphicsEffect):
    """ QGraphicsBlurEffect(parent: QObject = None) """
    def blurHints(self): # real signature unknown; restored from __doc__
        """ blurHints(self) -> QGraphicsBlurEffect.BlurHints """
        pass

    def blurHintsChanged(self, Union, QGraphicsBlurEffect_BlurHints=None, QGraphicsBlurEffect_BlurHint=None): # real signature unknown; restored from __doc__
        """ blurHintsChanged(self, Union[QGraphicsBlurEffect.BlurHints, QGraphicsBlurEffect.BlurHint]) [signal] """
        pass

    def blurRadius(self): # real signature unknown; restored from __doc__
        """ blurRadius(self) -> float """
        return 0.0

    def blurRadiusChanged(self, p_float): # real signature unknown; restored from __doc__
        """ blurRadiusChanged(self, float) [signal] """
        pass

    def boundingRectFor(self, QRectF): # real signature unknown; restored from __doc__
        """ boundingRectFor(self, QRectF) -> QRectF """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def draw(self, QPainter): # real signature unknown; restored from __doc__
        """ draw(self, QPainter) """
        pass

    def drawSource(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setBlurHints(self, Union, QGraphicsBlurEffect_BlurHints=None, QGraphicsBlurEffect_BlurHint=None): # real signature unknown; restored from __doc__
        """ setBlurHints(self, Union[QGraphicsBlurEffect.BlurHints, QGraphicsBlurEffect.BlurHint]) """
        pass

    def setBlurRadius(self, p_float): # real signature unknown; restored from __doc__
        """ setBlurRadius(self, float) """
        pass

    def sourceBoundingRect(self, *args, **kwargs): # real signature unknown
        pass

    def sourceChanged(self, *args, **kwargs): # real signature unknown
        pass

    def sourceIsPixmap(self, *args, **kwargs): # real signature unknown
        pass

    def sourcePixmap(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateBoundingRect(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    AnimationHint = 2
    PerformanceHint = 0
    QualityHint = 1


