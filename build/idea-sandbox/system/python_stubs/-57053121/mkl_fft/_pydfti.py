# encoding: utf-8
# module mkl_fft._pydfti
# from C:\Users\Doly\Anaconda3\lib\site-packages\mkl_fft\_pydfti.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py
from numpy.core._multiarray_tests import internal_overlap

from _thread import Lock


# functions

def fft(*args, **kwargs): # real signature unknown
    pass

def fft2(*args, **kwargs): # real signature unknown
    pass

def fftn(*args, **kwargs): # real signature unknown
    pass

def ifft(*args, **kwargs): # real signature unknown
    pass

def ifft2(*args, **kwargs): # real signature unknown
    pass

def ifftn(*args, **kwargs): # real signature unknown
    pass

def irfft(*args, **kwargs): # real signature unknown
    """ Inverse FFT of a real sequence, takes packed real-valued harmonics of FFT """
    pass

def irfft2_numpy(*args, **kwargs): # real signature unknown
    pass

def irfftn_numpy(*args, **kwargs): # real signature unknown
    pass

def irfft_numpy(*args, **kwargs): # real signature unknown
    pass

def rfft(*args, **kwargs): # real signature unknown
    """ Packed real-valued harmonics of FFT of a real sequence x """
    pass

def rfft2_numpy(*args, **kwargs): # real signature unknown
    pass

def rfftn_numpy(*args, **kwargs): # real signature unknown
    pass

def rfft_numpy(*args, **kwargs): # real signature unknown
    pass

def _check_shapes_for_direct(*args, **kwargs): # real signature unknown
    pass

def _cook_nd_args(*args, **kwargs): # real signature unknown
    pass

def _direct_fftnd(*args, **kwargs): # real signature unknown
    """ Perform n-dimensional FFT over all axes """
    pass

def _fft1d_impl(*args, **kwargs): # real signature unknown
    """ Uses MKL to perform 1D FFT on the input array x along the given axis. """
    pass

def _fftnd_impl(*args, **kwargs): # real signature unknown
    pass

def _fix_dimensions(*args, **kwargs): # real signature unknown
    """ Pads array arr with zeros to attain shape s associated with axes """
    pass

def _init_nd_shape_and_axes(*args, **kwargs): # real signature unknown
    """
    Handle shape and axes arguments for n-dimensional transforms.
        Returns the shape and axes in a standard form, taking into account negative
        values and checking for various potential errors.
        Parameters
        ----------
        x : array_like
            The input array.
        shape : int or array_like of ints or None
            The shape of the result.  If both `shape` and `axes` (see below) are
            None, `shape` is ``x.shape``; if `shape` is None but `axes` is
            not None, then `shape` is ``scipy.take(x.shape, axes, axis=0)``.
            If `shape` is -1, the size of the corresponding dimension of `x` is
            used.
        axes : int or array_like of ints or None
            Axes along which the calculation is computed.
            The default is over all axes.
            Negative indices are automatically converted to their positive
            counterpart.
        Returns
        -------
        shape : array
            The shape of the result. It is a 1D integer array.
        axes : array
            The shape of the result. It is a 1D integer array.
    """
    pass

def _iter_fftnd(*args, **kwargs): # real signature unknown
    pass

def _rc_fft1d_impl(*args, **kwargs): # real signature unknown
    """
    Uses MKL to perform 1D FFT on the real input array x along the given axis,
        producing complex output, but giving only half of the harmonics.
    
        cf. numpy.fft.rfft
    """
    pass

def _rc_ifft1d_impl(*args, **kwargs): # real signature unknown
    """
    Uses MKL to perform 1D FFT on the real input array x along the given axis,
        producing complex output, but giving only half of the harmonics.
    
        cf. numpy.fft.rfft
    """
    pass

def _remove_axis(*args, **kwargs): # real signature unknown
    pass

def _rrfft1d_impl(*args, **kwargs): # real signature unknown
    """ Uses MKL to perform real packed 1D FFT on the input array x along the given axis. """
    pass

# no classes
# variables with complex values

_lock = None # (!) real value is '<unlocked _thread.lock object at 0x000001F3D9B3A2D8>'

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001F3CB25EF28>'

__spec__ = None # (!) real value is "ModuleSpec(name='mkl_fft._pydfti', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001F3CB25EF28>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\mkl_fft\\\\_pydfti.cp37-win_amd64.pyd')"

__test__ = {}

