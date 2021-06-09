# encoding: utf-8
# module torch._C
# from C:\Users\Doly\Anaconda3\lib\site-packages\torch\_C.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import torch._C._onnx as _onnx # <module 'torch._C._onnx'>
import torch._C._jit_tree_views as _jit_tree_views # <module 'torch._C._jit_tree_views'>
import torch._C._nn as _nn # <module 'torch._C._nn'>
import torch._C.cpp as cpp # <module 'torch._C.cpp'>
import torch._C._functions as _functions # <module 'torch._C._functions'>
import pybind11_builtins as __pybind11_builtins


from .object import object

class CharStorageBase(object):
    # no doc
    def copy_(self, *args, **kwargs): # real signature unknown
        pass

    def data_ptr(self, *args, **kwargs): # real signature unknown
        pass

    def element_size(self, *args, **kwargs): # real signature unknown
        pass

    def fill_(self, *args, **kwargs): # real signature unknown
        pass

    def from_buffer(self, *args, **kwargs): # real signature unknown
        pass

    def from_file(self, filename, shared=False, size=0): # real signature unknown; restored from __doc__
        """
        from_file(filename, shared=False, size=0) -> Storage
        
        If `shared` is `True`, then memory is shared between all processes.
        All changes are written to the file. If `shared` is `False`, then the changes on
        the storage do not affect the file.
        
        `size` is the number of elements in the storage. If `shared` is `False`,
        then the file must contain at least `size * sizeof(Type)` bytes
        (`Type` is the type of storage). If `shared` is `True` the file will be
        created if needed.
        
        Args:
            filename (str): file name to map
            shared (bool): whether to share memory
            size (int): number of elements in the storage
        """
        pass

    def is_pinned(self, *args, **kwargs): # real signature unknown
        pass

    def is_shared(self, *args, **kwargs): # real signature unknown
        pass

    def new(self, *args, **kwargs): # real signature unknown
        pass

    def resize_(self, *args, **kwargs): # real signature unknown
        pass

    def size(self, *args, **kwargs): # real signature unknown
        pass

    def _expired(self, *args, **kwargs): # real signature unknown
        pass

    def _free_weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def _get_shared_fd(self, *args, **kwargs): # real signature unknown
        pass

    def _new_shared_fd(self, *args, **kwargs): # real signature unknown
        pass

    def _new_shared_filename(self, *args, **kwargs): # real signature unknown
        pass

    def _new_using_fd(self, *args, **kwargs): # real signature unknown
        pass

    def _new_using_filename(self, *args, **kwargs): # real signature unknown
        pass

    def _new_with_file(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def _new_with_weak_ptr(cls, *args, **kwargs): # real signature unknown
        pass

    def _set_cdata(self, *args, **kwargs): # real signature unknown
        pass

    def _set_from_file(self, *args, **kwargs): # real signature unknown
        pass

    def _shared_decref(self, *args, **kwargs): # real signature unknown
        pass

    def _shared_incref(self, *args, **kwargs): # real signature unknown
        pass

    def _share_fd_(self, *args, **kwargs): # real signature unknown
        pass

    def _share_filename_(self, *args, **kwargs): # real signature unknown
        pass

    def _weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def _write_file(self, *args, **kwargs): # real signature unknown
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    device = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dtype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _cdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



