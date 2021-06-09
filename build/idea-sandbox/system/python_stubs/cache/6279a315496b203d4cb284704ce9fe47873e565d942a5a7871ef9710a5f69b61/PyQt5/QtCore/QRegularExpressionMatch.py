# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QRegularExpressionMatch(__sip.simplewrapper):
    """
    QRegularExpressionMatch()
    QRegularExpressionMatch(QRegularExpressionMatch)
    """
    def captured(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        captured(self, nth: int = 0) -> str
        captured(self, str) -> str
        """
        return ""

    def capturedEnd(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        capturedEnd(self, nth: int = 0) -> int
        capturedEnd(self, str) -> int
        """
        return 0

    def capturedLength(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        capturedLength(self, nth: int = 0) -> int
        capturedLength(self, str) -> int
        """
        return 0

    def capturedStart(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        capturedStart(self, nth: int = 0) -> int
        capturedStart(self, str) -> int
        """
        return 0

    def capturedTexts(self): # real signature unknown; restored from __doc__
        """ capturedTexts(self) -> List[str] """
        return []

    def hasMatch(self): # real signature unknown; restored from __doc__
        """ hasMatch(self) -> bool """
        return False

    def hasPartialMatch(self): # real signature unknown; restored from __doc__
        """ hasPartialMatch(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def lastCapturedIndex(self): # real signature unknown; restored from __doc__
        """ lastCapturedIndex(self) -> int """
        return 0

    def matchOptions(self): # real signature unknown; restored from __doc__
        """ matchOptions(self) -> QRegularExpression.MatchOptions """
        pass

    def matchType(self): # real signature unknown; restored from __doc__
        """ matchType(self) -> QRegularExpression.MatchType """
        pass

    def regularExpression(self): # real signature unknown; restored from __doc__
        """ regularExpression(self) -> QRegularExpression """
        return QRegularExpression

    def swap(self, QRegularExpressionMatch): # real signature unknown; restored from __doc__
        """ swap(self, QRegularExpressionMatch) """
        pass

    def __init__(self, QRegularExpressionMatch=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



