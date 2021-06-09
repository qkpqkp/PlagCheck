# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QCollator(__sip.simplewrapper):
    """
    QCollator(locale: QLocale = QLocale())
    QCollator(QCollator)
    """
    def caseSensitivity(self): # real signature unknown; restored from __doc__
        """ caseSensitivity(self) -> Qt.CaseSensitivity """
        pass

    def compare(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ compare(self, str, str) -> int """
        return 0

    def ignorePunctuation(self): # real signature unknown; restored from __doc__
        """ ignorePunctuation(self) -> bool """
        return False

    def locale(self): # real signature unknown; restored from __doc__
        """ locale(self) -> QLocale """
        return QLocale

    def numericMode(self): # real signature unknown; restored from __doc__
        """ numericMode(self) -> bool """
        return False

    def setCaseSensitivity(self, Qt_CaseSensitivity): # real signature unknown; restored from __doc__
        """ setCaseSensitivity(self, Qt.CaseSensitivity) """
        pass

    def setIgnorePunctuation(self, bool): # real signature unknown; restored from __doc__
        """ setIgnorePunctuation(self, bool) """
        pass

    def setLocale(self, QLocale): # real signature unknown; restored from __doc__
        """ setLocale(self, QLocale) """
        pass

    def setNumericMode(self, bool): # real signature unknown; restored from __doc__
        """ setNumericMode(self, bool) """
        pass

    def sortKey(self, p_str): # real signature unknown; restored from __doc__
        """ sortKey(self, str) -> QCollatorSortKey """
        return QCollatorSortKey

    def swap(self, QCollator): # real signature unknown; restored from __doc__
        """ swap(self, QCollator) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



