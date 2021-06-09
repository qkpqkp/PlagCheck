# encoding: utf-8
# module bottleneck.reduce
# from C:\Users\Doly\Anaconda3\lib\site-packages\bottleneck\reduce.cp37-win_amd64.pyd
# by generator 1.147
""" Bottleneck functions that reduce the input array along a specified axis. """
# no imports

# functions

def allnan(a, axis=None): # real signature unknown; restored from __doc__
    """
    allnan(a, axis=None)
    
    Test whether all array elements along a given axis are NaN.
    
    Returns the same output as np.isnan(a).all(axis)
    
    Note that allnan([]) is True to match np.isnan([]).all() and all([])
    
    Parameters
    ----------
    a : array_like
        Input array. If `a` is not an array, a conversion is attempted.
    axis : {int, None}, optional
        Axis along which NaNs are searched. The default (`axis` = ``None``)
        is to search for NaNs over a flattened input array.
    
    Returns
    -------
    y : bool or ndarray
        A boolean or new `ndarray` is returned.
    
    See also
    --------
    bottleneck.anynan: Test if any array element along given axis is NaN
    
    Examples
    --------
    >>> bn.allnan(1)
    False
    >>> bn.allnan(np.nan)
    True
    >>> bn.allnan([1, np.nan])
    False
    >>> a = np.array([[1, np.nan], [1, np.nan]])
    >>> bn.allnan(a)
    False
    >>> bn.allnan(a, axis=0)
    array([False,  True], dtype=bool)
    
    An empty array returns True:
    
    >>> bn.allnan([])
    True
    
    which is similar to:
    
    >>> all([])
    True
    >>> np.isnan([]).all()
    True
    """
    pass

def anynan(a, axis=None): # real signature unknown; restored from __doc__
    """
    anynan(a, axis=None)
    
    Test whether any array element along a given axis is NaN.
    
    Returns the same output as np.isnan(a).any(axis)
    
    Parameters
    ----------
    a : array_like
        Input array. If `a` is not an array, a conversion is attempted.
    axis : {int, None}, optional
        Axis along which NaNs are searched. The default (`axis` = ``None``)
        is to search for NaNs over a flattened input array.
    
    Returns
    -------
    y : bool or ndarray
        A boolean or new `ndarray` is returned.
    
    See also
    --------
    bottleneck.allnan: Test if all array elements along given axis are NaN
    
    Examples
    --------
    >>> bn.anynan(1)
    False
    >>> bn.anynan(np.nan)
    True
    >>> bn.anynan([1, np.nan])
    True
    >>> a = np.array([[1, 4], [1, np.nan]])
    >>> bn.anynan(a)
    True
    >>> bn.anynan(a, axis=0)
    array([False,  True], dtype=bool)
    """
    pass

def median(a, axis=None): # real signature unknown; restored from __doc__
    """
    median(a, axis=None)
    
    Median of array elements along given axis.
    
    Parameters
    ----------
    a : array_like
        Input array. If `a` is not an array, a conversion is attempted.
    axis : {int, None}, optional
        Axis along which the median is computed. The default (axis=None) is to
        compute the median of the flattened array.
    
    Returns
    -------
    y : ndarray
        An array with the same shape as `a`, except that the specified axis
        has been removed. If `a` is a 0d array, or if axis is None, a scalar
        is returned. `float64` return values are used for integer inputs. NaN
        is returned for a slice that contains one or more NaNs.
    
    See also
    --------
    bottleneck.nanmedian: Median along specified axis ignoring NaNs.
    
    Examples
    --------
    >>> a = np.array([[10, 7, 4], [3, 2, 1]])
    >>> bn.median(a)
        3.5
    >>> bn.median(a, axis=0)
        array([ 6.5,  4.5,  2.5])
    >>> bn.median(a, axis=1)
        array([ 7.,  2.])
    """
    pass

def nanargmax(a, axis=None): # real signature unknown; restored from __doc__
    """
    nanargmax(a, axis=None)
    
    Indices of the maximum values along an axis, ignoring NaNs.
    
    For all-NaN slices ``ValueError`` is raised. Unlike NumPy, the results
    can be trusted if a slice contains only NaNs and Infs.
    
    Parameters
    ----------
    a : array_like
        Input array. If `a` is not an array, a conversion is attempted.
    axis : {int, None}, optional
        Axis along which to operate. By default (axis=None) flattened input
        is used.
    
    See also
    --------
    bottleneck.nanargmin: Indices of the minimum values along an axis.
    bottleneck.nanmax: Maximum values along specified axis, ignoring NaNs.
    
    Returns
    -------
    index_array : ndarray
        An array of indices or a single index value.
    
    Examples
    --------
    >>> a = np.array([[np.nan, 4], [2, 3]])
    >>> bn.nanargmax(a)
    1
    >>> a.flat[1]
    4.0
    >>> bn.nanargmax(a, axis=0)
    array([1, 0])
    >>> bn.nanargmax(a, axis=1)
    array([1, 1])
    """
    pass

