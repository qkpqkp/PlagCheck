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


class ScriptModule(__pybind11_builtins.pybind11_object):
    # no doc
    def apply(self, arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ apply(self: torch._C.ScriptModule, arg0: Callable[[torch._C.ScriptModule], None]) -> None """
        pass

    def clone_method(self, arg0, arg1): # real signature unknown; restored from __doc__
        """ clone_method(self: torch._C.ScriptModule, arg0: torch._C.ScriptModule, arg1: str) -> None """
        pass

    def get_debug_state(self): # real signature unknown; restored from __doc__
        """ get_debug_state(self: torch._C.ScriptModule) -> torch._C.GraphExecutorState """
        pass

    def save(self, filename, _extra_files=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ save(self: torch._C.ScriptModule, filename: str, _extra_files: torch._C.ExtraFilesMap = ExtraFilesMap{}) -> None """
        pass

    def save_to_buffer(self, _extra_files=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ save_to_buffer(self: torch._C.ScriptModule, _extra_files: torch._C.ExtraFilesMap = ExtraFilesMap{}) -> bytes """
        pass

    def _clone(self): # real signature unknown; restored from __doc__
        """ _clone(self: torch._C.ScriptModule) -> torch._C.ScriptModule """
        pass

    def _create_methods(self, arg0, arg1, torch__C__jit_tree_views_Def=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ _create_methods(self: torch._C.ScriptModule, arg0: object, arg1: List[torch._C._jit_tree_views.Def], arg2: List[Callable[[str], function]], arg3: List[Dict[str, object]]) -> None """
        pass

    def _create_method_from_trace(self, arg0, arg1, arg2, arg3, arg4): # real signature unknown; restored from __doc__
        """ _create_method_from_trace(self: torch._C.ScriptModule, arg0: str, arg1: function, arg2: tuple, arg3: function, arg4: bool) -> None """
        pass

    def _define(self, arg0, arg1, arg2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ _define(self: torch._C.ScriptModule, arg0: object, arg1: str, arg2: Callable[[str], function]) -> None """
        pass

    def _dump(self, code=True, attrs=True, params=True): # real signature unknown; restored from __doc__
        """ _dump(self: torch._C.ScriptModule, code: bool = True, attrs: bool = True, params: bool = True) -> None """
        pass

    def _get_attribute(self, arg0): # real signature unknown; restored from __doc__
        """ _get_attribute(self: torch._C.ScriptModule, arg0: str) -> IValue """
        pass

    def _get_attributes(self): # real signature unknown; restored from __doc__
        """ _get_attributes(self: torch._C.ScriptModule) -> tuple """
        return ()

    def _get_buffer(self, arg0): # real signature unknown; restored from __doc__
        """ _get_buffer(self: torch._C.ScriptModule, arg0: str) -> torch::autograd::Variable """
        pass

    def _get_method(self, arg0): # real signature unknown; restored from __doc__
        """ _get_method(self: torch._C.ScriptModule, arg0: str) -> torch::jit::script::Method """
        pass

    def _get_module(self, arg0): # real signature unknown; restored from __doc__
        """ _get_module(self: torch._C.ScriptModule, arg0: str) -> torch._C.ScriptModule """
        pass

    def _get_modules(self): # real signature unknown; restored from __doc__
        """ _get_modules(self: torch._C.ScriptModule) -> List[Tuple[str, torch._C.ScriptModule]] """
        return []

    def _get_parameter(self, arg0): # real signature unknown; restored from __doc__
        """ _get_parameter(self: torch._C.ScriptModule, arg0: str) -> torch::autograd::Variable """
        pass

    def _get_parameters(self): # real signature unknown; restored from __doc__
        """ _get_parameters(self: torch._C.ScriptModule) -> tuple """
        return ()

    def _has_attribute(self, arg0): # real signature unknown; restored from __doc__
        """ _has_attribute(self: torch._C.ScriptModule, arg0: str) -> bool """
        return False

    def _has_buffer(self, arg0): # real signature unknown; restored from __doc__
        """ _has_buffer(self: torch._C.ScriptModule, arg0: str) -> bool """
        return False

    def _has_method(self, arg0): # real signature unknown; restored from __doc__
        """ _has_method(self: torch._C.ScriptModule, arg0: str) -> bool """
        return False

    def _has_module(self, arg0): # real signature unknown; restored from __doc__
        """ _has_module(self: torch._C.ScriptModule, arg0: str) -> bool """
        return False

    def _has_parameter(self, arg0): # real signature unknown; restored from __doc__
        """ _has_parameter(self: torch._C.ScriptModule, arg0: str) -> bool """
        return False

    def _method_names(self): # real signature unknown; restored from __doc__
        """ _method_names(self: torch._C.ScriptModule) -> List[str] """
        return []

    def _register_attribute(self, arg0, arg1, arg2): # real signature unknown; restored from __doc__
        """ _register_attribute(self: torch._C.ScriptModule, arg0: str, arg1: torch._C.Type, arg2: object) -> None """
        pass

    def _register_buffer(self, arg0, arg1, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ _register_buffer(self: torch._C.ScriptModule, arg0: str, arg1: torch::autograd::Variable) -> None """
        pass

    def _register_module(self, arg0, arg1): # real signature unknown; restored from __doc__
        """ _register_module(self: torch._C.ScriptModule, arg0: str, arg1: torch._C.ScriptModule) -> None """
        pass

    def _register_parameter(self, arg0, arg1, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ _register_parameter(self: torch._C.ScriptModule, arg0: str, arg1: torch::autograd::Variable, arg2: bool) -> None """
        pass

    def _set_attribute(self, arg0, arg1): # real signature unknown; restored from __doc__
        """ _set_attribute(self: torch._C.ScriptModule, arg0: str, arg1: object) -> None """
        pass

    def _set_optimized(self, arg0): # real signature unknown; restored from __doc__
        """ _set_optimized(self: torch._C.ScriptModule, arg0: bool) -> None """
        pass

    def _set_parameter(self, arg0, arg1, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ _set_parameter(self: torch._C.ScriptModule, arg0: str, arg1: at::Tensor) -> None """
        pass

    def __init__(self, arg0, arg1, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ __init__(self: torch._C.ScriptModule, arg0: str, arg1: torch::jit::script::CompilationUnit, arg2: bool) -> None """
        pass

    code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



