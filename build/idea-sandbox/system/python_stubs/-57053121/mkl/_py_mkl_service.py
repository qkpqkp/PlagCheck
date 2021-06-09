# encoding: utf-8
# module mkl._py_mkl_service
# from C:\Users\Doly\Anaconda3\lib\site-packages\mkl\_py_mkl_service.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import six as six # C:\Users\Doly\.gradle\caches\modules-2\files-2.1\com.jetbrains.intellij.pycharm\pycharmPC\2020.3.2\bd70959d1ca4719d9c59fc98a65180388824b26d\pycharmPC-2020.3.2\plugins\python-ce\helpers\six.py
import warnings as warnings # C:\Users\Doly\Anaconda3\lib\warnings.py

# functions

def cbwr_get(*args, **kwargs): # real signature unknown
    """
    Returns the current CNR settings.
        https://software.intel.com/en-us/mkl-developer-reference-c-mkl-cbwr-get
    """
    pass

def cbwr_get_auto_branch(*args, **kwargs): # real signature unknown
    """
    Automatically detects the CNR code branch for your platform.
        https://software.intel.com/en-us/mkl-developer-reference-c-mkl-cbwr-get-auto-branch
    """
    pass

def cbwr_set(*args, **kwargs): # real signature unknown
    """
    Configures the CNR mode of Intel(R) MKL.
        https://software.intel.com/en-us/mkl-developer-reference-c-mkl-cbwr-set
    """
    pass

def disable_fast_mm(*args, **kwargs): # real signature unknown
    """
    Turns off the Intel(R) MKL Memory Allocator for Intel(R) MKL functions to directly use the system malloc/free functions.
        https://software.intel.com/en-us/mkl-developer-reference-c-mkl-disable-fast-mm
    """
    pass

def domain_get_max_threads(*args, **kwargs): # real signature unknown
    """
    Gets the number of OpenMP* threads targeted for parallelism for a particular function domain.
        https://software.intel.com/en-us/mkl-developer-reference-c-mkl-domain-get-max-threads
    """
    pass

def domain_set_num_threads(*args, **kwargs): # real signature unknown
    """
    Specifies the number of OpenMP* threads for a particular function domain.
        https://software.intel.com/en-us/mkl-developer-reference-c-mkl-domain-set-num-threads
    """
    pass

def dsecnd(*args, **kwargs): # real signature unknown
    """
    Returns elapsed time in seconds.
        Use to estimate real time between two calls to this function.
        https://software.intel.com/en-us/mkl-developer-reference-c-second/dsecnd
    """
    pass

def enable_instructions(*args, **kwargs): # real signature unknown
    """
    Enables dispatching for new Intel architectures or restricts the set of Intel instruction sets available for dispatching.
        https://software.intel.com/en-us/mkl-developer-reference-c-mkl-enable-instructions
    """
    pass

def free_buffers(*args, **kwargs): # real signature unknown
    """
    Frees unused memory allocated by the Intel(R) MKL Memory Allocator.
        https://software.intel.com/en-us/mkl-developer-reference-c-mkl-free-buffers
    """
    pass

def get_clocks_frequency(*args, **kwargs): # real signature unknown
    """
    Returns the frequency value in GHz based on constant-rate Time Stamp Counter.
        https://software.intel.com/en-us/mkl-developer-reference-c-mkl-get-clocks-frequency
    """
    pass

def get_cpu_clocks(*args, **kwargs): # real signature unknown
    """
    Returns elapsed CPU clocks.
        https://software.intel.com/en-us/mkl-developer-reference-c-mkl-get-cpu-clocks
    """
    pass

def get_cpu_frequency(*args, **kwargs): # real signature unknown
    """
    Returns the current CPU frequency value in GHz.
        https://software.intel.com/en-us/mkl-developer-reference-c-mkl-get-cpu-frequency
    """
    pass

def get_dynamic(*args, **kwargs): # real signature unknown
    """
    Determines whether Intel(R) MKL is enabled to dynamically change the number of OpenMP* threads.
        https://software.intel.com/en-us/mkl-developer-reference-c-mkl-get-dynamic
    """
    pass

def get_env_mode(*args, **kwargs): # real signature unknown
    """
    Query the current environment mode. See mkl_set_env_mode(0).
        https://software.intel.com/en-us/mkl-developer-reference-c-mkl-set-env-mode
    """
    pass

def get_max_cpu_frequency(*args, **kwargs): # real signature unknown
    """
    Returns the maximum CPU frequency value in GHz.
        https://software.intel.com/en-us/mkl-developer-reference-c-mkl-get-max-cpu-frequency
    """
    pass

def get_max_threads(*args, **kwargs): # real signature unknown
    """
    Gets the number of OpenMP* threads targeted for parallelism.
        https://software.intel.com/en-us/mkl-developer-reference-c-mkl-get-max-threads
    """
    pass

