# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QCommandLineOption(__sip.simplewrapper):
    """
    QCommandLineOption(str)
    QCommandLineOption(Iterable[str])
    QCommandLineOption(str, str, valueName: str = '', defaultValue: str = '')
    QCommandLineOption(Iterable[str], str, valueName: str = '', defaultValue: str = '')
    QCommandLineOption(QCommandLineOption)
    """
    def defaultValues(self): # real signature unknown; restored from __doc__
        """ defaultValues(self) -> List[str] """
        return []

    def description(self): # real signature unknown; restored from __doc__
        """ description(self) -> str """
        return ""

    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> QCommandLineOption.Flags """
        pass

    def isHidden(self): # real signature unknown; restored from __doc__
        """ isHidden(self) -> bool """
        return False

    def names(self): # real signature unknown; restored from __doc__
        """ names(self) -> List[str] """
        return []

    def setDefaultValue(self, p_str): # real signature unknown; restored from __doc__
        """ setDefaultValue(self, str) """
        pass

    def setDefaultValues(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ setDefaultValues(self, Iterable[str]) """
        pass

    def setDescription(self, p_str): # real signature unknown; restored from __doc__
        """ setDescription(self, str) """
        pass

    def setFlags(self, Union, QCommandLineOption_Flags=None, QCommandLineOption_Flag=None): # real signature unknown; restored from __doc__
        """ setFlags(self, Union[QCommandLineOption.Flags, QCommandLineOption.Flag]) """
        pass

    def setHidden(self, bool): # real signature unknown; restored from __doc__
        """ setHidden(self, bool) """
        pass

    def setValueName(self, p_str): # real signature unknown; restored from __doc__
        """ setValueName(self, str) """
        pass

    def swap(self, QCommandLineOption): # real signature unknown; restored from __doc__
        """ swap(self, QCommandLineOption) """
        pass

    def valueName(self): # real signature unknown; restored from __doc__
        """ valueName(self) -> str """
        return ""

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    HiddenFromHelp = 1
    ShortOptionStyle = 2


