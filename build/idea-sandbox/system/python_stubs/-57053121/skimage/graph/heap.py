# encoding: utf-8
# module skimage.graph.heap
# from C:\Users\Doly\Anaconda3\lib\site-packages\skimage\graph\heap.cp37-win_amd64.pyd
# by generator 1.147
"""
Cython implementation of a binary min heap.

Original author: Almar Klein
Modified by: Zachary Pincus

License: BSD

Copyright 2009 Almar Klein

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

# no functions
# classes

class BinaryHeap(object):
    """
    BinaryHeap(initial_capacity=128)
    
        A binary heap class that can store values and an integer reference.
    
        A binary heap is an object to store values in, optimized in such a way
        that the minimum (or maximum, but a minimum in this implementation)
        value can be found in O(log2(N)) time. In this implementation, a reference
        value (a single integer) can also be stored with each value.
    
        Use the methods push() and pop() to put in or extract values.
        In C, use the corresponding push_fast() and pop_fast().
    
        Parameters
        ----------
        initial_capacity : int
            Estimate of the size of the heap, if known in advance. (In any case,
            the heap will dynamically grow and shrink as required, though never
            below the `initial_capacity`.)
    
        Attributes
        ----------
        count : int
            The number of values in the heap
        levels : int
            The number of levels in the binary heap (see Notes below). The values
            are stored in the last level, so 2**levels is the capacity of the
            heap before another resize is required.
        min_levels : int
            The minimum number of levels in the heap (relates to the
            `initial_capacity` parameter.)
    
        Notes
        -----
        This implementation stores the binary heap in an array twice as long as
        the number of elements in the heap. The array is structured in levels,
        starting at level 0 with a single value, doubling the amount of values in
        each level. The final level contains the actual values, the level before
        it contains the pairwise minimum values. The level before that contains
        the pairwise minimum values of that level, etc. Take a look at this
        illustration:
    
        level: 0 11 2222 33333333 4444444444444444
        index: 0 12 3456 78901234 5678901234567890
                            1          2         3
    
         The actual values are stored in level 4. The minimum value of position 15
        and 16 is stored in position 7. min(17,18)->8, min(7,8)->3, min(3,4)->1.
        When adding a value, only the path to the top has to be updated, which
        takesO(log2(N)) time.
    
         The advantage of this implementation relative to more common
        implementations that swap values when pushing to the array is that data
        only needs to be swapped once when an element is removed. This means that
        keeping an array of references along with the values is very inexpensive.
        Th disadvantage is that if you pop the minimum value, the tree has to be
        traced from top to bottom and back. So if you only want values and no
        references, this implementation will probably be slower. If you need
        references (and maybe cross references to be kept up to date) this
        implementation will be faster.
    """
    def min_val(self): # real signature unknown; restored from __doc__
        """
        min_val()
        
                Get the minimum value on the heap.
        
                Returns only the value, and does not remove it from the heap.
        """
        pass

    def pop(self): # real signature unknown; restored from __doc__
        """
        pop()
        
                Get the minimum value and remove it from the list.
        
                Returns
                -------
                value : float
                reference : int
                    If no reference was provided, -1 is returned here.
        
                Raises
                ------
                IndexError
                    On attempt to pop from an empty heap
        """
        pass

    def push(self, value, reference=-1): # real signature unknown; restored from __doc__
        """
        push(value, reference=-1)
        
                Append a value to the heap, with optional reference.
        
                Parameters
                ----------
                value : float
                    Value to push onto the heap
                reference : int, optional
                    Reference to associate with the given value.
        """
        pass

    def references(self): # real signature unknown; restored from __doc__
        """
        references()
        
                Get the references in the heap as a list.
        """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """
        reset()
        
                Reset the heap to default, empty state.
        """
        pass

    def values(self): # real signature unknown; restored from __doc__
        """
        values()
        
                Get the values in the heap as a list.
        """
        pass

    def __init__(self, initial_capacity=128): # real signature unknown; restored from __doc__
        """
        __init__(initial_capacity=128)
        
                Class constructor.
        
                Takes an optional parameter 'initial_capacity' so that
                if the required heap capacity is known or can be estimated in advance,
                there will need to be fewer resize operations on the heap.
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

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    levels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    min_levels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001DFE0A60390>'


