# encoding: utf-8
# module pandas._libs.parsers
# from C:\Users\Doly\Anaconda3\lib\site-packages\pandas\_libs\parsers.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import bz2 as bz2 # C:\Users\Doly\Anaconda3\lib\bz2.py
import gzip as gzip # C:\Users\Doly\Anaconda3\lib\gzip.py
import io as io # C:\Users\Doly\Anaconda3\lib\io.py
import os as os # C:\Users\Doly\Anaconda3\lib\os.py
import sys as sys # <module 'sys' (built-in)>
import time as time # <module 'time' (built-in)>
import warnings as warnings # C:\Users\Doly\Anaconda3\lib\warnings.py
import zipfile as zipfile # C:\Users\Doly\Anaconda3\lib\zipfile.py
import numpy as np # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py
import pandas._libs.lib as lib # C:\Users\Doly\Anaconda3\lib\site-packages\pandas\_libs\lib.cp37-win_amd64.pyd
import pandas.io.common as icom # C:\Users\Doly\Anaconda3\lib\site-packages\pandas\io\common.py
import lzma as lzma # C:\Users\Doly\Anaconda3\lib\lzma.py
import numpy as __numpy
import pandas.core.arrays.base as __pandas_core_arrays_base
import pandas.core.base as __pandas_core_base


# Variables with simple values

DEFAULT_CHUNKSIZE = 262144

ENOENT = 2

QUOTE_MINIMAL = 0
QUOTE_NONE = 3
QUOTE_NONNUMERIC = 2

# functions

def is_bool_dtype(arr_or_dtype): # reliably restored by inspect
    """
    Check whether the provided array or dtype is of a boolean dtype.
    
        Parameters
        ----------
        arr_or_dtype : array-like
            The array or dtype to check.
    
        Returns
        -------
        boolean
            Whether or not the array or dtype is of a boolean dtype.
    
        Notes
        -----
        An ExtensionArray is considered boolean when the ``_is_boolean``
        attribute is set to True.
    
        Examples
        --------
        >>> is_bool_dtype(str)
        False
        >>> is_bool_dtype(int)
        False
        >>> is_bool_dtype(bool)
        True
        >>> is_bool_dtype(np.bool)
        True
        >>> is_bool_dtype(np.array(['a', 'b']))
        False
        >>> is_bool_dtype(pd.Series([1, 2]))
        False
        >>> is_bool_dtype(np.array([True, False]))
        True
        >>> is_bool_dtype(pd.Categorical([True, False]))
        True
        >>> is_bool_dtype(pd.arrays.SparseArray([True, False]))
        True
    """
    pass

def is_categorical_dtype(arr_or_dtype): # reliably restored by inspect
    """
    Check whether an array-like or dtype is of the Categorical dtype.
    
        Parameters
        ----------
        arr_or_dtype : array-like
            The array-like or dtype to check.
    
        Returns
        -------
        boolean
            Whether or not the array-like or dtype is of the Categorical dtype.
    
        Examples
        --------
        >>> is_categorical_dtype(object)
        False
        >>> is_categorical_dtype(CategoricalDtype())
        True
        >>> is_categorical_dtype([1, 2, 3])
        False
        >>> is_categorical_dtype(pd.Categorical([1, 2, 3]))
        True
        >>> is_categorical_dtype(pd.CategoricalIndex([1, 2, 3]))
        True
    """
    pass

def is_datetime64_dtype(arr_or_dtype): # reliably restored by inspect
    """
    Check whether an array-like or dtype is of the datetime64 dtype.
    
        Parameters
        ----------
        arr_or_dtype : array-like
            The array-like or dtype to check.
    
        Returns
        -------
        boolean
            Whether or not the array-like or dtype is of the datetime64 dtype.
    
        Examples
        --------
        >>> is_datetime64_dtype(object)
        False
        >>> is_datetime64_dtype(np.datetime64)
        True
        >>> is_datetime64_dtype(np.array([], dtype=int))
        False
        >>> is_datetime64_dtype(np.array([], dtype=np.datetime64))
        True
        >>> is_datetime64_dtype([1, 2, 3])
        False
    """
    pass

def is_extension_array_dtype(arr_or_dtype): # reliably restored by inspect
    """
    Check if an object is a pandas extension array type.
    
        See the :ref:`Use Guide <extending.extension-types>` for more.
    
        Parameters
        ----------
        arr_or_dtype : object
            For array-like input, the ``.dtype`` attribute will
            be extracted.
    
        Returns
        -------
        bool
            Whether the `arr_or_dtype` is an extension array type.
    
        Notes
        -----
        This checks whether an object implements the pandas extension
        array interface. In pandas, this includes:
    
        * Categorical
        * Sparse
        * Interval
        * Period
        * DatetimeArray
        * TimedeltaArray
    
        Third-party libraries may implement arrays or types satisfying
        this interface as well.
    
        Examples
        --------
        >>> from pandas.api.types import is_extension_array_dtype
        >>> arr = pd.Categorical(['a', 'b'])
        >>> is_extension_array_dtype(arr)
        True
        >>> is_extension_array_dtype(arr.dtype)
        True
    
        >>> arr = np.array(['a', 'b'])
        >>> is_extension_array_dtype(arr.dtype)
        False
    """
    pass

def is_float_dtype(arr_or_dtype): # reliably restored by inspect
    """
    Check whether the provided array or dtype is of a float dtype.
    
        This function is internal and should not be exposed in the public API.
    
        Parameters
        ----------
        arr_or_dtype : array-like
            The array or dtype to check.
    
        Returns
        -------
        boolean
            Whether or not the array or dtype is of a float dtype.
    
        Examples
        --------
        >>> is_float_dtype(str)
        False
        >>> is_float_dtype(int)
        False
        >>> is_float_dtype(float)
        True
        >>> is_float_dtype(np.array(['a', 'b']))
        False
        >>> is_float_dtype(pd.Series([1, 2]))
        False
        >>> is_float_dtype(pd.Index([1, 2.]))
        True
    """
    pass

def is_integer_dtype(arr_or_dtype): # reliably restored by inspect
    """
    Check whether the provided array or dtype is of an integer dtype.
    
        Unlike in `in_any_int_dtype`, timedelta64 instances will return False.
    
        .. versionchanged:: 0.24.0
    
           The nullable Integer dtypes (e.g. pandas.Int64Dtype) are also considered
           as integer by this function.
    
        Parameters
        ----------
        arr_or_dtype : array-like
            The array or dtype to check.
    
        Returns
        -------
        boolean
            Whether or not the array or dtype is of an integer dtype and
            not an instance of timedelta64.
    
        Examples
        --------
        >>> is_integer_dtype(str)
        False
        >>> is_integer_dtype(int)
        True
        >>> is_integer_dtype(float)
        False
        >>> is_integer_dtype(np.uint64)
        True
        >>> is_integer_dtype('int8')
        True
        >>> is_integer_dtype('Int8')
        True
        >>> is_integer_dtype(pd.Int8Dtype)
        True
        >>> is_integer_dtype(np.datetime64)
        False
        >>> is_integer_dtype(np.timedelta64)
        False
        >>> is_integer_dtype(np.array(['a', 'b']))
        False
        >>> is_integer_dtype(pd.Series([1, 2]))
        True
        >>> is_integer_dtype(np.array([], dtype=np.timedelta64))
        False
        >>> is_integer_dtype(pd.Index([1, 2.]))  # float
        False
    """
    pass