def nanargmin(a, axis=None): # real signature unknown; restored from __doc__
    """
    nanargmin(a, axis=None)
    
    Indices of the minimum values along an axis, ignoring NaNs.
    
    For all-NaN slices ``ValueError`` is raised. Unlike NumPy, the results
    can be trusted if a slice contains only NaNs and Infs.
    
    Parameters
    ----------
    a : array_like
        Input array. If `a` is not an array, a conversion is attempted.
    axis : {int, None}, optional
        Axis along which to operate. By default (axis=None) flattened input
        is used.
    
    See also
    --------
    bottleneck.nanargmax: Indices of the maximum values along an axis.
    bottleneck.nanmin: Minimum values along specified axis, ignoring NaNs.
    
    Returns
    -------
    index_array : ndarray
        An array of indices or a single index value.
    
    Examples
    --------
    >>> a = np.array([[np.nan, 4], [2, 3]])
    >>> bn.nanargmin(a)
    2
    >>> a.flat[2]
    2.0
    >>> bn.nanargmin(a, axis=0)
    array([1, 1])
    >>> bn.nanargmin(a, axis=1)
    array([1, 0])
    """
    pass

def nanmax(a, axis=None): # real signature unknown; restored from __doc__
    """
    nanmax(a, axis=None)
    
    Maximum values along specified axis, ignoring NaNs.
    
    When all-NaN slices are encountered, NaN is returned for that slice.
    
    Parameters
    ----------
    a : array_like
        Input array. If `a` is not an array, a conversion is attempted.
    axis : {int, None}, optional
        Axis along which the maximum is computed. The default (axis=None) is
        to compute the maximum of the flattened array.
    
    Returns
    -------
    y : ndarray
        An array with the same shape as `a`, with the specified axis removed.
        If `a` is a 0-d array, or if axis is None, a scalar is returned. The
        same dtype as `a` is returned.
    
    See also
    --------
    bottleneck.nanmin: Minimum along specified axis, ignoring NaNs.
    bottleneck.nanargmax: Indices of maximum values along axis, ignoring NaNs.
    
    Examples
    --------
    >>> bn.nanmax(1)
    1
    >>> bn.nanmax([1])
    1
    >>> bn.nanmax([1, np.nan])
    1.0
    >>> a = np.array([[1, 4], [1, np.nan]])
    >>> bn.nanmax(a)
    4.0
    >>> bn.nanmax(a, axis=0)
    array([ 1.,  4.])
    """
    pass

def nanmean(a, axis=None): # real signature unknown; restored from __doc__
    """
    nanmean(a, axis=None)
    
    Mean of array elements along given axis ignoring NaNs.
    
    `float64` intermediate and return values are used for integer inputs.
    
    Parameters
    ----------
    a : array_like
        Array containing numbers whose mean is desired. If `a` is not an
        array, a conversion is attempted.
    axis : {int, None}, optional
        Axis along which the means are computed. The default (axis=None) is to
        compute the mean of the flattened array.
    
    Returns
    -------
    y : ndarray
        An array with the same shape as `a`, with the specified axis removed.
        If `a` is a 0-d array, or if axis is None, a scalar is returned.
        `float64` intermediate and return values are used for integer inputs.
    
    See also
    --------
    bottleneck.nanmedian: Median along specified axis, ignoring NaNs.
    
    Notes
    -----
    No error is raised on overflow. (The sum is computed and then the result
    is divided by the number of non-NaN elements.)
    
    If positive or negative infinity are present the result is positive or
    negative infinity. But if both positive and negative infinity are present,
    the result is Not A Number (NaN).
    
    Examples
    --------
    >>> bn.nanmean(1)
    1.0
    >>> bn.nanmean([1])
    1.0
    >>> bn.nanmean([1, np.nan])
    1.0
    >>> a = np.array([[1, 4], [1, np.nan]])
    >>> bn.nanmean(a)
    2.0
    >>> bn.nanmean(a, axis=0)
    array([ 1.,  4.])
    
    When positive infinity and negative infinity are present:
    
    >>> bn.nanmean([1, np.nan, np.inf])
    inf
    >>> bn.nanmean([1, np.nan, np.NINF])
    -inf
    >>> bn.nanmean([1, np.nan, np.inf, np.NINF])
    nan
    """
    pass

