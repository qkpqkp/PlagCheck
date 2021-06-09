# encoding: utf-8
# module py.builtin
# from C:\Users\Doly\Anaconda3\lib\site-packages\sklearn\ensemble\_hist_gradient_boosting\_binning.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as builtins # <module 'builtins' (built-in)>

# Variables with simple values

_ApiModule__doc = None

__implprefix__ = 'py'

# functions

def all(*args, **kwargs): # real signature unknown
    """
    Return True if bool(x) is True for all values x in the iterable.
    
    If the iterable is empty, return True.
    """
    pass

def any(*args, **kwargs): # real signature unknown
    """
    Return True if bool(x) is True for any x in the iterable.
    
    If the iterable is empty, return False.
    """
    pass

def callable(i_e_, some_kind_of_function): # real signature unknown; restored from __doc__
    """
    Return whether the object is callable (i.e., some kind of function).
    
    Note that classes are callable, as are instances of classes with a
    __call__() method.
    """
    pass

def execfile(fn, globs=None, locs=None): # reliably restored by inspect
    # no doc
    pass

def exec_(*args, **kwargs): # real signature unknown
    """
    Execute the given source in the context of globals and locals.
    
    The source may be a string representing one or more Python statements
    or a code object as returned by compile().
    The globals must be a dictionary and locals can be any mapping,
    defaulting to the current globals and locals.
    If only globals is given, locals defaults to it.
    """
    pass

def print_(*args, **kwargs): # real signature unknown
    """
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
    """
    pass

def sorted(*args, **kwargs): # real signature unknown
    """
    Return a new list containing all items from the iterable in ascending order.
    
    A custom key function can be supplied to customize the sort order, and the
    reverse flag can be set to request the result in descending order.
    """
    pass

def _getcode(function): # reliably restored by inspect
    # no doc
    pass

def _getfuncdict(function): # reliably restored by inspect
    # no doc
    pass

def _getimself(function): # reliably restored by inspect
    # no doc
    pass

def _isbytes(x): # reliably restored by inspect
    # no doc
    pass

def _istext(x): # reliably restored by inspect
    # no doc
    pass

def _reraise(cls, val, tb): # reliably restored by inspect
    # no doc
    pass

def _totext(obj, encoding=None, errors=None): # reliably restored by inspect
    # no doc
    pass

def _tryimport(*names): # reliably restored by inspect
    """ return the first successfully imported module. """
    pass

# classes

class BaseException(object):
    """ Common base class for all exceptions """
    def with_traceback(self, tb): # real signature unknown; restored from __doc__
        """
        Exception.with_traceback(tb) --
            set self.__traceback__ to tb and return self.
        """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    args = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __cause__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """exception cause"""

    __context__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """exception context"""

    __suppress_context__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __traceback__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'__repr__': <slot wrapper '__repr__' of 'BaseException' objects>, '__str__': <slot wrapper '__str__' of 'BaseException' objects>, '__getattribute__': <slot wrapper '__getattribute__' of 'BaseException' objects>, '__setattr__': <slot wrapper '__setattr__' of 'BaseException' objects>, '__delattr__': <slot wrapper '__delattr__' of 'BaseException' objects>, '__init__': <slot wrapper '__init__' of 'BaseException' objects>, '__new__': <built-in method __new__ of type object at 0x00007FFB145E0810>, '__reduce__': <method '__reduce__' of 'BaseException' objects>, '__setstate__': <method '__setstate__' of 'BaseException' objects>, 'with_traceback': <method 'with_traceback' of 'BaseException' objects>, '__suppress_context__': <member '__suppress_context__' of 'BaseException' objects>, '__dict__': <attribute '__dict__' of 'BaseException' objects>, 'args': <attribute 'args' of 'BaseException' objects>, '__traceback__': <attribute '__traceback__' of 'BaseException' objects>, '__context__': <attribute '__context__' of 'BaseException' objects>, '__cause__': <attribute '__cause__' of 'BaseException' objects>, '__doc__': 'Common base class for all exceptions'})"


