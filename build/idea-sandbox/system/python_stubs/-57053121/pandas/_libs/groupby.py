# encoding: utf-8
# module pandas._libs.groupby
# from C:\Users\Doly\Anaconda3\lib\site-packages\pandas\_libs\groupby.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py
from pandas._libs.algos import (groupsort_indexer, 
    take_2d_axis1_float64_float64)


# Variables with simple values

_int64_max = 9223372036854775807

# functions

def group_add_complex128(*args, **kwargs): # real signature unknown
    """ Only aggregates on axis=0 """
    pass

def group_add_complex64(*args, **kwargs): # real signature unknown
    """ Only aggregates on axis=0 """
    pass

def group_add_float32(*args, **kwargs): # real signature unknown
    """ Only aggregates on axis=0 """
    pass

def group_add_float64(*args, **kwargs): # real signature unknown
    """ Only aggregates on axis=0 """
    pass

def group_any_all(*args, **kwargs): # real signature unknown
    """
    Aggregated boolean values to show truthfulness of group elements.
    
        Parameters
        ----------
        out : array of values which this method will write its results to
        labels : array containing unique label for each group, with its
            ordering matching up to the corresponding record in `values`
        values : array containing the truth value of each element
        mask : array indicating whether a value is na or not
        val_test : str {'any', 'all'}
            String object dictating whether to use any or all truth testing
        skipna : boolean
            Flag to ignore nan values during truth testing
    
        Notes
        -----
        This method modifies the `out` parameter rather than returning an object.
        The returned values will either be 0 or 1 (False or True, respectively).
    """
    pass

def group_cummax(*args, **kwargs): # real signature unknown
    """
    Cumulative maximum of columns of `values`, in row groups `labels`.
    
        Parameters
        ----------
        out : array
            Array to store cummax in.
        values : array
            Values to take cummax of.
        labels : int64 array
            Labels to group by.
        ngroups : int
            Number of groups, larger than all entries of `labels`.
        is_datetimelike : bool
            True if `values` contains datetime-like entries.
    
        Notes
        -----
        This method modifies the `out` parameter, rather than returning an object.
    """
    pass

def group_cummin(*args, **kwargs): # real signature unknown
    """
    Cumulative minimum of columns of `values`, in row groups `labels`.
    
        Parameters
        ----------
        out : array
            Array to store cummin in.
        values : array
            Values to take cummin of.
        labels : int64 array
            Labels to group by.
        ngroups : int
            Number of groups, larger than all entries of `labels`.
        is_datetimelike : bool
            True if `values` contains datetime-like entries.
    
        Notes
        -----
        This method modifies the `out` parameter, rather than returning an object.
    """
    pass

def group_cumprod_float64(*args, **kwargs): # real signature unknown
    """
    Cumulative product of columns of `values`, in row groups `labels`.
    
        Parameters
        ----------
        out : float64 array
            Array to store cumprod in.
        values : float64 array
            Values to take cumprod of.
        labels : int64 array
            Labels to group by.
        ngroups : int
            Number of groups, larger than all entries of `labels`.
        is_datetimelike : bool
            Always false, `values` is never datetime-like.
        skipna : bool
            If true, ignore nans in `values`.
    
        Notes
        -----
        This method modifies the `out` parameter, rather than returning an object.
    """
    pass

def group_cumsum(*args, **kwargs): # real signature unknown
    """
    Cumulative sum of columns of `values`, in row groups `labels`.
    
        Parameters
        ----------
        out : array
            Array to store cumsum in.
        values : array
            Values to take cumsum of.
        labels : int64 array
            Labels to group by.
        ngroups : int
            Number of groups, larger than all entries of `labels`.
        is_datetimelike : bool
            True if `values` contains datetime-like entries.
        skipna : bool
            If true, ignore nans in `values`.
    
        Notes
        -----
        This method modifies the `out` parameter, rather than returning an object.
    """
    pass

