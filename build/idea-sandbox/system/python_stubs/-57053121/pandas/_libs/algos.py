# encoding: utf-8
# module pandas._libs.algos
# from C:\Users\Doly\Anaconda3\lib\site-packages\pandas\_libs\algos.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py
import pandas._libs.missing as missing # C:\Users\Doly\Anaconda3\lib\site-packages\pandas\_libs\missing.cp37-win_amd64.pyd

# functions

def backfill(*args, **kwargs): # real signature unknown
    pass

def backfill_2d_inplace(*args, **kwargs): # real signature unknown
    pass

def backfill_inplace(*args, **kwargs): # real signature unknown
    pass

def diff_2d(*args, **kwargs): # real signature unknown
    pass

def ensure_float32(*args, **kwargs): # real signature unknown
    pass

def ensure_float64(*args, **kwargs): # real signature unknown
    pass

def ensure_int16(*args, **kwargs): # real signature unknown
    pass

def ensure_int32(*args, **kwargs): # real signature unknown
    pass

def ensure_int64(*args, **kwargs): # real signature unknown
    pass

def ensure_int8(*args, **kwargs): # real signature unknown
    pass

def ensure_object(*args, **kwargs): # real signature unknown
    pass

def ensure_platform_int(*args, **kwargs): # real signature unknown
    pass

def ensure_uint16(*args, **kwargs): # real signature unknown
    pass

def ensure_uint32(*args, **kwargs): # real signature unknown
    pass

def ensure_uint64(*args, **kwargs): # real signature unknown
    pass

def ensure_uint8(*args, **kwargs): # real signature unknown
    pass

def groupsort_indexer(*args, **kwargs): # real signature unknown
    """
    Compute a 1-d indexer.
    
        The indexer is an ordering of the passed index,
        ordered by the groups.
    
        Parameters
        ----------
        index: int64 ndarray
            Mappings from group -> position.
        ngroups: int64
            Number of groups.
    
        Returns
        -------
        tuple
            1-d indexer ordered by groups, group counts.
    
        Notes
        -----
        This is a reverse of the label factorization process.
    """
    pass

def is_lexsorted(*args, **kwargs): # real signature unknown
    pass

def is_monotonic(*args, **kwargs): # real signature unknown
    """
    Returns
        -------
        tuple
            is_monotonic_inc : bool
            is_monotonic_dec : bool
            is_unique : bool
    """
    pass

def kth_smallest(*args, **kwargs): # real signature unknown
    pass

def nancorr(*args, **kwargs): # real signature unknown
    pass

def nancorr_spearman(*args, **kwargs): # real signature unknown
    pass

def pad(*args, **kwargs): # real signature unknown
    pass

def pad_2d_inplace(*args, **kwargs): # real signature unknown
    pass

def pad_inplace(*args, **kwargs): # real signature unknown
    pass

def rank_1d(*args, **kwargs): # real signature unknown
    """ Fast NaN-friendly version of ``scipy.stats.rankdata``. """
    pass

def rank_2d(*args, **kwargs): # real signature unknown
    """ Fast NaN-friendly version of ``scipy.stats.rankdata``. """
    pass

def take_1d_bool_bool(*args, **kwargs): # real signature unknown
    pass

def take_1d_bool_object(*args, **kwargs): # real signature unknown
    pass

def take_1d_float32_float32(*args, **kwargs): # real signature unknown
    pass

def take_1d_float32_float64(*args, **kwargs): # real signature unknown
    pass

def take_1d_float64_float64(*args, **kwargs): # real signature unknown
    pass

def take_1d_int16_float64(*args, **kwargs): # real signature unknown
    pass

def take_1d_int16_int16(*args, **kwargs): # real signature unknown
    pass

def take_1d_int16_int32(*args, **kwargs): # real signature unknown
    pass

def take_1d_int16_int64(*args, **kwargs): # real signature unknown
    pass

def take_1d_int32_float64(*args, **kwargs): # real signature unknown
    pass

def take_1d_int32_int32(*args, **kwargs): # real signature unknown
    pass

def take_1d_int32_int64(*args, **kwargs): # real signature unknown
    pass

def take_1d_int64_float64(*args, **kwargs): # real signature unknown
    pass

