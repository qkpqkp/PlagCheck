# encoding: utf-8
# module bottleneck.move
# from C:\Users\Doly\Anaconda3\lib\site-packages\bottleneck\move.cp37-win_amd64.pyd
# by generator 1.147
""" Bottleneck moving window functions. """
# no imports

# functions

def move_argmax(a, window, min_count=None, axis=-1): # real signature unknown; restored from __doc__
    """
    move_argmax(a, window, min_count=None, axis=-1)
    
    Moving window index of maximum along the specified axis, optionally
    ignoring NaNs.
    
    Index 0 is at the rightmost edge of the window. For example, if the array
    is monotonically increasing (decreasing) along the specified axis then
    the output array will contain zeros (window-1).
    
    If there is a tie in input values within a window, then the rightmost
    index is returned.
    
    float64 output is returned for all input data types.
    
    Parameters
    ----------
    a : ndarray
        Input array. If `a` is not an array, a conversion is attempted.
    window : int
        The number of elements in the moving window.
    min_count: {int, None}, optional
        If the number of non-NaN values in a window is less than `min_count`,
        then a value of NaN is assigned to the window. By default `min_count`
        is None, which is equivalent to setting `min_count` equal to `window`.
    axis : int, optional
        The axis over which the window is moved. By default the last axis
        (axis=-1) is used. An axis of None is not allowed.
    
    Returns
    -------
    y : ndarray
        The moving index of maximum values of the input array along the
        specified axis. The output has the same shape as the input. The dtype
        of the output is always float64.
    
    Examples
    --------
    >>> a = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    >>> bn.move_argmax(a, window=2)
    array([ nan,   0.,   0.,   0.,   0.])
    
    >>> a = np.array([5.0, 4.0, 3.0, 2.0, 1.0])
    >>> bn.move_argmax(a, window=2)
    array([ nan,   1.,   1.,   1.,   1.])
    
    >>> a = np.array([2.0, 3.0, 4.0, 1.0, 7.0, 5.0, 6.0])
    >>> bn.move_argmax(a, window=3)
    array([ nan,  nan,   0.,   1.,   0.,   1.,   2.])
    """
    pass

def move_argmin(a, window, min_count=None, axis=-1): # real signature unknown; restored from __doc__
    """
    move_argmin(a, window, min_count=None, axis=-1)
    
    Moving window index of minimum along the specified axis, optionally
    ignoring NaNs.
    
    Index 0 is at the rightmost edge of the window. For example, if the array
    is monotonically decreasing (increasing) along the specified axis then
    the output array will contain zeros (window-1).
    
    If there is a tie in input values within a window, then the rightmost
    index is returned.
    
    float64 output is returned for all input data types.
    
    Parameters
    ----------
    a : ndarray
        Input array. If `a` is not an array, a conversion is attempted.
    window : int
        The number of elements in the moving window.
    min_count: {int, None}, optional
        If the number of non-NaN values in a window is less than `min_count`,
        then a value of NaN is assigned to the window. By default `min_count`
        is None, which is equivalent to setting `min_count` equal to `window`.
    axis : int, optional
        The axis over which the window is moved. By default the last axis
        (axis=-1) is used. An axis of None is not allowed.
    
    Returns
    -------
    y : ndarray
        The moving index of minimum values of the input array along the
        specified axis. The output has the same shape as the input. The dtype
        of the output is always float64.
    
    Examples
    --------
    >>> a = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    >>> bn.move_argmin(a, window=2)
    array([ nan,   1.,   1.,   1.,   1.])
    
    >>> a = np.array([5.0, 4.0, 3.0, 2.0, 1.0])
    >>> bn.move_argmin(a, window=2)
    array([ nan,   0.,   0.,   0.,   0.])
    
    >>> a = np.array([2.0, 3.0, 4.0, 1.0, 7.0, 5.0, 6.0])
    >>> bn.move_argmin(a, window=3)
    array([ nan,  nan,   2.,   0.,   1.,   2.,   1.])
    """
    pass

