# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QCursor(__sip.simplewrapper):
    """
    QCursor()
    QCursor(QBitmap, QBitmap, hotX: int = -1, hotY: int = -1)
    QCursor(QPixmap, hotX: int = -1, hotY: int = -1)
    QCursor(Union[QCursor, Qt.CursorShape])
    QCursor(Any)
    """
    def bitmap(self): # real signature unknown; restored from __doc__
        """ bitmap(self) -> QBitmap """
        return QBitmap

    def hotSpot(self): # real signature unknown; restored from __doc__
        """ hotSpot(self) -> QPoint """
        pass

    def mask(self): # real signature unknown; restored from __doc__
        """ mask(self) -> QBitmap """
        return QBitmap

    def pixmap(self): # real signature unknown; restored from __doc__
        """ pixmap(self) -> QPixmap """
        return QPixmap

    def pos(self): # real signature unknown; restored from __doc__
        """ pos() -> QPoint """
        pass

    def setPos(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setPos(int, int)
        setPos(QPoint)
        """
        pass

    def setShape(self, Qt_CursorShape): # real signature unknown; restored from __doc__
        """ setShape(self, Qt.CursorShape) """
        pass

    def shape(self): # real signature unknown; restored from __doc__
        """ shape(self) -> Qt.CursorShape """
        pass

    def swap(self, Union, QCursor=None, Qt_CursorShape=None): # real signature unknown; restored from __doc__
        """ swap(self, Union[QCursor, Qt.CursorShape]) """
        pass

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


    __hash__ = None