def take_1d_int64_int64(*args, **kwargs): # real signature unknown
    pass

def take_1d_int8_float64(*args, **kwargs): # real signature unknown
    pass

def take_1d_int8_int32(*args, **kwargs): # real signature unknown
    pass

def take_1d_int8_int64(*args, **kwargs): # real signature unknown
    pass

def take_1d_int8_int8(*args, **kwargs): # real signature unknown
    pass

def take_1d_object_object(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_bool_bool(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_bool_object(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_float32_float32(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_float32_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_float64_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int16_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int16_int16(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int16_int32(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int16_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int32_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int32_int32(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int32_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int64_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int64_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int8_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int8_int32(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int8_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int8_int8(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_object_object(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_bool_bool(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_bool_object(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_float32_float32(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_float32_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_float64_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int16_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int16_int16(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int16_int32(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int16_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int32_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int32_int32(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int32_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int64_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int64_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int8_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int8_int32(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int8_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int8_int8(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_object_object(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_bool_bool(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_bool_object(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_float32_float32(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_float32_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_float64_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int16_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int16_int16(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int16_int32(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int16_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int32_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int32_int32(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int32_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int64_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int64_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int8_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int8_int32(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int8_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int8_int8(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_object_object(*args, **kwargs): # real signature unknown
    pass

def unique_deltas(*args, **kwargs): # real signature unknown
    """
    Efficiently find the unique first-differences of the given array.
    
        Parameters
        ----------
        arr : ndarray[in64_t]
    
        Returns
        -------
        ndarray[int64_t]
            An ordered ndarray[int64_t]
    """
    pass

def _validate_limit(*args, **kwargs): # real signature unknown
    """
    Check that the `limit` argument is a positive integer.
    
        Parameters
        ----------
        nobs : int
        limit : object
    
        Returns
        -------
        int
            The limit.
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class Infinity(object):
    """ Provide a positive Infinity comparison method for ranking. """
    def __eq__(self, *args, **kwargs): # real signature unknown
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'pandas._libs.algos', '__doc__': '\\n    Provide a positive Infinity comparison method for ranking.\\n    ', '__lt__': <cyfunction Infinity.<lambda> at 0x000001FAEB70E048>, '__le__': <cyfunction Infinity.<lambda> at 0x000001FAEB70E100>, '__eq__': <cyfunction Infinity.<lambda> at 0x000001FAEB70E1B8>, '__ne__': <cyfunction Infinity.<lambda> at 0x000001FAEB70E270>, '__gt__': <cyfunction Infinity.<lambda> at 0x000001FAEB70E328>, '__ge__': <cyfunction Infinity.<lambda> at 0x000001FAEB70E3E0>, '__dict__': <attribute '__dict__' of 'Infinity' objects>, '__weakref__': <attribute '__weakref__' of 'Infinity' objects>, '__hash__': None})"
    __hash__ = None


class NegInfinity(object):
    """ Provide a negative Infinity comparison method for ranking. """
    def __eq__(self, *args, **kwargs): # real signature unknown
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'pandas._libs.algos', '__doc__': '\\n    Provide a negative Infinity comparison method for ranking.\\n    ', '__lt__': <cyfunction NegInfinity.<lambda> at 0x000001FAEB70E498>, '__le__': <cyfunction NegInfinity.<lambda> at 0x000001FAEB70E550>, '__eq__': <cyfunction NegInfinity.<lambda> at 0x000001FAEB70E608>, '__ne__': <cyfunction NegInfinity.<lambda> at 0x000001FAEB70E6C0>, '__gt__': <cyfunction NegInfinity.<lambda> at 0x000001FAEB70E778>, '__ge__': <cyfunction NegInfinity.<lambda> at 0x000001FAEB70E830>, '__dict__': <attribute '__dict__' of 'NegInfinity' objects>, '__weakref__': <attribute '__weakref__' of 'NegInfinity' objects>, '__hash__': None})"
    __hash__ = None


# variables with complex values

tiebreakers = {
    'average': 0,
    'dense': 5,
    'first': 3,
    'max': 2,
    'min': 1,
}

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001FAEB6C0F98>'

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.algos', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001FAEB6C0F98>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\pandas\\\\_libs\\\\algos.cp37-win_amd64.pyd')"

__test__ = {}

