# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QScroller(__PyQt5_QtCore.QObject):
    # no doc
    def activeScrollers(self): # real signature unknown; restored from __doc__
        """ activeScrollers() -> List[QScroller] """
        return []

    def ensureVisible(self, QRectF, p_float, p_float_1, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        ensureVisible(self, QRectF, float, float)
        ensureVisible(self, QRectF, float, float, int)
        """
        pass

    def finalPosition(self): # real signature unknown; restored from __doc__
        """ finalPosition(self) -> QPointF """
        pass

    def grabbedGesture(self, QObject): # real signature unknown; restored from __doc__
        """ grabbedGesture(QObject) -> Qt.GestureType """
        pass

    def grabGesture(self, QObject, scrollGestureType=None): # real signature unknown; restored from __doc__
        """ grabGesture(QObject, scrollGestureType: QScroller.ScrollerGestureType = QScroller.TouchGesture) -> Qt.GestureType """
        pass

    def handleInput(self, QScroller_Input, Union, QPointF=None, QPoint=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ handleInput(self, QScroller.Input, Union[QPointF, QPoint], timestamp: int = 0) -> bool """
        pass

    def hasScroller(self, QObject): # real signature unknown; restored from __doc__
        """ hasScroller(QObject) -> bool """
        return False

    def pixelPerMeter(self): # real signature unknown; restored from __doc__
        """ pixelPerMeter(self) -> QPointF """
        pass

    def resendPrepareEvent(self): # real signature unknown; restored from __doc__
        """ resendPrepareEvent(self) """
        pass

    def scroller(self, QObject): # real signature unknown; restored from __doc__
        """ scroller(QObject) -> QScroller """
        return QScroller

    def scrollerProperties(self): # real signature unknown; restored from __doc__
        """ scrollerProperties(self) -> QScrollerProperties """
        return QScrollerProperties

    def scrollerPropertiesChanged(self, QScrollerProperties): # real signature unknown; restored from __doc__
        """ scrollerPropertiesChanged(self, QScrollerProperties) [signal] """
        pass

    def scrollTo(self, Union, QPointF=None, QPoint=None, *args=None, **kwargs=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        scrollTo(self, Union[QPointF, QPoint])
        scrollTo(self, Union[QPointF, QPoint], int)
        """
        pass

    def setScrollerProperties(self, QScrollerProperties): # real signature unknown; restored from __doc__
        """ setScrollerProperties(self, QScrollerProperties) """
        pass

    def setSnapPositionsX(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setSnapPositionsX(self, Iterable[float])
        setSnapPositionsX(self, float, float)
        """
        pass

    def setSnapPositionsY(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setSnapPositionsY(self, Iterable[float])
        setSnapPositionsY(self, float, float)
        """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QScroller.State """
        pass

    def stateChanged(self, QScroller_State): # real signature unknown; restored from __doc__
        """ stateChanged(self, QScroller.State) [signal] """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) """
        pass

    def target(self): # real signature unknown; restored from __doc__
        """ target(self) -> QObject """
        pass

    def ungrabGesture(self, QObject): # real signature unknown; restored from __doc__
        """ ungrabGesture(QObject) """
        pass

    def velocity(self): # real signature unknown; restored from __doc__
        """ velocity(self) -> QPointF """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    Dragging = 2
    Inactive = 0
    InputMove = 2
    InputPress = 1
    InputRelease = 3
    LeftMouseButtonGesture = 1
    MiddleMouseButtonGesture = 3
    Pressed = 1
    RightMouseButtonGesture = 2
    Scrolling = 3
    TouchGesture = 0