def group_fillna_indexer(*args, **kwargs): # real signature unknown
    """
    Indexes how to fill values forwards or backwards within a group.
    
        Parameters
        ----------
        out : array of int64_t values which this method will write its results to
            Missing values will be written to with a value of -1
        labels : array containing unique label for each group, with its ordering
            matching up to the corresponding record in `values`
        mask : array of int64_t values where a 1 indicates a missing value
        direction : {'ffill', 'bfill'}
            Direction for fill to be applied (forwards or backwards, respectively)
        limit : Consecutive values to fill before stopping, or -1 for no limit
    
        Notes
        -----
        This method modifies the `out` parameter rather than returning an object
    """
    pass

def group_last(*args, **kwargs): # real signature unknown
    """ Only aggregates on axis=0 """
    pass

def group_max(*args, **kwargs): # real signature unknown
    """ Only aggregates on axis=0 """
    pass

def group_mean_float32(*args, **kwargs): # real signature unknown
    pass

def group_mean_float64(*args, **kwargs): # real signature unknown
    pass

def group_median_float64(*args, **kwargs): # real signature unknown
    """ Only aggregates on axis=0 """
    pass

def group_min(*args, **kwargs): # real signature unknown
    """ Only aggregates on axis=0 """
    pass

def group_nth(*args, **kwargs): # real signature unknown
    """ Only aggregates on axis=0 """
    pass

def group_ohlc_float32(*args, **kwargs): # real signature unknown
    """ Only aggregates on axis=0 """
    pass

def group_ohlc_float64(*args, **kwargs): # real signature unknown
    """ Only aggregates on axis=0 """
    pass

def group_prod_float32(*args, **kwargs): # real signature unknown
    """ Only aggregates on axis=0 """
    pass

def group_prod_float64(*args, **kwargs): # real signature unknown
    """ Only aggregates on axis=0 """
    pass

def group_quantile(*args, **kwargs): # real signature unknown
    """
    Calculate the quantile per group.
    
        Parameters
        ----------
        out : ndarray
            Array of aggregated values that will be written to.
        labels : ndarray
            Array containing the unique group labels.
        values : ndarray
            Array containing the values to apply the function against.
        q : float
            The quantile value to search for.
    
        Notes
        -----
        Rather than explicitly returning a value, this function modifies the
        provided `out` parameter.
    """
    pass

def group_rank(*args, **kwargs): # real signature unknown
    """
    Provides the rank of values within each group.
    
        Parameters
        ----------
        out : array of float64_t values which this method will write its results to
        values : array of rank_t values to be ranked
        labels : array containing unique label for each group, with its ordering
            matching up to the corresponding record in `values`
        ngroups : int
            This parameter is not used, is needed to match signatures of other
            groupby functions.
        is_datetimelike : bool, default False
            unused in this method but provided for call compatibility with other
            Cython transformations
        ties_method : {'average', 'min', 'max', 'first', 'dense'}, default
            'average'
            * average: average rank of group
            * min: lowest rank in group
            * max: highest rank in group
            * first: ranks assigned in order they appear in the array
            * dense: like 'min', but rank always increases by 1 between groups
        ascending : boolean, default True
            False for ranks by high (1) to low (N)
            na_option : {'keep', 'top', 'bottom'}, default 'keep'
        pct : boolean, default False
            Compute percentage rank of data within each group
        na_option : {'keep', 'top', 'bottom'}, default 'keep'
            * keep: leave NA values where they are
            * top: smallest rank if ascending
            * bottom: smallest rank if descending
    
        Notes
        -----
        This method modifies the `out` parameter rather than returning an object
    """
    pass

def group_shift_indexer(*args, **kwargs): # real signature unknown
    pass

def group_var_float32(*args, **kwargs): # real signature unknown
    pass

def group_var_float64(*args, **kwargs): # real signature unknown
    pass

def _group_add(*args, **kwargs): # real signature unknown
    """ Only aggregates on axis=0 """
    pass

def _group_mean(*args, **kwargs): # real signature unknown
    pass

def _group_ohlc(*args, **kwargs): # real signature unknown
    """ Only aggregates on axis=0 """
    pass

def _group_prod(*args, **kwargs): # real signature unknown
    """ Only aggregates on axis=0 """
    pass

def _group_var(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

tiebreakers = {
    'average': 0,
    'dense': 5,
    'first': 3,
    'max': 2,
    'min': 1,
}

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000024496960940>'

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.groupby', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000024496960940>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\pandas\\\\_libs\\\\groupby.cp37-win_amd64.pyd')"

__test__ = {}

