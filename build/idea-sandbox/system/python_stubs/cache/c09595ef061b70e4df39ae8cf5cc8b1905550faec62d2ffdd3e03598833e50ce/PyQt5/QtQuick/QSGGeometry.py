# encoding: utf-8
# module PyQt5.QtQuick
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtQuick.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import PyQt5.QtQml as __PyQt5_QtQml
import sip as __sip


class QSGGeometry(__sip.wrapper):
    """
    QSGGeometry(QSGGeometry.AttributeSet, int, indexCount: int = 0, indexType: int = GL_UNSIGNED_SHORT)
    QSGGeometry(QSGGeometry)
    """
    def allocate(self, p_int, indexCount=0): # real signature unknown; restored from __doc__
        """ allocate(self, int, indexCount: int = 0) """
        pass

    def attributeCount(self): # real signature unknown; restored from __doc__
        """ attributeCount(self) -> int """
        return 0

    def attributes(self): # real signature unknown; restored from __doc__
        """ attributes(self) -> sip.array[QSGGeometry.Attribute] """
        pass

    def defaultAttributes_ColoredPoint2D(self): # real signature unknown; restored from __doc__
        """ defaultAttributes_ColoredPoint2D() -> QSGGeometry.AttributeSet """
        pass

    def defaultAttributes_Point2D(self): # real signature unknown; restored from __doc__
        """ defaultAttributes_Point2D() -> QSGGeometry.AttributeSet """
        pass

    def defaultAttributes_TexturedPoint2D(self): # real signature unknown; restored from __doc__
        """ defaultAttributes_TexturedPoint2D() -> QSGGeometry.AttributeSet """
        pass

    def drawingMode(self): # real signature unknown; restored from __doc__
        """ drawingMode(self) -> int """
        return 0

    def indexCount(self): # real signature unknown; restored from __doc__
        """ indexCount(self) -> int """
        return 0

    def indexData(self): # real signature unknown; restored from __doc__
        """ indexData(self) -> sip.voidptr """
        pass

    def indexDataAsUInt(self): # real signature unknown; restored from __doc__
        """ indexDataAsUInt(self) -> sip.array[int] """
        pass

    def indexDataAsUShort(self): # real signature unknown; restored from __doc__
        """ indexDataAsUShort(self) -> sip.array[int] """
        pass

    def indexDataPattern(self): # real signature unknown; restored from __doc__
        """ indexDataPattern(self) -> QSGGeometry.DataPattern """
        pass

    def indexType(self): # real signature unknown; restored from __doc__
        """ indexType(self) -> int """
        return 0

    def lineWidth(self): # real signature unknown; restored from __doc__
        """ lineWidth(self) -> float """
        return 0.0

    def markIndexDataDirty(self): # real signature unknown; restored from __doc__
        """ markIndexDataDirty(self) """
        pass

    def markVertexDataDirty(self): # real signature unknown; restored from __doc__
        """ markVertexDataDirty(self) """
        pass

    def setDrawingMode(self, p_int): # real signature unknown; restored from __doc__
        """ setDrawingMode(self, int) """
        pass

    def setIndexDataPattern(self, QSGGeometry_DataPattern): # real signature unknown; restored from __doc__
        """ setIndexDataPattern(self, QSGGeometry.DataPattern) """
        pass

    def setLineWidth(self, p_float): # real signature unknown; restored from __doc__
        """ setLineWidth(self, float) """
        pass

    def setVertexDataPattern(self, QSGGeometry_DataPattern): # real signature unknown; restored from __doc__
        """ setVertexDataPattern(self, QSGGeometry.DataPattern) """
        pass

    def sizeOfIndex(self): # real signature unknown; restored from __doc__
        """ sizeOfIndex(self) -> int """
        return 0

    def sizeOfVertex(self): # real signature unknown; restored from __doc__
        """ sizeOfVertex(self) -> int """
        return 0

    def updateColoredRectGeometry(self, QSGGeometry, QRectF): # real signature unknown; restored from __doc__
        """ updateColoredRectGeometry(QSGGeometry, QRectF) """
        pass

    def updateRectGeometry(self, QSGGeometry, QRectF): # real signature unknown; restored from __doc__
        """ updateRectGeometry(QSGGeometry, QRectF) """
        pass

    def updateTexturedRectGeometry(self, QSGGeometry, QRectF, QRectF_1): # real signature unknown; restored from __doc__
        """ updateTexturedRectGeometry(QSGGeometry, QRectF, QRectF) """
        pass

    def vertexCount(self): # real signature unknown; restored from __doc__
        """ vertexCount(self) -> int """
        return 0

    def vertexData(self): # real signature unknown; restored from __doc__
        """ vertexData(self) -> sip.voidptr """
        pass

    def vertexDataAsColoredPoint2D(self): # real signature unknown; restored from __doc__
        """ vertexDataAsColoredPoint2D(self) -> sip.array[QSGGeometry.ColoredPoint2D] """
        pass

    def vertexDataAsPoint2D(self): # real signature unknown; restored from __doc__
        """ vertexDataAsPoint2D(self) -> sip.array[QSGGeometry.Point2D] """
        pass

    def vertexDataAsTexturedPoint2D(self): # real signature unknown; restored from __doc__
        """ vertexDataAsTexturedPoint2D(self) -> sip.array[QSGGeometry.TexturedPoint2D] """
        pass

    def vertexDataPattern(self): # real signature unknown; restored from __doc__
        """ vertexDataPattern(self) -> QSGGeometry.DataPattern """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AlwaysUploadPattern = 0
    ByteType = 5120
    ColorAttribute = 2
    DrawLineLoop = 2
    DrawLines = 1
    DrawLineStrip = 3
    DrawPoints = 0
    DrawTriangleFan = 6
    DrawTriangles = 4
    DrawTriangleStrip = 5
    DynamicPattern = 2
    FloatType = 5126
    GL_BYTE = 5120
    GL_DOUBLE = 5130
    GL_FLOAT = 5126
    GL_INT = 5124
    GL_LINES = 1
    GL_LINE_LOOP = 2
    GL_LINE_STRIP = 3
    GL_POINTS = 0
    GL_TRIANGLES = 4
    GL_TRIANGLE_FAN = 6
    GL_TRIANGLE_STRIP = 5
    IntType = 5124
    PositionAttribute = 1
    ShortType = 5122
    StaticPattern = 3
    StreamPattern = 1
    TexCoord1Attribute = 4
    TexCoord2Attribute = 5
    TexCoordAttribute = 3
    UnknownAttribute = 0
    UnsignedByteType = 5121
    UnsignedIntType = 5125
    UnsignedShortType = 5123


