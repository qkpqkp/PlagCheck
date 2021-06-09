# encoding: utf-8
# module zmq.backend.cython.message
# from C:\Users\Doly\Anaconda3\lib\site-packages\zmq\backend\cython\message.cp37-win_amd64.pyd
# by generator 1.147
""" 0MQ Message related classes. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import time as time # <module 'time' (built-in)>
import zmq as zmq # C:\Users\Doly\Anaconda3\lib\site-packages\zmq\__init__.py

# Variables with simple values

gc = None

# functions

def _check_version(min_version_info, msg=None): # reliably restored by inspect
    """
    Check for libzmq
        
        raises ZMQVersionError if current zmq version is not at least min_version
        
        min_version_info is a tuple of integers, and will be compared against zmq.zmq_version_info().
    """
    pass

def __reduce_cython__(*args, **kwargs): # real signature unknown
    pass

def __setstate_cython__(*args, **kwargs): # real signature unknown
    pass

# classes

class Event(object):
    """
    Class implementing event objects.
    
        Events manage a flag that can be set to true with the set() method and reset
        to false with the clear() method. The wait() method blocks until the flag is
        true.  The flag is initially false.
    """
    def clear(self): # reliably restored by inspect
        """
        Reset the internal flag to false.
        
                Subsequently, threads calling wait() will block until set() is called to
                set the internal flag to true again.
        """
        pass

    def isSet(self): # reliably restored by inspect
        """ Return true if and only if the internal flag is true. """
        pass

    def is_set(self): # reliably restored by inspect
        """ Return true if and only if the internal flag is true. """
        pass

    def set(self): # reliably restored by inspect
        """
        Set the internal flag to true.
        
                All threads waiting for it to become true are awakened. Threads
                that call wait() once the flag is true will not block at all.
        """
        pass

    def wait(self, timeout=None): # reliably restored by inspect
        """
        Block until the internal flag is true.
        
                If the internal flag is true on entry, return immediately. Otherwise,
                block until another thread calls set() to set the flag to true, or until
                the optional timeout occurs.
        
                When the timeout argument is present and not None, it should be a
                floating point number specifying a timeout for the operation in seconds
                (or fractions thereof).
        
                This method returns the internal flag on exit, so it will always return
                True except if a timeout is given and the operation times out.
        """
        pass

    def _reset_internal_locks(self): # reliably restored by inspect
        # no doc
        pass

    def __init__(self): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'threading', '__doc__': 'Class implementing event objects.\\n\\n    Events manage a flag that can be set to true with the set() method and reset\\n    to false with the clear() method. The wait() method blocks until the flag is\\n    true.  The flag is initially false.\\n\\n    ', '__init__': <function Event.__init__ at 0x0000019C49672AE8>, '_reset_internal_locks': <function Event._reset_internal_locks at 0x0000019C49672B70>, 'is_set': <function Event.is_set at 0x0000019C49672BF8>, 'isSet': <function Event.is_set at 0x0000019C49672BF8>, 'set': <function Event.set at 0x0000019C49672C80>, 'clear': <function Event.clear at 0x0000019C49672D08>, 'wait': <function Event.wait at 0x0000019C49672D90>, '__dict__': <attribute '__dict__' of 'Event' objects>, '__weakref__': <attribute '__weakref__' of 'Event' objects>})"


class Message(object):
    # no doc
    def get(self, option): # real signature unknown; restored from __doc__
        """
        Frame.get(option)
        
                Get a Frame option or property.
        
                See the 0MQ API documentation for zmq_msg_get and zmq_msg_gets
                for details on specific options.
        
                .. versionadded:: libzmq-3.2
                .. versionadded:: 13.0
        
                .. versionchanged:: 14.3
                    add support for zmq_msg_gets (requires libzmq-4.1)
                .. versionchanged:: 17.0
                    Added support for `routing_id` and `group`.
                    Only available if draft API is enabled
                    with libzmq >= 4.2.
        """
        pass

    def set(self, option, value): # real signature unknown; restored from __doc__
        """
        Frame.set(option, value)
                
                Set a Frame option.
                
                See the 0MQ API documentation for zmq_msg_set
                for details on specific options.
                
                .. versionadded:: libzmq-3.2
                .. versionadded:: 13.0
                .. versionchanged:: 17.0
                    Added support for `routing_id` and `group`.
                    Only available if draft API is enabled
                    with libzmq >= 4.2.
        """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        """
        Create a shallow copy of the message.
        
                This does not copy the contents of the Frame, just the pointer.
                This will increment the 0MQ ref count of the message, but not
                the ref count of the Python object. That is only done once when
                the Python is first turned into a 0MQ message.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """ Enforce signature """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return the length of the message in bytes. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return the str form of the message. """
        pass

    buffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A read-only buffer view of the message contents."""

    bytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The message content as a Python bytes object.

        The first time this property is accessed, a copy of the message 
        contents is made. From then on that same copy of the message is
        returned.
        """

    more = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tracker = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tracker_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000019C4B2B9FC0>'


Frame = Message


class MessageTracker(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


# variables with complex values

__all__ = [
    'Frame',
    'Message',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000019C4B41BB70>'

__spec__ = None # (!) real value is "ModuleSpec(name='zmq.backend.cython.message', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000019C4B41BB70>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\zmq\\\\backend\\\\cython\\\\message.cp37-win_amd64.pyd')"

__test__ = {}

