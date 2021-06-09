# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QRandomGenerator(__sip.simplewrapper):
    """
    QRandomGenerator(seed: int = 1)
    QRandomGenerator(QRandomGenerator)
    """
    def bounded(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        bounded(self, float) -> float
        bounded(self, int) -> int
        bounded(self, int, int) -> int
        """
        return 0.0 or 0

    def discard(self, p_int): # real signature unknown; restored from __doc__
        """ discard(self, int) """
        pass

    def generate(self): # real signature unknown; restored from __doc__
        """ generate(self) -> int """
        return 0

    def generate64(self): # real signature unknown; restored from __doc__
        """ generate64(self) -> int """
        return 0

    def generateDouble(self): # real signature unknown; restored from __doc__
        """ generateDouble(self) -> float """
        return 0.0

    def global_(self): # real signature unknown; restored from __doc__
        """ global_() -> QRandomGenerator """
        return QRandomGenerator

    def max(self): # real signature unknown; restored from __doc__
        """ max() -> int """
        return 0

    def min(self): # real signature unknown; restored from __doc__
        """ min() -> int """
        return 0

    def securelySeeded(self): # real signature unknown; restored from __doc__
        """ securelySeeded() -> QRandomGenerator """
        return QRandomGenerator

    def seed(self, seed=1): # real signature unknown; restored from __doc__
        """ seed(self, seed: int = 1) """
        pass

    def system(self): # real signature unknown; restored from __doc__
        """ system() -> QRandomGenerator """
        return QRandomGenerator

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
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

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __hash__ = None


