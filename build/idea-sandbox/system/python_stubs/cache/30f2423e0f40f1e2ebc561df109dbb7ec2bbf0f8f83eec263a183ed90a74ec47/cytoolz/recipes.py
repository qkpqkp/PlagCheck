# encoding: utf-8
# module cytoolz.recipes
# from C:\Users\Doly\Anaconda3\lib\site-packages\cytoolz\recipes.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
from itertools import groupby


# functions

def countby(key, seq): # real signature unknown; restored from __doc__
    """
    countby(key, seq)
    
        Count elements of a collection by a key function
    
        >>> countby(len, ['cat', 'mouse', 'dog'])
        {3: 2, 5: 1}
    
        >>> def iseven(x): return x % 2 == 0
        >>> countby(iseven, [1, 2, 3])  # doctest:+SKIP
        {True: 1, False: 2}
    
        See Also:
            groupby
    """
    pass

def __reduce_cython__(self): # real signature unknown; restored from __doc__
    """ partitionby.__reduce_cython__(self) """
    pass

def __setstate_cython__(self, __pyx_state): # real signature unknown; restored from __doc__
    """ partitionby.__setstate_cython__(self, __pyx_state) """
    pass

# classes

class map(object):
    """
    map(func, *iterables) --> map object
    
    Make an iterator that computes the function using arguments from
    each of the iterables.  Stops when the shortest iterable is exhausted.
    """
    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, func, *iterables): # real signature unknown; restored from __doc__
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


class partitionby(object):
    """
    partitionby(func, seq)
    
        Partition a sequence according to a function
    
        Partition `s` into a sequence of lists such that, when traversing
        `s`, every time the output of `func` changes a new list is started
        and that and subsequent items are collected into that list.
    
        >>> is_space = lambda c: c == " "
        >>> list(partitionby(is_space, "I have space"))
        [('I',), (' ',), ('h', 'a', 'v', 'e'), (' ',), ('s', 'p', 'a', 'c', 'e')]
    
        >>> is_large = lambda x: x > 10
        >>> list(partitionby(is_large, [1, 2, 1, 99, 88, 33, 99, -1, 5]))
        [(1, 2, 1), (99, 88, 33, 99), (-1, 5)]
    
        See also:
            partition
            groupby
            itertools.groupby
    """
    def __init__(self, func, seq): # real signature unknown; restored from __doc__
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ partitionby.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ partitionby.__setstate_cython__(self, __pyx_state) """
        pass


# variables with complex values

__all__ = [
    'countby',
    'partitionby',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000002A4EDE63D30>'

__pyx_capi__ = {
    'countby': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyObject *, int __pyx_skip_dispatch)" at 0x000002A4EDD98750>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='cytoolz.recipes', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000002A4EDE63D30>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\cytoolz\\\\recipes.cp37-win_amd64.pyd')"

__test__ = {
    'countby (line 11)': "\n    Count elements of a collection by a key function\n\n    >>> countby(len, ['cat', 'mouse', 'dog'])\n    {3: 2, 5: 1}\n\n    >>> def iseven(x): return x % 2 == 0\n    >>> countby(iseven, [1, 2, 3])  # doctest:+SKIP\n    {True: 1, False: 2}\n\n    See Also:\n        groupby\n    ",
}