def nanmedian(a, axis=None): # real signature unknown; restored from __doc__
    """
    nanmedian(a, axis=None)
    
    Median of array elements along given axis ignoring NaNs.
    
    Parameters
    ----------
    a : array_like
        Input array. If `a` is not an array, a conversion is attempted.
    axis : {int, None}, optional
        Axis along which the median is computed. The default (axis=None) is to
        compute the median of the flattened array.
    
    Returns
    -------
    y : ndarray
        An array with the same shape as `a`, except that the specified axis
        has been removed. If `a` is a 0d array, or if axis is None, a scalar
        is returned. `float64` return values are used for integer inputs.
    
    See also
    --------
    bottleneck.median: Median along specified axis.
    
    Examples
    --------
    >>> a = np.array([[np.nan, 7, 4], [3, 2, 1]])
    >>> a
    array([[ nan,   7.,   4.],
           [  3.,   2.,   1.]])
    >>> bn.nanmedian(a)
    3.0
    >> bn.nanmedian(a, axis=0)
    array([ 3. ,  4.5,  2.5])
    >> bn.nanmedian(a, axis=1)
    array([ 5.5,  2. ])
    """
    pass

def nanmin(a, axis=None): # real signature unknown; restored from __doc__
    """
    nanmin(a, axis=None)
    
    Minimum values along specified axis, ignoring NaNs.
    
    When all-NaN slices are encountered, NaN is returned for that slice.
    
    Parameters
    ----------
    a : array_like
        Input array. If `a` is not an array, a conversion is attempted.
    axis : {int, None}, optional
        Axis along which the minimum is computed. The default (axis=None) is
        to compute the minimum of the flattened array.
    
    Returns
    -------
    y : ndarray
        An array with the same shape as `a`, with the specified axis removed.
        If `a` is a 0-d array, or if axis is None, a scalar is returned. The
        same dtype as `a` is returned.
    
    See also
    --------
    bottleneck.nanmax: Maximum along specified axis, ignoring NaNs.
    bottleneck.nanargmin: Indices of minimum values along axis, ignoring NaNs.
    
    Examples
    --------
    >>> bn.nanmin(1)
    1
    >>> bn.nanmin([1])
    1
    >>> bn.nanmin([1, np.nan])
    1.0
    >>> a = np.array([[1, 4], [1, np.nan]])
    >>> bn.nanmin(a)
    1.0
    >>> bn.nanmin(a, axis=0)
    array([ 1.,  4.])
    """
    pass

def nanstd(a, axis=None, ddof=0): # real signature unknown; restored from __doc__
    """
    nanstd(a, axis=None, ddof=0)
    
    Standard deviation along the specified axis, ignoring NaNs.
    
    `float64` intermediate and return values are used for integer inputs.
    
    Instead of a faster one-pass algorithm, a more stable two-pass algorithm
    is used.
    
    An example of a one-pass algorithm:
    
        >>> np.sqrt((a*a).mean() - a.mean()**2)
    
    An example of a two-pass algorithm:
    
        >>> np.sqrt(((a - a.mean())**2).mean())
    
    Note in the two-pass algorithm the mean must be found (first pass) before
    the squared deviation (second pass) can be found.
    
    Parameters
    ----------
    a : array_like
        Input array. If `a` is not an array, a conversion is attempted.
    axis : {int, None}, optional
        Axis along which the standard deviation is computed. The default
        (axis=None) is to compute the standard deviation of the flattened
        array.
    ddof : int, optional
        Means Delta Degrees of Freedom. The divisor used in calculations
        is ``N - ddof``, where ``N`` represents the number of non-NaN elements.
        By default `ddof` is zero.
    
    Returns
    -------
    y : ndarray
        An array with the same shape as `a`, with the specified axis removed.
        If `a` is a 0-d array, or if axis is None, a scalar is returned.
        `float64` intermediate and return values are used for integer inputs.
        If ddof is >= the number of non-NaN elements in a slice or the slice
        contains only NaNs, then the result for that slice is NaN.
    
    See also
    --------
    bottleneck.nanvar: Variance along specified axis ignoring NaNs
    
    Notes
    -----
    If positive or negative infinity are present the result is Not A Number
    (NaN).
    
    Examples
    --------
    >>> bn.nanstd(1)
    0.0
    >>> bn.nanstd([1])
    0.0
    >>> bn.nanstd([1, np.nan])
    0.0
    >>> a = np.array([[1, 4], [1, np.nan]])
    >>> bn.nanstd(a)
    1.4142135623730951
    >>> bn.nanstd(a, axis=0)
    array([ 0.,  0.])
    
    When positive infinity or negative infinity are present NaN is returned:
    
    >>> bn.nanstd([1, np.nan, np.inf])
    nan
    """
    pass

