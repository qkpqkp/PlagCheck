# encoding: utf-8
# module statsmodels.tsa.statespace._tools
# from C:\Users\Doly\Anaconda3\lib\site-packages\statsmodels\tsa\statespace\_tools.cp37-win_amd64.pyd
# by generator 1.147
"""
State Space Model - Cython tools

Author: Chad Fulton  
License: Simplified-BSD
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py

# functions

def ccopy_index_matrix(*args, **kwargs): # real signature unknown
    pass

def ccopy_index_vector(*args, **kwargs): # real signature unknown
    pass

def ccopy_missing_matrix(*args, **kwargs): # real signature unknown
    pass

def ccopy_missing_vector(*args, **kwargs): # real signature unknown
    pass

def cldl(*args, **kwargs): # real signature unknown
    pass

def creorder_missing_matrix(*args, **kwargs): # real signature unknown
    pass

def creorder_missing_vector(*args, **kwargs): # real signature unknown
    pass

def dcopy_index_matrix(*args, **kwargs): # real signature unknown
    pass

def dcopy_index_vector(*args, **kwargs): # real signature unknown
    pass

def dcopy_missing_matrix(*args, **kwargs): # real signature unknown
    pass

def dcopy_missing_vector(*args, **kwargs): # real signature unknown
    pass

def dldl(*args, **kwargs): # real signature unknown
    pass

def dreorder_missing_matrix(*args, **kwargs): # real signature unknown
    pass

def dreorder_missing_vector(*args, **kwargs): # real signature unknown
    pass

def scopy_index_matrix(*args, **kwargs): # real signature unknown
    pass

def scopy_index_vector(*args, **kwargs): # real signature unknown
    pass

def scopy_missing_matrix(*args, **kwargs): # real signature unknown
    pass

def scopy_missing_vector(*args, **kwargs): # real signature unknown
    pass

def sldl(*args, **kwargs): # real signature unknown
    pass

def sreorder_missing_matrix(*args, **kwargs): # real signature unknown
    pass

def sreorder_missing_vector(*args, **kwargs): # real signature unknown
    pass

def zcopy_index_matrix(*args, **kwargs): # real signature unknown
    pass

def zcopy_index_vector(*args, **kwargs): # real signature unknown
    pass

def zcopy_missing_matrix(*args, **kwargs): # real signature unknown
    pass

def zcopy_missing_vector(*args, **kwargs): # real signature unknown
    pass

def zldl(*args, **kwargs): # real signature unknown
    pass

def zreorder_missing_matrix(*args, **kwargs): # real signature unknown
    pass

def zreorder_missing_vector(*args, **kwargs): # real signature unknown
    pass

def _ccompute_coefficients_from_multivariate_pacf(*args, **kwargs): # real signature unknown
    """
    Notes
        -----
    
        This uses the ?trmm BLAS functions which are not available in
        Scipy v0.11.0
    """
    pass

def _cconstrain_sv_less_than_one(*args, **kwargs): # real signature unknown
    """
    Transform arbitrary matrices to matrices with singular values less than
        one.
    
        Corresponds to Lemma 2.2 in Ansley and Kohn (1986). See
        `constrain_stationary_multivariate` for more details.
    """
    pass

def _dcompute_coefficients_from_multivariate_pacf(*args, **kwargs): # real signature unknown
    """
    Notes
        -----
    
        This uses the ?trmm BLAS functions which are not available in
        Scipy v0.11.0
    """
    pass

def _dconstrain_sv_less_than_one(*args, **kwargs): # real signature unknown
    """
    Transform arbitrary matrices to matrices with singular values less than
        one.
    
        Corresponds to Lemma 2.2 in Ansley and Kohn (1986). See
        `constrain_stationary_multivariate` for more details.
    """
    pass

def _scompute_coefficients_from_multivariate_pacf(*args, **kwargs): # real signature unknown
    """
    Notes
        -----
    
        This uses the ?trmm BLAS functions which are not available in
        Scipy v0.11.0
    """
    pass

def _sconstrain_sv_less_than_one(*args, **kwargs): # real signature unknown
    """
    Transform arbitrary matrices to matrices with singular values less than
        one.
    
        Corresponds to Lemma 2.2 in Ansley and Kohn (1986). See
        `constrain_stationary_multivariate` for more details.
    """
    pass

def _zcompute_coefficients_from_multivariate_pacf(*args, **kwargs): # real signature unknown
    """
    Notes
        -----
    
        This uses the ?trmm BLAS functions which are not available in
        Scipy v0.11.0
    """
    pass

def _zconstrain_sv_less_than_one(*args, **kwargs): # real signature unknown
    """
    Transform arbitrary matrices to matrices with singular values less than
        one.
    
        Corresponds to Lemma 2.2 in Ansley and Kohn (1986). See
        `constrain_stationary_multivariate` for more details.
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000020478245D68>'

