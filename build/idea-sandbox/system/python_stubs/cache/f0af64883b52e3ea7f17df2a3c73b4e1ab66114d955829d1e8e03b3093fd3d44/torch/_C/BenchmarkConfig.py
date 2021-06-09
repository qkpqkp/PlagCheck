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


class BenchmarkConfig(__pybind11_builtins.pybind11_object):
    # no doc
    def __init__(self): # real signature unknown; restored from __doc__
        """ __init__(self: torch._C.BenchmarkConfig) -> None """
        pass

    num_calling_threads = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_iters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_warmup_iters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_worker_threads = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



