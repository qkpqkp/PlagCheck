# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QOpenGLShaderProgram(__PyQt5_QtCore.QObject):
    """ QOpenGLShaderProgram(parent: QObject = None) """
    def addCacheableShaderFromSourceCode(self, Union, QOpenGLShader_ShaderType=None, QOpenGLShader_ShaderTypeBit=None, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addCacheableShaderFromSourceCode(self, Union[QOpenGLShader.ShaderType, QOpenGLShader.ShaderTypeBit], Union[QByteArray, bytes, bytearray]) -> bool
        addCacheableShaderFromSourceCode(self, Union[QOpenGLShader.ShaderType, QOpenGLShader.ShaderTypeBit], str) -> bool
        """
        pass

    def addCacheableShaderFromSourceFile(self, Union, QOpenGLShader_ShaderType=None, QOpenGLShader_ShaderTypeBit=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ addCacheableShaderFromSourceFile(self, Union[QOpenGLShader.ShaderType, QOpenGLShader.ShaderTypeBit], str) -> bool """
        pass

    def addShader(self, QOpenGLShader): # real signature unknown; restored from __doc__
        """ addShader(self, QOpenGLShader) -> bool """
        return False

    def addShaderFromSourceCode(self, Union, QOpenGLShader_ShaderType=None, QOpenGLShader_ShaderTypeBit=None, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addShaderFromSourceCode(self, Union[QOpenGLShader.ShaderType, QOpenGLShader.ShaderTypeBit], Union[QByteArray, bytes, bytearray]) -> bool
        addShaderFromSourceCode(self, Union[QOpenGLShader.ShaderType, QOpenGLShader.ShaderTypeBit], str) -> bool
        """
        pass

    def addShaderFromSourceFile(self, Union, QOpenGLShader_ShaderType=None, QOpenGLShader_ShaderTypeBit=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ addShaderFromSourceFile(self, Union[QOpenGLShader.ShaderType, QOpenGLShader.ShaderTypeBit], str) -> bool """
        pass

    def attributeLocation(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        attributeLocation(self, Union[QByteArray, bytes, bytearray]) -> int
        attributeLocation(self, str) -> int
        """
        return 0

    def bind(self): # real signature unknown; restored from __doc__
        """ bind(self) -> bool """
        return False

    def bindAttributeLocation(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        bindAttributeLocation(self, Union[QByteArray, bytes, bytearray], int)
        bindAttributeLocation(self, str, int)
        """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def create(self): # real signature unknown; restored from __doc__
        """ create(self) -> bool """
        return False

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultInnerTessellationLevels(self): # real signature unknown; restored from __doc__
        """ defaultInnerTessellationLevels(self) -> List[float] """
        return []

    def defaultOuterTessellationLevels(self): # real signature unknown; restored from __doc__
        """ defaultOuterTessellationLevels(self) -> List[float] """
        return []

    def disableAttributeArray(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        disableAttributeArray(self, int)
        disableAttributeArray(self, str)
        """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def enableAttributeArray(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        enableAttributeArray(self, int)
        enableAttributeArray(self, str)
        """
        pass

    def hasOpenGLShaderPrograms(self, context=None): # real signature unknown; restored from __doc__
        """ hasOpenGLShaderPrograms(context: QOpenGLContext = None) -> bool """
        return False

    def isLinked(self): # real signature unknown; restored from __doc__
        """ isLinked(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def link(self): # real signature unknown; restored from __doc__
        """ link(self) -> bool """
        return False

    def log(self): # real signature unknown; restored from __doc__
        """ log(self) -> str """
        return ""

    def maxGeometryOutputVertices(self): # real signature unknown; restored from __doc__
        """ maxGeometryOutputVertices(self) -> int """
        return 0

    def patchVertexCount(self): # real signature unknown; restored from __doc__
        """ patchVertexCount(self) -> int """
        return 0

    def programId(self): # real signature unknown; restored from __doc__
        """ programId(self) -> int """
        return 0

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def release(self): # real signature unknown; restored from __doc__
        """ release(self) """
        pass

    def removeAllShaders(self): # real signature unknown; restored from __doc__
        """ removeAllShaders(self) """
        pass

    def removeShader(self, QOpenGLShader): # real signature unknown; restored from __doc__
        """ removeShader(self, QOpenGLShader) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAttributeArray(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setAttributeArray(self, int, PYQT_SHADER_ATTRIBUTE_ARRAY)
        setAttributeArray(self, str, PYQT_SHADER_ATTRIBUTE_ARRAY)
        """
        pass

    def setAttributeBuffer(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setAttributeBuffer(self, int, int, int, int, stride: int = 0)
        setAttributeBuffer(self, str, int, int, int, stride: int = 0)
        """
        pass

    def setAttributeValue(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setAttributeValue(self, int, float)
        setAttributeValue(self, int, float, float)
        setAttributeValue(self, int, float, float, float)
        setAttributeValue(self, int, float, float, float, float)
        setAttributeValue(self, int, QVector2D)
        setAttributeValue(self, int, QVector3D)
        setAttributeValue(self, int, QVector4D)
        setAttributeValue(self, int, Union[QColor, Qt.GlobalColor, QGradient])
        setAttributeValue(self, str, float)
        setAttributeValue(self, str, float, float)
        setAttributeValue(self, str, float, float, float)
        setAttributeValue(self, str, float, float, float, float)
        setAttributeValue(self, str, QVector2D)
        setAttributeValue(self, str, QVector3D)
        setAttributeValue(self, str, QVector4D)
        setAttributeValue(self, str, Union[QColor, Qt.GlobalColor, QGradient])
        """
        pass

    def setDefaultInnerTessellationLevels(self, Iterable, p_float=None): # real signature unknown; restored from __doc__
        """ setDefaultInnerTessellationLevels(self, Iterable[float]) """
        pass

    def setDefaultOuterTessellationLevels(self, Iterable, p_float=None): # real signature unknown; restored from __doc__
        """ setDefaultOuterTessellationLevels(self, Iterable[float]) """
        pass

    def setPatchVertexCount(self, p_int): # real signature unknown; restored from __doc__
        """ setPatchVertexCount(self, int) """
        pass

    def setUniformValue(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setUniformValue(self, int, int)
        setUniformValue(self, int, float)
        setUniformValue(self, int, float, float)
        setUniformValue(self, int, float, float, float)
        setUniformValue(self, int, float, float, float, float)
        setUniformValue(self, int, QVector2D)
        setUniformValue(self, int, QVector3D)
        setUniformValue(self, int, QVector4D)
        setUniformValue(self, int, Union[QColor, Qt.GlobalColor, QGradient])
        setUniformValue(self, int, QPoint)
        setUniformValue(self, int, Union[QPointF, QPoint])
        setUniformValue(self, int, QSize)
        setUniformValue(self, int, QSizeF)
        setUniformValue(self, int, QMatrix2x2)
        setUniformValue(self, int, QMatrix2x3)
        setUniformValue(self, int, QMatrix2x4)
        setUniformValue(self, int, QMatrix3x2)
        setUniformValue(self, int, QMatrix3x3)
        setUniformValue(self, int, QMatrix3x4)
        setUniformValue(self, int, QMatrix4x2)
        setUniformValue(self, int, QMatrix4x3)
        setUniformValue(self, int, QMatrix4x4)
        setUniformValue(self, int, QTransform)
        setUniformValue(self, str, int)
        setUniformValue(self, str, float)
        setUniformValue(self, str, float, float)
        setUniformValue(self, str, float, float, float)
        setUniformValue(self, str, float, float, float, float)
        setUniformValue(self, str, QVector2D)
        setUniformValue(self, str, QVector3D)
        setUniformValue(self, str, QVector4D)
        setUniformValue(self, str, Union[QColor, Qt.GlobalColor, QGradient])
        setUniformValue(self, str, QPoint)
        setUniformValue(self, str, Union[QPointF, QPoint])
        setUniformValue(self, str, QSize)
        setUniformValue(self, str, QSizeF)
        setUniformValue(self, str, QMatrix2x2)
        setUniformValue(self, str, QMatrix2x3)
        setUniformValue(self, str, QMatrix2x4)
        setUniformValue(self, str, QMatrix3x2)
        setUniformValue(self, str, QMatrix3x3)
        setUniformValue(self, str, QMatrix3x4)
        setUniformValue(self, str, QMatrix4x2)
        setUniformValue(self, str, QMatrix4x3)
        setUniformValue(self, str, QMatrix4x4)
        setUniformValue(self, str, QTransform)
        """
        pass

    def setUniformValueArray(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setUniformValueArray(self, int, PYQT_SHADER_UNIFORM_VALUE_ARRAY)
        setUniformValueArray(self, str, PYQT_SHADER_UNIFORM_VALUE_ARRAY)
        """
        pass

    def shaders(self): # real signature unknown; restored from __doc__
        """ shaders(self) -> List[QOpenGLShader] """
        return []

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def uniformLocation(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        uniformLocation(self, Union[QByteArray, bytes, bytearray]) -> int
        uniformLocation(self, str) -> int
        """
        return 0

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


