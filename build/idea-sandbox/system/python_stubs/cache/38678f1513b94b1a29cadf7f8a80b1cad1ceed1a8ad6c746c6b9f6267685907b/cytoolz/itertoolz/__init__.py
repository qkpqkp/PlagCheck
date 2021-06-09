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


# Variables with simple values

no_default = '__no__default__'
no_pad = '__no__pad__'

# functions

def concat(seqs): # real signature unknown; restored from __doc__
    """
    concat(seqs)
    
        Concatenate zero or more iterables, any of which may be infinite.
    
        An infinite sequence will prevent the rest of the arguments from
        being included.
    
        We use chain.from_iterable rather than ``chain(*seqs)`` so that seqs
        can be a generator.
    
        >>> list(concat([[], [1], [2, 3]]))
        [1, 2, 3]
    
        See also:
            itertools.chain.from_iterable  equivalent
    """
    pass

def concatv(*seqs): # real signature unknown; restored from __doc__
    """
    concatv(*seqs)
    
        Variadic version of concat
    
        >>> list(concatv([], ["a"], ["b", "c"]))
        ['a', 'b', 'c']
    
        See also:
            itertools.chain
    """
    pass

def cons(el, seq): # real signature unknown; restored from __doc__
    """
    cons(el, seq)
    
        Add el to beginning of (possibly infinite) sequence seq.
    
        >>> list(cons(1, [2, 3]))
        [1, 2, 3]
    """
    pass

def count(seq): # real signature unknown; restored from __doc__
    """
    count(seq)
    
        Count the number of items in seq
    
        Like the builtin ``len`` but works on lazy sequencies.
    
        Not to be confused with ``itertools.count``
    
        See also:
            len
    """
    pass

def diff(*seqs, **kwargs): # real signature unknown; restored from __doc__
    """
    diff(*seqs, **kwargs)
    
        Return those items that differ between sequences
    
        >>> list(diff([1, 2, 3], [1, 2, 10, 100]))
        [(3, 10)]
    
        Shorter sequences may be padded with a ``default`` value:
    
        >>> list(diff([1, 2, 3], [1, 2, 10, 100], default=None))
        [(3, 10), (None, 100)]
    
        A ``key`` function may also be applied to each item to use during
        comparisons:
    
        >>> list(diff(['apples', 'bananas'], ['Apples', 'Oranges'], key=str.lower))
        [('bananas', 'Oranges')]
    """
    pass

def drop(Py_ssize_t_n, seq): # real signature unknown; restored from __doc__
    """
    drop(Py_ssize_t n, seq)
    
        The sequence following the first n elements
    
        >>> list(drop(2, [10, 20, 30, 40, 50]))
        [30, 40, 50]
    
        See Also:
            take
            tail
    """
    pass

def first(seq): # real signature unknown; restored from __doc__
    """
    first(seq)
    
        The first element in a sequence
    
        >>> first('ABC')
        'A'
    """
    pass

def frequencies(seq): # real signature unknown; restored from __doc__
    """
    frequencies(seq) -> dict
    
        Find number of occurrences of each value in seq
    
        >>> frequencies(['cat', 'cat', 'ox', 'pig', 'pig', 'cat'])  #doctest: +SKIP
        {'cat': 3, 'ox': 1, 'pig': 2}
    
        See Also:
            countby
            groupby
    """
    return {}

def get(ind, seq, default='__no__default__'): # real signature unknown; restored from __doc__
    """
    get(ind, seq, default='__no__default__')
    
        Get element in a sequence or dict
    
        Provides standard indexing
    
        >>> get(1, 'ABC')       # Same as 'ABC'[1]
        'B'
    
        Pass a list to get multiple values
    
        >>> get([1, 2], 'ABC')  # ('ABC'[1], 'ABC'[2])
        ('B', 'C')
    
        Works on any value that supports indexing/getitem
        For example here we see that it works with dictionaries
    
        >>> phonebook = {'Alice':  '555-1234',
        ...              'Bob':    '555-5678',
        ...              'Charlie':'555-9999'}
        >>> get('Alice', phonebook)
        '555-1234'
    
        >>> get(['Alice', 'Bob'], phonebook)
        ('555-1234', '555-5678')
    
        Provide a default for missing values
    
        >>> get(['Alice', 'Dennis'], phonebook, None)
        ('555-1234', None)
    
        See Also:
            pluck
    """
    pass

def getter(index): # real signature unknown; restored from __doc__
    """ getter(index) """
    pass

def groupby(key, seq): # real signature unknown; restored from __doc__
    """
    groupby(key, seq) -> dict
    
        Group a collection by a key function
    
        >>> names = ['Alice', 'Bob', 'Charlie', 'Dan', 'Edith', 'Frank']
        >>> groupby(len, names)  # doctest: +SKIP
        {3: ['Bob', 'Dan'], 5: ['Alice', 'Edith', 'Frank'], 7: ['Charlie']}
    
        >>> iseven = lambda x: x % 2 == 0
        >>> groupby(iseven, [1, 2, 3, 4, 5, 6, 7, 8])  # doctest: +SKIP
        {False: [1, 3, 5, 7], True: [2, 4, 6, 8]}
    
        Non-callable keys imply grouping on a member.
    
        >>> groupby('gender', [{'name': 'Alice', 'gender': 'F'},
        ...                    {'name': 'Bob', 'gender': 'M'},
        ...                    {'name': 'Charlie', 'gender': 'M'}]) # doctest:+SKIP
        {'F': [{'gender': 'F', 'name': 'Alice'}],
         'M': [{'gender': 'M', 'name': 'Bob'},
               {'gender': 'M', 'name': 'Charlie'}]}
    
        Not to be confused with ``itertools.groupby``
    
        See Also:
            countby
    """
    return {}

