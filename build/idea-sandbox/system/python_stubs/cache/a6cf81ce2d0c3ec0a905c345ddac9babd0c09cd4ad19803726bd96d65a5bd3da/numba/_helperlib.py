# encoding: utf-8
# module numba._helperlib
# from C:\Users\Doly\Anaconda3\lib\site-packages\numba\_helperlib.cp37-win_amd64.pyd
# by generator 1.147
""" No docs """
# no imports

# Variables with simple values

long_max = 2147483647
long_min = -2147483648

py_buffer_size = 80

py_gil_state_size = 4

py_unicode_1byte_kind = 1

py_unicode_2byte_kind = 2

py_unicode_4byte_kind = 4

py_unicode_wchar_kind = 0

# functions

def rnd_get_np_state_ptr(*args, **kwargs): # real signature unknown
    pass

def rnd_get_py_state_ptr(*args, **kwargs): # real signature unknown
    pass

def rnd_get_state(*args, **kwargs): # real signature unknown
    pass

def rnd_seed(*args, **kwargs): # real signature unknown
    pass

def rnd_set_state(*args, **kwargs): # real signature unknown
    pass

def rnd_shuffle(*args, **kwargs): # real signature unknown
    pass

def _import_cython_function(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

c_helpers = {
    'acos': 140716350964016,
    'acosf': 140716350964000,
    'acosh': 140716350963920,
    'acoshf': 140716350963904,
    'adapt_buffer': 140716350968784,
    'adapt_ndarray': 140716350968992,
    'asin': 140716350964048,
    'asinf': 140716350964032,
    'asinh': 140716350963952,
    'asinhf': 140716350963936,
    'atan': 140716350963984,
    'atan2': 140716350963408,
    'atan2_fixed': 140716350963424,
    'atan2f': 140716350963392,
    'atanf': 140716350963968,
    'atanh': 140716350963888,
    'atanhf': 140716350963872,
    'attempt_nocopy_reshape': 140716350967792,
    'ceil': 140716350963680,
    'ceilf': 140716350963664,
    'complex_adaptor': 140716350969680,
    'cos': 140716350964208,
    'cosf': 140716350964192,
    'cosh': 140716350964112,
    'coshf': 140716350964096,
    'cpow': 140716350970432,
    'cpowf': 140716350970176,
    'create_np_datetime': 140716350967152,
    'create_np_timedelta': 140716350967072,
    'dict_delitem': 140716350929136,
    'dict_dump': 140716350928272,
    'dict_free': 140716350932432,
    'dict_insert': 140716350930432,
    'dict_insert_ez': 140716350927888,
    'dict_iter': 140716350928208,
    'dict_iter_next': 140716350928000,
    'dict_iter_sizeof': 140716350928256,
    'dict_length': 140716350932416,
    'dict_lookup': 140716350931248,
    'dict_new_minsize': 140716350927776,
    'dict_popitem': 140716350928736,
    'dict_set_method_table': 140716350927728,
    'do_raise': 140716350964688,
    'erf': 140716350970096,
    'erfc': 140716350970064,
    'erfcf': 140716350970048,
    'erff': 140716350970080,
    'exp': 140716350963856,
    'expf': 140716350963840,
    'expm1': 140716350963824,
    'expm1f': 140716350963808,
    'extract_np_datetime': 140716350967328,
    'extract_np_timedelta': 140716350967232,
    'extract_record_data': 140716350969552,
    'extract_unicode': 140716350964272,
    'ez_cgeev': 140716350949696,
    'ez_gelsd': 140716350938528,
    'ez_geqrf': 140716350942816,
    'ez_gesdd': 140716350943952,
    'ez_rgeev': 140716350950960,
    'ez_xxgetri': 140716350952720,
    'ez_xxgqr': 140716350941632,
    'ez_xxxevd': 140716350946864,
    'fabs': 140716350963760,
    'fabsf': 140716350963728,
    'fatal_error': 140716350966016,
    'fixed_fmod': 140716350971232,
    'fixed_fmodf': 140716350971168,
    'floor': 140716350963712,
    'floorf': 140716350963696,
    'fmod': 140716350963456,
    'fmodf': 140716350963440,
    'fptoui': 140716350967056,
    'fptouif': 140716350967040,
    'frexp': 140716350970928,
    'frexpf': 140716350970784,
    'gamma': 140716350970160,
    'gammaf': 140716350970144,
    'gdb_breakpoint': 140716350964256,
    'get_buffer': 140716350968960,
    'get_np_random_state': 140716350936320,
    'get_py_random_state': 140716350936384,
    'get_pyobject_private_data': 140716350966560,
    'gil_ensure': 140716350967008,
    'gil_release': 140716350966992,
    'ldexp': 140716350970688,
    'ldexpf': 140716350970576,
    'lgamma': 140716350970128,
    'lgammaf': 140716350970112,
    'log': 140716350963648,
    'log10': 140716350963616,
    'log10f': 140716350963600,
    'log1p': 140716350963584,
    'log1pf': 140716350963568,
    'logf': 140716350963632,
    'ndarray_new': 140716350968688,
    'poisson_ptrs': 140716350933376,
    'pow': 140716350963488,
    'powf': 140716350963472,
    'py_type': 140716350966976,
    'recreate_record': 140716350969232,
    'release_buffer': 140716350968768,
    'reset_pyobject_private_data': 140716350966416,
    'rnd_init': 140716350937616,
    'rnd_shuffle': 140716350937712,
    'round': 140716350963552,
    'roundf': 140716350963536,
    'sdiv': 140716350971120,
    'set_fnclex': 140716350971152,
    'set_pyobject_private_data': 140716350966736,
    'signbit': 140716350970016,
    'signbitf': 140716350970032,
    'sin': 140716350964240,
    'sinf': 140716350964224,
    'sinh': 140716350964144,
    'sinhf': 140716350964128,
    'sqrt': 140716350963792,
    'sqrtf': 140716350963776,
    'srem': 140716350971056,
    'tan': 140716350964176,
    'tanf': 140716350964160,
    'tanh': 140716350964080,
    'tanhf': 140716350964064,
    'test_dict': 140716350924176,
    'trunc': 140716350963520,
    'truncf': 140716350963504,
    'udiv': 140716350971088,
    'unpack_slice': 140716350966064,
    'unpickle': 140716350964480,
    'urem': 140716350971024,
    'xgesv': 140716350937920,
    'xxdot': 140716350960288,
    'xxgemm': 140716350958976,
    'xxgemv': 140716350959664,
    'xxgetrf': 140716350953680,
    'xxnrm2': 140716350958400,
    'xxpotrf': 140716350952176,
}

npymath_exports = {
    'npy_exp2': 140716350902800,
    'npy_exp2f': 140716350903328,
    'npy_log2': 140716350902816,
    'npy_log2f': 140716350903344,
    'npy_logaddexp': 140716350904160,
    'npy_logaddexp2': 140716350904320,
    'npy_logaddexp2f': 140716350904928,
    'npy_logaddexpf': 140716350904784,
    'npy_modf': 140716350902864,
    'npy_modff': 140716350903456,
    'npy_nextafter': 140716350906224,
    'npy_nextafterf': 140716350906528,
    'npy_spacing': 140716350906240,
    'npy_spacingf': 140716350906544,
}

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001A0D9A01898>'

__spec__ = None # (!) real value is "ModuleSpec(name='numba._helperlib', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001A0D9A01898>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\numba\\\\_helperlib.cp37-win_amd64.pyd')"

