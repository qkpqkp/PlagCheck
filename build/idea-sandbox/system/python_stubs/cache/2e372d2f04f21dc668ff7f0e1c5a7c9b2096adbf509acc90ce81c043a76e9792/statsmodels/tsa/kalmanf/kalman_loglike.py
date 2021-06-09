# encoding: utf-8
# module statsmodels.tsa.kalmanf.kalman_loglike
# from C:\Users\Doly\Anaconda3\lib\site-packages\statsmodels\tsa\kalmanf\kalman_loglike.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

# Variables with simple values

pi = 3.141592653589793

# functions

def asfortranarray(a, dtype=None): # reliably restored by inspect
    """
    Return an array (ndim >= 1) laid out in Fortran order in memory.
    
        Parameters
        ----------
        a : array_like
            Input array.
        dtype : str or dtype object, optional
            By default, the data-type is inferred from the input data.
    
        Returns
        -------
        out : ndarray
            The input `a` in Fortran, or column-major, order.
    
        See Also
        --------
        ascontiguousarray : Convert input to a contiguous (C order) array.
        asanyarray : Convert input to an ndarray with either row or
            column-major memory order.
        require : Return an ndarray that satisfies requirements.
        ndarray.flags : Information about the memory layout of the array.
    
        Examples
        --------
        >>> x = np.arange(6).reshape(2,3)
        >>> y = np.asfortranarray(x)
        >>> x.flags['F_CONTIGUOUS']
        False
        >>> y.flags['F_CONTIGUOUS']
        True
    
        Note: This function returns an array with at least one-dimension (1-d) 
        so it will not preserve 0-d arrays.
    """
    pass

def dot(*args, **kwargs): # reliably restored by inspect
    """
    dot(a, b, out=None)
    
        Dot product of two arrays. Specifically,
    
        - If both `a` and `b` are 1-D arrays, it is inner product of vectors
          (without complex conjugation).
    
        - If both `a` and `b` are 2-D arrays, it is matrix multiplication,
          but using :func:`matmul` or ``a @ b`` is preferred.
    
        - If either `a` or `b` is 0-D (scalar), it is equivalent to :func:`multiply`
          and using ``numpy.multiply(a, b)`` or ``a * b`` is preferred.
    
        - If `a` is an N-D array and `b` is a 1-D array, it is a sum product over
          the last axis of `a` and `b`.
    
        - If `a` is an N-D array and `b` is an M-D array (where ``M>=2``), it is a
          sum product over the last axis of `a` and the second-to-last axis of `b`::
    
            dot(a, b)[i,j,k,m] = sum(a[i,j,:] * b[k,:,m])
    
        Parameters
        ----------
        a : array_like
            First argument.
        b : array_like
            Second argument.
        out : ndarray, optional
            Output argument. This must have the exact kind that would be returned
            if it was not used. In particular, it must have the right type, must be
            C-contiguous, and its dtype must be the dtype that would be returned
            for `dot(a,b)`. This is a performance feature. Therefore, if these
            conditions are not met, an exception is raised, instead of attempting
            to be flexible.
    
        Returns
        -------
        output : ndarray
            Returns the dot product of `a` and `b`.  If `a` and `b` are both
            scalars or both 1-D arrays then a scalar is returned; otherwise
            an array is returned.
            If `out` is given, then it is returned.
    
        Raises
        ------
        ValueError
            If the last dimension of `a` is not the same size as
            the second-to-last dimension of `b`.
    
        See Also
        --------
        vdot : Complex-conjugating dot product.
        tensordot : Sum products over arbitrary axes.
        einsum : Einstein summation convention.
        matmul : '@' operator as method with out parameter.
    
        Examples
        --------
        >>> np.dot(3, 4)
        12
    
        Neither argument is complex-conjugated:
    
        >>> np.dot([2j, 3j], [2j, 3j])
        (-13+0j)
    
        For 2-D arrays it is the matrix product:
    
        >>> a = [[1, 0], [0, 1]]
        >>> b = [[4, 1], [2, 2]]
        >>> np.dot(a, b)
        array([[4, 1],
               [2, 2]])
    
        >>> a = np.arange(3*4*5*6).reshape((3,4,5,6))
        >>> b = np.arange(3*4*5*6)[::-1].reshape((5,4,6,3))
        >>> np.dot(a, b)[2,3,2,1,2,2]
        499128
        >>> sum(a[2,3,2,:] * b[1,2,:,2])
        499128
    """
    pass

