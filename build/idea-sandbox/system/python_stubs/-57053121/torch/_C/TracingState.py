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


class TracingState(__pybind11_builtins.pybind11_object):
    # no doc
    def graph(self): # real signature unknown; restored from __doc__
        """ graph(self: torch._C.TracingState) -> torch._C.Graph """
        pass

    def pop_scope(self): # real signature unknown; restored from __doc__
        """ pop_scope(self: torch._C.TracingState) -> None """
        pass

    def push_scope(self, arg0): # real signature unknown; restored from __doc__
        """ push_scope(self: torch._C.TracingState, arg0: str) -> None """
        pass

    def set_graph(self, arg0): # real signature unknown; restored from __doc__
        """ set_graph(self: torch._C.TracingState, arg0: torch._C.Graph) -> None """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ __repr__(self: torch._C.TracingState) -> str """
        return ""

    def __str__(self): # real signature unknown; restored from __doc__
        """ __str__(self: torch._C.TracingState) -> str """
        return ""

    __dict__ = None # (!) real value is "mappingproxy({'__init__': <slot wrapper '__init__' of 'torch._C.TracingState' objects>, '__dict__': <attribute '__dict__' of 'torch._C.TracingState' objects>, '__doc__': None, '__module__': 'torch._C', '__repr__': <instancemethod __repr__ at 0x000002E10E3FDDC8>, '__str__': <instancemethod __str__ at 0x000002E10E3FDE28>, 'push_scope': <instancemethod push_scope at 0x000002E10E3FDE88>, 'pop_scope': <instancemethod pop_scope at 0x000002E10E3FDEE8>, 'set_graph': <instancemethod set_graph at 0x000002E10E3FDF48>, 'graph': <instancemethod graph at 0x000002E10E3FDFA8>})"


