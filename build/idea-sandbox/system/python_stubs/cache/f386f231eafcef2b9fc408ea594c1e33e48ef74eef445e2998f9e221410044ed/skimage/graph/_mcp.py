# encoding: utf-8
# module skimage.graph._mcp
# from C:\Users\Doly\Anaconda3\lib\site-packages\skimage\graph\_mcp.cp37-win_amd64.pyd
# by generator 1.147
"""
Cython implementation of Dijkstra's minimum cost path algorithm,
for use with data on a n-dimensional lattice.

Original author: Zachary Pincus
Inspired by code from Almar Klein
Later modifications by Almar Klein (Dec 2013)

License: BSD

Copyright 2009 Zachary Pincus

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:

1. Redistributions of source code must retain the above copyright
     notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright
     notice, this list of conditions and the following disclaimer in the
     documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py
import skimage.graph.heap as heap # C:\Users\Doly\Anaconda3\lib\site-packages\skimage\graph\heap.cp37-win_amd64.pyd
import numpy as __numpy


# functions

def make_offsets(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Make a list of offsets from a center point defining a n-dim
        neighborhood.
    
        Parameters
        ----------
        d : int
            dimension of the offsets to produce
        fully_connected : bool
            whether the neighborhood should be singly- of fully-connected
    
        Returns
        -------
        offsets : list of tuples of length `d`
    
        Examples
        --------
    
        The singly-connected 2-d neighborhood is four offsets:
    
        >>> make_offsets(2, False)
        [(-1,0), (1,0), (0,-1), (0,1)]
    
        While the fully-connected 2-d neighborhood is the full cartesian product
        of {-1, 0, 1} (less the origin (0,0)).
    """
    pass

def warn(message, category=None, stacklevel=2): # reliably restored by inspect
    """ A version of `warnings.warn` with a default stacklevel of 2. """
    pass

def _get_edge_map(*args, **kwargs): # real signature unknown
    """
    Return an array with edge points/lines/planes/hyperplanes marked.
    
        Given a shape (of length n), return an edge_map array with a shape of
        original_shape + (n,), where, for each dimension, edge_map[...,dim] will
        have zeros at indices not along an edge in that dimension, -1s at indices
        along the lower boundary, and +1s on the upper boundary.
    
        This allows one to, given an nd index, calculate not only if the index is
        at the edge of the array, but if so, which edge(s) it lies along.
    """
    pass

def _normalize_indices(indices, shape): # real signature unknown; restored from __doc__
    """
    _normalize_indices(indices, shape)
    
        Make all indices positive. If an index is out-of-bounds, return None.
    """
    pass

