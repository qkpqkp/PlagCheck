# encoding: utf-8
# module cytoolz.dicttoolz
# from C:\Users\Doly\Anaconda3\lib\site-packages\cytoolz\dicttoolz.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

# functions

def assoc(d, key, value, factory=None): # real signature unknown; restored from __doc__
    """
    assoc(d, key, value, factory=dict)
    
        Return a new dict with new key value pair
    
        New dict has d[key] set to value. Does not modify the initial dictionary.
    
        >>> assoc({'x': 1}, 'x', 2)
        {'x': 2}
        >>> assoc({'x': 1}, 'y', 3)   # doctest: +SKIP
        {'x': 1, 'y': 3}
    """
    pass

def assoc_in(d, keys, value, factory=None): # real signature unknown; restored from __doc__
    """
    assoc_in(d, keys, value, factory=dict)
    
        Return a new dict with new, potentially nested, key value pair
    
        >>> purchase = {'name': 'Alice',
        ...             'order': {'items': ['Apple', 'Orange'],
        ...                       'costs': [0.50, 1.25]},
        ...             'credit card': '5555-1234-1234-1234'}
        >>> assoc_in(purchase, ['order', 'costs'], [0.25, 1.00]) # doctest: +SKIP
        {'credit card': '5555-1234-1234-1234',
         'name': 'Alice',
         'order': {'costs': [0.25, 1.00], 'items': ['Apple', 'Orange']}}
    """
    pass

def copy(x): # reliably restored by inspect
    """
    Shallow copy operation on arbitrary Python objects.
    
        See the module's __doc__ string for more info.
    """
    pass

def dissoc(d, *keys, **kwargs): # real signature unknown; restored from __doc__
    """
    dissoc(d, *keys, **kwargs)
    
        Return a new dict with the given key(s) removed.
    
        New dict has d[key] deleted for each supplied key.
        Does not modify the initial dictionary.
    
        >>> dissoc({'x': 1, 'y': 2}, 'y')
        {'x': 1}
        >>> dissoc({'x': 1, 'y': 2}, 'y', 'x')
        {}
        >>> dissoc({'x': 1}, 'y') # Ignores missing keys
        {'x': 1}
    """
    pass

def get_in(keys, coll, default=None, no_default=False): # real signature unknown; restored from __doc__
    """
    get_in(keys, coll, default=None, no_default=False)
    
        Returns coll[i0][i1]...[iX] where [i0, i1, ..., iX]==keys.
    
        If coll[i0][i1]...[iX] cannot be found, returns ``default``, unless
        ``no_default`` is specified, then it raises KeyError or IndexError.
    
        ``get_in`` is a generalization of ``operator.getitem`` for nested data
        structures such as dictionaries and lists.
    
        >>> transaction = {'name': 'Alice',
        ...                'purchase': {'items': ['Apple', 'Orange'],
        ...                             'costs': [0.50, 1.25]},
        ...                'credit card': '5555-1234-1234-1234'}
        >>> get_in(['purchase', 'items', 0], transaction)
        'Apple'
        >>> get_in(['name'], transaction)
        'Alice'
        >>> get_in(['purchase', 'total'], transaction)
        >>> get_in(['purchase', 'items', 'apple'], transaction)
        >>> get_in(['purchase', 'items', 10], transaction)
        >>> get_in(['purchase', 'total'], transaction, 0)
        0
        >>> get_in(['y'], {}, no_default=True)
        Traceback (most recent call last):
            ...
        KeyError: 'y'
    
        See Also:
            itertoolz.get
            operator.getitem
    """
    pass

def itemfilter(predicate, d, factory=None): # real signature unknown; restored from __doc__
    """
    itemfilter(predicate, d, factory=dict)
    
        Filter items in dictionary by item
    
        >>> def isvalid(item):
        ...     k, v = item
        ...     return k % 2 == 0 and v < 4
    
        >>> d = {1: 2, 2: 3, 3: 4, 4: 5}
        >>> itemfilter(isvalid, d)
        {2: 3}
    
        See Also:
            keyfilter
            valfilter
            itemmap
    """
    pass