def identity(n, dtype=None): # reliably restored by inspect
    """
    Return the identity array.
    
        The identity array is a square array with ones on
        the main diagonal.
    
        Parameters
        ----------
        n : int
            Number of rows (and columns) in `n` x `n` output.
        dtype : data-type, optional
            Data-type of the output.  Defaults to ``float``.
    
        Returns
        -------
        out : ndarray
            `n` x `n` array with its main diagonal set to one,
            and all other elements 0.
    
        Examples
        --------
        >>> np.identity(3)
        array([[1.,  0.,  0.],
               [0.,  1.,  0.],
               [0.,  0.,  1.]])
    """
    pass

def kalman_filter_complex(*args, **kwargs): # real signature unknown
    """ Cython version of the Kalman filter recursions for an ARMA process. """
    pass

def kalman_filter_double(*args, **kwargs): # real signature unknown
    """ Cython version of the Kalman filter recursions for an ARMA process. """
    pass

def kalman_loglike_complex(*args, **kwargs): # real signature unknown
    """ Cython version of the Kalman filter recursions for an ARMA process. """
    pass

def kalman_loglike_double(*args, **kwargs): # real signature unknown
    """ Cython version of the Kalman filter recursions for an ARMA process. """
    pass

def kron(*args, **kwargs): # reliably restored by inspect
    """
    Kronecker product of two arrays.
    
        Computes the Kronecker product, a composite array made of blocks of the
        second array scaled by the first.
    
        Parameters
        ----------
        a, b : array_like
    
        Returns
        -------
        out : ndarray
    
        See Also
        --------
        outer : The outer product
    
        Notes
        -----
        The function assumes that the number of dimensions of `a` and `b`
        are the same, if necessary prepending the smallest with ones.
        If `a.shape = (r0,r1,..,rN)` and `b.shape = (s0,s1,...,sN)`,
        the Kronecker product has shape `(r0*s0, r1*s1, ..., rN*SN)`.
        The elements are products of elements from `a` and `b`, organized
        explicitly by::
    
            kron(a,b)[k0,k1,...,kN] = a[i0,i1,...,iN] * b[j0,j1,...,jN]
    
        where::
    
            kt = it * st + jt,  t = 0,...,N
    
        In the common 2-D case (N=1), the block structure can be visualized::
    
            [[ a[0,0]*b,   a[0,1]*b,  ... , a[0,-1]*b  ],
             [  ...                              ...   ],
             [ a[-1,0]*b,  a[-1,1]*b, ... , a[-1,-1]*b ]]
    
    
        Examples
        --------
        >>> np.kron([1,10,100], [5,6,7])
        array([  5,   6,   7, ..., 500, 600, 700])
        >>> np.kron([5,6,7], [1,10,100])
        array([  5,  50, 500, ...,   7,  70, 700])
    
        >>> np.kron(np.eye(2), np.ones((2,2)))
        array([[1.,  1.,  0.,  0.],
               [1.,  1.,  0.,  0.],
               [0.,  0.,  1.,  1.],
               [0.,  0.,  1.,  1.]])
    
        >>> a = np.arange(100).reshape((2,5,2,5))
        >>> b = np.arange(24).reshape((2,3,4))
        >>> c = np.kron(a,b)
        >>> c.shape
        (2, 10, 6, 20)
        >>> I = (1,3,0,2)
        >>> J = (0,2,1)
        >>> J1 = (0,) + J             # extend to ndim=4
        >>> S1 = (1,) + b.shape
        >>> K = tuple(np.array(I) * np.array(S1) + np.array(J1))
        >>> c[K] == a[I]*b[J]
        True
    """
    pass

