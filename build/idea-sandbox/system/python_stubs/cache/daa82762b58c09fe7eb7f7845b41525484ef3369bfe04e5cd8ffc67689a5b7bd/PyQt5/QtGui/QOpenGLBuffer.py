# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QOpenGLBuffer(__sip.simplewrapper):
    """
    QOpenGLBuffer()
    QOpenGLBuffer(QOpenGLBuffer.Type)
    QOpenGLBuffer(QOpenGLBuffer)
    """
    def allocate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        allocate(self, sip.voidptr, int)
        allocate(self, int)
        """
        pass

    def bind(self): # real signature unknown; restored from __doc__
        """ bind(self) -> bool """
        return False

    def bufferId(self): # real signature unknown; restored from __doc__
        """ bufferId(self) -> int """
        return 0

    def create(self): # real signature unknown; restored from __doc__
        """ create(self) -> bool """
        return False

    def destroy(self): # real signature unknown; restored from __doc__
        """ destroy(self) """
        pass

    def isCreated(self): # real signature unknown; restored from __doc__
        """ isCreated(self) -> bool """
        return False

    def map(self, QOpenGLBuffer_Access): # real signature unknown; restored from __doc__
        """ map(self, QOpenGLBuffer.Access) -> sip.voidptr """
        pass

    def mapRange(self, p_int, p_int_1, Union, QOpenGLBuffer_RangeAccessFlags=None, QOpenGLBuffer_RangeAccessFlag=None): # real signature unknown; restored from __doc__
        """ mapRange(self, int, int, Union[QOpenGLBuffer.RangeAccessFlags, QOpenGLBuffer.RangeAccessFlag]) -> sip.voidptr """
        pass

    def read(self, p_int, sip_voidptr, p_int_1): # real signature unknown; restored from __doc__
        """ read(self, int, sip.voidptr, int) -> bool """
        return False

    def release(self, QOpenGLBuffer_Type=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        release(self)
        release(QOpenGLBuffer.Type)
        """
        pass

    def setUsagePattern(self, QOpenGLBuffer_UsagePattern): # real signature unknown; restored from __doc__
        """ setUsagePattern(self, QOpenGLBuffer.UsagePattern) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QOpenGLBuffer.Type """
        pass

    def unmap(self): # real signature unknown; restored from __doc__
        """ unmap(self) -> bool """
        return False

    def usagePattern(self): # real signature unknown; restored from __doc__
        """ usagePattern(self) -> QOpenGLBuffer.UsagePattern """
        pass

    def write(self, p_int, sip_voidptr, p_int_1): # real signature unknown; restored from __doc__
        """ write(self, int, sip.voidptr, int) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    DynamicCopy = 35050
    DynamicDraw = 35048
    DynamicRead = 35049
    IndexBuffer = 34963
    PixelPackBuffer = 35051
    PixelUnpackBuffer = 35052
    RangeFlushExplicit = 16
    RangeInvalidate = 4
    RangeInvalidateBuffer = 8
    RangeRead = 1
    RangeUnsynchronized = 32
    RangeWrite = 2
    ReadOnly = 35000
    ReadWrite = 35002
    StaticCopy = 35046
    StaticDraw = 35044
    StaticRead = 35045
    StreamCopy = 35042
    StreamDraw = 35040
    StreamRead = 35041
    VertexBuffer = 34962
    WriteOnly = 35001


