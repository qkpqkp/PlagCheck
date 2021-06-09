# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QGraphicsSceneEvent import QGraphicsSceneEvent

class QGraphicsSceneContextMenuEvent(QGraphicsSceneEvent):
    # no doc
    def modifiers(self): # real signature unknown; restored from __doc__
        """ modifiers(self) -> Qt.KeyboardModifiers """
        pass

    def pos(self): # real signature unknown; restored from __doc__
        """ pos(self) -> QPointF """
        pass

    def reason(self): # real signature unknown; restored from __doc__
        """ reason(self) -> QGraphicsSceneContextMenuEvent.Reason """
        pass

    def scenePos(self): # real signature unknown; restored from __doc__
        """ scenePos(self) -> QPointF """
        pass

    def screenPos(self): # real signature unknown; restored from __doc__
        """ screenPos(self) -> QPoint """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    Keyboard = 1
    Mouse = 0
    Other = 2


