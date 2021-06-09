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

class random_sample(object):
    """
    random_sample(prob, seq, random_state=None)
    
        Return elements from a sequence with probability of prob
    
        Returns a lazy iterator of random items from seq.
    
        ``random_sample`` considers each item independently and without
        replacement. See below how the first time it returned 13 items and the
        next time it returned 6 items.
    
        >>> seq = list(range(100))
        >>> list(random_sample(0.1, seq)) # doctest: +SKIP
        [6, 9, 19, 35, 45, 50, 58, 62, 68, 72, 78, 86, 95]
        >>> list(random_sample(0.1, seq)) # doctest: +SKIP
        [6, 44, 54, 61, 69, 94]
    
        Providing an integer seed for ``random_state`` will result in
        deterministic sampling. Given the same seed it will return the same sample
        every time.
    
        >>> list(random_sample(0.1, seq, random_state=2016))
        [7, 9, 19, 25, 30, 32, 34, 48, 59, 60, 81, 98]
        >>> list(random_sample(0.1, seq, random_state=2016))
        [7, 9, 19, 25, 30, 32, 34, 48, 59, 60, 81, 98]
    
        ``random_state`` can also be any object with a method ``random`` that
        returns floats between 0.0 and 1.0 (exclusive).
    
        >>> from random import Random
        >>> randobj = Random(2016)
        >>> list(random_sample(0.1, seq, random_state=randobj))
        [7, 9, 19, 25, 30, 32, 34, 48, 59, 60, 81, 98]
    """
    def __init__(self, prob, seq, random_state=None): # real signature unknown; restored from __doc__
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
        """ random_sample.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ random_sample.__setstate_cython__(self, __pyx_state) """
        pass


