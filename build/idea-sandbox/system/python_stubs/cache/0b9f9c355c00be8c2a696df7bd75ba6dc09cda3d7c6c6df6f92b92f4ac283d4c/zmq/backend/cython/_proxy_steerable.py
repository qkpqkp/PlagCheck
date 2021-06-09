# encoding: utf-8
# module zmq.backend.cython._proxy_steerable
# from C:\Users\Doly\Anaconda3\lib\site-packages\zmq\backend\cython\_proxy_steerable.cp37-win_amd64.pyd
# by generator 1.147
""" Python binding for ZMQ steerable proxy function. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import zmq.error as __zmq_error


# functions

def proxy_steerable(frontend, backend, capture, control): # real signature unknown; restored from __doc__
    """
    proxy_steerable(frontend, backend, capture, control)
    
        Start a zeromq proxy with control flow.
    
        .. versionadded:: libzmq-4.1
        .. versionadded:: 18.0
    
        Parameters
        ----------
        frontend : Socket
            The Socket instance for the incoming traffic.
        backend : Socket
            The Socket instance for the outbound traffic.
        capture : Socket (optional)
            The Socket instance for capturing traffic.
        control : Socket (optional)
            The Socket instance for control flow.
    """
    pass

# classes

class InterruptedSystemCall(__zmq_error.ZMQError, InterruptedError):
    """
    Wrapper for EINTR
        
        This exception should be caught internally in pyzmq
        to retry system calls, and not propagate to the user.
        
        .. versionadded:: 14.7
    """
    def __init__(self, errno=None, msg=None): # reliably restored by inspect
        # no doc
        pass

    def __str__(self): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__all__ = [
    'proxy_steerable',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001F131650780>'

__spec__ = None # (!) real value is "ModuleSpec(name='zmq.backend.cython._proxy_steerable', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001F131650780>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\zmq\\\\backend\\\\cython\\\\_proxy_steerable.cp37-win_amd64.pyd')"

__test__ = {}

