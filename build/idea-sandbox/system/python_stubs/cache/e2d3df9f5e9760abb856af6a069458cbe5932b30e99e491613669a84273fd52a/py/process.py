# encoding: utf-8
# module py.process
# from C:\Users\Doly\Anaconda3\lib\site-packages\sklearn\cluster\_k_means_elkan.cp37-win_amd64.pyd
# by generator 1.147
""" high-level sub-process handling """
# no imports

# Variables with simple values

_ApiModule__doc = ' high-level sub-process handling '

__implprefix__ = 'py'

# functions

def cmdexec(cmd): # reliably restored by inspect
    """
    return unicode output of executing 'cmd' in a separate process.
    
        raise cmdexec.Error exeception if the command failed.
        the exception will provide an 'err' attribute containing
        the error-output from the command.
        if the subprocess module does not provide a proper encoding/unicode strings
        sys.getdefaultencoding() will be used, if that does not exist, 'UTF-8'.
    """
    pass

def kill(pid): # reliably restored by inspect
    """ kill process by id. """
    pass

# classes

class ForkedFunc(object):
    # no doc
    def waitfinish(self, waiter='<built-in function waitpid>'): # reliably restored by inspect
        # no doc
        pass

    def _child(self, nice_level, child_on_start, child_on_exit): # reliably restored by inspect
        # no doc
        pass

    def _removetemp(self): # reliably restored by inspect
        # no doc
        pass

    def __del__(self): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, fun, args=None, kwargs=None, nice_level=0, child_on_start=None, child_on_exit=None): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    EXITSTATUS_EXCEPTION = 3
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'py._process.forkedfunc', 'EXITSTATUS_EXCEPTION': 3, '__init__': <function ForkedFunc.__init__ at 0x0000017B6ABB2950>, '_child': <function ForkedFunc._child at 0x0000017B6ABB29D8>, 'waitfinish': <function ForkedFunc.waitfinish at 0x0000017B6ABB2A60>, '_removetemp': <function ForkedFunc._removetemp at 0x0000017B6ABB2AE8>, '__del__': <function ForkedFunc.__del__ at 0x0000017B6ABB2B70>, '__dict__': <attribute '__dict__' of 'ForkedFunc' objects>, '__weakref__': <attribute '__weakref__' of 'ForkedFunc' objects>, '__doc__': None})"


# variables with complex values

__all__ = [
    '__doc__',
    'cmdexec',
    'kill',
    'ForkedFunc',
]

__map__ = {}

