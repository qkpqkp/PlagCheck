# encoding: utf-8
# module py.io
# from C:\Users\Doly\Anaconda3\lib\site-packages\sklearn\ensemble\_hist_gradient_boosting\_gradient_boosting.cp37-win_amd64.pyd
# by generator 1.147
""" input/output helping """

# imports
from _io import BytesIO, TextIO

import py._io.capture as __py__io_capture


# Variables with simple values

_ApiModule__doc = ' input/output helping '

__implprefix__ = 'py'

# functions

def ansi_print(text, esc, file=None, newline=True, flush=False): # reliably restored by inspect
    # no doc
    pass

def dupfile(f, mode=None, buffering=0, raising=False, encoding=None): # reliably restored by inspect
    """
    return a new open file object that's a duplicate of f
    
            mode is duplicated if not given, 'buffering' controls
            buffer size (defaulting to no buffering) and 'raising'
            defines whether an exception is raised when an incompatible
            file object is passed in (if raising is False, the file
            object itself will be returned)
    """
    pass

def get_terminal_width(): # reliably restored by inspect
    # no doc
    pass

def saferepr(obj, maxsize=240): # reliably restored by inspect
    """
    return a size-limited safe repr-string for the given object.
        Failing __repr__ functions of user instances will be represented
        with a short exception info and 'saferepr' generally takes
        care to never raise exceptions itself.  This function is a wrapper
        around the Repr/reprlib functionality of the standard 2.6 lib.
    """
    pass

# classes

class FDCapture(object):
    """ Capture IO to/from a given os-level filedescriptor. """
    def done(self): # reliably restored by inspect
        """ unpatch and clean up, returns the self.tmpfile (file object) """
        pass

    def start(self): # reliably restored by inspect
        # no doc
        pass

    def writeorg(self, data): # reliably restored by inspect
        """ write a string to the original file descriptor """
        pass

    def __init__(self, targetfd, tmpfile=None, now=True, patchsys=False): # reliably restored by inspect
        """
        save targetfd descriptor, and open a new
                    temporary file there.  If no tmpfile is
                    specified a tempfile.Tempfile() will be opened
                    in text mode.
        """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'py._io.capture', '__doc__': ' Capture IO to/from a given os-level filedescriptor. ', '__init__': <function FDCapture.__init__ at 0x000001F5DC2DEF28>, 'start': <function FDCapture.start at 0x000001F5DBD4A268>, 'done': <function FDCapture.done at 0x000001F5DBD4A2F0>, 'writeorg': <function FDCapture.writeorg at 0x000001F5DBD4A378>, '__dict__': <attribute '__dict__' of 'FDCapture' objects>, '__weakref__': <attribute '__weakref__' of 'FDCapture' objects>})"


class StdCapture(__py__io_capture.Capture):
    """
    This class allows to capture writes to sys.stdout|stderr "in-memory"
            and will raise errors on tries to read from sys.stdin. It only
            modifies sys.stdout|stderr|stdin attributes and does not
            touch underlying File Descriptors (use StdCaptureFD for that).
    """
    def done(self, save=True): # reliably restored by inspect
        """ return (outfile, errfile) and stop capturing. """
        pass

    def readouterr(self): # reliably restored by inspect
        """ return snapshot value of stdout/stderr capturings. """
        pass

    def resume(self): # reliably restored by inspect
        """ resume capturing with original temp files. """
        pass

    def startall(self): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, out=True, err=True, in_=True, mixed=False, now=True): # reliably restored by inspect
        # no doc
        pass


class StdCaptureFD(__py__io_capture.Capture):
    """
    This class allows to capture writes to FD1 and FD2
            and may connect a NULL file to FD0 (and prevent
            reads from sys.stdin).  If any of the 0,1,2 file descriptors
            is invalid it will not be captured.
    """
    def done(self, save=True): # reliably restored by inspect
        """ return (outfile, errfile) and stop capturing. """
        pass

    def readouterr(self): # reliably restored by inspect
        """ return snapshot value of stdout/stderr capturings. """
        pass

    def resume(self): # reliably restored by inspect
        """ resume capturing with original temp files. """
        pass

    def startall(self): # reliably restored by inspect
        # no doc
        pass

    def _readsnapshot(self, f): # reliably restored by inspect
        # no doc
        pass

    def _save(self): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, out=True, err=True, mixed=False, in_=True, patchsys=True, now=True): # reliably restored by inspect
        # no doc
        pass