def nplog(*args, **kwargs): # real signature unknown
    """
    log(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Natural logarithm, element-wise.
    
    The natural logarithm `log` is the inverse of the exponential function,
    so that `log(exp(x)) = x`. The natural logarithm is logarithm in base
    `e`.
    
    Parameters
    ----------
    x : array_like
        Input value.
    out : ndarray, None, or tuple of ndarray and None, optional
        A location into which the result is stored. If provided, it must have
        a shape that the inputs broadcast to. If not provided or None,
        a freshly-allocated array is returned. A tuple (possible only as a
        keyword argument) must have length equal to the number of outputs.
    where : array_like, optional
        This condition is broadcast over the input. At locations where the
        condition is True, the `out` array will be set to the ufunc result.
        Elsewhere, the `out` array will retain its original value.
        Note that if an uninitialized `out` array is created via the default
        ``out=None``, locations within it where the condition is False will
        remain uninitialized.
    **kwargs
        For other keyword-only arguments, see the
        :ref:`ufunc docs <ufuncs.kwargs>`.
    
    Returns
    -------
    y : ndarray
        The natural logarithm of `x`, element-wise.
        This is a scalar if `x` is a scalar.
    
    See Also
    --------
    log10, log2, log1p, emath.log
    
    Notes
    -----
    Logarithm is a multivalued function: for each `x` there is an infinite
    number of `z` such that `exp(z) = x`. The convention is to return the
    `z` whose imaginary part lies in `[-pi, pi]`.
    
    For real-valued input data types, `log` always returns real output. For
    each value that cannot be expressed as a real number or infinity, it
    yields ``nan`` and sets the `invalid` floating point error flag.
    
    For complex-valued input, `log` is a complex analytical function that
    has a branch cut `[-inf, 0]` and is continuous from above on it. `log`
    handles the floating-point negative zero as an infinitesimal negative
    number, conforming to the C99 standard.
    
    References
    ----------
    .. [1] M. Abramowitz and I.A. Stegun, "Handbook of Mathematical Functions",
           10th printing, 1964, pp. 67. http://www.math.sfu.ca/~cbm/aands/
    .. [2] Wikipedia, "Logarithm". https://en.wikipedia.org/wiki/Logarithm
    
    Examples
    --------
    >>> np.log([1, np.e, np.e**2, 0])
    array([  0.,   1.,   2., -Inf])
    """
    pass

def ones(shape, dtype=None, order=None): # reliably restored by inspect
    """
    Return a new array of given shape and type, filled with ones.
    
        Parameters
        ----------
        shape : int or sequence of ints
            Shape of the new array, e.g., ``(2, 3)`` or ``2``.
        dtype : data-type, optional
            The desired data-type for the array, e.g., `numpy.int8`.  Default is
            `numpy.float64`.
        order : {'C', 'F'}, optional, default: C
            Whether to store multi-dimensional data in row-major
            (C-style) or column-major (Fortran-style) order in
            memory.
    
        Returns
        -------
        out : ndarray
            Array of ones with the given shape, dtype, and order.
    
        See Also
        --------
        ones_like : Return an array of ones with shape and type of input.
        empty : Return a new uninitialized array.
        zeros : Return a new array setting values to zero.
        full : Return a new array of given shape filled with value.
    
    
        Examples
        --------
        >>> np.ones(5)
        array([1., 1., 1., 1., 1.])
    
        >>> np.ones((5,), dtype=int)
        array([1, 1, 1, 1, 1])
    
        >>> np.ones((2, 1))
        array([[1.],
               [1.]])
    
        >>> s = (2,2)
        >>> np.ones(s)
        array([[1.,  1.],
               [1.,  1.]])
    """
    pass

