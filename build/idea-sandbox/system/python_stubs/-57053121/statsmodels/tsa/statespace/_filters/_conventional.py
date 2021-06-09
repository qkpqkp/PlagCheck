# encoding: utf-8
# module statsmodels.tsa.statespace._filters._conventional
# from C:\Users\Doly\Anaconda3\lib\site-packages\statsmodels\tsa\statespace\_filters\_conventional.cp37-win_amd64.pyd
# by generator 1.147
"""
State Space Models

Author: Chad Fulton  
License: Simplified-BSD
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

# functions

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000019AA177B9E8>'

__pyx_capi__ = {
    'cforecast_conventional': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_cKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_cStatespace *)" at 0x0000019AB30D4900>'
    'cforecast_missing_conventional': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_cKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_cStatespace *)" at 0x0000019AB30D4810>'
    'cinverse_missing_conventional': None, # (!) real value is '<capsule object "__pyx_t_float_complex (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_cKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_cStatespace *, __pyx_t_float_complex)" at 0x0000019AB30D4870>'
    'cloglikelihood_conventional': None, # (!) real value is '<capsule object "__pyx_t_float_complex (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_cKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_cStatespace *, __pyx_t_float_complex)" at 0x0000019AB30D4990>'
    'cloglikelihood_missing_conventional': None, # (!) real value is '<capsule object "__pyx_t_float_complex (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_cKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_cStatespace *, __pyx_t_float_complex)" at 0x0000019AB30D48A0>'
    'cprediction_conventional': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_cKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_cStatespace *)" at 0x0000019AB30D4960>'
    'cscale_conventional': None, # (!) real value is '<capsule object "__pyx_t_float_complex (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_cKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_cStatespace *)" at 0x0000019AB30D49C0>'
    'cscale_missing_conventional': None, # (!) real value is '<capsule object "__pyx_t_float_complex (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_cKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_cStatespace *)" at 0x0000019AB30D48D0>'
    'cupdating_conventional': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_cKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_cStatespace *)" at 0x0000019AB30D4930>'
    'cupdating_missing_conventional': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_cKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_cStatespace *)" at 0x0000019AB30D4840>'
    'dforecast_conventional': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_dKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_dStatespace *)" at 0x0000019AB30D4720>'
    'dforecast_missing_conventional': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_dKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_dStatespace *)" at 0x0000019AB30D4630>'
    'dinverse_missing_conventional': None, # (!) real value is '<capsule object "__pyx_t_5numpy_float64_t (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_dKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_dStatespace *, __pyx_t_5numpy_float64_t)" at 0x0000019AB30D4690>'
    'dloglikelihood_conventional': None, # (!) real value is '<capsule object "__pyx_t_5numpy_float64_t (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_dKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_dStatespace *, __pyx_t_5numpy_float64_t)" at 0x0000019AB30D47B0>'
    'dloglikelihood_missing_conventional': None, # (!) real value is '<capsule object "__pyx_t_5numpy_float64_t (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_dKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_dStatespace *, __pyx_t_5numpy_float64_t)" at 0x0000019AB30D46C0>'
    'dprediction_conventional': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_dKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_dStatespace *)" at 0x0000019AB30D4780>'
    'dscale_conventional': None, # (!) real value is '<capsule object "__pyx_t_5numpy_float64_t (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_dKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_dStatespace *)" at 0x0000019AB30D47E0>'
    'dscale_missing_conventional': None, # (!) real value is '<capsule object "__pyx_t_5numpy_float64_t (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_dKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_dStatespace *)" at 0x0000019AB30D46F0>'
    'dupdating_conventional': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_dKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_dStatespace *)" at 0x0000019AB30D4750>'
    'dupdating_missing_conventional': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_dKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_dStatespace *)" at 0x0000019AB30D4660>'
    'sforecast_conventional': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_sKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_sStatespace *)" at 0x0000019AB3000D20>'
    'sforecast_missing_conventional': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_sKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_sStatespace *)" at 0x0000019AB30008A0>'
    'sinverse_missing_conventional': None, # (!) real value is '<capsule object "__pyx_t_5numpy_float32_t (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_sKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_sStatespace *, __pyx_t_5numpy_float32_t)" at 0x0000019AB3000A80>'
    'sloglikelihood_conventional': None, # (!) real value is '<capsule object "__pyx_t_5numpy_float32_t (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_sKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_sStatespace *, __pyx_t_5numpy_float32_t)" at 0x0000019AB305D240>'
    'sloglikelihood_missing_conventional': None, # (!) real value is '<capsule object "__pyx_t_5numpy_float32_t (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_sKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_sStatespace *, __pyx_t_5numpy_float32_t)" at 0x0000019AB3000AB0>'
    'sprediction_conventional': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_sKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_sStatespace *)" at 0x0000019AB305D150>'
    'sscale_conventional': None, # (!) real value is '<capsule object "__pyx_t_5numpy_float32_t (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_sKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_sStatespace *)" at 0x0000019AB30D45D0>'
    'sscale_missing_conventional': None, # (!) real value is '<capsule object "__pyx_t_5numpy_float32_t (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_sKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_sStatespace *)" at 0x0000019AB3000CF0>'
    'supdating_conventional': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_sKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_sStatespace *)" at 0x0000019AB305D210>'
    'supdating_missing_conventional': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_sKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_sStatespace *)" at 0x0000019AB3000A50>'
    'zforecast_conventional': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_zKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_zStatespace *)" at 0x0000019AB30D4AE0>'
    'zforecast_missing_conventional': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_zKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_zStatespace *)" at 0x0000019AB30D49F0>'
    'zinverse_missing_conventional': None, # (!) real value is '<capsule object "__pyx_t_double_complex (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_zKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_zStatespace *, __pyx_t_double_complex)" at 0x0000019AB30D4A50>'
    'zloglikelihood_conventional': None, # (!) real value is '<capsule object "__pyx_t_double_complex (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_zKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_zStatespace *, __pyx_t_double_complex)" at 0x0000019AB30D4B70>'
    'zloglikelihood_missing_conventional': None, # (!) real value is '<capsule object "__pyx_t_double_complex (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_zKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_zStatespace *, __pyx_t_double_complex)" at 0x0000019AB30D4A80>'
    'zprediction_conventional': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_zKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_zStatespace *)" at 0x0000019AB30D4B40>'
    'zscale_conventional': None, # (!) real value is '<capsule object "__pyx_t_double_complex (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_zKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_zStatespace *)" at 0x0000019AB30D4BA0>'
    'zscale_missing_conventional': None, # (!) real value is '<capsule object "__pyx_t_double_complex (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_zKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_zStatespace *)" at 0x0000019AB30D4AB0>'
    'zupdating_conventional': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_zKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_zStatespace *)" at 0x0000019AB30D4B10>'
    'zupdating_missing_conventional': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_zKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_zStatespace *)" at 0x0000019AB30D4A20>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='statsmodels.tsa.statespace._filters._conventional', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000019AA177B9E8>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\statsmodels\\\\tsa\\\\statespace\\\\_filters\\\\_conventional.cp37-win_amd64.pyd')"

__test__ = {}

