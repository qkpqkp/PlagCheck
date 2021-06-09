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


class Node(__pybind11_builtins.pybind11_object):
    # no doc
    def addBlock(self): # real signature unknown; restored from __doc__
        """ addBlock(self: torch._C.Node) -> torch._C.Block """
        pass

    def addInput(self, arg0): # real signature unknown; restored from __doc__
        """ addInput(self: torch._C.Node, arg0: torch._C.Value) -> torch._C.Value """
        pass

    def addOutput(self): # real signature unknown; restored from __doc__
        """ addOutput(self: torch._C.Node) -> torch._C.Value """
        pass

    def attributeNames(self): # real signature unknown; restored from __doc__
        """ attributeNames(self: torch._C.Node) -> List[str] """
        return []

    def blocks(self): # real signature unknown; restored from __doc__
        """ blocks(self: torch._C.Node) -> iterator """
        pass

    def cconv(self): # real signature unknown; restored from __doc__
        """ cconv(self: torch._C.Node) -> str """
        return ""

    def copyAttributes(self, arg0): # real signature unknown; restored from __doc__
        """ copyAttributes(self: torch._C.Node, arg0: torch._C.Node) -> None """
        pass

    def destroy(self): # real signature unknown; restored from __doc__
        """ destroy(self: torch._C.Node) -> None """
        pass

    def eraseOutput(self, arg0): # real signature unknown; restored from __doc__
        """ eraseOutput(self: torch._C.Node, arg0: int) -> None """
        pass

    def f(self, arg0): # real signature unknown; restored from __doc__
        """ f(self: torch._C.Node, arg0: str) -> float """
        return 0.0

    def findAllNodes(self, kind, recurse=True): # real signature unknown; restored from __doc__
        """
        findAllNodes(self: torch._C.Node, kind: str, recurse: bool = True) -> List[torch._C.Node]
        
        Find all nodes
        """
        return []

    def findNode(self, kind, recurse=True): # real signature unknown; restored from __doc__
        """
        findNode(self: torch._C.Node, kind: str, recurse: bool = True) -> torch._C.Node
        
        Find Node
        """
        pass

    def fs(self, arg0): # real signature unknown; restored from __doc__
        """ fs(self: torch._C.Node, arg0: str) -> List[float] """
        return []

    def fs_(self, arg0, arg1, p_float=None): # real signature unknown; restored from __doc__
        """ fs_(self: torch._C.Node, arg0: str, arg1: List[float]) -> torch._C.Node """
        pass

    def f_(self, arg0, arg1): # real signature unknown; restored from __doc__
        """ f_(self: torch._C.Node, arg0: str, arg1: float) -> torch._C.Node """
        pass

    def g(self, arg0): # real signature unknown; restored from __doc__
        """ g(self: torch._C.Node, arg0: str) -> torch._C.Graph """
        pass

    def gs(self, arg0): # real signature unknown; restored from __doc__
        """ gs(self: torch._C.Node, arg0: str) -> List[torch._C.Graph] """
        return []

    def gs_(self, arg0, arg1, torch__C_Graph=None): # real signature unknown; restored from __doc__
        """ gs_(self: torch._C.Node, arg0: str, arg1: List[torch._C.Graph]) -> torch._C.Node """
        pass

    def g_(self, arg0, arg1): # real signature unknown; restored from __doc__
        """ g_(self: torch._C.Node, arg0: str, arg1: torch._C.Graph) -> torch._C.Node """
        pass

    def hasAttribute(self, arg0): # real signature unknown; restored from __doc__
        """ hasAttribute(self: torch._C.Node, arg0: str) -> bool """
        return False

    def hasAttributes(self): # real signature unknown; restored from __doc__
        """ hasAttributes(self: torch._C.Node) -> bool """
        return False

    def hasMultipleOutputs(self): # real signature unknown; restored from __doc__
        """ hasMultipleOutputs(self: torch._C.Node) -> bool """
        return False

    def hasUses(self): # real signature unknown; restored from __doc__
        """ hasUses(self: torch._C.Node) -> bool """
        return False

    def i(self, arg0): # real signature unknown; restored from __doc__
        """ i(self: torch._C.Node, arg0: str) -> int """
        return 0

    def input(self): # real signature unknown; restored from __doc__
        """ input(self: torch._C.Node) -> torch._C.Value """
        pass

    def inputs(self): # real signature unknown; restored from __doc__
        """ inputs(self: torch._C.Node) -> iterator """
        pass

    def inputsAt(self, arg0): # real signature unknown; restored from __doc__
        """ inputsAt(self: torch._C.Node, arg0: int) -> torch._C.Value """
        pass

    def insertAfter(self, arg0): # real signature unknown; restored from __doc__
        """ insertAfter(self: torch._C.Node, arg0: torch._C.Node) -> torch._C.Node """
        pass

    def insertBefore(self, arg0): # real signature unknown; restored from __doc__
        """ insertBefore(self: torch._C.Node, arg0: torch._C.Node) -> torch._C.Node """
        pass

    def isNondeterministic(self): # real signature unknown; restored from __doc__
        """ isNondeterministic(self: torch._C.Node) -> bool """
        return False

    def is_(self, arg0, arg1, p_int=None): # real signature unknown; restored from __doc__
        """ is_(self: torch._C.Node, arg0: str, arg1: List[int]) -> torch._C.Node """
        pass

    def i_(self, arg0, arg1): # real signature unknown; restored from __doc__
        """ i_(self: torch._C.Node, arg0: str, arg1: int) -> torch._C.Node """
        pass

    def kind(self): # real signature unknown; restored from __doc__
        """ kind(self: torch._C.Node) -> Symbol """
        pass

    def kindOf(self, arg0): # real signature unknown; restored from __doc__
        """ kindOf(self: torch._C.Node, arg0: str) -> AttributeKind """
        pass

    def moveAfter(self, arg0): # real signature unknown; restored from __doc__
        """ moveAfter(self: torch._C.Node, arg0: torch._C.Node) -> None """
        pass

    def moveBefore(self, arg0): # real signature unknown; restored from __doc__
        """ moveBefore(self: torch._C.Node, arg0: torch._C.Node) -> None """
        pass

    def mustBeNone(self): # real signature unknown; restored from __doc__
        """ mustBeNone(self: torch._C.Node) -> bool """
        return False

    def output(self): # real signature unknown; restored from __doc__
        """ output(self: torch._C.Node) -> torch._C.Value """
        pass

    def outputs(self): # real signature unknown; restored from __doc__
        """ outputs(self: torch._C.Node) -> iterator """
        pass

    def outputsAt(self, arg0): # real signature unknown; restored from __doc__
        """ outputsAt(self: torch._C.Node, arg0: int) -> torch._C.Value """
        pass

    def outputsSize(self): # real signature unknown; restored from __doc__
        """ outputsSize(self: torch._C.Node) -> int """
        return 0

    def pyname(self): # real signature unknown; restored from __doc__
        """ pyname(self: torch._C.Node) -> str """
        return ""

    def pyobj(self): # real signature unknown; restored from __doc__
        """ pyobj(self: torch._C.Node) -> object """
        return object()

    def removeAllInputs(self): # real signature unknown; restored from __doc__
        """ removeAllInputs(self: torch._C.Node) -> None """
        pass

    def removeAttribute(self, arg0): # real signature unknown; restored from __doc__
        """ removeAttribute(self: torch._C.Node, arg0: str) -> torch._C.Node """
        pass

    def removeInput(self, arg0): # real signature unknown; restored from __doc__
        """ removeInput(self: torch._C.Node, arg0: int) -> None """
        pass

    def replaceAllUsesWith(self, arg0): # real signature unknown; restored from __doc__
        """ replaceAllUsesWith(self: torch._C.Node, arg0: torch._C.Node) -> None """
        pass

    def replaceInput(self, arg0, arg1): # real signature unknown; restored from __doc__
        """ replaceInput(self: torch._C.Node, arg0: int, arg1: torch._C.Value) -> torch._C.Value """
        pass

    def replaceInputWith(self, arg0, arg1): # real signature unknown; restored from __doc__
        """ replaceInputWith(self: torch._C.Node, arg0: torch._C.Value, arg1: torch._C.Value) -> None """
        pass

    def s(self, arg0): # real signature unknown; restored from __doc__
        """ s(self: torch._C.Node, arg0: str) -> str """
        return ""

    def scalar_args(self): # real signature unknown; restored from __doc__
        """ scalar_args(self: torch._C.Node) -> list """
        return []

    def scopeName(self): # real signature unknown; restored from __doc__
        """ scopeName(self: torch._C.Node) -> str """
        return ""

    def sourceRange(self): # real signature unknown; restored from __doc__
        """ sourceRange(self: torch._C.Node) -> str """
        return ""

    def ss(self, arg0): # real signature unknown; restored from __doc__
        """ ss(self: torch._C.Node, arg0: str) -> List[str] """
        return []

    def ss_(self, arg0, arg1, p_str=None): # real signature unknown; restored from __doc__
        """ ss_(self: torch._C.Node, arg0: str, arg1: List[str]) -> torch._C.Node """
        pass

    def s_(self, arg0, arg1): # real signature unknown; restored from __doc__
        """ s_(self: torch._C.Node, arg0: str, arg1: str) -> torch._C.Node """
        pass

    def t(self, arg0): # real signature unknown; restored from __doc__
        """ t(self: torch._C.Node, arg0: str) -> at::Tensor """
        pass

    def ts(self, arg0): # real signature unknown; restored from __doc__
        """ ts(self: torch._C.Node, arg0: str) -> List[torch::autograd::Variable] """
        return []

    def ts_(self, arg0, arg1, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ ts_(self: torch._C.Node, arg0: str, arg1: List[torch::autograd::Variable]) -> torch._C.Node """
        pass

    def t_(self, arg0, arg1, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ t_(self: torch._C.Node, arg0: str, arg1: torch::autograd::Variable) -> torch._C.Node """
        pass

    def z(self, arg0): # real signature unknown; restored from __doc__
        """ z(self: torch._C.Node, arg0: str) -> at::Tensor """
        pass

    def zs(self, arg0): # real signature unknown; restored from __doc__
        """ zs(self: torch._C.Node, arg0: str) -> List[at::Tensor] """
        return []

    def zs_(self, arg0, arg1, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ zs_(self: torch._C.Node, arg0: str, arg1: List[at::Tensor]) -> torch._C.Node """
        pass

    def z_(self, arg0, arg1, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ z_(self: torch._C.Node, arg0: str, arg1: at::Tensor) -> torch._C.Node """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ __repr__(self: torch._C.Node) -> str """
        return ""


