# encoding: utf-8
# module numba.runtime._nrt_python
# from C:\Users\Doly\Anaconda3\lib\site-packages\numba\runtime\_nrt_python.cp37-win_amd64.pyd
# by generator 1.147
""" No docs """
# no imports

# functions

def meminfo_alloc(*args, **kwargs): # real signature unknown
    pass

def meminfo_alloc_safe(*args, **kwargs): # real signature unknown
    pass

def meminfo_new(*args, **kwargs): # real signature unknown
    pass

def memsys_get_stats_alloc(*args, **kwargs): # real signature unknown
    pass

def memsys_get_stats_free(*args, **kwargs): # real signature unknown
    pass

def memsys_get_stats_mi_alloc(*args, **kwargs): # real signature unknown
    pass

def memsys_get_stats_mi_free(*args, **kwargs): # real signature unknown
    pass

def memsys_set_atomic_cas(*args, **kwargs): # real signature unknown
    pass

def memsys_set_atomic_inc_dec(*args, **kwargs): # real signature unknown
    pass

def memsys_shutdown(*args, **kwargs): # real signature unknown
    pass

def memsys_use_cpython_allocator(*args, **kwargs): # real signature unknown
    pass

# classes

class _MemInfo(object):
    # no doc
    def acquire(self, *args, **kwargs): # real signature unknown
        """ Increment the reference count """
        pass

    def release(self, *args, **kwargs): # real signature unknown
        """ Decrement the reference count """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the data pointer as an integer"""

    refcount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the refcount"""



# variables with complex values

c_helpers = {
    'Allocate': 140716766936400,
    'Free': 140716766936496,
    'MemInfo_alloc': 140716766935680,
    'MemInfo_alloc_aligned': 140716766937376,
    'MemInfo_alloc_dtor_safe': 140716766936240,
    'MemInfo_alloc_safe': 140716766936544,
    'MemInfo_alloc_safe_aligned': 140716766936976,
    'MemInfo_call_dtor': 140716766936656,
    'MemInfo_data': 140716766936224,
    'MemInfo_new_varsize': 140716766935904,
    'MemInfo_new_varsize_dtor': 140716766936448,
    'MemInfo_release': 140716766936752,
    'MemInfo_varsize_alloc': 140716766936064,
    'MemInfo_varsize_free': 140716766937216,
    'MemInfo_varsize_realloc': 140716766936560,
    'adapt_buffer_from_python': 140716766931840,
    'adapt_ndarray_from_python': 140716766932912,
    'adapt_ndarray_to_python': 140716766932048,
    'meminfo_as_pyobject': 140716766933280,
    'meminfo_from_pyobject': 140716766933232,
    'meminfo_new_from_pyobject': 140716766934000,
}

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000222DA1367B8>'

__spec__ = None # (!) real value is "ModuleSpec(name='numba.runtime._nrt_python', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000222DA1367B8>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\numba\\\\runtime\\\\_nrt_python.cp37-win_amd64.pyd')"

