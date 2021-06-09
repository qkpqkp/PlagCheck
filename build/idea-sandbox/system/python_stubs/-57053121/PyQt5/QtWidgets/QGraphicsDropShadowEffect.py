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

class QGraphicsDropShadowEffect(QGraphicsEffect):
    """ QGraphicsDropShadowEffect(parent: QObject = None) """
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

    def color(self): # real signature unknown; restored from __doc__
        """ color(self) -> QColor """
        pass

    def colorChanged(self, Union, QColor=None, Qt_GlobalColor=None, QGradient=None): # real signature unknown; restored from __doc__
        """ colorChanged(self, Union[QColor, Qt.GlobalColor, QGradient]) [signal] """
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

    def offset(self): # real signature unknown; restored from __doc__
        """ offset(self) -> QPointF """
        pass

    def offsetChanged(self, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ offsetChanged(self, Union[QPointF, QPoint]) [signal] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setBlurRadius(self, p_float): # real signature unknown; restored from __doc__
        """ setBlurRadius(self, float) """
        pass

    def setColor(self, Union, QColor=None, Qt_GlobalColor=None, QGradient=None): # real signature unknown; restored from __doc__
        """ setColor(self, Union[QColor, Qt.GlobalColor, QGradient]) """
        pass

    def setOffset(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setOffset(self, Union[QPointF, QPoint])
        setOffset(self, float, float)
        setOffset(self, float)
        """
        pass

    def setXOffset(self, p_float): # real signature unknown; restored from __doc__
        """ setXOffset(self, float) """
        pass

    def setYOffset(self, p_float): # real signature unknown; restored from __doc__
        """ setYOffset(self, float) """
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

    def xOffset(self): # real signature unknown; restored from __doc__
        """ xOffset(self) -> float """
        return 0.0

    def yOffset(self): # real signature unknown; restored from __doc__
        """ yOffset(self) -> float """
        return 0.0

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


