# encoding: utf-8
# module lxml.etree
# from C:\Users\Doly\Anaconda3\lib\site-packages\lxml\etree.cp37-win_amd64.pyd
# by generator 1.147
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from .object import object

class ErrorLevels(object):
    """ Libxml2 error levels """
    def _getName(self, *args, **kwargs): # real signature unknown
        """ Return the value for key if key is in the dictionary, else default. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    ERROR = 2
    FATAL = 3
    NONE = 0
    WARNING = 1
    _names = {
        0: 'NONE',
        1: 'WARNING',
        2: 'ERROR',
        3: 'FATAL',
    }
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'lxml.etree', '__doc__': 'Libxml2 error levels', '__dict__': <attribute '__dict__' of 'ErrorLevels' objects>, '__weakref__': <attribute '__weakref__' of 'ErrorLevels' objects>, '_names': {0: 'NONE', 1: 'WARNING', 2: 'ERROR', 3: 'FATAL'}, '_getName': <built-in method get of dict object at 0x000002467EE00FC0>, 'NONE': 0, 'WARNING': 1, 'ERROR': 2, 'FATAL': 3})"


