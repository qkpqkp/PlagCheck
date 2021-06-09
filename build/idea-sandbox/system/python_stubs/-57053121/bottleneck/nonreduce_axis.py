# encoding: utf-8
# module bottleneck.nonreduce_axis
# from C:\Users\Doly\Anaconda3\lib\site-packages\bottleneck\nonreduce_axis.cp37-win_amd64.pyd
# by generator 1.147
""" Bottleneck non-reducing functions that operate along an axis. """
# no imports

# functions

def argpartition(a, kth, axis=-1): # real signature unknown; restored from __doc__
    """
    argpartition(a, kth, axis=-1)
    
    Return indices that would partition array along the given axis.
    
    A 1d array B is partitioned at array index `kth` if three conditions
    are met: (1) B[kth] is in its sorted position, (2) all elements to the
    left of `kth` are less than or equal to B[kth], and (3) all elements
    to the right of `kth` are greater than or equal to B[kth]. Note that
    the array elements in conditions (2) and (3) are in general unordered.
    
    Shuffling the input array may change the output. The only guarantee is
    given by the three conditions above.
    
    This functions is not protected against NaN. Therefore, you may get
    unexpected results if the input contains NaN.
    
    Parameters
    ----------
    a : array_like
        Input array. If `a` is not an array, a conversion is attempted.
    kth : int
        The value of the element at index `kth` will be in its sorted
        position. Smaller (larger) or equal values will be to the left
        (right) of index `kth`.
    axis : {int, None}, optional
        Axis along which the partition is performed. The default (axis=-1)
        is to partition along the last axis.
    
    Returns
    -------
    y : ndarray
        An array the same shape as the input array containing the indices
        that partition `a`. The dtype of the indices is numpy.intp.
    
    See Also
    --------
    bottleneck.partition: Partition array elements along given axis.
    
    Notes
    -----
    Unexpected results may occur if the input array contains NaN.
    
    Examples
    --------
    Create a numpy array:
    
    >>> a = np.array([10, 0, 30, 40, 20])
    
    Find the indices that partition the array so that the first 3
    elements are the smallest 3 elements:
    
    >>> index = bn.argpartition(a, kth=2)
    >>> index
    array([0, 1, 4, 3, 2])
    
    Let's use the indices to partition the array (note, as in this
    example, that the smallest 3 elements may not be in order):
    
    >>> a[index]
    array([10, 0, 20, 40, 30])
    """
    pass

def nanrankdata(a, axis=None): # real signature unknown; restored from __doc__
    """
    nanrankdata(a, axis=None)
    
    Ranks the data, dealing with ties and NaNs appropriately.
    
    Equal values are assigned a rank that is the average of the ranks that
    would have been otherwise assigned to all of the values within that set.
    Ranks begin at 1, not 0.
    
    NaNs in the input array are returned as NaNs.
    
    Parameters
    ----------
    a : array_like
        Input array. If `a` is not an array, a conversion is attempted.
    axis : {int, None}, optional
        Axis along which the elements of the array are ranked. The default
        (axis=None) is to rank the elements of the flattened array.
    
    Returns
    -------
    y : ndarray
        An array with the same shape as `a`. The dtype is 'float64'.
    
    See also
    --------
    bottleneck.rankdata: Ranks the data, dealing with ties and appropriately.
    
    Examples
    --------
    >>> bn.nanrankdata([np.nan, 2, 2, 3])
    array([ nan,  1.5,  1.5,  3. ])
    >>> bn.nanrankdata([[np.nan, 2], [2, 3]])
    array([ nan,  1.5,  1.5,  3. ])
    >>> bn.nanrankdata([[np.nan, 2], [2, 3]], axis=0)
    array([[ nan,   1.],
           [  1.,   2.]])
    >>> bn.nanrankdata([[np.nan, 2], [2, 3]], axis=1)
    array([[ nan,   1.],
           [  1.,   2.]])
    """
    pass

