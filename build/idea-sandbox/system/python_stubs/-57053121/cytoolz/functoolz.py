# encoding: utf-8
# module cytoolz.functoolz
# from C:\Users\Doly\Anaconda3\lib\site-packages\cytoolz\functoolz.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import inspect as inspect # C:\Users\Doly\Anaconda3\lib\inspect.py
import sys as sys # <module 'sys' (built-in)>
import cytoolz._signatures as _sigs # C:\Users\Doly\Anaconda3\lib\site-packages\cytoolz\_signatures.py
from _functools import reduce


# Variables with simple values

no_default = '__no__default__'

PY3 = True
PY34 = False

# functions

def apply(*func_and_args, **kwargs): # real signature unknown; restored from __doc__
    """
    apply(*func_and_args, **kwargs)
    
        Applies a function and returns the results
    
        >>> def double(x): return 2*x
        >>> def inc(x):    return x + 1
        >>> apply(double, 5)
        10
    
        >>> tuple(map(apply, [double, inc, double], [10, 500, 8000]))
        (20, 501, 16000)
    """
    pass

def compose(*funcs): # real signature unknown; restored from __doc__
    """
    compose(*funcs)
    
        Compose functions to operate in series.
    
        Returns a function that applies other functions in sequence.
    
        Functions are applied from right to left so that
        ``compose(f, g, h)(x, y)`` is the same as ``f(g(h(x, y)))``.
    
        If no arguments are provided, the identity function (f(x) = x) is returned.
    
        >>> inc = lambda i: i + 1
        >>> compose(str, inc)(3)
        '4'
    
        See Also:
            compose_left
            pipe
    """
    pass

def compose_left(*funcs): # real signature unknown; restored from __doc__
    """
    compose_left(*funcs)
    
        Compose functions to operate in series.
    
        Returns a function that applies other functions in sequence.
    
        Functions are applied from left to right so that
        ``compose_left(f, g, h)(x, y)`` is the same as ``h(g(f(x, y)))``.
    
        If no arguments are provided, the identity function (f(x) = x) is returned.
    
        >>> inc = lambda i: i + 1
        >>> compose_left(inc, str)(3)
        '4'
    
        See Also:
            compose
            pipe
    """
    pass

def dedent(text): # reliably restored by inspect
    """
    Remove any common leading whitespace from every line in `text`.
    
        This can be used to make triple-quoted strings line up with the left
        edge of the display, while still presenting them in the source code
        in indented form.
    
        Note that tabs and spaces are both treated as whitespace, but they
        are not equal: the lines "  hello" and "\thello" are
        considered to have no common leading whitespace.  (This behaviour is
        new in Python 2.5; older versions of this module incorrectly
        expanded tabs before searching for common leading whitespace.)
    """
    pass

def do(func, x): # real signature unknown; restored from __doc__
    """
    do(func, x)
    
        Runs ``func`` on ``x``, returns ``x``
    
        Because the results of ``func`` are not returned, only the side
        effects of ``func`` are relevant.
    
        Logging functions can be made by composing ``do`` with a storage function
        like ``list.append`` or ``file.write``
    
        >>> from cytoolz import compose
        >>> from cytoolz.curried import do
    
        >>> log = []
        >>> inc = lambda x: x + 1
        >>> inc = compose(inc, do(log.append))
        >>> inc(1)
        2
        >>> inc(11)
        12
        >>> log
        [1, 11]
    """
    pass

def flip(func, a, b): # real signature unknown; restored from __doc__
    """
    flip(func, a, b)
    
        Call the function call with the arguments flipped
    
        This function is curried.
    
        >>> def div(a, b):
        ...     return a // b
        ...
        >>> flip(div, 2, 6)
        3
        >>> div_by_two = flip(div, 2)
        >>> div_by_two(4)
        2
    
        This is particularly useful for built in functions and functions defined
        in C extensions that accept positional only arguments. For example:
        isinstance, issubclass.
    
        >>> data = [1, 'a', 'b', 2, 1.5, object(), 3]
        >>> only_ints = list(filter(flip(isinstance, int), data))
        >>> only_ints
        [1, 2, 3]
    """
    pass

def has_keywords(func, sigspec=None): # reliably restored by inspect
    """
    Does a function have keyword arguments?
    
        This function relies on introspection and does not call the function.
        Returns None if validity can't be determined.
    
        >>> def f(x, y=0):
        ...     return x + y
    
        >>> has_keywords(f)
        True
    """
    pass

