# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QPaintDevice import QPaintDevice

class QPicture(QPaintDevice):
    """
    QPicture(formatVersion: int = -1)
    QPicture(QPicture)
    """
    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> QRect """
        pass

    def data(self): # real signature unknown; restored from __doc__
        """ data(self) -> str """
        return ""

    def detach(self): # real signature unknown; restored from __doc__
        """ detach(self) """
        pass

    def devType(self): # real signature unknown; restored from __doc__
        """ devType(self) -> int """
        return 0

    def isDetached(self): # real signature unknown; restored from __doc__
        """ isDetached(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def load(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        load(self, QIODevice, format: str = None) -> bool
        load(self, str, format: str = None) -> bool
        """
        return False

    def metric(self, QPaintDevice_PaintDeviceMetric): # real signature unknown; restored from __doc__
        """ metric(self, QPaintDevice.PaintDeviceMetric) -> int """
        return 0

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ paintEngine(self) -> QPaintEngine """
        return QPaintEngine

    def play(self, QPainter): # real signature unknown; restored from __doc__
        """ play(self, QPainter) -> bool """
        return False

    def save(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        save(self, QIODevice, format: str = None) -> bool
        save(self, str, format: str = None) -> bool
        """
        return False

    def setBoundingRect(self, QRect): # real signature unknown; restored from __doc__
        """ setBoundingRect(self, QRect) """
        pass

    def setData(self, bytes): # real signature unknown; restored from __doc__
        """ setData(self, bytes) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def swap(self, QPicture): # real signature unknown; restored from __doc__
        """ swap(self, QPicture) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


