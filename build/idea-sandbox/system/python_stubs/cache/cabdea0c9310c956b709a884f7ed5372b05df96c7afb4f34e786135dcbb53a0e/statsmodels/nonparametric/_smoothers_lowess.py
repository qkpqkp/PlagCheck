# encoding: utf-8
# module statsmodels.nonparametric._smoothers_lowess
# from C:\Users\Doly\Anaconda3\lib\site-packages\statsmodels\nonparametric\_smoothers_lowess.cp37-win_amd64.pyd
# by generator 1.147
"""
Univariate lowess function, like in R.

References
----------
Hastie, Tibshirani, Friedman. (2009) The Elements of Statistical Learning: Data
Mining, Inference, and Prediction, Second Edition: Chapter 6.

Cleveland, W.S. (1979) "Robust Locally Weighted Regression and Smoothing
Scatterplots". Journal of the American Statistical Association 74 (368): 829-836.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py
import numpy as __numpy


# functions

def bisquare(*args, **kwargs): # real signature unknown
    """
    The bi-square function (1 - x**2)**2.
    
        Used to weight the residuals in the `robustifying`
        iterations. Called by the calculate_residual_weights function.
    
        Parameters
        ----------
        x: 1-D numpy array
            A vector of absolute regression residuals, in units of
            6 times the median absolute residual.
    
        Returns
        -------
        A 1-D numpy array of residual weights.
    """
    pass

def calculate_residual_weights(*args, **kwargs): # real signature unknown
    """
    Calculate residual weights for the next `robustifying` iteration.
    
        Parameters
        ----------
        y: 1-D numpy array
            The vector of actual input y-values.
        y_fit: 1-D numpy array
            The vector of fitted y-values from the current
            iteration.
    
        Returns
        -------
        resid_weights: 1-D numpy array
            The vector of residual weights, to be used in the
            next iteration of regressions.
    """
    pass

def lowess(endog, exog, frac=2.0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    lowess(endog, exog, frac=2.0/3.0, it=3, delta=0.0)
        LOWESS (Locally Weighted Scatterplot Smoothing)
    
        A lowess function that outs smoothed estimates of endog
        at the given exog values from points (exog, endog)
    
        Parameters
        ----------
        endog: 1-D numpy array
            The y-values of the observed points
        exog: 1-D numpy array
            The x-values of the observed points. exog has to be increasing.
        frac: float
            Between 0 and 1. The fraction of the data used
            when estimating each y-value.
        it: int
            The number of residual-based reweightings
            to perform.
        delta: float
            Distance within which to use linear-interpolation
            instead of weighted regression.
    
        Returns
        -------
        out: numpy array
            A numpy array with two columns. The first column
            is the sorted x values and the second column the
            associated estimated y-values.
    
        Notes
        -----
        This lowess function implements the algorithm given in the
        reference below using local linear estimates.
    
        Suppose the input data has N points. The algorithm works by
        estimating the `smooth` y_i by taking the frac*N closest points
        to (x_i,y_i) based on their x values and estimating y_i
        using a weighted linear regression. The weight for (x_j,y_j)
        is tricube function applied to |x_i-x_j|.
    
        If it > 1, then further weighted local linear regressions
        are performed, where the weights are the same as above
        times the _lowess_bisquare function of the residuals. Each iteration
        takes approximately the same amount of time as the original fit,
        so these iterations are expensive. They are most useful when
        the noise has extremely heavy tails, such as Cauchy noise.
        Noise with less heavy-tails, such as t-distributions with df>2,
        are less problematic. The weights downgrade the influence of
        points with large residuals. In the extreme case, points whose
        residuals are larger than 6 times the median absolute residual
        are given weight 0.
    
        delta can be used to save computations. For each x_i, regressions
        are skipped for points closer than delta. The next regression is
        fit for the farthest point within delta of x_i and all points in
        between are estimated by linearly interpolating between the two
        regression fits.
    
        Judicious choice of delta can cut computation time considerably
        for large data (N > 5000). A good choice is delta = 0.01 *
        range(exog).
    
        Some experimentation is likely required to find a good
        choice of frac and iter for a particular dataset.
    
        References
        ----------
        Cleveland, W.S. (1979) "Robust Locally Weighted Regression
        and Smoothing Scatterplots". Journal of the American Statistical
        Association 74 (368): 829-836.
    
        Examples
        --------
        The below allows a comparison between how different the fits from
        lowess for different values of frac can be.
    
        >>> import numpy as np
        >>> import statsmodels.api as sm
        >>> lowess = sm.nonparametric.lowess
        >>> x = np.random.uniform(low = -2*np.pi, high = 2*np.pi, size=500)
        >>> y = np.sin(x) + np.random.normal(size=len(x))
        >>> z = lowess(y, x)
        >>> w = lowess(y, x, frac=1./3)
    
        This gives a similar comparison for when it is 0 vs not.
    
        >>> import numpy as np
        >>> import scipy.stats as stats
        >>> import statsmodels.api as sm
        >>> lowess = sm.nonparametric.lowess
        >>> x = np.random.uniform(low = -2*np.pi, high = 2*np.pi, size=500)
        >>> y = np.sin(x) + stats.cauchy.rvs(size=len(x))
        >>> z = lowess(y, x, frac= 1./3, it=0)
        >>> w = lowess(y, x, frac=1./3)
    """
    pass