def move_max(a, window, min_count=None, axis=-1): # real signature unknown; restored from __doc__
    """
    move_max(a, window, min_count=None, axis=-1)
    
    Moving window maximum along the specified axis, optionally ignoring NaNs.
    
    float64 output is returned for all input data types.
    
    Parameters
    ----------
    a : ndarray
        Input array. If `a` is not an array, a conversion is attempted.
    window : int
        The number of elements in the moving window.
    min_count: {int, None}, optional
        If the number of non-NaN values in a window is less than `min_count`,
        then a value of NaN is assigned to the window. By default `min_count`
        is None, which is equivalent to setting `min_count` equal to `window`.
    axis : int, optional
        The axis over which the window is moved. By default the last axis
        (axis=-1) is used. An axis of None is not allowed.
    
    Returns
    -------
    y : ndarray
        The moving maximum of the input array along the specified axis. The
        output has the same shape as the input. The dtype of the output is
        always float64.
    
    Examples
    --------
    >>> a = np.array([1.0, 2.0, 3.0, np.nan, 5.0])
    >>> bn.move_max(a, window=2)
    array([ nan,   2.,   3.,  nan,  nan])
    >>> bn.move_max(a, window=2, min_count=1)
    array([ 1.,  2.,  3.,  3.,  5.])
    """
    pass

def move_mean(a, window, min_count=None, axis=-1): # real signature unknown; restored from __doc__
    """
    move_mean(a, window, min_count=None, axis=-1)
    
    Moving window mean along the specified axis, optionally ignoring NaNs.
    
    This function cannot handle input arrays that contain Inf. When the
    window contains Inf, the output will correctly be Inf. However, when Inf
    moves out of the window, the remaining output values in the slice will
    incorrectly be NaN.
    
    Parameters
    ----------
    a : ndarray
        Input array. If `a` is not an array, a conversion is attempted.
    window : int
        The number of elements in the moving window.
    min_count: {int, None}, optional
        If the number of non-NaN values in a window is less than `min_count`,
        then a value of NaN is assigned to the window. By default `min_count`
        is None, which is equivalent to setting `min_count` equal to `window`.
    axis : int, optional
        The axis over which the window is moved. By default the last axis
        (axis=-1) is used. An axis of None is not allowed.
    
    Returns
    -------
    y : ndarray
        The moving mean of the input array along the specified axis. The output
        has the same shape as the input.
    
    Examples
    --------
    >>> a = np.array([1.0, 2.0, 3.0, np.nan, 5.0])
    >>> bn.move_mean(a, window=2)
    array([ nan,  1.5,  2.5,  nan,  nan])
    >>> bn.move_mean(a, window=2, min_count=1)
    array([ 1. ,  1.5,  2.5,  3. ,  5. ])
    """
    pass

def move_median(a, window, min_count=None, axis=-1): # real signature unknown; restored from __doc__
    """
    move_median(a, window, min_count=None, axis=-1)
    
    Moving window median along the specified axis, optionally ignoring NaNs.
    
    float64 output is returned for all input data types.
    
    Parameters
    ----------
    a : ndarray
        Input array. If `a` is not an array, a conversion is attempted.
    window : int
        The number of elements in the moving window.
    min_count: {int, None}, optional
        If the number of non-NaN values in a window is less than `min_count`,
        then a value of NaN is assigned to the window. By default `min_count`
        is None, which is equivalent to setting `min_count` equal to `window`.
    axis : int, optional
        The axis over which the window is moved. By default the last axis
        (axis=-1) is used. An axis of None is not allowed.
    
    Returns
    -------
    y : ndarray
        The moving median of the input array along the specified axis. The
        output has the same shape as the input.
    
    Examples
    --------
    >>> a = np.array([1.0, 2.0, 3.0, 4.0])
    >>> bn.move_median(a, window=2)
    array([ nan,  1.5,  2.5,  3.5])
    >>> bn.move_median(a, window=2, min_count=1)
    array([ 1. ,  1.5,  2.5,  3.5])
    """
    pass

