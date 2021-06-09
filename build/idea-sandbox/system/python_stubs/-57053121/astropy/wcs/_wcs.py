# encoding: utf-8
# module astropy.wcs._wcs
# from C:\Users\Doly\Anaconda3\lib\site-packages\astropy\wcs\_wcs.cp37-win_amd64.pyd
# by generator 1.147
# no doc
# no imports

# Variables with simple values

WCSCOMPARE_ANCILLARY = 1
WCSCOMPARE_CRPIX = 4
WCSCOMPARE_TILING = 2

WCSHDO_all = 255
WCSHDO_CNAMna = 16
WCSHDO_CRPXna = 8
WCSHDO_DOBSn = 1
WCSHDO_EFMT = 262144
WCSHDO_none = 0
WCSHDO_P12 = 4096
WCSHDO_P13 = 8192
WCSHDO_P14 = 16384
WCSHDO_P15 = 32768
WCSHDO_P16 = 65536
WCSHDO_P17 = 131072

WCSHDO_PVn_ma = 4

WCSHDO_safe = 15

WCSHDO_TPCn_ka = 2

WCSHDO_WCSNna = 32

WCSHDR_all = 1048575
WCSHDR_ALLIMG = 131072
WCSHDR_AUXIMG = 65536
WCSHDR_BIMGARR = 2097152
WCSHDR_CD00i00j = 4

WCSHDR_CD0i_0ja = 32

WCSHDR_CNAMn = 32768
WCSHDR_CROTAia = 1
WCSHDR_DOBSn = 512
WCSHDR_EPOCHa = 4096
WCSHDR_IMGHEAD = 1048576
WCSHDR_LONGKEY = 16384
WCSHDR_none = 0
WCSHDR_PC00i00j = 8

WCSHDR_PC0i_0ja = 64

WCSHDR_PIXLIST = 4194304
WCSHDR_PROJPn = 16

WCSHDR_PS0i_0ma = 256

WCSHDR_PV0i_0ma = 128

WCSHDR_RADECSYS = 2048
WCSHDR_reject = 268435456
WCSHDR_strict = 536870912
WCSHDR_VELREFa = 2
WCSHDR_VSOURCE = 8192

WCSSUB_CELESTIAL = 4103
WCSSUB_CUBEFACE = 4100
WCSSUB_LATITUDE = 4098
WCSSUB_LONGITUDE = 4097
WCSSUB_SPECTRAL = 4104
WCSSUB_STOKES = 4112

__version__ = '6.2.0'

# functions

def find_all_wcs(relax=0, keysel=0): # real signature unknown; restored from __doc__
    """
    find_all_wcs(relax=0, keysel=0)
    
    Find all WCS transformations in the header.
    
    Parameters
    ----------
    
    header : str
        The raw FITS header data.
    
    relax : bool or int
        Degree of permissiveness:
    
        - `False`: Recognize only FITS keywords defined by the published
          WCS standard.
    
        - `True`: Admit all recognized informal extensions of the WCS
          standard.
    
        - `int`: a bit field selecting specific extensions to accept.  See
          :ref:`relaxread` for details.
    
    keysel : sequence of flags
        Used to restrict the keyword types considered:
    
        - ``WCSHDR_IMGHEAD``: Image header keywords.
    
        - ``WCSHDR_BIMGARR``: Binary table image array.
    
        - ``WCSHDR_PIXLIST``: Pixel list keywords.
    
        If zero, there is no restriction.  If -1, `wcspih` is called,
        rather than `wcstbh`.
    
    Returns
    -------
    wcs_list : list of `~astropy.wcs.Wcsprm` objects
    """
    pass

def _sanity_check(*args, **kwargs): # real signature unknown
    pass

# classes

class DistortionLookupTable(object):
    """
    DistortionLookupTable(*table*, *crpix*, *crval*, *cdelt*)
    
    Represents a single lookup table for a `distortion paper`_
    transformation.
    
    Parameters
    ----------
    table : 2-dimensional array
        The distortion lookup table.
    
    crpix : 2-tuple
        The distortion array reference pixel
    
    crval : 2-tuple
        The image array pixel coordinate
    
    cdelt : 2-tuple
        The grid step size
    """
    def get_offset(self, x, y): # real signature unknown; restored from __doc__
        """
        get_offset(x, y) -> (x, y)
        
        Returns the offset as defined in the distortion lookup table.
        
        Returns
        -------
        coordinate : coordinate pair
            The offset from the distortion table for pixel point (*x*, *y*).
        """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *table, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    cdelt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double array[naxis]`` Coordinate increments (``CDELTia``) for each
coord axis.

If a ``CDi_ja`` linear transformation matrix is present, a warning is
raised and `~astropy.wcs.Wcsprm.cdelt` is ignored.  The ``CDi_ja``
matrix may be deleted by::

  del wcs.wcs.cd

An undefined value is represented by NaN.
"""

    crpix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double array[naxis]`` Coordinate reference pixels (``CRPIXja``) for
each pixel axis.
"""

    crval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double array[naxis]`` Coordinate reference values (``CRVALia``) for
each coordinate axis.
"""

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``float array`` The array data for the
`~astropy.wcs.DistortionLookupTable`.
"""



class WcsError(ValueError):
    """ Base class of all invalid WCS errors. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class InconsistentAxisTypesError(WcsError):
    """
    InconsistentAxisTypesError()
    
    The WCS header inconsistent or unrecognized coordinate axis type(s).
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass


class InvalidCoordinateError(WcsError):
    """
    InvalidCoordinateError()
    
    One or more of the world coordinates is invalid.
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass


class InvalidSubimageSpecificationError(WcsError):
    """
    InvalidSubimageSpecificationError()
    
    The subimage specification is invalid.
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass


class InvalidTabularParametersError(WcsError):
    """
    InvalidTabularParametersError()
    
    The given tabular parameters are invalid.
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass


class InvalidTransformError(WcsError):
    """
    InvalidTransformError()
    
    The WCS transformation is invalid, or the transformation parameters
    are invalid.
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass


class NonseparableSubimageCoordinateSystemError(WcsError):
    """
    NonseparableSubimageCoordinateSystemError()
    
    Non-separable subimage coordinate system.
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass


class NoSolutionError(WcsError):
    """
    NoSolutionError()
    
    No solution can be found in the given interval.
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass


class NoWcsKeywordsFoundError(WcsError):
    """
    NoWcsKeywordsFoundError()
    
    No WCS keywords were found in the given header.
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass


class SingularMatrixError(WcsError):
    """
    SingularMatrixError()
    
    The linear transformation matrix is singular.
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass


class Sip(object):
    """
    Sip(*a, b, ap, bp, crpix*)
    
    The `~astropy.wcs.Sip` class performs polynomial distortion correction
    using the `SIP`_ convention in both directions.
    
    Parameters
    ----------
    a : double array[m+1][m+1]
        The ``A_i_j`` polynomial for pixel to focal plane transformation.
        Its size must be (*m* + 1, *m* + 1) where *m* = ``A_ORDER``.
    
    b : double array[m+1][m+1]
        The ``B_i_j`` polynomial for pixel to focal plane transformation.
        Its size must be (*m* + 1, *m* + 1) where *m* = ``B_ORDER``.
    
    ap : double array[m+1][m+1]
        The ``AP_i_j`` polynomial for pixel to focal plane transformation.
        Its size must be (*m* + 1, *m* + 1) where *m* = ``AP_ORDER``.
    
    bp : double array[m+1][m+1]
        The ``BP_i_j`` polynomial for pixel to focal plane transformation.
        Its size must be (*m* + 1, *m* + 1) where *m* = ``BP_ORDER``.
    
    crpix : double array[2]
        The reference pixel.
    
    Notes
    -----
    Shupe, D. L., M. Moshir, J. Li, D. Makovoz and R. Narron.  2005.
    "The SIP Convention for Representing Distortion in FITS Image
    Headers."  ADASS XIV.
    """
    def foc2pix(self, *foccrd, origin, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        sip_foc2pix(*foccrd, origin*) -> double array[ncoord][nelem]
        
        Convert focal plane coordinates to pixel coordinates using the `SIP`_
        polynomial distortion convention.
        
        Parameters
        ----------
        foccrd : double array[ncoord][nelem]
            Array of focal plane coordinates.
        
        
        origin : int
            Specifies the origin of pixel values.  The Fortran and FITS
            standards use an origin of 1.  Numpy and C use array indexing with
            origin at 0.
        
        
        Returns
        -------
        pixcrd : double array[ncoord][nelem]
            Returns an array of pixel coordinates.
        
        Raises
        ------
        MemoryError
            Memory allocation failed.
        
        ValueError
            Invalid coordinate transformation parameters.
        """
        pass

    def pix2foc(self, *pixcrd, origin, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        sip_pix2foc(*pixcrd, origin*) -> double array[ncoord][nelem]
        
        Convert pixel coordinates to focal plane coordinates using the `SIP`_
        polynomial distortion convention.
        
        Parameters
        ----------
        pixcrd : double array[ncoord][nelem]
            Array of pixel coordinates.
        
        
        origin : int
            Specifies the origin of pixel values.  The Fortran and FITS
            standards use an origin of 1.  Numpy and C use array indexing with
            origin at 0.
        
        
        Returns
        -------
        foccrd : double array[ncoord][nelem]
            Returns an array of focal plane coordinates.
        
        Raises
        ------
        MemoryError
            Memory allocation failed.
        
        ValueError
            Invalid coordinate transformation parameters.
        """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *a, b, ap, bp, crpix, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    a = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double array[a_order+1][a_order+1]`` Focal plane transformation
matrix.

The `SIP`_ ``A_i_j`` matrix used for pixel to focal plane
transformation.

Its values may be changed in place, but it may not be resized, without
creating a new `~astropy.wcs.Sip` object.
"""

    ap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double array[ap_order+1][ap_order+1]`` Focal plane to pixel
transformation matrix.

The `SIP`_ ``AP_i_j`` matrix used for focal plane to pixel
transformation.  Its values may be changed in place, but it may not be
resized, without creating a new `~astropy.wcs.Sip` object.
"""

    ap_order = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``int`` (read-only) Order of the polynomial (``AP_ORDER``).
"""

    a_order = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``int`` (read-only) Order of the polynomial (``A_ORDER``).
"""

    b = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double array[b_order+1][b_order+1]`` Pixel to focal plane
transformation matrix.

The `SIP`_ ``B_i_j`` matrix used for pixel to focal plane
transformation.  Its values may be changed in place, but it may not be
resized, without creating a new `~astropy.wcs.Sip` object.
"""

    bp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double array[bp_order+1][bp_order+1]`` Focal plane to pixel
transformation matrix.

The `SIP`_ ``BP_i_j`` matrix used for focal plane to pixel
transformation.  Its values may be changed in place, but it may not be
resized, without creating a new `~astropy.wcs.Sip` object.
"""

    bp_order = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``int`` (read-only) Order of the polynomial (``BP_ORDER``).
"""

    b_order = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``int`` (read-only) Order of the polynomial (``B_ORDER``).
"""

    crpix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double array[naxis]`` Coordinate reference pixels (``CRPIXja``) for
each pixel axis.
"""



class Tabprm(object):
    """
    A class to store the information related to tabular coordinates,
    i.e., coordinates that are defined via a lookup table.
    
    This class can not be constructed directly from Python, but instead is
    returned from `~astropy.wcs.Wcsprm.tab`.
    """
    def print_contents(self): # real signature unknown; restored from __doc__
        """
        print_contents()
        
        Print the contents of the `~astropy.wcs.Tabprm` object to
        stdout.  Probably only useful for debugging purposes, and may be
        removed in the future.
        
        To get a string of the contents, use `repr`.
        """
        pass

    def set(self): # real signature unknown; restored from __doc__
        """
        set()
        
        Allocates memory for work arrays.
        
        Also sets up the class according to information supplied within it.
        
        Note that this routine need not be called directly; it will be invoked
        by functions that need it.
        
        Raises
        ------
        MemoryError
            Memory allocation failed.
        
        InvalidTabularParameters
            Invalid tabular parameters.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    coord = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double array[K_M]...[K_2][K_1][M]`` The tabular coordinate array.

Has the dimensions::

    (K_M, ... K_2, K_1, M)

(see `~astropy.wcs.Tabprm.K`) i.e. with the `M` dimension
varying fastest so that the `M` elements of a coordinate vector are
stored contiguously in memory.
"""

    crval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double array[M]`` Index values for the reference pixel for each of
the tabular coord axes.
"""

    delta = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double array[M]`` (read-only) Interpolated indices into the coord
array.

Array of interpolated indices into the coordinate array such that
Upsilon_m, as defined in Paper III, is equal to
(`~astropy.wcs.Tabprm.p0` [m] + 1) + delta[m].
"""

    extrema = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double array[K_M]...[K_2][2][M]`` (read-only)

An array recording the minimum and maximum value of each element of
the coordinate vector in each row of the coordinate array, with the
dimensions::

    (K_M, ... K_2, 2, M)

(see `~astropy.wcs.Tabprm.K`).  The minimum is recorded
in the first element of the compressed K_1 dimension, then the
maximum.  This array is used by the inverse table lookup function to
speed up table searches.
"""

    K = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``int array[M]`` (read-only) The lengths of the axes of the coordinate
array.

An array of length `M` whose elements record the lengths of the axes of
the coordinate array and of each indexing vector.
"""

    M = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``int`` (read-only) Number of tabular coordinate axes.
"""

    map = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``int array[M]`` Association between axes.

A vector of length `~astropy.wcs.Tabprm.M` that defines
the association between axis *m* in the *M*-dimensional coordinate
array (1 <= *m* <= *M*) and the indices of the intermediate world
coordinate and world coordinate arrays.

When the intermediate and world coordinate arrays contain the full
complement of coordinate elements in image-order, as will usually be
the case, then ``map[m-1] == i-1`` for axis *i* in the *N*-dimensional
image (1 <= *i* <= *N*).  In terms of the FITS keywords::

    map[PVi_3a - 1] == i - 1.

However, a different association may result if the intermediate
coordinates, for example, only contains a (relevant) subset of
intermediate world coordinate elements.  For example, if *M* == 1 for
an image with *N* > 1, it is possible to fill the intermediate
coordinates with the relevant coordinate element with ``nelem`` set to
1.  In this case ``map[0] = 0`` regardless of the value of *i*.
"""

    nc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``int`` (read-only) Total number of coord vectors in the coord array.

Total number of coordinate vectors in the coordinate array being the
product K_1 * K_2 * ... * K_M.
"""

    p0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``int array[M]`` Interpolated indices into the coordinate array.

Vector of length `~astropy.wcs.Tabprm.M` of interpolated
indices into the coordinate array such that Upsilon_m, as defined in
Paper III, is equal to ``(p0[m] + 1) + delta[m]``.
"""

    sense = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``int array[M]`` +1 if monotonically increasing, -1 if decreasing.

A vector of length `~astropy.wcs.Tabprm.M` whose elements
indicate whether the corresponding indexing vector is monotonically
increasing (+1), or decreasing (-1).
"""



class Wcsprm(object):
    """
    Wcsprm(header=None, key=' ', relax=False, naxis=2, keysel=0, colsel=None)
    
    `~astropy.wcs.Wcsprm` performs the core WCS transformations.
    
    .. note::
        The members of this object correspond roughly to the key/value
        pairs in the FITS header.  However, they are adjusted and
        normalized in a number of ways that make performing the WCS
        transformation easier.  Therefore, they can not be relied upon to
        get the original values in the header.  For that, use
        `astropy.io.fits.Header` directly.
    
    The FITS header parsing enforces correct FITS "keyword = value" syntax
    with regard to the equals sign occurring in columns 9 and 10.
    However, it does recognize free-format character (NOST 100-2.0,
    Sect. 5.2.1), integer (Sect. 5.2.3), and floating-point values
    (Sect. 5.2.4) for all keywords.
    
    Parameters
    ----------
    header : An `astropy.io.fits.Header`, string, or `None`.
      If ``None``, the object will be initialized to default values.
    
    key : str, optional
        The key referring to a particular WCS transform in the header.
        This may be either ``' '`` or ``'A'``-``'Z'`` and corresponds to
        the ``"a"`` part of ``"CTYPEia"``.  (*key* may only be
        provided if *header* is also provided.)
    
    relax : bool or int, optional
    
        Degree of permissiveness:
    
        - `False`: Recognize only FITS keywords defined by the published
          WCS standard.
    
        - `True`: Admit all recognized informal extensions of the WCS
          standard.
    
        - `int`: a bit field selecting specific extensions to accept.  See
          :ref:`relaxread` for details.
    
    naxis : int, optional
        The number of world coordinates axes for the object.  (*naxis* may
        only be provided if *header* is `None`.)
    
    keysel : sequence of flag bits, optional
        Vector of flag bits that may be used to restrict the keyword types
        considered:
    
            - ``WCSHDR_IMGHEAD``: Image header keywords.
    
            - ``WCSHDR_BIMGARR``: Binary table image array.
    
            - ``WCSHDR_PIXLIST``: Pixel list keywords.
    
        If zero, there is no restriction.  If -1, the underlying wcslib
        function ``wcspih()`` is called, rather than ``wcstbh()``.
    
    colsel : sequence of int
        A sequence of table column numbers used to restrict the keywords
        considered.  `None` indicates no restriction.
    
    Raises
    ------
    MemoryError
         Memory allocation failed.
    
    ValueError
         Invalid key.
    
    KeyError
         Key not found in FITS header.
    """
    def bounds_check(self, pix2world, world2pix): # real signature unknown; restored from __doc__
        """
        bounds_check(pix2world, world2pix)
        
        Enable/disable bounds checking.
        
        Parameters
        ----------
        pix2world : bool, optional
            When `True`, enable bounds checking for the pixel-to-world (p2x)
            transformations.  Default is `True`.
        
        world2pix : bool, optional
            When `True`, enable bounds checking for the world-to-pixel (s2x)
            transformations.  Default is `True`.
        
        Notes
        -----
        Note that by default (without calling `bounds_check`) strict bounds
        checking is enabled.
        """
        pass

    def cdfix(self): # real signature unknown; restored from __doc__
        """
        cdfix()
        
        Fix erroneously omitted ``CDi_ja`` keywords.
        
        Sets the diagonal element of the ``CDi_ja`` matrix to unity if all
        ``CDi_ja`` keywords associated with a given axis were omitted.
        According to Paper I, if any ``CDi_ja`` keywords at all are given in a
        FITS header then those not given default to zero.  This results in a
        singular matrix with an intersecting row and column of zeros.
        
        Returns
        -------
        success : int
            Returns ``0`` for success; ``-1`` if no change required.
        """
        pass

    def celfix(self, *args, **kwargs): # real signature unknown
        """
        Translates AIPS-convention celestial projection types, ``-NCP`` and
        ``-GLS``.
        
        Returns
        -------
        success : int
            Returns ``0`` for success; ``-1`` if no change required.
        """
        pass

    def compare(self, other, cmp=0, tolerance=0.0): # real signature unknown; restored from __doc__
        """
        compare(other, cmp=0, tolerance=0.0)
        
        Compare two Wcsprm objects for equality.
        
        Parameters
        ----------
        
        other : Wcsprm
            The other Wcsprm object to compare to.
        
        cmp : int, optional
            A bit field controlling the strictness of the comparison.  When 0,
            (the default), all fields must be identical.
        
            The following constants may be or'ed together to loosen the
            comparison.
        
            - ``WCSCOMPARE_ANCILLARY``: Ignores ancillary keywords that don't
              change the WCS transformation, such as ``DATE-OBS`` or
              ``EQUINOX``.
        
            - ``WCSCOMPARE_TILING``: Ignore integral differences in
              ``CRPIXja``.  This is the 'tiling' condition, where two WCSes
              cover different regions of the same map projection and align on
              the same map grid.
        
            - ``WCSCOMPARE_CRPIX``: Ignore any differences at all in
              ``CRPIXja``.  The two WCSes cover different regions of the same
              map projection but may not align on the same grid map.
              Overrides ``WCSCOMPARE_TILING``.
        
        tolerance : float, optional
            The amount of tolerance required.  For example, for a value of
            1e-6, all floating-point values in the objects must be equal to
            the first 6 decimal places.  The default value of 0.0 implies
            exact equality.
        
        Returns
        -------
        equal : bool
        """
        pass

    def cylfix(self): # real signature unknown; restored from __doc__
        """
        cylfix()
        
        Fixes WCS keyvalues for malformed cylindrical projections.
        
        Returns
        -------
        success : int
            Returns ``0`` for success; ``-1`` if no change required.
        """
        pass

    def datfix(self): # real signature unknown; restored from __doc__
        """
        datfix()
        
        Translates the old ``DATE-OBS`` date format to year-2000 standard form
        ``(yyyy-mm-ddThh:mm:ss)`` and derives ``MJD-OBS`` from it if not
        already set.
        
        Alternatively, if `~astropy.wcs.Wcsprm.mjdobs` is set and
        `~astropy.wcs.Wcsprm.dateobs` isn't, then `~astropy.wcs.Wcsprm.datfix`
        derives `~astropy.wcs.Wcsprm.dateobs` from it.  If both are set but
        disagree by more than half a day then `ValueError` is raised.
        
        Returns
        -------
        success : int
            Returns ``0`` for success; ``-1`` if no change required.
        """
        pass

    def fix(self, translate_units='', naxis=0): # real signature unknown; restored from __doc__
        """
        fix(translate_units='', naxis=0)
        
        Applies all of the corrections handled separately by
        `~astropy.wcs.Wcsprm.datfix`, `~astropy.wcs.Wcsprm.unitfix`,
        `~astropy.wcs.Wcsprm.celfix`, `~astropy.wcs.Wcsprm.spcfix`,
        `~astropy.wcs.Wcsprm.cylfix` and `~astropy.wcs.Wcsprm.cdfix`.
        
        Parameters
        ----------
        
        translate_units : str, optional
            Specify which potentially unsafe translations of non-standard unit
            strings to perform.  By default, performs all.
        
            Although ``"S"`` is commonly used to represent seconds, its
            translation to ``"s"`` is potentially unsafe since the standard
            recognizes ``"S"`` formally as Siemens, however rarely that may be
            used.  The same applies to ``"H"`` for hours (Henry), and ``"D"``
            for days (Debye).
        
            This string controls what to do in such cases, and is
            case-insensitive.
        
            - If the string contains ``"s"``, translate ``"S"`` to ``"s"``.
        
            - If the string contains ``"h"``, translate ``"H"`` to ``"h"``.
        
            - If the string contains ``"d"``, translate ``"D"`` to ``"d"``.
        
            Thus ``''`` doesn't do any unsafe translations, whereas ``'shd'``
            does all of them.
        
        naxis : int array[naxis], optional
            Image axis lengths.  If this array is set to zero or ``None``,
            then `~astropy.wcs.Wcsprm.cylfix` will not be invoked.
        
        Returns
        -------
        status : dict
        
            Returns a dictionary containing the following keys, each referring
            to a status string for each of the sub-fix functions that were
            called:
        
            - `~astropy.wcs.Wcsprm.cdfix`
        
            - `~astropy.wcs.Wcsprm.datfix`
        
            - `~astropy.wcs.Wcsprm.unitfix`
        
            - `~astropy.wcs.Wcsprm.celfix`
        
            - `~astropy.wcs.Wcsprm.spcfix`
        
            - `~astropy.wcs.Wcsprm.cylfix`
        """
        pass

    def get_cdelt(self): # real signature unknown; restored from __doc__
        """
        get_cdelt() -> double array[naxis]
        
        Coordinate increments (``CDELTia``) for each coord axis.
        
        Returns the ``CDELT`` offsets in read-only form.  Unlike the
        `~astropy.wcs.Wcsprm.cdelt` property, this works even when the header
        specifies the linear transformation matrix in one of the alternative
        ``CDi_ja`` or ``CROTAia`` forms.  This is useful when you want access
        to the linear transformation matrix, but don't care how it was
        specified in the header.
        """
        return 0.0

    def get_pc(self): # real signature unknown; restored from __doc__
        """
        get_pc() -> double array[naxis][naxis]
        
        Returns the ``PC`` matrix in read-only form.  Unlike the
        `~astropy.wcs.Wcsprm.pc` property, this works even when the header
        specifies the linear transformation matrix in one of the alternative
        ``CDi_ja`` or ``CROTAia`` forms.  This is useful when you want access
        to the linear transformation matrix, but don't care how it was
        specified in the header.
        """
        return 0.0

    def get_ps(self): # real signature unknown; restored from __doc__
        """
        get_ps() -> list of tuples
        
        Returns ``PSi_ma`` keywords for each *i* and *m*.
        
        Returns
        -------
        ps : list of tuples
        
            Returned as a list of tuples of the form (*i*, *m*, *value*):
        
            - *i*: int.  Axis number, as in ``PSi_ma``, (i.e. 1-relative)
        
            - *m*: int.  Parameter number, as in ``PSi_ma``, (i.e. 0-relative)
        
            - *value*: string.  Parameter value.
        
        See also
        --------
        astropy.wcs.Wcsprm.set_ps : Set ``PSi_ma`` values
        """
        return []

    def get_pv(self): # real signature unknown; restored from __doc__
        """
        get_pv() -> list of tuples
        
        Returns ``PVi_ma`` keywords for each *i* and *m*.
        
        Returns
        -------
        
            Returned as a list of tuples of the form (*i*, *m*, *value*):
        
            - *i*: int.  Axis number, as in ``PVi_ma``, (i.e. 1-relative)
        
            - *m*: int.  Parameter number, as in ``PVi_ma``, (i.e. 0-relative)
        
            - *value*: string. Parameter value.
        
        See also
        --------
        astropy.wcs.Wcsprm.set_pv : Set ``PVi_ma`` values
        
        Notes
        -----
        
        Note that, if they were not given, `~astropy.wcs.Wcsprm.set` resets
        the entries for ``PVi_1a``, ``PVi_2a``, ``PVi_3a``, and ``PVi_4a`` for
        longitude axis *i* to match (``phi_0``, ``theta_0``), the native
        longitude and latitude of the reference point given by ``LONPOLEa``
        and ``LATPOLEa``.
        """
        return []

    def has_cd(self): # real signature unknown; restored from __doc__
        """
        has_cd() -> bool
        
        Returns `True` if ``CDi_ja`` is present.
        
        ``CDi_ja`` is an alternate specification of the linear transformation
        matrix, maintained for historical compatibility.
        
        Matrix elements in the IRAF convention are equivalent to the product
        ``CDi_ja = CDELTia * PCi_ja``, but the defaults differ from that of
        the ``PCi_ja`` matrix.  If one or more ``CDi_ja`` keywords are present
        then all unspecified ``CDi_ja`` default to zero.  If no ``CDi_ja`` (or
        ``CROTAia``) keywords are present, then the header is assumed to be in
        ``PCi_ja`` form whether or not any ``PCi_ja`` keywords are present
        since this results in an interpretation of ``CDELTia`` consistent with
        the original FITS specification.
        
        While ``CDi_ja`` may not formally co-exist with ``PCi_ja``, it may
        co-exist with ``CDELTia`` and ``CROTAia`` which are to be ignored.
        
        See also
        --------
        astropy.wcs.Wcsprm.cd : Get the raw ``CDi_ja`` values.
        """
        return False

    def has_cdi_ja(self): # real signature unknown; restored from __doc__
        """
        has_cdi_ja() -> bool
        
        Alias for `~astropy.wcs.Wcsprm.has_cd`.  Maintained for backward
        compatibility.
        """
        return False

    def has_crota(self): # real signature unknown; restored from __doc__
        """
        has_crota() -> bool
        
        Returns `True` if ``CROTAia`` is present.
        
        ``CROTAia`` is an alternate specification of the linear transformation
        matrix, maintained for historical compatibility.
        
        In the AIPS convention, ``CROTAia`` may only be associated with the
        latitude axis of a celestial axis pair.  It specifies a rotation in
        the image plane that is applied *after* the ``CDELTia``; any other
        ``CROTAia`` keywords are ignored.
        
        ``CROTAia`` may not formally co-exist with ``PCi_ja``.  ``CROTAia`` and
        ``CDELTia`` may formally co-exist with ``CDi_ja`` but if so are to be
        ignored.
        
        See also
        --------
        astropy.wcs.Wcsprm.crota : Get the raw ``CROTAia`` values
        """
        return False

    def has_crotaia(self): # real signature unknown; restored from __doc__
        """
        has_crotaia() -> bool
        
        Alias for `~astropy.wcs.Wcsprm.has_crota`.  Maintained for backward
        compatibility.
        """
        return False

    def has_pc(self): # real signature unknown; restored from __doc__
        """
        has_pc() -> bool
        
        Returns `True` if ``PCi_ja`` is present.  ``PCi_ja`` is the
        recommended way to specify the linear transformation matrix.
        
        See also
        --------
        astropy.wcs.Wcsprm.pc : Get the raw ``PCi_ja`` values
        """
        return False

    def has_pci_ja(self): # real signature unknown; restored from __doc__
        """
        has_pci_ja() -> bool
        
        Alias for `~astropy.wcs.Wcsprm.has_pc`.  Maintained for backward
        compatibility.
        """
        return False

    def is_unity(self): # real signature unknown; restored from __doc__
        """
        is_unity() -> bool
        
        Returns `True` if the linear transformation matrix
        (`~astropy.wcs.Wcsprm.cd`) is unity.
        """
        return False

    def mix(self, mixpix, mixcel, vspan, vstep, viter, world, pixcrd, origin): # real signature unknown; restored from __doc__
        """
        mix(mixpix, mixcel, vspan, vstep, viter, world, pixcrd, origin)
        
        Given either the celestial longitude or latitude plus an element of
        the pixel coordinate, solves for the remaining elements by iterating
        on the unknown celestial coordinate element using
        `~astropy.wcs.Wcsprm.s2p`.
        
        Parameters
        ----------
        mixpix : int
            Which element on the pixel coordinate is given.
        
        mixcel : int
            Which element of the celestial coordinate is given. If *mixcel* =
            ``1``, celestial longitude is given in ``world[self.lng]``,
            latitude returned in ``world[self.lat]``.  If *mixcel* = ``2``,
            celestial latitude is given in ``world[self.lat]``, longitude
            returned in ``world[self.lng]``.
        
        vspan : pair of floats
            Solution interval for the celestial coordinate, in degrees.  The
            ordering of the two limits is irrelevant.  Longitude ranges may be
            specified with any convenient normalization, for example
            ``(-120,+120)`` is the same as ``(240,480)``, except that the
            solution will be returned with the same normalization, i.e. lie
            within the interval specified.
        
        vstep : float
            Step size for solution search, in degrees.  If ``0``, a sensible,
            although perhaps non-optimal default will be used.
        
        viter : int
            If a solution is not found then the step size will be halved and
            the search recommenced.  *viter* controls how many times the step
            size is halved.  The allowed range is 5 - 10.
        
        world : double array[naxis]
            World coordinate elements.  ``world[self.lng]`` and
            ``world[self.lat]`` are the celestial longitude and latitude, in
            degrees.  Which is given and which returned depends on the value
            of *mixcel*.  All other elements are given.  The results will be
            written to this array in-place.
        
        pixcrd : double array[naxis].
            Pixel coordinates.  The element indicated by *mixpix* is given and
            the remaining elements will be written in-place.
        
        
        origin : int
            Specifies the origin of pixel values.  The Fortran and FITS
            standards use an origin of 1.  Numpy and C use array indexing with
            origin at 0.
        
        
        Returns
        -------
        result : dict
        
            Returns a dictionary with the following keys:
        
            - *phi* (double array[naxis])
        
            - *theta* (double array[naxis])
        
                - Longitude and latitude in the native coordinate system of
                  the projection, in degrees.
        
            - *imgcrd* (double array[naxis])
        
                - Image coordinate elements.  ``imgcrd[self.lng]`` and
                  ``imgcrd[self.lat]`` are the projected *x*- and
                  *y*-coordinates, in decimal degrees.
        
            - *world* (double array[naxis])
        
                - Another reference to the *world* argument passed in.
        
        Raises
        ------
        MemoryError
            Memory allocation failed.
        
        SingularMatrixError
            Linear transformation matrix is singular.
        
        InconsistentAxisTypesError
            Inconsistent or unrecognized coordinate axis types.
        
        ValueError
            Invalid parameter value.
        
        InvalidTransformError
            Invalid coordinate transformation parameters.
        
        InvalidTransformError
            Ill-conditioned coordinate transformation parameters.
        
        InvalidCoordinateError
            Invalid world coordinate.
        
        NoSolutionError
            No solution found in the specified interval.
        
        See also
        --------
        astropy.wcs.Wcsprm.lat, astropy.wcs.Wcsprm.lng
            Get the axes numbers for latitude and longitude
        
        Notes
        -----
        
        Initially, the specified solution interval is checked to see if it's a
        "crossing" interval.  If it isn't, a search is made for a crossing
        solution by iterating on the unknown celestial coordinate starting at
        the upper limit of the solution interval and decrementing by the
        specified step size.  A crossing is indicated if the trial value of
        the pixel coordinate steps through the value specified.  If a crossing
        interval is found then the solution is determined by a modified form
        of "regula falsi" division of the crossing interval.  If no crossing
        interval was found within the specified solution interval then a
        search is made for a "non-crossing" solution as may arise from a
        point of tangency.  The process is complicated by having to make
        allowance for the discontinuities that occur in all map projections.
        
        Once one solution has been determined others may be found by
        subsequent invocations of `~astropy.wcs.Wcsprm.mix` with suitably
        restricted solution intervals.
        
        Note the circumstance that arises when the solution point lies at a
        native pole of a projection in which the pole is represented as a
        finite curve, for example the zenithals and conics.  In such cases two
        or more valid solutions may exist but `~astropy.wcs.Wcsprm.mix` only
        ever returns one.
        
        Because of its generality, `~astropy.wcs.Wcsprm.mix` is very
        compute-intensive.  For compute-limited applications, more efficient
        special-case solvers could be written for simple projections, for
        example non-oblique cylindrical projections.
        """
        pass

    def p2s(self, pixcrd, origin): # real signature unknown; restored from __doc__
        """
        p2s(pixcrd, origin)
        
        Converts pixel to world coordinates.
        
        Parameters
        ----------
        
        pixcrd : double array[ncoord][nelem]
            Array of pixel coordinates.
        
        
        origin : int
            Specifies the origin of pixel values.  The Fortran and FITS
            standards use an origin of 1.  Numpy and C use array indexing with
            origin at 0.
        
        
        Returns
        -------
        result : dict
            Returns a dictionary with the following keys:
        
            - *imgcrd*: double array[ncoord][nelem]
        
              - Array of intermediate world coordinates.  For celestial axes,
                ``imgcrd[][self.lng]`` and ``imgcrd[][self.lat]`` are the
                projected *x*-, and *y*-coordinates, in pseudo degrees.  For
                spectral axes, ``imgcrd[][self.spec]`` is the intermediate
                spectral coordinate, in SI units.
        
            - *phi*: double array[ncoord]
        
            - *theta*: double array[ncoord]
        
              - Longitude and latitude in the native coordinate system of the
                projection, in degrees.
        
            - *world*: double array[ncoord][nelem]
        
              - Array of world coordinates.  For celestial axes,
                ``world[][self.lng]`` and ``world[][self.lat]`` are the
                celestial longitude and latitude, in degrees.  For spectral
                axes, ``world[][self.spec]`` is the intermediate spectral
                coordinate, in SI units.
        
            - *stat*: int array[ncoord]
        
              - Status return value for each coordinate. ``0`` for success,
                ``1+`` for invalid pixel coordinate.
        
        Raises
        ------
        
        MemoryError
            Memory allocation failed.
        
        SingularMatrixError
            Linear transformation matrix is singular.
        
        InconsistentAxisTypesError
            Inconsistent or unrecognized coordinate axis types.
        
        ValueError
            Invalid parameter value.
        
        ValueError
            *x*- and *y*-coordinate arrays are not the same size.
        
        InvalidTransformError
            Invalid coordinate transformation parameters.
        
        InvalidTransformError
            Ill-conditioned coordinate transformation parameters.
        
        See also
        --------
        astropy.wcs.Wcsprm.lat, astropy.wcs.Wcsprm.lng
            Definition of the latitude and longitude axes
        """
        pass

    def print_contents(self): # real signature unknown; restored from __doc__
        """
        print_contents()
        
        Print the contents of the `~astropy.wcs.Wcsprm` object to stdout.
        Probably only useful for debugging purposes, and may be removed in the
        future.
        
        To get a string of the contents, use `repr`.
        """
        pass

    def s2p(self, world, origin): # real signature unknown; restored from __doc__
        """
        s2p(world, origin)
        
        Transforms world coordinates to pixel coordinates.
        
        Parameters
        ----------
        world : double array[ncoord][nelem]
            Array of world coordinates, in decimal degrees.
        
        
        origin : int
            Specifies the origin of pixel values.  The Fortran and FITS
            standards use an origin of 1.  Numpy and C use array indexing with
            origin at 0.
        
        
        Returns
        -------
        result : dict
            Returns a dictionary with the following keys:
        
            - *phi*: double array[ncoord]
        
            - *theta*: double array[ncoord]
        
                - Longitude and latitude in the native coordinate system of
                  the projection, in degrees.
        
            - *imgcrd*: double array[ncoord][nelem]
        
               - Array of intermediate world coordinates.  For celestial axes,
                 ``imgcrd[][self.lng]`` and ``imgcrd[][self.lat]`` are the
                 projected *x*-, and *y*-coordinates, in pseudo "degrees".
                 For quadcube projections with a ``CUBEFACE`` axis, the face
                 number is also returned in ``imgcrd[][self.cubeface]``.  For
                 spectral axes, ``imgcrd[][self.spec]`` is the intermediate
                 spectral coordinate, in SI units.
        
            - *pixcrd*: double array[ncoord][nelem]
        
                - Array of pixel coordinates.  Pixel coordinates are
                  zero-based.
        
            - *stat*: int array[ncoord]
        
                - Status return value for each coordinate. ``0`` for success,
                  ``1+`` for invalid pixel coordinate.
        
        Raises
        ------
        MemoryError
            Memory allocation failed.
        
        SingularMatrixError
            Linear transformation matrix is singular.
        
        InconsistentAxisTypesError
            Inconsistent or unrecognized coordinate axis types.
        
        ValueError
            Invalid parameter value.
        
        InvalidTransformError
           Invalid coordinate transformation parameters.
        
        InvalidTransformError
            Ill-conditioned coordinate transformation parameters.
        
        See also
        --------
        astropy.wcs.Wcsprm.lat, astropy.wcs.Wcsprm.lng
            Definition of the latitude and longitude axes
        """
        pass

    def set(self): # real signature unknown; restored from __doc__
        """
        set()
        
        Sets up a WCS object for use according to information supplied within
        it.
        
        Note that this routine need not be called directly; it will be invoked
        by `~astropy.wcs.Wcsprm.p2s` and `~astropy.wcs.Wcsprm.s2p` if
        necessary.
        
        Some attributes that are based on other attributes (such as
        `~astropy.wcs.Wcsprm.lattyp` on `~astropy.wcs.Wcsprm.ctype`) may not
        be correct until after `~astropy.wcs.Wcsprm.set` is called.
        
        `~astropy.wcs.Wcsprm.set` strips off trailing blanks in all string
        members.
        
        `~astropy.wcs.Wcsprm.set` recognizes the ``NCP`` projection and
        converts it to the equivalent ``SIN`` projection and it also
        recognizes ``GLS`` as a synonym for ``SFL``.  It does alias
        translation for the AIPS spectral types (``FREQ-LSR``, ``FELO-HEL``,
        etc.) but without changing the input header keywords.
        
        Raises
        ------
        MemoryError
            Memory allocation failed.
        
        SingularMatrixError
            Linear transformation matrix is singular.
        
        InconsistentAxisTypesError
            Inconsistent or unrecognized coordinate axis types.
        
        ValueError
            Invalid parameter value.
        
        InvalidTransformError
            Invalid coordinate transformation parameters.
        
        InvalidTransformError
            Ill-conditioned coordinate transformation parameters.
        """
        pass

    def set_ps(self, ps): # real signature unknown; restored from __doc__
        """
        set_ps(ps)
        
        Sets ``PSi_ma`` keywords for each *i* and *m*.
        
        Parameters
        ----------
        ps : sequence of tuples
        
            The input must be a sequence of tuples of the form (*i*, *m*,
            *value*):
        
            - *i*: int.  Axis number, as in ``PSi_ma``, (i.e. 1-relative)
        
            - *m*: int.  Parameter number, as in ``PSi_ma``, (i.e. 0-relative)
        
            - *value*: string.  Parameter value.
        
        See also
        --------
        astropy.wcs.Wcsprm.get_ps
        """
        pass

    def set_pv(self, pv): # real signature unknown; restored from __doc__
        """
        set_pv(pv)
        
        Sets ``PVi_ma`` keywords for each *i* and *m*.
        
        Parameters
        ----------
        pv : list of tuples
        
            The input must be a sequence of tuples of the form (*i*, *m*,
            *value*):
        
            - *i*: int.  Axis number, as in ``PVi_ma``, (i.e. 1-relative)
        
            - *m*: int.  Parameter number, as in ``PVi_ma``, (i.e. 0-relative)
        
            - *value*: float.  Parameter value.
        
        See also
        --------
        astropy.wcs.Wcsprm.get_pv
        """
        pass

    def spcfix(self): # real signature unknown; restored from __doc__
        """
        spcfix() -> int
        
        Translates AIPS-convention spectral coordinate types.  {``FREQ``,
        ``VELO``, ``FELO``}-{``OBS``, ``HEL``, ``LSR``} (e.g. ``FREQ-LSR``,
        ``VELO-OBS``, ``FELO-HEL``)
        
        Returns
        -------
        success : int
            Returns ``0`` for success; ``-1`` if no change required.
        """
        return 0

    def sptr(self, ctype, i=-1): # real signature unknown; restored from __doc__
        """
        sptr(ctype, i=-1)
        
        Translates the spectral axis in a WCS object.
        
        For example, a ``FREQ`` axis may be translated into ``ZOPT-F2W`` and
        vice versa.
        
        Parameters
        ----------
        ctype : str
            Required spectral ``CTYPEia``, maximum of 8 characters.  The first
            four characters are required to be given and are never modified.
            The remaining four, the algorithm code, are completely determined
            by, and must be consistent with, the first four characters.
            Wildcarding may be used, i.e.  if the final three characters are
            specified as ``"???"``, or if just the eighth character is
            specified as ``"?"``, the correct algorithm code will be
            substituted and returned.
        
        i : int
            Index of the spectral axis (0-relative).  If ``i < 0`` (or not
            provided), it will be set to the first spectral axis identified
            from the ``CTYPE`` keyvalues in the FITS header.
        
        Raises
        ------
        MemoryError
            Memory allocation failed.
        
        SingularMatrixError
            Linear transformation matrix is singular.
        
        InconsistentAxisTypesError
            Inconsistent or unrecognized coordinate axis types.
        
        ValueError
            Invalid parameter value.
        
        InvalidTransformError
            Invalid coordinate transformation parameters.
        
        InvalidTransformError
            Ill-conditioned coordinate transformation parameters.
        
        InvalidSubimageSpecificationError
            Invalid subimage specification (no spectral axis).
        """
        pass

    def sub(self, axes): # real signature unknown; restored from __doc__
        """
        sub(axes)
        
        Extracts the coordinate description for a subimage from a
        `~astropy.wcs.WCS` object.
        
        The world coordinate system of the subimage must be separable in the
        sense that the world coordinates at any point in the subimage must
        depend only on the pixel coordinates of the axes extracted.  In
        practice, this means that the ``PCi_ja`` matrix of the original image
        must not contain non-zero off-diagonal terms that associate any of the
        subimage axes with any of the non-subimage axes.
        
        `sub` can also add axes to a wcsprm object.  The new axes will be
        created using the defaults set by the Wcsprm constructor which produce
        a simple, unnamed, linear axis with world coordinates equal to the
        pixel coordinate.  These default values can be changed before
        invoking `set`.
        
        Parameters
        ----------
        axes : int or a sequence.
        
            - If an int, include the first *N* axes in their original order.
        
            - If a sequence, may contain a combination of image axis numbers
              (1-relative) or special axis identifiers (see below).  Order is
              significant; ``axes[0]`` is the axis number of the input image
              that corresponds to the first axis in the subimage, etc.  Use an
              axis number of 0 to create a new axis using the defaults.
        
            - If ``0``, ``[]`` or ``None``, do a deep copy.
        
            Coordinate axes types may be specified using either strings or
            special integer constants.  The available types are:
        
            - ``'longitude'`` / ``WCSSUB_LONGITUDE``: Celestial longitude
        
            - ``'latitude'`` / ``WCSSUB_LATITUDE``: Celestial latitude
        
            - ``'cubeface'`` / ``WCSSUB_CUBEFACE``: Quadcube ``CUBEFACE`` axis
        
            - ``'spectral'`` / ``WCSSUB_SPECTRAL``: Spectral axis
        
            - ``'stokes'`` / ``WCSSUB_STOKES``: Stokes axis
        
            - ``'celestial'`` / ``WCSSUB_CELESTIAL``: An alias for the
              combination of ``'longitude'``, ``'latitude'`` and ``'cubeface'``.
        
        Returns
        -------
        new_wcs : `~astropy.wcs.WCS` object
        
        Raises
        ------
        MemoryError
            Memory allocation failed.
        
        InvalidSubimageSpecificationError
            Invalid subimage specification (no spectral axis).
        
        NonseparableSubimageCoordinateSystem
            Non-separable subimage coordinate system.
        
        Notes
        -----
        Combinations of subimage axes of particular types may be extracted in
        the same order as they occur in the input image by combining the
        integer constants with the 'binary or' (``|``) operator.  For
        example::
        
            wcs.sub([WCSSUB_LONGITUDE | WCSSUB_LATITUDE | WCSSUB_SPECTRAL])
        
        would extract the longitude, latitude, and spectral axes in the same
        order as the input image.  If one of each were present, the resulting
        object would have three dimensions.
        
        For convenience, ``WCSSUB_CELESTIAL`` is defined as the combination
        ``WCSSUB_LONGITUDE | WCSSUB_LATITUDE | WCSSUB_CUBEFACE``.
        
        The codes may also be negated to extract all but the types specified,
        for example::
        
            wcs.sub([
              WCSSUB_LONGITUDE,
              WCSSUB_LATITUDE,
              WCSSUB_CUBEFACE,
              -(WCSSUB_SPECTRAL | WCSSUB_STOKES)])
        
        The last of these specifies all axis types other than spectral or
        Stokes.  Extraction is done in the order specified by ``axes``, i.e. a
        longitude axis (if present) would be extracted first (via ``axes[0]``)
        and not subsequently (via ``axes[3]``).  Likewise for the latitude and
        cubeface axes in this example.
        
        The number of dimensions in the returned object may be less than or
        greater than the length of ``axes``.  However, it will never exceed the
        number of axes in the input image.
        """
        pass

    def to_header(self, relax=False): # real signature unknown; restored from __doc__
        """
        to_header(relax=False)
        
        `to_header` translates a WCS object into a FITS header.
        
        The details of the header depends on context:
        
            - If the `~astropy.wcs.Wcsprm.colnum` member is non-zero then a
              binary table image array header will be produced.
        
            - Otherwise, if the `~astropy.wcs.Wcsprm.colax` member is set
              non-zero then a pixel list header will be produced.
        
            - Otherwise, a primary image or image extension header will be
              produced.
        
        The output header will almost certainly differ from the input in a
        number of respects:
        
            1. The output header only contains WCS-related keywords.  In
               particular, it does not contain syntactically-required keywords
               such as ``SIMPLE``, ``NAXIS``, ``BITPIX``, or ``END``.
        
            2. Deprecated (e.g. ``CROTAn``) or non-standard usage will be
               translated to standard (this is partially dependent on whether
               ``fix`` was applied).
        
            3. Quantities will be converted to the units used internally,
               basically SI with the addition of degrees.
        
            4. Floating-point quantities may be given to a different decimal
               precision.
        
            5. Elements of the ``PCi_j`` matrix will be written if and only if
               they differ from the unit matrix.  Thus, if the matrix is unity
               then no elements will be written.
        
            6. Additional keywords such as ``WCSAXES``, ``CUNITia``,
               ``LONPOLEa`` and ``LATPOLEa`` may appear.
        
            7. The original keycomments will be lost, although
               `~astropy.wcs.Wcsprm.to_header` tries hard to write meaningful
               comments.
        
            8. Keyword order may be changed.
        
        Keywords can be translated between the image array, binary table, and
        pixel lists forms by manipulating the `~astropy.wcs.Wcsprm.colnum` or
        `~astropy.wcs.Wcsprm.colax` members of the `~astropy.wcs.WCS`
        object.
        
        Parameters
        ----------
        
        relax : bool or int
            Degree of permissiveness:
        
            - `False`: Recognize only FITS keywords defined by the published
              WCS standard.
        
            - `True`: Admit all recognized informal extensions of the WCS
              standard.
        
            - `int`: a bit field selecting specific extensions to write.
              See :ref:`relaxwrite` for details.
        
        Returns
        -------
        header : str
            Raw FITS header as a string.
        """
        pass

    def unitfix(self, translate_units=''): # real signature unknown; restored from __doc__
        """
        unitfix(translate_units='')
        
        Translates non-standard ``CUNITia`` keyvalues.
        
        For example, ``DEG`` -> ``deg``, also stripping off unnecessary
        whitespace.
        
        Parameters
        ----------
        translate_units : str, optional
            Do potentially unsafe translations of non-standard unit strings.
        
            Although ``"S"`` is commonly used to represent seconds, its
            recognizes ``"S"`` formally as Siemens, however rarely that may
            be translation to ``"s"`` is potentially unsafe since the
            standard used.  The same applies to ``"H"`` for hours (Henry),
            and ``"D"`` for days (Debye).
        
            This string controls what to do in such cases, and is
            case-insensitive.
        
            - If the string contains ``"s"``, translate ``"S"`` to ``"s"``.
        
            - If the string contains ``"h"``, translate ``"H"`` to ``"h"``.
        
            - If the string contains ``"d"``, translate ``"D"`` to ``"d"``.
        
            Thus ``''`` doesn't do any unsafe translations, whereas ``'shd'``
            does all of them.
        
        Returns
        -------
        success : int
            Returns ``0`` for success; ``-1`` if no change required.
        """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        """ Creates a deep copy of the WCS object. """
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        """ Creates a deep copy of the WCS object. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, header=None, key=' ', relax=False, naxis=2, keysel=0, colsel=None): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    alt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``str`` Character code for alternate coordinate descriptions.

For example, the ``"a"`` in keyword names such as ``CTYPEia``.  This
is a space character for the primary coordinate description, or one of
the 26 upper-case letters, A-Z.
"""

    axis_types = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``int array[naxis]`` An array of four-digit type codes for each axis.

- First digit (i.e. 1000s):

  - 0: Non-specific coordinate type.

  - 1: Stokes coordinate.

  - 2: Celestial coordinate (including ``CUBEFACE``).

  - 3: Spectral coordinate.

- Second digit (i.e. 100s):

  - 0: Linear axis.

  - 1: Quantized axis (``STOKES``, ``CUBEFACE``).

  - 2: Non-linear celestial axis.

  - 3: Non-linear spectral axis.

  - 4: Logarithmic axis.

  - 5: Tabular axis.

- Third digit (i.e. 10s):

  - 0: Group number, e.g. lookup table number

- The fourth digit is used as a qualifier depending on the axis type.

  - For celestial axes:

    - 0: Longitude coordinate.

    - 1: Latitude coordinate.

    - 2: ``CUBEFACE`` number.

  - For lookup tables: the axis number in a multidimensional table.

``CTYPEia`` in ``"4-3"`` form with unrecognized algorithm code will
have its type set to -1 and generate an error.
"""

    bepoch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double`` Equivalent to ``DATE-OBS``.

Expressed as a Besselian epoch.

See also
--------
astropy.wcs.Wcsprm.dateobs
"""

    cd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double array[naxis][naxis]`` The ``CDi_ja`` linear transformation
matrix.

For historical compatibility, three alternate specifications of the
linear transformations are available in wcslib.  The canonical
``PCi_ja`` with ``CDELTia``, ``CDi_ja``, and the deprecated
``CROTAia`` keywords.  Although the latter may not formally co-exist
with ``PCi_ja``, the approach here is simply to ignore them if given
in conjunction with ``PCi_ja``.

`~astropy.wcs.Wcsprm.has_pc`, `~astropy.wcs.Wcsprm.has_cd` and
`~astropy.wcs.Wcsprm.has_crota` can be used to determine which of
these alternatives are present in the header.

These alternate specifications of the linear transformation matrix are
translated immediately to ``PCi_ja`` by `~astropy.wcs.Wcsprm.set` and
are nowhere visible to the lower-level routines.  In particular,
`~astropy.wcs.Wcsprm.set` resets `~astropy.wcs.Wcsprm.cdelt` to unity
if ``CDi_ja`` is present (and no ``PCi_ja``).  If no ``CROTAia`` is
associated with the latitude axis, `~astropy.wcs.Wcsprm.set` reverts
to a unity ``PCi_ja`` matrix.
"""

    cdelt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double array[naxis]`` Coordinate increments (``CDELTia``) for each
coord axis.

If a ``CDi_ja`` linear transformation matrix is present, a warning is
raised and `~astropy.wcs.Wcsprm.cdelt` is ignored.  The ``CDi_ja``
matrix may be deleted by::

  del wcs.wcs.cd

An undefined value is represented by NaN.
"""

    cel_offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``boolean`` Is there an offset?

If `True`, an offset will be applied to ``(x, y)`` to force ``(x, y) =
(0, 0)`` at the fiducial point, (phi_0, theta_0).  Default is `False`.
"""

    cname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``list of strings`` A list of the coordinate axis names, from
``CNAMEia``.
"""

    colax = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``int array[naxis]`` An array recording the column numbers for each
axis in a pixel list.
"""

    colnum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``int`` Column of FITS binary table associated with this WCS.

Where the coordinate representation is associated with an image-array
column in a FITS binary table, this property may be used to record the
relevant column number.

It should be set to zero for an image header or pixel list.
"""

    cperi = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double array[naxis]`` period of a phase axis, CPERIia.

An undefined value is represented by NaN.
"""

    crder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double array[naxis]`` The random error in each coordinate axis,
``CRDERia``.

An undefined value is represented by NaN.
"""

    crota = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double array[naxis]`` ``CROTAia`` keyvalues for each coordinate
axis.

For historical compatibility, three alternate specifications of the
linear transformations are available in wcslib.  The canonical
``PCi_ja`` with ``CDELTia``, ``CDi_ja``, and the deprecated
``CROTAia`` keywords.  Although the latter may not formally co-exist
with ``PCi_ja``, the approach here is simply to ignore them if given
in conjunction with ``PCi_ja``.

`~astropy.wcs.Wcsprm.has_pc`, `~astropy.wcs.Wcsprm.has_cd` and
`~astropy.wcs.Wcsprm.has_crota` can be used to determine which of
these alternatives are present in the header.

These alternate specifications of the linear transformation matrix are
translated immediately to ``PCi_ja`` by `~astropy.wcs.Wcsprm.set` and
are nowhere visible to the lower-level routines.  In particular,
`~astropy.wcs.Wcsprm.set` resets `~astropy.wcs.Wcsprm.cdelt` to unity
if ``CDi_ja`` is present (and no ``PCi_ja``).  If no ``CROTAia`` is
associated with the latitude axis, `~astropy.wcs.Wcsprm.set` reverts
to a unity ``PCi_ja`` matrix.
"""

    crpix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double array[naxis]`` Coordinate reference pixels (``CRPIXja``) for
each pixel axis.
"""

    crval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double array[naxis]`` Coordinate reference values (``CRVALia``) for
each coordinate axis.
"""

    csyer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double array[naxis]`` The systematic error in the coordinate value
axes, ``CSYERia``.

An undefined value is represented by NaN.
"""

    ctype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``list of strings[naxis]`` List of ``CTYPEia`` keyvalues.

The `~astropy.wcs.Wcsprm.ctype` keyword values must be in upper case
and there must be zero or one pair of matched celestial axis types,
and zero or one spectral axis.
"""

    cubeface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``int`` Index into the ``pixcrd`` (pixel coordinate) array for the
``CUBEFACE`` axis.

This is used for quadcube projections where the cube faces are stored
on a separate axis.

The quadcube projections (``TSC``, ``CSC``, ``QSC``) may be
represented in FITS in either of two ways:

    - The six faces may be laid out in one plane and numbered as
      follows::


                                       0

                              4  3  2  1  4  3  2

                                       5

      Faces 2, 3 and 4 may appear on one side or the other (or both).
      The world-to-pixel routines map faces 2, 3 and 4 to the left but
      the pixel-to-world routines accept them on either side.

    - The ``COBE`` convention in which the six faces are stored in a
      three-dimensional structure using a ``CUBEFACE`` axis indexed
      from 0 to 5 as above.

These routines support both methods; `~astropy.wcs.Wcsprm.set`
determines which is being used by the presence or absence of a
``CUBEFACE`` axis in `~astropy.wcs.Wcsprm.ctype`.
`~astropy.wcs.Wcsprm.p2s` and `~astropy.wcs.Wcsprm.s2p` translate the
``CUBEFACE`` axis representation to the single plane representation
understood by the lower-level projection routines.
"""

    cunit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``list of astropy.UnitBase[naxis]`` List of ``CUNITia`` keyvalues as
`astropy.units.UnitBase` instances.

These define the units of measurement of the ``CRVALia``, ``CDELTia``
and ``CDi_ja`` keywords.

As ``CUNITia`` is an optional header keyword,
`~astropy.wcs.Wcsprm.cunit` may be left blank but otherwise is
expected to contain a standard units specification as defined by WCS
Paper I.  `~astropy.wcs.Wcsprm.unitfix` is available to translate
commonly used non-standard units specifications but this must be done
as a separate step before invoking `~astropy.wcs.Wcsprm.set`.

For celestial axes, if `~astropy.wcs.Wcsprm.cunit` is not blank,
`~astropy.wcs.Wcsprm.set` uses ``wcsunits`` to parse it and scale
`~astropy.wcs.Wcsprm.cdelt`, `~astropy.wcs.Wcsprm.crval`, and
`~astropy.wcs.Wcsprm.cd` to decimal degrees.  It then resets
`~astropy.wcs.Wcsprm.cunit` to ``"deg"``.

For spectral axes, if `~astropy.wcs.Wcsprm.cunit` is not blank,
`~astropy.wcs.Wcsprm.set` uses ``wcsunits`` to parse it and scale
`~astropy.wcs.Wcsprm.cdelt`, `~astropy.wcs.Wcsprm.crval`, and
`~astropy.wcs.Wcsprm.cd` to SI units.  It then resets
`~astropy.wcs.Wcsprm.cunit` accordingly.

`~astropy.wcs.Wcsprm.set` ignores `~astropy.wcs.Wcsprm.cunit` for
other coordinate types; `~astropy.wcs.Wcsprm.cunit` may be used to
label coordinate values.
"""

    czphs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double array[naxis]`` The time at the zero point of a phase axis, ``CSPHSia``.

An undefined value is represented by NaN.
"""

    dateavg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``string`` Representative mid-point of the date of observation.

In ISO format, ``yyyy-mm-ddThh:mm:ss``.

See also
--------
astropy.wcs.Wcsprm.dateobs
"""

    datebeg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``string`` Date at the start of the observation.

In ISO format, ``yyyy-mm-ddThh:mm:ss``.

See also
--------
astropy.wcs.Wcsprm.datebeg
"""

    dateend = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``string`` Date at the end of the observation.

In ISO format, ``yyyy-mm-ddThh:mm:ss``.

See also
--------
astropy.wcs.Wcsprm.dateend
"""

    dateobs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``string`` Start of the date of observation.

In ISO format, ``yyyy-mm-ddThh:mm:ss``.

See also
--------
astropy.wcs.Wcsprm.dateavg
"""

    dateref = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``string`` Date of a reference epoch relative to which
other time measurements refer.

See also
--------
astropy.wcs.Wcsprm.dateref
"""

    equinox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double`` The equinox associated with dynamical equatorial or
ecliptic coordinate systems.

``EQUINOXa`` (or ``EPOCH`` in older headers).  Not applicable to ICRS
equatorial or ecliptic coordinates.

An undefined value is represented by NaN.
"""

    imgpix_matrix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double array[2][2]`` (read-only) Inverse of the ``CDELT`` or ``PC``
matrix.

Inverse containing the product of the ``CDELTia`` diagonal matrix and
the ``PCi_ja`` matrix.
"""

    jepoch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double`` Equivalent to ``DATE-OBS``.

Expressed as a Julian epoch.

See also
--------
astropy.wcs.Wcsprm.dateobs
"""

    lat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``int`` (read-only) The index into the world coord array containing
latitude values.
"""

    latpole = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double`` The native latitude of the celestial pole, ``LATPOLEa`` (deg).
"""

    lattyp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``string`` (read-only) Celestial axis type for latitude.

For example, "RA", "DEC", "GLON", "GLAT", etc. extracted from "RA--",
"DEC-", "GLON", "GLAT", etc. in the first four characters of
``CTYPEia`` but with trailing dashes removed.
"""

    lng = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``int`` (read-only) The index into the world coord array containing
longitude values.
"""

    lngtyp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``string`` (read-only) Celestial axis type for longitude.

For example, "RA", "DEC", "GLON", "GLAT", etc. extracted from "RA--",
"DEC-", "GLON", "GLAT", etc. in the first four characters of
``CTYPEia`` but with trailing dashes removed.
"""

    lonpole = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double`` The native longitude of the celestial pole.

``LONPOLEa`` (deg).
"""

    mjdavg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double`` Modified Julian Date corresponding to ``DATE-AVG``.

``(MJD = JD - 2400000.5)``.

An undefined value is represented by NaN.

See also
--------
astropy.wcs.Wcsprm.mjdobs
"""

    mjdbeg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double`` Modified Julian Date corresponding to ``DATE-BEG``.

``(MJD = JD - 2400000.5)``.

An undefined value is represented by NaN.

See also
--------
astropy.wcs.Wcsprm.mjdbeg
"""

    mjdend = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double`` Modified Julian Date corresponding to ``DATE-END``.

``(MJD = JD - 2400000.5)``.

An undefined value is represented by NaN.

See also
--------
astropy.wcs.Wcsprm.mjdend
"""

    mjdobs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double`` Modified Julian Date corresponding to ``DATE-OBS``.

``(MJD = JD - 2400000.5)``.

An undefined value is represented by NaN.

See also
--------
astropy.wcs.Wcsprm.mjdavg
"""

    mjdref = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double`` Modified Julian Date corresponding to ``DATE-REF``.

``(MJD = JD - 2400000.5)``.

An undefined value is represented by NaN.

See also
--------
astropy.wcs.Wcsprm.dateref
"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``string`` The name given to the coordinate representation
``WCSNAMEa``.
"""

    naxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``int`` (read-only) The number of axes (pixel and coordinate).

Given by the ``NAXIS`` or ``WCSAXESa`` keyvalues.

The number of coordinate axes is determined at parsing time, and can
not be subsequently changed.

It is determined from the highest of the following:

  1. ``NAXIS``

  2. ``WCSAXESa``

  3. The highest axis number in any parameterized WCS keyword.  The
     keyvalue, as well as the keyword, must be syntactically valid
     otherwise it will not be considered.

If none of these keyword types is present, i.e. if the header only
contains auxiliary WCS keywords for a particular coordinate
representation, then no coordinate description is constructed for it.

This value may differ for different coordinate representations of the
same image.
"""

    obsgeo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double array[3]`` Location of the observer in a standard terrestrial
reference frame.

``OBSGEO-X``, ``OBSGEO-Y``, ``OBSGEO-Z`` (in meters).

An undefined value is represented by NaN.
"""

    obsorbit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``string`` URI, URL, or name of an orbit ephemeris file giving spacecraft coordinates relating to TREFPOS.

See also
--------
astropy.wcs.Wcsprm.trefpos

"""

    pc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double array[naxis][naxis]`` The ``PCi_ja`` (pixel coordinate)
transformation matrix.

The order is::

  [[PC1_1, PC1_2],
   [PC2_1, PC2_2]]

For historical compatibility, three alternate specifications of the
linear transformations are available in wcslib.  The canonical
``PCi_ja`` with ``CDELTia``, ``CDi_ja``, and the deprecated
``CROTAia`` keywords.  Although the latter may not formally co-exist
with ``PCi_ja``, the approach here is simply to ignore them if given
in conjunction with ``PCi_ja``.

`~astropy.wcs.Wcsprm.has_pc`, `~astropy.wcs.Wcsprm.has_cd` and
`~astropy.wcs.Wcsprm.has_crota` can be used to determine which of
these alternatives are present in the header.

These alternate specifications of the linear transformation matrix are
translated immediately to ``PCi_ja`` by `~astropy.wcs.Wcsprm.set` and
are nowhere visible to the lower-level routines.  In particular,
`~astropy.wcs.Wcsprm.set` resets `~astropy.wcs.Wcsprm.cdelt` to unity
if ``CDi_ja`` is present (and no ``PCi_ja``).  If no ``CROTAia`` is
associated with the latitude axis, `~astropy.wcs.Wcsprm.set` reverts
to a unity ``PCi_ja`` matrix.
"""

    phi0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double`` The native latitude of the fiducial point.

The point whose celestial coordinates are given in ``ref[1:2]``.  If
undefined (NaN) the initialization routine, `~astropy.wcs.Wcsprm.set`,
will set this to a projection-specific default.

See also
--------
astropy.wcs.Wcsprm.theta0
"""

    piximg_matrix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double array[2][2]`` (read-only) Matrix containing the product of
the ``CDELTia`` diagonal matrix and the ``PCi_ja`` matrix.
"""

    plephem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``string`` The Solar System ephemeris used for calculating a pathlength delay.

See also
--------
astropy.wcs.Wcsprm.plephem
"""

    radesys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``string`` The equatorial or ecliptic coordinate system type,
``RADESYSa``.
"""

    restfrq = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double`` Rest frequency (Hz) from ``RESTFRQa``.

An undefined value is represented by NaN.
"""

    restwav = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double`` Rest wavelength (m) from ``RESTWAVa``.

An undefined value is represented by NaN.
"""

    spec = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``int`` (read-only) The index containing the spectral axis values.
"""

    specsys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``string`` Spectral reference frame (standard of rest), ``SPECSYSa``.

See also
--------
astropy.wcs.Wcsprm.ssysobs, astropy.wcs.Wcsprm.velosys
"""

    ssysobs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``string`` Spectral reference frame.

The spectral reference frame in which there is no differential
variation in the spectral coordinate across the field-of-view,
``SSYSOBSa``.

See also
--------
astropy.wcs.Wcsprm.specsys, astropy.wcs.Wcsprm.velosys
"""

    ssyssrc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``string`` Spectral reference frame for redshift.

The spectral reference frame (standard of rest) in which the redshift
was measured, ``SSYSSRCa``.
"""

    tab = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``list of Tabprm`` Tabular coordinate objects.

A list of tabular coordinate objects associated with this WCS.
"""

    telapse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double`` equivalent to the elapsed time between DATE-BEG and DATE-END, in units of TIMEUNIT.

See also
--------
astropy.wcs.Wcsprm.tstart
"""

    theta0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double``  The native longitude of the fiducial point.

The point whose celestial coordinates are given in ``ref[1:2]``.  If
undefined (NaN) the initialization routine, `~astropy.wcs.Wcsprm.set`,
will set this to a projection-specific default.

See also
--------
astropy.wcs.Wcsprm.phi0
"""

    timedel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double`` the resolution of the time stamps.

See also
--------
astropy.wcs.Wcsprm.timedel
"""

    timeoffs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double`` Time offset, which may be used, for example, to provide a uniform clock correction
           for times referenced to DATEREF.

See also
--------
astropy.wcs.Wcsprm.timeoffs
"""

    timepixr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double`` relative position of the time stamps in binned time intervals, a value between 0.0 and 1.0.

See also
--------
astropy.wcs.Wcsprm.timepixr
"""

    timesys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``string`` Time scale (UTC, TAI, etc.) in which all other time-related
auxiliary header values are recorded. Also defines the time scale for
an image axis with CTYPEia set to 'TIME'.

See also
--------
astropy.wcs.Wcsprm.timesys
"""

    timeunit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``string`` Time units in which the following header values are expressed:
``TSTART``, ``TSTOP``, ``TIMEOFFS``, ``TIMSYER``, ``TIMRDER``, ``TIMEDEL``.

It also provides the default value for ``CUNITia`` for time axes.

See also
--------
astropy.wcs.Wcsprm.trefdir
"""

    timrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double`` the accuracy of time stamps relative to each other, in units of TIMEUNIT.

See also
--------
astropy.wcs.Wcsprm.timsyer
"""

    timsyer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double`` the absolute error of the time values, in units of TIMEUNIT.

See also
--------
astropy.wcs.Wcsprm.timrder
"""

    trefdir = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``string`` Reference direction used in calculating a pathlength delay.

See also
--------
astropy.wcs.Wcsprm.trefdir
"""

    trefpos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``string`` Location in space where the recorded time is valid.

See also
--------
astropy.wcs.Wcsprm.trefpos
"""

    tstart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double`` equivalent to DATE-BEG expressed as a time in units of TIMEUNIT relative to DATEREF+TIMEOFFS.

See also
--------
astropy.wcs.Wcsprm.tstop
"""

    tstop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double`` equivalent to DATE-END expressed as a time in units of TIMEUNIT relative to DATEREF+TIMEOFFS.

See also
--------
astropy.wcs.Wcsprm.tstart
"""

    velangl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double`` Velocity angle.

The angle in degrees that should be used to decompose an observed
velocity into radial and transverse components.

An undefined value is represented by NaN.
"""

    velosys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double`` Relative radial velocity.

The relative radial velocity (m/s) between the observer and the
selected standard of rest in the direction of the celestial reference
coordinate, ``VELOSYSa``.

An undefined value is represented by NaN.

See also
--------
astropy.wcs.Wcsprm.specsys, astropy.wcs.Wcsprm.ssysobs
"""

    velref = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``int`` AIPS velocity code.

From ``VELREF`` keyword.
"""

    xposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double`` effective exposure time in units of TIMEUNIT.

See also
--------
astropy.wcs.Wcsprm.timeunit
"""

    zsource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``double`` The redshift, ``ZSOURCEa``, of the source.

An undefined value is represented by NaN.
"""


    __hash__ = None


class _Wcs(object):
    """
    Wcs(*sip, cpdis, wcsprm, det2im*)
    
    Wcs objects amalgamate basic WCS (as provided by `wcslib`_), with
    `SIP`_ and `distortion paper`_ operations.
    
    To perform all distortion corrections and WCS transformation, use
    ``all_pix2world``.
    
    Parameters
    ----------
    sip : `~astropy.wcs.Sip` object or `None`
    
    cpdis : A pair of `~astropy.wcs.DistortionLookupTable` objects, or
      ``(None, None)``.
    
    wcsprm : `~astropy.wcs.Wcsprm` object
    
    det2im : A pair of `~astropy.wcs.DistortionLookupTable` objects, or
       ``(None, None)``.
    """
    def _all_pix2world(self, *args, **kwargs): # real signature unknown
        """
        all_pix2world(pixcrd, origin) -> ``double array[ncoord][nelem]``
        
        Transforms pixel coordinates to world coordinates.
        
        Does the following:
        
            - Detector to image plane correction (if present)
        
            - SIP distortion correction (if present)
        
            - FITS WCS distortion correction (if present)
        
            - wcslib "core" WCS transformation
        
        The first three (the distortion corrections) are done in parallel.
        
        Parameters
        ----------
        pixcrd : double array[ncoord][nelem]
            Array of pixel coordinates.
        
        
        origin : int
            Specifies the origin of pixel values.  The Fortran and FITS
            standards use an origin of 1.  Numpy and C use array indexing with
            origin at 0.
        
        
        Returns
        -------
        world : double array[ncoord][nelem]
            Returns an array of world coordinates.
        
        Raises
        ------
        MemoryError
            Memory allocation failed.
        
        SingularMatrixError
            Linear transformation matrix is singular.
        
        InconsistentAxisTypesError
            Inconsistent or unrecognized coordinate axis types.
        
        ValueError
            Invalid parameter value.
        
        ValueError
            Invalid coordinate transformation parameters.
        
        ValueError
            x- and y-coordinate arrays are not the same size.
        
        InvalidTransformError
            Invalid coordinate transformation.
        
        InvalidTransformError
            Ill-conditioned coordinate transformation parameters.
        """
        pass

    def _det2im(self, *args, **kwargs): # real signature unknown
        """ Convert detector coordinates to image plane coordinates. """
        pass

    def _p4_pix2foc(self, *args, **kwargs): # real signature unknown
        """
        p4_pix2foc(*pixcrd, origin*) -> double array[ncoord][nelem]
        
        Convert pixel coordinates to focal plane coordinates using `distortion
        paper`_ lookup-table correction.
        
        Parameters
        ----------
        pixcrd : double array[ncoord][nelem].
            Array of pixel coordinates.
        
        
        origin : int
            Specifies the origin of pixel values.  The Fortran and FITS
            standards use an origin of 1.  Numpy and C use array indexing with
            origin at 0.
        
        
        Returns
        -------
        foccrd : double array[ncoord][nelem]
            Returns an array of focal plane coordinates.
        
        Raises
        ------
        MemoryError
            Memory allocation failed.
        
        ValueError
            Invalid coordinate transformation parameters.
        """
        pass

    def _pix2foc(self, *args, **kwargs): # real signature unknown
        """
        pix2foc(*pixcrd, origin*) -> double array[ncoord][nelem]
        
        Perform both `SIP`_ polynomial and `distortion paper`_ lookup-table
        correction in parallel.
        
        Parameters
        ----------
        pixcrd : double array[ncoord][nelem]
            Array of pixel coordinates.
        
        
        origin : int
            Specifies the origin of pixel values.  The Fortran and FITS
            standards use an origin of 1.  Numpy and C use array indexing with
            origin at 0.
        
        
        Returns
        -------
        foccrd : double array[ncoord][nelem]
            Returns an array of focal plane coordinates.
        
        Raises
        ------
        MemoryError
            Memory allocation failed.
        
        ValueError
            Invalid coordinate transformation parameters.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    cpdis1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """`~astropy.wcs.DistortionLookupTable`

The pre-linear transformation distortion lookup table, ``CPDIS1``.
"""

    cpdis2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """`~astropy.wcs.DistortionLookupTable`

The pre-linear transformation distortion lookup table, ``CPDIS2``.
"""

    det2im1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A `~astropy.wcs.DistortionLookupTable` object for detector to image plane
correction in the *x*-axis.
"""

    det2im2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A `~astropy.wcs.DistortionLookupTable` object for detector to image plane
correction in the *y*-axis.
"""

    sip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get/set the `~astropy.wcs.Sip` object for performing `SIP`_ distortion
correction.
"""

    wcs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A `~astropy.wcs.Wcsprm` object to perform the basic `wcslib`_ WCS
transformation.
"""



# variables with complex values

_ASTROPY_WCS_API = None # (!) real value is '<capsule object "_wcs._ASTROPY_WCS_API" at 0x0000029958537930>'

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000029958548518>'

__spec__ = None # (!) real value is "ModuleSpec(name='astropy.wcs._wcs', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000029958548518>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\astropy\\\\wcs\\\\_wcs.cp37-win_amd64.pyd')"