__pyx_capi__ = {
    '_ccopy_index_cols': None, # (!) real value is '<capsule object "int (__pyx_t_float_complex *, __pyx_t_float_complex *, int *, int, int)" at 0x000002047825D2D0>'
    '_ccopy_index_diagonal': None, # (!) real value is '<capsule object "int (__pyx_t_float_complex *, __pyx_t_float_complex *, int *, int)" at 0x000002047825D090>'
    '_ccopy_index_rows': None, # (!) real value is '<capsule object "int (__pyx_t_float_complex *, __pyx_t_float_complex *, int *, int, int)" at 0x000002047825D210>'
    '_ccopy_index_submatrix': None, # (!) real value is '<capsule object "int (__pyx_t_float_complex *, __pyx_t_float_complex *, int *, int)" at 0x000002047825D150>'
    '_ccopy_missing_cols': None, # (!) real value is '<capsule object "int (__pyx_t_float_complex *, __pyx_t_float_complex *, int *, int, int)" at 0x0000020478202E10>'
    '_ccopy_missing_diagonal': None, # (!) real value is '<capsule object "int (__pyx_t_float_complex *, __pyx_t_float_complex *, int *, int)" at 0x0000020478202BD0>'
    '_ccopy_missing_rows': None, # (!) real value is '<capsule object "int (__pyx_t_float_complex *, __pyx_t_float_complex *, int *, int, int)" at 0x0000020478202D50>'
    '_ccopy_missing_submatrix': None, # (!) real value is '<capsule object "int (__pyx_t_float_complex *, __pyx_t_float_complex *, int *, int)" at 0x0000020478202C90>'
    '_cldl': None, # (!) real value is '<capsule object "int (__pyx_t_float_complex *, int)" at 0x000002047818D240>'
    '_creorder_missing_cols': None, # (!) real value is '<capsule object "int (__pyx_t_float_complex *, int *, int, int)" at 0x0000020478202990>'
    '_creorder_missing_diagonal': None, # (!) real value is '<capsule object "int (__pyx_t_float_complex *, int *, int)" at 0x0000020478202750>'
    '_creorder_missing_rows': None, # (!) real value is '<capsule object "int (__pyx_t_float_complex *, int *, int, int)" at 0x00000204782028D0>'
    '_creorder_missing_submatrix': None, # (!) real value is '<capsule object "int (__pyx_t_float_complex *, int *, int)" at 0x0000020478202810>'
    '_cselect_cov': None, # (!) real value is '<capsule object "int (int, int, int, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *)" at 0x000002047825D510>'
    '_csolve_discrete_lyapunov': None, # (!) real value is '<capsule object "int (__pyx_t_float_complex *, __pyx_t_float_complex *, int, struct __pyx_opt_args_11statsmodels_3tsa_10statespace_6_tools__csolve_discrete_lyapunov *__pyx_optional_args)" at 0x0000020478130CF0>'
    '_dcopy_index_cols': None, # (!) real value is '<capsule object "int (__pyx_t_5numpy_float64_t *, __pyx_t_5numpy_float64_t *, int *, int, int)" at 0x000002047825D2A0>'
    '_dcopy_index_diagonal': None, # (!) real value is '<capsule object "int (__pyx_t_5numpy_float64_t *, __pyx_t_5numpy_float64_t *, int *, int)" at 0x000002047825D060>'
    '_dcopy_index_rows': None, # (!) real value is '<capsule object "int (__pyx_t_5numpy_float64_t *, __pyx_t_5numpy_float64_t *, int *, int, int)" at 0x000002047825D1E0>'
    '_dcopy_index_submatrix': None, # (!) real value is '<capsule object "int (__pyx_t_5numpy_float64_t *, __pyx_t_5numpy_float64_t *, int *, int)" at 0x000002047825D120>'
    '_dcopy_missing_cols': None, # (!) real value is '<capsule object "int (__pyx_t_5numpy_float64_t *, __pyx_t_5numpy_float64_t *, int *, int, int)" at 0x0000020478202DE0>'
    '_dcopy_missing_diagonal': None, # (!) real value is '<capsule object "int (__pyx_t_5numpy_float64_t *, __pyx_t_5numpy_float64_t *, int *, int)" at 0x0000020478202BA0>'
    '_dcopy_missing_rows': None, # (!) real value is '<capsule object "int (__pyx_t_5numpy_float64_t *, __pyx_t_5numpy_float64_t *, int *, int, int)" at 0x0000020478202D20>'
    '_dcopy_missing_submatrix': None, # (!) real value is '<capsule object "int (__pyx_t_5numpy_float64_t *, __pyx_t_5numpy_float64_t *, int *, int)" at 0x0000020478202C60>'
    '_dldl': None, # (!) real value is '<capsule object "int (__pyx_t_5numpy_float64_t *, int)" at 0x000002047818D150>'
    '_dreorder_missing_cols': None, # (!) real value is '<capsule object "int (__pyx_t_5numpy_float64_t *, int *, int, int)" at 0x0000020478202960>'
    '_dreorder_missing_diagonal': None, # (!) real value is '<capsule object "int (__pyx_t_5numpy_float64_t *, int *, int)" at 0x0000020478202720>'
    '_dreorder_missing_rows': None, # (!) real value is '<capsule object "int (__pyx_t_5numpy_float64_t *, int *, int, int)" at 0x00000204782028A0>'
    '_dreorder_missing_submatrix': None, # (!) real value is '<capsule object "int (__pyx_t_5numpy_float64_t *, int *, int)" at 0x00000204782027E0>'
    '_dselect_cov': None, # (!) real value is '<capsule object "int (int, int, int, __pyx_t_5numpy_float64_t *, __pyx_t_5numpy_float64_t *, __pyx_t_5numpy_float64_t *, __pyx_t_5numpy_float64_t *)" at 0x000002047825D4E0>'
    '_dsolve_discrete_lyapunov': None, # (!) real value is '<capsule object "int (__pyx_t_5numpy_float64_t *, __pyx_t_5numpy_float64_t *, int, struct __pyx_opt_args_11statsmodels_3tsa_10statespace_6_tools__dsolve_discrete_lyapunov *__pyx_optional_args)" at 0x0000020478130AB0>'
    '_scopy_index_cols': None, # (!) real value is '<capsule object "int (__pyx_t_5numpy_float32_t *, __pyx_t_5numpy_float32_t *, int *, int, int)" at 0x000002047825D270>'
    '_scopy_index_diagonal': None, # (!) real value is '<capsule object "int (__pyx_t_5numpy_float32_t *, __pyx_t_5numpy_float32_t *, int *, int)" at 0x000002047825D030>'
    '_scopy_index_rows': None, # (!) real value is '<capsule object "int (__pyx_t_5numpy_float32_t *, __pyx_t_5numpy_float32_t *, int *, int, int)" at 0x000002047825D1B0>'
    '_scopy_index_submatrix': None, # (!) real value is '<capsule object "int (__pyx_t_5numpy_float32_t *, __pyx_t_5numpy_float32_t *, int *, int)" at 0x000002047825D0F0>'
    '_scopy_missing_cols': None, # (!) real value is '<capsule object "int (__pyx_t_5numpy_float32_t *, __pyx_t_5numpy_float32_t *, int *, int, int)" at 0x0000020478202DB0>'
    '_scopy_missing_diagonal': None, # (!) real value is '<capsule object "int (__pyx_t_5numpy_float32_t *, __pyx_t_5numpy_float32_t *, int *, int)" at 0x0000020478202B70>'
    '_scopy_missing_rows': None, # (!) real value is '<capsule object "int (__pyx_t_5numpy_float32_t *, __pyx_t_5numpy_float32_t *, int *, int, int)" at 0x0000020478202CF0>'
    '_scopy_missing_submatrix': None, # (!) real value is '<capsule object "int (__pyx_t_5numpy_float32_t *, __pyx_t_5numpy_float32_t *, int *, int)" at 0x0000020478202C30>'
    '_sldl': None, # (!) real value is '<capsule object "int (__pyx_t_5numpy_float32_t *, int)" at 0x000002047818D210>'
    '_sreorder_missing_cols': None, # (!) real value is '<capsule object "int (__pyx_t_5numpy_float32_t *, int *, int, int)" at 0x0000020478202930>'
    '_sreorder_missing_diagonal': None, # (!) real value is '<capsule object "int (__pyx_t_5numpy_float32_t *, int *, int)" at 0x00000204782026F0>'
    '_sreorder_missing_rows': None, # (!) real value is '<capsule object "int (__pyx_t_5numpy_float32_t *, int *, int, int)" at 0x0000020478202870>'
    '_sreorder_missing_submatrix': None, # (!) real value is '<capsule object "int (__pyx_t_5numpy_float32_t *, int *, int)" at 0x00000204782027B0>'
    '_sselect_cov': None, # (!) real value is '<capsule object "int (int, int, int, __pyx_t_5numpy_float32_t *, __pyx_t_5numpy_float32_t *, __pyx_t_5numpy_float32_t *, __pyx_t_5numpy_float32_t *)" at 0x000002047825D4B0>'
    '_ssolve_discrete_lyapunov': None, # (!) real value is '<capsule object "int (__pyx_t_5numpy_float32_t *, __pyx_t_5numpy_float32_t *, int, struct __pyx_opt_args_11statsmodels_3tsa_10statespace_6_tools__ssolve_discrete_lyapunov *__pyx_optional_args)" at 0x0000020478130A80>'
    '_zcopy_index_cols': None, # (!) real value is '<capsule object "int (__pyx_t_double_complex *, __pyx_t_double_complex *, int *, int, int)" at 0x000002047825D300>'
    '_zcopy_index_diagonal': None, # (!) real value is '<capsule object "int (__pyx_t_double_complex *, __pyx_t_double_complex *, int *, int)" at 0x000002047825D0C0>'
    '_zcopy_index_rows': None, # (!) real value is '<capsule object "int (__pyx_t_double_complex *, __pyx_t_double_complex *, int *, int, int)" at 0x000002047825D240>'
    '_zcopy_index_submatrix': None, # (!) real value is '<capsule object "int (__pyx_t_double_complex *, __pyx_t_double_complex *, int *, int)" at 0x000002047825D180>'
    '_zcopy_missing_cols': None, # (!) real value is '<capsule object "int (__pyx_t_double_complex *, __pyx_t_double_complex *, int *, int, int)" at 0x0000020478202E40>'
    '_zcopy_missing_diagonal': None, # (!) real value is '<capsule object "int (__pyx_t_double_complex *, __pyx_t_double_complex *, int *, int)" at 0x0000020478202C00>'
    '_zcopy_missing_rows': None, # (!) real value is '<capsule object "int (__pyx_t_double_complex *, __pyx_t_double_complex *, int *, int, int)" at 0x0000020478202D80>'
    '_zcopy_missing_submatrix': None, # (!) real value is '<capsule object "int (__pyx_t_double_complex *, __pyx_t_double_complex *, int *, int)" at 0x0000020478202CC0>'
    '_zldl': None, # (!) real value is '<capsule object "int (__pyx_t_double_complex *, int)" at 0x00000204782025D0>'
    '_zreorder_missing_cols': None, # (!) real value is '<capsule object "int (__pyx_t_double_complex *, int *, int, int)" at 0x00000204782029C0>'
    '_zreorder_missing_diagonal': None, # (!) real value is '<capsule object "int (__pyx_t_double_complex *, int *, int)" at 0x0000020478202780>'
    '_zreorder_missing_rows': None, # (!) real value is '<capsule object "int (__pyx_t_double_complex *, int *, int, int)" at 0x0000020478202900>'
    '_zreorder_missing_submatrix': None, # (!) real value is '<capsule object "int (__pyx_t_double_complex *, int *, int)" at 0x0000020478202840>'
    '_zselect_cov': None, # (!) real value is '<capsule object "int (int, int, int, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *)" at 0x000002047825D540>'
    '_zsolve_discrete_lyapunov': None, # (!) real value is '<capsule object "int (__pyx_t_double_complex *, __pyx_t_double_complex *, int, struct __pyx_opt_args_11statsmodels_3tsa_10statespace_6_tools__zsolve_discrete_lyapunov *__pyx_optional_args)" at 0x0000020478130D20>'
    'ccopy_index_matrix': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice, __Pyx_memviewslice, __Pyx_memviewslice, int, int, int, int __pyx_skip_dispatch)" at 0x000002047825D390>'
    'ccopy_index_vector': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice, __Pyx_memviewslice, __Pyx_memviewslice, int __pyx_skip_dispatch)" at 0x000002047825D450>'
    'ccopy_missing_matrix': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice, __Pyx_memviewslice, __Pyx_memviewslice, int, int, int, int __pyx_skip_dispatch)" at 0x0000020478202ED0>'
    'ccopy_missing_vector': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice, __Pyx_memviewslice, __Pyx_memviewslice, int __pyx_skip_dispatch)" at 0x0000020478202F90>'
    'cldl': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice, int __pyx_skip_dispatch)" at 0x0000020478202690>'
    'creorder_missing_matrix': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice, __Pyx_memviewslice, int, int, int, int __pyx_skip_dispatch)" at 0x0000020478202A50>'
    'creorder_missing_vector': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice, __Pyx_memviewslice, int __pyx_skip_dispatch)" at 0x0000020478202B10>'
    'dcopy_index_matrix': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice, __Pyx_memviewslice, __Pyx_memviewslice, int, int, int, int __pyx_skip_dispatch)" at 0x000002047825D360>'
    'dcopy_index_vector': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice, __Pyx_memviewslice, __Pyx_memviewslice, int __pyx_skip_dispatch)" at 0x000002047825D420>'
    'dcopy_missing_matrix': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice, __Pyx_memviewslice, __Pyx_memviewslice, int, int, int, int __pyx_skip_dispatch)" at 0x0000020478202EA0>'
    'dcopy_missing_vector': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice, __Pyx_memviewslice, __Pyx_memviewslice, int __pyx_skip_dispatch)" at 0x0000020478202F60>'
    'dldl': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice, int __pyx_skip_dispatch)" at 0x0000020478202660>'
    'dreorder_missing_matrix': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice, __Pyx_memviewslice, int, int, int, int __pyx_skip_dispatch)" at 0x0000020478202A20>'
    'dreorder_missing_vector': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice, __Pyx_memviewslice, int __pyx_skip_dispatch)" at 0x0000020478202AE0>'
    'scopy_index_matrix': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice, __Pyx_memviewslice, __Pyx_memviewslice, int, int, int, int __pyx_skip_dispatch)" at 0x000002047825D330>'
    'scopy_index_vector': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice, __Pyx_memviewslice, __Pyx_memviewslice, int __pyx_skip_dispatch)" at 0x000002047825D3F0>'
    'scopy_missing_matrix': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice, __Pyx_memviewslice, __Pyx_memviewslice, int, int, int, int __pyx_skip_dispatch)" at 0x0000020478202E70>'
    'scopy_missing_vector': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice, __Pyx_memviewslice, __Pyx_memviewslice, int __pyx_skip_dispatch)" at 0x0000020478202F30>'
    'sldl': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice, int __pyx_skip_dispatch)" at 0x0000020478202630>'
    'sreorder_missing_matrix': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice, __Pyx_memviewslice, int, int, int, int __pyx_skip_dispatch)" at 0x00000204782029F0>'
    'sreorder_missing_vector': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice, __Pyx_memviewslice, int __pyx_skip_dispatch)" at 0x0000020478202AB0>'
    'validate_matrix_shape': None, # (!) real value is '<capsule object "PyObject *(PyObject *, Py_ssize_t *, int, int, struct __pyx_opt_args_11statsmodels_3tsa_10statespace_6_tools_validate_matrix_shape *__pyx_optional_args)" at 0x00000204781308A0>'
    'validate_vector_shape': None, # (!) real value is '<capsule object "PyObject *(PyObject *, Py_ssize_t *, int, struct __pyx_opt_args_11statsmodels_3tsa_10statespace_6_tools_validate_vector_shape *__pyx_optional_args)" at 0x0000020478130A50>'
    'zcopy_index_matrix': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice, __Pyx_memviewslice, __Pyx_memviewslice, int, int, int, int __pyx_skip_dispatch)" at 0x000002047825D3C0>'
    'zcopy_index_vector': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice, __Pyx_memviewslice, __Pyx_memviewslice, int __pyx_skip_dispatch)" at 0x000002047825D480>'
    'zcopy_missing_matrix': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice, __Pyx_memviewslice, __Pyx_memviewslice, int, int, int, int __pyx_skip_dispatch)" at 0x0000020478202F00>'
    'zcopy_missing_vector': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice, __Pyx_memviewslice, __Pyx_memviewslice, int __pyx_skip_dispatch)" at 0x0000020478202FC0>'
    'zldl': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice, int __pyx_skip_dispatch)" at 0x00000204782026C0>'
    'zreorder_missing_matrix': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice, __Pyx_memviewslice, int, int, int, int __pyx_skip_dispatch)" at 0x0000020478202A80>'
    'zreorder_missing_vector': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice, __Pyx_memviewslice, int __pyx_skip_dispatch)" at 0x0000020478202B40>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='statsmodels.tsa.statespace._tools', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000020478245D68>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\statsmodels\\\\tsa\\\\statespace\\\\_tools.cp37-win_amd64.pyd')"

__test__ = {}

