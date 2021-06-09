# encoding: utf-8
# module statsmodels.tsa.statespace._smoothers._univariate
# from C:\Users\Doly\Anaconda3\lib\site-packages\statsmodels\tsa\statespace\_smoothers\_univariate.cp37-win_amd64.pyd
# by generator 1.147
"""
State Space Models

Note: there is a typo in Durbin and Koopman (2012) in the equations for the
univariate smoothed measurement disturbances and smoothed measurement
disturbance covariances. In each equation (p157), the Kalman gain vector
K_{t,i} is used, but in fact these should be multiplied by the forecast error
covariance F_{t,i}. The original paper on the univariate approach, Koopman and
Durbin (2000) has the correct form. The typo arose because the original paper
defines the Kalman gain as K_{t,i} = P_{t,i} Z_{t,i}' but the book defines it
as K_{t,i} = P_{t,i} Z_{t,i}' F_{t,i}^{-1}, and the book does not correct the
disturbances formulas for this change.

Furthermore, in analogy to the disturbance smoother from chapter 4, the
formula for the univariate covariance ought to be subtracted from the
observation covariance.

So, what we ought to have is:

\hat arepsilon_{t,i} = \sigma_{t,i}^2 F_{t,i}^{-1} (v_{t,i} - F_{t,i} K_{t,i}' r_{t,i})
Var(\hat arepsilon_{t,i}) = \sigma_{t,i}^2 - \sigma_{t,i}^4 F_{t,i}^{-2} (v_{t,i} - F_{t,i} K_{t,i}' r_{t,i})

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

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000265811EB940>'

__pyx_capi__ = {
    'csmoothed_disturbances_univariate': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_16_kalman_smoother_cKalmanSmoother *, struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_cKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_cStatespace *)" at 0x0000026592ACD240>'
    'csmoothed_estimators_measurement_univariate': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_16_kalman_smoother_cKalmanSmoother *, struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_cKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_cStatespace *)" at 0x0000026592ACD210>'
    'csmoothed_estimators_time_univariate': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_16_kalman_smoother_cKalmanSmoother *, struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_cKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_cStatespace *)" at 0x0000026592ACD150>'
    'dsmoothed_disturbances_univariate': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_16_kalman_smoother_dKalmanSmoother *, struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_dKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_dStatespace *)" at 0x0000026592A70D20>'
    'dsmoothed_estimators_measurement_univariate': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_16_kalman_smoother_dKalmanSmoother *, struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_dKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_dStatespace *)" at 0x0000026592A70AB0>'
    'dsmoothed_estimators_time_univariate': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_16_kalman_smoother_dKalmanSmoother *, struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_dKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_dStatespace *)" at 0x0000026592A70CF0>'
    'ssmoothed_disturbances_univariate': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_16_kalman_smoother_sKalmanSmoother *, struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_sKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_sStatespace *)" at 0x0000026592A70A80>'
    'ssmoothed_estimators_measurement_univariate': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_16_kalman_smoother_sKalmanSmoother *, struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_sKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_sStatespace *)" at 0x0000026592A708A0>'
    'ssmoothed_estimators_time_univariate': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_16_kalman_smoother_sKalmanSmoother *, struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_sKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_sStatespace *)" at 0x0000026592A70A50>'
    'zsmoothed_disturbances_univariate': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_16_kalman_smoother_zKalmanSmoother *, struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_zKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_zStatespace *)" at 0x0000026592B44660>'
    'zsmoothed_estimators_measurement_univariate': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_16_kalman_smoother_zKalmanSmoother *, struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_zKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_zStatespace *)" at 0x0000026592B445D0>'
    'zsmoothed_estimators_time_univariate': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_16_kalman_smoother_zKalmanSmoother *, struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_zKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_zStatespace *)" at 0x0000026592B44630>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='statsmodels.tsa.statespace._smoothers._univariate', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000265811EB940>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\statsmodels\\\\tsa\\\\statespace\\\\_smoothers\\\\_univariate.cp37-win_amd64.pyd')"

__test__ = {}

