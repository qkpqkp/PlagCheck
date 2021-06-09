# encoding: utf-8
# module statsmodels.tsa.statespace._simulation_smoother
# from C:\Users\Doly\Anaconda3\lib\site-packages\statsmodels\tsa\statespace\_simulation_smoother.cp37-win_amd64.pyd
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

class cSimulationSmoother(object):
    # no doc
    def draw_disturbance_variates(self, *args, **kwargs): # real signature unknown
        pass

    def draw_initial_state_variates(self, *args, **kwargs): # real signature unknown
        pass

    def set_disturbance_variates(self, *args, **kwargs): # real signature unknown
        pass

    def set_initial_state(self, *args, **kwargs): # real signature unknown
        pass

    def set_initial_state_variates(self, *args, **kwargs): # real signature unknown
        pass

    def simulate(self, *args, **kwargs): # real signature unknown
        """ Draw a simulation """
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

    disturbance_variates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fixed_initial_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    generated_obs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    generated_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    has_missing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    initial_state_variates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    kfilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    model = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nobs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pretransformed_disturbance_variates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pretransformed_initial_state_variates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    secondary_simulated_kfilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    secondary_simulated_model = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    secondary_simulated_smoother = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    simulated_kfilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    simulated_measurement_disturbance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    simulated_model = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    simulated_smoother = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    simulated_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    simulated_state_disturbance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    simulation_output = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    smoother = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001D28704D150>'


class dSimulationSmoother(object):
    # no doc
    def draw_disturbance_variates(self, *args, **kwargs): # real signature unknown
        pass

    def draw_initial_state_variates(self, *args, **kwargs): # real signature unknown
        pass

    def set_disturbance_variates(self, *args, **kwargs): # real signature unknown
        pass

    def set_initial_state(self, *args, **kwargs): # real signature unknown
        pass

    def set_initial_state_variates(self, *args, **kwargs): # real signature unknown
        pass

    def simulate(self, *args, **kwargs): # real signature unknown
        """ Draw a simulation """
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

    disturbance_variates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fixed_initial_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    generated_obs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    generated_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    has_missing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    initial_state_variates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    kfilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    model = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nobs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pretransformed_disturbance_variates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pretransformed_initial_state_variates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    secondary_simulated_kfilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    secondary_simulated_model = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    secondary_simulated_smoother = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    simulated_kfilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    simulated_measurement_disturbance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    simulated_model = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    simulated_smoother = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    simulated_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    simulated_state_disturbance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    simulation_output = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    smoother = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001D28704D210>'


class sSimulationSmoother(object):
    # no doc
    def draw_disturbance_variates(self, *args, **kwargs): # real signature unknown
        pass

    def draw_initial_state_variates(self, *args, **kwargs): # real signature unknown
        pass

    def set_disturbance_variates(self, *args, **kwargs): # real signature unknown
        pass

    def set_initial_state(self, *args, **kwargs): # real signature unknown
        pass

    def set_initial_state_variates(self, *args, **kwargs): # real signature unknown
        pass

    def simulate(self, *args, **kwargs): # real signature unknown
        """ Draw a simulation """
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

    disturbance_variates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fixed_initial_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    generated_obs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    generated_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    has_missing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    initial_state_variates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    kfilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    model = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nobs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pretransformed_disturbance_variates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pretransformed_initial_state_variates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    secondary_simulated_kfilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    secondary_simulated_model = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    secondary_simulated_smoother = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    simulated_kfilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    simulated_measurement_disturbance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    simulated_model = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    simulated_smoother = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    simulated_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    simulated_state_disturbance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    simulation_output = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    smoother = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001D286FF1D20>'


class zSimulationSmoother(object):
    # no doc
    def draw_disturbance_variates(self, *args, **kwargs): # real signature unknown
        pass

    def draw_initial_state_variates(self, *args, **kwargs): # real signature unknown
        pass

    def set_disturbance_variates(self, *args, **kwargs): # real signature unknown
        pass

    def set_initial_state(self, *args, **kwargs): # real signature unknown
        pass

    def set_initial_state_variates(self, *args, **kwargs): # real signature unknown
        pass

    def simulate(self, *args, **kwargs): # real signature unknown
        """ Draw a simulation """
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

    disturbance_variates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fixed_initial_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    generated_obs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    generated_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    has_missing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    initial_state_variates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    kfilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    model = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nobs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pretransformed_disturbance_variates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pretransformed_initial_state_variates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    secondary_simulated_kfilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    secondary_simulated_model = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    secondary_simulated_smoother = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    simulated_kfilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    simulated_measurement_disturbance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    simulated_model = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    simulated_smoother = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    simulated_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    simulated_state_disturbance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    simulation_output = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    smoother = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001D28704D240>'


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001D287102FD0>'

__pyx_capi__ = {
    'SMOOTHER_ALL': None, # (!) real value is '<capsule object "int" at 0x000001D286FF1CF0>'
    'SMOOTHER_DISTURBANCE': None, # (!) real value is '<capsule object "int" at 0x000001D286FF1A80>'
    'SMOOTHER_DISTURBANCE_COV': None, # (!) real value is '<capsule object "int" at 0x000001D286FF1AB0>'
    'SMOOTHER_STATE': None, # (!) real value is '<capsule object "int" at 0x000001D286FF18A0>'
    'SMOOTHER_STATE_COV': None, # (!) real value is '<capsule object "int" at 0x000001D286FF1A50>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='statsmodels.tsa.statespace._simulation_smoother', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001D287102FD0>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\statsmodels\\\\tsa\\\\statespace\\\\_simulation_smoother.cp37-win_amd64.pyd')"

__test__ = {}

