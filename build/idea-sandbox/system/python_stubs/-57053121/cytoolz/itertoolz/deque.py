# encoding: utf-8
# module cytoolz.itertoolz
# from C:\Users\Doly\Anaconda3\lib\site-packages\cytoolz\itertoolz.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
from itertools import chain, islice, zip_longest

from _heapq import heapify, heappop, heapreplace

import _random as ___random


from .object import object

class deque(object):
    """
    deque([iterable[, maxlen]]) --> deque object
    
    A list-like sequence optimized for data accesses near its endpoints.
    """
    def append(self, *args, **kwargs): # real signature unknown
        """ Add an element to the right side of the deque. """
        pass

    def appendleft(self, *args, **kwargs): # real signature unknown
        """ Add an element to the left side of the deque. """
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        """ Remove all elements from the deque. """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        """ Return a shallow copy of a deque. """
        pass

    def count(self, value): # real signature unknown; restored from __doc__
        """ D.count(value) -> integer -- return number of occurrences of value """
        return 0

    def extend(self, *args, **kwargs): # real signature unknown
        """ Extend the right side of the deque with elements from the iterable """
        pass

    def extendleft(self, *args, **kwargs): # real signature unknown
        """ Extend the left side of the deque with elements from the iterable """
        pass

    def index(self, value, start=None, stop=None): # real signature unknown; restored from __doc__
        """
        D.index(value, [start, [stop]]) -> integer -- return first index of value.
        Raises ValueError if the value is not present.
        """
        return 0

    def insert(self, index, p_object): # real signature unknown; restored from __doc__
        """ D.insert(index, object) -- insert object before index """
        pass

    def pop(self, *args, **kwargs): # real signature unknown
        """ Remove and return the rightmost element. """
        pass

    def popleft(self, *args, **kwargs): # real signature unknown
        """ Remove and return the leftmost element. """
        pass

    def remove(self, value): # real signature unknown; restored from __doc__
        """ D.remove(value) -- remove first occurrence of value. """
        pass

    def reverse(self): # real signature unknown; restored from __doc__
        """ D.reverse() -- reverse *IN PLACE* """
        pass

    def rotate(self, *args, **kwargs): # real signature unknown
        """ Rotate the deque n steps to the right (default n=1).  If n is negative, rotates left. """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        """ Return a shallow copy of a deque. """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
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

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __iadd__(self, *args, **kwargs): # real signature unknown
        """ Implement self+=value. """
        pass

    def __imul__(self, *args, **kwargs): # real signature unknown
        """ Implement self*=value. """
        pass

    def __init__(self, iterable=None, maxlen=None): # real signature unknown; restored from __doc__
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

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Return state information for pickling. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __reversed__(self): # real signature unknown; restored from __doc__
        """ D.__reversed__() -- return a reverse iterator over the deque """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    def __sizeof__(self): # real signature unknown; restored from __doc__
        """ D.__sizeof__() -- size of D in memory, in bytes """
        pass

    maxlen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """maximum size of a deque or None if unbounded"""


    __hash__ = None