class bytes(object):
    """
    bytes(iterable_of_ints) -> bytes
    bytes(string, encoding[, errors]) -> bytes
    bytes(bytes_or_buffer) -> immutable copy of bytes_or_buffer
    bytes(int) -> bytes object of size given by the parameter initialized with null bytes
    bytes() -> empty bytes object
    
    Construct an immutable array of bytes from:
      - an iterable yielding integers in range(256)
      - a text string encoded using the specified encoding
      - any object implementing the buffer API.
      - an integer
    """
    def capitalize(self): # real signature unknown; restored from __doc__
        """
        B.capitalize() -> copy of B
        
        Return a copy of B with only its first character capitalized (ASCII)
        and the rest lower-cased.
        """
        pass

    def center(self, width, fillchar=None): # real signature unknown; restored from __doc__
        """
        B.center(width[, fillchar]) -> copy of B
        
        Return B centered in a string of length width.  Padding is
        done using the specified fill character (default is a space).
        """
        pass

    def count(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        B.count(sub[, start[, end]]) -> int
        
        Return the number of non-overlapping occurrences of subsection sub in
        bytes B[start:end].  Optional arguments start and end are interpreted
        as in slice notation.
        """
        return 0

    def decode(self, *args, **kwargs): # real signature unknown
        """
        Decode the bytes using the codec registered for encoding.
        
          encoding
            The encoding with which to decode the bytes.
          errors
            The error handling scheme to use for the handling of decoding errors.
            The default is 'strict' meaning that decoding errors raise a
            UnicodeDecodeError. Other possible values are 'ignore' and 'replace'
            as well as any other name registered with codecs.register_error that
            can handle UnicodeDecodeErrors.
        """
        pass

    def endswith(self, suffix, start=None, end=None): # real signature unknown; restored from __doc__
        """
        B.endswith(suffix[, start[, end]]) -> bool
        
        Return True if B ends with the specified suffix, False otherwise.
        With optional start, test B beginning at that position.
        With optional end, stop comparing B at that position.
        suffix can also be a tuple of bytes to try.
        """
        return False

    def expandtabs(self, tabsize=8): # real signature unknown; restored from __doc__
        """
        B.expandtabs(tabsize=8) -> copy of B
        
        Return a copy of B where all tab characters are expanded using spaces.
        If tabsize is not given, a tab size of 8 characters is assumed.
        """
        pass

    def find(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        B.find(sub[, start[, end]]) -> int
        
        Return the lowest index in B where subsection sub is found,
        such that sub is contained within B[start,end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
        """
        return 0

    @classmethod
    def fromhex(cls, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Create a bytes object from a string of hexadecimal numbers.
        
        Spaces between two numbers are accepted.
        Example: bytes.fromhex('B9 01EF') -> b'\\xb9\\x01\\xef'.
        """
        pass

    def hex(self): # real signature unknown; restored from __doc__
        """
        B.hex() -> string
        
        Create a string of hexadecimal numbers from a bytes object.
        Example: b'\xb9\x01\xef'.hex() -> 'b901ef'.
        """
        return ""

    def index(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        B.index(sub[, start[, end]]) -> int
        
        Return the lowest index in B where subsection sub is found,
        such that sub is contained within B[start,end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Raises ValueError when the subsection is not found.
        """
        return 0

    def isalnum(self): # real signature unknown; restored from __doc__
        """
        B.isalnum() -> bool
        
        Return True if all characters in B are alphanumeric
        and there is at least one character in B, False otherwise.
        """
        return False

    def isalpha(self): # real signature unknown; restored from __doc__
        """
        B.isalpha() -> bool
        
        Return True if all characters in B are alphabetic
        and there is at least one character in B, False otherwise.
        """
        return False

    def isascii(self): # real signature unknown; restored from __doc__
        """
        B.isascii() -> bool
        
        Return True if B is empty or all characters in B are ASCII,
        False otherwise.
        """
        return False

    def isdigit(self): # real signature unknown; restored from __doc__
        """
        B.isdigit() -> bool
        
        Return True if all characters in B are digits
        and there is at least one character in B, False otherwise.
        """
        return False

    def islower(self): # real signature unknown; restored from __doc__
        """
        B.islower() -> bool
        
        Return True if all cased characters in B are lowercase and there is
        at least one cased character in B, False otherwise.
        """
        return False

    def isspace(self): # real signature unknown; restored from __doc__
        """
        B.isspace() -> bool
        
        Return True if all characters in B are whitespace
        and there is at least one character in B, False otherwise.
        """
        return False

    def istitle(self): # real signature unknown; restored from __doc__
        """
        B.istitle() -> bool
        
        Return True if B is a titlecased string and there is at least one
        character in B, i.e. uppercase characters may only follow uncased
        characters and lowercase characters only cased ones. Return False
        otherwise.
        """
        return False

    def isupper(self): # real signature unknown; restored from __doc__
        """
        B.isupper() -> bool
        
        Return True if all cased characters in B are uppercase and there is
        at least one cased character in B, False otherwise.
        """
        return False

    def join(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Concatenate any number of bytes objects.
        
        The bytes whose method is called is inserted in between each pair.
        
        The result is returned as a new bytes object.
        
        Example: b'.'.join([b'ab', b'pq', b'rs']) -> b'ab.pq.rs'.
        """
        pass

    def ljust(self, width, fillchar=None): # real signature unknown; restored from __doc__
        """
        B.ljust(width[, fillchar]) -> copy of B
        
        Return B left justified in a string of length width. Padding is
        done using the specified fill character (default is a space).
        """
        pass

    def lower(self): # real signature unknown; restored from __doc__
        """
        B.lower() -> copy of B
        
        Return a copy of B with all ASCII characters converted to lowercase.
        """
        pass

    def lstrip(self, *args, **kwargs): # real signature unknown
        """
        Strip leading bytes contained in the argument.
        
        If the argument is omitted or None, strip leading  ASCII whitespace.
        """
        pass

    def maketrans(self, *args, **kwargs): # real signature unknown
        """
        Return a translation table useable for the bytes or bytearray translate method.
        
        The returned table will be one where each byte in frm is mapped to the byte at
        the same position in to.
        
        The bytes objects frm and to must be of the same length.
        """
        pass

    def partition(self, *args, **kwargs): # real signature unknown
        """
        Partition the bytes into three parts using the given separator.
        
        This will search for the separator sep in the bytes. If the separator is found,
        returns a 3-tuple containing the part before the separator, the separator
        itself, and the part after it.
        
        If the separator is not found, returns a 3-tuple containing the original bytes
        object and two empty bytes objects.
        """
        pass

    def replace(self, *args, **kwargs): # real signature unknown
        """
        Return a copy with all occurrences of substring old replaced by new.
        
          count
            Maximum number of occurrences to replace.
            -1 (the default value) means replace all occurrences.
        
        If the optional argument count is given, only the first count occurrences are
        replaced.
        """
        pass

    def rfind(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        B.rfind(sub[, start[, end]]) -> int
        
        Return the highest index in B where subsection sub is found,
        such that sub is contained within B[start,end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
        """
        return 0

    def rindex(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        B.rindex(sub[, start[, end]]) -> int
        
        Return the highest index in B where subsection sub is found,
        such that sub is contained within B[start,end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Raise ValueError when the subsection is not found.
        """
        return 0

    def rjust(self, width, fillchar=None): # real signature unknown; restored from __doc__
        """
        B.rjust(width[, fillchar]) -> copy of B
        
        Return B right justified in a string of length width. Padding is
        done using the specified fill character (default is a space)
        """
        pass

    def rpartition(self, *args, **kwargs): # real signature unknown
        """
        Partition the bytes into three parts using the given separator.
        
        This will search for the separator sep in the bytes, starting at the end. If
        the separator is found, returns a 3-tuple containing the part before the
        separator, the separator itself, and the part after it.
        
        If the separator is not found, returns a 3-tuple containing two empty bytes
        objects and the original bytes object.
        """
        pass

    def rsplit(self, *args, **kwargs): # real signature unknown
        """
        Return a list of the sections in the bytes, using sep as the delimiter.
        
          sep
            The delimiter according which to split the bytes.
            None (the default value) means split on ASCII whitespace characters
            (space, tab, return, newline, formfeed, vertical tab).
          maxsplit
            Maximum number of splits to do.
            -1 (the default value) means no limit.
        
        Splitting is done starting at the end of the bytes and working to the front.
        """
        pass

    def rstrip(self, *args, **kwargs): # real signature unknown
        """
        Strip trailing bytes contained in the argument.
        
        If the argument is omitted or None, strip trailing ASCII whitespace.
        """
        pass

    def split(self, *args, **kwargs): # real signature unknown
        """
        Return a list of the sections in the bytes, using sep as the delimiter.
        
          sep
            The delimiter according which to split the bytes.
            None (the default value) means split on ASCII whitespace characters
            (space, tab, return, newline, formfeed, vertical tab).
          maxsplit
            Maximum number of splits to do.
            -1 (the default value) means no limit.
        """
        pass

    def splitlines(self, *args, **kwargs): # real signature unknown
        """
        Return a list of the lines in the bytes, breaking at line boundaries.
        
        Line breaks are not included in the resulting list unless keepends is given and
        true.
        """
        pass

    def startswith(self, prefix, start=None, end=None): # real signature unknown; restored from __doc__
        """
        B.startswith(prefix[, start[, end]]) -> bool
        
        Return True if B starts with the specified prefix, False otherwise.
        With optional start, test B beginning at that position.
        With optional end, stop comparing B at that position.
        prefix can also be a tuple of bytes to try.
        """
        return False

    def strip(self, *args, **kwargs): # real signature unknown
        """
        Strip leading and trailing bytes contained in the argument.
        
        If the argument is omitted or None, strip leading and trailing ASCII whitespace.
        """
        pass

    def swapcase(self): # real signature unknown; restored from __doc__
        """
        B.swapcase() -> copy of B
        
        Return a copy of B with uppercase ASCII characters converted
        to lowercase ASCII and vice versa.
        """
        pass

    def title(self): # real signature unknown; restored from __doc__
        """
        B.title() -> copy of B
        
        Return a titlecased version of B, i.e. ASCII words start with uppercase
        characters, all remaining cased characters have lowercase.
        """
        pass

    def translate(self, *args, **kwargs): # real signature unknown
        """
        Return a copy with each character mapped by the given translation table.
        
          table
            Translation table, which must be a bytes object of length 256.
        
        All characters occurring in the optional argument delete are removed.
        The remaining characters are mapped through the given translation table.
        """
        pass

    def upper(self): # real signature unknown; restored from __doc__
        """
        B.upper() -> copy of B
        
        Return a copy of B with all ASCII characters converted to uppercase.
        """
        pass

    def zfill(self, width): # real signature unknown; restored from __doc__
        """
        B.zfill(width) -> copy of B
        
        Pad a numeric string B with zeros on the left, to fill a field
        of the specified width.  B is never truncated.
        """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, iterable_of_ints): # real signature unknown; restored from __doc__
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass


class enumerate(object):
    """
    Return an enumerate object.
    
      iterable
        an object supporting iteration
    
    The enumerate object yields pairs containing a count (from start, which
    defaults to zero) and a value yielded by the iterable argument.
    
    enumerate is useful for obtaining an indexed list:
        (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
    """
    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Implement next(self). """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Return state information for pickling. """
        pass


class frozenset(object):
    """
    frozenset() -> empty frozenset object
    frozenset(iterable) -> frozenset object
    
    Build an immutable unordered collection of unique elements.
    """
    def copy(self, *args, **kwargs): # real signature unknown
        """ Return a shallow copy of a set. """
        pass

    def difference(self, *args, **kwargs): # real signature unknown
        """
        Return the difference of two or more sets as a new set.
        
        (i.e. all elements that are in this set but not the others.)
        """
        pass

    def intersection(self, *args, **kwargs): # real signature unknown
        """
        Return the intersection of two sets as a new set.
        
        (i.e. all elements that are in both sets.)
        """
        pass

    def isdisjoint(self, *args, **kwargs): # real signature unknown
        """ Return True if two sets have a null intersection. """
        pass

    def issubset(self, *args, **kwargs): # real signature unknown
        """ Report whether another set contains this set. """
        pass

    def issuperset(self, *args, **kwargs): # real signature unknown
        """ Report whether this set contains another set. """
        pass

    def symmetric_difference(self, *args, **kwargs): # real signature unknown
        """
        Return the symmetric difference of two sets as a new set.
        
        (i.e. all elements that are in exactly one of the sets.)
        """
        pass

    def union(self, *args, **kwargs): # real signature unknown
        """
        Return the union of sets as a new set.
        
        (i.e. all elements that are in either set.)
        """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __contains__(self, y): # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Return state information for pickling. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __sizeof__(self): # real signature unknown; restored from __doc__
        """ S.__sizeof__() -> size of S in memory, in bytes """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass


class GeneratorExit(BaseException):
    """ Request that a generator exit. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class reversed(object):
    """ Return a reverse iterator over the values of the given sequence. """
    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __length_hint__(self, *args, **kwargs): # real signature unknown
        """ Private method returning an estimate of len(list(it)). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Implement next(self). """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Return state information for pickling. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Set state information for unpickling. """
        pass


class set(object):
    """
    set() -> new empty set object
    set(iterable) -> new set object
    
    Build an unordered collection of unique elements.
    """
    def add(self, *args, **kwargs): # real signature unknown
        """
        Add an element to a set.
        
        This has no effect if the element is already present.
        """
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        """ Remove all elements from this set. """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        """ Return a shallow copy of a set. """
        pass

    def difference(self, *args, **kwargs): # real signature unknown
        """
        Return the difference of two or more sets as a new set.
        
        (i.e. all elements that are in this set but not the others.)
        """
        pass

    def difference_update(self, *args, **kwargs): # real signature unknown
        """ Remove all elements of another set from this set. """
        pass

    def discard(self, *args, **kwargs): # real signature unknown
        """
        Remove an element from a set if it is a member.
        
        If the element is not a member, do nothing.
        """
        pass

    def intersection(self, *args, **kwargs): # real signature unknown
        """
        Return the intersection of two sets as a new set.
        
        (i.e. all elements that are in both sets.)
        """
        pass

    def intersection_update(self, *args, **kwargs): # real signature unknown
        """ Update a set with the intersection of itself and another. """
        pass

    def isdisjoint(self, *args, **kwargs): # real signature unknown
        """ Return True if two sets have a null intersection. """
        pass

    def issubset(self, *args, **kwargs): # real signature unknown
        """ Report whether another set contains this set. """
        pass

    def issuperset(self, *args, **kwargs): # real signature unknown
        """ Report whether this set contains another set. """
        pass

    def pop(self, *args, **kwargs): # real signature unknown
        """
        Remove and return an arbitrary set element.
        Raises KeyError if the set is empty.
        """
        pass

    def remove(self, *args, **kwargs): # real signature unknown
        """
        Remove an element from a set; it must be a member.
        
        If the element is not a member, raise a KeyError.
        """
        pass

    def symmetric_difference(self, *args, **kwargs): # real signature unknown
        """
        Return the symmetric difference of two sets as a new set.
        
        (i.e. all elements that are in exactly one of the sets.)
        """
        pass

    def symmetric_difference_update(self, *args, **kwargs): # real signature unknown
        """ Update a set with the symmetric difference of itself and another. """
        pass

    def union(self, *args, **kwargs): # real signature unknown
        """
        Return the union of sets as a new set.
        
        (i.e. all elements that are in either set.)
        """
        pass

    def update(self, *args, **kwargs): # real signature unknown
        """ Update a set with the union of itself and others. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __contains__(self, y): # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __iand__(self, *args, **kwargs): # real signature unknown
        """ Return self&=value. """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __ior__(self, *args, **kwargs): # real signature unknown
        """ Return self|=value. """
        pass

    def __isub__(self, *args, **kwargs): # real signature unknown
        """ Return self-=value. """
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __ixor__(self, *args, **kwargs): # real signature unknown
        """ Return self^=value. """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Return state information for pickling. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __sizeof__(self): # real signature unknown; restored from __doc__
        """ S.__sizeof__() -> size of S in memory, in bytes """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    __hash__ = None


class _basestring(object):
    """
    str(object='') -> str
    str(bytes_or_buffer[, encoding[, errors]]) -> str
    
    Create a new string object from the given object. If encoding or
    errors is specified, then the object must expose a data buffer
    that will be decoded using the given encoding and error handler.
    Otherwise, returns the result of object.__str__() (if defined)
    or repr(object).
    encoding defaults to sys.getdefaultencoding().
    errors defaults to 'strict'.
    """
    def capitalize(self, *args, **kwargs): # real signature unknown
        """
        Return a capitalized version of the string.
        
        More specifically, make the first character have upper case and the rest lower
        case.
        """
        pass

    def casefold(self, *args, **kwargs): # real signature unknown
        """ Return a version of the string suitable for caseless comparisons. """
        pass

    def center(self, *args, **kwargs): # real signature unknown
        """
        Return a centered string of length width.
        
        Padding is done using the specified fill character (default is a space).
        """
        pass

    def count(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.count(sub[, start[, end]]) -> int
        
        Return the number of non-overlapping occurrences of substring sub in
        string S[start:end].  Optional arguments start and end are
        interpreted as in slice notation.
        """
        return 0

    def encode(self, *args, **kwargs): # real signature unknown
        """
        Encode the string using the codec registered for encoding.
        
          encoding
            The encoding in which to encode the string.
          errors
            The error handling scheme to use for encoding errors.
            The default is 'strict' meaning that encoding errors raise a
            UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
            'xmlcharrefreplace' as well as any other name registered with
            codecs.register_error that can handle UnicodeEncodeErrors.
        """
        pass

    def endswith(self, suffix, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.endswith(suffix[, start[, end]]) -> bool
        
        Return True if S ends with the specified suffix, False otherwise.
        With optional start, test S beginning at that position.
        With optional end, stop comparing S at that position.
        suffix can also be a tuple of strings to try.
        """
        return False

    def expandtabs(self, *args, **kwargs): # real signature unknown
        """
        Return a copy where all tab characters are expanded using spaces.
        
        If tabsize is not given, a tab size of 8 characters is assumed.
        """
        pass

    def find(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.find(sub[, start[, end]]) -> int
        
        Return the lowest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
        """
        return 0

    def format(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        S.format(*args, **kwargs) -> str
        
        Return a formatted version of S, using substitutions from args and kwargs.
        The substitutions are identified by braces ('{' and '}').
        """
        return ""

    def format_map(self, mapping): # real signature unknown; restored from __doc__
        """
        S.format_map(mapping) -> str
        
        Return a formatted version of S, using substitutions from mapping.
        The substitutions are identified by braces ('{' and '}').
        """
        return ""

    def index(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.index(sub[, start[, end]]) -> int
        
        Return the lowest index in S where substring sub is found, 
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Raises ValueError when the substring is not found.
        """
        return 0

    def isalnum(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is an alpha-numeric string, False otherwise.
        
        A string is alpha-numeric if all characters in the string are alpha-numeric and
        there is at least one character in the string.
        """
        pass

    def isalpha(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is an alphabetic string, False otherwise.
        
        A string is alphabetic if all characters in the string are alphabetic and there
        is at least one character in the string.
        """
        pass

    def isascii(self, *args, **kwargs): # real signature unknown
        """
        Return True if all characters in the string are ASCII, False otherwise.
        
        ASCII characters have code points in the range U+0000-U+007F.
        Empty string is ASCII too.
        """
        pass

    def isdecimal(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is a decimal string, False otherwise.
        
        A string is a decimal string if all characters in the string are decimal and
        there is at least one character in the string.
        """
        pass

    def isdigit(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is a digit string, False otherwise.
        
        A string is a digit string if all characters in the string are digits and there
        is at least one character in the string.
        """
        pass

    def isidentifier(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is a valid Python identifier, False otherwise.
        
        Use keyword.iskeyword() to test for reserved identifiers such as "def" and
        "class".
        """
        pass

    def islower(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is a lowercase string, False otherwise.
        
        A string is lowercase if all cased characters in the string are lowercase and
        there is at least one cased character in the string.
        """
        pass

    def isnumeric(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is a numeric string, False otherwise.
        
        A string is numeric if all characters in the string are numeric and there is at
        least one character in the string.
        """
        pass

    def isprintable(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is printable, False otherwise.
        
        A string is printable if all of its characters are considered printable in
        repr() or if it is empty.
        """
        pass

    def isspace(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is a whitespace string, False otherwise.
        
        A string is whitespace if all characters in the string are whitespace and there
        is at least one character in the string.
        """
        pass

    def istitle(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is a title-cased string, False otherwise.
        
        In a title-cased string, upper- and title-case characters may only
        follow uncased characters and lowercase characters only cased ones.
        """
        pass

    def isupper(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is an uppercase string, False otherwise.
        
        A string is uppercase if all cased characters in the string are uppercase and
        there is at least one cased character in the string.
        """
        pass

    def join(self, ab=None, pq=None, rs=None): # real signature unknown; restored from __doc__
        """
        Concatenate any number of strings.
        
        The string whose method is called is inserted in between each given string.
        The result is returned as a new string.
        
        Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
        """
        pass

    def ljust(self, *args, **kwargs): # real signature unknown
        """
        Return a left-justified string of length width.
        
        Padding is done using the specified fill character (default is a space).
        """
        pass

    def lower(self, *args, **kwargs): # real signature unknown
        """ Return a copy of the string converted to lowercase. """
        pass

    def lstrip(self, *args, **kwargs): # real signature unknown
        """
        Return a copy of the string with leading whitespace removed.
        
        If chars is given and not None, remove characters in chars instead.
        """
        pass

    def maketrans(self, *args, **kwargs): # real signature unknown
        """
        Return a translation table usable for str.translate().
        
        If there is only one argument, it must be a dictionary mapping Unicode
        ordinals (integers) or characters to Unicode ordinals, strings or None.
        Character keys will be then converted to ordinals.
        If there are two arguments, they must be strings of equal length, and
        in the resulting dictionary, each character in x will be mapped to the
        character at the same position in y. If there is a third argument, it
        must be a string, whose characters will be mapped to None in the result.
        """
        pass

    def partition(self, *args, **kwargs): # real signature unknown
        """
        Partition the string into three parts using the given separator.
        
        This will search for the separator in the string.  If the separator is found,
        returns a 3-tuple containing the part before the separator, the separator
        itself, and the part after it.
        
        If the separator is not found, returns a 3-tuple containing the original string
        and two empty strings.
        """
        pass

    def replace(self, *args, **kwargs): # real signature unknown
        """
        Return a copy with all occurrences of substring old replaced by new.
        
          count
            Maximum number of occurrences to replace.
            -1 (the default value) means replace all occurrences.
        
        If the optional argument count is given, only the first count occurrences are
        replaced.
        """
        pass

    def rfind(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.rfind(sub[, start[, end]]) -> int
        
        Return the highest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
        """
        return 0

    def rindex(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.rindex(sub[, start[, end]]) -> int
        
        Return the highest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Raises ValueError when the substring is not found.
        """
        return 0

    def rjust(self, *args, **kwargs): # real signature unknown
        """
        Return a right-justified string of length width.
        
        Padding is done using the specified fill character (default is a space).
        """
        pass

    def rpartition(self, *args, **kwargs): # real signature unknown
        """
        Partition the string into three parts using the given separator.
        
        This will search for the separator in the string, starting at the end. If
        the separator is found, returns a 3-tuple containing the part before the
        separator, the separator itself, and the part after it.
        
        If the separator is not found, returns a 3-tuple containing two empty strings
        and the original string.
        """
        pass

    def rsplit(self, *args, **kwargs): # real signature unknown
        """
        Return a list of the words in the string, using sep as the delimiter string.
        
          sep
            The delimiter according which to split the string.
            None (the default value) means split according to any whitespace,
            and discard empty strings from the result.
          maxsplit
            Maximum number of splits to do.
            -1 (the default value) means no limit.
        
        Splits are done starting at the end of the string and working to the front.
        """
        pass

    def rstrip(self, *args, **kwargs): # real signature unknown
        """
        Return a copy of the string with trailing whitespace removed.
        
        If chars is given and not None, remove characters in chars instead.
        """
        pass

    def split(self, *args, **kwargs): # real signature unknown
        """
        Return a list of the words in the string, using sep as the delimiter string.
        
          sep
            The delimiter according which to split the string.
            None (the default value) means split according to any whitespace,
            and discard empty strings from the result.
          maxsplit
            Maximum number of splits to do.
            -1 (the default value) means no limit.
        """
        pass

    def splitlines(self, *args, **kwargs): # real signature unknown
        """
        Return a list of the lines in the string, breaking at line boundaries.
        
        Line breaks are not included in the resulting list unless keepends is given and
        true.
        """
        pass

    def startswith(self, prefix, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.startswith(prefix[, start[, end]]) -> bool
        
        Return True if S starts with the specified prefix, False otherwise.
        With optional start, test S beginning at that position.
        With optional end, stop comparing S at that position.
        prefix can also be a tuple of strings to try.
        """
        return False

    def strip(self, *args, **kwargs): # real signature unknown
        """
        Return a copy of the string with leading and trailing whitespace remove.
        
        If chars is given and not None, remove characters in chars instead.
        """
        pass

    def swapcase(self, *args, **kwargs): # real signature unknown
        """ Convert uppercase characters to lowercase and lowercase characters to uppercase. """
        pass

    def title(self, *args, **kwargs): # real signature unknown
        """
        Return a version of the string where each word is titlecased.
        
        More specifically, words start with uppercased characters and all remaining
        cased characters have lower case.
        """
        pass

    def translate(self, *args, **kwargs): # real signature unknown
        """
        Replace each character in the string using the given translation table.
        
          table
            Translation table, which must be a mapping of Unicode ordinals to
            Unicode ordinals, strings, or None.
        
        The table must implement lookup/indexing via __getitem__, for instance a
        dictionary or list.  If this operation raises LookupError, the character is
        left untouched.  Characters mapped to None are deleted.
        """
        pass

    def upper(self, *args, **kwargs): # real signature unknown
        """ Return a copy of the string converted to uppercase. """
        pass

    def zfill(self, *args, **kwargs): # real signature unknown
        """
        Pad a numeric string with zeros on the left, to fill a field of the given width.
        
        The string is never truncated.
        """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ Return a formatted version of the string as described by format_spec. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Return the size of the string in memory, in bytes. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass


text = _basestring


# variables with complex values

_sysex = (
    KeyboardInterrupt,
    SystemExit,
    MemoryError,
    GeneratorExit,
)

__all__ = [
    '__doc__',
    'enumerate',
    'reversed',
    'sorted',
    'any',
    'all',
    'set',
    'frozenset',
    'BaseException',
    'GeneratorExit',
    '_sysex',
    'print_',
    '_reraise',
    '_tryimport',
    'exec_',
    '_basestring',
    '_totext',
    '_isbytes',
    '_istext',
    '_getimself',
    '_getfuncdict',
    '_getcode',
    'builtins',
    'execfile',
    'callable',
    'bytes',
    'text',
]

__map__ = {}

