# encoding: utf-8
# module pandas._libs.ops_dispatch
# from C:\Users\Doly\Anaconda3\lib\site-packages\pandas\_libs\ops_dispatch.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

# functions

def maybe_dispatch_ufunc_to_dunder_op(*args, **kwargs): # real signature unknown
    """
    Dispatch a ufunc to the equivalent dunder method.
    
        Parameters
        ----------
        self : ArrayLike
            The array whose dunder method we dispatch to
        ufunc : Callable
            A NumPy ufunc
        method : {'reduce', 'accumulate', 'reduceat', 'outer', 'at', '__call__'}
        inputs : ArrayLike
            The input arrays.
        kwargs : Any
            The additional keyword arguments, e.g. ``out``.
    
        Returns
        -------
        result : Any
            The result of applying the ufunc
    """
    pass

# no classes
# variables with complex values

DISPATCHED_UFUNCS = None # (!) real value is "{'ne', 'mul', 'lt', 'gt', 'eq', 'mod', 'or', 'sub', 'and', 'matmul', 'floordiv', 'add', 'divmod', 'xor', 'le', 'truediv', 'ge', 'remainder', 'pow'}"

REVERSED_NAMES = {
    'eq': '__eq__',
    'ge': '__le__',
    'gt': '__lt__',
    'le': '__ge__',
    'lt': '__gt__',
    'ne': '__ne__',
}

UFUNC_ALIASES = {
    'bitwise_and': 'and',
    'bitwise_or': 'or',
    'bitwise_xor': 'xor',
    'divide': 'div',
    'equal': 'eq',
    'floor_divide': 'floordiv',
    'greater': 'gt',
    'greater_equal': 'ge',
    'less': 'lt',
    'less_equal': 'le',
    'multiply': 'mul',
    'not_equal': 'ne',
    'power': 'pow',
    'remainder': 'mod',
    'subtract': 'sub',
    'true_divide': 'truediv',
}

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000028E6139D278>'

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.ops_dispatch', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000028E6139D278>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\pandas\\\\_libs\\\\ops_dispatch.cp37-win_amd64.pyd')"

__test__ = {}

