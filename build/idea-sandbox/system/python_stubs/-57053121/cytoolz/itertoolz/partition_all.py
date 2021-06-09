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

class partition_all(object):
    """
    partition_all(n, seq)
    
        Partition all elements of sequence into tuples of length at most n
    
        The final tuple may be shorter to accommodate extra elements.
    
        >>> list(partition_all(2, [1, 2, 3, 4]))
        [(1, 2), (3, 4)]
    
        >>> list(partition_all(2, [1, 2, 3, 4, 5]))
        [(1, 2), (3, 4), (5,)]
    
        See Also:
            partition
    """
    def __init__(self, n, seq): # real signature unknown; restored from __doc__
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
        """ partition_all.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ partition_all.__setstate_cython__(self, __pyx_state) """
        pass


