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


# Variables with simple values

has_cuda = True
has_cudnn = True
has_lapack = True
has_mkl = True
has_mkldnn = False
has_openmp = True

_BUILD_NAMEDTENSOR = True

_GLIBCXX_USE_CXX11_ABI = False

# functions

def fork(*args): # real signature unknown; restored from __doc__
    """ fork(*args) -> torch._C.Future """
    pass

def get_default_dtype(): # real signature unknown; restored from __doc__
    """
    get_default_dtype() -> torch.dtype
    
    Get the current default floating point :class:`torch.dtype`.
    
    Example::
    
        >>> torch.get_default_dtype()  # initial default for floating point is torch.float32
        torch.float32
        >>> torch.set_default_dtype(torch.float64)
        >>> torch.get_default_dtype()  # default is now changed to torch.float64
        torch.float64
        >>> torch.set_default_tensor_type(torch.FloatTensor)  # setting tensor type also affects this
        >>> torch.get_default_dtype()  # changed to torch.float32, the dtype for torch.FloatTensor
        torch.float32
    """
    pass

def get_num_interop_threads(): # real signature unknown; restored from __doc__
    """
    get_num_interop_threads() -> int
    
    Returns the number of threads used for inter-op parallelism on CPU
    (e.g. in JIT interpreter)
    """
    return 0

def get_num_threads(): # real signature unknown; restored from __doc__
    """
    get_num_threads() -> int
    
    Returns the number of threads used for parallelizing CPU operations
    """
    return 0

def import_ir_module(arg0, arg1, arg2, arg3): # real signature unknown; restored from __doc__
    """ import_ir_module(arg0: torch._C.CompilationUnit, arg1: str, arg2: object, arg3: torch._C.ExtraFilesMap) -> torch._C.ScriptModule """
    pass

def import_ir_module_from_buffer(arg0, arg1, arg2, arg3): # real signature unknown; restored from __doc__
    """ import_ir_module_from_buffer(arg0: torch._C.CompilationUnit, arg1: str, arg2: object, arg3: torch._C.ExtraFilesMap) -> torch._C.ScriptModule """
    pass

def is_anomaly_enabled(*args, **kwargs): # real signature unknown
    pass

def is_grad_enabled(*args, **kwargs): # real signature unknown
    pass

def merge_type_from_type_comment(arg0, arg1, arg2): # real signature unknown; restored from __doc__
    """ merge_type_from_type_comment(arg0: torch._C._jit_tree_views.Decl, arg1: torch._C._jit_tree_views.Decl, arg2: bool) -> torch._C._jit_tree_views.Decl """
    pass

def parse_ir(arg0): # real signature unknown; restored from __doc__
    """ parse_ir(arg0: str) -> torch::jit::Graph """
    pass

def parse_schema(arg0): # real signature unknown; restored from __doc__
    """ parse_schema(arg0: str) -> c10::FunctionSchema """
    pass

def parse_type_comment(arg0): # real signature unknown; restored from __doc__
    """ parse_type_comment(arg0: str) -> torch._C._jit_tree_views.Decl """
    pass

def set_anomaly_enabled(*args, **kwargs): # real signature unknown
    pass

def set_flush_denormal(mode): # real signature unknown; restored from __doc__
    """
    set_flush_denormal(mode) -> bool
    
    Disables denormal floating numbers on CPU.
    
    Returns ``True`` if your system supports flushing denormal numbers and it
    successfully configures flush denormal mode.  :meth:`~torch.set_flush_denormal`
    is only supported on x86 architectures supporting SSE3.
    
    Args:
        mode (bool): Controls whether to enable flush denormal mode or not
    
    Example::
    
        >>> torch.set_flush_denormal(True)
        True
        >>> torch.tensor([1e-323], dtype=torch.float64)
        tensor([ 0.], dtype=torch.float64)
        >>> torch.set_flush_denormal(False)
        True
        >>> torch.tensor([1e-323], dtype=torch.float64)
        tensor(9.88131e-324 *
               [ 1.0000], dtype=torch.float64)
    """
    return False

def set_grad_enabled(*args, **kwargs): # real signature unknown
    pass

def set_num_interop_threads(p_int): # real signature unknown; restored from __doc__
    """
    set_num_interop_threads(int)
    
    Sets the number of threads used for interop parallelism
    (e.g. in JIT interpreter) on CPU.
    WARNING: Can only be called once and before any inter-op parallel work
    is started (e.g. JIT execution).
    """
    pass

