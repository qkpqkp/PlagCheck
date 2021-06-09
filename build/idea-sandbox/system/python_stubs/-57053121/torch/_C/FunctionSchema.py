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


class FunctionSchema(__pybind11_builtins.pybind11_object):
    # no doc
    def is_backward_compatible_with(self, arg0): # real signature unknown; restored from __doc__
        """ is_backward_compatible_with(self: torch._C.FunctionSchema, arg0: torch._C.FunctionSchema) -> bool """
        return False

    def __eq__(self, arg0): # real signature unknown; restored from __doc__
        """ __eq__(self: torch._C.FunctionSchema, arg0: torch._C.FunctionSchema) -> bool """
        return False

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ __str__(self: torch._C.FunctionSchema) -> str """
        return ""

    arguments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    overload_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    returns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



