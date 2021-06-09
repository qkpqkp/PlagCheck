# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QCameraFocusZone(__sip.simplewrapper):
    """ QCameraFocusZone(QCameraFocusZone) """
    def area(self): # real signature unknown; restored from __doc__
        """ area(self) -> QRectF """
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def status(self): # real signature unknown; restored from __doc__
        """ status(self) -> QCameraFocusZone.FocusZoneStatus """
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

    def __init__(self, QCameraFocusZone): # real signature unknown; restored from __doc__
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


    Focused = 3
    Invalid = 0
    Selected = 2
    Unused = 1
    __hash__ = None


