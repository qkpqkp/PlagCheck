# encoding: utf-8
# module py.code
# from C:\Users\Doly\Anaconda3\lib\site-packages\sklearn\decomposition\cdnmf_fast.cp37-win_amd64.pyd
# by generator 1.147
""" python inspection/code generation API """
# no imports

# Variables with simple values

_ApiModule__doc = ' python inspection/code generation API '

_reinterpret_old = 'old reinterpretation not available for py3'

_reprcompare = None

__implprefix__ = 'py'

# functions

def compile(source, filename=None, mode=None, flags=0, dont_inherit=0): # reliably restored by inspect
    """
    compile the given source to a raw code object,
            and maintain an internal cache which allows later
            retrieval of the source code for the code object
            and any recursively created code objects.
    """
    pass

def getfslineno(obj): # reliably restored by inspect
    """
    Return source location (path, lineno) for the given object.
        If the source cannot be determined return ("", -1)
    """
    pass

def getrawcode(obj, trycall=True): # reliably restored by inspect
    """ return code object for given function. """
    pass

def patch_builtins(assertion=True, compile=True): # reliably restored by inspect
    """ put compile and AssertionError builtins to Python's builtins. """
    pass

def unpatch_builtins(assertion=True, compile=True): # reliably restored by inspect
    """ remove compile and AssertionError builtins from Python builtins. """
    pass

def _format_explanation(explanation): # reliably restored by inspect
    """
    This formats an explanation
    
        Normally all embedded newlines are escaped, however there are
        three exceptions: 
    {, 
    } and 
    ~.  The first two are intended
        cover nested explanations, see function and attribute explanations
        for examples (.visit_Call(), visit_Attribute()).  The last one is
        for when one explanation needs to span multiple lines, e.g. when
        displaying diffs.
    """
    pass

def _reinterpret(source, frame, should_fail=False): # reliably restored by inspect
    # no doc
    pass

# classes

class Code(object):
    """ wrapper around Python code objects """
    def getargs(self, var=False): # reliably restored by inspect
        """
        return a tuple with the argument names for the code object
        
                    if 'var' is set True also return the names of the variable and
                    keyword arguments when present
        """
        pass

    def source(self): # reliably restored by inspect
        """ return a py.code.Source object for the code object's source only """
        pass

    def __eq__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, rawcode): # reliably restored by inspect
        # no doc
        pass

    def __ne__(self, other): # reliably restored by inspect
        # no doc
        pass

    fullsource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ return a py.code.Source object for the full source file of the code
        """

    path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ return a path object pointing to source code (note that it
        might not point to an actually existing file). """

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'py._code.code', '__doc__': ' wrapper around Python code objects ', '__init__': <function Code.__init__ at 0x0000023A846E6C80>, '__eq__': <function Code.__eq__ at 0x0000023A846E6D08>, '__ne__': <function Code.__ne__ at 0x0000023A846E6D90>, 'path': <property object at 0x0000023A846F2368>, 'fullsource': <property object at 0x0000023A846F23B8>, 'source': <function Code.source at 0x0000023A846E6F28>, 'getargs': <function Code.getargs at 0x0000023A846FA048>, '__dict__': <attribute '__dict__' of 'Code' objects>, '__weakref__': <attribute '__weakref__' of 'Code' objects>, '__hash__': None})"
    __hash__ = None


class ExceptionInfo(object):
    """
    wraps sys.exc_info() objects and offers
            help for navigating the traceback.
    """
    def errisinstance(self, exc): # reliably restored by inspect
        """ return True if the exception is an instance of exc """
        pass

    def exconly(self, tryshort=False): # reliably restored by inspect
        """
        return the exception as a string
        
                    when 'tryshort' resolves to True, and the exception is a
                    py.code._AssertionError, only the actual exception part of
                    the exception representation is returned (so 'AssertionError: ' is
                    removed from the beginning)
        """
        pass

    def getrepr(self, showlocals=False, style=None, abspath=False, tbfilter=True, funcargs=False): # reliably restored by inspect
        """
        return str()able representation of this exception info.
                    showlocals: show locals per traceback entry
                    style: long|short|no|native traceback style
                    tbfilter: hide entries (where __tracebackhide__ is true)
        
                    in case of style==native, tbfilter and showlocals is ignored.
        """
        pass

    def _getreprcrash(self): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, tup=None, exprinfo=None): # reliably restored by inspect
        # no doc
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    def __str__(self): # reliably restored by inspect
        # no doc
        pass

    def __unicode__(self): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _striptext = ''
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'py._code.code', '__doc__': ' wraps sys.exc_info() objects and offers\\n        help for navigating the traceback.\\n    ', '_striptext': '', '__init__': <function ExceptionInfo.__init__ at 0x0000023A846FB048>, '__repr__': <function ExceptionInfo.__repr__ at 0x0000023A846FB0D0>, 'exconly': <function ExceptionInfo.exconly at 0x0000023A846FB158>, 'errisinstance': <function ExceptionInfo.errisinstance at 0x0000023A846FB1E0>, '_getreprcrash': <function ExceptionInfo._getreprcrash at 0x0000023A846FB268>, 'getrepr': <function ExceptionInfo.getrepr at 0x0000023A846FB2F0>, '__str__': <function ExceptionInfo.__str__ at 0x0000023A846FB378>, '__unicode__': <function ExceptionInfo.__unicode__ at 0x0000023A846FB400>, '__dict__': <attribute '__dict__' of 'ExceptionInfo' objects>, '__weakref__': <attribute '__weakref__' of 'ExceptionInfo' objects>})"


