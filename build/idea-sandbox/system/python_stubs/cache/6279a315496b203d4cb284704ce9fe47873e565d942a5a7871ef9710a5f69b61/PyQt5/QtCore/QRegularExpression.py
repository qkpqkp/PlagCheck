# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QRegularExpression(__sip.simplewrapper):
    """
    QRegularExpression()
    QRegularExpression(str, options: Union[QRegularExpression.PatternOptions, QRegularExpression.PatternOption] = QRegularExpression.NoPatternOption)
    QRegularExpression(QRegularExpression)
    """
    def anchoredPattern(self, p_str): # real signature unknown; restored from __doc__
        """ anchoredPattern(str) -> str """
        return ""

    def captureCount(self): # real signature unknown; restored from __doc__
        """ captureCount(self) -> int """
        return 0

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def escape(self, p_str): # real signature unknown; restored from __doc__
        """ escape(str) -> str """
        return ""

    def globalMatch(self, p_str, offset=0, matchType=None, matchOptions, QRegularExpression_MatchOptions=None, QRegularExpression_MatchOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ globalMatch(self, str, offset: int = 0, matchType: QRegularExpression.MatchType = QRegularExpression.NormalMatch, matchOptions: Union[QRegularExpression.MatchOptions, QRegularExpression.MatchOption] = QRegularExpression.NoMatchOption) -> QRegularExpressionMatchIterator """
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def match(self, p_str, offset=0, matchType=None, matchOptions, QRegularExpression_MatchOptions=None, QRegularExpression_MatchOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ match(self, str, offset: int = 0, matchType: QRegularExpression.MatchType = QRegularExpression.NormalMatch, matchOptions: Union[QRegularExpression.MatchOptions, QRegularExpression.MatchOption] = QRegularExpression.NoMatchOption) -> QRegularExpressionMatch """
        pass

    def namedCaptureGroups(self): # real signature unknown; restored from __doc__
        """ namedCaptureGroups(self) -> List[str] """
        return []

    def optimize(self): # real signature unknown; restored from __doc__
        """ optimize(self) """
        pass

    def pattern(self): # real signature unknown; restored from __doc__
        """ pattern(self) -> str """
        return ""

    def patternErrorOffset(self): # real signature unknown; restored from __doc__
        """ patternErrorOffset(self) -> int """
        return 0

    def patternOptions(self): # real signature unknown; restored from __doc__
        """ patternOptions(self) -> QRegularExpression.PatternOptions """
        pass

    def setPattern(self, p_str): # real signature unknown; restored from __doc__
        """ setPattern(self, str) """
        pass

    def setPatternOptions(self, Union, QRegularExpression_PatternOptions=None, QRegularExpression_PatternOption=None): # real signature unknown; restored from __doc__
        """ setPatternOptions(self, Union[QRegularExpression.PatternOptions, QRegularExpression.PatternOption]) """
        pass

    def swap(self, QRegularExpression): # real signature unknown; restored from __doc__
        """ swap(self, QRegularExpression) """
        pass

    def wildcardToRegularExpression(self, p_str): # real signature unknown; restored from __doc__
        """ wildcardToRegularExpression(str) -> str """
        return ""

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AnchoredMatchOption = 1
    CaseInsensitiveOption = 1
    DontAutomaticallyOptimizeOption = 256
    DontCaptureOption = 32
    DontCheckSubjectStringMatchOption = 2
    DotMatchesEverythingOption = 2
    ExtendedPatternSyntaxOption = 8
    InvertedGreedinessOption = 16
    MultilineOption = 4
    NoMatch = 3
    NoMatchOption = 0
    NoPatternOption = 0
    NormalMatch = 0
    OptimizeOnFirstUsageOption = 128
    PartialPreferCompleteMatch = 1
    PartialPreferFirstMatch = 2
    UseUnicodePropertiesOption = 64


