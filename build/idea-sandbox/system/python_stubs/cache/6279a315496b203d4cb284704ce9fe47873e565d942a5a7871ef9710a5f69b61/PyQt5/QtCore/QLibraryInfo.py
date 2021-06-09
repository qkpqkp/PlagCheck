# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QLibraryInfo(__sip.simplewrapper):
    """ QLibraryInfo(QLibraryInfo) """
    def buildDate(self): # real signature unknown; restored from __doc__
        """ buildDate() -> QDate """
        return QDate

    def isDebugBuild(self): # real signature unknown; restored from __doc__
        """ isDebugBuild() -> bool """
        return False

    def licensedProducts(self): # real signature unknown; restored from __doc__
        """ licensedProducts() -> str """
        return ""

    def licensee(self): # real signature unknown; restored from __doc__
        """ licensee() -> str """
        return ""

    def location(self, QLibraryInfo_LibraryLocation): # real signature unknown; restored from __doc__
        """ location(QLibraryInfo.LibraryLocation) -> str """
        return ""

    def version(self): # real signature unknown; restored from __doc__
        """ version() -> QVersionNumber """
        return QVersionNumber

    def __init__(self, QLibraryInfo): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    ArchDataPath = 9
    BinariesPath = 5
    DataPath = 10
    DocumentationPath = 1
    ExamplesPath = 12
    HeadersPath = 2
    ImportsPath = 7
    LibrariesPath = 3
    LibraryExecutablesPath = 4
    PluginsPath = 6
    PrefixPath = 0
    Qml2ImportsPath = 8
    SettingsPath = 100
    TestsPath = 13
    TranslationsPath = 11