def has_varargs(func, sigspec=None): # reliably restored by inspect
    """
    Does a function have variadic positional arguments?
    
        This function relies on introspection and does not call the function.
        Returns None if validity can't be determined.
    
        >>> def f(*args):
        ...    return args
        >>> has_varargs(f)
        True
        >>> def g(**kwargs):
        ...    return kwargs
        >>> has_varargs(g)
        False
    """
    pass

def identity(x): # real signature unknown; restored from __doc__
    """ identity(x) """
    pass

def import_module(name, package=None): # reliably restored by inspect
    """
    Import a module.
    
        The 'package' argument is required when performing a relative import. It
        specifies the package to use as the anchor point from which to resolve the
        relative import to an absolute import.
    """
    pass

def instanceproperty(fget=None, fset=None, fdel=None, doc=None, classval=None): # reliably restored by inspect
    """
    Like @property, but returns ``classval`` when used as a class attribute
    
        >>> class MyClass(object):
        ...     '''The class docstring'''
        ...     @instanceproperty(classval=__doc__)
        ...     def __doc__(self):
        ...         return 'An object docstring'
        ...     @instanceproperty
        ...     def val(self):
        ...         return 42
        ...
        >>> MyClass.__doc__
        'The class docstring'
        >>> MyClass.val is None
        True
        >>> obj = MyClass()
        >>> obj.__doc__
        'An object docstring'
        >>> obj.val
        42
    """
    pass

def is_arity(n, func, sigspec=None): # reliably restored by inspect
    """
    Does a function have only n positional arguments?
    
        This function relies on introspection and does not call the function.
        Returns None if validity can't be determined.
    
        >>> def f(x):
        ...     return x
        >>> is_arity(1, f)
        True
        >>> def g(x, y=1):
        ...     return x + y
        >>> is_arity(1, g)
        False
    """
    pass

def is_partial_args(func, args, kwargs, sigspec=None): # reliably restored by inspect
    """
    Can partial(func, *args, **kwargs)(*args2, **kwargs2) be a valid call?
    
        Returns True *only* if the call is valid or if it is possible for the
        call to become valid by adding more positional or keyword arguments.
    
        This function relies on introspection and does not call the function.
        Returns None if validity can't be determined.
    
        >>> def add(x, y):
        ...     return x + y
    
        >>> is_partial_args(add, (1,), {})
        True
        >>> is_partial_args(add, (1, 2), {})
        True
        >>> is_partial_args(add, (1, 2, 3), {})
        False
        >>> is_partial_args(map, (), {})
        True
    
        **Implementation notes**
        Python 2 relies on ``inspect.getargspec``, which only works for
        user-defined functions.  Python 3 uses ``inspect.signature``, which
        works for many more types of callables.
    
        Many builtins in the standard library are also supported.
    """
    pass

def is_valid_args(func, args, kwargs, sigspec=None): # reliably restored by inspect
    """
    Is ``func(*args, **kwargs)`` a valid function call?
    
        This function relies on introspection and does not call the function.
        Returns None if validity can't be determined.
    
        >>> def add(x, y):
        ...     return x + y
    
        >>> is_valid_args(add, (1,), {})
        False
        >>> is_valid_args(add, (1, 2), {})
        True
        >>> is_valid_args(map, (), {})
        False
    
        **Implementation notes**
        Python 2 relies on ``inspect.getargspec``, which only works for
        user-defined functions.  Python 3 uses ``inspect.signature``, which
        works for many more types of callables.
    
        Many builtins in the standard library are also supported.
    """
    pass

def juxt(*funcs): # real signature unknown; restored from __doc__
    """
    juxt(*funcs)
    
        Creates a function that calls several functions with the same arguments
    
        Takes several functions and returns a function that applies its arguments
        to each of those functions then returns a tuple of the results.
    
        Name comes from juxtaposition: the fact of two things being seen or placed
        close together with contrasting effect.
    
        >>> inc = lambda x: x + 1
        >>> double = lambda x: x * 2
        >>> juxt(inc, double)(10)
        (11, 20)
        >>> juxt([inc, double])(10)
        (11, 20)
    """
    pass