def identity(x): # real signature unknown; restored from __doc__
    """ identity(x) """
    pass

def isdistinct(seq): # real signature unknown; restored from __doc__
    """
    isdistinct(seq)
    
        All values in sequence are distinct
    
        >>> isdistinct([1, 2, 3])
        True
        >>> isdistinct([1, 2, 1])
        False
    
        >>> isdistinct("Hello")
        False
        >>> isdistinct("World")
        True
    """
    pass

def isiterable(x): # real signature unknown; restored from __doc__
    """
    isiterable(x)
    
        Is x iterable?
    
        >>> isiterable([1, 2, 3])
        True
        >>> isiterable('abc')
        True
        >>> isiterable(5)
        False
    """
    pass

def join(leftkey, leftseq, rightkey, rightseq, left_default='__no__default__', right_default='__no__default__'): # real signature unknown; restored from __doc__
    """
    join(leftkey, leftseq, rightkey, rightseq, left_default='__no__default__', right_default='__no__default__')
    
        Join two sequences on common attributes
    
        This is a semi-streaming operation.  The LEFT sequence is fully evaluated
        and placed into memory.  The RIGHT sequence is evaluated lazily and so can
        be arbitrarily large.
        (Note: If right_default is defined, then unique keys of rightseq
            will also be stored in memory.)
    
        >>> friends = [('Alice', 'Edith'),
        ...            ('Alice', 'Zhao'),
        ...            ('Edith', 'Alice'),
        ...            ('Zhao', 'Alice'),
        ...            ('Zhao', 'Edith')]
    
        >>> cities = [('Alice', 'NYC'),
        ...           ('Alice', 'Chicago'),
        ...           ('Dan', 'Syndey'),
        ...           ('Edith', 'Paris'),
        ...           ('Edith', 'Berlin'),
        ...           ('Zhao', 'Shanghai')]
    
        >>> # Vacation opportunities
        >>> # In what cities do people have friends?
        >>> result = join(second, friends,
        ...               first, cities)
        >>> for ((a, b), (c, d)) in sorted(unique(result)):
        ...     print((a, d))
        ('Alice', 'Berlin')
        ('Alice', 'Paris')
        ('Alice', 'Shanghai')
        ('Edith', 'Chicago')
        ('Edith', 'NYC')
        ('Zhao', 'Chicago')
        ('Zhao', 'NYC')
        ('Zhao', 'Berlin')
        ('Zhao', 'Paris')
    
        Specify outer joins with keyword arguments ``left_default`` and/or
        ``right_default``.  Here is a full outer join in which unmatched elements
        are paired with None.
    
        >>> identity = lambda x: x
        >>> list(join(identity, [1, 2, 3],
        ...           identity, [2, 3, 4],
        ...           left_default=None, right_default=None))
        [(2, 2), (3, 3), (None, 4), (1, None)]
    
        Usually the key arguments are callables to be applied to the sequences.  If
        the keys are not obviously callable then it is assumed that indexing was
        intended, e.g. the following is a legal change.
        The join is implemented as a hash join and the keys of leftseq must be
        hashable. Additionally, if right_default is defined, then keys of rightseq
        must also be hashable.
    
        >>> # result = join(second, friends, first, cities)
        >>> result = join(1, friends, 0, cities)  # doctest: +SKIP
    """
    pass

def last(seq): # real signature unknown; restored from __doc__
    """
    last(seq)
    
        The last element in a sequence
    
        >>> last('ABC')
        'C'
    """
    pass

def mapcat(func, seqs): # real signature unknown; restored from __doc__
    """
    mapcat(func, seqs)
    
        Apply func to each sequence in seqs, concatenating results.
    
        >>> list(mapcat(lambda s: [c.upper() for c in s],
        ...             [["a", "b"], ["c", "d", "e"]]))
        ['A', 'B', 'C', 'D', 'E']
    """
    pass

def merge_sorted(*seqs, **kwargs): # real signature unknown; restored from __doc__
    """
    merge_sorted(*seqs, **kwargs)
    
        Merge and sort a collection of sorted collections
    
        This works lazily and only keeps one value from each iterable in memory.
    
        >>> list(merge_sorted([1, 3, 5], [2, 4, 6]))
        [1, 2, 3, 4, 5, 6]
    
        >>> ''.join(merge_sorted('abc', 'abc', 'abc'))
        'aaabbbccc'
    
        The "key" function used to sort the input may be passed as a keyword.
    
        >>> list(merge_sorted([2, 3], [1, 3], key=lambda x: x // 3))
        [2, 1, 3, 3]
    """
    pass