def itemmap(func, d, factory=None): # real signature unknown; restored from __doc__
    """
    itemmap(func, d, factory=dict)
    
        Apply function to items of dictionary
    
        >>> accountids = {"Alice": 10, "Bob": 20}
        >>> itemmap(reversed, accountids)  # doctest: +SKIP
        {10: "Alice", 20: "Bob"}
    
        See Also:
            keymap
            valmap
    """
    pass

def keyfilter(predicate, d, factory=None): # real signature unknown; restored from __doc__
    """
    keyfilter(predicate, d, factory=dict)
    
        Filter items in dictionary by key
    
        >>> iseven = lambda x: x % 2 == 0
        >>> d = {1: 2, 2: 3, 3: 4, 4: 5}
        >>> keyfilter(iseven, d)
        {2: 3, 4: 5}
    
        See Also:
            valfilter
            itemfilter
            keymap
    """
    pass

def keymap(func, d, factory=None): # real signature unknown; restored from __doc__
    """
    keymap(func, d, factory=dict)
    
        Apply function to keys of dictionary
    
        >>> bills = {"Alice": [20, 15, 30], "Bob": [10, 35]}
        >>> keymap(str.lower, bills)  # doctest: +SKIP
        {'alice': [20, 15, 30], 'bob': [10, 35]}
    
        See Also:
            valmap
            itemmap
    """
    pass

def merge(*dicts, **kwargs): # real signature unknown; restored from __doc__
    """
    merge(*dicts, **kwargs)
    
        Merge a collection of dictionaries
    
        >>> merge({1: 'one'}, {2: 'two'})
        {1: 'one', 2: 'two'}
    
        Later dictionaries have precedence
    
        >>> merge({1: 2, 3: 4}, {3: 3, 4: 4})
        {1: 2, 3: 3, 4: 4}
    
        See Also:
            merge_with
    """
    pass

def merge_with(func, *dicts, **kwargs): # real signature unknown; restored from __doc__
    """
    merge_with(func, *dicts, **kwargs)
    
        Merge dictionaries and apply function to combined values
    
        A key may occur in more than one dict, and all values mapped from the key
        will be passed to the function as a list, such as func([val1, val2, ...]).
    
        >>> merge_with(sum, {1: 1, 2: 2}, {1: 10, 2: 20})
        {1: 11, 2: 22}
    
        >>> merge_with(first, {1: 1, 2: 2}, {2: 20, 3: 30})  # doctest: +SKIP
        {1: 1, 2: 2, 3: 30}
    
        See Also:
            merge
    """
    pass

def update_in(d, keys, func, default=None, factory=None): # real signature unknown; restored from __doc__
    """
    update_in(d, keys, func, default=None, factory=dict)
    
        Update value in a (potentially) nested dictionary
    
        inputs:
        d - dictionary on which to operate
        keys - list or tuple giving the location of the value to be changed in d
        func - function to operate on that value
    
        If keys == [k0,..,kX] and d[k0]..[kX] == v, update_in returns a copy of the
        original dictionary with v replaced by func(v), but does not mutate the
        original dictionary.
    
        If k0 is not a key in d, update_in creates nested dictionaries to the depth
        specified by the keys, with the innermost value set to func(default).
    
        >>> inc = lambda x: x + 1
        >>> update_in({'a': 0}, ['a'], inc)
        {'a': 1}
    
        >>> transaction = {'name': 'Alice',
        ...                'purchase': {'items': ['Apple', 'Orange'],
        ...                             'costs': [0.50, 1.25]},
        ...                'credit card': '5555-1234-1234-1234'}
        >>> update_in(transaction, ['purchase', 'costs'], sum) # doctest: +SKIP
        {'credit card': '5555-1234-1234-1234',
         'name': 'Alice',
         'purchase': {'costs': 1.75, 'items': ['Apple', 'Orange']}}
    
        >>> # updating a value when k0 is not in d
        >>> update_in({}, [1, 2, 3], str, default="bar")
        {1: {2: {3: 'bar'}}}
        >>> update_in({1: 'foo'}, [2, 3, 4], inc, 0)
        {1: 'foo', 2: {3: {4: 1}}}
    """
    pass