def is_object_dtype(arr_or_dtype): # reliably restored by inspect
    """
    Check whether an array-like or dtype is of the object dtype.
    
        Parameters
        ----------
        arr_or_dtype : array-like
            The array-like or dtype to check.
    
        Returns
        -------
        boolean
            Whether or not the array-like or dtype is of the object dtype.
    
        Examples
        --------
        >>> is_object_dtype(object)
        True
        >>> is_object_dtype(int)
        False
        >>> is_object_dtype(np.array([], dtype=object))
        True
        >>> is_object_dtype(np.array([], dtype=int))
        False
        >>> is_object_dtype([1, 2, 3])
        False
    """
    pass

def pandas_dtype(dtype): # reliably restored by inspect
    """
    Convert input into a pandas only dtype object or a numpy dtype object.
    
        Parameters
        ----------
        dtype : object to be converted
    
        Returns
        -------
        np.dtype or a pandas dtype
    
        Raises
        ------
        TypeError if not a dtype
    """
    pass

def sanitize_objects(*args, **kwargs): # real signature unknown
    """
    Convert specified values, including the given set na_values and empty
        strings if convert_empty is True, to np.nan.
    
        Parameters
        ----------
        values : ndarray[object]
        na_values : set
        convert_empty : bool (default True)
    """
    pass

def union_categoricals(to_union, sort_categories=False, ignore_order=False): # reliably restored by inspect
    """
    Combine list-like of Categorical-like, unioning categories.
    
        All categories must have the same dtype.
    
        Parameters
        ----------
        to_union : list-like
            Categorical, CategoricalIndex, or Series with dtype='category'.
        sort_categories : bool, default False
            If true, resulting categories will be lexsorted, otherwise
            they will be ordered as they appear in the data.
        ignore_order : bool, default False
            If true, the ordered attribute of the Categoricals will be ignored.
            Results in an unordered categorical.
    
        Returns
        -------
        Categorical
    
        Raises
        ------
        TypeError
            - all inputs do not have the same dtype
            - all inputs do not have the same ordered property
            - all inputs are ordered and their categories are not identical
            - sort_categories=True and Categoricals are ordered
        ValueError
            Empty list of categoricals passed
    
        Notes
        -----
    
        To learn more about categories, see `link
        <https://pandas.pydata.org/pandas-docs/stable/user_guide/categorical.html#unioning>`__
    
        Examples
        --------
    
        >>> from pandas.api.types import union_categoricals
    
        If you want to combine categoricals that do not necessarily have
        the same categories, `union_categoricals` will combine a list-like
        of categoricals. The new categories will be the union of the
        categories being combined.
    
        >>> a = pd.Categorical(["b", "c"])
        >>> b = pd.Categorical(["a", "b"])
        >>> union_categoricals([a, b])
        [b, c, a, b]
        Categories (3, object): [b, c, a]
    
        By default, the resulting categories will be ordered as they appear
        in the `categories` of the data. If you want the categories to be
        lexsorted, use `sort_categories=True` argument.
    
        >>> union_categoricals([a, b], sort_categories=True)
        [b, c, a, b]
        Categories (3, object): [a, b, c]
    
        `union_categoricals` also works with the case of combining two
        categoricals of the same categories and order information (e.g. what
        you could also `append` for).
    
        >>> a = pd.Categorical(["a", "b"], ordered=True)
        >>> b = pd.Categorical(["a", "b", "a"], ordered=True)
        >>> union_categoricals([a, b])
        [a, b, a, b, a]
        Categories (2, object): [a < b]
    
        Raises `TypeError` because the categories are ordered and not identical.
    
        >>> a = pd.Categorical(["a", "b"], ordered=True)
        >>> b = pd.Categorical(["a", "b", "c"], ordered=True)
        >>> union_categoricals([a, b])
        TypeError: to union ordered Categoricals, all categories must be the same
    
        New in version 0.20.0
    
        Ordered categoricals with different categories or orderings can be
        combined by using the `ignore_ordered=True` argument.
    
        >>> a = pd.Categorical(["a", "b", "c"], ordered=True)
        >>> b = pd.Categorical(["c", "b", "a"], ordered=True)
        >>> union_categoricals([a, b], ignore_order=True)
        [a, b, c, c, b, a]
        Categories (3, object): [a, b, c]
    
        `union_categoricals` also works with a `CategoricalIndex`, or `Series`
        containing categorical data, but note that the resulting array will
        always be a plain `Categorical`
    
        >>> a = pd.Series(["b", "c"], dtype='category')
        >>> b = pd.Series(["a", "b"], dtype='category')
        >>> union_categoricals([a, b])
        [b, c, a, b]
        Categories (3, object): [b, c, a]
    """
    pass

def _compute_na_values(*args, **kwargs): # real signature unknown
    pass

def _concatenate_chunks(*args, **kwargs): # real signature unknown
    pass

def _ensure_encoded(*args, **kwargs): # real signature unknown
    pass

def _get_lzma_file(lzma): # reliably restored by inspect
    """
    Importing the `LZMAFile` class from the `lzma` module.
    
        Returns
        -------
        class
            The `LZMAFile` class from the `lzma` module.
    
        Raises
        ------
        RuntimeError
            If the `lzma` module was not imported correctly, or didn't exist.
    """
    pass

def _import_lzma(): # reliably restored by inspect
    """
    Importing the `lzma` module.
    
        Warns
        -----
        When the `lzma` module is not available.
    """
    pass

def _maybe_encode(*args, **kwargs): # real signature unknown
    pass