def set_num_threads(p_int): # real signature unknown; restored from __doc__
    """
    set_num_threads(int)
    
    Sets the number of threads used for parallelizing CPU operations.
    WARNING:
    To ensure that the correct number of threads is used, set_num_threads
    must be called before running eager, JIT or autograd code.
    """
    pass

def wait(arg0): # real signature unknown; restored from __doc__
    """ wait(arg0: torch._C.Future) -> IValue """
    pass

def _add_docstr(*args, **kwargs): # real signature unknown
    pass

def _assign_output_shapes(arg0, arg1, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _assign_output_shapes(arg0: torch._C.Graph, arg1: List[at::Tensor]) -> torch._C.Graph """
    pass

def _autograd_init(*args, **kwargs): # real signature unknown
    pass

def _broadcast(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _broadcast(arg0: at::Tensor, arg1: List[int]) -> List[at::Tensor] """
    pass

def _broadcast_coalesced(tensors, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _broadcast_coalesced(tensors: List[at::Tensor], devices: List[int], buffer_size: int) -> List[List[at::Tensor]] """
    pass

def _crash_if_aten_asan(*args, **kwargs): # real signature unknown
    pass

def _crash_if_csrc_asan(*args, **kwargs): # real signature unknown
    pass

def _crash_if_csrc_ubsan(*args, **kwargs): # real signature unknown
    pass

def _create_function_from_graph(arg0, arg1): # real signature unknown; restored from __doc__
    """ _create_function_from_graph(arg0: str, arg1: torch._C.Graph) -> torch._C.Function """
    pass

def _create_function_from_trace(arg0, arg1, arg2, arg3, arg4): # real signature unknown; restored from __doc__
    """ _create_function_from_trace(arg0: str, arg1: function, arg2: tuple, arg3: function, arg4: bool) -> torch._C.Function """
    pass

def _cuda_cudaHostAllocator(*args, **kwargs): # real signature unknown
    pass

def _cuda_emptyCache(*args, **kwargs): # real signature unknown
    pass

def _cuda_getCompiledVersion(*args, **kwargs): # real signature unknown
    pass

def _cuda_getCurrentBlasHandle(*args, **kwargs): # real signature unknown
    pass

def _cuda_getCurrentStream(*args, **kwargs): # real signature unknown
    pass

def _cuda_getDefaultStream(*args, **kwargs): # real signature unknown
    pass

def _cuda_getDevice(*args, **kwargs): # real signature unknown
    pass

def _cuda_getDeviceCount(*args, **kwargs): # real signature unknown
    pass

def _cuda_getDriverVersion(*args, **kwargs): # real signature unknown
    pass

def _cuda_hasPrimaryContext(*args, **kwargs): # real signature unknown
    pass

def _cuda_init(*args, **kwargs): # real signature unknown
    pass

def _cuda_ipc_collect(*args, **kwargs): # real signature unknown
    pass

def _cuda_isDriverSufficient(*args, **kwargs): # real signature unknown
    pass

def _cuda_lock_mutex(*args, **kwargs): # real signature unknown
    pass

def _cuda_maxMemoryAllocated(*args, **kwargs): # real signature unknown
    pass

def _cuda_maxMemoryCached(*args, **kwargs): # real signature unknown
    pass

def _cuda_memoryAllocated(*args, **kwargs): # real signature unknown
    pass

def _cuda_memoryCached(*args, **kwargs): # real signature unknown
    pass

def _cuda_resetMaxMemoryAllocated(*args, **kwargs): # real signature unknown
    pass

def _cuda_resetMaxMemoryCached(*args, **kwargs): # real signature unknown
    pass

def _cuda_setDevice(*args, **kwargs): # real signature unknown
    pass

def _cuda_setStream(*args, **kwargs): # real signature unknown
    pass

def _cuda_set_run_yet_variable_to_false(*args, **kwargs): # real signature unknown
    pass

def _cuda_sleep(*args, **kwargs): # real signature unknown
    pass

def _cuda_synchronize(*args, **kwargs): # real signature unknown
    pass

def _cuda_unlock_mutex(*args, **kwargs): # real signature unknown
    pass

def _cudnn_version(*args, **kwargs): # real signature unknown
    pass

def _debug_set_autodiff_subgraph_inlining(arg0): # real signature unknown; restored from __doc__
    """ _debug_set_autodiff_subgraph_inlining(arg0: bool) -> None """
    pass

def _demangle(arg0): # real signature unknown; restored from __doc__
    """ _demangle(arg0: str) -> str """
    return ""

def _error_if_any_worker_fails(*args, **kwargs): # real signature unknown
    pass

def _from_dlpack(*args, **kwargs): # real signature unknown
    pass

def _gather(tensors, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _gather(tensors: List[at::Tensor], dim: int, destination_index: Optional[int]) -> at::Tensor """
    pass

def _get_backcompat_broadcast_warn(*args, **kwargs): # real signature unknown
    pass

def _get_backcompat_keepdim_warn(*args, **kwargs): # real signature unknown
    pass

def _get_cudnn_benchmark(*args, **kwargs): # real signature unknown
    pass

def _get_cudnn_deterministic(*args, **kwargs): # real signature unknown
    pass

def _get_cudnn_enabled(*args, **kwargs): # real signature unknown
    pass

def _get_default_device(*args, **kwargs): # real signature unknown
    pass

def _get_graph_executor_optimize(): # real signature unknown; restored from __doc__
    """ _get_graph_executor_optimize() -> bool """
    return False

def _get_mkldnn_enabled(*args, **kwargs): # real signature unknown
    pass

def _get_qengine(*args, **kwargs): # real signature unknown
    pass

def _get_tracing_state(): # real signature unknown; restored from __doc__
    """ _get_tracing_state() -> torch._C.TracingState """
    pass

def _get_value_trace(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _get_value_trace(arg0: torch::autograd::Variable) -> torch._C.Value """
    pass

def _has_distributed(*args, **kwargs): # real signature unknown
    pass

def _infer_size(*args, **kwargs): # real signature unknown
    pass

def _initExtension(*args, **kwargs): # real signature unknown
    pass

def _init_names(*args, **kwargs): # real signature unknown
    pass

def _ivalue_tags_match(arg0, arg1): # real signature unknown; restored from __doc__
    """ _ivalue_tags_match(arg0: torch._C.ScriptModule, arg1: torch._C.ScriptModule) -> bool """
    return False

def _jit_assert_is_instance(arg0, arg1, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_assert_is_instance(arg0: object, arg1: c10::Type) -> None """
    pass

def _jit_check_alias_annotation(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_check_alias_annotation(arg0: torch::jit::Graph, arg1: tuple, arg2: str) -> None """
    pass

def _jit_clear_class_registry(): # real signature unknown; restored from __doc__
    """ _jit_clear_class_registry() -> None """
    pass

def _jit_debug_fuser_num_cached_kernel_specs(): # real signature unknown; restored from __doc__
    """ _jit_debug_fuser_num_cached_kernel_specs() -> int """
    return 0

def _jit_differentiate(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_differentiate(arg0: torch::jit::Graph) -> torch::jit::Gradient """
    pass

def _jit_flatten(arg0): # real signature unknown; restored from __doc__
    """ _jit_flatten(arg0: handle) -> Tuple[List[torch::autograd::Variable], torch._C.IODescriptor] """
    pass

def _jit_fuser_get_fused_kernel_code(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_fuser_get_fused_kernel_code(arg0: torch::jit::Graph, arg1: List[at::Tensor]) -> str """
    pass

def _jit_get_all_schemas(): # real signature unknown; restored from __doc__
    """ _jit_get_all_schemas() -> List[torch._C.FunctionSchema] """
    return []

def _jit_get_emit_hooks(): # real signature unknown; restored from __doc__
    """ _jit_get_emit_hooks() -> Tuple[Callable[[torch._C.ScriptModule], None], Callable[[torch._C.Function], None]] """
    pass

def _jit_get_inline_everything_mode(): # real signature unknown; restored from __doc__
    """ _jit_get_inline_everything_mode() -> bool """
    return False

def _jit_get_operation(qualified_name): # real signature unknown; restored from __doc__
    """ _jit_get_operation(qualified_name: str) -> cpp_function """
    pass

def _jit_get_schemas_for_operator(arg0): # real signature unknown; restored from __doc__
    """ _jit_get_schemas_for_operator(arg0: str) -> List[torch._C.FunctionSchema] """
    return []

def _jit_init(): # real signature unknown; restored from __doc__
    """ _jit_init() -> bool """
    return False

def _jit_override_can_fuse_on_cpu(arg0): # real signature unknown; restored from __doc__
    """ _jit_override_can_fuse_on_cpu(arg0: bool) -> None """
    pass

def _jit_pass_canonicalize(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_pass_canonicalize(arg0: torch::jit::Graph) -> torch::jit::Graph """
    pass

def _jit_pass_canonicalize_ops(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_pass_canonicalize_ops(arg0: torch::jit::Graph) -> None """
    pass

def _jit_pass_complete_shape_analysis(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_pass_complete_shape_analysis(arg0: torch::jit::Graph, arg1: tuple, arg2: bool) -> None """
    pass

def _jit_pass_constant_pooling(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_pass_constant_pooling(arg0: torch::jit::Graph) -> None """
    pass

def _jit_pass_constant_propagation(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_pass_constant_propagation(arg0: torch::jit::Graph) -> None """
    pass

def _jit_pass_create_autodiff_subgraphs(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_pass_create_autodiff_subgraphs(arg0: torch::jit::Graph) -> None """
    pass

def _jit_pass_cse(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_pass_cse(arg0: torch::jit::Graph) -> None """
    pass

def _jit_pass_custom_pattern_based_rewrite(arg0, arg1, arg2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_pass_custom_pattern_based_rewrite(arg0: str, arg1: str, arg2: torch::jit::script::Module) -> None """
    pass

def _jit_pass_custom_pattern_based_rewrite_graph(arg0, arg1, arg2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_pass_custom_pattern_based_rewrite_graph(arg0: str, arg1: str, arg2: torch::jit::Graph) -> None """
    pass

def _jit_pass_dce(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_pass_dce(arg0: torch::jit::Graph) -> None """
    pass

def _jit_pass_dce_allow_deleting_nodes_with_side_effects(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_pass_dce_allow_deleting_nodes_with_side_effects(arg0: torch::jit::Graph) -> None """
    pass

def _jit_pass_decompose_ops(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_pass_decompose_ops(arg0: torch::jit::Graph) -> None """
    pass

def _jit_pass_erase_number_types(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_pass_erase_number_types(arg0: torch::jit::Graph) -> None """
    pass

def _jit_pass_erase_shape_information(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_pass_erase_shape_information(arg0: torch::jit::Graph) -> None """
    pass

def _jit_pass_fixup_onnx_loops(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_pass_fixup_onnx_loops(arg0: torch::jit::Graph) -> None """
    pass

def _jit_pass_fold_convbn(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_pass_fold_convbn(arg0: torch::jit::script::Module) -> None """
    pass

def _jit_pass_fold_quantize(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_pass_fold_quantize(arg0: torch::jit::script::Module, arg1: str) -> None """
    pass

def _jit_pass_fold_quant_inputs(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_pass_fold_quant_inputs(arg0: torch::jit::Graph) -> None """
    pass

def _jit_pass_fuse(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_pass_fuse(arg0: torch::jit::Graph) -> None """
    pass

def _jit_pass_fuse_linear(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_pass_fuse_linear(arg0: torch::jit::Graph) -> None """
    pass

def _jit_pass_inline(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_pass_inline(arg0: torch::jit::Graph) -> None """
    pass

def _jit_pass_inline_fork_wait(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_pass_inline_fork_wait(arg0: torch::jit::Graph) -> None """
    pass

def _jit_pass_insert_observers(module, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_pass_insert_observers(module: torch::jit::script::Module, method_name: str, qconfig_dict: dict, inplace: bool = False) -> torch::jit::script::Module """
    pass

def _jit_pass_insert_quant_dequant(module, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_pass_insert_quant_dequant(module: torch::jit::script::Module, method_name: str, inplace: bool = False) -> torch::jit::script::Module """
    pass

def _jit_pass_lint(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_pass_lint(arg0: torch::jit::Graph) -> None """
    pass

def _jit_pass_loop_unrolling(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_pass_loop_unrolling(arg0: torch::jit::Graph) -> None """
    pass

def _jit_pass_lower_all_tuples(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_pass_lower_all_tuples(arg0: torch::jit::Graph) -> None """
    pass

def _jit_pass_onnx(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_pass_onnx(arg0: torch::jit::Graph, arg1: torch._C._onnx.OperatorExportTypes) -> torch::jit::Graph """
    pass

def _jit_pass_onnx_block(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_pass_onnx_block(arg0: torch::jit::Block, arg1: torch::jit::Block, arg2: torch._C._onnx.OperatorExportTypes, arg3: Dict[torch::jit::Value, torch::jit::Value]) -> None """
    pass

def _jit_pass_onnx_cast_all_constant_to_floating(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_pass_onnx_cast_all_constant_to_floating(arg0: torch::jit::Graph) -> None """
    pass

def _jit_pass_onnx_constant_fold(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_pass_onnx_constant_fold(arg0: torch::jit::Graph, arg1: Dict[str, at::Tensor], arg2: int) -> Dict[str, at::Tensor] """
    pass

def _jit_pass_onnx_peephole(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_pass_onnx_peephole(arg0: torch::jit::Graph, arg1: int, arg2: bool) -> None """
    pass

def _jit_pass_onnx_preprocess_caffe2(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_pass_onnx_preprocess_caffe2(arg0: torch::jit::Graph) -> None """
    pass

def _jit_pass_onnx_remove_print(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_pass_onnx_remove_print(arg0: torch::jit::Graph) -> None """
    pass

def _jit_pass_onnx_scalar_type_analysis(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_pass_onnx_scalar_type_analysis(arg0: torch::jit::Graph) -> None """
    pass

def _jit_pass_pattern_based_rewrite(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_pass_pattern_based_rewrite(arg0: torch::jit::script::Module) -> torch::jit::script::Module """
    pass

def _jit_pass_peephole(graph, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_pass_peephole(graph: torch::jit::Graph, addmm_fusion_enabled: bool = False) -> None """
    pass

def _jit_pass_prepare_division_for_onnx(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_pass_prepare_division_for_onnx(arg0: torch::jit::Graph) -> None """
    pass

def _jit_pass_quant_fusion(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_pass_quant_fusion(arg0: torch::jit::Graph) -> None """
    pass

def _jit_pass_remove_expands(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_pass_remove_expands(arg0: torch::jit::Graph) -> None """
    pass

def _jit_pass_remove_inplace_ops(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_pass_remove_inplace_ops(arg0: torch::jit::Graph) -> None """
    pass

def _jit_pass_specialize_autogradzero(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_pass_specialize_autogradzero(arg0: torch::jit::Graph) -> None """
    pass

def _jit_run_cpp_tests(run_cuda): # real signature unknown; restored from __doc__
    """ _jit_run_cpp_tests(run_cuda: bool) -> None """
    pass

def _jit_script_class_compile(arg0, arg1, arg2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_script_class_compile(arg0: str, arg1: torch._C._jit_tree_views.ClassDef, arg2: Callable[[str], function]) -> None """
    pass

def _jit_script_compile(arg0, arg1, arg2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_script_compile(arg0: str, arg1: torch._C._jit_tree_views.Def, arg2: Callable[[str], function], arg3: Dict[str, object]) -> torch._C.Function """
    pass

def _jit_script_compile_overload(arg0, arg1, arg2, arg3, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_script_compile_overload(arg0: str, arg1: torch._C._jit_tree_views.Decl, arg2: torch._C._jit_tree_views.Def, arg3: Callable[[str], function], arg4: Dict[str, object]) -> torch._C.Function """
    pass

def _jit_script_interface_compile(arg0, arg1, arg2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_script_interface_compile(arg0: str, arg1: torch._C._jit_tree_views.ClassDef, arg2: Callable[[str], function]) -> None """
    pass

def _jit_set_emit_hooks(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_set_emit_hooks(arg0: Callable[[torch._C.ScriptModule], None], arg1: Callable[[torch._C.Function], None]) -> None """
    pass

def _jit_set_inline_everything_mode(arg0): # real signature unknown; restored from __doc__
    """ _jit_set_inline_everything_mode(arg0: bool) -> None """
    pass

def _jit_set_profiling_mode(arg0): # real signature unknown; restored from __doc__
    """ _jit_set_profiling_mode(arg0: bool) -> None """
    pass

def _jit_try_infer_type(arg0): # real signature unknown; restored from __doc__
    """ _jit_try_infer_type(arg0: object) -> c10::Type """
    pass

def _jit_unflatten(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _jit_unflatten(arg0: List[torch::autograd::Variable], arg1: torch._C.IODescriptor) -> object """
    pass

def _last_executed_optimized_graph(): # real signature unknown; restored from __doc__
    """
    _last_executed_optimized_graph() -> torch._C.Graph
    
    Retrieve the optimized graph that was run the last time the graph executor ran on this thread
    """
    pass

def _logging_set_logger(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _logging_set_logger(arg0: torch::jit::logging::LoggerBase) -> torch::jit::logging::LoggerBase """
    pass

def _log_api_usage_once(arg0): # real signature unknown; restored from __doc__
    """ _log_api_usage_once(arg0: str) -> None """
    pass

def _multiprocessing_init(*args, **kwargs): # real signature unknown
    pass

def _parallel_info(*args, **kwargs): # real signature unknown
    pass

def _propagate_and_assign_input_shapes(arg0, arg1, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _propagate_and_assign_input_shapes(arg0: torch._C.Graph, arg1: List[at::Tensor], arg2: bool, arg3: bool) -> torch._C.Graph """
    pass

def _propagate_shapes(arg0, arg1, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _propagate_shapes(arg0: torch._C.Graph, arg1: List[at::Tensor], arg2: bool) -> torch._C.Graph """
    pass

def _remove_worker_pids(*args, **kwargs): # real signature unknown
    pass

def _replace_overloaded_method_decl(arg0, arg1, arg2): # real signature unknown; restored from __doc__
    """ _replace_overloaded_method_decl(arg0: torch._C._jit_tree_views.Decl, arg1: torch._C._jit_tree_views.Def, arg2: str) -> torch._C._jit_tree_views.Def """
    pass

def _resolve_type(arg0, arg1, arg2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _resolve_type(arg0: str, arg1: torch._C._jit_tree_views.SourceRange, arg2: Callable[[str], function]) -> torch._C.Type """
    pass

def _safe_call(*args, **kwargs): # real signature unknown
    pass

def _scatter(tensor, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _scatter(tensor: at::Tensor, devices: List[int], chunk_sizes: Optional[List[int]], dim: int, streams: Optional[object]) -> List[at::Tensor] """
    pass

def _set_backcompat_broadcast_warn(*args, **kwargs): # real signature unknown
    pass

def _set_backcompat_keepdim_warn(*args, **kwargs): # real signature unknown
    pass

def _set_cudnn_benchmark(*args, **kwargs): # real signature unknown
    pass

def _set_cudnn_deterministic(*args, **kwargs): # real signature unknown
    pass

def _set_cudnn_enabled(*args, **kwargs): # real signature unknown
    pass

def _set_default_dtype(*args, **kwargs): # real signature unknown
    pass

def _set_default_tensor_type(*args, **kwargs): # real signature unknown
    pass

def _set_graph_executor_optimize(arg0): # real signature unknown; restored from __doc__
    """ _set_graph_executor_optimize(arg0: bool) -> None """
    pass

def _set_mkldnn_enabled(*args, **kwargs): # real signature unknown
    pass

def _set_qengine(*args, **kwargs): # real signature unknown
    pass

def _set_tracing_state(arg0): # real signature unknown; restored from __doc__
    """ _set_tracing_state(arg0: torch._C.TracingState) -> None """
    pass

def _set_value_trace(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _set_value_trace(arg0: torch::autograd::Variable, arg1: torch._C.Value) -> None """
    pass

def _set_worker_pids(*args, **kwargs): # real signature unknown
    pass

def _set_worker_signal_handlers(*args, **kwargs): # real signature unknown
    pass

def _show_config(*args, **kwargs): # real signature unknown
    pass

def _supported_qengines(*args, **kwargs): # real signature unknown
    pass

def _tensor_impl_raw_handle(arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _tensor_impl_raw_handle(arg0: torch::autograd::Variable) -> capsule """
    pass

def _to_dlpack(*args, **kwargs): # real signature unknown
    pass

def _tracer_abandon(): # real signature unknown; restored from __doc__
    """ _tracer_abandon() -> None """
    pass

def _tracer_enter(*args): # real signature unknown; restored from __doc__
    """ _tracer_enter(*args) -> Tuple[torch._C.TracingState, List[IValue]] """
    pass

def _tracer_exit(arg0): # real signature unknown; restored from __doc__
    """ _tracer_exit(arg0: tuple) -> None """
    pass

def _tracer_set_force_outplace(arg0): # real signature unknown; restored from __doc__
    """ _tracer_set_force_outplace(arg0: bool) -> None """
    pass

def _tracer_set_get_unique_name_fn(arg0): # real signature unknown; restored from __doc__
    """ _tracer_set_get_unique_name_fn(arg0: function) -> None """
    pass

def _tracer_warn_use_python(): # real signature unknown; restored from __doc__
    """ _tracer_warn_use_python() -> None """
    pass

def _wrap_tensor_impl(arg0): # real signature unknown; restored from __doc__
    """ _wrap_tensor_impl(arg0: capsule) -> object """
    return object()

# classes

from .AggregationType import AggregationType
from .Argument import Argument
from .ArgumentSpec import ArgumentSpec
from .BenchmarkConfig import BenchmarkConfig
from .BenchmarkExecutionStats import BenchmarkExecutionStats
from .BFloat16StorageBase import BFloat16StorageBase
from .Block import Block
from .BoolStorageBase import BoolStorageBase
from .Type import Type
from .BoolType import BoolType
from .ByteStorageBase import ByteStorageBase
from .CharStorageBase import CharStorageBase
from .ClassType import ClassType
from .Code import Code
from .CompilationUnit import CompilationUnit
from .CompleteArgumentSpec import CompleteArgumentSpec
from .CudaBFloat16StorageBase import CudaBFloat16StorageBase
from .CudaBoolStorageBase import CudaBoolStorageBase
from .CudaByteStorageBase import CudaByteStorageBase
from .CudaCharStorageBase import CudaCharStorageBase
from .CudaDoubleStorageBase import CudaDoubleStorageBase
from .CudaFloatStorageBase import CudaFloatStorageBase
from .CudaHalfStorageBase import CudaHalfStorageBase
from .CudaIntStorageBase import CudaIntStorageBase
from .CudaLongStorageBase import CudaLongStorageBase
from .CudaShortStorageBase import CudaShortStorageBase
from .device import device
from .DictType import DictType
from .DoubleStorageBase import DoubleStorageBase
from .dtype import dtype
from .ErrorReport import ErrorReport
from .ExecutionPlan import ExecutionPlan
from .ExtraFilesMap import ExtraFilesMap
from .FatalError import FatalError
from .FileCheck import FileCheck
from .finfo import finfo
from .FloatStorageBase import FloatStorageBase
from .FloatType import FloatType
from .Function import Function
from .FunctionSchema import FunctionSchema
from .Future import Future
from .Generator import Generator
from .Gradient import Gradient
from .Graph import Graph
from .GraphExecutorState import GraphExecutorState
from .HalfStorageBase import HalfStorageBase
from .iinfo import iinfo
from .IntStorageBase import IntStorageBase
from .IntType import IntType
from .IODescriptor import IODescriptor
from .JITException import JITException
from .layout import layout
from .ListType import ListType
from .LoggerBase import LoggerBase
from .LockingLogger import LockingLogger
from .LongStorageBase import LongStorageBase
from .memory_format import memory_format
from .Node import Node
from .NoopLogger import NoopLogger
from .NumberType import NumberType
from .OptionalType import OptionalType
from .PyTorchFileReader import PyTorchFileReader
from .PyTorchFileWriter import PyTorchFileWriter
from .QInt32StorageBase import QInt32StorageBase
from .QInt8StorageBase import QInt8StorageBase
from .qscheme import qscheme
from .QUInt8StorageBase import QUInt8StorageBase
from .ScriptMethod import ScriptMethod
from .ScriptModule import ScriptModule
from .ShortStorageBase import ShortStorageBase
from .Size import Size
from .StringType import StringType
from .TensorType import TensorType
from .ThroughputBenchmark import ThroughputBenchmark
from .TracingState import TracingState
from .TupleType import TupleType
from .Use import Use
from .Value import Value
from ._CudaEventBase import _CudaEventBase
from ._CudaStreamBase import _CudaStreamBase
from ._FunctionBase import _FunctionBase
from ._ImperativeEngine import _ImperativeEngine
from ._LegacyVariableBase import _LegacyVariableBase
from ._TensorBase import _TensorBase
from ._VariableFunctions import _VariableFunctions
# variables with complex values

AVG = None # (!) real value is 'AggregationType.AVG'

default_generator = None # (!) real value is '<torch._C.Generator object at 0x000002E10E4088F0>'

SUM = None # (!) real value is 'AggregationType.SUM'

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000002E17F17E908>'

__spec__ = None # (!) real value is "ModuleSpec(name='torch._C', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000002E17F17E908>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\torch\\\\_C.cp37-win_amd64.pyd')"