def valfilter(predicate, d, factory=None): # real signature unknown; restored from __doc__
    """
    valfilter(predicate, d, factory=dict)
    
        Filter items in dictionary by value
    
        >>> iseven = lambda x: x % 2 == 0
        >>> d = {1: 2, 2: 3, 3: 4, 4: 5}
        >>> valfilter(iseven, d)
        {1: 2, 3: 4}
    
        See Also:
            keyfilter
            itemfilter
            valmap
    """
    pass

def valmap(func, d, factory=None): # real signature unknown; restored from __doc__
    """
    valmap(func, d, factory=dict)
    
        Apply function to values of dictionary
    
        >>> bills = {"Alice": [20, 15, 30], "Bob": [10, 35]}
        >>> valmap(sum, bills)  # doctest: +SKIP
        {'Alice': 65, 'Bob': 45}
    
        See Also:
            keymap
            itemmap
    """
    pass

def __reduce_cython__(self): # real signature unknown; restored from __doc__
    """ _iter_mapping.__reduce_cython__(self) """
    pass

def __setstate_cython__(self, __pyx_state): # real signature unknown; restored from __doc__
    """ _iter_mapping.__setstate_cython__(self, __pyx_state) """
    pass

# classes

class _iter_mapping(object):
    """ Keep a handle on the current item to prevent memory clean up too early """
    def __init__(self, *args, **kwargs): # real signature unknown
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
        """ _iter_mapping.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ _iter_mapping.__setstate_cython__(self, __pyx_state) """
        pass


# variables with complex values

__all__ = [
    'merge',
    'merge_with',
    'valmap',
    'keymap',
    'itemmap',
    'valfilter',
    'keyfilter',
    'itemfilter',
    'assoc',
    'dissoc',
    'assoc_in',
    'get_in',
    'update_in',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000002368FF66FD0>'

__pyx_capi__ = {
    'PyMapping_Next': None, # (!) real value is '<capsule object "int (PyObject *, Py_ssize_t *, PyObject **, PyObject **)" at 0x000002368FF684B0>'
    'assoc': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyObject *, PyObject *, int __pyx_skip_dispatch, struct __pyx_opt_args_7cytoolz_9dicttoolz_assoc *__pyx_optional_args)" at 0x000002368FF68660>'
    'assoc_in': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyObject *, PyObject *, int __pyx_skip_dispatch, struct __pyx_opt_args_7cytoolz_9dicttoolz_assoc_in *__pyx_optional_args)" at 0x000002368FF68690>'
    'c_dissoc': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyObject *, struct __pyx_opt_args_7cytoolz_9dicttoolz_c_dissoc *__pyx_optional_args)" at 0x000002368FF686C0>'
    'c_merge': None, # (!) real value is '<capsule object "PyObject *(PyObject *, struct __pyx_opt_args_7cytoolz_9dicttoolz_c_merge *__pyx_optional_args)" at 0x000002368FF684E0>'
    'c_merge_with': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyObject *, struct __pyx_opt_args_7cytoolz_9dicttoolz_c_merge_with *__pyx_optional_args)" at 0x000002368FF68510>'
    'get_in': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyObject *, int __pyx_skip_dispatch, struct __pyx_opt_args_7cytoolz_9dicttoolz_get_in *__pyx_optional_args)" at 0x000002368FF68720>'
    'get_map_iter': None, # (!) real value is '<capsule object "__pyx_t_7cytoolz_9dicttoolz_f_map_next (PyObject *, PyObject **)" at 0x000002368FF68480>'
    'itemfilter': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyObject *, int __pyx_skip_dispatch, struct __pyx_opt_args_7cytoolz_9dicttoolz_itemfilter *__pyx_optional_args)" at 0x000002368FF68630>'
    'itemmap': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyObject *, int __pyx_skip_dispatch, struct __pyx_opt_args_7cytoolz_9dicttoolz_itemmap *__pyx_optional_args)" at 0x000002368FF685A0>'
    'keyfilter': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyObject *, int __pyx_skip_dispatch, struct __pyx_opt_args_7cytoolz_9dicttoolz_keyfilter *__pyx_optional_args)" at 0x000002368FF68600>'
    'keymap': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyObject *, int __pyx_skip_dispatch, struct __pyx_opt_args_7cytoolz_9dicttoolz_keymap *__pyx_optional_args)" at 0x000002368FF68570>'
    'update_in': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyObject *, PyObject *, int __pyx_skip_dispatch, struct __pyx_opt_args_7cytoolz_9dicttoolz_update_in *__pyx_optional_args)" at 0x000002368FF686F0>'
    'valfilter': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyObject *, int __pyx_skip_dispatch, struct __pyx_opt_args_7cytoolz_9dicttoolz_valfilter *__pyx_optional_args)" at 0x000002368FF685D0>'
    'valmap': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyObject *, int __pyx_skip_dispatch, struct __pyx_opt_args_7cytoolz_9dicttoolz_valmap *__pyx_optional_args)" at 0x000002368FF68540>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='cytoolz.dicttoolz', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000002368FF66FD0>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\cytoolz\\\\dicttoolz.cp37-win_amd64.pyd')"