def nansum(a, axis=None): # real signature unknown; restored from __doc__
    """
    nansum(a, axis=None)
    
    Sum of array elements along given axis treating NaNs as zero.
    
    The data type (dtype) of the output is the same as the input. On 64-bit
    operating systems, 32-bit input is NOT upcast to 64-bit accumulator and
    return values.
    
    Parameters
    ----------
    a : array_like
        Array containing numbers whose sum is desired. If `a` is not an
        array, a conversion is attempted.
    axis : {int, None}, optional
        Axis along which the sum is computed. The default (axis=None) is to
        compute the sum of the flattened array.
    
    Returns
    -------
    y : ndarray
        An array with the same shape as `a`, with the specified axis removed.
        If `a` is a 0-d array, or if axis is None, a scalar is returned.
    
    Notes
    -----
    No error is raised on overflow.
    
    If positive or negative infinity are present the result is positive or
    negative infinity. But if both positive and negative infinity are present,
    the result is Not A Number (NaN).
    
    Examples
    --------
    >>> bn.nansum(1)
    1
    >>> bn.nansum([1])
    1
    >>> bn.nansum([1, np.nan])
    1.0
    >>> a = np.array([[1, 1], [1, np.nan]])
    >>> bn.nansum(a)
    3.0
    >>> bn.nansum(a, axis=0)
    array([ 2.,  1.])
    
    When positive infinity and negative infinity are present:
    
    >>> bn.nansum([1, np.nan, np.inf])
    inf
    >>> bn.nansum([1, np.nan, np.NINF])
    -inf
    >>> bn.nansum([1, np.nan, np.inf, np.NINF])
    nan
    """
    pass

def nanvar(a, axis=None, ddof=0): # real signature unknown; restored from __doc__
    """
    nanvar(a, axis=None, ddof=0)
    
    Variance along the specified axis, ignoring NaNs.
    
    `float64` intermediate and return values are used for integer inputs.
    
    Instead of a faster one-pass algorithm, a more stable two-pass algorithm
    is used.
    
    An example of a one-pass algorithm:
    
        >>> (a*a).mean() - a.mean()**2
    
    An example of a two-pass algorithm:
    
        >>> ((a - a.mean())**2).mean()
    
    Note in the two-pass algorithm the mean must be found (first pass) before
    the squared deviation (second pass) can be found.
    
    Parameters
    ----------
    a : array_like
        Input array. If `a` is not an array, a conversion is attempted.
    axis : {int, None}, optional
        Axis along which the variance is computed. The default (axis=None) is
        to compute the variance of the flattened array.
    ddof : int, optional
        Means Delta Degrees of Freedom. The divisor used in calculations
        is ``N - ddof``, where ``N`` represents the number of non_NaN elements.
        By default `ddof` is zero.
    
    Returns
    -------
    y : ndarray
        An array with the same shape as `a`, with the specified axis
        removed. If `a` is a 0-d array, or if axis is None, a scalar is
        returned. `float64` intermediate and return values are used for
        integer inputs. If ddof is >= the number of non-NaN elements in a
        slice or the slice contains only NaNs, then the result for that slice
        is NaN.
    
    See also
    --------
    bottleneck.nanstd: Standard deviation along specified axis ignoring NaNs.
    
    Notes
    -----
    If positive or negative infinity are present the result is Not A Number
    (NaN).
    
    Examples
    --------
    >>> bn.nanvar(1)
    0.0
    >>> bn.nanvar([1])
    0.0
    >>> bn.nanvar([1, np.nan])
    0.0
    >>> a = np.array([[1, 4], [1, np.nan]])
    >>> bn.nanvar(a)
    2.0
    >>> bn.nanvar(a, axis=0)
    array([ 0.,  0.])
    
    When positive infinity or negative infinity are present NaN is returned:
    
    >>> bn.nanvar([1, np.nan, np.inf])
    nan
    """
    pass

def ss(a, axis=None): # real signature unknown; restored from __doc__
    """
    ss(a, axis=None)
    
    Sum of the square of each element along the specified axis.
    
    Parameters
    ----------
    a : array_like
        Array whose sum of squares is desired. If `a` is not an array, a
        conversion is attempted.
    axis : {int, None}, optional
        Axis along which the sum of squares is computed. The default
        (axis=None) is to sum the squares of the flattened array.
    
    Returns
    -------
    y : ndarray
        The sum of a**2 along the given axis.
    
    Examples
    --------
    >>> a = np.array([1., 2., 5.])
    >>> bn.ss(a)
    30.0
    
    And calculating along an axis:
    
    >>> b = np.array([[1., 2., 5.], [2., 5., 6.]])
    >>> bn.ss(b, axis=1)
    array([ 30., 65.])
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001A749C78278>'

__spec__ = None # (!) real value is "ModuleSpec(name='bottleneck.reduce', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001A749C78278>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\bottleneck\\\\reduce.cp37-win_amd64.pyd')"

