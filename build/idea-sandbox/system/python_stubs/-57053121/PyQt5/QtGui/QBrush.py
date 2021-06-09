# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QBrush(__sip.simplewrapper):
    """
    QBrush()
    QBrush(Qt.BrushStyle)
    QBrush(Union[QColor, Qt.GlobalColor, QGradient], style: Qt.BrushStyle = Qt.SolidPattern)
    QBrush(Union[QColor, Qt.GlobalColor, QGradient], QPixmap)
    QBrush(QPixmap)
    QBrush(QImage)
    QBrush(Union[QBrush, QColor, Qt.GlobalColor, QGradient])
    QBrush(Any)
    """
    def color(self): # real signature unknown; restored from __doc__
        """ color(self) -> QColor """
        return QColor

    def gradient(self): # real signature unknown; restored from __doc__
        """ gradient(self) -> QGradient """
        return QGradient

    def isOpaque(self): # real signature unknown; restored from __doc__
        """ isOpaque(self) -> bool """
        return False

    def setColor(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setColor(self, Union[QColor, Qt.GlobalColor, QGradient])
        setColor(self, Qt.GlobalColor)
        """
        pass

    def setStyle(self, Qt_BrushStyle): # real signature unknown; restored from __doc__
        """ setStyle(self, Qt.BrushStyle) """
        pass

    def setTexture(self, QPixmap): # real signature unknown; restored from __doc__
        """ setTexture(self, QPixmap) """
        pass

    def setTextureImage(self, QImage): # real signature unknown; restored from __doc__
        """ setTextureImage(self, QImage) """
        pass

    def setTransform(self, QTransform): # real signature unknown; restored from __doc__
        """ setTransform(self, QTransform) """
        pass

    def style(self): # real signature unknown; restored from __doc__
        """ style(self) -> Qt.BrushStyle """
        pass

    def swap(self, QBrush): # real signature unknown; restored from __doc__
        """ swap(self, QBrush) """
        pass

    def texture(self): # real signature unknown; restored from __doc__
        """ texture(self) -> QPixmap """
        return QPixmap

    def textureImage(self): # real signature unknown; restored from __doc__
        """ textureImage(self) -> QImage """
        return QImage

    def transform(self): # real signature unknown; restored from __doc__
        """ transform(self) -> QTransform """
        return QTransform

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