def update_indices(*args, **kwargs): # real signature unknown
    """
    Update the counters of the local regression.
    
        Parameters
        ----------
        x: 1-D numpy array
            The vector of input x-values.
        y_fit: 1-D numpy array
            The vector of fitted y-values
        delta: float
            Indicates the range of x values within which linear
            interpolation should be used to estimate y_fit instead
            of weighted regression.
        i: indexing integer
            The index of the current point being fit.
        n: indexing integer
            The length of the input vectors, x and y.
        last_fit_i: indexing integer
            The last point at which y_fit was calculated.
    
        Returns
        -------
        i: indexing integer
            The next point at which to run a weighted regression.
        last_fit_i: indexing integer
            The updated last point at which y_fit was calculated
    
        Notes
        -----
        The relationship between the outputs is s.t. x[i+1] >
        x[last_fit_i] + delta.
    """
    pass

def update_neighborhood(*args, **kwargs): # real signature unknown
    """
    Find the indices bounding the k-nearest-neighbors of the current point.
    
        Parameters
        ----------
        x: 1-D numpy array
            The input x-values
        i: indexing integer
            The index of the point currently being fit.
        n: indexing integer
            The length of the input vectors, x and y.
        left_end: indexing integer
            The index of the left-most point in the neighborhood
            of x[i-1] (the previously-fit point).
        right_end: indexing integer
            The index of the right-most point in the neighborhood
            of x[i-1]. Non-inclusive, s.t. the neighborhood is
            x[left_end] <= x < x[right_end].
        radius: float
            The radius of the current neighborhood. The larger of
            distances between x[i] and its left-most or right-most
            neighbor.
    
        Returns
        -------
        left_end: indexing integer
            The index of the left-most point in the neighborhood
                  of x[i] (the current point).
        right_end: indexing integer
            The index of the right-most point in the neighborhood
                   of x[i]. Non-inclusive, s.t. the neighborhood is
                   x[left_end] <= x < x[right_end].
        radius: float
            The radius of the current neighborhood. The larger of
            distances between x[i] and its left-most or right-most
            neighbor.
    """
    pass

# classes

class DTYPE(__numpy.floating, float):
    """
    Double-precision floating-point number type, compatible with Python `float`
        and C ``double``.
        Character code: ``'d'``.
        Canonical name: ``np.double``.
        Alias: ``np.float_``.
        Alias *on this platform*: ``np.float64``: 64-bit precision floating-point number type: sign bit, 11 bits exponent, 52 bits mantissa.
    """
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        double.as_integer_ratio() -> (int, int)
        
                Return a pair of integers, whose ratio is exactly equal to the original
                floating point number, and with a positive denominator.
                Raise OverflowError on infinities and a ValueError on NaNs.
        
                >>> np.double(10.0).as_integer_ratio()
                (10, 1)
                >>> np.double(0.0).as_integer_ratio()
                (0, 1)
                >>> np.double(-.25).as_integer_ratio()
                (-1, 4)
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
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

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001ECBDA0BD68>'

