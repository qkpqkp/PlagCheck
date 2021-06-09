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


class Function(__pybind11_builtins.pybind11_object):
    # no doc
    def get_debug_state(self): # real signature unknown; restored from __doc__
        """ get_debug_state(self: torch._C.Function) -> torch._C.GraphExecutorState """
        pass

    def graph_for(self, *args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def save(self, filename, _extra_files=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ save(self: torch._C.Function, filename: str, _extra_files: torch._C.ExtraFilesMap = ExtraFilesMap{}) -> None """
        pass

    def save_to_buffer(self, _extra_files=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ save_to_buffer(self: torch._C.Function, _extra_files: torch._C.ExtraFilesMap = ExtraFilesMap{}) -> bytes """
        pass

    def __call__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """ __call__(*args, **kwargs) -> object """
        return object()

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    graph = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qualified_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    schema = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'__init__': <slot wrapper '__init__' of 'torch._C.Function' objects>, '__dict__': <attribute '__dict__' of 'torch._C.Function' objects>, '__doc__': None, '__module__': 'torch._C', '__call__': <instancemethod __call__ at 0x000002E10E411738>, 'save': <instancemethod save at 0x000002E10E411798>, 'save_to_buffer': <instancemethod save_to_buffer at 0x000002E10E4117F8>, 'graph': <property object at 0x000002E10E40E458>, 'schema': <property object at 0x000002E10E40E4A8>, 'code': <property object at 0x000002E10E40E4F8>, 'get_debug_state': <instancemethod get_debug_state at 0x000002E10E4118E8>, 'name': <property object at 0x000002E10E3E9E08>, 'qualified_name': <property object at 0x000002E10E40E548>, 'graph_for': <function _graph_for at 0x000002E110A85158>})"


