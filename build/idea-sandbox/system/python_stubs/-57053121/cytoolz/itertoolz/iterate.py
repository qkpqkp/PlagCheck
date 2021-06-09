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

class iterate(object):
    """
    iterate(func, x)
    
        Repeatedly apply a function func onto an original input
    
        Yields x, then func(x), then func(func(x)), then func(func(func(x))), etc..
    
        >>> def inc(x):  return x + 1
        >>> counter = iterate(inc, 0)
        >>> next(counter)
        0
        >>> next(counter)
        1
        >>> next(counter)
        2
    
        >>> double = lambda x: x * 2
        >>> powers_of_two = iterate(double, 1)
        >>> next(powers_of_two)
        1
        >>> next(powers_of_two)
        2
        >>> next(powers_of_two)
        4
        >>> next(powers_of_two)
        8
    """
    def __init__(self, func, x): # real signature unknown; restored from __doc__
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
        """ iterate.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ iterate.__setstate_cython__(self, __pyx_state) """
        pass