__spec__ = None # (!) real value is "ModuleSpec(name='statsmodels.nonparametric._smoothers_lowess', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001ECBDA0BD68>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\statsmodels\\\\nonparametric\\\\_smoothers_lowess.cp37-win_amd64.pyd')"

__test__ = {
    'lowess (line 28)': 'lowess(endog, exog, frac=2.0/3.0, it=3, delta=0.0)\n    LOWESS (Locally Weighted Scatterplot Smoothing)\n\n    A lowess function that outs smoothed estimates of endog\n    at the given exog values from points (exog, endog)\n\n    Parameters\n    ----------\n    endog: 1-D numpy array\n        The y-values of the observed points\n    exog: 1-D numpy array\n        The x-values of the observed points. exog has to be increasing.\n    frac: float\n        Between 0 and 1. The fraction of the data used\n        when estimating each y-value.\n    it: int\n        The number of residual-based reweightings\n        to perform.\n    delta: float\n        Distance within which to use linear-interpolation\n        instead of weighted regression.\n\n    Returns\n    -------\n    out: numpy array\n        A numpy array with two columns. The first column\n        is the sorted x values and the second column the\n        associated estimated y-values.\n\n    Notes\n    -----\n    This lowess function implements the algorithm given in the\n    reference below using local linear estimates.\n\n    Suppose the input data has N points. The algorithm works by\n    estimating the `smooth` y_i by taking the frac*N closest points\n    to (x_i,y_i) based on their x values and estimating y_i\n    using a weighted linear regression. The weight for (x_j,y_j)\n    is tricube function applied to |x_i-x_j|.\n\n    If it > 1, then further weighted local linear regressions\n    are performed, where the weights are the same as above\n    times the _lowess_bisquare function of the residuals. Each iteration\n    takes approximately the same amount of time as the original fit,\n    so these iterations are expensive. They are most useful when\n    the noise has extremely heavy tails, such as Cauchy noise.\n    Noise with less heavy-tails, such as t-distributions with df>2,\n    are less problematic. The weights downgrade the influence of\n    points with large residuals. In the extreme case, points whose\n    residuals are larger than 6 times the median absolute residual\n    are given weight 0.\n\n    delta can be used to save computations. For each x_i, regressions\n    are skipped for points closer than delta. The next regression is\n    fit for the farthest point within delta of x_i and all points in\n    between are estimated by linearly interpolating between the two\n    regression fits.\n\n    Judicious choice of delta can cut computation time considerably\n    for large data (N > 5000). A good choice is delta = 0.01 *\n    range(exog).\n\n    Some experimentation is likely required to find a good\n    choice of frac and iter for a particular dataset.\n\n    References\n    ----------\n    Cleveland, W.S. (1979) "Robust Locally Weighted Regression\n    and Smoothing Scatterplots". Journal of the American Statistical\n    Association 74 (368): 829-836.\n\n    Examples\n    --------\n    The below allows a comparison between how different the fits from\n    lowess for different values of frac can be.\n\n    >>> import numpy as np\n    >>> import statsmodels.api as sm\n    >>> lowess = sm.nonparametric.lowess\n    >>> x = np.random.uniform(low = -2*np.pi, high = 2*np.pi, size=500)\n    >>> y = np.sin(x) + np.random.normal(size=len(x))\n    >>> z = lowess(y, x)\n    >>> w = lowess(y, x, frac=1./3)\n\n    This gives a similar comparison for when it is 0 vs not.\n\n    >>> import numpy as np\n    >>> import scipy.stats as stats\n    >>> import statsmodels.api as sm\n    >>> lowess = sm.nonparametric.lowess\n    >>> x = np.random.uniform(low = -2*np.pi, high = 2*np.pi, size=500)\n    >>> y = np.sin(x) + stats.cauchy.rvs(size=len(x))\n    >>> z = lowess(y, x, frac= 1./3, it=0)\n    >>> w = lowess(y, x, frac=1./3)\n\n    ',
}

