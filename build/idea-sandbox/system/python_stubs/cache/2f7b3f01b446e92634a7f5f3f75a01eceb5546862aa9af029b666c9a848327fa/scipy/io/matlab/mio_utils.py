# encoding: utf-8
# module scipy.io.matlab.mio_utils
# from C:\Users\Doly\Anaconda3\lib\site-packages\scipy\io\matlab\mio_utils.cp37-win_amd64.pyd
# by generator 1.147
""" Utilities for generic processing of return arrays from read """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py

# functions

def chars_to_strings(*args, **kwargs): # real signature unknown
    """
    Convert final axis of char array to strings
    
        Parameters
        ----------
        in_arr : array
           dtype of 'U1'
    
        Returns
        -------
        str_arr : array
           dtype of 'UN' where N is the length of the last dimension of
           ``arr``
    """
    pass

def squeeze_element(*args, **kwargs): # real signature unknown
    """
    Return squeezed element
    
        The returned object may not be an ndarray - for example if we do
        ``arr.item`` to return a ``mat_struct`` object from a struct array
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000002DE4771A908>'

__pyx_capi__ = {
    'chars_to_strings': None, # (!) real value is '<capsule object "PyArrayObject *(PyObject *, int __pyx_skip_dispatch)" at 0x000002DE476AB780>'
    'squeeze_element': None, # (!) real value is '<capsule object "PyObject *(PyArrayObject *, int __pyx_skip_dispatch)" at 0x000002DE476AB750>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.io.matlab.mio_utils', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000002DE4771A908>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\scipy\\\\io\\\\matlab\\\\mio_utils.cp37-win_amd64.pyd')"

__test__ = {}

