# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QPixmap import QPixmap

class QBitmap(QPixmap):
    """
    QBitmap()
    QBitmap(QBitmap)
    QBitmap(QPixmap)
    QBitmap(int, int)
    QBitmap(QSize)
    QBitmap(str, format: str = None)
    QBitmap(Any)
    """
    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def fromData(self, QSize, bytes, format=None): # real signature unknown; restored from __doc__
        """ fromData(QSize, bytes, format: QImage.Format = QImage.Format_MonoLSB) -> QBitmap """
        return QBitmap

    def fromImage(self, QImage, flags, Qt_ImageConversionFlags=None, Qt_ImageConversionFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ fromImage(QImage, flags: Union[Qt.ImageConversionFlags, Qt.ImageConversionFlag] = Qt.AutoColor) -> QBitmap """
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def swap(self, QBitmap): # real signature unknown; restored from __doc__
        """ swap(self, QBitmap) """
        pass

    def transformed(self, QTransform): # real signature unknown; restored from __doc__
        """ transformed(self, QTransform) -> QBitmap """
        return QBitmap

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