def pinv(*args, **kwargs): # reliably restored by inspect
    """
    Compute the (Moore-Penrose) pseudo-inverse of a matrix.
    
        Calculate the generalized inverse of a matrix using its
        singular-value decomposition (SVD) and including all
        *large* singular values.
    
        .. versionchanged:: 1.14
           Can now operate on stacks of matrices
    
        Parameters
        ----------
        a : (..., M, N) array_like
            Matrix or stack of matrices to be pseudo-inverted.
        rcond : (...) array_like of float
            Cutoff for small singular values.
            Singular values less than or equal to
            ``rcond * largest_singular_value`` are set to zero.
            Broadcasts against the stack of matrices.
        hermitian : bool, optional
            If True, `a` is assumed to be Hermitian (symmetric if real-valued),
            enabling a more efficient method for finding singular values.
            Defaults to False.
    
            .. versionadded:: 1.17.0
    
        Returns
        -------
        B : (..., N, M) ndarray
            The pseudo-inverse of `a`. If `a` is a `matrix` instance, then so
            is `B`.
    
        Raises
        ------
        LinAlgError
            If the SVD computation does not converge.
    
        Notes
        -----
        The pseudo-inverse of a matrix A, denoted :math:`A^+`, is
        defined as: "the matrix that 'solves' [the least-squares problem]
        :math:`Ax = b`," i.e., if :math:`\bar{x}` is said solution, then
        :math:`A^+` is that matrix such that :math:`\bar{x} = A^+b`.
    
        It can be shown that if :math:`Q_1 \Sigma Q_2^T = A` is the singular
        value decomposition of A, then
        :math:`A^+ = Q_2 \Sigma^+ Q_1^T`, where :math:`Q_{1,2}` are
        orthogonal matrices, :math:`\Sigma` is a diagonal matrix consisting
        of A's so-called singular values, (followed, typically, by
        zeros), and then :math:`\Sigma^+` is simply the diagonal matrix
        consisting of the reciprocals of A's singular values
        (again, followed by zeros). [1]_
    
        References
        ----------
        .. [1] G. Strang, *Linear Algebra and Its Applications*, 2nd Ed., Orlando,
               FL, Academic Press, Inc., 1980, pp. 139-142.
    
        Examples
        --------
        The following example checks that ``a * a+ * a == a`` and
        ``a+ * a * a+ == a+``:
    
        >>> a = np.random.randn(9, 6)
        >>> B = np.linalg.pinv(a)
        >>> np.allclose(a, np.dot(a, np.dot(B, a)))
        True
        >>> np.allclose(B, np.dot(B, np.dot(a, B)))
        True
    """
    pass

def sum(*args, **kwargs): # reliably restored by inspect
    """
    Sum of array elements over a given axis.
    
        Parameters
        ----------
        a : array_like
            Elements to sum.
        axis : None or int or tuple of ints, optional
            Axis or axes along which a sum is performed.  The default,
            axis=None, will sum all of the elements of the input array.  If
            axis is negative it counts from the last to the first axis.
    
            .. versionadded:: 1.7.0
    
            If axis is a tuple of ints, a sum is performed on all of the axes
            specified in the tuple instead of a single axis or all the axes as
            before.
        dtype : dtype, optional
            The type of the returned array and of the accumulator in which the
            elements are summed.  The dtype of `a` is used by default unless `a`
            has an integer dtype of less precision than the default platform
            integer.  In that case, if `a` is signed then the platform integer
            is used while if `a` is unsigned then an unsigned integer of the
            same precision as the platform integer is used.
        out : ndarray, optional
            Alternative output array in which to place the result. It must have
            the same shape as the expected output, but the type of the output
            values will be cast if necessary.
        keepdims : bool, optional
            If this is set to True, the axes which are reduced are left
            in the result as dimensions with size one. With this option,
            the result will broadcast correctly against the input array.
    
            If the default value is passed, then `keepdims` will not be
            passed through to the `sum` method of sub-classes of
            `ndarray`, however any non-default value will be.  If the
            sub-class' method does not implement `keepdims` any
            exceptions will be raised.
        initial : scalar, optional
            Starting value for the sum. See `~numpy.ufunc.reduce` for details.
    
            .. versionadded:: 1.15.0
    
        where : array_like of bool, optional
            Elements to include in the sum. See `~numpy.ufunc.reduce` for details.
    
            .. versionadded:: 1.17.0
    
        Returns
        -------
        sum_along_axis : ndarray
            An array with the same shape as `a`, with the specified
            axis removed.   If `a` is a 0-d array, or if `axis` is None, a scalar
            is returned.  If an output array is specified, a reference to
            `out` is returned.
    
        See Also
        --------
        ndarray.sum : Equivalent method.
    
        add.reduce : Equivalent functionality of `add`.
    
        cumsum : Cumulative sum of array elements.
    
        trapz : Integration of array values using the composite trapezoidal rule.
    
        mean, average
    
        Notes
        -----
        Arithmetic is modular when using integer types, and no error is
        raised on overflow.
    
        The sum of an empty array is the neutral element 0:
    
        >>> np.sum([])
        0.0
    
        For floating point numbers the numerical precision of sum (and
        ``np.add.reduce``) is in general limited by directly adding each number
        individually to the result causing rounding errors in every step.
        However, often numpy will use a  numerically better approach (partial
        pairwise summation) leading to improved precision in many use-cases.
        This improved precision is always provided when no ``axis`` is given.
        When ``axis`` is given, it will depend on which axis is summed.
        Technically, to provide the best speed possible, the improved precision
        is only used when the summation is along the fast axis in memory.
        Note that the exact precision may vary depending on other parameters.
        In contrast to NumPy, Python's ``math.fsum`` function uses a slower but
        more precise approach to summation.
        Especially when summing a large number of lower precision floating point
        numbers, such as ``float32``, numerical errors can become significant.
        In such cases it can be advisable to use `dtype="float64"` to use a higher
        precision for the output.
    
        Examples
        --------
        >>> np.sum([0.5, 1.5])
        2.0
        >>> np.sum([0.5, 0.7, 0.2, 1.5], dtype=np.int32)
        1
        >>> np.sum([[0, 1], [0, 5]])
        6
        >>> np.sum([[0, 1], [0, 5]], axis=0)
        array([0, 6])
        >>> np.sum([[0, 1], [0, 5]], axis=1)
        array([1, 5])
        >>> np.sum([[0, 1], [np.nan, 5]], where=[False, True], axis=1)
        array([1., 5.])
    
        If the accumulator is too small, overflow occurs:
    
        >>> np.ones(128, dtype=np.int8).sum(dtype=np.int8)
        -128
    
        You can also start the sum with a value other than zero:
    
        >>> np.sum([10], initial=5)
        15
    """
    pass

