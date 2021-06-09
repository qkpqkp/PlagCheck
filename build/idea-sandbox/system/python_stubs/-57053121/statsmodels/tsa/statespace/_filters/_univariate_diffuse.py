# encoding: utf-8
# module statsmodels.tsa.statespace._filters._univariate_diffuse
# from C:\Users\Doly\Anaconda3\lib\site-packages\statsmodels\tsa\statespace\_filters\_univariate_diffuse.cp37-win_amd64.pyd
# by generator 1.147
"""
State Space Models

Author: Chad Fulton  
License: Simplified-BSD
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py

# functions

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001E88C73B780>'

__pyx_capi__ = {
    'cforecast_error_diffuse_cov': None, # (!) real value is '<capsule object "__pyx_t_float_complex (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_cKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_cStatespace *, int)" at 0x000001E89E0937E0>'
    'cforecast_univariate_diffuse': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_cKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_cStatespace *)" at 0x000001E89E0936F0>'
    'cinverse_noop_univariate_diffuse': None, # (!) real value is '<capsule object "__pyx_t_float_complex (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_cKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_cStatespace *, __pyx_t_float_complex)" at 0x000001E89E093780>'
    'cloglikelihood_univariate_diffuse': None, # (!) real value is '<capsule object "__pyx_t_float_complex (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_cKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_cStatespace *, __pyx_t_float_complex)" at 0x000001E89E0937B0>'
    'cpredicted_diffuse_state_cov': None, # (!) real value is '<capsule object "void (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_cKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_cStatespace *)" at 0x000001E89E093810>'
    'cprediction_univariate_diffuse': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_cKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_cStatespace *)" at 0x000001E89E093750>'
    'cupdating_univariate_diffuse': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_cKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_cStatespace *)" at 0x000001E89E093720>'
    'dforecast_error_diffuse_cov': None, # (!) real value is '<capsule object "__pyx_t_5numpy_float64_t (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_dKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_dStatespace *, int)" at 0x000001E89E093690>'
    'dforecast_univariate_diffuse': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_dKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_dStatespace *)" at 0x000001E89E01E150>'
    'dinverse_noop_univariate_diffuse': None, # (!) real value is '<capsule object "__pyx_t_5numpy_float64_t (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_dKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_dStatespace *, __pyx_t_5numpy_float64_t)" at 0x000001E89E093630>'
    'dloglikelihood_univariate_diffuse': None, # (!) real value is '<capsule object "__pyx_t_5numpy_float64_t (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_dKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_dStatespace *, __pyx_t_5numpy_float64_t)" at 0x000001E89E093660>'
    'dpredicted_diffuse_state_cov': None, # (!) real value is '<capsule object "void (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_dKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_dStatespace *)" at 0x000001E89E0936C0>'
    'dprediction_univariate_diffuse': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_dKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_dStatespace *)" at 0x000001E89E0935D0>'
    'dupdating_univariate_diffuse': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_dKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_dStatespace *)" at 0x000001E89E01E240>'
    'sforecast_error_diffuse_cov': None, # (!) real value is '<capsule object "__pyx_t_5numpy_float32_t (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_sKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_sStatespace *, int)" at 0x000001E89DFC1D20>'
    'sforecast_univariate_diffuse': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_sKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_sStatespace *)" at 0x000001E89DFC18A0>'
    'sinverse_noop_univariate_diffuse': None, # (!) real value is '<capsule object "__pyx_t_5numpy_float32_t (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_sKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_sStatespace *, __pyx_t_5numpy_float32_t)" at 0x000001E89DFC1AB0>'
    'sloglikelihood_univariate_diffuse': None, # (!) real value is '<capsule object "__pyx_t_5numpy_float32_t (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_sKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_sStatespace *, __pyx_t_5numpy_float32_t)" at 0x000001E89DFC1CF0>'
    'spredicted_diffuse_state_cov': None, # (!) real value is '<capsule object "void (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_sKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_sStatespace *)" at 0x000001E89E01E210>'
    'sprediction_univariate_diffuse': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_sKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_sStatespace *)" at 0x000001E89DFC1A80>'
    'supdating_univariate_diffuse': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_sKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_sStatespace *)" at 0x000001E89DFC1A50>'
    'zforecast_error_diffuse_cov': None, # (!) real value is '<capsule object "__pyx_t_double_complex (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_zKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_zStatespace *, int)" at 0x000001E89E093930>'
    'zforecast_univariate_diffuse': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_zKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_zStatespace *)" at 0x000001E89E093840>'
    'zinverse_noop_univariate_diffuse': None, # (!) real value is '<capsule object "__pyx_t_double_complex (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_zKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_zStatespace *, __pyx_t_double_complex)" at 0x000001E89E0938D0>'
    'zloglikelihood_univariate_diffuse': None, # (!) real value is '<capsule object "__pyx_t_double_complex (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_zKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_zStatespace *, __pyx_t_double_complex)" at 0x000001E89E093900>'
    'zpredicted_diffuse_state_cov': None, # (!) real value is '<capsule object "void (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_zKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_zStatespace *)" at 0x000001E89E093960>'
    'zprediction_univariate_diffuse': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_zKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_zStatespace *)" at 0x000001E89E0938A0>'
    'zupdating_univariate_diffuse': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_zKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_zStatespace *)" at 0x000001E89E093870>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='statsmodels.tsa.statespace._filters._univariate_diffuse', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001E88C73B780>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\statsmodels\\\\tsa\\\\statespace\\\\_filters\\\\_univariate_diffuse.cp37-win_amd64.pyd')"

__test__ = {}

