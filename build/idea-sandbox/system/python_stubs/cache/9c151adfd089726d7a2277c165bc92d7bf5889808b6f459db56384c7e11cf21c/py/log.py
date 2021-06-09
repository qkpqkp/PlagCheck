# encoding: utf-8
# module py.log
# from C:\Users\Doly\Anaconda3\lib\site-packages\sklearn\neighbors\kd_tree.cp37-win_amd64.pyd
# by generator 1.147
""" logging API ('producers' and 'consumers' connected via keywords) """
# no imports

# Variables with simple values

_ApiModule__doc = " logging API ('producers' and 'consumers' connected via keywords) "

__implprefix__ = 'py'

# functions

def setconsumer(keywords, consumer): # reliably restored by inspect
    # no doc
    pass

def STDERR(msg): # reliably restored by inspect
    """ consumer that writes to sys.stderr """
    pass

def STDOUT(msg): # reliably restored by inspect
    """ consumer that writes to sys.stdout """
    pass

def _apiwarn(startversion, msg, stacklevel=2, function=None): # reliably restored by inspect
    # no doc
    pass

def _getstate(): # reliably restored by inspect
    # no doc
    pass

def _setstate(state): # reliably restored by inspect
    # no doc
    pass

# classes

class Path(object):
    """ log consumer that opens and writes to a Path """
    def _openfile(self): # reliably restored by inspect
        # no doc
        pass

    def __call__(self, msg): # reliably restored by inspect
        """ write a message to the log """
        pass

    def __init__(self, filename, append=False, delayed_create=False, buffering=False): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'py._log.log', '__doc__': ' log consumer that opens and writes to a Path ', '__init__': <function Path.__init__ at 0x00000256F90EF048>, '_openfile': <function Path._openfile at 0x00000256F90EF0D0>, '__call__': <function Path.__call__ at 0x00000256F90EF158>, '__dict__': <attribute '__dict__' of 'Path' objects>, '__weakref__': <attribute '__weakref__' of 'Path' objects>})"


class Producer(object):
    """
    (deprecated) Log producer API which sends messages to be logged
            to a 'consumer' object, which then prints them to stdout,
            stderr, files, etc. Used extensively by PyPy-1.1.
    """
    def __call__(self, *args): # reliably restored by inspect
        """ write a message to the appropriate consumer(s) """
        pass

    def __getattr__(self, name): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, keywords, keywordmapper=None, **kw): # reliably restored by inspect
        # no doc
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    keywords2consumer = {}
    Message = None # (!) real value is "<class 'py._log.log.Message'>"
    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'py._log.log\', \'__doc__\': " (deprecated) Log producer API which sends messages to be logged\\n        to a \'consumer\' object, which then prints them to stdout,\\n        stderr, files, etc. Used extensively by PyPy-1.1.\\n    ", \'Message\': <class \'py._log.log.Message\'>, \'keywords2consumer\': {}, \'__init__\': <function Producer.__init__ at 0x00000256F90E9510>, \'__repr__\': <function Producer.__repr__ at 0x00000256F90E2488>, \'__getattr__\': <function Producer.__getattr__ at 0x00000256F90E2BF8>, \'__call__\': <function Producer.__call__ at 0x00000256F8FB57B8>, \'__dict__\': <attribute \'__dict__\' of \'Producer\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'Producer\' objects>})'


class Syslog(object):
    """ consumer that writes to the syslog daemon """
    def __call__(self, msg): # reliably restored by inspect
        """ write a message to the log """
        pass

    def __init__(self, priority=None): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'py._log.log', '__doc__': ' consumer that writes to the syslog daemon ', '__init__': <function Syslog.__init__ at 0x00000256F90EF2F0>, '__call__': <function Syslog.__call__ at 0x00000256F90EF378>, '__dict__': <attribute '__dict__' of 'Syslog' objects>, '__weakref__': <attribute '__weakref__' of 'Syslog' objects>})"


# variables with complex values

__all__ = [
    '__doc__',
    '_apiwarn',
    'Producer',
    'setconsumer',
    '_setstate',
    '_getstate',
    'Path',
    'STDOUT',
    'STDERR',
    'Syslog',
]

__map__ = {}

