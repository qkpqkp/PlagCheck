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


from .LoggerBase import LoggerBase

class LockingLogger(LoggerBase):
    # no doc
    def get_counter_val(self, arg0): # real signature unknown; restored from __doc__
        """ get_counter_val(self: torch._C.LockingLogger, arg0: str) -> int """
        return 0

    def set_aggregation_type(self, arg0, arg1): # real signature unknown; restored from __doc__
        """ set_aggregation_type(self: torch._C.LockingLogger, arg0: str, arg1: torch._C.AggregationType) -> None """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        """ __init__(self: torch._C.LockingLogger) -> None """
        pass