def memoize(func, cache=None, key=None): # real signature unknown; restored from __doc__
    """
    memoize(func, cache=None, key=None)
    
        Cache a function's result for speedy future evaluation
    
        Considerations:
            Trades memory for speed.
            Only use on pure functions.
    
        >>> def add(x, y):  return x + y
        >>> add = memoize(add)
    
        Or use as a decorator
    
        >>> @memoize
        ... def add(x, y):
        ...     return x + y
    
        Use the ``cache`` keyword to provide a dict-like object as an initial cache
    
        >>> @memoize(cache={(1, 2): 3})
        ... def add(x, y):
        ...     return x + y
    
        Note that the above works as a decorator because ``memoize`` is curried.
    
        It is also possible to provide a ``key(args, kwargs)`` function that
        calculates keys used for the cache, which receives an ``args`` tuple and
        ``kwargs`` dict as input, and must return a hashable value.  However,
        the default key function should be sufficient most of the time.
    
        >>> # Use key function that ignores extraneous keyword arguments
        >>> @memoize(key=lambda args, kwargs: args)
        ... def add(x, y, verbose=False):
        ...     if verbose:
        ...         print('Calculating %s + %s' % (x, y))
        ...     return x + y
    """
    pass

def num_required_args(func, sigspec=None): # reliably restored by inspect
    """
    Number of required positional arguments
    
        This function relies on introspection and does not call the function.
        Returns None if validity can't be determined.
    
        >>> def f(x, y, z=3):
        ...     return x + y + z
        >>> num_required_args(f)
        2
        >>> def g(*args, **kwargs):
        ...     pass
        >>> num_required_args(g)
        0
    """
    pass

def pipe(data, *funcs): # real signature unknown; restored from __doc__
    """
    pipe(data, *funcs)
    
        Pipe a value through a sequence of functions
    
        I.e. ``pipe(data, f, g, h)`` is equivalent to ``h(g(f(data)))``
    
        We think of the value as progressing through a pipe of several
        transformations, much like pipes in UNIX
    
        ``$ cat data | f | g | h``
    
        >>> double = lambda i: 2 * i
        >>> pipe(3, double, str)
        '6'
    
        See Also:
            compose
            compose_left
            thread_first
            thread_last
    """
    pass

def return_none(exc): # real signature unknown; restored from __doc__
    """
    return_none(exc)
    
        Returns None.
    """
    pass

def thread_first(val, *forms): # real signature unknown; restored from __doc__
    """
    thread_first(val, *forms)
    
        Thread value through a sequence of functions/forms
    
        >>> def double(x): return 2*x
        >>> def inc(x):    return x + 1
        >>> thread_first(1, inc, double)
        4
    
        If the function expects more than one input you can specify those inputs
        in a tuple.  The value is used as the first input.
    
        >>> def add(x, y): return x + y
        >>> def pow(x, y): return x**y
        >>> thread_first(1, (add, 4), (pow, 2))  # pow(add(1, 4), 2)
        25
    
        So in general
            thread_first(x, f, (g, y, z))
        expands to
            g(f(x), y, z)
    
        See Also:
            thread_last
    """
    pass

def thread_last(val, *forms): # real signature unknown; restored from __doc__
    """
    thread_last(val, *forms)
    
        Thread value through a sequence of functions/forms
    
        >>> def double(x): return 2*x
        >>> def inc(x):    return x + 1
        >>> thread_last(1, inc, double)
        4
    
        If the function expects more than one input you can specify those inputs
        in a tuple.  The value is used as the last input.
    
        >>> def add(x, y): return x + y
        >>> def pow(x, y): return x**y
        >>> thread_last(1, (add, 4), (pow, 2))  # pow(2, add(4, 1))
        32
    
        So in general
            thread_last(x, f, (g, y, z))
        expands to
            g(y, z, f(x))
    
        >>> def iseven(x):
        ...     return x % 2 == 0
        >>> list(thread_last([1, 2, 3], (map, inc), (filter, iseven)))
        [2, 4]
    
        See Also:
            thread_first
    """
    pass

