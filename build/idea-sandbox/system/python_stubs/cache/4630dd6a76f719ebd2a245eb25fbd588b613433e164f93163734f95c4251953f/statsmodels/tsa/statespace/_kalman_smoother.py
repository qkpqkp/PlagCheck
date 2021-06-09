# encoding: utf-8
# module statsmodels.tsa.statespace._kalman_smoother
# from C:\Users\Doly\Anaconda3\lib\site-packages\statsmodels\tsa\statespace\_kalman_smoother.cp37-win_amd64.pyd
# by generator 1.147
"""
State Space Models

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

class cKalmanSmoother(object):
    """
    cKalmanSmoother(model, kfilter, smoother_output=SMOOTHING_ALL)
    
        A representation of the Kalman smoother recursions; it performs a single
        backwards pass through the data (after the forwards pass via the Kalman
        filter has already been completed). In all cases, it calculates:
    
        - `scaled_smoothed_estimator`
        - `smoothing_error`
    
        it can optionally peform three types of smoothing:
    
        - State smoothing provides `smoothed_state` and `smoothed_state_cov`
        - Disturbance smoothing provides `smoothed_measurement_disturbance` and
          `smoothed_state_disturbance`
        - Simulation smoothing provides `sampled_measurement_disturbance` and
          `sampled_state_disturbance` (note that this requires Disturbance
          smoothing as well).
    
        Note: this output arrays in this class are always defined in-memory
        according to the original dimensions in the cStatespace object.
    
        Note: if the `filter_method` of the underlying cKalmanFilter
        changes, the smoother *must* be reset using the object callable (__call__)
        or the `reset` method. This is because when the filter method is changed,
        the filter output arrays are reset.
    """
    def reset(self): # real signature unknown; restored from __doc__
        """
        reset(self)
        
                Reset the smoother.
        """
        pass

    def seek(self, t): # real signature unknown; restored from __doc__
        """
        seek(self, t)
        
                Change the time-state of the smoother
        
                Notes
                -----
                Between seek calls, the `filter_method` parameter of the associated
                Kalman filter object is not allowed to change. If the `filter_method`
                has changed, either recall the smoother using the object callable or
                explicitly reset the smoother using the `reset` method.
        """
        pass

    def set_smoother_output(self, *args, **kwargs): # real signature unknown
        pass

    def set_smooth_method(self, *args, **kwargs): # real signature unknown
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Iterate the smoother across the entire set of observations. """
        pass

    def __init__(self, model, kfilter, smoother_output=None): # real signature unknown; restored from __doc__
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Perform an iteration of the Kalman smoother """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    filter_method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    kfilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    model = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scaled_smoothed_diffuse1_estimator_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scaled_smoothed_diffuse2_estimator_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scaled_smoothed_diffuse_estimator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scaled_smoothed_estimator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scaled_smoothed_estimator_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selected_design = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selected_obs_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    smoothed_measurement_disturbance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    smoothed_measurement_disturbance_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    smoothed_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    smoothed_state_autocov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    smoothed_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    smoothed_state_disturbance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    smoothed_state_disturbance_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    smoother_output = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    smoothing_error = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    smooth_method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    t = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp00 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp000 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmpL = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmpL2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp_autocov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _smooth_method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000245707B2690>'


class dKalmanSmoother(object):
    """
    dKalmanSmoother(model, kfilter, smoother_output=SMOOTHING_ALL)
    
        A representation of the Kalman smoother recursions; it performs a single
        backwards pass through the data (after the forwards pass via the Kalman
        filter has already been completed). In all cases, it calculates:
    
        - `scaled_smoothed_estimator`
        - `smoothing_error`
    
        it can optionally peform three types of smoothing:
    
        - State smoothing provides `smoothed_state` and `smoothed_state_cov`
        - Disturbance smoothing provides `smoothed_measurement_disturbance` and
          `smoothed_state_disturbance`
        - Simulation smoothing provides `sampled_measurement_disturbance` and
          `sampled_state_disturbance` (note that this requires Disturbance
          smoothing as well).
    
        Note: this output arrays in this class are always defined in-memory
        according to the original dimensions in the dStatespace object.
    
        Note: if the `filter_method` of the underlying dKalmanFilter
        changes, the smoother *must* be reset using the object callable (__call__)
        or the `reset` method. This is because when the filter method is changed,
        the filter output arrays are reset.
    """
    def reset(self): # real signature unknown; restored from __doc__
        """
        reset(self)
        
                Reset the smoother.
        """
        pass

    def seek(self, t): # real signature unknown; restored from __doc__
        """
        seek(self, t)
        
                Change the time-state of the smoother
        
                Notes
                -----
                Between seek calls, the `filter_method` parameter of the associated
                Kalman filter object is not allowed to change. If the `filter_method`
                has changed, either recall the smoother using the object callable or
                explicitly reset the smoother using the `reset` method.
        """
        pass

    def set_smoother_output(self, *args, **kwargs): # real signature unknown
        pass

    def set_smooth_method(self, *args, **kwargs): # real signature unknown
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Iterate the smoother across the entire set of observations. """
        pass

    def __init__(self, model, kfilter, smoother_output=None): # real signature unknown; restored from __doc__
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Perform an iteration of the Kalman smoother """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    filter_method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    kfilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    model = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scaled_smoothed_diffuse1_estimator_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scaled_smoothed_diffuse2_estimator_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scaled_smoothed_diffuse_estimator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scaled_smoothed_estimator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scaled_smoothed_estimator_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selected_design = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selected_obs_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    smoothed_measurement_disturbance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    smoothed_measurement_disturbance_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    smoothed_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    smoothed_state_autocov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    smoothed_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    smoothed_state_disturbance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    smoothed_state_disturbance_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    smoother_output = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    smoothing_error = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    smooth_method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    t = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp00 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp000 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmpL = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmpL2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp_autocov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _smooth_method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000245707B2660>'


class sKalmanSmoother(object):
    """
    sKalmanSmoother(model, kfilter, smoother_output=SMOOTHING_ALL)
    
        A representation of the Kalman smoother recursions; it performs a single
        backwards pass through the data (after the forwards pass via the Kalman
        filter has already been completed). In all cases, it calculates:
    
        - `scaled_smoothed_estimator`
        - `smoothing_error`
    
        it can optionally peform three types of smoothing:
    
        - State smoothing provides `smoothed_state` and `smoothed_state_cov`
        - Disturbance smoothing provides `smoothed_measurement_disturbance` and
          `smoothed_state_disturbance`
        - Simulation smoothing provides `sampled_measurement_disturbance` and
          `sampled_state_disturbance` (note that this requires Disturbance
          smoothing as well).
    
        Note: this output arrays in this class are always defined in-memory
        according to the original dimensions in the sStatespace object.
    
        Note: if the `filter_method` of the underlying sKalmanFilter
        changes, the smoother *must* be reset using the object callable (__call__)
        or the `reset` method. This is because when the filter method is changed,
        the filter output arrays are reset.
    """
    def reset(self): # real signature unknown; restored from __doc__
        """
        reset(self)
        
                Reset the smoother.
        """
        pass

    def seek(self, t): # real signature unknown; restored from __doc__
        """
        seek(self, t)
        
                Change the time-state of the smoother
        
                Notes
                -----
                Between seek calls, the `filter_method` parameter of the associated
                Kalman filter object is not allowed to change. If the `filter_method`
                has changed, either recall the smoother using the object callable or
                explicitly reset the smoother using the `reset` method.
        """
        pass

    def set_smoother_output(self, *args, **kwargs): # real signature unknown
        pass

    def set_smooth_method(self, *args, **kwargs): # real signature unknown
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Iterate the smoother across the entire set of observations. """
        pass

    def __init__(self, model, kfilter, smoother_output=None): # real signature unknown; restored from __doc__
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Perform an iteration of the Kalman smoother """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    filter_method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    kfilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    model = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scaled_smoothed_diffuse1_estimator_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scaled_smoothed_diffuse2_estimator_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scaled_smoothed_diffuse_estimator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scaled_smoothed_estimator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scaled_smoothed_estimator_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selected_design = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selected_obs_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    smoothed_measurement_disturbance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    smoothed_measurement_disturbance_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    smoothed_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    smoothed_state_autocov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    smoothed_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    smoothed_state_disturbance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    smoothed_state_disturbance_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    smoother_output = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    smoothing_error = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    smooth_method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    t = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp00 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp000 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmpL = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmpL2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp_autocov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _smooth_method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000245707B2630>'


class zKalmanSmoother(object):
    """
    zKalmanSmoother(model, kfilter, smoother_output=SMOOTHING_ALL)
    
        A representation of the Kalman smoother recursions; it performs a single
        backwards pass through the data (after the forwards pass via the Kalman
        filter has already been completed). In all cases, it calculates:
    
        - `scaled_smoothed_estimator`
        - `smoothing_error`
    
        it can optionally peform three types of smoothing:
    
        - State smoothing provides `smoothed_state` and `smoothed_state_cov`
        - Disturbance smoothing provides `smoothed_measurement_disturbance` and
          `smoothed_state_disturbance`
        - Simulation smoothing provides `sampled_measurement_disturbance` and
          `sampled_state_disturbance` (note that this requires Disturbance
          smoothing as well).
    
        Note: this output arrays in this class are always defined in-memory
        according to the original dimensions in the zStatespace object.
    
        Note: if the `filter_method` of the underlying zKalmanFilter
        changes, the smoother *must* be reset using the object callable (__call__)
        or the `reset` method. This is because when the filter method is changed,
        the filter output arrays are reset.
    """
    def reset(self): # real signature unknown; restored from __doc__
        """
        reset(self)
        
                Reset the smoother.
        """
        pass

    def seek(self, t): # real signature unknown; restored from __doc__
        """
        seek(self, t)
        
                Change the time-state of the smoother
        
                Notes
                -----
                Between seek calls, the `filter_method` parameter of the associated
                Kalman filter object is not allowed to change. If the `filter_method`
                has changed, either recall the smoother using the object callable or
                explicitly reset the smoother using the `reset` method.
        """
        pass

    def set_smoother_output(self, *args, **kwargs): # real signature unknown
        pass

    def set_smooth_method(self, *args, **kwargs): # real signature unknown
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Iterate the smoother across the entire set of observations. """
        pass

    def __init__(self, model, kfilter, smoother_output=None): # real signature unknown; restored from __doc__
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Perform an iteration of the Kalman smoother """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    filter_method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    kfilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    model = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scaled_smoothed_diffuse1_estimator_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scaled_smoothed_diffuse2_estimator_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scaled_smoothed_diffuse_estimator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scaled_smoothed_estimator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scaled_smoothed_estimator_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selected_design = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selected_obs_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    smoothed_measurement_disturbance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    smoothed_measurement_disturbance_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    smoothed_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    smoothed_state_autocov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    smoothed_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    smoothed_state_disturbance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    smoothed_state_disturbance_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    smoother_output = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    smoothing_error = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    smooth_method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    t = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp00 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp000 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmpL = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmpL2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp_autocov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _smooth_method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000245707B26C0>'


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000245707F5D68>'

__pyx_capi__ = {
    'SMOOTHER_ALL': None, # (!) real value is '<capsule object "int" at 0x00000245706E1D20>'
    'SMOOTHER_DISTURBANCE': None, # (!) real value is '<capsule object "int" at 0x00000245706E1A80>'
    'SMOOTHER_DISTURBANCE_COV': None, # (!) real value is '<capsule object "int" at 0x00000245706E1AB0>'
    'SMOOTHER_STATE': None, # (!) real value is '<capsule object "int" at 0x00000245706E18A0>'
    'SMOOTHER_STATE_AUTOCOV': None, # (!) real value is '<capsule object "int" at 0x00000245706E1CF0>'
    'SMOOTHER_STATE_COV': None, # (!) real value is '<capsule object "int" at 0x00000245706E1A50>'
    'SMOOTH_ALTERNATIVE': None, # (!) real value is '<capsule object "int" at 0x000002457073D240>'
    'SMOOTH_CLASSICAL': None, # (!) real value is '<capsule object "int" at 0x000002457073D150>'
    'SMOOTH_CONVENTIONAL': None, # (!) real value is '<capsule object "int" at 0x000002457073D210>'
    'SMOOTH_UNIVARIATE': None, # (!) real value is '<capsule object "int" at 0x00000245707B25D0>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='statsmodels.tsa.statespace._kalman_smoother', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000245707F5D68>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\statsmodels\\\\tsa\\\\statespace\\\\_kalman_smoother.cp37-win_amd64.pyd')"

__test__ = {}