class FastUpdateBinaryHeap(BinaryHeap):
    """
    FastUpdateBinaryHeap(initial_capacity=128, max_reference=None)
    
        Binary heap that allows the value of a reference to be updated quickly.
    
        This heap class keeps cross-references so that the value associated with a
        given reference can be quickly queried (O(1) time) or updated (O(log2(N))
        time). This is ideal for pathfinding algorithms that implement some
        variant of Dijkstra's algorithm.
    
        Parameters
        ----------
        initial_capacity : int
            Estimate of the size of the heap, if known in advance. (In any case,
            the heap will dynamically grow and shrink as required, though never
            below the `initial_capacity`.)
    
        max_reference : int, optional
            Largest reference value that might be pushed to the heap. (Pushing a
            larger value will result in an error.) If no value is provided,
            `1-initial_capacity` will be used. For the cross-reference index to
            work, all references must be in the range [0, max_reference];
            references pushed outside of that range will not be added to the heap.
            The cross-references are kept as a 1-d array of length
            `max_reference+1', so memory use of this heap is effectively
            O(max_reference)
    
        Attributes
        ----------
        count : int
            The number of values in the heap
        levels : int
            The number of levels in the binary heap (see Notes below). The values
            are stored in the last level, so 2**levels is the capacity of the
            heap before another resize is required.
        min_levels : int
            The minimum number of levels in the heap (relates to the
            `initial_capacity` parameter.)
        max_reference : int
            The provided or calculated maximum allowed reference value.
    
        Notes
        -----
        The cross-references map data[reference]->internalindex, such that the
        value corresponding to a given reference can be found efficiently. This
        can be queried with the value_of() method.
    
        A special method, push_if_lower() is provided that will update the heap if
        the given reference is not in the heap, or if it is and the provided value
        is lower than the current value in the heap. This is again useful for
        pathfinding algorithms.
    """
    def cross_references(self, *args, **kwargs): # real signature unknown
        """ Get the cross references in the heap as a list. """
        pass

    def push(self, value, reference): # real signature unknown; restored from __doc__
        """
        push(value, reference)
        
                Append/update a value in the heap.
        
                Parameters
                ----------
                value : float
                reference : int
                    If the reference is already present in the array, the value for
                    that reference will be updated, otherwise the (value, reference)
                    pair will be added to the heap.
        
                Raises
                ------
                ValueError
                    On pushing a reference outside the range [0, max_reference].
        """
        pass

    def push_if_lower(self, value, reference): # real signature unknown; restored from __doc__
        """
        push_if_lower(value, reference)
        
                Append/update a value in the heap if the extant value is lower.
        
                If the reference is already in the heap, update only of the new value
                is lower than the current one. If the reference is not present, the
                value will always be pushed to the heap.
        
                Parameters
                ----------
                value : float
                reference : int
                    If the reference is already present in the array, the value for
                    that reference will be updated, otherwise the (value, reference)
                    pair will be added to the heap.
        
                Returns
                -------
                pushed : bool
                    True if an append/update occurred, False if otherwise.
        
                Raises
                ------
                ValueError
                    On pushing a reference outside the range [0, max_reference].
        """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """
        reset()
        
                Reset the heap to default, empty state.
        """
        pass

    def value_of(self, reference): # real signature unknown; restored from __doc__
        """
        value_of(reference)
        
                Get the value corresponding to a given reference.
        
                Parameters
                ----------
                reference : int
                    A reference already pushed to the heap.
        
                Returns
                -------
                value : float
        
                Raises
                ------
                ValueError
                    On querying a reference outside the range [0, max_reference], or
                    not already pushed to the heap.
        """
        pass

    def __init__(self, initial_capacity=128, max_reference=None): # real signature unknown; restored from __doc__
        """
        __init__(initial_capacity=128, max_reference=None)
        
                Class constructor.
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

    max_reference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001DFE0A603C0>'


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001DFE0A67FD0>'

__spec__ = None # (!) real value is "ModuleSpec(name='skimage.graph.heap', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001DFE0A67FD0>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\skimage\\\\graph\\\\heap.cp37-win_amd64.pyd')"

__test__ = {}