def move_min(a, window, min_count=None, axis=-1): # real signature unknown; restored from __doc__
    """
    move_min(a, window, min_count=None, axis=-1)
    
    Moving window minimum along the specified axis, optionally ignoring NaNs.
    
    float64 output is returned for all input data types.
    
    Parameters
    ----------
    a : ndarray
        Input array. If `a` is not an array, a conversion is attempted.
    window : int
        The number of elements in the moving window.
    min_count: {int, None}, optional
        If the number of non-NaN values in a window is less than `min_count`,
        then a value of NaN is assigned to the window. By default `min_count`
        is None, which is equivalent to setting `min_count` equal to `window`.
    axis : int, optional
        The axis over which the window is moved. By default the last axis
        (axis=-1) is used. An axis of None is not allowed.
    
    Returns
    -------
    y : ndarray
        The moving minimum of the input array along the specified axis. The
        output has the same shape as the input. The dtype of the output is
        always float64.
    
    Examples
    --------
    >>> a = np.array([1.0, 2.0, 3.0, np.nan, 5.0])
    >>> bn.move_min(a, window=2)
    array([ nan,   1.,   2.,  nan,  nan])
    >>> bn.move_min(a, window=2, min_count=1)
    array([ 1.,  1.,  2.,  3.,  5.])
    """
    pass

def move_rank(a, window, min_count=None, axis=-1): # real signature unknown; restored from __doc__
    """
    move_rank(a, window, min_count=None, axis=-1)
    
    Moving window ranking along the specified axis, optionally ignoring NaNs.
    
    The output is normalized to be between -1 and 1. For example, with a
    window width of 3 (and with no ties), the possible output values are
    -1, 0, 1.
    
    Ties are broken by averaging the rankings. See the examples below.
    
    The runtime depends almost linearly on `window`. The more NaNs there are
    in the input array, the shorter the runtime.
    
    Parameters
    ----------
    a : ndarray
        Input array. If `a` is not an array, a conversion is attempted.
    window : int
        The number of elements in the moving window.
    min_count: {int, None}, optional
        If the number of non-NaN values in a window is less than `min_count`,
        then a value of NaN is assigned to the window. By default `min_count`
        is None, which is equivalent to setting `min_count` equal to `window`.
    axis : int, optional
        The axis over which the window is moved. By default the last axis
        (axis=-1) is used. An axis of None is not allowed.
    
    Returns
    -------
    y : ndarray
        The moving ranking along the specified axis. The output has the same
        shape as the input. For integer input arrays, the dtype of the output
        is float64.
    
    Examples
    --------
    With window=3 and no ties, there are 3 possible output values, i.e.
    [-1., 0., 1.]:
    
    >>> a = np.array([1, 2, 3, 9, 8, 7, 5, 6, 4])
    >>> bn.move_rank(a, window=3)
        array([ nan,  nan,   1.,   1.,   0.,  -1.,  -1.,   0.,  -1.])
    
    Ties are broken by averaging the rankings of the tied elements:
    
    >>> a = np.array([1, 2, 3, 3, 3, 4])
    >>> bn.move_rank(a, window=3)
        array([ nan,  nan,  1. ,  0.5,  0. ,  1. ])
    
    In an increasing sequence, the moving window ranking is always equal to 1:
    
    >>> a = np.array([1, 2, 3, 4, 5])
    >>> bn.move_rank(a, window=2)
        array([ nan,   1.,   1.,   1.,   1.])
    """
    pass

def move_std(a, window, min_count=None, axis=-1, ddof=0): # real signature unknown; restored from __doc__
    """
    move_std(a, window, min_count=None, axis=-1, ddof=0)
    
    Moving window standard deviation along the specified axis, optionally
    ignoring NaNs.
    
    This function cannot handle input arrays that contain Inf. When Inf
    enters the moving window, the outout becomes NaN and will continue to
    be NaN for the remainer of the slice.
    
    Unlike bn.nanstd, which uses a two-pass algorithm, move_nanstd uses a
    one-pass algorithm called Welford's method. The algorithm is slow but
    numerically stable for cases where the mean is large compared to the
    standard deviation.
    
    Parameters
    ----------
    a : ndarray
        Input array. If `a` is not an array, a conversion is attempted.
    window : int
        The number of elements in the moving window.
    min_count: {int, None}, optional
        If the number of non-NaN values in a window is less than `min_count`,
        then a value of NaN is assigned to the window. By default `min_count`
        is None, which is equivalent to setting `min_count` equal to `window`.
    axis : int, optional
        The axis over which the window is moved. By default the last axis
        (axis=-1) is used. An axis of None is not allowed.
    ddof : int, optional
        Means Delta Degrees of Freedom. The divisor used in calculations
        is ``N - ddof``, where ``N`` represents the number of elements.
        By default `ddof` is zero.
    
    Returns
    -------
    y : ndarray
        The moving standard deviation of the input array along the specified
        axis. The output has the same shape as the input.
    
    Examples
    --------
    >>> a = np.array([1.0, 2.0, 3.0, np.nan, 5.0])
    >>> bn.move_std(a, window=2)
    array([ nan,  0.5,  0.5,  nan,  nan])
    >>> bn.move_std(a, window=2, min_count=1)
    array([ 0. ,  0.5,  0.5,  0. ,  0. ])
    """
    pass

