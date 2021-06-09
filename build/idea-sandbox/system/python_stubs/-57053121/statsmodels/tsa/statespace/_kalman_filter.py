# encoding: utf-8
# module statsmodels.tsa.statespace._kalman_filter
# from C:\Users\Doly\Anaconda3\lib\site-packages\statsmodels\tsa\statespace\_kalman_filter.cp37-win_amd64.pyd
# by generator 1.147
"""
Kalman Filter

Author: Chad Fulton  
License: Simplified-BSD
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py
import warnings as warnings # C:\Users\Doly\Anaconda3\lib\warnings.py

# functions

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class cKalmanFilter(object):
    """
    cKalmanFilter(model, filter_method=FILTER_CONVENTIONAL, inversion_method=INVERT_UNIVARIATE | SOLVE_CHOLESKY, stability_method=STABILITY_FORCE_SYMMETRY, filter_timing=TIMING_INIT_PREDICTED, tolerance=1e-19)
    
        A representation of the Kalman filter recursions.
    
        While the filter is mathematically represented as a recursion, it is here
        translated into Python as a stateful iterator.
    
        Because there are actually several types of Kalman filter depending on the
        state space model of interest, this class only handles the *iteration*
        aspect of filtering, and delegates the actual operations to four general
        workhorse routines, which can be implemented separately for each type of
        Kalman filter.
    
        In order to maintain a consistent interface, and because these four general
        routines may be quite different across filter types, their argument is only
        the stateful ?KalmanFilter object. Furthermore, in order to allow the
        different types of filter to substitute alternate matrices, this class
        defines a set of pointers to the various state space arrays and the
        filtering output arrays.
    
        For example, handling missing observations requires not only substituting
        `obs`, `design`, and `obs_cov` matrices, but the new matrices actually have
        different dimensions than the originals. This can be flexibly accomodated
        simply by replacing e.g. the `obs` pointer to the substituted `obs` array
        and replacing `k_endog` for that iteration. Then in the next iteration, when
        the `obs` vector may be missing different elements (or none at all), it can
        again be redefined.
    
        Each iteration of the filter (see `__next__`) proceeds in a number of
        steps.
    
        `initialize_object_pointers` initializes pointers to current-iteration
        objects (i.e. the state space arrays and filter output arrays).  
    
        `initialize_function_pointers` initializes pointers to the appropriate
        Kalman filtering routines (i.e. `forecast_conventional` or
        `forecast_exact_initial`, etc.).  
    
        `select_arrays` converts the base arrays into "selected" arrays using
        selection matrices. In particular, it handles the state covariance matrix
        and redefined matrices based on missing values.  
    
        `post_convergence` handles copying arrays from time $t-1$ to time $t$ when
        the Kalman filter has converged and they don't need to be re-calculated.  
    
        `forecasting` calls the Kalman filter `forcasting_<filter type>` routine
    
        `inversion` calls the appropriate function to invert the forecast error
        covariance matrix.  
    
        `updating` calls the Kalman filter `updating_<filter type>` routine
    
        `loglikelihood` calls the Kalman filter `loglikelihood_<filter type>` routine
    
        `prediction` calls the Kalman filter `prediction_<filter type>` routine
    
        `numerical_stability` performs end-of-iteration tasks to improve the numerical
        stability of the filter 
    
        `check_convergence` checks for convergence of the filter to steady-state.
    """
    def seek(self, t, reset=True): # real signature unknown; restored from __doc__
        """
        seek(self, t, reset = True)
        
                Change the time-state of the filter
        
                Is usually called to reset the filter to the beginning.
        """
        pass

    def set_filter_method(self, filter_method, force_reset=True): # real signature unknown; restored from __doc__
        """
        set_filter_method(self, filter_method, force_reset=True)
        
                Change the filter method.
        """
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Iterate the filter across the entire set of observations. """
        pass

    def __init__(self, model, filter_method=None, inversion_method=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Perform an iteration of the Kalman filter """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    conserve_memory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged_determinant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged_filtered_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged_forecast_error_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged_kalman_gain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged_M = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged_predicted_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    determinant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    filtered_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    filtered_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    filter_method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    filter_timing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast_error = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast_error_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast_error_diffuse_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast_error_fac = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast_error_ipiv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast_error_work = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    inversion_method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    kalman_gain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_endog = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_endog2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_endogstates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_posdef = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_posdef2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_states = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_states2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_statesposdef = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ldwork = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    loglikelihood = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    loglikelihood_burn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    M = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    model = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    M_inf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nobs_diffuse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nobs_kendog_diffuse_nonsingular = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nobs_kendog_univariate_singular = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    period_converged = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    predicted_diffuse_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    predicted_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    predicted_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stability_method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    standardized_forecast_error = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    t = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    time_invariant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp00 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmpK0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmpK1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmpL0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmpL1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmpM_inf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tolerance_diffuse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000273BBF03990>'


class dKalmanFilter(object):
    """
    dKalmanFilter(model, filter_method=FILTER_CONVENTIONAL, inversion_method=INVERT_UNIVARIATE | SOLVE_CHOLESKY, stability_method=STABILITY_FORCE_SYMMETRY, filter_timing=TIMING_INIT_PREDICTED, tolerance=1e-19)
    
        A representation of the Kalman filter recursions.
    
        While the filter is mathematically represented as a recursion, it is here
        translated into Python as a stateful iterator.
    
        Because there are actually several types of Kalman filter depending on the
        state space model of interest, this class only handles the *iteration*
        aspect of filtering, and delegates the actual operations to four general
        workhorse routines, which can be implemented separately for each type of
        Kalman filter.
    
        In order to maintain a consistent interface, and because these four general
        routines may be quite different across filter types, their argument is only
        the stateful ?KalmanFilter object. Furthermore, in order to allow the
        different types of filter to substitute alternate matrices, this class
        defines a set of pointers to the various state space arrays and the
        filtering output arrays.
    
        For example, handling missing observations requires not only substituting
        `obs`, `design`, and `obs_cov` matrices, but the new matrices actually have
        different dimensions than the originals. This can be flexibly accomodated
        simply by replacing e.g. the `obs` pointer to the substituted `obs` array
        and replacing `k_endog` for that iteration. Then in the next iteration, when
        the `obs` vector may be missing different elements (or none at all), it can
        again be redefined.
    
        Each iteration of the filter (see `__next__`) proceeds in a number of
        steps.
    
        `initialize_object_pointers` initializes pointers to current-iteration
        objects (i.e. the state space arrays and filter output arrays).  
    
        `initialize_function_pointers` initializes pointers to the appropriate
        Kalman filtering routines (i.e. `forecast_conventional` or
        `forecast_exact_initial`, etc.).  
    
        `select_arrays` converts the base arrays into "selected" arrays using
        selection matrices. In particular, it handles the state covariance matrix
        and redefined matrices based on missing values.  
    
        `post_convergence` handles copying arrays from time $t-1$ to time $t$ when
        the Kalman filter has converged and they don't need to be re-calculated.  
    
        `forecasting` calls the Kalman filter `forcasting_<filter type>` routine
    
        `inversion` calls the appropriate function to invert the forecast error
        covariance matrix.  
    
        `updating` calls the Kalman filter `updating_<filter type>` routine
    
        `loglikelihood` calls the Kalman filter `loglikelihood_<filter type>` routine
    
        `prediction` calls the Kalman filter `prediction_<filter type>` routine
    
        `numerical_stability` performs end-of-iteration tasks to improve the numerical
        stability of the filter 
    
        `check_convergence` checks for convergence of the filter to steady-state.
    """
    def seek(self, t, reset=True): # real signature unknown; restored from __doc__
        """
        seek(self, t, reset = True)
        
                Change the time-state of the filter
        
                Is usually called to reset the filter to the beginning.
        """
        pass

    def set_filter_method(self, filter_method, force_reset=True): # real signature unknown; restored from __doc__
        """
        set_filter_method(self, filter_method, force_reset=True)
        
                Change the filter method.
        """
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Iterate the filter across the entire set of observations. """
        pass

    def __init__(self, model, filter_method=None, inversion_method=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Perform an iteration of the Kalman filter """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    conserve_memory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged_determinant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged_filtered_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged_forecast_error_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged_kalman_gain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged_M = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged_predicted_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    determinant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    filtered_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    filtered_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    filter_method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    filter_timing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast_error = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast_error_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast_error_diffuse_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast_error_fac = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast_error_ipiv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast_error_work = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    inversion_method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    kalman_gain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_endog = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_endog2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_endogstates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_posdef = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_posdef2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_states = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_states2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_statesposdef = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ldwork = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    loglikelihood = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    loglikelihood_burn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    M = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    model = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    M_inf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nobs_diffuse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nobs_kendog_diffuse_nonsingular = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nobs_kendog_univariate_singular = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    period_converged = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    predicted_diffuse_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    predicted_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    predicted_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stability_method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    standardized_forecast_error = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    t = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    time_invariant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp00 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmpK0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmpK1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmpL0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmpL1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmpM_inf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tolerance_diffuse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000273BBF03960>'


class sKalmanFilter(object):
    """
    sKalmanFilter(model, filter_method=FILTER_CONVENTIONAL, inversion_method=INVERT_UNIVARIATE | SOLVE_CHOLESKY, stability_method=STABILITY_FORCE_SYMMETRY, filter_timing=TIMING_INIT_PREDICTED, tolerance=1e-19)
    
        A representation of the Kalman filter recursions.
    
        While the filter is mathematically represented as a recursion, it is here
        translated into Python as a stateful iterator.
    
        Because there are actually several types of Kalman filter depending on the
        state space model of interest, this class only handles the *iteration*
        aspect of filtering, and delegates the actual operations to four general
        workhorse routines, which can be implemented separately for each type of
        Kalman filter.
    
        In order to maintain a consistent interface, and because these four general
        routines may be quite different across filter types, their argument is only
        the stateful ?KalmanFilter object. Furthermore, in order to allow the
        different types of filter to substitute alternate matrices, this class
        defines a set of pointers to the various state space arrays and the
        filtering output arrays.
    
        For example, handling missing observations requires not only substituting
        `obs`, `design`, and `obs_cov` matrices, but the new matrices actually have
        different dimensions than the originals. This can be flexibly accomodated
        simply by replacing e.g. the `obs` pointer to the substituted `obs` array
        and replacing `k_endog` for that iteration. Then in the next iteration, when
        the `obs` vector may be missing different elements (or none at all), it can
        again be redefined.
    
        Each iteration of the filter (see `__next__`) proceeds in a number of
        steps.
    
        `initialize_object_pointers` initializes pointers to current-iteration
        objects (i.e. the state space arrays and filter output arrays).  
    
        `initialize_function_pointers` initializes pointers to the appropriate
        Kalman filtering routines (i.e. `forecast_conventional` or
        `forecast_exact_initial`, etc.).  
    
        `select_arrays` converts the base arrays into "selected" arrays using
        selection matrices. In particular, it handles the state covariance matrix
        and redefined matrices based on missing values.  
    
        `post_convergence` handles copying arrays from time $t-1$ to time $t$ when
        the Kalman filter has converged and they don't need to be re-calculated.  
    
        `forecasting` calls the Kalman filter `forcasting_<filter type>` routine
    
        `inversion` calls the appropriate function to invert the forecast error
        covariance matrix.  
    
        `updating` calls the Kalman filter `updating_<filter type>` routine
    
        `loglikelihood` calls the Kalman filter `loglikelihood_<filter type>` routine
    
        `prediction` calls the Kalman filter `prediction_<filter type>` routine
    
        `numerical_stability` performs end-of-iteration tasks to improve the numerical
        stability of the filter 
    
        `check_convergence` checks for convergence of the filter to steady-state.
    """
    def seek(self, t, reset=True): # real signature unknown; restored from __doc__
        """
        seek(self, t, reset = True)
        
                Change the time-state of the filter
        
                Is usually called to reset the filter to the beginning.
        """
        pass

    def set_filter_method(self, filter_method, force_reset=True): # real signature unknown; restored from __doc__
        """
        set_filter_method(self, filter_method, force_reset=True)
        
                Change the filter method.
        """
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Iterate the filter across the entire set of observations. """
        pass

    def __init__(self, model, filter_method=None, inversion_method=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Perform an iteration of the Kalman filter """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    conserve_memory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged_determinant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged_filtered_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged_forecast_error_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged_kalman_gain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged_M = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged_predicted_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    determinant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    filtered_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    filtered_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    filter_method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    filter_timing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast_error = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast_error_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast_error_diffuse_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast_error_fac = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast_error_ipiv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast_error_work = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    inversion_method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    kalman_gain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_endog = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_endog2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_endogstates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_posdef = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_posdef2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_states = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_states2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_statesposdef = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ldwork = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    loglikelihood = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    loglikelihood_burn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    M = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    model = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    M_inf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nobs_diffuse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nobs_kendog_diffuse_nonsingular = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nobs_kendog_univariate_singular = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    period_converged = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    predicted_diffuse_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    predicted_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    predicted_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stability_method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    standardized_forecast_error = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    t = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    time_invariant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp00 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmpK0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmpK1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmpL0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmpL1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tolerance_diffuse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000273BBF03930>'


class zKalmanFilter(object):
    """
    zKalmanFilter(model, filter_method=FILTER_CONVENTIONAL, inversion_method=INVERT_UNIVARIATE | SOLVE_CHOLESKY, stability_method=STABILITY_FORCE_SYMMETRY, filter_timing=TIMING_INIT_PREDICTED, tolerance=1e-19)
    
        A representation of the Kalman filter recursions.
    
        While the filter is mathematically represented as a recursion, it is here
        translated into Python as a stateful iterator.
    
        Because there are actually several types of Kalman filter depending on the
        state space model of interest, this class only handles the *iteration*
        aspect of filtering, and delegates the actual operations to four general
        workhorse routines, which can be implemented separately for each type of
        Kalman filter.
    
        In order to maintain a consistent interface, and because these four general
        routines may be quite different across filter types, their argument is only
        the stateful ?KalmanFilter object. Furthermore, in order to allow the
        different types of filter to substitute alternate matrices, this class
        defines a set of pointers to the various state space arrays and the
        filtering output arrays.
    
        For example, handling missing observations requires not only substituting
        `obs`, `design`, and `obs_cov` matrices, but the new matrices actually have
        different dimensions than the originals. This can be flexibly accomodated
        simply by replacing e.g. the `obs` pointer to the substituted `obs` array
        and replacing `k_endog` for that iteration. Then in the next iteration, when
        the `obs` vector may be missing different elements (or none at all), it can
        again be redefined.
    
        Each iteration of the filter (see `__next__`) proceeds in a number of
        steps.
    
        `initialize_object_pointers` initializes pointers to current-iteration
        objects (i.e. the state space arrays and filter output arrays).  
    
        `initialize_function_pointers` initializes pointers to the appropriate
        Kalman filtering routines (i.e. `forecast_conventional` or
        `forecast_exact_initial`, etc.).  
    
        `select_arrays` converts the base arrays into "selected" arrays using
        selection matrices. In particular, it handles the state covariance matrix
        and redefined matrices based on missing values.  
    
        `post_convergence` handles copying arrays from time $t-1$ to time $t$ when
        the Kalman filter has converged and they don't need to be re-calculated.  
    
        `forecasting` calls the Kalman filter `forcasting_<filter type>` routine
    
        `inversion` calls the appropriate function to invert the forecast error
        covariance matrix.  
    
        `updating` calls the Kalman filter `updating_<filter type>` routine
    
        `loglikelihood` calls the Kalman filter `loglikelihood_<filter type>` routine
    
        `prediction` calls the Kalman filter `prediction_<filter type>` routine
    
        `numerical_stability` performs end-of-iteration tasks to improve the numerical
        stability of the filter 
    
        `check_convergence` checks for convergence of the filter to steady-state.
    """
    def seek(self, t, reset=True): # real signature unknown; restored from __doc__
        """
        seek(self, t, reset = True)
        
                Change the time-state of the filter
        
                Is usually called to reset the filter to the beginning.
        """
        pass

    def set_filter_method(self, filter_method, force_reset=True): # real signature unknown; restored from __doc__
        """
        set_filter_method(self, filter_method, force_reset=True)
        
                Change the filter method.
        """
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Iterate the filter across the entire set of observations. """
        pass

    def __init__(self, model, filter_method=None, inversion_method=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Perform an iteration of the Kalman filter """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    conserve_memory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged_determinant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged_filtered_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged_forecast_error_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged_kalman_gain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged_M = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged_predicted_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    determinant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    filtered_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    filtered_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    filter_method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    filter_timing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast_error = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast_error_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast_error_diffuse_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast_error_fac = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast_error_ipiv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast_error_work = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    inversion_method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    kalman_gain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_endog = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_endog2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_endogstates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_posdef = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_posdef2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_states = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_states2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_statesposdef = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ldwork = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    loglikelihood = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    loglikelihood_burn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    M = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    model = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    M_inf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nobs_diffuse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nobs_kendog_diffuse_nonsingular = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nobs_kendog_univariate_singular = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    period_converged = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    predicted_diffuse_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    predicted_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    predicted_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stability_method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    standardized_forecast_error = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    t = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    time_invariant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp00 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmpK0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmpK1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmpL0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmpL1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmpM_inf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tolerance_diffuse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000273BBF039C0>'


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000273BBF42EB8>'

__pyx_capi__ = {
    'FILTER_AUGMENTED': None, # (!) real value is '<capsule object "int" at 0x00000273BBE30A80>'
    'FILTER_COLLAPSED': None, # (!) real value is '<capsule object "int" at 0x00000273BBE30D20>'
    'FILTER_CONCENTRATED': None, # (!) real value is '<capsule object "int" at 0x00000273BBE8D240>'
    'FILTER_CONVENTIONAL': None, # (!) real value is '<capsule object "int" at 0x00000273BBE308A0>'
    'FILTER_EXACT_INITIAL': None, # (!) real value is '<capsule object "int" at 0x00000273BBE30A50>'
    'FILTER_EXTENDED': None, # (!) real value is '<capsule object "int" at 0x00000273BBE8D210>'
    'FILTER_SQUARE_ROOT': None, # (!) real value is '<capsule object "int" at 0x00000273BBE30AB0>'
    'FILTER_UNIVARIATE': None, # (!) real value is '<capsule object "int" at 0x00000273BBE30CF0>'
    'FILTER_UNSCENTED': None, # (!) real value is '<capsule object "int" at 0x00000273BBE8D150>'
    'INVERT_CHOLESKY': None, # (!) real value is '<capsule object "int" at 0x00000273BBF036C0>'
    'INVERT_LU': None, # (!) real value is '<capsule object "int" at 0x00000273BBF03660>'
    'INVERT_UNIVARIATE': None, # (!) real value is '<capsule object "int" at 0x00000273BBF035D0>'
    'MEMORY_CONSERVE': None, # (!) real value is '<capsule object "int" at 0x00000273BBF038A0>'
    'MEMORY_NO_FILTERED': None, # (!) real value is '<capsule object "int" at 0x00000273BBF037B0>'
    'MEMORY_NO_FORECAST': None, # (!) real value is '<capsule object "int" at 0x00000273BBF03750>'
    'MEMORY_NO_GAIN': None, # (!) real value is '<capsule object "int" at 0x00000273BBF03810>'
    'MEMORY_NO_LIKELIHOOD': None, # (!) real value is '<capsule object "int" at 0x00000273BBF037E0>'
    'MEMORY_NO_PREDICTED': None, # (!) real value is '<capsule object "int" at 0x00000273BBF03780>'
    'MEMORY_NO_SMOOTHING': None, # (!) real value is '<capsule object "int" at 0x00000273BBF03840>'
    'MEMORY_NO_STD_FORECAST': None, # (!) real value is '<capsule object "int" at 0x00000273BBF03870>'
    'MEMORY_STORE_ALL': None, # (!) real value is '<capsule object "int" at 0x00000273BBF03720>'
    'SOLVE_CHOLESKY': None, # (!) real value is '<capsule object "int" at 0x00000273BBF03690>'
    'SOLVE_LU': None, # (!) real value is '<capsule object "int" at 0x00000273BBF03630>'
    'STABILITY_FORCE_SYMMETRY': None, # (!) real value is '<capsule object "int" at 0x00000273BBF036F0>'
    'TIMING_INIT_FILTERED': None, # (!) real value is '<capsule object "int" at 0x00000273BBF038D0>'
    'TIMING_INIT_PREDICTED': None, # (!) real value is '<capsule object "int" at 0x00000273BBF03900>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='statsmodels.tsa.statespace._kalman_filter', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000273BBF42EB8>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\statsmodels\\\\tsa\\\\statespace\\\\_kalman_filter.cp37-win_amd64.pyd')"

__test__ = {}

