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

class interleave(object):
    """
    interleave(seqs)
    
        Interleave a sequence of sequences
    
        >>> list(interleave([[1, 2], [3, 4]]))
        [1, 3, 2, 4]
    
        >>> ''.join(interleave(('ABC', 'XY')))
        'AXBYC'
    
        Both the individual sequences and the sequence of sequences may be infinite
    
        Returns a lazy iterator
    """
    def __init__(self, seqs): # real signature unknown; restored from __doc__
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
        """ interleave.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ interleave.__setstate_cython__(self, __pyx_state) """
        pass