class Frame(object):
    """
    Wrapper around a Python frame holding f_locals and f_globals
        in which expressions can be evaluated.
    """
    def eval(self, code, **vars): # reliably restored by inspect
        """
        evaluate 'code' in the frame
        
                    'vars' are optional additional local variables
        
                    returns the result of the evaluation
        """
        pass

    def exec_(self, code, **vars): # reliably restored by inspect
        """
        exec 'code' in the frame
        
                    'vars' are optiona; additional local variables
        """
        pass

    def getargs(self, var=False): # reliably restored by inspect
        """
        return a list of tuples (name, value) for all arguments
        
                    if 'var' is set True also include the variable and keyword
                    arguments when present
        """
        pass

    def is_true(self, object): # reliably restored by inspect
        # no doc
        pass

    def repr(self, object): # reliably restored by inspect
        """ return a 'safe' (non-recursive, one-line) string repr for 'object' """
        pass

    def __init__(self, frame): # reliably restored by inspect
        # no doc
        pass

    statement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ statement this frame is at """

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'py._code.code', '__doc__': 'Wrapper around a Python frame holding f_locals and f_globals\\n    in which expressions can be evaluated.', '__init__': <function Frame.__init__ at 0x0000023A846FA0D0>, 'statement': <property object at 0x0000023A846F2548>, 'eval': <function Frame.eval at 0x0000023A846FA1E0>, 'exec_': <function Frame.exec_ at 0x0000023A846FA268>, 'repr': <function Frame.repr at 0x0000023A846FA2F0>, 'is_true': <function Frame.is_true at 0x0000023A846FA378>, 'getargs': <function Frame.getargs at 0x0000023A846FA400>, '__dict__': <attribute '__dict__' of 'Frame' objects>, '__weakref__': <attribute '__weakref__' of 'Frame' objects>})"


class Source(object):
    """
    a immutable object holding a source code fragment,
            possibly deindenting it.
    """
    def compile(self, filename=None, mode=None, flag=0, dont_inherit=0, _genframe=None): # reliably restored by inspect
        """
        return compiled code object. if filename is None
                    invent an artificial filename which displays
                    the source/line position of the caller frame.
        """
        pass

    def deindent(self, offset=None): # reliably restored by inspect
        """
        return a new source object deindented by offset.
                    If offset is None then guess an indentation offset from
                    the first non-blank line.  Subsequent lines which have a
                    lower indentation offset will be copied verbatim as
                    they are assumed to be part of multilines.
        """
        pass

    def getstatement(self, lineno, assertion=False): # reliably restored by inspect
        """
        return Source statement which contains the
                    given linenumber (counted from 0).
        """
        pass

    def getstatementrange(self, lineno, assertion=False): # reliably restored by inspect
        """
        return (start, end) tuple which spans the minimal
                    statement region which containing the given lineno.
        """
        pass

    def indent(self, indent=None): # reliably restored by inspect
        """
        return a copy of the source object with
                    all lines indented by the given indent-string.
        """
        pass

    def isparseable(self, deindent=True): # reliably restored by inspect
        """
        return True if source is parseable, heuristically
                    deindenting it by default.
        """
        pass

    def putaround(self, before=None, after=None, indent=None): # reliably restored by inspect
        """
        return a copy of the source object with
                    'before' and 'after' wrapped around it.
        """
        pass

    def strip(self): # reliably restored by inspect
        """
        return new source object with trailing
                    and leading blank lines removed.
        """
        pass

    def __eq__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __getitem__(self, key): # reliably restored by inspect
        # no doc
        pass

    def __getslice__(self, start, end): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, *parts, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def __len__(self): # reliably restored by inspect
        # no doc
        pass

    def __str__(self): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _compilecounter = 0
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'py._code.source', '__doc__': ' a immutable object holding a source code fragment,\\n        possibly deindenting it.\\n    ', '_compilecounter': 0, '__init__': <function Source.__init__ at 0x0000023A843507B8>, '__eq__': <function Source.__eq__ at 0x0000023A843509D8>, '__getitem__': <function Source.__getitem__ at 0x0000023A84350950>, '__len__': <function Source.__len__ at 0x0000023A843508C8>, '__getslice__': <function Source.__getslice__ at 0x0000023A84350AE8>, 'strip': <function Source.strip at 0x0000023A84350B70>, 'putaround': <function Source.putaround at 0x0000023A84350A60>, 'indent': <function Source.indent at 0x0000023A84350BF8>, 'getstatement': <function Source.getstatement at 0x0000023A84350C80>, 'getstatementrange': <function Source.getstatementrange at 0x0000023A84350D08>, 'deindent': <function Source.deindent at 0x0000023A84350D90>, 'isparseable': <function Source.isparseable at 0x0000023A84350E18>, '__str__': <function Source.__str__ at 0x0000023A84350EA0>, 'compile': <function Source.compile at 0x0000023A84350F28>, '__dict__': <attribute '__dict__' of 'Source' objects>, '__weakref__': <attribute '__weakref__' of 'Source' objects>, '__hash__': None})"
    __hash__ = None


class Traceback(list):
    """
    Traceback objects encapsulate and offer higher level
            access to Traceback entries.
    """
    def cut(self, path=None, lineno=None, firstlineno=None, excludepath=None): # reliably restored by inspect
        """
        return a Traceback instance wrapping part of this Traceback
        
                    by provding any combination of path, lineno and firstlineno, the
                    first frame to start the to-be-returned traceback is determined
        
                    this allows cutting the first part of a Traceback instance e.g.
                    for formatting reasons (removing some uninteresting bits that deal
                    with handling of the exception/traceback)
        """
        pass

    def filter(self, fn='<function Traceback.<lambda> at 0x0000023A846FAD90>'): # reliably restored by inspect
        """
        return a Traceback instance with certain items removed
        
                    fn is a function that gets a single argument, a TracebackItem
                    instance, and should return True when the item should be added
                    to the Traceback, False when not
        
                    by default this removes all the TracebackItems which are hidden
                    (see ishidden() above)
        """
        pass

    def getcrashentry(self): # reliably restored by inspect
        """
        return last non-hidden traceback entry that lead
                to the exception of a traceback.
        """
        pass

    def recursionindex(self): # reliably restored by inspect
        """
        return the index of the frame/TracebackItem where recursion
                    originates if appropriate, None if no recursion occurred
        """
        pass

    def __getitem__(self, key): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, tb): # reliably restored by inspect
        """ initialize from given python traceback object. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Entry = None # (!) real value is "<class 'py._code.code.TracebackEntry'>"
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'py._code.code', '__doc__': ' Traceback objects encapsulate and offer higher level\\n        access to Traceback entries.\\n    ', 'Entry': <class 'py._code.code.TracebackEntry'>, '__init__': <function Traceback.__init__ at 0x0000023A846FABF8>, 'cut': <function Traceback.cut at 0x0000023A846FAC80>, '__getitem__': <function Traceback.__getitem__ at 0x0000023A846FAD08>, 'filter': <function Traceback.filter at 0x0000023A846FAE18>, 'getcrashentry': <function Traceback.getcrashentry at 0x0000023A846FAEA0>, 'recursionindex': <function Traceback.recursionindex at 0x0000023A846FAF28>, '__dict__': <attribute '__dict__' of 'Traceback' objects>, '__weakref__': <attribute '__weakref__' of 'Traceback' objects>})"


class _AssertionError(AssertionError):
    # no doc
    def __init__(self, *args): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__all__ = [
    '__doc__',
    'compile',
    'Source',
    'Code',
    'Frame',
    'ExceptionInfo',
    'Traceback',
    'getfslineno',
    'getrawcode',
    'patch_builtins',
    'unpatch_builtins',
    '_AssertionError',
    '_reinterpret_old',
    '_reinterpret',
    '_reprcompare',
    '_format_explanation',
]

__map__ = {}