def _offset_edge_map(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Return an array with positions marked where offsets will step
        out of bounds.
    
        Given a shape (of length n) and a list of n-d offsets, return a two arrays
        of (n,) + shape: pos_edge_map and neg_edge_map.
        For each dimension xxx_edge_map[dim, ...] has zeros at indices at which
        none of the given offsets (in that dimension) of the given sign (positive
        or negative, respectively) will step out of bounds. If the value is
        nonzero, it gives the largest offset (in terms of absolute value) that
        will step out of bounds in that direction.
    
        An example will be explanatory:
        >>> offsets = [[-2,0], [1,1], [0,2]]
        >>> pos_edge_map, neg_edge_map = _offset_edge_map((4,4), offsets)
        >>> neg_edge_map[0]
        array([[-1, -1, -1, -1],
              [-2, -2, -2, -2],
              [ 0,  0,  0,  0],
              [ 0,  0,  0,  0]], dtype=int8)
    
        >>> pos_edge_map[1]
        array([[0, 0, 2, 1],
              [0, 0, 2, 1],
              [0, 0, 2, 1],
              [0, 0, 2, 1]], dtype=int8)
    """
    pass

def _ravel_index_fortran(flat_indices, shape): # real signature unknown; restored from __doc__
    """
    _ravel_index_fortran(flat_indices, shape)
    
        Given an index tuple into an n-d fortran-strided array, return a
        flat index.
    """
    pass

def _reverse(*args, **kwargs): # real signature unknown
    """ Reverse index an array safely, with bounds/wraparound checks on. """
    pass

def _unravel_index_fortran(flat_indices, shape): # real signature unknown; restored from __doc__
    """
    _unravel_index_fortran(flat_indices, shape)
    
        Given a flat index into an n-d fortran-strided array, return an
        index tuple.
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_MCP(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_MCP_Connect(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_MCP_Flexible(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_MCP_Geometric(*args, **kwargs): # real signature unknown
    pass

# classes

class OFFSET_D(__numpy.signedinteger):
    """
    Signed integer type, compatible with C ``char``.
        Character code: ``'b'``.
        Canonical name: ``np.byte``.
        Alias *on this platform*: ``np.int8``: 8-bit signed integer (-128 to 127).
    """
    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
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

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
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

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass


EDGE_D = OFFSET_D


class FLOAT_D(__numpy.floating, float):
    """
    Double-precision floating-point number type, compatible with Python `float`
        and C ``double``.
        Character code: ``'d'``.
        Canonical name: ``np.double``.
        Alias: ``np.float_``.
        Alias *on this platform*: ``np.float64``: 64-bit precision floating-point number type: sign bit, 11 bits exponent, 52 bits mantissa.
    """
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        double.as_integer_ratio() -> (int, int)
        
                Return a pair of integers, whose ratio is exactly equal to the original
                floating point number, and with a positive denominator.
                Raise OverflowError on infinities and a ValueError on NaNs.
        
                >>> np.double(10.0).as_integer_ratio()
                (10, 1)
                >>> np.double(0.0).as_integer_ratio()
                (0, 1)
                >>> np.double(-.25).as_integer_ratio()
                (-1, 4)
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
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

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
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

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass


class INDEX_D(__numpy.signedinteger):
    """
    Signed integer type, compatible with C ``long long``.
        Character code: ``'q'``.
        Canonical name: ``np.longlong``.
        Alias *on this platform*: ``np.int64``: 64-bit signed integer (-9223372036854775808 to 9223372036854775807).
        Alias *on this platform*: ``np.intp``: Signed integer large enough to fit pointer, compatible with C ``intptr_t``.
    """
    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
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

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
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

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass


class MCP(object):
    """
    MCP(costs, offsets=None, fully_connected=True, sampling=None)
    
        A class for finding the minimum cost path through a given n-d costs array.
    
        Given an n-d costs array, this class can be used to find the minimum-cost
        path through that array from any set of points to any other set of points.
        Basic usage is to initialize the class and call find_costs() with a one
        or more starting indices (and an optional list of end indices). After
        that, call traceback() one or more times to find the path from any given
        end-position to the closest starting index. New paths through the same
        costs array can be found by calling find_costs() repeatedly.
    
        The cost of a path is calculated simply as the sum of the values of the
        `costs` array at each point on the path. The class MCP_Geometric, on the
        other hand, accounts for the fact that diagonal vs. axial moves are of
        different lengths, and weights the path cost accordingly.
    
        Array elements with infinite or negative costs will simply be ignored, as
        will paths whose cumulative cost overflows to infinite.
    
        Parameters
        ----------
        costs : ndarray
        offsets : iterable, optional
            A list of offset tuples: each offset specifies a valid move from a
            given n-d position.
            If not provided, offsets corresponding to a singly- or fully-connected
            n-d neighborhood will be constructed with make_offsets(), using the
            `fully_connected` parameter value.
        fully_connected : bool, optional
            If no `offsets` are provided, this determines the connectivity of the
            generated neighborhood. If true, the path may go along diagonals
            between elements of the `costs` array; otherwise only axial moves are
            permitted.
        sampling : tuple, optional
            For each dimension, specifies the distance between two cells/voxels.
            If not given or None, the distance is assumed unit.
    
        Attributes
        ----------
        offsets : ndarray
            Equivalent to the `offsets` provided to the constructor, or if none
            were so provided, the offsets created for the requested n-d
            neighborhood. These are useful for interpreting the `traceback` array
            returned by the find_costs() method.
    """
    def find_costs(self, *args, **kwargs): # real signature unknown
        """
        Find the minimum-cost path from the given starting points.
        
                This method finds the minimum-cost path to the specified ending
                indices from any one of the specified starting indices. If no end
                positions are given, then the minimum-cost path to every position in
                the costs array will be found.
        
                Parameters
                ----------
                starts : iterable
                    A list of n-d starting indices (where n is the dimension of the
                    `costs` array). The minimum cost path to the closest/cheapest
                    starting point will be found.
                ends : iterable, optional
                    A list of n-d ending indices.
                find_all_ends : bool, optional
                    If 'True' (default), the minimum-cost-path to every specified
                    end-position will be found; otherwise the algorithm will stop when
                    a a path is found to any end-position. (If no `ends` were
                    specified, then this parameter has no effect.)
        
                Returns
                -------
                cumulative_costs : ndarray
                    Same shape as the `costs` array; this array records the minimum
                    cost path from the nearest/cheapest starting index to each index
                    considered. (If `ends` were specified, not all elements in the
                    array will necessarily be considered: positions not evaluated will
                    have a cumulative cost of inf. If `find_all_ends` is 'False', only
                    one of the specified end-positions will have a finite cumulative
                    cost.)
                traceback : ndarray
                    Same shape as the `costs` array; this array contains the offset to
                    any given index from its predecessor index. The offset indices
                    index into the `offsets` attribute, which is a array of n-d
                    offsets. In the 2-d case, if offsets[traceback[x, y]] is (-1, -1),
                    that means that the predecessor of [x, y] in the minimum cost path
                    to some start position is [x+1, y+1]. Note that if the
                    offset_index is -1, then the given index was not considered.
        """
        pass

    def goal_reached(self, int_index, float_cumcost): # real signature unknown; restored from __doc__
        """
        int goal_reached(int index, float cumcost)
                This method is called each iteration after popping an index
                from the heap, before examining the neighbours.
        
                This method can be overloaded to modify the behavior of the MCP
                algorithm. An example might be to stop the algorithm when a
                certain cumulative cost is reached, or when the front is a
                certain distance away from the seed point.
        
                This method should return 1 if the algorithm should not check
                the current point's neighbours and 2 if the algorithm is now
                done.
        """
        return 0

    def traceback(self, end): # real signature unknown; restored from __doc__
        """
        traceback(end)
        
                Trace a minimum cost path through the pre-calculated traceback array.
        
                This convenience function reconstructs the the minimum cost path to a
                given end position from one of the starting indices provided to
                find_costs(), which must have been called previously. This function
                can be called as many times as desired after find_costs() has been
                run.
        
                Parameters
                ----------
                end : iterable
                    An n-d index into the `costs` array.
        
                Returns
                -------
                traceback : list of n-d tuples
                    A list of indices into the `costs` array, starting with one of
                    the start positions passed to find_costs(), and ending with the
                    given `end` index. These indices specify the minimum-cost path
                    from any given start index to the `end` index. (The total cost
                    of that path can be read out from the `cumulative_costs` array
                    returned by find_costs().)
        """
        pass

    def _reset(self): # real signature unknown; restored from __doc__
        """
        _reset()
                Clears paths found by find_costs().
        """
        pass

    def __init__(self, costs, offsets=None, fully_connected=True, sampling=None): # real signature unknown; restored from __doc__
        """
        __init__(costs, offsets=None, fully_connected=True, sampling=None)
        
                See class documentation.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001E58D890240>'


class MCP_Connect(MCP):
    """
    MCP_Connect(costs, offsets=None, fully_connected=True)
    
        Connect source points using the distance-weighted minimum cost function.
    
        A front is grown from each seed point simultaneously, while the
        origin of the front is tracked as well. When two fronts meet,
        create_connection() is called. This method must be overloaded to
        deal with the found edges in a way that is appropriate for the
        application.
    """
    def create_connection(self, *args, **kwargs): # real signature unknown
        """
        create_connection id1, id2, pos1, pos2, cost1, cost2)
        
                Overload this method to keep track of the connections that are
                found during MCP processing. Note that a connection with the
                same ids can be found multiple times (but with different
                positions and costs).
        
                At the time that this method is called, both points are "frozen"
                and will not be visited again by the MCP algorithm.
        
                Parameters
                ----------
                id1 : int
                    The seed point id where the first neighbor originated from.
                id2 : int
                    The seed point id where the second neighbor originated from.
                pos1 : tuple
                    The index of of the first neighbour in the connection.
                pos2 : tuple
                    The index of of the second neighbour in the connection.
                cost1 : float
                    The cumulative cost at `pos1`.
                cost2 : float
                    The cumulative costs at `pos2`.
        """
        pass

    def _reset(self, *args, **kwargs): # real signature unknown
        """ Reset the id map. """
        pass

    def __init__(self, costs, offsets=None, fully_connected=True): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001E58D8902A0>'


class MCP_Flexible(MCP):
    """
    MCP_Flexible(costs, offsets=None, fully_connected=True)
    
        Find minimum cost paths through an N-d costs array.
    
        See the documentation for MCP for full details. This class differs from
        MCP in that several methods can be overloaded (from pure Python) to
        modify the behavior of the algorithm and/or create custom algorithms
        based on MCP. Note that goal_reached can also be overloaded in the
        MCP class.
    """
    def examine_neighbor(self, index, new_index, offset_length): # real signature unknown; restored from __doc__
        """
        examine_neighbor(index, new_index, offset_length)
                This method is called once for every pair of neighboring nodes,
                as soon as both nodes are frozen.
        
                This method can be overloaded to obtain information about
                neightboring nodes, and/or to modify the behavior of the MCP
                algorithm. One example is the MCP_Connect class, which checks
                for meeting fronts using this hook.
        """
        pass

    def travel_cost(self, old_cost, new_cost, offset_length): # real signature unknown; restored from __doc__
        """
        travel_cost(old_cost, new_cost, offset_length)
                This method calculates the travel cost for going from the
                current node to the next. The default implementation returns
                new_cost. Overload this method to adapt the behaviour of the
                algorithm.
        """
        pass

    def update_node(self, index, new_index, offset_length): # real signature unknown; restored from __doc__
        """
        update_node(index, new_index, offset_length)
                This method is called when a node is updated, right after
                new_index is pushed onto the heap and the traceback map is
                updated.
        
                This method can be overloaded to keep track of other arrays
                that are used by a specific implementation of the algorithm.
                For instance the MCP_Connect class uses it to update an id map.
        """
        pass

    def __init__(self, costs, offsets=None, fully_connected=True, sampling=None): # real signature unknown; restored from __doc__
        """
        __init__(costs, offsets=None, fully_connected=True, sampling=None)
        
                See class documentation.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001E58D8902D0>'


class MCP_Geometric(MCP):
    """
    MCP_Geometric(costs, offsets=None, fully_connected=True)
    
        Find distance-weighted minimum cost paths through an n-d costs array.
    
        See the documentation for MCP for full details. This class differs from
        MCP in that the cost of a path is not simply the sum of the costs along
        that path.
    
        This class instead assumes that the costs array contains at each position
        the "cost" of a unit distance of travel through that position. For
        example, a move (in 2-d) from (1, 1) to (1, 2) is assumed to originate in
        the center of the pixel (1, 1) and terminate in the center of (1, 2). The
        entire move is of distance 1, half through (1, 1) and half through (1, 2);
        thus the cost of that move is `(1/2)*costs[1,1] + (1/2)*costs[1,2]`.
    
        On the other hand, a move from (1, 1) to (2, 2) is along the diagonal and
        is sqrt(2) in length. Half of this move is within the pixel (1, 1) and the
        other half in (2, 2), so the cost of this move is calculated as
        `(sqrt(2)/2)*costs[1,1] + (sqrt(2)/2)*costs[2,2]`.
    
        These calculations don't make a lot of sense with offsets of magnitude
        greater than 1. Use the `sampling` argument in order to deal with
        anisotropic data.
    """
    def __init__(self, costs, offsets=None, fully_connected=True, sampling=None): # real signature unknown; restored from __doc__
        """
        __init__(costs, offsets=None, fully_connected=True, sampling=None)
        
                See class documentation.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001E58D890270>'


class OFFSETS_INDEX_D(__numpy.signedinteger):
    """
    Signed integer type, compatible with C ``short``.
        Character code: ``'h'``.
        Canonical name: ``np.short``.
        Alias *on this platform*: ``np.int16``: 16-bit signed integer (-32768 to 32767).
    """
    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
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

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
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

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001E58D897278>'

__spec__ = None # (!) real value is "ModuleSpec(name='skimage.graph._mcp', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001E58D897278>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\skimage\\\\graph\\\\_mcp.cp37-win_amd64.pyd')"

__test__ = {
    '_offset_edge_map (line 79)': 'Return an array with positions marked where offsets will step\n    out of bounds.\n\n    Given a shape (of length n) and a list of n-d offsets, return a two arrays\n    of (n,) + shape: pos_edge_map and neg_edge_map.\n    For each dimension xxx_edge_map[dim, ...] has zeros at indices at which\n    none of the given offsets (in that dimension) of the given sign (positive\n    or negative, respectively) will step out of bounds. If the value is\n    nonzero, it gives the largest offset (in terms of absolute value) that\n    will step out of bounds in that direction.\n\n    An example will be explanatory:\n    >>> offsets = [[-2,0], [1,1], [0,2]]\n    >>> pos_edge_map, neg_edge_map = _offset_edge_map((4,4), offsets)\n    >>> neg_edge_map[0]\n    array([[-1, -1, -1, -1],\n          [-2, -2, -2, -2],\n          [ 0,  0,  0,  0],\n          [ 0,  0,  0,  0]], dtype=int8)\n\n    >>> pos_edge_map[1]\n    array([[0, 0, 2, 1],\n          [0, 0, 2, 1],\n          [0, 0, 2, 1],\n          [0, 0, 2, 1]], dtype=int8)\n\n    ',
    'make_offsets (line 124)': 'Make a list of offsets from a center point defining a n-dim\n    neighborhood.\n\n    Parameters\n    ----------\n    d : int\n        dimension of the offsets to produce\n    fully_connected : bool\n        whether the neighborhood should be singly- of fully-connected\n\n    Returns\n    -------\n    offsets : list of tuples of length `d`\n\n    Examples\n    --------\n\n    The singly-connected 2-d neighborhood is four offsets:\n\n    >>> make_offsets(2, False)\n    [(-1,0), (1,0), (0,-1), (0,1)]\n\n    While the fully-connected 2-d neighborhood is the full cartesian product\n    of {-1, 0, 1} (less the origin (0,0)).\n\n    ',
}

