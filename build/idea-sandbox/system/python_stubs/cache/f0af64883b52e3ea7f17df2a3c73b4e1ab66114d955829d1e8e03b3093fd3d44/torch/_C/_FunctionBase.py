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

class _FunctionBase(object):
    # no doc
    @classmethod
    def apply(cls, *args, **kwargs): # real signature unknown
        pass

    def register_hook(self, *args, **kwargs): # real signature unknown
        pass

    def _do_backward(self, *args, **kwargs): # real signature unknown
        pass

    def _do_forward(self, *args, **kwargs): # real signature unknown
        pass

    def _register_hook_dict(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    dirty_tensors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    metadata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    needs_input_grad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    next_functions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    non_differentiable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    requires_grad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    saved_tensors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    saved_variables = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    to_save = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