def nth(Py_ssize_t_n, seq): # real signature unknown; restored from __doc__
    """
    nth(Py_ssize_t n, seq)
    
        The nth element in a sequence
    
        >>> nth(1, 'ABC')
        'B'
    """
    pass

def partition(Py_ssize_t_n, seq, pad='__no__pad__'): # real signature unknown; restored from __doc__
    """
    partition(Py_ssize_t n, seq, pad='__no__pad__')
    
        Partition sequence into tuples of length n
    
        >>> list(partition(2, [1, 2, 3, 4]))
        [(1, 2), (3, 4)]
    
        If the length of ``seq`` is not evenly divisible by ``n``, the final tuple
        is dropped if ``pad`` is not specified, or filled to length ``n`` by pad:
    
        >>> list(partition(2, [1, 2, 3, 4, 5]))
        [(1, 2), (3, 4)]
    
        >>> list(partition(2, [1, 2, 3, 4, 5], pad=None))
        [(1, 2), (3, 4), (5, None)]
    
        See Also:
            partition_all
    """
    pass

def peek(seq): # real signature unknown; restored from __doc__
    """
    peek(seq)
    
        Retrieve the next element of a sequence
    
        Returns the first element and an iterable equivalent to the original
        sequence, still having the element retrieved.
    
        >>> seq = [0, 1, 2, 3, 4]
        >>> first, seq = peek(seq)
        >>> first
        0
        >>> list(seq)
        [0, 1, 2, 3, 4]
    """
    pass

def peekn(Py_ssize_t_n, seq): # real signature unknown; restored from __doc__
    """
    peekn(Py_ssize_t n, seq)
    
        Retrieve the next n elements of a sequence
    
        Returns a tuple of the first n elements and an iterable equivalent
        to the original, still having the elements retrieved.
    
        >>> seq = [0, 1, 2, 3, 4]
        >>> first_two, seq = peekn(2, seq)
        >>> first_two
        (0, 1)
        >>> list(seq)
        [0, 1, 2, 3, 4]
    """
    pass

def pluck(ind, seqs, default='__no__default__'): # real signature unknown; restored from __doc__
    """
    pluck(ind, seqs, default='__no__default__')
    
        plucks an element or several elements from each item in a sequence.
    
        ``pluck`` maps ``itertoolz.get`` over a sequence and returns one or more
        elements of each item in the sequence.
    
        This is equivalent to running `map(curried.get(ind), seqs)`
    
        ``ind`` can be either a single string/index or a list of strings/indices.
        ``seqs`` should be sequence containing sequences or dicts.
    
        e.g.
    
        >>> data = [{'id': 1, 'name': 'Cheese'}, {'id': 2, 'name': 'Pies'}]
        >>> list(pluck('name', data))
        ['Cheese', 'Pies']
        >>> list(pluck([0, 1], [[1, 2, 3], [4, 5, 7]]))
        [(1, 2), (4, 5)]
    
        See Also:
            get
            map
    """
    pass

def reduceby(key, binop, seq, init='__no__default__'): # real signature unknown; restored from __doc__
    """
    reduceby(key, binop, seq, init='__no__default__') -> dict
    
        Perform a simultaneous groupby and reduction
    
        The computation:
    
        >>> result = reduceby(key, binop, seq, init)      # doctest: +SKIP
    
        is equivalent to the following:
    
        >>> def reduction(group):                           # doctest: +SKIP
        ...     return reduce(binop, group, init)           # doctest: +SKIP
    
        >>> groups = groupby(key, seq)                    # doctest: +SKIP
        >>> result = valmap(reduction, groups)              # doctest: +SKIP
    
        But the former does not build the intermediate groups, allowing it to
        operate in much less space.  This makes it suitable for larger datasets
        that do not fit comfortably in memory
    
        The ``init`` keyword argument is the default initialization of the
        reduction.  This can be either a constant value like ``0`` or a callable
        like ``lambda : 0`` as might be used in ``defaultdict``.
    
        Simple Examples
        ---------------
    
        >>> from operator import add, mul
        >>> iseven = lambda x: x % 2 == 0
    
        >>> data = [1, 2, 3, 4, 5]
    
        >>> reduceby(iseven, add, data)  # doctest: +SKIP
        {False: 9, True: 6}
    
        >>> reduceby(iseven, mul, data)  # doctest: +SKIP
        {False: 15, True: 8}
    
        Complex Example
        ---------------
    
        >>> projects = [{'name': 'build roads', 'state': 'CA', 'cost': 1000000},
        ...             {'name': 'fight crime', 'state': 'IL', 'cost': 100000},
        ...             {'name': 'help farmers', 'state': 'IL', 'cost': 2000000},
        ...             {'name': 'help farmers', 'state': 'CA', 'cost': 200000}]
    
        >>> reduceby('state',                        # doctest: +SKIP
        ...          lambda acc, x: acc + x['cost'],
        ...          projects, 0)
        {'CA': 1200000, 'IL': 2100000}
    
        Example Using ``init``
        ----------------------
    
        >>> def set_add(s, i):
        ...     s.add(i)
        ...     return s
    
        >>> reduceby(iseven, set_add, [1, 2, 3, 4, 1, 2, 3], set)  # doctest: +SKIP
        {True:  set([2, 4]),
         False: set([1, 3])}
    """
    return {}

