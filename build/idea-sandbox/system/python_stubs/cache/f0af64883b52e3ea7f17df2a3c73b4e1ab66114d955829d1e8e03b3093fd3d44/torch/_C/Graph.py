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


class Graph(__pybind11_builtins.pybind11_object):
    # no doc
    def addInput(self): # real signature unknown; restored from __doc__
        """ addInput(self: torch._C.Graph) -> torch::jit::Value """
        pass

    def appendNode(self, arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ appendNode(self: torch._C.Graph, arg0: torch::jit::Node) -> torch::jit::Node """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self: torch._C.Graph) -> torch._C.Graph """
        pass

    def create(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        create(*args, **kwargs)
        Overloaded function.
        
        1. create(self: torch._C.Graph, arg0: str) -> torch::jit::Node
        
        2. create(self: torch._C.Graph, arg0: str, arg1: int) -> torch::jit::Node
        
        3. create(self: torch._C.Graph, arg0: str, arg1: List[torch::jit::Value]) -> torch::jit::Node
        
        4. create(self: torch._C.Graph, arg0: str, arg1: List[torch::jit::Value], arg2: int) -> torch::jit::Node
        """
        pass

    def createClone(self, arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ createClone(self: torch._C.Graph, arg0: torch::jit::Node, arg1: object) -> torch::jit::Node """
        pass

    def createFusionGroup(self): # real signature unknown; restored from __doc__
        """ createFusionGroup(self: torch._C.Graph) -> torch::jit::Node """
        pass

    def dump_alias_db(self): # real signature unknown; restored from __doc__
        """ dump_alias_db(self: torch._C.Graph) -> None """
        pass

    def eraseInput(self, arg0): # real signature unknown; restored from __doc__
        """ eraseInput(self: torch._C.Graph, arg0: int) -> None """
        pass

    def findAllNodes(self, kind, recurse=True): # real signature unknown; restored from __doc__
        """
        findAllNodes(self: torch._C.Graph, kind: str, recurse: bool = True) -> List[torch::jit::Node]
        
        Find all nodes
        """
        return []

    def findNode(self, kind, recurse=True): # real signature unknown; restored from __doc__
        """
        findNode(self: torch._C.Graph, kind: str, recurse: bool = True) -> torch::jit::Node
        
        Find Node
        """
        pass

    def inputs(self): # real signature unknown; restored from __doc__
        """ inputs(self: torch._C.Graph) -> iterator """
        pass

    def insertNode(self, arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ insertNode(self: torch._C.Graph, arg0: torch::jit::Node) -> torch::jit::Node """
        pass

    def lint(self): # real signature unknown; restored from __doc__
        """ lint(self: torch._C.Graph) -> None """
        pass

    def nodes(self): # real signature unknown; restored from __doc__
        """ nodes(self: torch._C.Graph) -> iterator """
        pass

    def outputs(self): # real signature unknown; restored from __doc__
        """ outputs(self: torch._C.Graph) -> iterator """
        pass

    def param_node(self): # real signature unknown; restored from __doc__
        """ param_node(self: torch._C.Graph) -> torch::jit::Node """
        pass

    def prependNode(self, arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ prependNode(self: torch._C.Graph, arg0: torch::jit::Node) -> torch::jit::Node """
        pass

    def registerOutput(self, arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ registerOutput(self: torch._C.Graph, arg0: torch::jit::Value) -> int """
        pass

    def return_node(self): # real signature unknown; restored from __doc__
        """ return_node(self: torch._C.Graph) -> torch::jit::Node """
        pass

    def str(self, print_source_ranges=True): # real signature unknown; restored from __doc__
        """ str(self: torch._C.Graph, print_source_ranges: bool = True) -> str """
        return ""

    def _export_onnx(self, initializers, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ _export_onnx(self: torch._C.Graph, initializers: Dict[str, at::Tensor], onnx_opset_version: int = 0, dynamic_axes: Dict[str, Dict[int, str]], defer_weight_export: bool = False, operator_export_type: torch._C._onnx.OperatorExportTypes = OperatorExportTypes.ONNX, strip_doc_string: bool = True, keep_initializers_as_inputs: bool = True) -> Tuple[bytes, Dict[str, bytes]] """
        pass

    def _pretty_print_onnx(self, initializers, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ _pretty_print_onnx(self: torch._C.Graph, initializers: Dict[str, at::Tensor], onnx_opset_version: int = 0, defer_weight_export: bool = False, operator_export_type: torch._C._onnx.OperatorExportTypes = OperatorExportTypes.ONNX, google_printer: bool = False, keep_initializers_as_inputs: bool = True) -> str """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        """ __init__(self: torch._C.Graph) -> None """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ __repr__(self: torch._C.Graph) -> str """
        return ""


