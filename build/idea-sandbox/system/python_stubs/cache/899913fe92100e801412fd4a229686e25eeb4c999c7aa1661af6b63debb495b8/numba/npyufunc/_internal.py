# encoding: utf-8
# module numba.npyufunc._internal
# from C:\Users\Doly\Anaconda3\lib\site-packages\numba\npyufunc\_internal.cp37-win_amd64.pyd
# by generator 1.147
""" No docs """
# no imports

# Variables with simple values

PyUFunc_None = -1
PyUFunc_One = 1
PyUFunc_ReorderableNone = -2
PyUFunc_Zero = 0

# functions

def fromfunc(*args, **kwargs): # real signature unknown
    pass

# classes

class _DUFunc(object):
    # no doc
    def accumulate(self, *args, **kwargs): # real signature unknown
        pass

    def at(self, *args, **kwargs): # real signature unknown
        pass

    def outer(self, *args, **kwargs): # real signature unknown
        pass

    def reduce(self, *args, **kwargs): # real signature unknown
        pass

    def reduceat(self, *args, **kwargs): # real signature unknown
        pass

    def _add_loop(self, *args, **kwargs): # real signature unknown
        pass

    def _compile_for_args(self): # real signature unknown; restored from __doc__
        """ Abstract method: subclasses should overload _compile_for_args() to compile the ufunc at the given arguments' types. """
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    ufunc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Numpy Ufunc for the dynamic ufunc."""

    _dispatcher = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Dispatcher object for the core Python function."""

    _frozen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """flag indicating call-time compilation has been disabled"""

    _keepalive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """List of objects to keep alive during life of dufunc."""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000022456CBE2B0>'

__spec__ = None # (!) real value is "ModuleSpec(name='numba.npyufunc._internal', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000022456CBE2B0>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\numba\\\\npyufunc\\\\_internal.cp37-win_amd64.pyd')"

