# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QCommandLineParser(__sip.simplewrapper):
    """ QCommandLineParser() """
    def addHelpOption(self): # real signature unknown; restored from __doc__
        """ addHelpOption(self) -> QCommandLineOption """
        return QCommandLineOption

    def addOption(self, QCommandLineOption): # real signature unknown; restored from __doc__
        """ addOption(self, QCommandLineOption) -> bool """
        return False

    def addOptions(self, Iterable, QCommandLineOption=None): # real signature unknown; restored from __doc__
        """ addOptions(self, Iterable[QCommandLineOption]) -> bool """
        return False

    def addPositionalArgument(self, p_str, p_str_1, syntax=''): # real signature unknown; restored from __doc__
        """ addPositionalArgument(self, str, str, syntax: str = '') """
        pass

    def addVersionOption(self): # real signature unknown; restored from __doc__
        """ addVersionOption(self) -> QCommandLineOption """
        return QCommandLineOption

    def applicationDescription(self): # real signature unknown; restored from __doc__
        """ applicationDescription(self) -> str """
        return ""

    def clearPositionalArguments(self): # real signature unknown; restored from __doc__
        """ clearPositionalArguments(self) """
        pass

    def errorText(self): # real signature unknown; restored from __doc__
        """ errorText(self) -> str """
        return ""

    def helpText(self): # real signature unknown; restored from __doc__
        """ helpText(self) -> str """
        return ""

    def isSet(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        isSet(self, str) -> bool
        isSet(self, QCommandLineOption) -> bool
        """
        return False

    def optionNames(self): # real signature unknown; restored from __doc__
        """ optionNames(self) -> List[str] """
        return []

    def parse(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ parse(self, Iterable[str]) -> bool """
        return False

    def positionalArguments(self): # real signature unknown; restored from __doc__
        """ positionalArguments(self) -> List[str] """
        return []

    def process(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        process(self, Iterable[str])
        process(self, QCoreApplication)
        """
        pass

    def setApplicationDescription(self, p_str): # real signature unknown; restored from __doc__
        """ setApplicationDescription(self, str) """
        pass

    def setOptionsAfterPositionalArgumentsMode(self, QCommandLineParser_OptionsAfterPositionalArgumentsMode): # real signature unknown; restored from __doc__
        """ setOptionsAfterPositionalArgumentsMode(self, QCommandLineParser.OptionsAfterPositionalArgumentsMode) """
        pass

    def setSingleDashWordOptionMode(self, QCommandLineParser_SingleDashWordOptionMode): # real signature unknown; restored from __doc__
        """ setSingleDashWordOptionMode(self, QCommandLineParser.SingleDashWordOptionMode) """
        pass

    def showHelp(self, exitCode=0): # real signature unknown; restored from __doc__
        """ showHelp(self, exitCode: int = 0) """
        pass

    def showVersion(self): # real signature unknown; restored from __doc__
        """ showVersion(self) """
        pass

    def unknownOptionNames(self): # real signature unknown; restored from __doc__
        """ unknownOptionNames(self) -> List[str] """
        return []

    def value(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        value(self, str) -> str
        value(self, QCommandLineOption) -> str
        """
        return ""

    def values(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        values(self, str) -> List[str]
        values(self, QCommandLineOption) -> List[str]
        """
        return []

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    ParseAsCompactedShortOptions = 0
    ParseAsLongOptions = 1
    ParseAsOptions = 0
    ParseAsPositionalArguments = 1


