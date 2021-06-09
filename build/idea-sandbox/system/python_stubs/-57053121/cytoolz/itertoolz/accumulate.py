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

class accumulate(object):
    """
    accumulate(binop, seq, initial='__no__default__')
    
        Repeatedly apply binary function to a sequence, accumulating results
    
        >>> from operator import add, mul
        >>> list(accumulate(add, [1, 2, 3, 4, 5]))
        [1, 3, 6, 10, 15]
        >>> list(accumulate(mul, [1, 2, 3, 4, 5]))
        [1, 2, 6, 24, 120]
    
        Accumulate is similar to ``reduce`` and is good for making functions like
        cumulative sum:
    
        >>> from functools import partial, reduce
        >>> sum    = partial(reduce, add)
        >>> cumsum = partial(accumulate, add)
    
        Accumulate also takes an optional argument that will be used as the first
        value. This is similar to reduce.
    
        >>> list(accumulate(add, [1, 2, 3], -1))
        [-1, 0, 2, 5]
        >>> list(accumulate(add, [], 1))
        [1]
    
        See Also:
            itertools.accumulate :  In standard itertools for Python 3.2+
    """
    def __init__(self, binop, seq, initial='__no__default__'): # real signature unknown; restored from __doc__
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
        """ accumulate.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ accumulate.__setstate_cython__(self, __pyx_state) """
        pass


