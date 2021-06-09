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


class Value(__pybind11_builtins.pybind11_object):
    # no doc
    def copyMetadata(self, arg0): # real signature unknown; restored from __doc__
        """ copyMetadata(self: torch._C.Value, arg0: torch._C.Value) -> torch._C.Value """
        pass

    def debugName(self): # real signature unknown; restored from __doc__
        """ debugName(self: torch._C.Value) -> str """
        return ""

    def inferTypeFrom(self, arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ inferTypeFrom(self: torch._C.Value, arg0: at::Tensor) -> None """
        pass

    def isCompleteTensor(self): # real signature unknown; restored from __doc__
        """ isCompleteTensor(self: torch._C.Value) -> bool """
        return False

    def node(self): # real signature unknown; restored from __doc__
        """ node(self: torch._C.Value) -> torch::jit::Node """
        pass

    def offset(self): # real signature unknown; restored from __doc__
        """ offset(self: torch._C.Value) -> int """
        return 0

    def replaceAllUsesWith(self, arg0): # real signature unknown; restored from __doc__
        """ replaceAllUsesWith(self: torch._C.Value, arg0: torch._C.Value) -> None """
        pass

    def requires_grad(self): # real signature unknown; restored from __doc__
        """ requires_grad(self: torch._C.Value) -> bool """
        return False

    def setDebugName(self, arg0): # real signature unknown; restored from __doc__
        """ setDebugName(self: torch._C.Value, arg0: str) -> torch._C.Value """
        pass

    def setType(self, arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setType(self: torch._C.Value, arg0: c10::Type) -> torch._C.Value """
        pass

    def setTypeAs(self, arg0): # real signature unknown; restored from __doc__
        """ setTypeAs(self: torch._C.Value, arg0: torch._C.Value) -> torch._C.Value """
        pass

    def toIValue(self): # real signature unknown; restored from __doc__
        """ toIValue(self: torch._C.Value) -> Optional[IValue] """
        pass

    def type(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        type(*args, **kwargs)
        Overloaded function.
        
        1. type(self: torch._C.Value) -> c10::Type
        
        2. type(self: torch._C.Value) -> c10::Type
        """
        pass

    def unique(self): # real signature unknown; restored from __doc__
        """ unique(self: torch._C.Value) -> int """
        return 0

    def uses(self): # real signature unknown; restored from __doc__
        """ uses(self: torch._C.Value) -> List[torch::jit::Use] """
        return []

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ __repr__(self: torch._C.Value) -> str """
        return ""


