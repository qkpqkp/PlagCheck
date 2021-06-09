# encoding: utf-8
# module pywt._extensions._swt
# from C:\Users\Doly\Anaconda3\lib\site-packages\pywt\_extensions\_swt.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import warnings as warnings # C:\Users\Doly\Anaconda3\lib\warnings.py
import numpy as np # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py

# functions

def swt(*args, **kwargs): # real signature unknown
    pass

def swt_axis(*args, **kwargs): # real signature unknown
    pass

def swt_max_level(input_len): # real signature unknown; restored from __doc__
    """
    swt_max_level(input_len)
    
        Calculates the maximum level of Stationary Wavelet Transform for data of
        given length.
    
        Parameters
        ----------
        input_len : int
            Input data length.
    
        Returns
        -------
        max_level : int
            Maximum level of Stationary Wavelet Transform for data of given length.
    
        Notes
        -----
        For the current implementation of the stationary wavelet transform, this
        corresponds to the number of times ``input_len`` is evenly divisible by
        two. In other words, for an n-level transform, the signal length must be a
        multiple of ``2**n``. ``numpy.pad`` can be used to pad a signal up to an
        appropriate length as needed.
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000165D82B97F0>'

__spec__ = None # (!) real value is "ModuleSpec(name='pywt._extensions._swt', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000165D82B97F0>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\pywt\\\\_extensions\\\\_swt.cp37-win_amd64.pyd')"

__test__ = {}