def rest(seq): # real signature unknown; restored from __doc__
    """ rest(seq) """
    pass

def second(seq): # real signature unknown; restored from __doc__
    """
    second(seq)
    
        The second element in a sequence
    
        >>> second('ABC')
        'B'
    """
    pass

def tail(Py_ssize_t_n, seq): # real signature unknown; restored from __doc__
    """
    tail(Py_ssize_t n, seq)
    
        The last n elements of a sequence
    
        >>> tail(2, [10, 20, 30, 40, 50])
        [40, 50]
    
        See Also:
            drop
            take
    """
    pass

def take(Py_ssize_t_n, seq): # real signature unknown; restored from __doc__
    """
    take(Py_ssize_t n, seq)
    
        The first n elements of a sequence
    
        >>> list(take(2, [10, 20, 30, 40, 50]))
        [10, 20]
    
        See Also:
            drop
            tail
    """
    pass

def take_nth(Py_ssize_t_n, seq): # real signature unknown; restored from __doc__
    """
    take_nth(Py_ssize_t n, seq)
    
        Every nth item in seq
    
        >>> list(take_nth(2, [10, 20, 30, 40, 50]))
        [10, 30, 50]
    """
    pass

def topk(Py_ssize_t_k, seq, key=None): # real signature unknown; restored from __doc__
    """
    topk(Py_ssize_t k, seq, key=None)
    
        Find the k largest elements of a sequence
    
        Operates lazily in ``n*log(k)`` time
    
        >>> topk(2, [1, 100, 10, 1000])
        (1000, 100)
    
        Use a key function to change sorted order
    
        >>> topk(2, ['Alice', 'Bob', 'Charlie', 'Dan'], key=len)
        ('Charlie', 'Alice')
    
        See also:
            heapq.nlargest
    """
    pass

def unique(seq, key=None): # real signature unknown; restored from __doc__
    """
    unique(seq, key=None)
    
        Return only unique elements of a sequence
    
        >>> tuple(unique((1, 2, 3)))
        (1, 2, 3)
        >>> tuple(unique((1, 2, 1, 3)))
        (1, 2, 3)
    
        Uniqueness can be defined by key keyword
    
        >>> tuple(unique(['cat', 'mouse', 'dog', 'hen'], key=len))
        ('cat', 'mouse')
    """
    pass