def partition(a, kth, axis=-1): # real signature unknown; restored from __doc__
    """
    partition(a, kth, axis=-1)
    
    Partition array elements along given axis.
    
    A 1d array B is partitioned at array index `kth` if three conditions
    are met: (1) B[kth] is in its sorted position, (2) all elements to the
    left of `kth` are less than or equal to B[kth], and (3) all elements
    to the right of `kth` are greater than or equal to B[kth]. Note that
    the array elements in conditions (2) and (3) are in general unordered.
    
    Shuffling the input array may change the output. The only guarantee is
    given by the three conditions above.
    
    This functions is not protected against NaN. Therefore, you may get
    unexpected results if the input contains NaN.
    
    Parameters
    ----------
    a : array_like
        Input array. If `a` is not an array, a conversion is attempted.
    kth : int
        The value of the element at index `kth` will be in its sorted
        position. Smaller (larger) or equal values will be to the left
        (right) of index `kth`.
    axis : {int, None}, optional
        Axis along which the partition is performed. The default
        (axis=-1) is to partition along the last axis.
    
    Returns
    -------
    y : ndarray
        A partitioned copy of the input array with the same shape and
        type of `a`.
    
    See Also
    --------
    bottleneck.argpartition: Indices that would partition an array
    
    Notes
    -----
    Unexpected results may occur if the input array contains NaN.
    
    Examples
    --------
    Create a numpy array:
    
    >>> a = np.array([1, 0, 3, 4, 2])
    
    Partition array so that the first 3 elements (indices 0, 1, 2) are the
    smallest 3 elements (note, as in this example, that the smallest 3
    elements may not be sorted):
    
    >>> bn.partition(a, kth=2)
    array([1, 0, 2, 4, 3])
    
    Now Partition array so that the last 2 elements are the largest 2
    elements:
    
    >>> bn.partition(a, kth=3)
    array([1, 0, 2, 3, 4])
    """
    pass

def push(a, n=None, axis=-1): # real signature unknown; restored from __doc__
    """
    push(a, n=None, axis=-1)
    
    Fill missing values (NaNs) with most recent non-missing values.
    
    Filling proceeds along the specified axis from small index values to large
    index values.
    
    Parameters
    ----------
    a : array_like
        Input array. If `a` is not an array, a conversion is attempted.
    n : {int, None}, optional
        How far to push values. If the most recent non-NaN array element is
        more than `n` index positions away, than a NaN is returned. The default
        (n = None) is to push the entire length of the slice. If `n` is an integer
        it must be nonnegative.
    axis : int, optional
        Axis along which the elements of the array are pushed. The default
        (axis=-1) is to push along the last axis of the input array.
    
    Returns
    -------
    y : ndarray
        An array with the same shape and dtype as `a`.
    
    See also
    --------
    bottleneck.replace: Replace specified value of an array with new value.
    
    Examples
    --------
    >>> a = np.array([5, np.nan, np.nan, 6, np.nan])
    >>> bn.push(a)
        array([ 5.,  5.,  5.,  6.,  6.])
    >>> bn.push(a, n=1)
        array([  5.,   5.,  nan,   6.,   6.])
    >>> bn.push(a, n=2)
        array([ 5.,  5.,  5.,  6.,  6.])
    """
    pass

def rankdata(a, axis=None): # real signature unknown; restored from __doc__
    """
    rankdata(a, axis=None)
    
    Ranks the data, dealing with ties appropriately.
    
    Equal values are assigned a rank that is the average of the ranks that
    would have been otherwise assigned to all of the values within that set.
    Ranks begin at 1, not 0.
    
    Parameters
    ----------
    a : array_like
        Input array. If `a` is not an array, a conversion is attempted.
    axis : {int, None}, optional
        Axis along which the elements of the array are ranked. The default
        (axis=None) is to rank the elements of the flattened array.
    
    Returns
    -------
    y : ndarray
        An array with the same shape as `a`. The dtype is 'float64'.
    
    See also
    --------
    bottleneck.nanrankdata: Ranks the data dealing with ties and NaNs.
    
    Examples
    --------
    >>> bn.rankdata([0, 2, 2, 3])
    array([ 1. ,  2.5,  2.5,  4. ])
    >>> bn.rankdata([[0, 2], [2, 3]])
    array([ 1. ,  2.5,  2.5,  4. ])
    >>> bn.rankdata([[0, 2], [2, 3]], axis=0)
    array([[ 1.,  1.],
           [ 2.,  2.]])
    >>> bn.rankdata([[0, 2], [2, 3]], axis=1)
    array([[ 1.,  2.],
           [ 1.,  2.]])
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000002496242AE80>'

__spec__ = None # (!) real value is "ModuleSpec(name='bottleneck.nonreduce_axis', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000002496242AE80>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\bottleneck\\\\nonreduce_axis.cp37-win_amd64.pyd')"