def _maybe_upcast(*args, **kwargs): # real signature unknown
    """  """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class Categorical(__pandas_core_arrays_base.ExtensionArray, __pandas_core_base.PandasObject):
    """
    Represent a categorical variable in classic R / S-plus fashion.
    
        `Categoricals` can only take on only a limited, and usually fixed, number
        of possible values (`categories`). In contrast to statistical categorical
        variables, a `Categorical` might have an order, but numerical operations
        (additions, divisions, ...) are not possible.
    
        All values of the `Categorical` are either in `categories` or `np.nan`.
        Assigning values outside of `categories` will raise a `ValueError`. Order
        is defined by the order of the `categories`, not lexical order of the
        values.
    
        Parameters
        ----------
        values : list-like
            The values of the categorical. If categories are given, values not in
            categories will be replaced with NaN.
        categories : Index-like (unique), optional
            The unique categories for this categorical. If not given, the
            categories are assumed to be the unique values of `values` (sorted, if
            possible, otherwise in the order in which they appear).
        ordered : bool, default False
            Whether or not this categorical is treated as a ordered categorical.
            If True, the resulting categorical will be ordered.
            An ordered categorical respects, when sorted, the order of its
            `categories` attribute (which in turn is the `categories` argument, if
            provided).
        dtype : CategoricalDtype
            An instance of ``CategoricalDtype`` to use for this categorical.
    
            .. versionadded:: 0.21.0
    
        Attributes
        ----------
        categories : Index
            The categories of this categorical
        codes : ndarray
            The codes (integer positions, which point to the categories) of this
            categorical, read only.
        ordered : bool
            Whether or not this Categorical is ordered.
        dtype : CategoricalDtype
            The instance of ``CategoricalDtype`` storing the ``categories``
            and ``ordered``.
    
            .. versionadded:: 0.21.0
    
        Methods
        -------
        from_codes
        __array__
    
        Raises
        ------
        ValueError
            If the categories do not validate.
        TypeError
            If an explicit ``ordered=True`` is given but no `categories` and the
            `values` are not sortable.
    
        See Also
        --------
        CategoricalDtype : Type for categorical data.
        CategoricalIndex : An Index with an underlying ``Categorical``.
    
        Notes
        -----
        See the `user guide
        <https://pandas.pydata.org/pandas-docs/stable/user_guide/categorical.html>`_
        for more.
    
        Examples
        --------
        >>> pd.Categorical([1, 2, 3, 1, 2, 3])
        [1, 2, 3, 1, 2, 3]
        Categories (3, int64): [1, 2, 3]
    
        >>> pd.Categorical(['a', 'b', 'c', 'a', 'b', 'c'])
        [a, b, c, a, b, c]
        Categories (3, object): [a, b, c]
    
        Ordered `Categoricals` can be sorted according to the custom order
        of the categories and can have a min and max value.
    
        >>> c = pd.Categorical(['a', 'b', 'c', 'a', 'b', 'c'], ordered=True,
        ...                    categories=['c', 'b', 'a'])
        >>> c
        [a, b, c, a, b, c]
        Categories (3, object): [c < b < a]
        >>> c.min()
        'c'
    """
    def add_categories(self, new_categories, inplace=False): # reliably restored by inspect
        """
        Add new categories.
        
                `new_categories` will be included at the last/highest place in the
                categories and will be unused directly after this call.
        
                Parameters
                ----------
                new_categories : category or list-like of category
                   The new categories to be included.
                inplace : bool, default False
                   Whether or not to add the categories inplace or return a copy of
                   this categorical with added categories.
        
                Returns
                -------
                cat : Categorical with new categories added or None if inplace.
        
                Raises
                ------
                ValueError
                    If the new categories include old categories or do not validate as
                    categories
        
                See Also
                --------
                rename_categories
                reorder_categories
                remove_categories
                remove_unused_categories
                set_categories
        """
        pass

    def argsort(self, ascending=True, kind=None, *args, **kwargs): # reliably restored by inspect
        """
        Return the indices that would sort the Categorical.
        
                .. versionchanged:: 0.25.0
        
                   Changed to sort missing values at the end.
        
                Parameters
                ----------
                ascending : bool, default True
                    Whether the indices should result in an ascending
                    or descending sort.
                kind : {'quicksort', 'mergesort', 'heapsort'}, optional
                    Sorting algorithm.
                *args, **kwargs:
                    passed through to :func:`numpy.argsort`.
        
                Returns
                -------
                numpy.array
        
                See Also
                --------
                numpy.ndarray.argsort
        
                Notes
                -----
                While an ordering is applied to the category values, arg-sorting
                in this context refers more to organizing and grouping together
                based on matching category values. Thus, this function can be
                called on an unordered Categorical instance unlike the functions
                'Categorical.min' and 'Categorical.max'.
        
                Examples
                --------
                >>> pd.Categorical(['b', 'b', 'a', 'c']).argsort()
                array([2, 0, 1, 3])
        
                >>> cat = pd.Categorical(['b', 'b', 'a', 'c'],
                ...                      categories=['c', 'b', 'a'],
                ...                      ordered=True)
                >>> cat.argsort()
                array([3, 0, 1, 2])
        
                Missing values are placed at the end
        
                >>> cat = pd.Categorical([2, None, 1])
                >>> cat.argsort()
                array([2, 0, 1])
        """
        pass

    def astype(self, dtype, copy=True): # reliably restored by inspect
        """
        Coerce this type to another dtype
        
                Parameters
                ----------
                dtype : numpy dtype or pandas type
                copy : bool, default True
                    By default, astype always returns a newly allocated object.
                    If copy is set to False and dtype is categorical, the original
                    object is returned.
        """
        pass

    def as_ordered(self, inplace=False): # reliably restored by inspect
        """
        Set the Categorical to be ordered.
        
                Parameters
                ----------
                inplace : bool, default False
                   Whether or not to set the ordered attribute in-place or return
                   a copy of this categorical with ordered set to True.
        
                Returns
                -------
                Categorical
                    Ordered Categorical.
        """
        pass

    def as_unordered(self, inplace=False): # reliably restored by inspect
        """
        Set the Categorical to be unordered.
        
                Parameters
                ----------
                inplace : bool, default False
                   Whether or not to set the ordered attribute in-place or return
                   a copy of this categorical with ordered set to False.
        
                Returns
                -------
                Categorical
                    Unordered Categorical.
        """
        pass

    def check_for_ordered(self, op): # reliably restored by inspect
        """ assert that we are ordered """
        pass

    def copy(self): # reliably restored by inspect
        """ Copy constructor. """
        pass

    def describe(self): # reliably restored by inspect
        """
        Describes this Categorical
        
                Returns
                -------
                description: `DataFrame`
                    A dataframe with frequency and counts by category.
        """
        pass

    def dropna(self): # reliably restored by inspect
        """
        Return the Categorical without null values.
        
                Missing values (-1 in .codes) are detected.
        
                Returns
                -------
                valid : Categorical
        """
        pass

    def equals(self, other): # reliably restored by inspect
        """
        Returns True if categorical arrays are equal.
        
                Parameters
                ----------
                other : `Categorical`
        
                Returns
                -------
                bool
        """
        pass

    def fillna(self, value=None, method=None, limit=None): # reliably restored by inspect
        """
        Fill NA/NaN values using the specified method.
        
                Parameters
                ----------
                value : scalar, dict, Series
                    If a scalar value is passed it is used to fill all missing values.
                    Alternatively, a Series or dict can be used to fill in different
                    values for each index. The value should not be a list. The
                    value(s) passed should either be in the categories or should be
                    NaN.
                method : {'backfill', 'bfill', 'pad', 'ffill', None}, default None
                    Method to use for filling holes in reindexed Series
                    pad / ffill: propagate last valid observation forward to next valid
                    backfill / bfill: use NEXT valid observation to fill gap
                limit : int, default None
                    (Not implemented yet for Categorical!)
                    If method is specified, this is the maximum number of consecutive
                    NaN values to forward/backward fill. In other words, if there is
                    a gap with more than this number of consecutive NaNs, it will only
                    be partially filled. If method is not specified, this is the
                    maximum number of entries along the entire axis where NaNs will be
                    filled.
        
                Returns
                -------
                filled : Categorical with NA/NaN filled
        """
        pass

    @classmethod
    def from_codes(cls, codes=None, dtype=None): # real signature unknown; restored from __doc__
        """
        Make a Categorical type from codes and categories or dtype.
        
                This constructor is useful if you already have codes and
                categories/dtype and so do not need the (computation intensive)
                factorization step, which is usually done on the constructor.
        
                If your data does not follow this convention, please use the normal
                constructor.
        
                Parameters
                ----------
                codes : array-like of int
                    An integer array, where each integer points to a category in
                    categories or dtype.categories, or else is -1 for NaN.
                categories : index-like, optional
                    The categories for the categorical. Items need to be unique.
                    If the categories are not given here, then they must be provided
                    in `dtype`.
                ordered : bool, optional
                    Whether or not this categorical is treated as an ordered
                    categorical. If not given here or in `dtype`, the resulting
                    categorical will be unordered.
                dtype : CategoricalDtype or "category", optional
                    If :class:`CategoricalDtype`, cannot be used together with
                    `categories` or `ordered`.
        
                    .. versionadded:: 0.24.0
        
                       When `dtype` is provided, neither `categories` nor `ordered`
                       should be provided.
        
                Returns
                -------
                Categorical
        
                Examples
                --------
                >>> dtype = pd.CategoricalDtype(['a', 'b'], ordered=True)
                >>> pd.Categorical.from_codes(codes=[0, 1, 0, 1], dtype=dtype)
                [a, b, a, b]
                Categories (2, object): [a < b]
        """
        pass

    def isin(self, values): # reliably restored by inspect
        """
        Check whether `values` are contained in Categorical.
        
                Return a boolean NumPy Array showing whether each element in
                the Categorical matches an element in the passed sequence of
                `values` exactly.
        
                Parameters
                ----------
                values : set or list-like
                    The sequence of values to test. Passing in a single string will
                    raise a ``TypeError``. Instead, turn a single string into a
                    list of one element.
        
                Returns
                -------
                isin : numpy.ndarray (bool dtype)
        
                Raises
                ------
                TypeError
                  * If `values` is not a set or list-like
        
                See Also
                --------
                pandas.Series.isin : Equivalent method on Series.
        
                Examples
                --------
        
                >>> s = pd.Categorical(['lama', 'cow', 'lama', 'beetle', 'lama',
                ...                'hippo'])
                >>> s.isin(['cow', 'lama'])
                array([ True,  True,  True, False,  True, False])
        
                Passing a single string as ``s.isin('lama')`` will raise an error. Use
                a list of one element instead:
        
                >>> s.isin(['lama'])
                array([ True, False,  True, False,  True, False])
        """
        pass

    def isna(self): # reliably restored by inspect
        """
        Detect missing values
        
                Missing values (-1 in .codes) are detected.
        
                Returns
                -------
                a boolean array of whether my values are null
        
                See Also
                --------
                isna : Top-level isna.
                isnull : Alias of isna.
                Categorical.notna : Boolean inverse of Categorical.isna.
        """
        pass

    def isnull(self): # reliably restored by inspect
        """
        Detect missing values
        
                Missing values (-1 in .codes) are detected.
        
                Returns
                -------
                a boolean array of whether my values are null
        
                See Also
                --------
                isna : Top-level isna.
                isnull : Alias of isna.
                Categorical.notna : Boolean inverse of Categorical.isna.
        """
        pass

    def is_dtype_equal(self, other): # reliably restored by inspect
        """
        Returns True if categoricals are the same dtype
                  same categories, and same ordered
        
                Parameters
                ----------
                other : Categorical
        
                Returns
                -------
                bool
        """
        pass

    def map(self, mapper): # reliably restored by inspect
        """
        Map categories using input correspondence (dict, Series, or function).
        
                Maps the categories to new categories. If the mapping correspondence is
                one-to-one the result is a :class:`~pandas.Categorical` which has the
                same order property as the original, otherwise a :class:`~pandas.Index`
                is returned. NaN values are unaffected.
        
                If a `dict` or :class:`~pandas.Series` is used any unmapped category is
                mapped to `NaN`. Note that if this happens an :class:`~pandas.Index`
                will be returned.
        
                Parameters
                ----------
                mapper : function, dict, or Series
                    Mapping correspondence.
        
                Returns
                -------
                pandas.Categorical or pandas.Index
                    Mapped categorical.
        
                See Also
                --------
                CategoricalIndex.map : Apply a mapping correspondence on a
                    :class:`~pandas.CategoricalIndex`.
                Index.map : Apply a mapping correspondence on an
                    :class:`~pandas.Index`.
                Series.map : Apply a mapping correspondence on a
                    :class:`~pandas.Series`.
                Series.apply : Apply more complex functions on a
                    :class:`~pandas.Series`.
        
                Examples
                --------
                >>> cat = pd.Categorical(['a', 'b', 'c'])
                >>> cat
                [a, b, c]
                Categories (3, object): [a, b, c]
                >>> cat.map(lambda x: x.upper())
                [A, B, C]
                Categories (3, object): [A, B, C]
                >>> cat.map({'a': 'first', 'b': 'second', 'c': 'third'})
                [first, second, third]
                Categories (3, object): [first, second, third]
        
                If the mapping is one-to-one the ordering of the categories is
                preserved:
        
                >>> cat = pd.Categorical(['a', 'b', 'c'], ordered=True)
                >>> cat
                [a, b, c]
                Categories (3, object): [a < b < c]
                >>> cat.map({'a': 3, 'b': 2, 'c': 1})
                [3, 2, 1]
                Categories (3, int64): [3 < 2 < 1]
        
                If the mapping is not one-to-one an :class:`~pandas.Index` is returned:
        
                >>> cat.map({'a': 'first', 'b': 'second', 'c': 'first'})
                Index(['first', 'second', 'first'], dtype='object')
        
                If a `dict` is used, all unmapped categories are mapped to `NaN` and
                the result is an :class:`~pandas.Index`:
        
                >>> cat.map({'a': 'first', 'b': 'second'})
                Index(['first', 'second', nan], dtype='object')
        """
        pass

    def max(*args, **kwargs): # reliably restored by inspect
        """
        The maximum value of the object.
        
                Only ordered `Categoricals` have a maximum!
        
                .. versionchanged:: 1.0.0
        
                   Returns an NA value on empty arrays
        
                Raises
                ------
                TypeError
                    If the `Categorical` is not `ordered`.
        
                Returns
                -------
                max : the maximum of this `Categorical`
        """
        pass

    def memory_usage(self, deep=False): # reliably restored by inspect
        """
        Memory usage of my values
        
                Parameters
                ----------
                deep : bool
                    Introspect the data deeply, interrogate
                    `object` dtypes for system-level memory consumption
        
                Returns
                -------
                bytes used
        
                Notes
                -----
                Memory usage does not include memory consumed by elements that
                are not components of the array if deep=False
        
                See Also
                --------
                numpy.ndarray.nbytes
        """
        pass

    def min(*args, **kwargs): # reliably restored by inspect
        """
        The minimum value of the object.
        
                Only ordered `Categoricals` have a minimum!
        
                .. versionchanged:: 1.0.0
        
                   Returns an NA value on empty arrays
        
                Raises
                ------
                TypeError
                    If the `Categorical` is not `ordered`.
        
                Returns
                -------
                min : the minimum of this `Categorical`
        """
        pass

    def mode(self, dropna=True): # reliably restored by inspect
        """
        Returns the mode(s) of the Categorical.
        
                Always returns `Categorical` even if only one value.
        
                Parameters
                ----------
                dropna : bool, default True
                    Don't consider counts of NaN/NaT.
        
                    .. versionadded:: 0.24.0
        
                Returns
                -------
                modes : `Categorical` (sorted)
        """
        pass

    def notna(self): # reliably restored by inspect
        """
        Inverse of isna
        
                Both missing values (-1 in .codes) and NA as a category are detected as
                null.
        
                Returns
                -------
                a boolean array of whether my values are not null
        
                See Also
                --------
                notna : Top-level notna.
                notnull : Alias of notna.
                Categorical.isna : Boolean inverse of Categorical.notna.
        """
        pass

    def notnull(self): # reliably restored by inspect
        """
        Inverse of isna
        
                Both missing values (-1 in .codes) and NA as a category are detected as
                null.
        
                Returns
                -------
                a boolean array of whether my values are not null
        
                See Also
                --------
                notna : Top-level notna.
                notnull : Alias of notna.
                Categorical.isna : Boolean inverse of Categorical.notna.
        """
        pass

    def put(self, *args, **kwargs): # reliably restored by inspect
        """ Replace specific elements in the Categorical with given values. """
        pass

    def remove_categories(self, removals, inplace=False): # reliably restored by inspect
        """
        Remove the specified categories.
        
                `removals` must be included in the old categories. Values which were in
                the removed categories will be set to NaN
        
                Parameters
                ----------
                removals : category or list of categories
                   The categories which should be removed.
                inplace : bool, default False
                   Whether or not to remove the categories inplace or return a copy of
                   this categorical with removed categories.
        
                Returns
                -------
                cat : Categorical with removed categories or None if inplace.
        
                Raises
                ------
                ValueError
                    If the removals are not contained in the categories
        
                See Also
                --------
                rename_categories
                reorder_categories
                add_categories
                remove_unused_categories
                set_categories
        """
        pass

    def remove_unused_categories(self, inplace=False): # reliably restored by inspect
        """
        Remove categories which are not used.
        
                Parameters
                ----------
                inplace : bool, default False
                   Whether or not to drop unused categories inplace or return a copy of
                   this categorical with unused categories dropped.
        
                Returns
                -------
                cat : Categorical with unused categories dropped or None if inplace.
        
                See Also
                --------
                rename_categories
                reorder_categories
                add_categories
                remove_categories
                set_categories
        """
        pass

    def rename_categories(self, new_categories, inplace=False): # reliably restored by inspect
        """
        Rename categories.
        
                Parameters
                ----------
                new_categories : list-like, dict-like or callable
        
                    New categories which will replace old categories.
        
                    * list-like: all items must be unique and the number of items in
                      the new categories must match the existing number of categories.
        
                    * dict-like: specifies a mapping from
                      old categories to new. Categories not contained in the mapping
                      are passed through and extra categories in the mapping are
                      ignored.
        
                    .. versionadded:: 0.21.0.
        
                    * callable : a callable that is called on all items in the old
                      categories and whose return values comprise the new categories.
        
                    .. versionadded:: 0.23.0.
        
                inplace : bool, default False
                    Whether or not to rename the categories inplace or return a copy of
                    this categorical with renamed categories.
        
                Returns
                -------
                cat : Categorical or None
                   With ``inplace=False``, the new categorical is returned.
                   With ``inplace=True``, there is no return value.
        
                Raises
                ------
                ValueError
                    If new categories are list-like and do not have the same number of
                    items than the current categories or do not validate as categories
        
                See Also
                --------
                reorder_categories
                add_categories
                remove_categories
                remove_unused_categories
                set_categories
        
                Examples
                --------
                >>> c = pd.Categorical(['a', 'a', 'b'])
                >>> c.rename_categories([0, 1])
                [0, 0, 1]
                Categories (2, int64): [0, 1]
        
                For dict-like ``new_categories``, extra keys are ignored and
                categories not in the dictionary are passed through
        
                >>> c.rename_categories({'a': 'A', 'c': 'C'})
                [A, A, b]
                Categories (2, object): [A, b]
        
                You may also provide a callable to create the new categories
        
                >>> c.rename_categories(lambda x: x.upper())
                [A, A, B]
                Categories (2, object): [A, B]
        """
        pass

    def reorder_categories(self, new_categories, ordered=None, inplace=False): # reliably restored by inspect
        """
        Reorder categories as specified in new_categories.
        
                `new_categories` need to include all old categories and no new category
                items.
        
                Parameters
                ----------
                new_categories : Index-like
                   The categories in new order.
                ordered : bool, optional
                   Whether or not the categorical is treated as a ordered categorical.
                   If not given, do not change the ordered information.
                inplace : bool, default False
                   Whether or not to reorder the categories inplace or return a copy of
                   this categorical with reordered categories.
        
                Returns
                -------
                cat : Categorical with reordered categories or None if inplace.
        
                Raises
                ------
                ValueError
                    If the new categories do not contain all old category items or any
                    new ones
        
                See Also
                --------
                rename_categories
                add_categories
                remove_categories
                remove_unused_categories
                set_categories
        """
        pass

    def repeat(self, repeats, axis=None): # reliably restored by inspect
        """
        Repeat elements of a Categorical.
        
        Returns a new Categorical where each element of the current Categorical
        is repeated consecutively a given number of times.
        
        Parameters
        ----------
        repeats : int or array of ints
            The number of repetitions for each element. This should be a
            non-negative integer. Repeating 0 times will return an empty
            Categorical.
        axis : None
            Must be ``None``. Has no effect but is accepted for compatibility
            with numpy.
        
        Returns
        -------
        repeated_array : Categorical
            Newly created Categorical with repeated elements.
        
        See Also
        --------
        Series.repeat : Equivalent function for Series.
        Index.repeat : Equivalent function for Index.
        numpy.repeat : Similar method for :class:`numpy.ndarray`.
        ExtensionArray.take : Take arbitrary positions.
        
        Examples
        --------
        >>> cat = pd.Categorical(['a', 'b', 'c'])
        >>> cat
        [a, b, c]
        Categories (3, object): [a, b, c]
        >>> cat.repeat(2)
        [a, a, b, b, c, c]
        Categories (3, object): [a, b, c]
        >>> cat.repeat([1, 2, 3])
        [a, b, b, c, c, c]
        Categories (3, object): [a, b, c]
        """
        pass

    def replace(self, to_replace, value, inplace=False): # reliably restored by inspect
        """
        Replaces all instances of one value with another
        
                Parameters
                ----------
                to_replace: object
                    The value to be replaced
        
                value: object
                    The value to replace it with
        
                inplace: bool
                    Whether the operation is done in-place
        
                Returns
                -------
                None if inplace is True, otherwise the new Categorical after replacement
        
        
                Examples
                --------
                >>> s = pd.Categorical([1, 2, 1, 3])
                >>> s.replace(1, 3)
                [3, 3, 2, 3]
                Categories (2, int64): [2, 3]
        """
        pass

    def searchsorted(self, value, side=None, sorter=None): # reliably restored by inspect
        """
        Find indices where elements should be inserted to maintain order.
        
        Find the indices into a sorted Categorical `self` such that, if the
        corresponding elements in `value` were inserted before the indices,
        the order of `self` would be preserved.
        
        .. note::
        
            The Categorical *must* be monotonically sorted, otherwise
            wrong locations will likely be returned. Pandas does *not*
            check this for you.
        
        Parameters
        ----------
        value : array_like
            Values to insert into `self`.
        side : {'left', 'right'}, optional
            If 'left', the index of the first suitable location found is given.
            If 'right', return the last such index.  If there is no suitable
            index, return either 0 or N (where N is the length of `self`).
        sorter : 1-D array_like, optional
            Optional array of integer indices that sort `self` into ascending
            order. They are typically the result of ``np.argsort``.
        
        Returns
        -------
        int or array of int
            A scalar or array of insertion points with the
            same shape as `value`.
        
            .. versionchanged:: 0.24.0
                If `value` is a scalar, an int is now always returned.
                Previously, scalar inputs returned an 1-item array for
                :class:`Series` and :class:`Categorical`.
        
        See Also
        --------
        sort_values
        numpy.searchsorted
        
        Notes
        -----
        Binary search is used to find the required insertion points.
        
        Examples
        --------
        
        >>> x = pd.Series([1, 2, 3])
        >>> x
        0    1
        1    2
        2    3
        dtype: int64
        
        >>> x.searchsorted(4)
        3
        
        >>> x.searchsorted([0, 4])
        array([0, 3])
        
        >>> x.searchsorted([1, 3], side='left')
        array([0, 2])
        
        >>> x.searchsorted([1, 3], side='right')
        array([1, 3])
        
        >>> x = pd.Categorical(['apple', 'bread', 'bread',
                                'cheese', 'milk'], ordered=True)
        [apple, bread, bread, cheese, milk]
        Categories (4, object): [apple < bread < cheese < milk]
        
        >>> x.searchsorted('bread')
        1
        
        >>> x.searchsorted(['bread'], side='right')
        array([3])
        
        If the values are not monotonically sorted, wrong locations
        may be returned:
        
        >>> x = pd.Series([2, 1, 3])
        >>> x.searchsorted(1)
        0  # wrong result, correct would be 1
        """
        pass

    def set_categories(self, new_categories, ordered=None, rename=False, inplace=False): # reliably restored by inspect
        """
        Set the categories to the specified new_categories.
        
                `new_categories` can include new categories (which will result in
                unused categories) or remove old categories (which results in values
                set to NaN). If `rename==True`, the categories will simple be renamed
                (less or more items than in old categories will result in values set to
                NaN or in unused categories respectively).
        
                This method can be used to perform more than one action of adding,
                removing, and reordering simultaneously and is therefore faster than
                performing the individual steps via the more specialised methods.
        
                On the other hand this methods does not do checks (e.g., whether the
                old categories are included in the new categories on a reorder), which
                can result in surprising changes, for example when using special string
                dtypes, which does not considers a S1 string equal to a single char
                python string.
        
                Parameters
                ----------
                new_categories : Index-like
                   The categories in new order.
                ordered : bool, default False
                   Whether or not the categorical is treated as a ordered categorical.
                   If not given, do not change the ordered information.
                rename : bool, default False
                   Whether or not the new_categories should be considered as a rename
                   of the old categories or as reordered categories.
                inplace : bool, default False
                   Whether or not to reorder the categories in-place or return a copy
                   of this categorical with reordered categories.
        
                Returns
                -------
                Categorical with reordered categories or None if inplace.
        
                Raises
                ------
                ValueError
                    If new_categories does not validate as categories
        
                See Also
                --------
                rename_categories
                reorder_categories
                add_categories
                remove_categories
                remove_unused_categories
        """
        pass

    def set_ordered(self, value, inplace=False): # reliably restored by inspect
        """
        Set the ordered attribute to the boolean value.
        
                Parameters
                ----------
                value : bool
                   Set whether this categorical is ordered (True) or not (False).
                inplace : bool, default False
                   Whether or not to set the ordered attribute in-place or return
                   a copy of this categorical with ordered set to the value.
        """
        pass

    def shift(self, periods, fill_value=None): # reliably restored by inspect
        """
        Shift Categorical by desired number of periods.
        
                Parameters
                ----------
                periods : int
                    Number of periods to move, can be positive or negative
                fill_value : object, optional
                    The scalar value to use for newly introduced missing values.
        
                    .. versionadded:: 0.24.0
        
                Returns
                -------
                shifted : Categorical
        """
        pass

    def sort_values(self, inplace=False, ascending=True, na_position=None): # reliably restored by inspect
        """
        Sort the Categorical by category value returning a new
                Categorical by default.
        
                While an ordering is applied to the category values, sorting in this
                context refers more to organizing and grouping together based on
                matching category values. Thus, this function can be called on an
                unordered Categorical instance unlike the functions 'Categorical.min'
                and 'Categorical.max'.
        
                Parameters
                ----------
                inplace : bool, default False
                    Do operation in place.
                ascending : bool, default True
                    Order ascending. Passing False orders descending. The
                    ordering parameter provides the method by which the
                    category values are organized.
                na_position : {'first', 'last'} (optional, default='last')
                    'first' puts NaNs at the beginning
                    'last' puts NaNs at the end
        
                Returns
                -------
                Categorical or None
        
                See Also
                --------
                Categorical.sort
                Series.sort_values
        
                Examples
                --------
                >>> c = pd.Categorical([1, 2, 2, 1, 5])
                >>> c
                [1, 2, 2, 1, 5]
                Categories (3, int64): [1, 2, 5]
                >>> c.sort_values()
                [1, 1, 2, 2, 5]
                Categories (3, int64): [1, 2, 5]
                >>> c.sort_values(ascending=False)
                [5, 2, 2, 1, 1]
                Categories (3, int64): [1, 2, 5]
        
                Inplace sorting can be done as well:
        
                >>> c.sort_values(inplace=True)
                >>> c
                [1, 1, 2, 2, 5]
                Categories (3, int64): [1, 2, 5]
                >>>
                >>> c = pd.Categorical([1, 2, 2, 1, 5])
        
                'sort_values' behaviour with NaNs. Note that 'na_position'
                is independent of the 'ascending' parameter:
        
                >>> c = pd.Categorical([np.nan, 2, 2, np.nan, 5])
                >>> c
                [NaN, 2.0, 2.0, NaN, 5.0]
                Categories (2, int64): [2, 5]
                >>> c.sort_values()
                [2.0, 2.0, 5.0, NaN, NaN]
                Categories (2, int64): [2, 5]
                >>> c.sort_values(ascending=False)
                [5.0, 2.0, 2.0, NaN, NaN]
                Categories (2, int64): [2, 5]
                >>> c.sort_values(na_position='first')
                [NaN, NaN, 2.0, 2.0, 5.0]
                Categories (2, int64): [2, 5]
                >>> c.sort_values(ascending=False, na_position='first')
                [NaN, NaN, 5.0, 2.0, 2.0]
                Categories (2, int64): [2, 5]
        """
        pass

    def take(self, indexer, allow_fill=False, fill_value=None): # reliably restored by inspect
        """
        Take elements from the Categorical.
        
                Parameters
                ----------
                indexer : sequence of int
                    The indices in `self` to take. The meaning of negative values in
                    `indexer` depends on the value of `allow_fill`.
                allow_fill : bool, default False
                    How to handle negative values in `indexer`.
        
                    * False: negative values in `indices` indicate positional indices
                      from the right. This is similar to
                      :func:`numpy.take`.
        
                    * True: negative values in `indices` indicate missing values
                      (the default). These values are set to `fill_value`. Any other
                      other negative values raise a ``ValueError``.
        
                    .. versionchanged:: 1.0.0
        
                       Default value changed from ``True`` to ``False``.
        
                fill_value : object
                    The value to use for `indices` that are missing (-1), when
                    ``allow_fill=True``. This should be the category, i.e. a value
                    in ``self.categories``, not a code.
        
                Returns
                -------
                Categorical
                    This Categorical will have the same categories and ordered as
                    `self`.
        
                See Also
                --------
                Series.take : Similar method for Series.
                numpy.ndarray.take : Similar method for NumPy arrays.
        
                Examples
                --------
                >>> cat = pd.Categorical(['a', 'a', 'b'])
                >>> cat
                [a, a, b]
                Categories (2, object): [a, b]
        
                Specify ``allow_fill==False`` to have negative indices mean indexing
                from the right.
        
                >>> cat.take([0, -1, -2], allow_fill=False)
                [a, b, a]
                Categories (2, object): [a, b]
        
                With ``allow_fill=True``, indices equal to ``-1`` mean "missing"
                values that should be filled with the `fill_value`, which is
                ``np.nan`` by default.
        
                >>> cat.take([0, -1, -1], allow_fill=True)
                [a, NaN, NaN]
                Categories (2, object): [a, b]
        
                The fill value can be specified.
        
                >>> cat.take([0, -1, -1], allow_fill=True, fill_value='a')
                [a, a, a]
                Categories (3, object): [a, b]
        
                Specifying a fill value that's not in ``self.categories``
                will raise a ``TypeError``.
        """
        pass

    def take_nd(self, indexer, allow_fill=False, fill_value=None): # reliably restored by inspect
        # no doc
        pass

    def tolist(self): # reliably restored by inspect
        """
        Return a list of the values.
        
                These are each a scalar type, which is a Python scalar
                (for str, int, float) or a pandas scalar
                (for Timestamp/Timedelta/Interval/Period)
        """
        pass

    def to_dense(self): # reliably restored by inspect
        """
        Return my 'dense' representation
        
                For internal compatibility with numpy arrays.
        
                Returns
                -------
                dense : array
        """
        pass

    def to_list(self): # reliably restored by inspect
        """
        Return a list of the values.
        
                These are each a scalar type, which is a Python scalar
                (for str, int, float) or a pandas scalar
                (for Timestamp/Timedelta/Interval/Period)
        """
        pass

    def unique(self): # reliably restored by inspect
        """
        Return the ``Categorical`` which ``categories`` and ``codes`` are
                unique. Unused categories are NOT returned.
        
                - unordered category: values and categories are sorted by appearance
                  order.
                - ordered category: values are sorted by appearance order, categories
                  keeps existing order.
        
                Returns
                -------
                unique values : ``Categorical``
        
                Examples
                --------
                An unordered Categorical will return categories in the
                order of appearance.
        
                >>> pd.Categorical(list('baabc'))
                [b, a, c]
                Categories (3, object): [b, a, c]
        
                >>> pd.Categorical(list('baabc'), categories=list('abc'))
                [b, a, c]
                Categories (3, object): [b, a, c]
        
                An ordered Categorical preserves the category ordering.
        
                >>> pd.Categorical(list('baabc'),
                ...                categories=list('abc'),
                ...                ordered=True)
                [b, a, c]
                Categories (3, object): [a < b < c]
        
                See Also
                --------
                unique
                CategoricalIndex.unique
                Series.unique
        """
        pass

    def value_counts(self, dropna=True): # reliably restored by inspect
        """
        Return a Series containing counts of each category.
        
                Every category will have an entry, even those with a count of 0.
        
                Parameters
                ----------
                dropna : bool, default True
                    Don't include counts of NaN.
        
                Returns
                -------
                counts : Series
        
                See Also
                --------
                Series.value_counts
        """
        pass

    def view(self, dtype=None): # reliably restored by inspect
        # no doc
        pass

    @classmethod
    def _concat_same_type(cls, *args, **kwargs): # real signature unknown
        pass

    def _formatter(self, boxed=False): # reliably restored by inspect
        # no doc
        pass

    @classmethod
    def _from_factorized(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def _from_inferred_categories(cls, *args, **kwargs): # real signature unknown
        """
        Construct a Categorical from inferred values.
        
                For inferred categories (`dtype` is None) the categories are sorted.
                For explicit `dtype`, the `inferred_categories` are cast to the
                appropriate type.
        
                Parameters
                ----------
                inferred_categories : Index
                inferred_codes : Index
                dtype : CategoricalDtype or 'category'
                true_values : list, optional
                    If none are provided, the default ones are
                    "True", "TRUE", and "true."
        
                Returns
                -------
                Categorical
        """
        pass

    @classmethod
    def _from_sequence(cls, *args, **kwargs): # real signature unknown
        pass

    def _get_codes(self): # reliably restored by inspect
        """
        Get the codes.
        
                Returns
                -------
                codes : integer array view
                    A non writable view of the `codes` array.
        """
        pass

    def _get_repr(self, length=True, na_rep=None, footer=True): # reliably restored by inspect
        # no doc
        pass

    def _internal_get_values(self): # reliably restored by inspect
        """
        Return the values.
        
                For internal compatibility with pandas formatting.
        
                Returns
                -------
                np.ndarray or Index
                    A numpy array of the same dtype as categorical.categories.dtype or
                    Index if datetime / periods.
        """
        pass

    def _maybe_coerce_indexer(self, indexer): # reliably restored by inspect
        """ return an indexer coerced to the codes dtype """
        pass

    def _reduce(self, name, axis=0, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def _repr_categories(self): # reliably restored by inspect
        """ return the base repr for the categories """
        pass

    def _repr_categories_info(self): # reliably restored by inspect
        """ Returns a string representation of the footer. """
        pass

    def _repr_footer(self): # reliably restored by inspect
        # no doc
        pass

    def _reverse_indexer(self): # reliably restored by inspect
        """
        Compute the inverse of a categorical, returning
                a dict of categories -> indexers.
        
                *This is an internal function*
        
                Returns
                -------
                dict of categories -> indexers
        
                Examples
                --------
                >>> c = pd.Categorical(list('aabca'))
                >>> c
                [a, a, b, c, a]
                Categories (3, object): [a, b, c]
                >>> c.categories
                Index(['a', 'b', 'c'], dtype='object')
                >>> c.codes
                array([0, 0, 1, 2, 0], dtype=int8)
                >>> c._reverse_indexer()
                {'a': array([0, 1, 4]), 'b': array([2]), 'c': array([3])}
        """
        pass

    def _set_categories(self, categories, fastpath=False): # reliably restored by inspect
        """
        Sets new categories inplace
        
                Parameters
                ----------
                fastpath : bool, default False
                   Don't perform validation of the categories for uniqueness or nulls
        
                Examples
                --------
                >>> c = pd.Categorical(['a', 'b'])
                >>> c
                [a, b]
                Categories (2, object): [a, b]
        
                >>> c._set_categories(pd.Index(['a', 'c']))
                >>> c
                [a, c]
                Categories (2, object): [a, c]
        """
        pass

    def _set_codes(self, codes): # reliably restored by inspect
        """ Not settable by the user directly """
        pass

    def _set_dtype(self, dtype): # reliably restored by inspect
        """
        Internal method for directly updating the CategoricalDtype
        
                Parameters
                ----------
                dtype : CategoricalDtype
        
                Notes
                -----
                We don't do any validation here. It's assumed that the dtype is
                a (valid) instance of `CategoricalDtype`.
        """
        pass

    def _tidy_repr(self, max_vals=10, footer=True): # reliably restored by inspect
        """
        a short repr displaying only max_vals and an optional (but default
                footer)
        """
        pass

    def _values_for_argsort(self): # reliably restored by inspect
        # no doc
        pass

    def _values_for_factorize(self): # reliably restored by inspect
        # no doc
        pass

    def _values_for_rank(self): # reliably restored by inspect
        """
        For correctly ranking ordered categorical data. See GH#15420
        
                Ordered categorical data should be ranked on the basis of
                codes with -1 translated to NaN.
        
                Returns
                -------
                numpy.array
        """
        pass

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def __array__(self, dtype=None): # reliably restored by inspect
        """
        The numpy array interface.
        
                Returns
                -------
                numpy.array
                    A numpy array of either the specified dtype or,
                    if dtype==None (default), the same dtype as
                    categorical.categories.dtype.
        """
        pass

    def __contains__(self, key): # reliably restored by inspect
        """ Returns True if `key` is in this Categorical. """
        pass

    def __eq__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __getitem__(self, key): # reliably restored by inspect
        """ Return an item. """
        pass

    def __ge__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __gt__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, values, categories=None, ordered=None, dtype=None, fastpath=False): # reliably restored by inspect
        # no doc
        pass

    def __iter__(self): # reliably restored by inspect
        """ Returns an Iterator over the values of this Categorical. """
        pass

    def __len__(self): # reliably restored by inspect
        """ The length of this Categorical. """
        pass

    def __le__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __lt__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __ne__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __repr__(self): # reliably restored by inspect
        """ String representation. """
        pass

    def __setitem__(self, key, value): # reliably restored by inspect
        """
        Item assignment.
        
                Raises
                ------
                ValueError
                    If (one or more) Value is not in categories or if a assigned
                    `Categorical` does not have the same categories
        """
        pass

    def __setstate__(self, state): # reliably restored by inspect
        """ Necessary for making this object picklable """
        pass

    categories = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The categories of this categorical.

        Setting assigns new values to each category (effectively a rename of
        each individual category).

        The assigned value has to be a list-like object. All items must be
        unique and the number of items in the new categories must be the same
        as the number of items in the old categories.

        Assigning to `categories` is a inplace operation!

        Raises
        ------
        ValueError
            If the new categories do not validate as categories or if the
            number of new categories is unequal the number of old categories

        See Also
        --------
        rename_categories
        reorder_categories
        add_categories
        remove_categories
        remove_unused_categories
        set_categories
        """

    codes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
The category codes of this categorical.

Level codes are an array if integer which are the positions of the real
values in the categories array.

There is not setter, use the other categorical methods and the normal item
setter to change values in the categorical.
"""

    dtype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The :class:`~pandas.api.types.CategoricalDtype` for this instance.
        """

    nbytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ordered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Whether the categories have an ordered relationship.
        """

    shape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Shape of the Categorical.

        For internal compatibility with numpy arrays.

        Returns
        -------
        shape : tuple
        """

    T = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return transposed numpy array.
        """

    _can_hold_na = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _constructor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _ndarray_values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    itemsize = None # (!) real value is '<pandas._libs.properties.CachedProperty object at 0x000001DF4ABC8FC8>'
    size = None # (!) real value is '<pandas._libs.properties.CachedProperty object at 0x000001DF4ABC8F88>'
    _deprecations = frozenset({'tolist'})
    _dtype = CategoricalDtype(categories=None, ordered=False)
    _typ = 'categorical'
    __array_priority__ = 1000
    __hash__ = None


class DtypeWarning(Warning):
    """
    Warning raised when reading different dtypes in a column from a file.
    
        Raised for a dtype incompatibility. This can happen whenever `read_csv`
        or `read_table` encounter non-uniform dtypes in a column(s) of a given
        CSV file.
    
        See Also
        --------
        read_csv : Read CSV (comma-separated) file into a DataFrame.
        read_table : Read general delimited file into a DataFrame.
    
        Notes
        -----
        This warning is issued when dealing with larger files because the dtype
        checking happens per chunk read.
    
        Despite the warning, the CSV file is read with mixed types in a single
        column which will be an object type. See the examples below to better
        understand this issue.
    
        Examples
        --------
        This example creates and reads a large CSV file with a column that contains
        `int` and `str`.
    
        >>> df = pd.DataFrame({'a': (['1'] * 100000 + ['X'] * 100000 +
        ...                          ['1'] * 100000),
        ...                    'b': ['b'] * 300000})
        >>> df.to_csv('test.csv', index=False)
        >>> df2 = pd.read_csv('test.csv')
        ... # DtypeWarning: Columns (0) have mixed types
    
        Important to notice that ``df2`` will contain both `str` and `int` for the
        same input, '1'.
    
        >>> df2.iloc[262140, 0]
        '1'
        >>> type(df2.iloc[262140, 0])
        <class 'str'>
        >>> df2.iloc[262150, 0]
        1
        >>> type(df2.iloc[262150, 0])
        <class 'int'>
    
        One way to solve this issue is using the `dtype` parameter in the
        `read_csv` and `read_table` functions to explicit the conversion:
    
        >>> df2 = pd.read_csv('test.csv', sep=',', dtype={'a': str})
    
        No warning was issued.
    
        >>> import os
        >>> os.remove('test.csv')
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class EmptyDataError(ValueError):
    """
    Exception that is thrown in `pd.read_csv` (by both the C and
        Python engines) when empty data or header is encountered.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class k(__numpy.generic):
    """
    Any Python object.
        Character code: ``'O'``.
    """
    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
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

    def __iadd__(self, *args, **kwargs): # real signature unknown
        """ Implement self+=value. """
        pass

    def __imul__(self, *args, **kwargs): # real signature unknown
        """ Implement self*=value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass


class ParserError(ValueError):
    """
    Exception that is raised by an error encountered in parsing file contents.
    
        This is a generic error raised for errors encountered when functions like
        `read_csv` or `read_html` are parsing contents of a file.
    
        See Also
        --------
        read_csv : Read CSV (comma-separated) file into a DataFrame.
        read_html : Read HTML table into a DataFrame.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class ParserWarning(Warning):
    """
    Warning raised when reading a file that doesn't use the default 'c' parser.
    
        Raised by `pd.read_csv` and `pd.read_table` when it is necessary to change
        parsers, generally from the default 'c' parser to 'python'.
    
        It happens due to a lack of support or functionality for parsing a
        particular attribute of a CSV file with the requested engine.
    
        Currently, 'c' unsupported options include the following parameters:
    
        1. `sep` other than a single character (e.g. regex separators)
        2. `skipfooter` higher than 0
        3. `sep=None` with `delim_whitespace=False`
    
        The warning can be avoided by adding `engine='python'` as a parameter in
        `pd.read_csv` and `pd.read_table` methods.
    
        See Also
        --------
        pd.read_csv : Read CSV (comma-separated) file into DataFrame.
        pd.read_table : Read general delimited file into DataFrame.
    
        Examples
        --------
        Using a `sep` in `pd.read_csv` other than a single character:
    
        >>> import io
        >>> csv = '''a;b;c
        ...           1;1,8
        ...           1;2,1'''
        >>> df = pd.read_csv(io.StringIO(csv), sep='[;,]')  # doctest: +SKIP
        ... # ParserWarning: Falling back to the 'python' engine...
    
        Adding `engine='python'` to `pd.read_csv` removes the Warning:
    
        >>> df = pd.read_csv(io.StringIO(csv), sep='[;,]', engine='python')
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class TextReader(object):
    """ # source: StringIO or file object """
    def close(self, *args, **kwargs): # real signature unknown
        pass

    def read(self, *args, **kwargs): # real signature unknown
        """ rows=None --> read all rows """
        pass

    def remove_noconvert(self, *args, **kwargs): # real signature unknown
        pass

    def set_error_bad_lines(self, *args, **kwargs): # real signature unknown
        pass

    def set_noconvert(self, *args, **kwargs): # real signature unknown
        pass

    def _convert_column_data(self, *args, **kwargs): # real signature unknown
        pass

    def _get_converter(self, *args, **kwargs): # real signature unknown
        pass

    def _set_quoting(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    allow_leading_cols = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    buffer_lines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    compression = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    delimiter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    delim_whitespace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dtype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dtype_cast_order = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    encoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    header = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    header_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    header_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    index_col = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leading_cols = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    low_memory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mangle_dupe_cols = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    memory_map = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    na_values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    noconvert = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    orig_header = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    skipfooter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    skiprows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    table_width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unnamed_cols = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    usecols = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001DF4B353240>'


# variables with complex values

na_values = {
    np.double: 
        nan
    ,
    np.intp: 
        -9223372036854775808
    ,
    np.int32: 
        -2147483648
    ,
    np.short: 
        -32768
    ,
    np.byte: 
        -128
    ,
    np.uintp: 
        18446744073709551615
    ,
    np.uint: 
        4294967295
    ,
    np.ushort: 
        65535
    ,
    np.ubyte: 
        255
    ,
    np.bool8: 
        255
    ,
    np.object0: 
        nan
    ,
    dtype('float64'): 
        nan
    ,
    dtype('int64'): 
        -9223372036854775808
    ,
    dtype('int32'): 
        -2147483648
    ,
    dtype('int16'): 
        -32768
    ,
    dtype('int8'): 
        -128
    ,
    dtype('uint64'): 
        18446744073709551615
    ,
    dtype('uint32'): 
        4294967295
    ,
    dtype('uint16'): 
        65535
    ,
    dtype('uint8'): 
        255
    ,
    dtype('bool'): 
        255
    ,
    dtype('O'): 
        nan
    ,
}

STR_NA_VALUES = None # (!) real value is "{'', 'nan', '-nan', '1.#QNAN', '-1.#IND', 'NA', 'N/A', 'NaN', '-NaN', '1.#IND', 'NULL', 'null', '#NA', 'n/a', '<NA>', '#N/A N/A', '#N/A', '-1.#QNAN'}"

_NA_VALUES = [
    b'',
    b'nan',
    b'-nan',
    b'1.#QNAN',
    b'-1.#IND',
    b'NA',
    b'N/A',
    b'NaN',
    b'-NaN',
    b'1.#IND',
    b'NULL',
    b'null',
    b'#NA',
    b'n/a',
    b'<NA>',
    b'#N/A N/A',
    b'#N/A',
    b'-1.#QNAN',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001DF4B360F98>'

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.parsers', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001DF4B360F98>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\pandas\\\\_libs\\\\parsers.cp37-win_amd64.pyd')"

__test__ = {}