def __pyx_unpickle__getter_null(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle__getter_null(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __reduce_cython__(self): # real signature unknown; restored from __doc__
    """ random_sample.__reduce_cython__(self) """
    pass

def __setstate_cython__(self, __pyx_state): # real signature unknown; restored from __doc__
    """ random_sample.__setstate_cython__(self, __pyx_state) """
    pass

# classes

from .accumulate import accumulate
from .deque import deque
from .interleave import interleave
from .interpose import interpose
from .itemgetter import itemgetter
from .iterate import iterate
from .map import map
from .partition_all import partition_all
from .Random import Random
from .random_sample import random_sample
from .remove import remove
from .sliding_window import sliding_window
from .zip import zip
from ._diff_identity import _diff_identity
from ._diff_key import _diff_key
from ._getter_index import _getter_index
from ._getter_list import _getter_list
from ._getter_null import _getter_null
from ._join import _join
from ._inner_join import _inner_join
from ._inner_join_index import _inner_join_index
from ._inner_join_indices import _inner_join_indices
from ._inner_join_key import _inner_join_key
from ._left_outer_join import _left_outer_join
from ._left_outer_join_index import _left_outer_join_index
from ._left_outer_join_indices import _left_outer_join_indices
from ._left_outer_join_key import _left_outer_join_key
from ._merge_sorted import _merge_sorted
from ._merge_sorted_key import _merge_sorted_key
from ._outer_join import _outer_join
from ._outer_join_index import _outer_join_index
from ._outer_join_indices import _outer_join_indices
from ._outer_join_key import _outer_join_key
from ._pluck_index import _pluck_index
from ._pluck_index_default import _pluck_index_default
from ._pluck_list import _pluck_list
from ._pluck_list_default import _pluck_list_default
from ._right_outer_join import _right_outer_join
from ._right_outer_join_index import _right_outer_join_index
from ._right_outer_join_indices import _right_outer_join_indices
from ._right_outer_join_key import _right_outer_join_key
from ._unique_identity import _unique_identity
from ._unique_key import _unique_key
# variables with complex values

__all__ = [
    'remove',
    'accumulate',
    'groupby',
    'merge_sorted',
    'interleave',
    'unique',
    'isiterable',
    'isdistinct',
    'take',
    'drop',
    'take_nth',
    'first',
    'second',
    'nth',
    'last',
    'get',
    'concat',
    'concatv',
    'mapcat',
    'cons',
    'interpose',
    'frequencies',
    'reduceby',
    'iterate',
    'sliding_window',
    'partition',
    'partition_all',
    'count',
    'pluck',
    'join',
    'tail',
    'diff',
    'topk',
    'peek',
    'peekn',
    'random_sample',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000212791F5F98>'

__pyx_capi__ = {
    'c_diff': None, # (!) real value is '<capsule object "PyObject *(PyObject *, struct __pyx_opt_args_7cytoolz_9itertoolz_c_diff *__pyx_optional_args)" at 0x0000021279089B70>'
    'c_merge_sorted': None, # (!) real value is '<capsule object "PyObject *(PyObject *, struct __pyx_opt_args_7cytoolz_9itertoolz_c_merge_sorted *__pyx_optional_args)" at 0x0000021279089690>'
    'concat': None, # (!) real value is '<capsule object "PyObject *(PyObject *, int __pyx_skip_dispatch)" at 0x00000212790899C0>'
    'cons': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyObject *, int __pyx_skip_dispatch)" at 0x0000021279089990>'
    'count': None, # (!) real value is '<capsule object "PyObject *(PyObject *, int __pyx_skip_dispatch)" at 0x0000021279089AB0>'
    'drop': None, # (!) real value is '<capsule object "PyObject *(Py_ssize_t, PyObject *, int __pyx_skip_dispatch)" at 0x0000021279089810>'
    'first': None, # (!) real value is '<capsule object "PyObject *(PyObject *, int __pyx_skip_dispatch)" at 0x0000021279089870>'
    'frequencies': None, # (!) real value is '<capsule object "PyObject *(PyObject *, int __pyx_skip_dispatch)" at 0x0000021279089A20>'
    'get': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyObject *, int __pyx_skip_dispatch, struct __pyx_opt_args_7cytoolz_9itertoolz_get *__pyx_optional_args)" at 0x0000021279089960>'
    'getter': None, # (!) real value is '<capsule object "PyObject *(PyObject *, int __pyx_skip_dispatch)" at 0x0000021279089B10>'
    'groupby': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyObject *, int __pyx_skip_dispatch)" at 0x0000021279089660>'
    'isdistinct': None, # (!) real value is '<capsule object "PyObject *(PyObject *, int __pyx_skip_dispatch)" at 0x0000021279089780>'
    'isiterable': None, # (!) real value is '<capsule object "PyObject *(PyObject *, int __pyx_skip_dispatch)" at 0x0000021279089750>'
    'join': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyObject *, PyObject *, PyObject *, int __pyx_skip_dispatch, struct __pyx_opt_args_7cytoolz_9itertoolz_join *__pyx_optional_args)" at 0x0000021279089B40>'
    'last': None, # (!) real value is '<capsule object "PyObject *(PyObject *, int __pyx_skip_dispatch)" at 0x0000021279089900>'
    'mapcat': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyObject *, int __pyx_skip_dispatch)" at 0x00000212790899F0>'
    'nth': None, # (!) real value is '<capsule object "PyObject *(Py_ssize_t, PyObject *, int __pyx_skip_dispatch)" at 0x00000212790898D0>'
    'partition': None, # (!) real value is '<capsule object "PyObject *(Py_ssize_t, PyObject *, int __pyx_skip_dispatch, struct __pyx_opt_args_7cytoolz_9itertoolz_partition *__pyx_optional_args)" at 0x0000021279089A80>'
    'peek': None, # (!) real value is '<capsule object "PyObject *(PyObject *, int __pyx_skip_dispatch)" at 0x0000021279089BD0>'
    'peekn': None, # (!) real value is '<capsule object "PyObject *(Py_ssize_t, PyObject *, int __pyx_skip_dispatch)" at 0x0000021279089C00>'
    'pluck': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyObject *, int __pyx_skip_dispatch, struct __pyx_opt_args_7cytoolz_9itertoolz_pluck *__pyx_optional_args)" at 0x0000021279089AE0>'
    'reduceby': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyObject *, PyObject *, int __pyx_skip_dispatch, struct __pyx_opt_args_7cytoolz_9itertoolz_reduceby *__pyx_optional_args)" at 0x0000021279089A50>'
    'rest': None, # (!) real value is '<capsule object "PyObject *(PyObject *, int __pyx_skip_dispatch)" at 0x0000021279089930>'
    'second': None, # (!) real value is '<capsule object "PyObject *(PyObject *, int __pyx_skip_dispatch)" at 0x00000212790898A0>'
    'tail': None, # (!) real value is '<capsule object "PyObject *(Py_ssize_t, PyObject *, int __pyx_skip_dispatch)" at 0x00000212790897E0>'
    'take': None, # (!) real value is '<capsule object "PyObject *(Py_ssize_t, PyObject *, int __pyx_skip_dispatch)" at 0x00000212790897B0>'
    'take_nth': None, # (!) real value is '<capsule object "PyObject *(Py_ssize_t, PyObject *, int __pyx_skip_dispatch)" at 0x0000021279089840>'
    'topk': None, # (!) real value is '<capsule object "PyObject *(Py_ssize_t, PyObject *, int __pyx_skip_dispatch, struct __pyx_opt_args_7cytoolz_9itertoolz_topk *__pyx_optional_args)" at 0x0000021279089BA0>'
    'unique': None, # (!) real value is '<capsule object "PyObject *(PyObject *, int __pyx_skip_dispatch, struct __pyx_opt_args_7cytoolz_9itertoolz_unique *__pyx_optional_args)" at 0x0000021279089720>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='cytoolz.itertoolz', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000212791F5F98>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\cytoolz\\\\itertoolz.cp37-win_amd64.pyd')"

