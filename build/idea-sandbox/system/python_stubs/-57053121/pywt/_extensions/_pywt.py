# encoding: utf-8
# module pywt._extensions._pywt
# from C:\Users\Doly\Anaconda3\lib\site-packages\pywt\_extensions\_pywt.cp37-win_amd64.pyd
# by generator 1.147
""" Cython wrapper for low-level C wavelet transform implementation. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import warnings as warnings # C:\Users\Doly\Anaconda3\lib\warnings.py
import re as re # C:\Users\Doly\Anaconda3\lib\re.py
import numpy as np # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py

# Variables with simple values

_attr_deprecation_msg = '{old} has been renamed to {new} and will be unavailable in a future version of pywt.'

# functions

def DiscreteContinuousWavelet(name, filter_bank=None): # real signature unknown; restored from __doc__
    """
    DiscreteContinuousWavelet(name, filter_bank=None) returns a
        Wavelet or a ContinuousWavelet object depending of the given name.
    
        In order to use a built-in wavelet the parameter name must be
        a valid name from the wavelist() list.
        To create a custom wavelet object, filter_bank parameter must
        be specified. It can be either a list of four filters or an object
        that a `filter_bank` attribute which returns a list of four
        filters - just like the Wavelet instance itself.
    
        For a ContinuousWavelet, filter_bank cannot be used and must remain unset.
    """
    pass

def families(short=True): # real signature unknown; restored from __doc__
    """
    families(short=True)
    
        Returns a list of available built-in wavelet families.
    
        Currently the built-in families are:
    
        * Haar (``haar``)
        * Daubechies (``db``)
        * Symlets (``sym``)
        * Coiflets (``coif``)
        * Biorthogonal (``bior``)
        * Reverse biorthogonal (``rbio``)
        * `"Discrete"` FIR approximation of Meyer wavelet (``dmey``)
        * Gaussian wavelets (``gaus``)
        * Mexican hat wavelet (``mexh``)
        * Morlet wavelet (``morl``)
        * Complex Gaussian wavelets (``cgau``)
        * Shannon wavelets (``shan``)
        * Frequency B-Spline wavelets (``fbsp``)
        * Complex Morlet wavelets (``cmor``)
    
        Parameters
        ----------
        short : bool, optional
            Use short names (default: True).
    
        Returns
        -------
        families : list
            List of available wavelet families.
    
        Examples
        --------
        >>> import pywt
        >>> pywt.families()
        ['haar', 'db', 'sym', 'coif', 'bior', 'rbio', 'dmey', 'gaus', 'mexh', 'morl', 'cgau', 'shan', 'fbsp', 'cmor']
        >>> pywt.families(short=False)
        ['Haar', 'Daubechies', 'Symlets', 'Coiflets', 'Biorthogonal', 'Reverse biorthogonal', 'Discrete Meyer (FIR Approximation)', 'Gaussian', 'Mexican hat wavelet', 'Morlet wavelet', 'Complex Gaussian wavelets', 'Shannon wavelets', 'Frequency B-Spline wavelets', 'Complex Morlet wavelets']
    """
    pass

def keep(*args, **kwargs): # real signature unknown
    pass

def wavelet_from_object(*args, **kwargs): # real signature unknown
    pass

def wavelist(family=None, kind='all'): # real signature unknown; restored from __doc__
    """
    wavelist(family=None, kind='all')
    
        Returns list of available wavelet names for the given family name.
    
        Parameters
        ----------
        family : str, optional
            Short family name. If the family name is None (default) then names
            of all the built-in wavelets are returned. Otherwise the function
            returns names of wavelets that belong to the given family.
            Valid names are::
    
                'haar', 'db', 'sym', 'coif', 'bior', 'rbio', 'dmey', 'gaus',
                'mexh', 'morl', 'cgau', 'shan', 'fbsp', 'cmor'
    
        kind : {'all', 'continuous', 'discrete'}, optional
            Whether to return only wavelet names of discrete or continuous
            wavelets, or all wavelets.  Default is ``'all'``.
            Ignored if ``family`` is specified.
    
        Returns
        -------
        wavelist : list of str
            List of available wavelet names.
    
        Examples
        --------
        >>> import pywt
        >>> pywt.wavelist('coif')
        ['coif1', 'coif2', 'coif3', 'coif4', 'coif5', 'coif6', 'coif7', ...
        >>> pywt.wavelist(kind='continuous')
        ['cgau1', 'cgau2', 'cgau3', 'cgau4', 'cgau5', 'cgau6', 'cgau7', ...
    """
    pass

def _check_dtype(*args, **kwargs): # real signature unknown
    """ Check for cA/cD input what (if any) the dtype is. """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class ContinuousWavelet(object):
    """
    ContinuousWavelet(name) object describe properties of
        a continuous wavelet identified by name.
    
        In order to use a built-in wavelet the parameter name must be
        a valid name from the wavelist() list.
    """
    def wavefun(self, level=8, length=None): # real signature unknown; restored from __doc__
        """
        wavefun(self, level=8, length=None)
        
                Calculates approximations of wavelet function (``psi``) on xgrid
                (``x``) at a given level of refinement or length itself.
        
                Parameters
                ----------
                level : int, optional
                    Level of refinement (default: 8). Defines the length by
                    ``2**level`` if length is not set.
                length : int, optional
                    Number of samples. If set to None, the length is set to
                    ``2**level`` instead.
        
                Returns
                -------
                psi : array_like
                    Wavelet function computed for grid xval
                xval : array_like
                    grid going from lower_bound to upper_bound
        
                Notes
                -----
                The effective support are set with ``lower_bound`` and ``upper_bound``.
                The wavelet function is complex for ``'cmor'``, ``'shan'``, ``'fbsp'``
                and ``'cgau'``.
        
                The complex frequency B-spline wavelet (``'fbsp'``) has
                ``bandwidth_frequency``, ``center_frequency`` and ``fbsp_order`` as
                additional parameters.
        
                The complex Shannon wavelet (``'shan'``) has ``bandwidth_frequency``
                and ``center_frequency`` as additional parameters.
        
                The complex Morlet wavelet (``'cmor'``) has ``bandwidth_frequency``
                and ``center_frequency`` as additional parameters.
        
                Examples
                --------
                >>> import pywt
                >>> import matplotlib.pyplot as plt
                >>> lb = -5
                >>> ub = 5
                >>> n = 1000
                >>> wavelet = pywt.ContinuousWavelet("gaus8")
                >>> wavelet.upper_bound = ub
                >>> wavelet.lower_bound = lb
                >>> [psi,xval] = wavelet.wavefun(length=n)
                >>> plt.plot(xval,psi) # doctest: +ELLIPSIS
                [<matplotlib.lines.Line2D object at ...>]
                >>> plt.title("Gaussian Wavelet of order 8") # doctest: +ELLIPSIS
                <matplotlib.text.Text object at ...>
                >>> plt.show() # doctest: +SKIP
        
                >>> import pywt
                >>> import matplotlib.pyplot as plt
                >>> lb = -5
                >>> ub = 5
                >>> n = 1000
                >>> wavelet = pywt.ContinuousWavelet("cgau4")
                >>> wavelet.upper_bound = ub
                >>> wavelet.lower_bound = lb
                >>> [psi,xval] = wavelet.wavefun(length=n)
                >>> plt.subplot(211) # doctest: +ELLIPSIS
                <matplotlib.axes._subplots.AxesSubplot object at ...>
                >>> plt.plot(xval,np.real(psi)) # doctest: +ELLIPSIS
                [<matplotlib.lines.Line2D object at ...>]
                >>> plt.title("Real part") # doctest: +ELLIPSIS
                <matplotlib.text.Text object at ...>
                >>> plt.subplot(212) # doctest: +ELLIPSIS
                <matplotlib.axes._subplots.AxesSubplot object at ...>
                >>> plt.plot(xval,np.imag(psi)) # doctest: +ELLIPSIS
                [<matplotlib.lines.Line2D object at ...>]
                >>> plt.title("Imaginary part") # doctest: +ELLIPSIS
                <matplotlib.text.Text object at ...>
                >>> plt.show() # doctest: +SKIP
        """
        pass

    def __init__(self, name): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    bandwidth_frequency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Bandwidth frequency (shan, fbsp, cmor)"""

    biorthogonal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is biorthogonal"""

    center_frequency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Center frequency (shan, fbsp, cmor)"""

    complex_cwt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """CWT is complex"""

    dt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    family_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Wavelet family name"""

    family_number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Wavelet family number"""

    fbsp_order = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """order parameter for fbsp"""

    lower_bound = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Lower Bound"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    orthogonal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is orthogonal"""

    short_family_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Short wavelet family name"""

    symmetry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Wavelet symmetry"""

    upper_bound = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Upper Bound"""



class Wavelet(object):
    """
    Wavelet(name, filter_bank=None) object describe properties of
        a wavelet identified by name.
    
        In order to use a built-in wavelet the parameter name must be
        a valid name from the wavelist() list.
        To create a custom wavelet object, filter_bank parameter must
        be specified. It can be either a list of four filters or an object
        that a `filter_bank` attribute which returns a list of four
        filters - just like the Wavelet instance itself.
    """
    def get_filters_coeffs(self, *args, **kwargs): # real signature unknown
        pass

    def get_reverse_filters_coeffs(self, *args, **kwargs): # real signature unknown
        pass

    def wavefun(self, level=8): # real signature unknown; restored from __doc__
        """
        wavefun(self, level=8)
        
                Calculates approximations of scaling function (`phi`) and wavelet
                function (`psi`) on xgrid (`x`) at a given level of refinement.
        
                Parameters
                ----------
                level : int, optional
                    Level of refinement (default: 8).
        
                Returns
                -------
                [phi, psi, x] : array_like
                    For orthogonal wavelets returns scaling function, wavelet function
                    and xgrid - [phi, psi, x].
        
                [phi_d, psi_d, phi_r, psi_r, x] : array_like
                    For biorthogonal wavelets returns scaling and wavelet function both
                    for decomposition and reconstruction and xgrid
        
                Examples
                --------
                >>> import pywt
                >>> # Orthogonal
                >>> wavelet = pywt.Wavelet('db2')
                >>> phi, psi, x = wavelet.wavefun(level=5)
                >>> # Biorthogonal
                >>> wavelet = pywt.Wavelet('bior3.5')
                >>> phi_d, psi_d, phi_r, psi_r, x = wavelet.wavefun(level=5)
        """
        pass

    def __init__(self, name, filter_bank=None): # real signature unknown; restored from __doc__
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    biorthogonal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is biorthogonal"""

    dec_hi = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Highpass decomposition filter"""

    dec_len = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Decomposition filters length"""

    dec_lo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Lowpass decomposition filter"""

    family_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Wavelet family name"""

    family_number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Wavelet family number"""

    filter_bank = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns tuple of wavelet filters coefficients
        (dec_lo, dec_hi, rec_lo, rec_hi)
        """

    inverse_filter_bank = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Tuple of inverse wavelet filters coefficients
        (rec_lo[::-1], rec_hi[::-1], dec_lo[::-1], dec_hi[::-1])
        """

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    orthogonal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is orthogonal"""

    rec_hi = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Highpass reconstruction filter"""

    rec_len = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reconstruction filters length"""

    rec_lo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Lowpass reconstruction filter"""

    short_family_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Short wavelet family name"""

    symmetry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Wavelet symmetry"""

    vanishing_moments_phi = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of vanishing moments for scaling function"""

    vanishing_moments_psi = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of vanishing moments for wavelet function"""



class _Modes(object):
    """
    Because the most common and practical way of representing digital signals
        in computer science is with finite arrays of values, some extrapolation of
        the input data has to be performed in order to extend the signal before
        computing the :ref:`Discrete Wavelet Transform <ref-dwt>` using the
        cascading filter banks algorithm.
    
        Depending on the extrapolation method, significant artifacts at the
        signal's borders can be introduced during that process, which in turn may
        lead to inaccurate computations of the :ref:`DWT <ref-dwt>` at the signal's
        ends.
    
        PyWavelets provides several methods of signal extrapolation that can be
        used to minimize this negative effect:
    
        zero - zero-padding                   0  0 | x1 x2 ... xn | 0  0
        constant - constant-padding          x1 x1 | x1 x2 ... xn | xn xn
        symmetric - symmetric-padding        x2 x1 | x1 x2 ... xn | xn xn-1
        reflect - reflect-padding            x3 x2 | x1 x2 ... xn | xn-1 xn-2
        periodic - periodic-padding        xn-1 xn | x1 x2 ... xn | x1 x2
        smooth - smooth-padding             (1st derivative interpolation)
        antisymmetric -                    -x2 -x1 | x1 x2 ... xn | -xn -xn-1
        antireflect -                      -x3 -x2 | x1 x2 ... xn | -xn-1 -xn-2
    
        DWT performed for these extension modes is slightly redundant, but ensure a
        perfect reconstruction for IDWT. To receive the smallest possible number of
        coefficients, computations can be performed with the periodization mode:
    
        periodization - like periodic-padding but gives the smallest possible
                        number of decomposition coefficients. IDWT must be
                        performed with the same mode.
    
        Examples
        --------
        >>> import pywt
        >>> pywt.Modes.modes
            ['zero', 'constant', 'symmetric', 'reflect', 'periodic', 'smooth', 'periodization', 'antisymmetric', 'antireflect']
        >>> # The different ways of passing wavelet and mode parameters
        >>> (a, d) = pywt.dwt([1,2,3,4,5,6], 'db2', 'smooth')
        >>> (a, d) = pywt.dwt([1,2,3,4,5,6], pywt.Wavelet('db2'), pywt.Modes.smooth)
    
        Notes
        -----
        Extending data in context of PyWavelets does not mean reallocation of the
        data in computer's physical memory and copying values, but rather computing
        the extra values only when they are needed. This feature saves extra
        memory and CPU resources and helps to avoid page swapping when handling
        relatively big data arrays on computers with low physical memory.
    """
    def from_object(self, *args, **kwargs): # real signature unknown
        pass

    def __getattr__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    antireflect = 8
    antisymmetric = 7
    constant = 2
    modes = [
        'zero',
        'constant',
        'symmetric',
        'periodic',
        'smooth',
        'periodization',
        'reflect',
        'antisymmetric',
        'antireflect',
    ]
    periodic = 4
    periodization = 5
    reflect = 6
    smooth = 3
    symmetric = 1
    zero = 0
    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pywt._extensions._pywt\', \'__doc__\': "\\n    Because the most common and practical way of representing digital signals\\n    in computer science is with finite arrays of values, some extrapolation of\\n    the input data has to be performed in order to extend the signal before\\n    computing the :ref:`Discrete Wavelet Transform <ref-dwt>` using the\\n    cascading filter banks algorithm.\\n\\n    Depending on the extrapolation method, significant artifacts at the\\n    signal\'s borders can be introduced during that process, which in turn may\\n    lead to inaccurate computations of the :ref:`DWT <ref-dwt>` at the signal\'s\\n    ends.\\n\\n    PyWavelets provides several methods of signal extrapolation that can be\\n    used to minimize this negative effect:\\n\\n    zero - zero-padding                   0  0 | x1 x2 ... xn | 0  0\\n    constant - constant-padding          x1 x1 | x1 x2 ... xn | xn xn\\n    symmetric - symmetric-padding        x2 x1 | x1 x2 ... xn | xn xn-1\\n    reflect - reflect-padding            x3 x2 | x1 x2 ... xn | xn-1 xn-2\\n    periodic - periodic-padding        xn-1 xn | x1 x2 ... xn | x1 x2\\n    smooth - smooth-padding             (1st derivative interpolation)\\n    antisymmetric -                    -x2 -x1 | x1 x2 ... xn | -xn -xn-1\\n    antireflect -                      -x3 -x2 | x1 x2 ... xn | -xn-1 -xn-2\\n\\n    DWT performed for these extension modes is slightly redundant, but ensure a\\n    perfect reconstruction for IDWT. To receive the smallest possible number of\\n    coefficients, computations can be performed with the periodization mode:\\n\\n    periodization - like periodic-padding but gives the smallest possible\\n                    number of decomposition coefficients. IDWT must be\\n                    performed with the same mode.\\n\\n    Examples\\n    --------\\n    >>> import pywt\\n    >>> pywt.Modes.modes\\n        [\'zero\', \'constant\', \'symmetric\', \'reflect\', \'periodic\', \'smooth\', \'periodization\', \'antisymmetric\', \'antireflect\']\\n    >>> # The different ways of passing wavelet and mode parameters\\n    >>> (a, d) = pywt.dwt([1,2,3,4,5,6], \'db2\', \'smooth\')\\n    >>> (a, d) = pywt.dwt([1,2,3,4,5,6], pywt.Wavelet(\'db2\'), pywt.Modes.smooth)\\n\\n    Notes\\n    -----\\n    Extending data in context of PyWavelets does not mean reallocation of the\\n    data in computer\'s physical memory and copying values, but rather computing\\n    the extra values only when they are needed. This feature saves extra\\n    memory and CPU resources and helps to avoid page swapping when handling\\n    relatively big data arrays on computers with low physical memory.\\n\\n    ", \'zero\': 0, \'constant\': 2, \'symmetric\': 1, \'reflect\': 6, \'periodic\': 4, \'smooth\': 3, \'periodization\': 5, \'antisymmetric\': 7, \'antireflect\': 8, \'modes\': [\'zero\', \'constant\', \'symmetric\', \'periodic\', \'smooth\', \'periodization\', \'reflect\', \'antisymmetric\', \'antireflect\'], \'from_object\': <cyfunction _Modes.from_object at 0x0000011CACE02DF0>, \'__getattr__\': <cyfunction _Modes.__getattr__ at 0x0000011CACE02EA8>, \'__dict__\': <attribute \'__dict__\' of \'_Modes\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'_Modes\' objects>})'


class _DeprecatedMODES(_Modes):
    # no doc
    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """
        Override so that deprecation warning is shown
                every time MODES is used.
        
                N.B. have to use __getattribute__ as well as __getattr__
                to ensure warning on e.g. `MODES.symmetric`.
        """
        pass

    def __getattr__(self, *args, **kwargs): # real signature unknown
        """
        Override so that deprecation warning is shown
                every time MODES is used.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    msg = 'MODES has been renamed to Modes and will be removed in a future version of pywt.'


# variables with complex values

cwt_pattern = None # (!) real value is "re.compile('\\\\D+(\\\\d+\\\\.*\\\\d*)+')"

Modes = None # (!) real value is '<pywt._extensions._pywt._Modes object at 0x0000011CACF27CC0>'

MODES = None # (!) real value is '<pywt._extensions._pywt._DeprecatedMODES object at 0x0000011CACF27BE0>'

_old_modes = [
    'zpd',
    'cpd',
    'sym',
    'ppd',
    'sp1',
    'per',
]

__all__ = [
    'MODES',
    'Modes',
    'DiscreteContinuousWavelet',
    'Wavelet',
    'ContinuousWavelet',
    'wavelist',
    'families',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000011C9E72F4A8>'

__pyx_capi__ = {
    '_check_dtype': None, # (!) real value is '<capsule object "PyArray_Descr *(PyObject *, int __pyx_skip_dispatch)" at 0x0000011C9E5C97E0>'
    'c_wavelet_from_object': None, # (!) real value is '<capsule object "PyObject *(PyObject *)" at 0x0000011C9E5C9840>'
    'have_c99_complex': None, # (!) real value is '<capsule object "int" at 0x0000011C9E5C9870>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='pywt._extensions._pywt', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000011C9E72F4A8>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\pywt\\\\_extensions\\\\_pywt.cp37-win_amd64.pyd')"

__test__ = {
    'ContinuousWavelet.wavefun (line 855)': '\n        wavefun(self, level=8, length=None)\n\n        Calculates approximations of wavelet function (``psi``) on xgrid\n        (``x``) at a given level of refinement or length itself.\n\n        Parameters\n        ----------\n        level : int, optional\n            Level of refinement (default: 8). Defines the length by\n            ``2**level`` if length is not set.\n        length : int, optional\n            Number of samples. If set to None, the length is set to\n            ``2**level`` instead.\n\n        Returns\n        -------\n        psi : array_like\n            Wavelet function computed for grid xval\n        xval : array_like\n            grid going from lower_bound to upper_bound\n\n        Notes\n        -----\n        The effective support are set with ``lower_bound`` and ``upper_bound``.\n        The wavelet function is complex for ``\'cmor\'``, ``\'shan\'``, ``\'fbsp\'``\n        and ``\'cgau\'``.\n\n        The complex frequency B-spline wavelet (``\'fbsp\'``) has\n        ``bandwidth_frequency``, ``center_frequency`` and ``fbsp_order`` as\n        additional parameters.\n\n        The complex Shannon wavelet (``\'shan\'``) has ``bandwidth_frequency``\n        and ``center_frequency`` as additional parameters.\n\n        The complex Morlet wavelet (``\'cmor\'``) has ``bandwidth_frequency``\n        and ``center_frequency`` as additional parameters.\n\n        Examples\n        --------\n        >>> import pywt\n        >>> import matplotlib.pyplot as plt\n        >>> lb = -5\n        >>> ub = 5\n        >>> n = 1000\n        >>> wavelet = pywt.ContinuousWavelet("gaus8")\n        >>> wavelet.upper_bound = ub\n        >>> wavelet.lower_bound = lb\n        >>> [psi,xval] = wavelet.wavefun(length=n)\n        >>> plt.plot(xval,psi) # doctest: +ELLIPSIS\n        [<matplotlib.lines.Line2D object at ...>]\n        >>> plt.title("Gaussian Wavelet of order 8") # doctest: +ELLIPSIS\n        <matplotlib.text.Text object at ...>\n        >>> plt.show() # doctest: +SKIP\n\n        >>> import pywt\n        >>> import matplotlib.pyplot as plt\n        >>> lb = -5\n        >>> ub = 5\n        >>> n = 1000\n        >>> wavelet = pywt.ContinuousWavelet("cgau4")\n        >>> wavelet.upper_bound = ub\n        >>> wavelet.lower_bound = lb\n        >>> [psi,xval] = wavelet.wavefun(length=n)\n        >>> plt.subplot(211) # doctest: +ELLIPSIS\n        <matplotlib.axes._subplots.AxesSubplot object at ...>\n        >>> plt.plot(xval,np.real(psi)) # doctest: +ELLIPSIS\n        [<matplotlib.lines.Line2D object at ...>]\n        >>> plt.title("Real part") # doctest: +ELLIPSIS\n        <matplotlib.text.Text object at ...>\n        >>> plt.subplot(212) # doctest: +ELLIPSIS\n        <matplotlib.axes._subplots.AxesSubplot object at ...>\n        >>> plt.plot(xval,np.imag(psi)) # doctest: +ELLIPSIS\n        [<matplotlib.lines.Line2D object at ...>]\n        >>> plt.title("Imaginary part") # doctest: +ELLIPSIS\n        <matplotlib.text.Text object at ...>\n        >>> plt.show() # doctest: +SKIP\n\n        ',
    'Wavelet.wavefun (line 547)': "\n        wavefun(self, level=8)\n\n        Calculates approximations of scaling function (`phi`) and wavelet\n        function (`psi`) on xgrid (`x`) at a given level of refinement.\n\n        Parameters\n        ----------\n        level : int, optional\n            Level of refinement (default: 8).\n\n        Returns\n        -------\n        [phi, psi, x] : array_like\n            For orthogonal wavelets returns scaling function, wavelet function\n            and xgrid - [phi, psi, x].\n\n        [phi_d, psi_d, phi_r, psi_r, x] : array_like\n            For biorthogonal wavelets returns scaling and wavelet function both\n            for decomposition and reconstruction and xgrid\n\n        Examples\n        --------\n        >>> import pywt\n        >>> # Orthogonal\n        >>> wavelet = pywt.Wavelet('db2')\n        >>> phi, psi, x = wavelet.wavefun(level=5)\n        >>> # Biorthogonal\n        >>> wavelet = pywt.Wavelet('bior3.5')\n        >>> phi_d, psi_d, phi_r, psi_r, x = wavelet.wavefun(level=5)\n\n        ",
    'families (line 256)': '\n    families(short=True)\n\n    Returns a list of available built-in wavelet families.\n\n    Currently the built-in families are:\n\n    * Haar (``haar``)\n    * Daubechies (``db``)\n    * Symlets (``sym``)\n    * Coiflets (``coif``)\n    * Biorthogonal (``bior``)\n    * Reverse biorthogonal (``rbio``)\n    * `"Discrete"` FIR approximation of Meyer wavelet (``dmey``)\n    * Gaussian wavelets (``gaus``)\n    * Mexican hat wavelet (``mexh``)\n    * Morlet wavelet (``morl``)\n    * Complex Gaussian wavelets (``cgau``)\n    * Shannon wavelets (``shan``)\n    * Frequency B-Spline wavelets (``fbsp``)\n    * Complex Morlet wavelets (``cmor``)\n\n    Parameters\n    ----------\n    short : bool, optional\n        Use short names (default: True).\n\n    Returns\n    -------\n    families : list\n        List of available wavelet families.\n\n    Examples\n    --------\n    >>> import pywt\n    >>> pywt.families()\n    [\'haar\', \'db\', \'sym\', \'coif\', \'bior\', \'rbio\', \'dmey\', \'gaus\', \'mexh\', \'morl\', \'cgau\', \'shan\', \'fbsp\', \'cmor\']\n    >>> pywt.families(short=False)\n    [\'Haar\', \'Daubechies\', \'Symlets\', \'Coiflets\', \'Biorthogonal\', \'Reverse biorthogonal\', \'Discrete Meyer (FIR Approximation)\', \'Gaussian\', \'Mexican hat wavelet\', \'Morlet wavelet\', \'Complex Gaussian wavelets\', \'Shannon wavelets\', \'Frequency B-Spline wavelets\', \'Complex Morlet wavelets\']\n\n    ',
    'wavelist (line 184)': "\n    wavelist(family=None, kind='all')\n\n    Returns list of available wavelet names for the given family name.\n\n    Parameters\n    ----------\n    family : str, optional\n        Short family name. If the family name is None (default) then names\n        of all the built-in wavelets are returned. Otherwise the function\n        returns names of wavelets that belong to the given family.\n        Valid names are::\n\n            'haar', 'db', 'sym', 'coif', 'bior', 'rbio', 'dmey', 'gaus',\n            'mexh', 'morl', 'cgau', 'shan', 'fbsp', 'cmor'\n\n    kind : {'all', 'continuous', 'discrete'}, optional\n        Whether to return only wavelet names of discrete or continuous\n        wavelets, or all wavelets.  Default is ``'all'``.\n        Ignored if ``family`` is specified.\n\n    Returns\n    -------\n    wavelist : list of str\n        List of available wavelet names.\n\n    Examples\n    --------\n    >>> import pywt\n    >>> pywt.wavelist('coif')\n    ['coif1', 'coif2', 'coif3', 'coif4', 'coif5', 'coif6', 'coif7', ...\n    >>> pywt.wavelist(kind='continuous')\n    ['cgau1', 'cgau2', 'cgau3', 'cgau4', 'cgau5', 'cgau6', 'cgau7', ...\n\n    ",
}