def _flip(*args, **kwargs): # real signature unknown
    """
    flip(func, a, b)
    
        Call the function call with the arguments flipped
    
        This function is curried.
    
        >>> def div(a, b):
        ...     return a // b
        ...
        >>> flip(div, 2, 6)
        3
        >>> div_by_two = flip(div, 2)
        >>> div_by_two(4)
        2
    
        This is particularly useful for built in functions and functions defined
        in C extensions that accept positional only arguments. For example:
        isinstance, issubclass.
    
        >>> data = [1, 'a', 'b', 2, 1.5, object(), 3]
        >>> only_ints = list(filter(flip(isinstance, int), data))
        >>> only_ints
        [1, 2, 3]
    """
    pass

def _restore_curry(cls, func, args, kwargs, is_decorated): # real signature unknown; restored from __doc__
    """ _restore_curry(cls, func, args, kwargs, is_decorated) """
    pass

def __pyx_unpickle_excepts(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_excepts(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __reduce_cython__(self): # real signature unknown; restored from __doc__
    """ excepts.__reduce_cython__(self) """
    pass

def __setstate_cython__(self, __pyx_state): # real signature unknown; restored from __doc__
    """ excepts.__setstate_cython__(self, __pyx_state) """
    pass

# classes

class attrgetter(object):
    """
    attrgetter(attr, ...) --> attrgetter object
    
    Return a callable object that fetches the given attribute(s) from its operand.
    After f = attrgetter('name'), the call f(r) returns r.name.
    After g = attrgetter('name', 'date'), the call g(r) returns (r.name, r.date).
    After h = attrgetter('name.first', 'name.last'), the call h(r) returns
    (r.name.first, r.name.last).
    """
    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, attr, *more): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Return state information for pickling """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass


class complement(object):
    """
    complement(func)
    
        Convert a predicate function to its logical complement.
    
        In other words, return a function that, for inputs that normally
        yield True, yields False, and vice-versa.
    
        >>> def iseven(n): return n % 2 == 0
        >>> isodd = complement(iseven)
        >>> iseven(2)
        True
        >>> isodd(2)
        False
    """
    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __init__(self, func): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ complement.__reduce__(self) """
        pass


class Compose(object):
    """
    Compose(self, *funcs)
    
        A composition of functions
    
        See Also:
            compose
    """
    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __get__(self, *args, **kwargs): # real signature unknown
        """ Return an attribute of instance, which is of type owner. """
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

    def __init__(self, *funcs): # real signature unknown; restored from __doc__
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

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ Compose.__reduce__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, state): # real signature unknown; restored from __doc__
        """ Compose.__setstate__(self, state) """
        pass

    first = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """first: object"""

    funcs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """funcs: tuple"""

    __signature__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __wrapped__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __name__ = 'Compose'