def get_version(*args, **kwargs): # real signature unknown
    """
    Returns the Intel(R) MKL version as a dictionary.
        https://software.intel.com/en-us/mkl-developer-reference-c-mkl-get-version
    """
    pass

def get_version_string(*args, **kwargs): # real signature unknown
    """
    Returns the Intel(R) MKL version as a string.
        https://software.intel.com/en-us/mkl-developer-reference-c-mkl-get-version-string
    """
    pass

def mem_stat(*args, **kwargs): # real signature unknown
    """
    Reports the status of the Intel(R) MKL Memory Allocator.
        https://software.intel.com/en-us/mkl-developer-reference-c-mkl-mem-stat
    """
    pass

def peak_mem_usage(*args, **kwargs): # real signature unknown
    """
    Reports the peak memory allocated by the Intel(R) MKL Memory Allocator.
        https://software.intel.com/en-us/mkl-developer-reference-c-mkl-peak-mem-usage
    """
    pass

def second(*args, **kwargs): # real signature unknown
    """
    Returns elapsed time in seconds.
        Use to estimate real time between two calls to this function.
        https://software.intel.com/en-us/mkl-developer-reference-c-second/dsecnd
    """
    pass

def set_dynamic(*args, **kwargs): # real signature unknown
    """
    Enables Intel(R) MKL to dynamically change the number of OpenMP* threads.
        https://software.intel.com/en-us/mkl-developer-reference-c-mkl-set-dynamic
    """
    pass

def set_env_mode(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Sets up the mode that ignores environment settings specific to Intel(R) MKL. See mkl_set_env_mode(1).
        https://software.intel.com/en-us/mkl-developer-reference-c-mkl-set-env-mode
    """
    pass

def set_memory_limit(*args, **kwargs): # real signature unknown
    """
    On Linux, sets the limit of memory that Intel(R) MKL can allocate for a specified type of memory.
        https://software.intel.com/en-us/mkl-developer-reference-c-mkl-set-memory-limit
    """
    pass

def set_mpi(*args, **kwargs): # real signature unknown
    """
    Sets the implementation of the message-passing interface to be used by Intel(R) MKL.
        https://software.intel.com/en-us/mkl-developer-reference-c-mkl-set-mpi
    """
    pass

def set_num_threads(*args, **kwargs): # real signature unknown
    """
    Specifies the number of OpenMP* threads to use.
        https://software.intel.com/en-us/mkl-developer-reference-c-mkl-set-num-threads
    """
    pass

def set_num_threads_local(*args, **kwargs): # real signature unknown
    """
    Specifies the number of OpenMP* threads for all Intel(R) MKL functions on the current execution thread.
        https://software.intel.com/en-us/mkl-developer-reference-c-mkl-set-num-threads-local
    """
    pass

def thread_free_buffers(*args, **kwargs): # real signature unknown
    """
    Frees unused memory allocated by the Intel(R) MKL Memory Allocator in the current thread.
        https://software.intel.com/en-us/mkl-developer-reference-c-mkl-thread-free-buffers
    """
    pass

def verbose(*args, **kwargs): # real signature unknown
    """
    Enables or disables Intel(R) MKL Verbose mode.
        https://software.intel.com/en-us/mkl-developer-reference-c-mkl-verbose
    """
    pass

def vml_clear_err_status(*args, **kwargs): # real signature unknown
    """
    Sets the VM Error Status to VML_STATUS_OK and stores the previous VM Error Status to olderr.
        https://software.intel.com/en-us/mkl-developer-reference-c-vmlclearerrstatus
    """
    pass

def vml_get_err_status(*args, **kwargs): # real signature unknown
    """
    Gets the VM Error Status.
        https://software.intel.com/en-us/mkl-developer-reference-c-vmlgeterrstatus
    """
    pass

def vml_get_mode(*args, **kwargs): # real signature unknown
    """
    Gets the VM mode.
        https://software.intel.com/en-us/mkl-developer-reference-c-vmlgetmode
    """
    pass

def vml_set_err_status(*args, **kwargs): # real signature unknown
    """
    Sets the new VM Error Status according to err and stores the previous VM Error Status to olderr.
        https://software.intel.com/en-us/mkl-developer-reference-c-vmlseterrstatus
    """
    pass

def vml_set_mode(*args, **kwargs): # real signature unknown
    """
    Sets a new mode for VM functions according to the mode parameter and stores the previous VM mode to oldmode.
        https://software.intel.com/en-us/mkl-developer-reference-c-vmlsetmode
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000019F446D95F8>'

__mkl_vml_status = {
    'accuracywarning': 1000,
    'badmem': -2,
    'badsize': -1,
    'errdom': 1,
    'ok': 0,
    'overflow': 3,
    'sing': 2,
    'underflow': 4,
}

__spec__ = None # (!) real value is "ModuleSpec(name='mkl._py_mkl_service', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000019F446D95F8>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\mkl\\\\_py_mkl_service.cp37-win_amd64.pyd')"

__test__ = {}