def zeros_like(*args, **kwargs): # reliably restored by inspect
    """
    Return an array of zeros with the same shape and type as a given array.
    
        Parameters
        ----------
        a : array_like
            The shape and data-type of `a` define these same attributes of
            the returned array.
        dtype : data-type, optional
            Overrides the data type of the result.
    
            .. versionadded:: 1.6.0
        order : {'C', 'F', 'A', or 'K'}, optional
            Overrides the memory layout of the result. 'C' means C-order,
            'F' means F-order, 'A' means 'F' if `a` is Fortran contiguous,
            'C' otherwise. 'K' means match the layout of `a` as closely
            as possible.
    
            .. versionadded:: 1.6.0
        subok : bool, optional.
            If True, then the newly created array will use the sub-class
            type of 'a', otherwise it will be a base-class array. Defaults
            to True.
        shape : int or sequence of ints, optional.
            Overrides the shape of the result. If order='K' and the number of
            dimensions is unchanged, will try to keep order, otherwise,
            order='C' is implied.
    
            .. versionadded:: 1.17.0
    
        Returns
        -------
        out : ndarray
            Array of zeros with the same shape and type as `a`.
    
        See Also
        --------
        empty_like : Return an empty array with shape and type of input.
        ones_like : Return an array of ones with shape and type of input.
        full_like : Return a new array with shape of input filled with value.
        zeros : Return a new array setting values to zero.
    
        Examples
        --------
        >>> x = np.arange(6)
        >>> x = x.reshape((2, 3))
        >>> x
        array([[0, 1, 2],
               [3, 4, 5]])
        >>> np.zeros_like(x)
        array([[0, 0, 0],
               [0, 0, 0]])
    
        >>> y = np.arange(3, dtype=float)
        >>> y
        array([0., 1., 2.])
        >>> np.zeros_like(y)
        array([0.,  0.,  0.])
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001F38AEAF0F0>'

__spec__ = None # (!) real value is "ModuleSpec(name='statsmodels.tsa.kalmanf.kalman_loglike', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001F38AEAF0F0>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\statsmodels\\\\tsa\\\\kalmanf\\\\kalman_loglike.cp37-win_amd64.pyd')"

__test__ = {}

