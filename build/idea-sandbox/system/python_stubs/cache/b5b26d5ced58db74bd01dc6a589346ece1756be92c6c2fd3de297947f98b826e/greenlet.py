# encoding: utf-8
# module greenlet
# from C:\Users\Doly\Anaconda3\lib\site-packages\greenlet.cp37-win_amd64.pyd
# by generator 1.147
# no doc
# no imports

# Variables with simple values

GREENLET_USE_GC = True
GREENLET_USE_TRACING = True

__version__ = '0.4.15'

# functions

def getcurrent(*args, **kwargs): # real signature unknown
    pass

def gettrace(*args, **kwargs): # real signature unknown
    pass

def settrace(*args, **kwargs): # real signature unknown
    pass

# classes

class error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class greenlet(object):
    """
    greenlet(run=None, parent=None) -> greenlet
    
    Creates a new greenlet object (without running it).
    
     - *run* -- The callable to invoke.
     - *parent* -- The parent greenlet. The default is the current greenlet.
    """
    def getcurrent(self, *args, **kwargs): # real signature unknown
        pass

    def gettrace(self, *args, **kwargs): # real signature unknown
        pass

    def settrace(self, *args, **kwargs): # real signature unknown
        pass

    def switch(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        switch(*args, **kwargs)
        
        Switch execution to this greenlet.
        
        If this greenlet has never been run, then this greenlet
        will be switched to using the body of self.run(*args, **kwargs).
        
        If the greenlet is active (has been run, but was switch()'ed
        out before leaving its run function), then this greenlet will
        be resumed and the return value to its switch call will be
        None if no arguments are given, the given argument if one
        argument is given, or the args tuple and keyword args dict if
        multiple arguments are given.
        
        If the greenlet is dead, or is the current greenlet then this
        function will simply return the arguments using the same rules as
        above.
        """
        pass

    def throw(self, *args, **kwargs): # real signature unknown
        """
        Switches execution to the greenlet ``g``, but immediately raises the
        given exception in ``g``.  If no argument is provided, the exception
        defaults to ``greenlet.GreenletExit``.  The normal exception
        propagation rules apply, as described above.  Note that calling this
        method is almost equivalent to the following::
        
            def raiser():
                raise typ, val, tb
            g_raiser = greenlet(raiser, parent=g)
            g_raiser.switch()
        
        except that this trick does not work for the
        ``greenlet.GreenletExit`` exception, which would not propagate
        from ``g_raiser`` to ``g``.
        """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, run=None, parent=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    dead = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    gr_frame = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    run = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _stack_saved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    error = error
    GreenletExit = None # (!) forward: GreenletExit, real value is "<class 'greenlet.GreenletExit'>"
    __dict__ = None # (!) real value is "mappingproxy({'__init__': <slot wrapper '__init__' of 'greenlet.greenlet' objects>, '__bool__': <slot wrapper '__bool__' of 'greenlet.greenlet' objects>, '__new__': <built-in method __new__ of type object at 0x00007FFB32027F00>, 'switch': <method 'switch' of 'greenlet.greenlet' objects>, 'throw': <method 'throw' of 'greenlet.greenlet' objects>, '__getstate__': <method '__getstate__' of 'greenlet.greenlet' objects>, '__dict__': <attribute '__dict__' of 'greenlet.greenlet' objects>, 'run': <attribute 'run' of 'greenlet.greenlet' objects>, 'parent': <attribute 'parent' of 'greenlet.greenlet' objects>, 'gr_frame': <attribute 'gr_frame' of 'greenlet.greenlet' objects>, 'dead': <attribute 'dead' of 'greenlet.greenlet' objects>, '_stack_saved': <attribute '_stack_saved' of 'greenlet.greenlet' objects>, '__doc__': 'greenlet(run=None, parent=None) -> greenlet\\n\\nCreates a new greenlet object (without running it).\\n\\n - *run* -- The callable to invoke.\\n - *parent* -- The parent greenlet. The default is the current greenlet.', 'getcurrent': <built-in function getcurrent>, 'error': <class 'greenlet.error'>, 'GreenletExit': <class 'greenlet.GreenletExit'>, 'settrace': <built-in function settrace>, 'gettrace': <built-in function gettrace>})"


class GreenletExit(BaseException):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

_C_API = None # (!) real value is '<capsule object "greenlet._C_API" at 0x00000175CD9C9690>'

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000175CD9D5438>'

__spec__ = None # (!) real value is "ModuleSpec(name='greenlet', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000175CD9D5438>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\greenlet.cp37-win_amd64.pyd')"