class curry(object):
    """
    curry(self, *args, **kwargs)
    
        Curry a callable function
    
        Enables partial application of arguments through calling a function with an
        incomplete set of arguments.
    
        >>> def mul(x, y):
        ...     return x * y
        >>> mul = curry(mul)
    
        >>> double = mul(2)
        >>> double(10)
        20
    
        Also supports keyword arguments
    
        >>> @curry                  # Can use curry as a decorator
        ... def f(x, y, a=10):
        ...     return a * (x + y)
    
        >>> add = f(a=1)
        >>> add(2, 3)
        5
    
        See Also:
            cytoolz.curried - namespace of curried functions
                            https://toolz.readthedocs.io/en/latest/curry.html
    """
    def bind(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """ curry.bind(self, *args, **kwargs) """
        pass

    def call(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """ curry.call(self, *args, **kwargs) """
        pass

    def _should_curry(self, args, kwargs, exc=None): # real signature unknown; restored from __doc__
        """ curry._should_curry(self, args, kwargs, exc=None) """
        pass

    def _should_curry_internal(self, args, kwargs, exc=None): # real signature unknown; restored from __doc__
        """ curry._should_curry_internal(self, args, kwargs, exc=None) """
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __get__(self, *args, **kwargs): # real signature unknown
        """ Return an attribute of instance, which is of type owner. """
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

    def __init__(self, *args, **kwargs): # real signature unknown; restored from __doc__
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

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ curry.__reduce__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    args = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    func = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    keywords = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _has_unknown_args = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _sigspec = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __signature__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __name__ = 'curry'
    __qualname__ = 'curry'


class excepts(object):
    """
    excepts(exc, func, handler=return_none)
    
        A wrapper around a function to catch exceptions and
        dispatch to a handler.
    
        This is like a functional try/except block, in the same way that
        ifexprs are functional if/else blocks.
    
        Examples
        --------
        >>> excepting = excepts(
        ...     ValueError,
        ...     lambda a: [1, 2].index(a),
        ...     lambda _: -1,
        ... )
        >>> excepting(1)
        0
        >>> excepting(3)
        -1
    
        Multiple exceptions and default except clause.
        >>> excepting = excepts((IndexError, KeyError), lambda a: a[0])
        >>> excepting([])
        >>> excepting([1])
        1
        >>> excepting({})
        >>> excepting({0: 1})
        1
    """
    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __init__(self, exc, func, handler=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ excepts.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ excepts.__setstate_cython__(self, __pyx_state) """
        pass

    exc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """exc: object"""

    func = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """func: object"""

    handler = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """handler: object"""


    __name__ = 'excepts'


class ifilter(object):
    """
    filter(function or None, iterable) --> filter object
    
    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true.
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


class imap(object):
    """
    map(func, *iterables) --> map object
    
    Make an iterator that computes the function using arguments from
    each of the iterables.  Stops when the shortest iterable is exhausted.
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


class InstanceProperty(property):
    """
    Like @property, but returns ``classval`` when used as a class attribute
    
        Should not be used directly.  Use ``instanceproperty`` instead.
    """
    def __get__(self, obj, type=None): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, fget=None, fset=None, fdel=None, doc=None, classval=None): # reliably restored by inspect
        # no doc
        pass

    def __reduce__(self): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'toolz.functoolz', '__doc__': ' Like @property, but returns ``classval`` when used as a class attribute\\n\\n    Should not be used directly.  Use ``instanceproperty`` instead.\\n    ', '__init__': <function InstanceProperty.__init__ at 0x0000027B8CFA2BF8>, '__get__': <function InstanceProperty.__get__ at 0x0000027B8CFA2C80>, '__reduce__': <function InstanceProperty.__reduce__ at 0x0000027B8CFA2D08>, '__dict__': <attribute '__dict__' of 'InstanceProperty' objects>, '__weakref__': <attribute '__weakref__' of 'InstanceProperty' objects>})"


class MethodType(object):
    """
    method(function, instance)
    
    Create a bound instance method object.
    """
    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __get__(self, *args, **kwargs): # real signature unknown
        """ Return an attribute of instance, which is of type owner. """
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

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    __func__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the function (or other callable) implementing a method"""

    __self__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the instance to which a method is bound"""



class partial(object):
    """
    partial(func, *args, **keywords) - new function with partial application
        of the given arguments and keywords.
    """
    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, func, *args, **keywords): # real signature unknown; restored from __doc__
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

    args = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """tuple of arguments to future partial calls"""

    func = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """function object to use in future partial calls"""

    keywords = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """dictionary of keyword arguments to future partial calls"""


    __dict__ = None # (!) real value is "mappingproxy({'__repr__': <slot wrapper '__repr__' of 'functools.partial' objects>, '__call__': <slot wrapper '__call__' of 'functools.partial' objects>, '__getattribute__': <slot wrapper '__getattribute__' of 'functools.partial' objects>, '__setattr__': <slot wrapper '__setattr__' of 'functools.partial' objects>, '__delattr__': <slot wrapper '__delattr__' of 'functools.partial' objects>, '__new__': <built-in method __new__ of type object at 0x00007FFB145ED5E0>, '__reduce__': <method '__reduce__' of 'functools.partial' objects>, '__setstate__': <method '__setstate__' of 'functools.partial' objects>, 'func': <member 'func' of 'functools.partial' objects>, 'args': <member 'args' of 'functools.partial' objects>, 'keywords': <member 'keywords' of 'functools.partial' objects>, '__dict__': <attribute '__dict__' of 'functools.partial' objects>, '__doc__': 'partial(func, *args, **keywords) - new function with partial application\\n    of the given arguments and keywords.\\n'})"


class _juxt_inner(object):
    # no doc
    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ _juxt_inner.__reduce__(self) """
        pass

    funcs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """funcs: tuple"""



class _memoize(object):
    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __get__(self, *args, **kwargs): # real signature unknown
        """ Return an attribute of instance, which is of type owner. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ _memoize.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ _memoize.__setstate_cython__(self, __pyx_state) """
        pass

    __wrapped__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __name__ = '_memoize'


# variables with complex values

__all__ = [
    'identity',
    'thread_first',
    'thread_last',
    'memoize',
    'compose',
    'compose_left',
    'pipe',
    'complement',
    'juxt',
    'do',
    'curry',
    'memoize',
    'flip',
    'excepts',
    'apply',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000027B8CF83D68>'

__pyx_capi__ = {
    'c_compose': None, # (!) real value is '<capsule object "PyObject *(PyObject *)" at 0x0000027B8CEF82A0>'
    'c_compose_left': None, # (!) real value is '<capsule object "PyObject *(PyObject *)" at 0x0000027B8CEF82D0>'
    'c_juxt': None, # (!) real value is '<capsule object "PyObject *(PyObject *)" at 0x0000027B8CEF8330>'
    'c_pipe': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyObject *)" at 0x0000027B8CEF8300>'
    'c_thread_first': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyObject *)" at 0x0000027B8CEF8210>'
    'c_thread_last': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyObject *)" at 0x0000027B8CEF8240>'
    'do': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyObject *, int __pyx_skip_dispatch)" at 0x0000027B8CEF8360>'
    'flip': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyObject *, PyObject *, int __pyx_skip_dispatch)" at 0x0000027B8CEF8390>'
    'identity': None, # (!) real value is '<capsule object "PyObject *(PyObject *, int __pyx_skip_dispatch)" at 0x0000027B8CEF81E0>'
    'memoize': None, # (!) real value is '<capsule object "PyObject *(PyObject *, int __pyx_skip_dispatch, struct __pyx_opt_args_7cytoolz_9functoolz_memoize *__pyx_optional_args)" at 0x0000027B8CEF8270>'
    'return_none': None, # (!) real value is '<capsule object "PyObject *(PyObject *, int __pyx_skip_dispatch)" at 0x0000027B8CEF83C0>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='cytoolz.functoolz', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000027B8CF83D68>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\cytoolz\\\\functoolz.cp37-win_amd64.pyd')"

