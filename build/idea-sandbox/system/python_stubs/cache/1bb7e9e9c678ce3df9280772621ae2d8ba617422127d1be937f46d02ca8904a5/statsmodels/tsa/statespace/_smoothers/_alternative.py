# encoding: utf-8
# module statsmodels.tsa.statespace._smoothers._alternative
# from C:\Users\Doly\Anaconda3\lib\site-packages\statsmodels\tsa\statespace\_smoothers\_alternative.cp37-win_amd64.pyd
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

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000261DDEEB9B0>'

__pyx_capi__ = {
    'csmoothed_disturbances_alternative': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_16_kalman_smoother_cKalmanSmoother *, struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_cKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_cStatespace *)" at 0x00000261EF843660>'
    'csmoothed_estimators_measurement_alternative': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_16_kalman_smoother_cKalmanSmoother *, struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_cKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_cStatespace *)" at 0x00000261EF7CD240>'
    'csmoothed_estimators_time_alternative': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_16_kalman_smoother_cKalmanSmoother *, struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_cKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_cStatespace *)" at 0x00000261EF8435D0>'
    'csmoothed_state_alternative': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_16_kalman_smoother_cKalmanSmoother *, struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_cKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_cStatespace *)" at 0x00000261EF843630>'
    'dsmoothed_disturbances_alternative': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_16_kalman_smoother_dKalmanSmoother *, struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_dKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_dStatespace *)" at 0x00000261EF7CD150>'
    'dsmoothed_estimators_measurement_alternative': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_16_kalman_smoother_dKalmanSmoother *, struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_dKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_dStatespace *)" at 0x00000261EF771CF0>'
    'dsmoothed_estimators_time_alternative': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_16_kalman_smoother_dKalmanSmoother *, struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_dKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_dStatespace *)" at 0x00000261EF771D20>'
    'dsmoothed_state_alternative': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_16_kalman_smoother_dKalmanSmoother *, struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_dKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_dStatespace *)" at 0x00000261EF7CD210>'
    'ssmoothed_disturbances_alternative': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_16_kalman_smoother_sKalmanSmoother *, struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_sKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_sStatespace *)" at 0x00000261EF771AB0>'
    'ssmoothed_estimators_measurement_alternative': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_16_kalman_smoother_sKalmanSmoother *, struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_sKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_sStatespace *)" at 0x00000261EF7718A0>'
    'ssmoothed_estimators_time_alternative': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_16_kalman_smoother_sKalmanSmoother *, struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_sKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_sStatespace *)" at 0x00000261EF771A50>'
    'ssmoothed_state_alternative': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_16_kalman_smoother_sKalmanSmoother *, struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_sKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_sStatespace *)" at 0x00000261EF771A80>'
    'zsmoothed_disturbances_alternative': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_16_kalman_smoother_zKalmanSmoother *, struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_zKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_zStatespace *)" at 0x00000261EF843720>'
    'zsmoothed_estimators_measurement_alternative': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_16_kalman_smoother_zKalmanSmoother *, struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_zKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_zStatespace *)" at 0x00000261EF843690>'
    'zsmoothed_estimators_time_alternative': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_16_kalman_smoother_zKalmanSmoother *, struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_zKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_zStatespace *)" at 0x00000261EF8436C0>'
    'zsmoothed_state_alternative': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_16_kalman_smoother_zKalmanSmoother *, struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_zKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_zStatespace *)" at 0x00000261EF8436F0>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='statsmodels.tsa.statespace._smoothers._alternative', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000261DDEEB9B0>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\statsmodels\\\\tsa\\\\statespace\\\\_smoothers\\\\_alternative.cp37-win_amd64.pyd')"

__test__ = {}