class TerminalWriter(object):
    # no doc
    def line(self, s=None, **kw): # reliably restored by inspect
        # no doc
        pass

    def markup(self, text, **kw): # reliably restored by inspect
        # no doc
        pass

    def reline(self, line, **kw): # reliably restored by inspect
        # no doc
        pass

    def sep(self, sepchar, title=None, fullwidth=None, **kw): # reliably restored by inspect
        # no doc
        pass

    def write(self, msg, **kw): # reliably restored by inspect
        # no doc
        pass

    def _checkfill(self, line): # reliably restored by inspect
        # no doc
        pass

    def _escaped(self, text, esc): # reliably restored by inspect
        # no doc
        pass

    def _update_chars_on_current_line(self, text_or_bytes): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, file=None, stringio=False, encoding=None): # reliably restored by inspect
        # no doc
        pass

    chars_on_current_line = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the number of characters written so far in the current line.

        Please note that this count does not produce correct results after a reline() call,
        see #164.

        .. versionadded:: 1.5.0

        :rtype: int
        """

    fullwidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    width_of_current_line = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return an estimate of the width so far in the current line.

        .. versionadded:: 1.6.0

        :rtype: int
        """

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _esctable = {
        'Black': 40,
        'Blue': 44,
        'Cyan': 46,
        'Green': 42,
        'Purple': 45,
        'Red': 41,
        'White': 47,
        'Yellow': 43,
        'black': 30,
        'blink': 5,
        'blue': 34,
        'bold': 1,
        'cyan': 36,
        'green': 32,
        'invert': 7,
        'light': 2,
        'purple': 35,
        'red': 31,
        'white': 37,
        'yellow': 33,
    }
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'py._io.terminalwriter', '_esctable': {'black': 30, 'red': 31, 'green': 32, 'yellow': 33, 'blue': 34, 'purple': 35, 'cyan': 36, 'white': 37, 'Black': 40, 'Red': 41, 'Green': 42, 'Yellow': 43, 'Blue': 44, 'Purple': 45, 'Cyan': 46, 'White': 47, 'bold': 1, 'light': 2, 'blink': 5, 'invert': 7}, '__init__': <function TerminalWriter.__init__ at 0x000001F5DBD4EB70>, 'fullwidth': <property object at 0x000001F5DC26A728>, 'chars_on_current_line': <property object at 0x000001F5DC26A778>, 'width_of_current_line': <property object at 0x000001F5DB773BD8>, '_escaped': <function TerminalWriter._escaped at 0x000001F5DBD4EE18>, 'markup': <function TerminalWriter.markup at 0x000001F5DBD4EEA0>, 'sep': <function TerminalWriter.sep at 0x000001F5DBD4EF28>, 'write': <function TerminalWriter.write at 0x000001F5DBD4F048>, '_update_chars_on_current_line': <function TerminalWriter._update_chars_on_current_line at 0x000001F5DBD4F0D0>, 'line': <function TerminalWriter.line at 0x000001F5DBD4F158>, 'reline': <function TerminalWriter.reline at 0x000001F5DBD4F1E0>, '_checkfill': <function TerminalWriter._checkfill at 0x000001F5DBD4F268>, '__dict__': <attribute '__dict__' of 'TerminalWriter' objects>, '__weakref__': <attribute '__weakref__' of 'TerminalWriter' objects>, '__doc__': None})"


# variables with complex values

__all__ = [
    '__doc__',
    'dupfile',
    'TextIO',
    'BytesIO',
    'FDCapture',
    'StdCapture',
    'StdCaptureFD',
    'TerminalWriter',
    'ansi_print',
    'get_terminal_width',
    'saferepr',
]

__map__ = {}

