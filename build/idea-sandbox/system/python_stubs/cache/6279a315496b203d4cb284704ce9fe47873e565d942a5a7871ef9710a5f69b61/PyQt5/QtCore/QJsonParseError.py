# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QJsonParseError(__sip.simplewrapper):
    """
    QJsonParseError()
    QJsonParseError(QJsonParseError)
    """
    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def __init__(self, QJsonParseError=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    DeepNesting = 12
    DocumentTooLarge = 13
    GarbageAtEnd = 14
    IllegalEscapeSequence = 8
    IllegalNumber = 7
    IllegalUTF8String = 9
    IllegalValue = 5
    MissingNameSeparator = 2
    MissingObject = 11
    MissingValueSeparator = 4
    NoError = 0
    TerminationByNumber = 6
    UnterminatedArray = 3
    UnterminatedObject = 1
    UnterminatedString = 10