__test__ = {
    'assoc (line 368)': "\n    Return a new dict with new key value pair\n\n    New dict has d[key] set to value. Does not modify the initial dictionary.\n\n    >>> assoc({'x': 1}, 'x', 2)\n    {'x': 2}\n    >>> assoc({'x': 1}, 'y', 3)   # doctest: +SKIP\n    {'x': 1, 'y': 3}\n    ",
    'assoc_in (line 389)': "\n    Return a new dict with new, potentially nested, key value pair\n\n    >>> purchase = {'name': 'Alice',\n    ...             'order': {'items': ['Apple', 'Orange'],\n    ...                       'costs': [0.50, 1.25]},\n    ...             'credit card': '5555-1234-1234-1234'}\n    >>> assoc_in(purchase, ['order', 'costs'], [0.25, 1.00]) # doctest: +SKIP\n    {'credit card': '5555-1234-1234-1234',\n     'name': 'Alice',\n     'order': {'costs': [0.25, 1.00], 'items': ['Apple', 'Orange']}}\n    ",
    'dissoc (line 448)': "\n    Return a new dict with the given key(s) removed.\n\n    New dict has d[key] deleted for each supplied key.\n    Does not modify the initial dictionary.\n\n    >>> dissoc({'x': 1, 'y': 2}, 'y')\n    {'x': 1}\n    >>> dissoc({'x': 1, 'y': 2}, 'y', 'x')\n    {}\n    >>> dissoc({'x': 1}, 'y') # Ignores missing keys\n    {'x': 1}\n    ",
    'get_in (line 536)': "\n    Returns coll[i0][i1]...[iX] where [i0, i1, ..., iX]==keys.\n\n    If coll[i0][i1]...[iX] cannot be found, returns ``default``, unless\n    ``no_default`` is specified, then it raises KeyError or IndexError.\n\n    ``get_in`` is a generalization of ``operator.getitem`` for nested data\n    structures such as dictionaries and lists.\n\n    >>> transaction = {'name': 'Alice',\n    ...                'purchase': {'items': ['Apple', 'Orange'],\n    ...                             'costs': [0.50, 1.25]},\n    ...                'credit card': '5555-1234-1234-1234'}\n    >>> get_in(['purchase', 'items', 0], transaction)\n    'Apple'\n    >>> get_in(['name'], transaction)\n    'Alice'\n    >>> get_in(['purchase', 'total'], transaction)\n    >>> get_in(['purchase', 'items', 'apple'], transaction)\n    >>> get_in(['purchase', 'items', 10], transaction)\n    >>> get_in(['purchase', 'total'], transaction, 0)\n    0\n    >>> get_in(['y'], {}, no_default=True)\n    Traceback (most recent call last):\n        ...\n    KeyError: 'y'\n\n    See Also:\n        itertoolz.get\n        operator.getitem\n    ",
    'itemfilter (line 331)': '\n    Filter items in dictionary by item\n\n    >>> def isvalid(item):\n    ...     k, v = item\n    ...     return k % 2 == 0 and v < 4\n\n    >>> d = {1: 2, 2: 3, 3: 4, 4: 5}\n    >>> itemfilter(isvalid, d)\n    {2: 3}\n\n    See Also:\n        keyfilter\n        valfilter\n        itemmap\n    ',
    'itemmap (line 237)': '\n    Apply function to items of dictionary\n\n    >>> accountids = {"Alice": 10, "Bob": 20}\n    >>> itemmap(reversed, accountids)  # doctest: +SKIP\n    {10: "Alice", 20: "Bob"}\n\n    See Also:\n        keymap\n        valmap\n    ',
    'keyfilter (line 299)': '\n    Filter items in dictionary by key\n\n    >>> iseven = lambda x: x % 2 == 0\n    >>> d = {1: 2, 2: 3, 3: 4, 4: 5}\n    >>> keyfilter(iseven, d)\n    {2: 3, 4: 5}\n\n    See Also:\n        valfilter\n        itemfilter\n        keymap\n    ',
    'keymap (line 208)': '\n    Apply function to keys of dictionary\n\n    >>> bills = {"Alice": [20, 15, 30], "Bob": [10, 35]}\n    >>> keymap(str.lower, bills)  # doctest: +SKIP\n    {\'alice\': [20, 15, 30], \'bob\': [10, 35]}\n\n    See Also:\n        valmap\n        itemmap\n    ',
    'merge (line 100)': "\n    Merge a collection of dictionaries\n\n    >>> merge({1: 'one'}, {2: 'two'})\n    {1: 'one', 2: 'two'}\n\n    Later dictionaries have precedence\n\n    >>> merge({1: 2, 3: 4}, {3: 3, 4: 4})\n    {1: 2, 3: 3, 4: 4}\n\n    See Also:\n        merge_with\n    ",
    'merge_with (line 157)': '\n    Merge dictionaries and apply function to combined values\n\n    A key may occur in more than one dict, and all values mapped from the key\n    will be passed to the function as a list, such as func([val1, val2, ...]).\n\n    >>> merge_with(sum, {1: 1, 2: 2}, {1: 10, 2: 20})\n    {1: 11, 2: 22}\n\n    >>> merge_with(first, {1: 1, 2: 2}, {2: 20, 3: 30})  # doctest: +SKIP\n    {1: 1, 2: 2, 3: 30}\n\n    See Also:\n        merge\n    ',
    'update_in (line 465)': '\n    Update value in a (potentially) nested dictionary\n\n    inputs:\n    d - dictionary on which to operate\n    keys - list or tuple giving the location of the value to be changed in d\n    func - function to operate on that value\n\n    If keys == [k0,..,kX] and d[k0]..[kX] == v, update_in returns a copy of the\n    original dictionary with v replaced by func(v), but does not mutate the\n    original dictionary.\n\n    If k0 is not a key in d, update_in creates nested dictionaries to the depth\n    specified by the keys, with the innermost value set to func(default).\n\n    >>> inc = lambda x: x + 1\n    >>> update_in({\'a\': 0}, [\'a\'], inc)\n    {\'a\': 1}\n\n    >>> transaction = {\'name\': \'Alice\',\n    ...                \'purchase\': {\'items\': [\'Apple\', \'Orange\'],\n    ...                             \'costs\': [0.50, 1.25]},\n    ...                \'credit card\': \'5555-1234-1234-1234\'}\n    >>> update_in(transaction, [\'purchase\', \'costs\'], sum) # doctest: +SKIP\n    {\'credit card\': \'5555-1234-1234-1234\',\n     \'name\': \'Alice\',\n     \'purchase\': {\'costs\': 1.75, \'items\': [\'Apple\', \'Orange\']}}\n\n    >>> # updating a value when k0 is not in d\n    >>> update_in({}, [1, 2, 3], str, default="bar")\n    {1: {2: {3: \'bar\'}}}\n    >>> update_in({1: \'foo\'}, [2, 3, 4], inc, 0)\n    {1: \'foo\', 2: {3: {4: 1}}}\n    ',
    'valfilter (line 267)': '\n    Filter items in dictionary by value\n\n    >>> iseven = lambda x: x % 2 == 0\n    >>> d = {1: 2, 2: 3, 3: 4, 4: 5}\n    >>> valfilter(iseven, d)\n    {1: 2, 3: 4}\n\n    See Also:\n        keyfilter\n        itemfilter\n        valmap\n    ',
    'valmap (line 179)': '\n    Apply function to values of dictionary\n\n    >>> bills = {"Alice": [20, 15, 30], "Bob": [10, 35]}\n    >>> valmap(sum, bills)  # doctest: +SKIP\n    {\'Alice\': 65, \'Bob\': 45}\n\n    See Also:\n        keymap\n        itemmap\n    ',
}

