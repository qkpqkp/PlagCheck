# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QVariant(__sip.simplewrapper):
    """
    QVariant()
    QVariant(QVariant.Type)
    QVariant(object)
    QVariant(QVariant)
    """
    def canConvert(self, p_int): # real signature unknown; restored from __doc__
        """ canConvert(self, int) -> bool """
        return False

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def convert(self, p_int): # real signature unknown; restored from __doc__
        """ convert(self, int) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def load(self, QDataStream): # real signature unknown; restored from __doc__
        """ load(self, QDataStream) """
        pass

    def nameToType(self, p_str): # real signature unknown; restored from __doc__
        """ nameToType(str) -> QVariant.Type """
        pass

    def save(self, QDataStream): # real signature unknown; restored from __doc__
        """ save(self, QDataStream) """
        pass

    def swap(self, QVariant): # real signature unknown; restored from __doc__
        """ swap(self, QVariant) """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QVariant.Type """
        pass

    def typeName(self): # real signature unknown; restored from __doc__
        """ typeName(self) -> str """
        return ""

    def typeToName(self, p_int): # real signature unknown; restored from __doc__
        """ typeToName(int) -> str """
        return ""

    def userType(self): # real signature unknown; restored from __doc__
        """ userType(self) -> int """
        return 0

    def value(self): # real signature unknown; restored from __doc__
        """ value(self) -> object """
        return object()

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


    BitArray = 13
    Bitmap = 73
    Bool = 1
    Brush = 66
    ByteArray = 12
    Char = 7
    Color = 67
    Cursor = 74
    Date = 14
    DateTime = 16
    Double = 6
    EasingCurve = 29
    Font = 64
    Hash = 28
    Icon = 69
    Image = 70
    Int = 2
    Invalid = 0
    KeySequence = 75
    Line = 23
    LineF = 24
    List = 9
    Locale = 18
    LongLong = 4
    Map = 8
    Matrix = 79
    Matrix4x4 = 81
    ModelIndex = 42
    Palette = 68
    Pen = 76
    PersistentModelIndex = 50
    Pixmap = 65
    Point = 25
    PointF = 26
    Polygon = 71
    PolygonF = 86
    Quaternion = 85
    Rect = 19
    RectF = 20
    RegExp = 27
    Region = 72
    RegularExpression = 44
    Size = 21
    SizeF = 22
    SizePolicy = 121
    String = 10
    StringList = 11
    TextFormat = 78
    TextLength = 77
    Time = 15
    Transform = 80
    UInt = 3
    ULongLong = 5
    Url = 17
    UserType = 1024
    Uuid = 30
    Vector2D = 82
    Vector3D = 83
    Vector4D = 84
    __hash__ = None