def move_sum(a, window, min_count=None, axis=-1): # real signature unknown; restored from __doc__
    """
    move_sum(a, window, min_count=None, axis=-1)
    
    Moving window sum along the specified axis, optionally ignoring NaNs.
    
    This function cannot handle input arrays that contain Inf. When the
    window contains Inf, the output will correctly be Inf. However, when Inf
    moves out of the window, the remaining output values in the slice will
    incorrectly be NaN.
    
    Parameters
    ----------
    a : ndarray
        Input array. If `a` is not an array, a conversion is attempted.
    window : int
        The number of elements in the moving window.
    min_count: {int, None}, optional
        If the number of non-NaN values in a window is less than `min_count`,
        then a value of NaN is assigned to the window. By default `min_count`
        is None, which is equivalent to setting `min_count` equal to `window`.
    axis : int, optional
        The axis over which the window is moved. By default the last axis
        (axis=-1) is used. An axis of None is not allowed.
    
    Returns
    -------
    y : ndarray
        The moving sum of the input array along the specified axis. The output
        has the same shape as the input.
    
    Examples
    --------
    >>> a = np.array([1.0, 2.0, 3.0, np.nan, 5.0])
    >>> bn.move_sum(a, window=2)
    array([ nan,   3.,   5.,  nan,  nan])
    >>> bn.move_sum(a, window=2, min_count=1)
    array([ 1.,  3.,  5.,  3.,  5.])
    """
    pass

def move_var(a, window, min_count=None, axis=-1, ddof=0): # real signature unknown; restored from __doc__
    """
    move_var(a, window, min_count=None, axis=-1, ddof=0)
    
    Moving window variance along the specified axis, optionally ignoring NaNs.
    
    This function cannot handle input arrays that contain Inf. When Inf
    enters the moving window, the outout becomes NaN and will continue to
    be NaN for the remainer of the slice.
    
    Unlike bn.nanvar, which uses a two-pass algorithm, move_nanvar uses a
    one-pass algorithm called Welford's method. The algorithm is slow but
    numerically stable for cases where the mean is large compared to the
    standard deviation.
    
    Parameters
    ----------
    a : ndarray
        Input array. If `a` is not an array, a conversion is attempted.
    window : int
        The number of elements in the moving window.
    min_count: {int, None}, optional
        If the number of non-NaN values in a window is less than `min_count`,
        then a value of NaN is assigned to the window. By default `min_count`
        is None, which is equivalent to setting `min_count` equal to `window`.
    axis : int, optional
        The axis over which the window is moved. By default the last axis
        (axis=-1) is used. An axis of None is not allowed.
    ddof : int, optional
        Means Delta Degrees of Freedom. The divisor used in calculations
        is ``N - ddof``, where ``N`` represents the number of elements.
        By default `ddof` is zero.
    
    Returns
    -------
    y : ndarray
        The moving variance of the input array along the specified axis. The
        output has the same shape as the input.
    
    Examples
    --------
    >>> a = np.array([1.0, 2.0, 3.0, np.nan, 5.0])
    >>> bn.move_var(a, window=2)
    array([ nan,  0.25,  0.25,  nan,  nan])
    >>> bn.move_var(a, window=2, min_count=1)
    array([ 0. ,  0.25,  0.25,  0. ,  0. ])
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000021BE4BCD198>'

__spec__ = None # (!) real value is "ModuleSpec(name='bottleneck.move', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000021BE4BCD198>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\bottleneck\\\\move.cp37-win_amd64.pyd')"

