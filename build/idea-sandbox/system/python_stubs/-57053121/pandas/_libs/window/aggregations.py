# encoding: utf-8
# module pandas._libs.window.aggregations
# from C:\Users\Doly\Anaconda3\lib\site-packages\pandas\_libs\window\aggregations.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py
from pandas._libs.algos import is_monotonic


# functions

def ewma(*args, **kwargs): # real signature unknown
    """
    Compute exponentially-weighted moving average using center-of-mass.
    
        Parameters
        ----------
        vals : ndarray (float64 type)
        com : float64
        adjust: int
        ignore_na: bool
        minp: int
    
        Returns
        -------
        ndarray
    """
    pass

def ewmcov(*args, **kwargs): # real signature unknown
    """
    Compute exponentially-weighted moving variance using center-of-mass.
    
        Parameters
        ----------
        input_x : ndarray (float64 type)
        input_y : ndarray (float64 type)
        com : float64
        adjust: int
        ignore_na: bool
        minp: int
        bias: int
    
        Returns
        -------
        ndarray
    """
    pass

def roll_count(*args, **kwargs): # real signature unknown
    pass

def roll_generic_fixed(*args, **kwargs): # real signature unknown
    pass

def roll_generic_variable(*args, **kwargs): # real signature unknown
    pass

def roll_kurt_fixed(*args, **kwargs): # real signature unknown
    pass

def roll_kurt_variable(*args, **kwargs): # real signature unknown
    pass

def roll_max_fixed(*args, **kwargs): # real signature unknown
    """
    Moving max of 1d array of any numeric type along axis=0 ignoring NaNs.
    
        Parameters
        ----------
        values : np.ndarray[np.float64]
        window : int, size of rolling window
        minp : if number of observations in window
              is below this, output a NaN
        index : ndarray, optional
           index for window computation
        closed : 'right', 'left', 'both', 'neither'
                make the interval closed on the right, left,
                both or neither endpoints
    """
    pass

def roll_max_variable(*args, **kwargs): # real signature unknown
    """
    Moving max of 1d array of any numeric type along axis=0 ignoring NaNs.
    
        Parameters
        ----------
        values : np.ndarray[np.float64]
        window : int, size of rolling window
        minp : if number of observations in window
              is below this, output a NaN
        index : ndarray, optional
           index for window computation
        closed : 'right', 'left', 'both', 'neither'
                make the interval closed on the right, left,
                both or neither endpoints
    """
    pass

def roll_mean_fixed(*args, **kwargs): # real signature unknown
    pass

def roll_mean_variable(*args, **kwargs): # real signature unknown
    pass

def roll_median_c(*args, **kwargs): # real signature unknown
    pass

def roll_min_fixed(*args, **kwargs): # real signature unknown
    """
    Moving min of 1d array of any numeric type along axis=0 ignoring NaNs.
    
        Parameters
        ----------
        values : np.ndarray[np.float64]
        window : int, size of rolling window
        minp : if number of observations in window
              is below this, output a NaN
        index : ndarray, optional
           index for window computation
    """
    pass

def roll_min_variable(*args, **kwargs): # real signature unknown
    """
    Moving min of 1d array of any numeric type along axis=0 ignoring NaNs.
    
        Parameters
        ----------
        values : np.ndarray[np.float64]
        window : int, size of rolling window
        minp : if number of observations in window
              is below this, output a NaN
        index : ndarray, optional
           index for window computation
    """
    pass

def roll_quantile(*args, **kwargs): # real signature unknown
    """ O(N log(window)) implementation using skip list """
    pass

def roll_skew_fixed(*args, **kwargs): # real signature unknown
    pass

def roll_skew_variable(*args, **kwargs): # real signature unknown
    pass

def roll_sum_fixed(*args, **kwargs): # real signature unknown
    pass

def roll_sum_variable(*args, **kwargs): # real signature unknown
    pass

def roll_var_fixed(*args, **kwargs): # real signature unknown
    """ Numerically stable implementation using Welford's method. """
    pass

def roll_var_variable(*args, **kwargs): # real signature unknown
    """ Numerically stable implementation using Welford's method. """
    pass

def roll_weighted_mean(*args, **kwargs): # real signature unknown
    pass

def roll_weighted_sum(*args, **kwargs): # real signature unknown
    pass

def roll_weighted_var(*args, **kwargs): # real signature unknown
    """
    Calculates weighted rolling variance using West's online algorithm.
    
        Paper: https://dl.acm.org/citation.cfm?id=359153
    
        Parameters
        ----------
        values: float64_t[:]
            values to roll window over
        weights: float64_t[:]
            array of weights whose length is window size
        minp: int64_t
            minimum number of observations to calculate
            variance of a window
        ddof: unsigned int
             the divisor used in variance calculations
             is the window size - ddof
    
        Returns
        -------
        output: float64_t[:]
            weighted variances of windows
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

interpolation_types = {
    'higher': 2,
    'linear': 0,
    'lower': 1,
    'midpoint': 4,
    'nearest': 3,
}

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000015D3C544668>'

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.window.aggregations', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000015D3C544668>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\pandas\\\\_libs\\\\window\\\\aggregations.cp37-win_amd64.pyd')"

__test__ = {}

