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

class remove(object):
    """
    remove(predicate, seq)
    
        Return those items of sequence for which predicate(item) is False
    
        >>> def iseven(x):
        ...     return x % 2 == 0
        >>> list(remove(iseven, [1, 2, 3, 4]))
        [1, 3]
    """
    def __init__(self, predicate, seq): # real signature unknown; restored from __doc__
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
        """ remove.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ remove.__setstate_cython__(self, __pyx_state) """
        pass


