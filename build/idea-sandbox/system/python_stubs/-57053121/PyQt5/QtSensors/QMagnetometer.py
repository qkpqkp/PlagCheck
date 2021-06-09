# encoding: utf-8
# module PyQt5.QtSensors
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtSensors.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QSensor import QSensor

class QMagnetometer(QSensor):
    """ QMagnetometer(parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def reading(self): # real signature unknown; restored from __doc__
        """ reading(self) -> QMagnetometerReading """
        return QMagnetometerReading

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def returnGeoValues(self): # real signature unknown; restored from __doc__
        """ returnGeoValues(self) -> bool """
        return False

    def returnGeoValuesChanged(self, bool): # real signature unknown; restored from __doc__
        """ returnGeoValuesChanged(self, bool) [signal] """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setReturnGeoValues(self, bool): # real signature unknown; restored from __doc__
        """ setReturnGeoValues(self, bool) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


