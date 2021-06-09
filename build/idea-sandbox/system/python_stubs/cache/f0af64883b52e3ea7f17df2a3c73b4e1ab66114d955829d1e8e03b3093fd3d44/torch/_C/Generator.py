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


from .object import object

class Generator(object):
    """
    Generator(device='cpu') -> Generator
    
    Creates and returns a generator object which manages the state of the algorithm that
    produces pseudo random numbers. Used as a keyword argument in many :ref:`inplace-random-sampling`
    functions.
    
    Arguments:
        device (:class:`torch.device`, optional): the desired device for the generator.
    
    Returns:
        Generator: An torch.Generator object.
    
    Example::
    
        >>> g_cpu = torch.Generator()
        >>> g_cuda = torch.Generator(device='cuda')
    """
    def get_state(self): # real signature unknown; restored from __doc__
        """
        Generator.get_state() -> Tensor
        
        Returns the Generator state as a ``torch.ByteTensor``.
        
        Returns:
            Tensor: A ``torch.ByteTensor`` which contains all the necessary bits
            to restore a Generator to a specific point in time.
        
        Example::
        
            >>> g_cpu = torch.Generator()
            >>> g_cpu.get_state()
        """
        pass

    def initial_seed(self): # real signature unknown; restored from __doc__
        """
        Generator.initial_seed() -> int
        
        Returns the initial seed for generating random numbers.
        
        Example::
        
            >>> g_cpu = torch.Generator()
            >>> g_cpu.initial_seed()
            2147483647
        """
        return 0

    def manual_seed(self, seed): # real signature unknown; restored from __doc__
        """
        Generator.manual_seed(seed) -> Generator
        
        Sets the seed for generating random numbers. Returns a `torch.Generator` object.
        It is recommended to set a large seed, i.e. a number that has a good balance of 0
        and 1 bits. Avoid having many 0 bits in the seed.
        
        Arguments:
            seed (int): The desired seed.
        
        Returns:
            Generator: An torch.Generator object.
        
        Example::
        
            >>> g_cpu = torch.Generator()
            >>> g_cpu.manual_seed(2147483647)
        """
        return Generator

    def seed(self): # real signature unknown; restored from __doc__
        """
        Generator.seed() -> int
        
        Gets a non-deterministic random number from std::random_device or the current
        time and uses it to seed a Generator.
        
        Example::
        
            >>> g_cpu = torch.Generator()
            >>> g_cpu.seed()
            1516516984916
        """
        return 0

    def set_state(self, new_state): # real signature unknown; restored from __doc__
        """
        Generator.set_state(new_state) -> void
        
        Sets the Generator state.
        
        Arguments:
            new_state (torch.ByteTensor): The desired state.
        
        Example::
        
            >>> g_cpu = torch.Generator()
            >>> g_cpu_other = torch.Generator()
            >>> g_cpu.set_state(g_cpu_other.get_state())
        """
        pass

    def __init__(self, device='cpu'): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    device = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
Generator.device -> device

Gets the current device of the generator.

Example::

    >>> g_cpu = torch.Generator()
    >>> g_cpu.device
    device(type='cpu')
"""

    _cdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



