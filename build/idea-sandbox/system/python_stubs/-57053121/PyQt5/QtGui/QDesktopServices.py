# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QDesktopServices(__sip.simplewrapper):
    """
    QDesktopServices()
    QDesktopServices(QDesktopServices)
    """
    def openUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ openUrl(QUrl) -> bool """
        return False

    def setUrlHandler(self, p_str, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setUrlHandler(str, QObject, str)
        setUrlHandler(str, Callable[[QUrl], None])
        """
        pass

    def unsetUrlHandler(self, p_str): # real signature unknown; restored from __doc__
        """ unsetUrlHandler(str) """
        pass

    def __init__(self, QDesktopServices=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



