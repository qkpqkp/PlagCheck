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


class AggregationType(__pybind11_builtins.pybind11_object):
    """
    Members:
    
      SUM
    
      AVG
    """
    def __eq__(self, *args, **kwargs): # real signature unknown
        """ (self: object, arg0: object) -> bool """
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        """ (self: object) -> int_ """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ (self: object) -> int_ """
        pass

    def __init__(self, arg0): # real signature unknown; restored from __doc__
        """ __init__(self: torch._C.AggregationType, arg0: int) -> None """
        pass

    def __int__(self): # real signature unknown; restored from __doc__
        """ __int__(self: torch._C.AggregationType) -> int """
        return 0

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ (self: object, arg0: object) -> bool """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ (self: handle) -> str """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ (self: torch._C.AggregationType, arg0: int) -> None """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """(self: handle) -> str
"""


    AVG = AggregationType.AVG # (!) forward: AVG, real value is 'AggregationType.AVG'
    SUM = AggregationType.SUM # (!) forward: SUM, real value is 'AggregationType.SUM'
    __entries = {
        'AVG': (
            AggregationType.AVG, # (!) forward: AVG, real value is 'AggregationType.AVG'
            None,
        ),
        'SUM': (
            AggregationType.SUM, # (!) forward: SUM, real value is 'AggregationType.SUM'
            None,
        ),
    }
    __members__ = {
        'AVG': AggregationType.AVG, # (!) forward: AVG, real value is 'AggregationType.AVG'
        'SUM': AggregationType.SUM, # (!) forward: SUM, real value is 'AggregationType.SUM'
    }


