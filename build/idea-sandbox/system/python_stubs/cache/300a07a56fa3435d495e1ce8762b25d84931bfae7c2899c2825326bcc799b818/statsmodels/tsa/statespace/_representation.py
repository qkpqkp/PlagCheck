# encoding: utf-8
# module statsmodels.tsa.statespace._representation
# from C:\Users\Doly\Anaconda3\lib\site-packages\statsmodels\tsa\statespace\_representation.cp37-win_amd64.pyd
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

class cStatespace(object):
    """
    cStatespace(obs, design, obs_intercept, obs_cov, transition, state_intercept, selection, state_cov)
    
        *See Durbin and Koopman (2012), Chapter 4 for all notation*
    """
    def initialize(self, *args, **kwargs): # real signature unknown
        pass

    def initialize_approximate_diffuse(self, variance=1, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ initialize_approximate_diffuse(variance=1e2) """
        pass

    def initialize_known(self, initial_state, initial_state_cov): # real signature unknown; restored from __doc__
        """ initialize_known(initial_state, initial_state_cov) """
        pass

    def initialize_stationary(self): # real signature unknown; restored from __doc__
        """ initialize_stationary() """
        pass

    def seek(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, obs, design, obs_intercept, obs_cov, transition, state_intercept, selection, state_cov): # real signature unknown; restored from __doc__
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Advance to the next location """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    collapse_cholesky = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    collapse_design = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    collapse_loglikelihood = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    collapse_obs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    collapse_obs_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    collapse_obs_tmp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    companion_transition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    design = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    diagonal_obs_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    has_missing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    initialized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    initial_diffuse_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    initial_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    initial_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_endog = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_posdef = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_states = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    missing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nmissing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nobs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    obs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    obs_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    obs_intercept = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selected_design = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selected_obs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selected_obs_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selected_obs_intercept = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selected_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state_intercept = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    subset_design = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    time_invariant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transform_cholesky = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transform_design = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transform_determinant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transform_obs_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002906E52D210>'


class dStatespace(object):
    """
    dStatespace(obs, design, obs_intercept, obs_cov, transition, state_intercept, selection, state_cov)
    
        *See Durbin and Koopman (2012), Chapter 4 for all notation*
    """
    def initialize(self, *args, **kwargs): # real signature unknown
        pass

    def initialize_approximate_diffuse(self, variance=1, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ initialize_approximate_diffuse(variance=1e2) """
        pass

    def initialize_known(self, initial_state, initial_state_cov): # real signature unknown; restored from __doc__
        """ initialize_known(initial_state, initial_state_cov) """
        pass

    def initialize_stationary(self): # real signature unknown; restored from __doc__
        """ initialize_stationary() """
        pass

    def seek(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, obs, design, obs_intercept, obs_cov, transition, state_intercept, selection, state_cov): # real signature unknown; restored from __doc__
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Advance to the next location """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    collapse_cholesky = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    collapse_design = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    collapse_loglikelihood = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    collapse_obs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    collapse_obs_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    collapse_obs_tmp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    companion_transition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    design = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    diagonal_obs_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    has_missing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    initialized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    initial_diffuse_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    initial_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    initial_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_endog = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_posdef = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_states = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    missing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nmissing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nobs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    obs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    obs_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    obs_intercept = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selected_design = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selected_obs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selected_obs_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selected_obs_intercept = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selected_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state_intercept = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    subset_design = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    time_invariant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transform_cholesky = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transform_design = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transform_determinant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transform_obs_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002906E4D1D20>'


class sStatespace(object):
    """
    sStatespace(obs, design, obs_intercept, obs_cov, transition, state_intercept, selection, state_cov)
    
        *See Durbin and Koopman (2012), Chapter 4 for all notation*
    """
    def initialize(self, *args, **kwargs): # real signature unknown
        pass

    def initialize_approximate_diffuse(self, variance=1, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ initialize_approximate_diffuse(variance=1e2) """
        pass

    def initialize_known(self, initial_state, initial_state_cov): # real signature unknown; restored from __doc__
        """ initialize_known(initial_state, initial_state_cov) """
        pass

    def initialize_stationary(self): # real signature unknown; restored from __doc__
        """ initialize_stationary() """
        pass

    def seek(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, obs, design, obs_intercept, obs_cov, transition, state_intercept, selection, state_cov): # real signature unknown; restored from __doc__
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Advance to the next location """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    collapse_cholesky = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    collapse_design = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    collapse_loglikelihood = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    collapse_obs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    collapse_obs_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    collapse_obs_tmp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    companion_transition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    design = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    diagonal_obs_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    has_missing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    initialized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    initial_diffuse_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    initial_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    initial_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_endog = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_posdef = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_states = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    missing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nmissing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nobs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    obs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    obs_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    obs_intercept = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selected_design = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selected_obs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selected_obs_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selected_obs_intercept = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selected_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state_intercept = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    subset_design = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    time_invariant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transform_cholesky = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transform_design = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transform_determinant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transform_obs_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002906E4D1CF0>'


class zStatespace(object):
    """
    zStatespace(obs, design, obs_intercept, obs_cov, transition, state_intercept, selection, state_cov)
    
        *See Durbin and Koopman (2012), Chapter 4 for all notation*
    """
    def initialize(self, *args, **kwargs): # real signature unknown
        pass

    def initialize_approximate_diffuse(self, variance=1, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ initialize_approximate_diffuse(variance=1e2) """
        pass

    def initialize_known(self, initial_state, initial_state_cov): # real signature unknown; restored from __doc__
        """ initialize_known(initial_state, initial_state_cov) """
        pass

    def initialize_stationary(self): # real signature unknown; restored from __doc__
        """ initialize_stationary() """
        pass

    def seek(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, obs, design, obs_intercept, obs_cov, transition, state_intercept, selection, state_cov): # real signature unknown; restored from __doc__
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Advance to the next location """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    collapse_cholesky = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    collapse_design = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    collapse_loglikelihood = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    collapse_obs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    collapse_obs_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    collapse_obs_tmp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    companion_transition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    design = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    diagonal_obs_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    has_missing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    initialized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    initial_diffuse_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    initial_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    initial_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_endog = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_posdef = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_states = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    missing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nmissing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nobs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    obs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    obs_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    obs_intercept = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selected_design = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selected_obs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selected_obs_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selected_obs_intercept = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selected_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state_intercept = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    subset_design = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    time_invariant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transform_cholesky = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transform_design = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transform_determinant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transform_obs_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002906E52D150>'


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000002906E5E5D68>'

__pyx_capi__ = {
    'cselect_cov': None, # (!) real value is '<capsule object "int (int, int, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *)" at 0x000002906E4D1A80>'
    'dselect_cov': None, # (!) real value is '<capsule object "int (int, int, __pyx_t_5numpy_float64_t *, __pyx_t_5numpy_float64_t *, __pyx_t_5numpy_float64_t *, __pyx_t_5numpy_float64_t *)" at 0x000002906E4D1A50>'
    'sselect_cov': None, # (!) real value is '<capsule object "int (int, int, __pyx_t_5numpy_float32_t *, __pyx_t_5numpy_float32_t *, __pyx_t_5numpy_float32_t *, __pyx_t_5numpy_float32_t *)" at 0x000002906E4D18A0>'
    'zselect_cov': None, # (!) real value is '<capsule object "int (int, int, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *)" at 0x000002906E4D1AB0>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='statsmodels.tsa.statespace._representation', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000002906E5E5D68>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\statsmodels\\\\tsa\\\\statespace\\\\_representation.cp37-win_amd64.pyd')"

__test__ = {}