__test__ = {
    'concat (line 697)': '\n    Concatenate zero or more iterables, any of which may be infinite.\n\n    An infinite sequence will prevent the rest of the arguments from\n    being included.\n\n    We use chain.from_iterable rather than ``chain(*seqs)`` so that seqs\n    can be a generator.\n\n    >>> list(concat([[], [1], [2, 3]]))\n    [1, 2, 3]\n\n    See also:\n        itertools.chain.from_iterable  equivalent\n    ',
    'concatv (line 716)': '\n    Variadic version of concat\n\n    >>> list(concatv([], ["a"], ["b", "c"]))\n    [\'a\', \'b\', \'c\']\n\n    See also:\n        itertools.chain\n    ',
    'cons (line 740)': '\n    Add el to beginning of (possibly infinite) sequence seq.\n\n    >>> list(cons(1, [2, 3]))\n    [1, 2, 3]\n    ',
    'diff (line 1620)': "\n    Return those items that differ between sequences\n\n    >>> list(diff([1, 2, 3], [1, 2, 10, 100]))\n    [(3, 10)]\n\n    Shorter sequences may be padded with a ``default`` value:\n\n    >>> list(diff([1, 2, 3], [1, 2, 10, 100], default=None))\n    [(3, 10), (None, 100)]\n\n    A ``key`` function may also be applied to each item to use during\n    comparisons:\n\n    >>> list(diff(['apples', 'bananas'], ['Apples', 'Oranges'], key=str.lower))\n    [('bananas', 'Oranges')]\n    ",
    'drop (line 517)': '\n    The sequence following the first n elements\n\n    >>> list(drop(2, [10, 20, 30, 40, 50]))\n    [30, 40, 50]\n\n    See Also:\n        take\n        tail\n    ',
    'first (line 551)': "\n    The first element in a sequence\n\n    >>> first('ABC')\n    'A'\n    ",
    'frequencies (line 780)': "\n    Find number of occurrences of each value in seq\n\n    >>> frequencies(['cat', 'cat', 'ox', 'pig', 'pig', 'cat'])  #doctest: +SKIP\n    {'cat': 3, 'ox': 1, 'pig': 2}\n\n    See Also:\n        countby\n        groupby\n    ",
    'get (line 619)': "\n    Get element in a sequence or dict\n\n    Provides standard indexing\n\n    >>> get(1, 'ABC')       # Same as 'ABC'[1]\n    'B'\n\n    Pass a list to get multiple values\n\n    >>> get([1, 2], 'ABC')  # ('ABC'[1], 'ABC'[2])\n    ('B', 'C')\n\n    Works on any value that supports indexing/getitem\n    For example here we see that it works with dictionaries\n\n    >>> phonebook = {'Alice':  '555-1234',\n    ...              'Bob':    '555-5678',\n    ...              'Charlie':'555-9999'}\n    >>> get('Alice', phonebook)\n    '555-1234'\n\n    >>> get(['Alice', 'Bob'], phonebook)\n    ('555-1234', '555-5678')\n\n    Provide a default for missing values\n\n    >>> get(['Alice', 'Dennis'], phonebook, None)\n    ('555-1234', None)\n\n    See Also:\n        pluck\n    ",
    'groupby (line 118)': "\n    Group a collection by a key function\n\n    >>> names = ['Alice', 'Bob', 'Charlie', 'Dan', 'Edith', 'Frank']\n    >>> groupby(len, names)  # doctest: +SKIP\n    {3: ['Bob', 'Dan'], 5: ['Alice', 'Edith', 'Frank'], 7: ['Charlie']}\n\n    >>> iseven = lambda x: x % 2 == 0\n    >>> groupby(iseven, [1, 2, 3, 4, 5, 6, 7, 8])  # doctest: +SKIP\n    {False: [1, 3, 5, 7], True: [2, 4, 6, 8]}\n\n    Non-callable keys imply grouping on a member.\n\n    >>> groupby('gender', [{'name': 'Alice', 'gender': 'F'},\n    ...                    {'name': 'Bob', 'gender': 'M'},\n    ...                    {'name': 'Charlie', 'gender': 'M'}]) # doctest:+SKIP\n    {'F': [{'gender': 'F', 'name': 'Alice'}],\n     'M': [{'gender': 'M', 'name': 'Bob'},\n           {'gender': 'M', 'name': 'Charlie'}]}\n\n    Not to be confused with ``itertools.groupby``\n\n    See Also:\n        countby\n    ",
    'isdistinct (line 462)': '\n    All values in sequence are distinct\n\n    >>> isdistinct([1, 2, 3])\n    True\n    >>> isdistinct([1, 2, 1])\n    False\n\n    >>> isdistinct("Hello")\n    False\n    >>> isdistinct("World")\n    True\n    ',
    'isiterable (line 443)': "\n    Is x iterable?\n\n    >>> isiterable([1, 2, 3])\n    True\n    >>> isiterable('abc')\n    True\n    >>> isiterable(5)\n    False\n    ",
    'join (line 1247)': "\n    Join two sequences on common attributes\n\n    This is a semi-streaming operation.  The LEFT sequence is fully evaluated\n    and placed into memory.  The RIGHT sequence is evaluated lazily and so can\n    be arbitrarily large.\n    (Note: If right_default is defined, then unique keys of rightseq\n        will also be stored in memory.)\n\n    >>> friends = [('Alice', 'Edith'),\n    ...            ('Alice', 'Zhao'),\n    ...            ('Edith', 'Alice'),\n    ...            ('Zhao', 'Alice'),\n    ...            ('Zhao', 'Edith')]\n\n    >>> cities = [('Alice', 'NYC'),\n    ...           ('Alice', 'Chicago'),\n    ...           ('Dan', 'Syndey'),\n    ...           ('Edith', 'Paris'),\n    ...           ('Edith', 'Berlin'),\n    ...           ('Zhao', 'Shanghai')]\n\n    >>> # Vacation opportunities\n    >>> # In what cities do people have friends?\n    >>> result = join(second, friends,\n    ...               first, cities)\n    >>> for ((a, b), (c, d)) in sorted(unique(result)):\n    ...     print((a, d))\n    ('Alice', 'Berlin')\n    ('Alice', 'Paris')\n    ('Alice', 'Shanghai')\n    ('Edith', 'Chicago')\n    ('Edith', 'NYC')\n    ('Zhao', 'Chicago')\n    ('Zhao', 'NYC')\n    ('Zhao', 'Berlin')\n    ('Zhao', 'Paris')\n\n    Specify outer joins with keyword arguments ``left_default`` and/or\n    ``right_default``.  Here is a full outer join in which unmatched elements\n    are paired with None.\n\n    >>> identity = lambda x: x\n    >>> list(join(identity, [1, 2, 3],\n    ...           identity, [2, 3, 4],\n    ...           left_default=None, right_default=None))\n    [(2, 2), (3, 3), (None, 4), (1, None)]\n\n    Usually the key arguments are callables to be applied to the sequences.  If\n    the keys are not obviously callable then it is assumed that indexing was\n    intended, e.g. the following is a legal change.\n    The join is implemented as a hash join and the keys of leftseq must be\n    hashable. Additionally, if right_default is defined, then keys of rightseq\n    must also be hashable.\n\n    >>> # result = join(second, friends, first, cities)\n    >>> result = join(1, friends, 0, cities)  # doctest: +SKIP\n    ",
    'last (line 591)': "\n    The last element in a sequence\n\n    >>> last('ABC')\n    'C'\n    ",
    'mapcat (line 729)': '\n    Apply func to each sequence in seqs, concatenating results.\n\n    >>> list(mapcat(lambda s: [c.upper() for c in s],\n    ...             [["a", "b"], ["c", "d", "e"]]))\n    [\'A\', \'B\', \'C\', \'D\', \'E\']\n    ',
    'merge_sorted (line 295)': '\n    Merge and sort a collection of sorted collections\n\n    This works lazily and only keeps one value from each iterable in memory.\n\n    >>> list(merge_sorted([1, 3, 5], [2, 4, 6]))\n    [1, 2, 3, 4, 5, 6]\n\n    >>> \'\'.join(merge_sorted(\'abc\', \'abc\', \'abc\'))\n    \'aaabbbccc\'\n\n    The "key" function used to sort the input may be passed as a keyword.\n\n    >>> list(merge_sorted([2, 3], [1, 3], key=lambda x: x // 3))\n    [2, 1, 3, 3]\n    ',
    'nth (line 573)': "\n    The nth element in a sequence\n\n    >>> nth(1, 'ABC')\n    'B'\n    ",
    'partition (line 995)': '\n    Partition sequence into tuples of length n\n\n    >>> list(partition(2, [1, 2, 3, 4]))\n    [(1, 2), (3, 4)]\n\n    If the length of ``seq`` is not evenly divisible by ``n``, the final tuple\n    is dropped if ``pad`` is not specified, or filled to length ``n`` by pad:\n\n    >>> list(partition(2, [1, 2, 3, 4, 5]))\n    [(1, 2), (3, 4)]\n\n    >>> list(partition(2, [1, 2, 3, 4, 5], pad=None))\n    [(1, 2), (3, 4), (5, None)]\n\n    See Also:\n        partition_all\n    ',
    'peek (line 1718)': '\n    Retrieve the next element of a sequence\n\n    Returns the first element and an iterable equivalent to the original\n    sequence, still having the element retrieved.\n\n    >>> seq = [0, 1, 2, 3, 4]\n    >>> first, seq = peek(seq)\n    >>> first\n    0\n    >>> list(seq)\n    [0, 1, 2, 3, 4]\n    ',
    'peekn (line 1737)': '\n    Retrieve the next n elements of a sequence\n\n    Returns a tuple of the first n elements and an iterable equivalent\n    to the original, still having the elements retrieved.\n\n    >>> seq = [0, 1, 2, 3, 4]\n    >>> first_two, seq = peekn(2, seq)\n    >>> first_two\n    (0, 1)\n    >>> list(seq)\n    [0, 1, 2, 3, 4]\n    ',
    'pluck (line 1171)': "\n    plucks an element or several elements from each item in a sequence.\n\n    ``pluck`` maps ``itertoolz.get`` over a sequence and returns one or more\n    elements of each item in the sequence.\n\n    This is equivalent to running `map(curried.get(ind), seqs)`\n\n    ``ind`` can be either a single string/index or a list of strings/indices.\n    ``seqs`` should be sequence containing sequences or dicts.\n\n    e.g.\n\n    >>> data = [{'id': 1, 'name': 'Cheese'}, {'id': 2, 'name': 'Pies'}]\n    >>> list(pluck('name', data))\n    ['Cheese', 'Pies']\n    >>> list(pluck([0, 1], [[1, 2, 3], [4, 5, 7]]))\n    [(1, 2), (4, 5)]\n\n    See Also:\n        get\n        map\n    ",
    'reduceby (line 817)': "\n    Perform a simultaneous groupby and reduction\n\n    The computation:\n\n    >>> result = reduceby(key, binop, seq, init)      # doctest: +SKIP\n\n    is equivalent to the following:\n\n    >>> def reduction(group):                           # doctest: +SKIP\n    ...     return reduce(binop, group, init)           # doctest: +SKIP\n\n    >>> groups = groupby(key, seq)                    # doctest: +SKIP\n    >>> result = valmap(reduction, groups)              # doctest: +SKIP\n\n    But the former does not build the intermediate groups, allowing it to\n    operate in much less space.  This makes it suitable for larger datasets\n    that do not fit comfortably in memory\n\n    The ``init`` keyword argument is the default initialization of the\n    reduction.  This can be either a constant value like ``0`` or a callable\n    like ``lambda : 0`` as might be used in ``defaultdict``.\n\n    Simple Examples\n    ---------------\n\n    >>> from operator import add, mul\n    >>> iseven = lambda x: x % 2 == 0\n\n    >>> data = [1, 2, 3, 4, 5]\n\n    >>> reduceby(iseven, add, data)  # doctest: +SKIP\n    {False: 9, True: 6}\n\n    >>> reduceby(iseven, mul, data)  # doctest: +SKIP\n    {False: 15, True: 8}\n\n    Complex Example\n    ---------------\n\n    >>> projects = [{'name': 'build roads', 'state': 'CA', 'cost': 1000000},\n    ...             {'name': 'fight crime', 'state': 'IL', 'cost': 100000},\n    ...             {'name': 'help farmers', 'state': 'IL', 'cost': 2000000},\n    ...             {'name': 'help farmers', 'state': 'CA', 'cost': 200000}]\n\n    >>> reduceby('state',                        # doctest: +SKIP\n    ...          lambda acc, x: acc + x['cost'],\n    ...          projects, 0)\n    {'CA': 1200000, 'IL': 2100000}\n\n    Example Using ``init``\n    ----------------------\n\n    >>> def set_add(s, i):\n    ...     s.add(i)\n    ...     return s\n\n    >>> reduceby(iseven, set_add, [1, 2, 3, 4, 1, 2, 3], set)  # doctest: +SKIP\n    {True:  set([2, 4]),\n     False: set([1, 3])}\n    ",
    'second (line 561)': "\n    The second element in a sequence\n\n    >>> second('ABC')\n    'B'\n    ",
    'tail (line 501)': '\n    The last n elements of a sequence\n\n    >>> tail(2, [10, 20, 30, 40, 50])\n    [40, 50]\n\n    See Also:\n        drop\n        take\n    ',
    'take (line 487)': '\n    The first n elements of a sequence\n\n    >>> list(take(2, [10, 20, 30, 40, 50]))\n    [10, 20]\n\n    See Also:\n        drop\n        tail\n    ',
    'take_nth (line 541)': '\n    Every nth item in seq\n\n    >>> list(take_nth(2, [10, 20, 30, 40, 50]))\n    [10, 30, 50]\n    ',
    'topk (line 1646)': "\n    Find the k largest elements of a sequence\n\n    Operates lazily in ``n*log(k)`` time\n\n    >>> topk(2, [1, 100, 10, 1000])\n    (1000, 100)\n\n    Use a key function to change sorted order\n\n    >>> topk(2, ['Alice', 'Bob', 'Charlie', 'Dan'], key=len)\n    ('Charlie', 'Alice')\n\n    See also:\n        heapq.nlargest\n    ",
    'unique (line 423)': "\n    Return only unique elements of a sequence\n\n    >>> tuple(unique((1, 2, 3)))\n    (1, 2, 3)\n    >>> tuple(unique((1, 2, 1, 3)))\n    (1, 2, 3)\n\n    Uniqueness can be defined by key keyword\n\n    >>> tuple(unique(['cat', 'mouse', 'dog', 'hen'], key=len))\n    ('cat', 'mouse')\n    ",
}

