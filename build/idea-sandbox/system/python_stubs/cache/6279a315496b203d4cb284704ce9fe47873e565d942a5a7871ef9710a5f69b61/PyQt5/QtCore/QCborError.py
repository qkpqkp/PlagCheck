# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QCborError(__sip.simplewrapper):
    """
    QCborError()
    QCborError(QCborError)
    """
    def code(self): # real signature unknown; restored from __doc__
        """ code(self) -> QCborError.Code """
        pass

    def toString(self): # real signature unknown; restored from __doc__
        """ toString(self) -> str """
        return ""

    def __init__(self, QCborError=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AdvancePastEnd = 3
    DataTooLarge = 1024
    EndOfFile = 257
    GarbageAtEnd = 256
    IllegalNumber = 261
    IllegalSimpleType = 262
    IllegalType = 260
    InputOutputError = 4
    InvalidUtf8String = 516
    NestingTooDeep = 1025
    NoError = 0
    UnexpectedBreak = 258
    UnknownError = 1
    UnknownType = 259
    UnsupportedType = 1026


