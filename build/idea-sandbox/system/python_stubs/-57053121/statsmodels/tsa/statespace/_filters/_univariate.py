# encoding: utf-8
# module statsmodels.tsa.statespace._filters._univariate
# from C:\Users\Doly\Anaconda3\lib\site-packages\statsmodels\tsa\statespace\_filters\_univariate.cp37-win_amd64.pyd
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

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001D8D2D6B7B8>'

__pyx_capi__ = {
    'cfiltered_state': None, # (!) real value is '<capsule object "void (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_cKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_cStatespace *, int, __pyx_t_float_complex)" at 0x000001D8E46C2B40>'
    'cfiltered_state_cov': None, # (!) real value is '<capsule object "void (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_cKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_cStatespace *, int, __pyx_t_float_complex)" at 0x000001D8E46C2B70>'
    'cforecast_error': None, # (!) real value is '<capsule object "void (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_cKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_cStatespace *, int)" at 0x000001D8E46C2AB0>'
    'cforecast_error_cov': None, # (!) real value is '<capsule object "__pyx_t_float_complex (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_cKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_cStatespace *, int)" at 0x000001D8E46C2AE0>'
    'cforecast_univariate': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_cKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_cStatespace *)" at 0x000001D8E46C2990>'
    'cinverse_noop_univariate': None, # (!) real value is '<capsule object "__pyx_t_float_complex (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_cKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_cStatespace *, __pyx_t_float_complex)" at 0x000001D8E46C2A20>'
    'cloglikelihood': None, # (!) real value is '<capsule object "void (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_cKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_cStatespace *, int, __pyx_t_float_complex, __pyx_t_float_complex)" at 0x000001D8E46C2C00>'
    'cloglikelihood_univariate': None, # (!) real value is '<capsule object "__pyx_t_float_complex (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_cKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_cStatespace *, __pyx_t_float_complex)" at 0x000001D8E46C2A50>'
    'cpredicted_state': None, # (!) real value is '<capsule object "void (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_cKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_cStatespace *)" at 0x000001D8E46C2BA0>'
    'cpredicted_state_cov': None, # (!) real value is '<capsule object "void (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_cKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_cStatespace *)" at 0x000001D8E46C2BD0>'
    'cprediction_univariate': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_cKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_cStatespace *)" at 0x000001D8E46C29F0>'
    'cscale_univariate': None, # (!) real value is '<capsule object "__pyx_t_float_complex (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_cKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_cStatespace *)" at 0x000001D8E46C2A80>'
    'ctemp_arrays': None, # (!) real value is '<capsule object "void (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_cKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_cStatespace *, int, __pyx_t_float_complex)" at 0x000001D8E46C2B10>'
    'cupdating_univariate': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_cKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_cStatespace *)" at 0x000001D8E46C29C0>'
    'dfiltered_state': None, # (!) real value is '<capsule object "void (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_dKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_dStatespace *, int, __pyx_t_5numpy_float64_t)" at 0x000001D8E46C28A0>'
    'dfiltered_state_cov': None, # (!) real value is '<capsule object "void (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_dKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_dStatespace *, int, __pyx_t_5numpy_float64_t)" at 0x000001D8E46C28D0>'
    'dforecast_error': None, # (!) real value is '<capsule object "void (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_dKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_dStatespace *, int)" at 0x000001D8E46C2810>'
    'dforecast_error_cov': None, # (!) real value is '<capsule object "__pyx_t_5numpy_float64_t (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_dKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_dStatespace *, int)" at 0x000001D8E46C2840>'
    'dforecast_univariate': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_dKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_dStatespace *)" at 0x000001D8E46C26F0>'
    'dinverse_noop_univariate': None, # (!) real value is '<capsule object "__pyx_t_5numpy_float64_t (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_dKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_dStatespace *, __pyx_t_5numpy_float64_t)" at 0x000001D8E46C2780>'
    'dloglikelihood': None, # (!) real value is '<capsule object "void (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_dKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_dStatespace *, int, __pyx_t_5numpy_float64_t, __pyx_t_5numpy_float64_t)" at 0x000001D8E46C2960>'
    'dloglikelihood_univariate': None, # (!) real value is '<capsule object "__pyx_t_5numpy_float64_t (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_dKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_dStatespace *, __pyx_t_5numpy_float64_t)" at 0x000001D8E46C27B0>'
    'dpredicted_state': None, # (!) real value is '<capsule object "void (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_dKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_dStatespace *)" at 0x000001D8E46C2900>'
    'dpredicted_state_cov': None, # (!) real value is '<capsule object "void (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_dKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_dStatespace *)" at 0x000001D8E46C2930>'
    'dprediction_univariate': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_dKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_dStatespace *)" at 0x000001D8E46C2750>'
    'dscale_univariate': None, # (!) real value is '<capsule object "__pyx_t_5numpy_float64_t (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_dKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_dStatespace *)" at 0x000001D8E46C27E0>'
    'dtemp_arrays': None, # (!) real value is '<capsule object "void (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_dKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_dStatespace *, int, __pyx_t_5numpy_float64_t)" at 0x000001D8E46C2870>'
    'dupdating_univariate': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_dKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_dStatespace *)" at 0x000001D8E46C2720>'
    'sfiltered_state': None, # (!) real value is '<capsule object "void (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_sKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_sStatespace *, int, __pyx_t_5numpy_float32_t)" at 0x000001D8E46C25D0>'
    'sfiltered_state_cov': None, # (!) real value is '<capsule object "void (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_sKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_sStatespace *, int, __pyx_t_5numpy_float32_t)" at 0x000001D8E46C2630>'
    'sforecast_error': None, # (!) real value is '<capsule object "void (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_sKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_sStatespace *, int)" at 0x000001D8E464E210>'
    'sforecast_error_cov': None, # (!) real value is '<capsule object "__pyx_t_5numpy_float32_t (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_sKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_sStatespace *, int)" at 0x000001D8E464E150>'
    'sforecast_univariate': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_sKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_sStatespace *)" at 0x000001D8E45F08A0>'
    'sinverse_noop_univariate': None, # (!) real value is '<capsule object "__pyx_t_5numpy_float32_t (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_sKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_sStatespace *, __pyx_t_5numpy_float32_t)" at 0x000001D8E45F0AB0>'
    'sloglikelihood': None, # (!) real value is '<capsule object "void (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_sKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_sStatespace *, int, __pyx_t_5numpy_float32_t, __pyx_t_5numpy_float32_t)" at 0x000001D8E46C26C0>'
    'sloglikelihood_univariate': None, # (!) real value is '<capsule object "__pyx_t_5numpy_float32_t (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_sKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_sStatespace *, __pyx_t_5numpy_float32_t)" at 0x000001D8E45F0CF0>'
    'spredicted_state': None, # (!) real value is '<capsule object "void (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_sKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_sStatespace *)" at 0x000001D8E46C2660>'
    'spredicted_state_cov': None, # (!) real value is '<capsule object "void (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_sKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_sStatespace *)" at 0x000001D8E46C2690>'
    'sprediction_univariate': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_sKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_sStatespace *)" at 0x000001D8E45F0A80>'
    'sscale_univariate': None, # (!) real value is '<capsule object "__pyx_t_5numpy_float32_t (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_sKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_sStatespace *)" at 0x000001D8E45F0D20>'
    'stemp_arrays': None, # (!) real value is '<capsule object "void (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_sKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_sStatespace *, int, __pyx_t_5numpy_float32_t)" at 0x000001D8E464E240>'
    'supdating_univariate': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_sKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_sStatespace *)" at 0x000001D8E45F0A50>'
    'zfiltered_state': None, # (!) real value is '<capsule object "void (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_zKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_zStatespace *, int, __pyx_t_double_complex)" at 0x000001D8E46C2DE0>'
    'zfiltered_state_cov': None, # (!) real value is '<capsule object "void (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_zKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_zStatespace *, int, __pyx_t_double_complex)" at 0x000001D8E46C2E10>'
    'zforecast_error': None, # (!) real value is '<capsule object "void (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_zKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_zStatespace *, int)" at 0x000001D8E46C2D50>'
    'zforecast_error_cov': None, # (!) real value is '<capsule object "__pyx_t_double_complex (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_zKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_zStatespace *, int)" at 0x000001D8E46C2D80>'
    'zforecast_univariate': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_zKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_zStatespace *)" at 0x000001D8E46C2C30>'
    'zinverse_noop_univariate': None, # (!) real value is '<capsule object "__pyx_t_double_complex (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_zKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_zStatespace *, __pyx_t_double_complex)" at 0x000001D8E46C2CC0>'
    'zloglikelihood': None, # (!) real value is '<capsule object "void (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_zKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_zStatespace *, int, __pyx_t_double_complex, __pyx_t_double_complex)" at 0x000001D8E46C2EA0>'
    'zloglikelihood_univariate': None, # (!) real value is '<capsule object "__pyx_t_double_complex (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_zKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_zStatespace *, __pyx_t_double_complex)" at 0x000001D8E46C2CF0>'
    'zpredicted_state': None, # (!) real value is '<capsule object "void (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_zKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_zStatespace *)" at 0x000001D8E46C2E40>'
    'zpredicted_state_cov': None, # (!) real value is '<capsule object "void (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_zKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_zStatespace *)" at 0x000001D8E46C2E70>'
    'zprediction_univariate': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_zKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_zStatespace *)" at 0x000001D8E46C2C90>'
    'zscale_univariate': None, # (!) real value is '<capsule object "__pyx_t_double_complex (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_zKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_zStatespace *)" at 0x000001D8E46C2D20>'
    'ztemp_arrays': None, # (!) real value is '<capsule object "void (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_zKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_zStatespace *, int, __pyx_t_double_complex)" at 0x000001D8E46C2DB0>'
    'zupdating_univariate': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_zKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_zStatespace *)" at 0x000001D8E46C2C60>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='statsmodels.tsa.statespace._filters._univariate', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001D8D2D6B7B8>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\statsmodels\\\\tsa\\\\statespace\\\\_filters\\\\_univariate.cp37-win_amd64.pyd')"

__test__ = {}

