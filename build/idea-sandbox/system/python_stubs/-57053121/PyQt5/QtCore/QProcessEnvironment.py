# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QProcessEnvironment(__sip.simplewrapper):
    """
    QProcessEnvironment()
    QProcessEnvironment(QProcessEnvironment)
    """
    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def contains(self, p_str): # real signature unknown; restored from __doc__
        """ contains(self, str) -> bool """
        return False

    def insert(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        insert(self, str, str)
        insert(self, QProcessEnvironment)
        """
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def keys(self): # real signature unknown; restored from __doc__
        """ keys(self) -> List[str] """
        return []

    def remove(self, p_str): # real signature unknown; restored from __doc__
        """ remove(self, str) """
        pass

    def swap(self, QProcessEnvironment): # real signature unknown; restored from __doc__
        """ swap(self, QProcessEnvironment) """
        pass

    def systemEnvironment(self): # real signature unknown; restored from __doc__
        """ systemEnvironment() -> QProcessEnvironment """
        return QProcessEnvironment

    def toStringList(self): # real signature unknown; restored from __doc__
        """ toStringList(self) -> List[str] """
        return []

    def value(self, p_str, defaultValue=''): # real signature unknown; restored from __doc__
        """ value(self, str, defaultValue: str = '') -> str """
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

    def __init__(self, QProcessEnvironment=None): # real signature unknown; restored from __doc__ with multiple overloads
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

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __hash__ = None


