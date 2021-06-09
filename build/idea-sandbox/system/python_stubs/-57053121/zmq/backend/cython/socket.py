# encoding: utf-8
# module zmq.backend.cython.socket
# from C:\Users\Doly\Anaconda3\lib\site-packages\zmq\backend\cython\socket.cp37-win_amd64.pyd
# by generator 1.147
""" 0MQ Socket class. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import copy as copy_mod # C:\Users\Doly\Anaconda3\lib\copy.py
import time as time # <module 'time' (built-in)>
import sys as sys # <module 'sys' (built-in)>
import random as random # C:\Users\Doly\Anaconda3\lib\random.py
import struct as struct # C:\Users\Doly\Anaconda3\lib\struct.py
import codecs as codecs # C:\Users\Doly\Anaconda3\lib\codecs.py
import pickle as pickle # C:\Users\Doly\Anaconda3\lib\pickle.py
import zmq as zmq # C:\Users\Doly\Anaconda3\lib\site-packages\zmq\__init__.py
import zmq.backend.cython.constants as constants # C:\Users\Doly\Anaconda3\lib\site-packages\zmq\backend\cython\constants.cp37-win_amd64.pyd
import zmq.error as __zmq_error


# Variables with simple values

cPickle = None

IPC_PATH_MAX_LEN = 0

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

class ZMQError(__zmq_error.ZMQBaseError):
    """
    Wrap an errno style error.
    
        Parameters
        ----------
        errno : int
            The ZMQ errno or None.  If None, then ``zmq_errno()`` is called and
            used.
        msg : string
            Description of the error or None.
    """
    def __init__(self, errno=None, msg=None): # reliably restored by inspect
        """
        Wrap an errno style error.
        
                Parameters
                ----------
                errno : int
                    The ZMQ errno or None.  If None, then ``zmq_errno()`` is called and
                    used.
                msg : string
                    Description of the error or None.
        """
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    def __str__(self): # reliably restored by inspect
        # no doc
        pass

    errno = None


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



class Socket(object):
    """
    Socket(context, socket_type)
    
        A 0MQ socket.
    
        These objects will generally be constructed via the socket() method of a Context object.
        
        Note: 0MQ Sockets are *not* threadsafe. **DO NOT** share them across threads.
        
        Parameters
        ----------
        context : Context
            The 0MQ Context this Socket belongs to.
        socket_type : int
            The socket type, which can be any of the 0MQ socket types: 
            REQ, REP, PUB, SUB, PAIR, DEALER, ROUTER, PULL, PUSH, XPUB, XSUB.
        
        See Also
        --------
        .Context.socket : method for creating a socket bound to a Context.
    """
    def bind(self, addr): # real signature unknown; restored from __doc__
        """
        s.bind(addr)
        
                Bind the socket to an address.
        
                This causes the socket to listen on a network port. Sockets on the
                other side of this connection will use ``Socket.connect(addr)`` to
                connect to this socket.
        
                Parameters
                ----------
                addr : str
                    The address string. This has the form 'protocol://interface:port',
                    for example 'tcp://127.0.0.1:5555'. Protocols supported include
                    tcp, udp, pgm, epgm, inproc and ipc. If the address is unicode, it is
                    encoded to utf-8 first.
        """
        pass

    def close(self, linger=None): # real signature unknown; restored from __doc__
        """
        s.close(linger=None)
        
                Close the socket.
        
                If linger is specified, LINGER sockopt will be set prior to closing.
        
                This can be called to close the socket by hand. If this is not
                called, the socket will automatically be closed when it is
                garbage collected.
        """
        pass

    def connect(self, addr): # real signature unknown; restored from __doc__
        """
        s.connect(addr)
        
                Connect to a remote 0MQ socket.
        
                Parameters
                ----------
                addr : str
                    The address string. This has the form 'protocol://interface:port',
                    for example 'tcp://127.0.0.1:5555'. Protocols supported are
                    tcp, upd, pgm, inproc and ipc. If the address is unicode, it is
                    encoded to utf-8 first.
        """
        pass

    def disconnect(self, addr): # real signature unknown; restored from __doc__
        """
        s.disconnect(addr)
        
                Disconnect from a remote 0MQ socket (undoes a call to connect).
                
                .. versionadded:: libzmq-3.2
                .. versionadded:: 13.0
        
                Parameters
                ----------
                addr : str
                    The address string. This has the form 'protocol://interface:port',
                    for example 'tcp://127.0.0.1:5555'. Protocols supported are
                    tcp, upd, pgm, inproc and ipc. If the address is unicode, it is
                    encoded to utf-8 first.
        """
        pass

    def get(self, option): # real signature unknown; restored from __doc__
        """
        s.get(option)
        
                Get the value of a socket option.
        
                See the 0MQ API documentation for details on specific options.
        
                Parameters
                ----------
                option : int
                    The option to get.  Available values will depend on your
                    version of libzmq.  Examples include::
                    
                        zmq.IDENTITY, HWM, LINGER, FD, EVENTS
        
                Returns
                -------
                optval : int or bytes
                    The value of the option as a bytestring or int.
        """
        pass

    def join(self, group): # real signature unknown; restored from __doc__
        """
        join(group)
        
                Join a RADIO-DISH group
        
                Only for DISH sockets.
        
                libzmq and pyzmq must have been built with ZMQ_BUILD_DRAFT_API
        
                .. versionadded:: 17
        """
        pass

    def leave(self, group): # real signature unknown; restored from __doc__
        """
        leave(group)
        
                Leave a RADIO-DISH group
        
                Only for DISH sockets.
        
                libzmq and pyzmq must have been built with ZMQ_BUILD_DRAFT_API
        
                .. versionadded:: 17
        """
        pass

    def monitor(self, addr, flags): # real signature unknown; restored from __doc__
        """
        s.monitor(addr, flags)
        
                Start publishing socket events on inproc.
                See libzmq docs for zmq_monitor for details.
        
                While this function is available from libzmq 3.2,
                pyzmq cannot parse monitor messages from libzmq prior to 4.0.
        
                .. versionadded: libzmq-3.2
                .. versionadded: 14.0
        
                Parameters
                ----------
                addr : str
                    The inproc url used for monitoring. Passing None as
                    the addr will cause an existing socket monitor to be
                    deregistered.
                events : int [default: zmq.EVENT_ALL]
                    The zmq event bitmask for which events will be sent to the monitor.
        """
        pass

    def recv(self, flags=0, copy=True, track=False): # real signature unknown; restored from __doc__
        """
        s.recv(flags=0, copy=True, track=False)
        
                Receive a message.
        
                With flags=NOBLOCK, this raises :class:`ZMQError` if no messages have
                arrived; otherwise, this waits until a message arrives.
                See :class:`Poller` for more general non-blocking I/O.
        
                Parameters
                ----------
                flags : int
                    0 or NOBLOCK.
                copy : bool
                    Should the message be received in a copying or non-copying manner?
                    If False a Frame object is returned, if True a string copy of
                    message is returned.
                track : bool
                    Should the message be tracked for notification that ZMQ has
                    finished with it? (ignored if copy=True)
        
                Returns
                -------
                msg : bytes or Frame
                    The received message frame.  If `copy` is False, then it will be a Frame,
                    otherwise it will be bytes.
        
                Raises
                ------
                ZMQError
                    for any of the reasons zmq_msg_recv might fail (including if
                    NOBLOCK is set and no new messages have arrived).
        """
        pass

    def send(self, *args, **kwargs): # real signature unknown
        """
        Send a single zmq message frame on this socket.
        
                This queues the message to be sent by the IO thread at a later time.
        
                With flags=NOBLOCK, this raises :class:`ZMQError` if the queue is full;
                otherwise, this waits until space is available.
                See :class:`Poller` for more general non-blocking I/O.
        
                Parameters
                ----------
                data : bytes, Frame, memoryview
                    The content of the message. This can be any object that provides
                    the Python buffer API (`memoryview(data)` can be called).
                flags : int
                    0, NOBLOCK, SNDMORE, or NOBLOCK|SNDMORE.
                copy : bool
                    Should the message be sent in a copying or non-copying manner.
                track : bool
                    Should the message be tracked for notification that ZMQ has
                    finished with it? (ignored if copy=True)
        
                Returns
                -------
                None : if `copy` or not track
                    None if message was sent, raises an exception otherwise.
                MessageTracker : if track and not copy
                    a MessageTracker object, whose `pending` property will
                    be True until the send is completed.
                
                Raises
                ------
                TypeError
                    If a unicode object is passed
                ValueError
                    If `track=True`, but an untracked Frame is passed.
                ZMQError
                    for any of the reasons zmq_msg_send might fail (including
                    if NOBLOCK is set and the outgoing queue is full).
        """
        pass

    def set(self, option, optval): # real signature unknown; restored from __doc__
        """
        s.set(option, optval)
        
                Set socket options.
        
                See the 0MQ API documentation for details on specific options.
        
                Parameters
                ----------
                option : int
                    The option to set.  Available values will depend on your
                    version of libzmq.  Examples include::
        
                        zmq.SUBSCRIBE, UNSUBSCRIBE, IDENTITY, HWM, LINGER, FD
        
                optval : int or bytes
                    The value of the option to set.
        
                Notes
                -----
                .. warning::
        
                    All options other than zmq.SUBSCRIBE, zmq.UNSUBSCRIBE and
                    zmq.LINGER only take effect for subsequent socket bind/connects.
        """
        pass

    def unbind(self, addr): # real signature unknown; restored from __doc__
        """
        s.unbind(addr)
                
                Unbind from an address (undoes a call to bind).
                
                .. versionadded:: libzmq-3.2
                .. versionadded:: 13.0
        
                Parameters
                ----------
                addr : str
                    The address string. This has the form 'protocol://interface:port',
                    for example 'tcp://127.0.0.1:5555'. Protocols supported are
                    tcp, upd, pgm, inproc and ipc. If the address is unicode, it is
                    encoded to utf-8 first.
        """
        pass

    def __init__(self, context, socket_type): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    copy_threshold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    underlying = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The address of the underlying libzmq socket"""

    _closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000018979E19F90>'


class ZMQBindError(__zmq_error.ZMQBaseError):
    """
    An error for ``Socket.bind_to_random_port()``.
        
        See Also
        --------
        .Socket.bind_to_random_port
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


# variables with complex values

__all__ = [
    'Socket',
    'IPC_PATH_MAX_LEN',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000018979F87DA0>'

__spec__ = None # (!) real value is "ModuleSpec(name='zmq.backend.cython.socket', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000018979F87DA0>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\zmq\\\\backend\\\\cython\\\\socket.cp37-win_amd64.pyd')"

__test__ = {}