__test__ = {
    'apply (line 34)': '\n    Applies a function and returns the results\n\n    >>> def double(x): return 2*x\n    >>> def inc(x):    return x + 1\n    >>> apply(double, 5)\n    10\n\n    >>> tuple(map(apply, [double, inc, double], [10, 500, 8000]))\n    (20, 501, 16000)\n    ',
    'compose (line 588)': "\n    Compose functions to operate in series.\n\n    Returns a function that applies other functions in sequence.\n\n    Functions are applied from right to left so that\n    ``compose(f, g, h)(x, y)`` is the same as ``f(g(h(x, y)))``.\n\n    If no arguments are provided, the identity function (f(x) = x) is returned.\n\n    >>> inc = lambda i: i + 1\n    >>> compose(str, inc)(3)\n    '4'\n\n    See Also:\n        compose_left\n        pipe\n    ",
    'compose_left (line 619)': "\n    Compose functions to operate in series.\n\n    Returns a function that applies other functions in sequence.\n\n    Functions are applied from left to right so that\n    ``compose_left(f, g, h)(x, y)`` is the same as ``h(g(f(x, y)))``.\n\n    If no arguments are provided, the identity function (f(x) = x) is returned.\n\n    >>> inc = lambda i: i + 1\n    >>> compose_left(inc, str)(3)\n    '4'\n\n    See Also:\n        compose\n        pipe\n    ",
    'do (line 737)': '\n    Runs ``func`` on ``x``, returns ``x``\n\n    Because the results of ``func`` are not returned, only the side\n    effects of ``func`` are relevant.\n\n    Logging functions can be made by composing ``do`` with a storage function\n    like ``list.append`` or ``file.write``\n\n    >>> from cytoolz import compose\n    >>> from cytoolz.curried import do\n\n    >>> log = []\n    >>> inc = lambda x: x + 1\n    >>> inc = compose(inc, do(log.append))\n    >>> inc(1)\n    2\n    >>> inc(11)\n    12\n    >>> log\n    [1, 11]\n    ',
    'flip (line 764)': "\n    Call the function call with the arguments flipped\n\n    This function is curried.\n\n    >>> def div(a, b):\n    ...     return a // b\n    ...\n    >>> flip(div, 2, 6)\n    3\n    >>> div_by_two = flip(div, 2)\n    >>> div_by_two(4)\n    2\n\n    This is particularly useful for built in functions and functions defined\n    in C extensions that accept positional only arguments. For example:\n    isinstance, issubclass.\n\n    >>> data = [1, 'a', 'b', 2, 1.5, object(), 3]\n    >>> only_ints = list(filter(flip(isinstance, int), data))\n    >>> only_ints\n    [1, 2, 3]\n    ",
    'juxt (line 715)': '\n    Creates a function that calls several functions with the same arguments\n\n    Takes several functions and returns a function that applies its arguments\n    to each of those functions then returns a tuple of the results.\n\n    Name comes from juxtaposition: the fact of two things being seen or placed\n    close together with contrasting effect.\n\n    >>> inc = lambda x: x + 1\n    >>> double = lambda x: x * 2\n    >>> juxt(inc, double)(10)\n    (11, 20)\n    >>> juxt([inc, double])(10)\n    (11, 20)\n    ',
    'memoize (line 391)': "\n    Cache a function's result for speedy future evaluation\n\n    Considerations:\n        Trades memory for speed.\n        Only use on pure functions.\n\n    >>> def add(x, y):  return x + y\n    >>> add = memoize(add)\n\n    Or use as a decorator\n\n    >>> @memoize\n    ... def add(x, y):\n    ...     return x + y\n\n    Use the ``cache`` keyword to provide a dict-like object as an initial cache\n\n    >>> @memoize(cache={(1, 2): 3})\n    ... def add(x, y):\n    ...     return x + y\n\n    Note that the above works as a decorator because ``memoize`` is curried.\n\n    It is also possible to provide a ``key(args, kwargs)`` function that\n    calculates keys used for the cache, which receives an ``args`` tuple and\n    ``kwargs`` dict as input, and must return a hashable value.  However,\n    the default key function should be sufficient most of the time.\n\n    >>> # Use key function that ignores extraneous keyword arguments\n    >>> @memoize(key=lambda args, kwargs: args)\n    ... def add(x, y, verbose=False):\n    ...     if verbose:\n    ...         print('Calculating %s + %s' % (x, y))\n    ...     return x + y\n    ",
    'pipe (line 648)': "\n    Pipe a value through a sequence of functions\n\n    I.e. ``pipe(data, f, g, h)`` is equivalent to ``h(g(f(data)))``\n\n    We think of the value as progressing through a pipe of several\n    transformations, much like pipes in UNIX\n\n    ``$ cat data | f | g | h``\n\n    >>> double = lambda i: 2 * i\n    >>> pipe(3, double, str)\n    '6'\n\n    See Also:\n        compose\n        compose_left\n        thread_first\n        thread_last\n    ",
    'thread_first (line 65)': '\n    Thread value through a sequence of functions/forms\n\n    >>> def double(x): return 2*x\n    >>> def inc(x):    return x + 1\n    >>> thread_first(1, inc, double)\n    4\n\n    If the function expects more than one input you can specify those inputs\n    in a tuple.  The value is used as the first input.\n\n    >>> def add(x, y): return x + y\n    >>> def pow(x, y): return x**y\n    >>> thread_first(1, (add, 4), (pow, 2))  # pow(add(1, 4), 2)\n    25\n\n    So in general\n        thread_first(x, f, (g, y, z))\n    expands to\n        g(f(x), y, z)\n\n    See Also:\n        thread_last\n    ',
    'thread_last (line 107)': '\n    Thread value through a sequence of functions/forms\n\n    >>> def double(x): return 2*x\n    >>> def inc(x):    return x + 1\n    >>> thread_last(1, inc, double)\n    4\n\n    If the function expects more than one input you can specify those inputs\n    in a tuple.  The value is used as the last input.\n\n    >>> def add(x, y): return x + y\n    >>> def pow(x, y): return x**y\n    >>> thread_last(1, (add, 4), (pow, 2))  # pow(2, add(4, 1))\n    32\n\n    So in general\n        thread_last(x, f, (g, y, z))\n    expands to\n        g(y, z, f(x))\n\n    >>> def iseven(x):\n    ...     return x % 2 == 0\n    >>> list(thread_last([1, 2, 3], (map, inc), (filter, iseven)))\n    [2, 4]\n\n    See Also:\n        thread_first\n    ',
}

