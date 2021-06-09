# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QAbstractVideoBuffer(__sip.simplewrapper):
    """ QAbstractVideoBuffer(QAbstractVideoBuffer.HandleType) """
    def handle(self): # real signature unknown; restored from __doc__
        """ handle(self) -> Any """
        pass

    def handleType(self): # real signature unknown; restored from __doc__
        """ handleType(self) -> QAbstractVideoBuffer.HandleType """
        pass

    def map(self, QAbstractVideoBuffer_MapMode): # real signature unknown; restored from __doc__
        """ map(self, QAbstractVideoBuffer.MapMode) -> Tuple[sip.voidptr, int, int] """
        pass

    def mapMode(self): # real signature unknown; restored from __doc__
        """ mapMode(self) -> QAbstractVideoBuffer.MapMode """
        pass

    def release(self): # real signature unknown; restored from __doc__
        """ release(self) """
        pass

    def unmap(self): # real signature unknown; restored from __doc__
        """ unmap(self) """
        pass

    def __init__(self, QAbstractVideoBuffer_HandleType): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    CoreImageHandle = 3
    EGLImageHandle = 5
    GLTextureHandle = 1
    NoHandle = 0
    NotMapped = 0
    QPixmapHandle = 4
    ReadOnly = 1
    ReadWrite = 3
    UserHandle = 1000
    WriteOnly = 2
    XvShmImageHandle = 2


