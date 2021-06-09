# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QCameraInfo(__sip.simplewrapper):
    """
    QCameraInfo(name: Union[QByteArray, bytes, bytearray] = QByteArray())
    QCameraInfo(QCamera)
    QCameraInfo(QCameraInfo)
    """
    def availableCameras(self, position=None): # real signature unknown; restored from __doc__
        """ availableCameras(position: QCamera.Position = QCamera.UnspecifiedPosition) -> List[QCameraInfo] """
        return []

    def defaultCamera(self): # real signature unknown; restored from __doc__
        """ defaultCamera() -> QCameraInfo """
        return QCameraInfo

    def description(self): # real signature unknown; restored from __doc__
        """ description(self) -> str """
        return ""

    def deviceName(self): # real signature unknown; restored from __doc__
        """ deviceName(self) -> str """
        return ""

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def orientation(self): # real signature unknown; restored from __doc__
        """ orientation(self) -> int """
        return 0

    def position(self): # real signature unknown; restored from __doc__
        """ position(self) -> QCamera.Position """
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


