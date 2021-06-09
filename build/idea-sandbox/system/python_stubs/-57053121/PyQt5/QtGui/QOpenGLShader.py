# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QOpenGLShader(__PyQt5_QtCore.QObject):
    """ QOpenGLShader(Union[QOpenGLShader.ShaderType, QOpenGLShader.ShaderTypeBit], parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def compileSourceCode(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        compileSourceCode(self, Union[QByteArray, bytes, bytearray]) -> bool
        compileSourceCode(self, str) -> bool
        """
        return False

    def compileSourceFile(self, p_str): # real signature unknown; restored from __doc__
        """ compileSourceFile(self, str) -> bool """
        return False

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def hasOpenGLShaders(self, Union, QOpenGLShader_ShaderType=None, QOpenGLShader_ShaderTypeBit=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ hasOpenGLShaders(Union[QOpenGLShader.ShaderType, QOpenGLShader.ShaderTypeBit], context: QOpenGLContext = None) -> bool """
        pass

    def isCompiled(self): # real signature unknown; restored from __doc__
        """ isCompiled(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def log(self): # real signature unknown; restored from __doc__
        """ log(self) -> str """
        return ""

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def shaderId(self): # real signature unknown; restored from __doc__
        """ shaderId(self) -> int """
        return 0

    def shaderType(self): # real signature unknown; restored from __doc__
        """ shaderType(self) -> QOpenGLShader.ShaderType """
        pass

    def sourceCode(self): # real signature unknown; restored from __doc__
        """ sourceCode(self) -> QByteArray """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, Union, QOpenGLShader_ShaderType=None, QOpenGLShader_ShaderTypeBit=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    Compute = 32
    Fragment = 2
    Geometry = 4
    TessellationControl = 8
    TessellationEvaluation = 16
    Vertex = 1


