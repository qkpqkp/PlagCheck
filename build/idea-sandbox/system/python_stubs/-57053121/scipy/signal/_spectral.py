# encoding: utf-8
# module scipy.signal._spectral
# from C:\Users\Doly\Anaconda3\lib\site-packages\scipy\signal\_spectral.cp37-win_amd64.pyd
# by generator 1.147
""" Tools for spectral analysis of unequally sampled signals. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py

# functions

def _lombscargle(x, y, freqs): # real signature unknown; restored from __doc__
    """
    _lombscargle(x, y, freqs)
    
        Computes the Lomb-Scargle periodogram.
    
        Parameters
        ----------
        x : array_like
            Sample times.
        y : array_like
            Measurement values (must be registered so the mean is zero).
        freqs : array_like
            Angular frequencies for output periodogram.
    
        Returns
        -------
        pgram : array_like
            Lomb-Scargle periodogram.
    
        Raises
        ------
        ValueError
            If the input arrays `x` and `y` do not have the same shape.
    
        See also
        --------
        lombscargle
    """
    pass

# no classes
# variables with complex values

__all__ = [
    '_lombscargle',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001FE4FB0E2B0>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.signal._spectral', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001FE4FB0E2B0>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\scipy\\\\signal\\\\_spectral.cp37-win_amd64.pyd')"

__test__ = {}

