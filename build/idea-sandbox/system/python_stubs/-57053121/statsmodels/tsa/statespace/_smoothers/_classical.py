# encoding: utf-8
# module statsmodels.tsa.statespace._smoothers._classical
# from C:\Users\Doly\Anaconda3\lib\site-packages\statsmodels\tsa\statespace\_smoothers\_classical.cp37-win_amd64.pyd
# by generator 1.147
"""
State Space Models

Author: Chad Fulton  
License: Simplified-BSD

Notes
-----

The dimensions used in all the BLAS / LAPACK calls below use the following
convention:

- The dimensions of the arrays *as they are to be manipulated* are all defined
  as model._k_*
- If the array in question is defined in the Statespace object
  (obs, obs_intercept, design, obs_cov, state_intercept, transition, selection,
  state_cov, selected_state_cov), then the dimension in-memory is defined as
  model._k_*
  This is because the in-memory shape of matrices changes according to whether
  or not data is missing and whether or not the generalized collapse transform
  is applied.
- If the array in question is defined in the Kalman filter object
  (forecast_*, filtered_*, predicted_*, etc.), then the dimension in-memory is
  defined as kfilter.k_*
  This is because the in-memory shape of matrices only changes according to
  filter_method.
- If the array in question is defined in the Kalman smoother object
  (smoothed_*, etc.), then the dimension in-memory is defined as kfilter.k_*
  This is because the in-memory shape of matrices only changes according to
  filter_method.

Thus, for example, a ?gemm call has the following signature:

dgemm(transa, transb, m, n, k, alpha, a, lda, b, ldb, beta, c, ldc)

- m, n, and k are the dimensions *as they are to be manipulated*, and are
  always defined as model._k_*
- lda, ldb, and ldc are the *in-memory* dimension, and they are set as
  model._k_* if the array is defined in the Statespace object, otherwise
  (in either the filter or smoother cases) they are set as kfilter.k_*

Note that for ?copy calls, the number of elements to be copied is defined to be
the dimension in memory of the array that is being copied *from*.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py

# functions

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001DBBEE7B9E8>'

__pyx_capi__ = {
    'csmoothed_estimators_measurement_classical': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_16_kalman_smoother_cKalmanSmoother *, struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_cKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_cStatespace *)" at 0x000001DBD075E210>'
    'csmoothed_estimators_time_classical': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_16_kalman_smoother_cKalmanSmoother *, struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_cKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_cStatespace *)" at 0x000001DBD075E150>'
    'csmoothed_state_classical': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_16_kalman_smoother_cKalmanSmoother *, struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_cKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_cStatespace *)" at 0x000001DBD075E240>'
    'dsmoothed_estimators_measurement_classical': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_16_kalman_smoother_dKalmanSmoother *, struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_dKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_dStatespace *)" at 0x000001DBD0700AB0>'
    'dsmoothed_estimators_time_classical': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_16_kalman_smoother_dKalmanSmoother *, struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_dKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_dStatespace *)" at 0x000001DBD0700CF0>'
    'dsmoothed_state_classical': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_16_kalman_smoother_dKalmanSmoother *, struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_dKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_dStatespace *)" at 0x000001DBD0700D20>'
    'ssmoothed_estimators_measurement_classical': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_16_kalman_smoother_sKalmanSmoother *, struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_sKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_sStatespace *)" at 0x000001DBD07008A0>'
    'ssmoothed_estimators_time_classical': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_16_kalman_smoother_sKalmanSmoother *, struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_sKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_sStatespace *)" at 0x000001DBD0700A50>'
    'ssmoothed_state_classical': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_16_kalman_smoother_sKalmanSmoother *, struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_sKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_sStatespace *)" at 0x000001DBD0700A80>'
    'zsmoothed_estimators_measurement_classical': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_16_kalman_smoother_zKalmanSmoother *, struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_zKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_zStatespace *)" at 0x000001DBD07D35D0>'
    'zsmoothed_estimators_time_classical': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_16_kalman_smoother_zKalmanSmoother *, struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_zKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_zStatespace *)" at 0x000001DBD07D3630>'
    'zsmoothed_state_classical': None, # (!) real value is '<capsule object "int (struct __pyx_obj_11statsmodels_3tsa_10statespace_16_kalman_smoother_zKalmanSmoother *, struct __pyx_obj_11statsmodels_3tsa_10statespace_14_kalman_filter_zKalmanFilter *, struct __pyx_obj_11statsmodels_3tsa_10statespace_15_representation_zStatespace *)" at 0x000001DBD07D3660>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='statsmodels.tsa.statespace._smoothers._classical', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001DBBEE7B9E8>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\statsmodels\\\\tsa\\\\statespace\\\\_smoothers\\\\_classical.cp37-win_amd64.pyd')"

__test__ = {}

