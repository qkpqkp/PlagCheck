# encoding: utf-8
# module winpty.cywinpty
# from C:\Users\Doly\Anaconda3\lib\site-packages\winpty\cywinpty.cp37-win_amd64.pyd
# by generator 1.147
""" Cython wrapper around Winpty and Windows functions. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

# Variables with simple values

__path__ = None

# no functions
# classes

class Agent(object):
    """
    This class wraps a winpty agent and offers communication with
        a winpty-agent process.
    """
    def isalive(self, *args, **kwargs): # real signature unknown
        """
        This tests if the pty process is running or not.
                This is non-blocking.
        """
        pass

    def set_size(self, *args, **kwargs): # real signature unknown
        """ Resize the console size of current agent process. """
        pass

    def spawn(self, *args, **kwargs): # real signature unknown
        """ Start a windows process that communicates through a winpty-agent process. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """ Initialize a winpty agent wrapper of size ``(cols, rows)``. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    conin_pipe_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    conout_pipe_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    exitstatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000002692FB67E80>'

__spec__ = None # (!) real value is "ModuleSpec(name='winpty.cywinpty', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000002692FB67E80>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\winpty\\\\cywinpty.cp37-win_amd64.pyd')"

__test__ = {}

