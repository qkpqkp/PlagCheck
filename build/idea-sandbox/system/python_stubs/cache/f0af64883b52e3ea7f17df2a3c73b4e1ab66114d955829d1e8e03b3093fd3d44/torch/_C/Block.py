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


class Block(__pybind11_builtins.pybind11_object):
    # no doc
    def findAllNodes(self, kind, recurse=True): # real signature unknown; restored from __doc__
        """
        findAllNodes(self: torch._C.Block, kind: str, recurse: bool = True) -> List[torch::jit::Node]
        
        Find all nodes
        """
        return []

    def findNode(self, kind, recurse=True): # real signature unknown; restored from __doc__
        """
        findNode(self: torch._C.Block, kind: str, recurse: bool = True) -> torch::jit::Node
        
        Find Node
        """
        pass

    def inputs(self): # real signature unknown; restored from __doc__
        """ inputs(self: torch._C.Block) -> iterator """
        pass

    def nodes(self): # real signature unknown; restored from __doc__
        """ nodes(self: torch._C.Block) -> iterator """
        pass

    def outputs(self): # real signature unknown; restored from __doc__
        """ outputs(self: torch._C.Block) -> iterator """
        pass

    def paramNode(self): # real signature unknown; restored from __doc__
        """ paramNode(self: torch._C.Block) -> torch::jit::Node """
        pass

    def returnNode(self): # real signature unknown; restored from __doc__
        """ returnNode(self: torch._C.Block) -> torch::jit::Node """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


