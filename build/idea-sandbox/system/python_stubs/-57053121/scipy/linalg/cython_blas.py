# encoding: utf-8
# module scipy.linalg.cython_blas
# from C:\Users\Doly\Anaconda3\lib\site-packages\scipy\linalg\cython_blas.cp37-win_amd64.pyd
# by generator 1.147
"""
BLAS Functions for Cython
=========================

Usable from Cython via::

    cimport scipy.linalg.cython_blas

These wrappers do not check for alignment of arrays.
Alignment should be checked before these wrappers are used.

Raw function pointers (Fortran-style pointer arguments):

- caxpy
- ccopy
- cdotc
- cdotu
- cgbmv
- cgemm
- cgemv
- cgerc
- cgeru
- chbmv
- chemm
- chemv
- cher
- cher2
- cher2k
- cherk
- chpmv
- chpr
- chpr2
- crotg
- cscal
- csrot
- csscal
- cswap
- csymm
- csyr2k
- csyrk
- ctbmv
- ctbsv
- ctpmv
- ctpsv
- ctrmm
- ctrmv
- ctrsm
- ctrsv
- dasum
- daxpy
- dcabs1
- dcopy
- ddot
- dgbmv
- dgemm
- dgemv
- dger
- dnrm2
- drot
- drotg
- drotm
- drotmg
- dsbmv
- dscal
- dsdot
- dspmv
- dspr
- dspr2
- dswap
- dsymm
- dsymv
- dsyr
- dsyr2
- dsyr2k
- dsyrk
- dtbmv
- dtbsv
- dtpmv
- dtpsv
- dtrmm
- dtrmv
- dtrsm
- dtrsv
- dzasum
- dznrm2
- icamax
- idamax
- isamax
- izamax
- lsame
- sasum
- saxpy
- scasum
- scnrm2
- scopy
- sdot
- sdsdot
- sgbmv
- sgemm
- sgemv
- sger
- snrm2
- srot
- srotg
- srotm
- srotmg
- ssbmv
- sscal
- sspmv
- sspr
- sspr2
- sswap
- ssymm
- ssymv
- ssyr
- ssyr2
- ssyr2k
- ssyrk
- stbmv
- stbsv
- stpmv
- stpsv
- strmm
- strmv
- strsm
- strsv
- zaxpy
- zcopy
- zdotc
- zdotu
- zdrot
- zdscal
- zgbmv
- zgemm
- zgemv
- zgerc
- zgeru
- zhbmv
- zhemm
- zhemv
- zher
- zher2
- zher2k
- zherk
- zhpmv
- zhpr
- zhpr2
- zrotg
- zscal
- zswap
- zsymm
- zsyr2k
- zsyrk
- ztbmv
- ztbsv
- ztpmv
- ztpsv
- ztrmm
- ztrmv
- ztrsm
- ztrsv
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

# functions

def _test_cdotc(*args, **kwargs): # real signature unknown
    pass

def _test_cdotu(*args, **kwargs): # real signature unknown
    pass

def _test_dasum(*args, **kwargs): # real signature unknown
    pass

def _test_ddot(*args, **kwargs): # real signature unknown
    pass

def _test_dgemm(*args, **kwargs): # real signature unknown
    pass

def _test_dnrm2(*args, **kwargs): # real signature unknown
    pass

def _test_dzasum(*args, **kwargs): # real signature unknown
    pass

def _test_dznrm2(*args, **kwargs): # real signature unknown
    pass

def _test_icamax(*args, **kwargs): # real signature unknown
    pass

def _test_idamax(*args, **kwargs): # real signature unknown
    pass

def _test_isamax(*args, **kwargs): # real signature unknown
    pass

def _test_izamax(*args, **kwargs): # real signature unknown
    pass

def _test_sasum(*args, **kwargs): # real signature unknown
    pass

def _test_scasum(*args, **kwargs): # real signature unknown
    pass

def _test_scnrm2(*args, **kwargs): # real signature unknown
    pass

def _test_sdot(*args, **kwargs): # real signature unknown
    pass

def _test_snrm2(*args, **kwargs): # real signature unknown
    pass

def _test_zdotc(*args, **kwargs): # real signature unknown
    pass

def _test_zdotu(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001C0168DB5C0>'

__pyx_capi__ = {
    'caxpy': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x000001C01687D870>'
    'ccopy': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x000001C01687D8A0>'
    'cdotc': None, # (!) real value is '<capsule object "__pyx_t_float_complex (int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x000001C01687D8D0>'
    'cdotu': None, # (!) real value is '<capsule object "__pyx_t_float_complex (int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x000001C01687D900>'
    'cgbmv': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x000001C01687D930>'
    'cgemm': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x000001C01687D960>'
    'cgemv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x000001C01687D990>'
    'cgerc': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x000001C01687D9C0>'
    'cgeru': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x000001C01687D9F0>'
    'chbmv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x000001C01687DA20>'
    'chemm': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x000001C01687DA50>'
    'chemv': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x000001C01687DA80>'
    'cher': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x000001C01687DAB0>'
    'cher2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x000001C01687DAE0>'
    'cher2k': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_float_complex *, int *)" at 0x000001C01687DB10>'
    'cherk': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_float_complex *, int *)" at 0x000001C01687DB40>'
    'chpmv': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x000001C01687DB70>'
    'chpr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *)" at 0x000001C01687DBA0>'
    'chpr2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *)" at 0x000001C01687DBD0>'
    'crotg': None, # (!) real value is '<capsule object "void (__pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_float_complex *)" at 0x000001C01687DC00>'
    'cscal': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x000001C01687DC30>'
    'csrot': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *)" at 0x000001C01687DC60>'
    'csscal': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_float_complex *, int *)" at 0x000001C01687DC90>'
    'cswap': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x000001C01687DCC0>'
    'csymm': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x000001C01687DCF0>'
    'csyr2k': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x000001C01687DD20>'
    'csyrk': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x000001C01687DD50>'
    'ctbmv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x000001C01687DD80>'
    'ctbsv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x000001C01687DDB0>'
    'ctpmv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x000001C01687DDE0>'
    'ctpsv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x000001C01687DE10>'
    'ctrmm': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x000001C01687DE40>'
    'ctrmv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x000001C01687DE70>'
    'ctrsm': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x000001C01687DEA0>'
    'ctrsv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x000001C01687DED0>'
    'dasum': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_11cython_blas_d (int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x000001C01687DF00>'
    'daxpy': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x000001C01687DF30>'
    'dcabs1': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_11cython_blas_d (__pyx_t_double_complex *)" at 0x000001C01687DF60>'
    'dcopy': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x000001C01687DF90>'
    'ddot': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_11cython_blas_d (int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x000001C01687DFC0>'
    'dgbmv': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x000001C0168DF030>'
    'dgemm': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x000001C0168DF060>'
    'dgemv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x000001C0168DF090>'
    'dger': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x000001C0168DF0C0>'
    'dnrm2': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_11cython_blas_d (int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x000001C0168DF0F0>'
    'drot': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *)" at 0x000001C0168DF120>'
    'drotg': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *)" at 0x000001C0168DF150>'
    'drotm': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *)" at 0x000001C0168DF180>'
    'drotmg': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *)" at 0x000001C0168DF1B0>'
    'dsbmv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x000001C0168DF1E0>'
    'dscal': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x000001C0168DF210>'
    'dsdot': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_11cython_blas_d (int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x000001C0168DF240>'
    'dspmv': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x000001C0168DF270>'
    'dspr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *)" at 0x000001C0168DF2A0>'
    'dspr2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *)" at 0x000001C0168DF2D0>'
    'dswap': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x000001C0168DF300>'
    'dsymm': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x000001C0168DF330>'
    'dsymv': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x000001C0168DF360>'
    'dsyr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x000001C0168DF390>'
    'dsyr2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x000001C0168DF3C0>'
    'dsyr2k': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x000001C0168DF3F0>'
    'dsyrk': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x000001C0168DF420>'
    'dtbmv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x000001C0168DF450>'
    'dtbsv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x000001C0168DF480>'
    'dtpmv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x000001C0168DF4B0>'
    'dtpsv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x000001C0168DF4E0>'
    'dtrmm': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x000001C0168DF510>'
    'dtrmv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x000001C0168DF540>'
    'dtrsm': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x000001C0168DF570>'
    'dtrsv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x000001C0168DF5A0>'
    'dzasum': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_11cython_blas_d (int *, __pyx_t_double_complex *, int *)" at 0x000001C0168DF5D0>'
    'dznrm2': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_11cython_blas_d (int *, __pyx_t_double_complex *, int *)" at 0x000001C0168DF600>'
    'icamax': None, # (!) real value is '<capsule object "int (int *, __pyx_t_float_complex *, int *)" at 0x000001C0168DF630>'
    'idamax': None, # (!) real value is '<capsule object "int (int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x000001C0168DF660>'
    'isamax': None, # (!) real value is '<capsule object "int (int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x000001C0168DF690>'
    'izamax': None, # (!) real value is '<capsule object "int (int *, __pyx_t_double_complex *, int *)" at 0x000001C0168DF6C0>'
    'lsame': None, # (!) real value is '<capsule object "int (char *, char *)" at 0x000001C0168DF6F0>'
    'sasum': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_11cython_blas_s (int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x000001C0168DF720>'
    'saxpy': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x000001C0168DF750>'
    'scasum': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_11cython_blas_s (int *, __pyx_t_float_complex *, int *)" at 0x000001C0168DF780>'
    'scnrm2': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_11cython_blas_s (int *, __pyx_t_float_complex *, int *)" at 0x000001C0168DF7B0>'
    'scopy': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x000001C0168DF7E0>'
    'sdot': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_11cython_blas_s (int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x000001C0168DF810>'
    'sdsdot': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_11cython_blas_s (int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x000001C0168DF840>'
    'sgbmv': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x000001C0168DF870>'
    'sgemm': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x000001C0168DF8A0>'
    'sgemv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x000001C0168DF8D0>'
    'sger': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x000001C0168DF900>'
    'snrm2': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_11cython_blas_s (int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x000001C0168DF930>'
    'srot': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *)" at 0x000001C0168DF960>'
    'srotg': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *)" at 0x000001C0168DF990>'
    'srotm': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *)" at 0x000001C0168DF9C0>'
    'srotmg': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *)" at 0x000001C0168DF9F0>'
    'ssbmv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x000001C0168DFA20>'
    'sscal': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x000001C0168DFA50>'
    'sspmv': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x000001C0168DFA80>'
    'sspr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *)" at 0x000001C0168DFAB0>'
    'sspr2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *)" at 0x000001C0168DFAE0>'
    'sswap': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x000001C0168DFB10>'
    'ssymm': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x000001C0168DFB40>'
    'ssymv': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x000001C0168DFB70>'
    'ssyr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x000001C0168DFBA0>'
    'ssyr2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x000001C0168DFBD0>'
    'ssyr2k': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x000001C0168DFC00>'
    'ssyrk': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x000001C0168DFC30>'
    'stbmv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x000001C0168DFC60>'
    'stbsv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x000001C0168DFC90>'
    'stpmv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x000001C0168DFCC0>'
    'stpsv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x000001C0168DFCF0>'
    'strmm': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x000001C0168DFD20>'
    'strmv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x000001C0168DFD50>'
    'strsm': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x000001C0168DFD80>'
    'strsv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x000001C0168DFDB0>'
    'zaxpy': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x000001C0168DFDE0>'
    'zcopy': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x000001C0168DFE10>'
    'zdotc': None, # (!) real value is '<capsule object "__pyx_t_double_complex (int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x000001C0168DFE40>'
    'zdotu': None, # (!) real value is '<capsule object "__pyx_t_double_complex (int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x000001C0168DFE70>'
    'zdrot': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *)" at 0x000001C0168DFEA0>'
    'zdscal': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_double_complex *, int *)" at 0x000001C0168DFED0>'
    'zgbmv': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x000001C0168DFF00>'
    'zgemm': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x000001C0168DFF30>'
    'zgemv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x000001C0168DFF60>'
    'zgerc': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x000001C0168DFF90>'
    'zgeru': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x000001C0168DFFC0>'
    'zhbmv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x000001C0168E0030>'
    'zhemm': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x000001C0168E0060>'
    'zhemv': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x000001C0168E0090>'
    'zher': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x000001C0168E00C0>'
    'zher2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x000001C0168E00F0>'
    'zher2k': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_double_complex *, int *)" at 0x000001C0168E0120>'
    'zherk': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_double_complex *, int *)" at 0x000001C0168E0150>'
    'zhpmv': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x000001C0168E0180>'
    'zhpr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *)" at 0x000001C0168E01B0>'
    'zhpr2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *)" at 0x000001C0168E01E0>'
    'zrotg': None, # (!) real value is '<capsule object "void (__pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_double_complex *)" at 0x000001C0168E0210>'
    'zscal': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x000001C0168E0240>'
    'zswap': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x000001C0168E0270>'
    'zsymm': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x000001C0168E02A0>'
    'zsyr2k': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x000001C0168E02D0>'
    'zsyrk': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x000001C0168E0300>'
    'ztbmv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x000001C0168E0330>'
    'ztbsv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x000001C0168E0360>'
    'ztpmv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x000001C0168E0390>'
    'ztpsv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x000001C0168E03C0>'
    'ztrmm': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x000001C0168E03F0>'
    'ztrmv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x000001C0168E0420>'
    'ztrsm': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x000001C0168E0450>'
    'ztrsv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x000001C0168E0480>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.linalg.cython_blas', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001C0168DB5C0>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\scipy\\\\linalg\\\\cython_blas.cp37-win_amd64.pyd')"

__test__ = {}

