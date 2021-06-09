# encoding: utf-8
# module PyQt5.QtSensors
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtSensors.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QSensorReading import QSensorReading

class QOrientationReading(QSensorReading):
    # no doc
    def orientation(self): # real signature unknown; restored from __doc__
        """ orientation(self) -> QOrientationReading.Orientation """
        pass

    def setOrientation(self, QOrientationReading_Orientation): # real signature unknown; restored from __doc__
        """ setOrientation(self, QOrientationReading.Orientation) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    FaceDown = 6
    FaceUp = 5
    LeftUp = 3
    RightUp = 4
    TopDown = 2
    TopUp = 1
    Undefined = 0


