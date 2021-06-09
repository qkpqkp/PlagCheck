# encoding: utf-8
# module tables.utilsextension
# from C:\Users\Doly\Anaconda3\lib\site-packages\tables\utilsextension.cp37-win_amd64.pyd
# by generator 1.147
""" Cython utilities for PyTables and HDF5 library. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import os as os # C:\Users\Doly\Anaconda3\lib\os.py
import sys as sys # <module 'sys' (built-in)>
import warnings as warnings # C:\Users\Doly\Anaconda3\lib\warnings.py
import zlib as zlib # <module 'zlib' (built-in)>
import numpy as numpy # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py
import tables as tables # C:\Users\Doly\Anaconda3\lib\site-packages\tables\__init__.py
import tables.atom as __tables_atom


# Variables with simple values

H5T_IEEE_F32 = 216172782113783862
H5T_IEEE_F64 = 216172782113783864

H5T_STD_B8 = 216172782113783884
H5T_STD_I16 = 216172782113783870
H5T_STD_I32 = 216172782113783872
H5T_STD_I64 = 216172782113783874
H5T_STD_I8 = 216172782113783868
H5T_STD_U16 = 216172782113783878
H5T_STD_U32 = 216172782113783880
H5T_STD_U64 = 216172782113783882
H5T_STD_U8 = 216172782113783876

H5T_UNIX_D32 = 216172782113783892
H5T_UNIX_D64 = 216172782113783894

platform_byteorder = 0

zlib_imported = True

# functions

def atom_from_hdf5_type(*args, **kwargs): # real signature unknown
    """
    Get an atom from a type_id.
    
      See `hdf5_to_np_ext_type` for an explanation of the `pure_numpy_types`
      parameter.
    """
    pass

def atom_to_hdf5_type(*args, **kwargs): # real signature unknown
    pass

def bisect_left(*args, **kwargs): # real signature unknown
    """
    Return the index where to insert item x in list a, assuming a is sorted.
    
      The return value i is such that all e in a[:i] have e < x, and all e in
      a[i:] have e >= x.  So if x already appears in the list, i points just
      before the leftmost x already there.
    """
    pass

def bisect_right(*args, **kwargs): # real signature unknown
    """
    Return the index where to insert item x in list a, assuming a is sorted.
    
      The return value i is such that all e in a[:i] have e <= x, and all e in
      a[i:] have e > x.  So if x already appears in the list, i points just
      beyond the rightmost x already there.
    """
    pass

def blosc_compcode_to_compname_(*args, **kwargs): # real signature unknown
    """
    blosc_compcode_to_compname()
    
      Returns the compressor name associated with compressor code.
    
      Parameters
      ----------
      None
    
      Returns
      -------
      out : string
          The name of the compressor.
    """
    pass

def blosc_compressor_list(): # real signature unknown; restored from __doc__
    """
    blosc_compressor_list()
    
      Returns a list of compressors available in the Blosc build.
    
      Parameters
      ----------
      None
    
      Returns
      -------
      out : list
          The list of names.
    """
    pass

def blosc_get_complib_info_(*args, **kwargs): # real signature unknown
    """
    Get info from compression libraries included in the current build
      of blosc.
    
      Returns a mapping containing the compressor names as keys and the
      tuple (complib, version) as values.
    """
    pass

def check_file_access(filename, mode=None): # reliably restored by inspect
    """
    Check for file access in the specified `mode`.
    
        `mode` is one of the modes supported by `File` objects.  If the file
        indicated by `filename` can be accessed using that `mode`, the
        function ends successfully.  Else, an ``IOError`` is raised
        explaining the reason of the failure.
    
        All this paraphernalia is used to avoid the lengthy and scaring HDF5
        messages produced when there are problems opening a file.  No
        changes are ever made to the file system.
    """
    pass

def create_nested_type(*args, **kwargs): # real signature unknown
    """ Create a nested type based on a description and return an HDF5 type. """
    pass

def encode_filename(*args, **kwargs): # real signature unknown
    """ Return the encoded filename in the filesystem encoding. """
    pass

def enum_from_hdf5(enumId): # real signature unknown; restored from __doc__
    """
    enum_from_hdf5(enumId) -> (Enum, npType)
    
      Convert an HDF5 enumerated type to a PyTables one.
    
      This function takes an HDF5 enumerated type and returns an `Enum`
      instance built from that, and the NumPy type used to encode it.
    """
    pass

def enum_to_hdf5(*args, **kwargs): # real signature unknown
    """
    Convert a PyTables enumerated type to an HDF5 one.
    
      This function creates an HDF5 enumerated type from the information
      contained in `enumAtom` (an ``Atom`` object), with the specified
      `byteorder` (a string).  The resulting HDF5 enumerated type is
      returned.
    """
    pass

def get_filters(*args, **kwargs): # real signature unknown
    """ Get a dictionary with the filter names and cd_values """
    pass

def get_hdf5_version(*args, **kwargs): # real signature unknown
    """ Get the underlying HDF5 library version """
    pass

def get_nested_field(*args, **kwargs): # real signature unknown
    """
    Get the maybe nested field named `fieldname` from the `recarray`.
    
      The `fieldname` may be a simple field name or a nested field name
      with slah-separated components.
    """
    pass

def get_pytables_version(*args, **kwargs): # real signature unknown
    """ Return this extension version. """
    pass

def get_type_enum(*args, **kwargs): # real signature unknown
    """
    _getTypeEnum(h5type) -> hid_t
    
      Get the native HDF5 enumerated type of `h5type`.
    
      If `h5type` is an enumerated type, it is returned.  If it is a
      variable-length type with an enumerated base type, this is returned.  If it
      is a multi-dimensional type with an enumerated base type, this is returned.
      Else, a ``TypeError`` is raised.
    """
    pass

def hdf5_to_np_ext_type(*args, **kwargs): # real signature unknown
    """
    Map the atomic HDF5 type to a string repr of NumPy extended codes.
    
      If `pure_numpy_types` is true, detected HDF5 types that does not match pure
      NumPy types will raise a ``TypeError`` exception.  If not, HDF5 types like
      TIME, VLEN or ENUM are passed through.
    
      If `atom` is true, the resulting repr is meant for atoms.  If not, the
      result is meant for attributes.
    
      Returns the string repr of type and its shape.  The exception is for
      compounds types, that returns a NumPy dtype and shape instead.
    """
    pass

def hdf5_to_np_nested_type(*args, **kwargs): # real signature unknown
    """ Given a HDF5 `type_id`, return a dtype string representation of it. """
    pass

def is_hdf5_file(filename): # real signature unknown; restored from __doc__
    """
    is_hdf5_file(filename)
    
      Determine whether a file is in the HDF5 format.
    
      When successful, it returns a true value if the file is an HDF5
      file, false otherwise.  If there were problems identifying the file,
      an HDF5ExtError is raised.
    """
    pass

def is_pytables_file(filename): # real signature unknown; restored from __doc__
    """
    is_pytables_file(filename)
    
      Determine whether a file is in the PyTables format.
    
      When successful, it returns the format version string if the file is a
      PyTables file, None otherwise.  If there were problems identifying the
      file, an HDF5ExtError is raised.
    """
    pass

def load_enum(): # real signature unknown; restored from __doc__
    """
    load_enum() -> (Enum, npType)
    
      Load the enumerated HDF5 type associated with this type_id.
    
      It returns an `Enum` instance built from that, and the
      NumPy type used to encode it.
    """
    pass

def nan_aware_ge(*args, **kwargs): # real signature unknown
    pass

def nan_aware_gt(*args, **kwargs): # real signature unknown
    pass

def nan_aware_le(*args, **kwargs): # real signature unknown
    pass

def nan_aware_lt(*args, **kwargs): # real signature unknown
    pass

def read_f_attr(*args, **kwargs): # real signature unknown
    """
    Read PyTables file attributes (i.e. in root group).
    
      Returns the value of the `attr_name` attribute in root group, or `None`
      if it does not exist.  This call cannot fail.
    """
    pass

def set_blosc_max_threads(nthreads): # real signature unknown; restored from __doc__
    """
    set_blosc_max_threads(nthreads)
    
      Set the maximum number of threads that Blosc can use.
    
      This actually overrides the :data:`tables.parameters.MAX_BLOSC_THREADS`
      setting in :mod:`tables.parameters`, so the new value will be effective until
      this function is called again or a new file with a different
      :data:`tables.parameters.MAX_BLOSC_THREADS` value is specified.
    
      Returns the previous setting for maximum threads.
    """
    pass

def silence_hdf5_messages(silence=True): # real signature unknown; restored from __doc__
    """
    silence_hdf5_messages(silence=True)
    
        Silence (or re-enable) messages from the HDF5 C library.
    
        The *silence* parameter can be used control the behaviour and reset
        the standard HDF5 logging.
    
        .. versionadded:: 2.4
    """
    pass

def which_class(*args, **kwargs): # real signature unknown
    """ Detects a class ID using heuristics. """
    pass

def which_lib_version(name): # real signature unknown; restored from __doc__
    """
    which_lib_version(name)
    
      Get version information about a C library.
    
      If the library indicated by name is available, this function returns a
      3-tuple containing the major library version as an integer, its full version
      as a string, and the version date as a string. If the library is not
      available, None is returned.
    
      The currently supported library names are hdf5, zlib, lzo, bzip2, and blosc. If
      another name is given, a ValueError is raised.
    """
    pass

def _arch_without_blosc(*args, **kwargs): # real signature unknown
    pass

def _broken_hdf5_long_double(*args, **kwargs): # real signature unknown
    pass

def _dump_h5_backtrace(*args, **kwargs): # real signature unknown
    pass

# classes

class Atom(object):
    """
    Defines the type of atomic cells stored in a dataset.
    
        The meaning of *atomic* is that individual elements of a cell can
        not be extracted directly by indexing (i.e.  __getitem__()) the
        dataset; e.g. if a dataset has shape (2, 2) and its atoms have
        shape (3,), to get the third element of the cell at (1, 0) one
        should use dataset[1,0][2] instead of dataset[1,0,2].
    
        The Atom class is meant to declare the different properties of the
        *base element* (also known as *atom*) of CArray, EArray and
        VLArray datasets, although they are also used to describe the base
        elements of Array datasets. Atoms have the property that their
        length is always the same.  However, you can grow datasets along
        the extensible dimension in the case of EArray or put a variable
        number of them on a VLArray row. Moreover, they are not restricted
        to scalar values, and they can be *fully multidimensional
        objects*.
    
        Parameters
        ----------
        itemsize : int
            For types with a non-fixed size, this sets the size in
            bytes of individual items in the atom.
        shape : tuple
            Sets the shape of the atom. An integer shape of
            N is equivalent to the tuple (N,).
        dflt
            Sets the default value for the atom.
    
        The following are the public methods and attributes of the Atom class.
    
        Notes
        -----
        A series of descendant classes are offered in order to make the
        use of these element descriptions easier. You should use a
        particular Atom descendant class whenever you know the exact type
        you will need when writing your code. Otherwise, you may use one
        of the Atom.from_*() factory Methods.
    
        .. rubric:: Atom attributes
    
        .. attribute:: dflt
    
            The default value of the atom.
    
            If the user does not supply a value for an element while
            filling a dataset, this default value will be written to disk.
            If the user supplies a scalar value for a multidimensional
            atom, this value is automatically *broadcast* to all the items
            in the atom cell. If dflt is not supplied, an appropriate zero
            value (or *null* string) will be chosen by default.  Please
            note that default values are kept internally as NumPy objects.
    
        .. attribute:: dtype
    
            The NumPy dtype that most closely matches this atom.
    
        .. attribute:: itemsize
    
            Size in bytes of a single item in the atom.
            Specially useful for atoms of the string kind.
    
        .. attribute:: kind
    
            The PyTables kind of the atom (a string).
    
        .. attribute:: shape
    
            The shape of the atom (a tuple for scalar atoms).
    
        .. attribute:: type
    
            The PyTables type of the atom (a string).
    
            Atoms can be compared with atoms and other objects for
            strict (in)equality without having to compare individual
            attributes::
    
                >>> atom1 = StringAtom(itemsize=10)  # same as ``atom2``
                >>> atom2 = Atom.from_kind('string', 10)  # same as ``atom1``
                >>> atom3 = IntAtom()
                >>> atom1 == 'foo'
                False
                >>> atom1 == atom2
                True
                >>> atom2 != atom1
                False
                >>> atom1 == atom3
                False
                >>> atom3 != atom2
                True
    """
    def copy(self, **override): # reliably restored by inspect
        """
        Get a copy of the atom, possibly overriding some arguments.
        
                Constructor arguments to be overridden must be passed as
                keyword arguments::
        
                    >>> atom1 = Int32Atom(shape=12)
                    >>> atom2 = atom1.copy()
                    >>> print(atom1)
                    Int32Atom(shape=(12,), dflt=0)
                    >>> print(atom2)
                    Int32Atom(shape=(12,), dflt=0)
                    >>> atom1 is atom2
                    False
                    >>> atom3 = atom1.copy(shape=(2, 2))
                    >>> print(atom3)
                    Int32Atom(shape=(2, 2), dflt=0)
                    >>> atom1.copy(foobar=42)
                    Traceback (most recent call last):
                    ...
                    TypeError: __init__() got an unexpected keyword argument 'foobar'
        """
        pass

    @classmethod
    def from_dtype(cls, numpy_dtype, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Create an Atom from a NumPy dtype.
        
                An optional default value may be specified as the dflt
                argument. Information in the dtype not represented in an Atom is
                ignored::
        
                    >>> import numpy
                    >>> Atom.from_dtype(numpy.dtype((numpy.int16, (2, 2))))
                    Int16Atom(shape=(2, 2), dflt=0)
                    >>> Atom.from_dtype(numpy.dtype('float64'))
                    Float64Atom(shape=(), dflt=0.0)
        
                Note: for easier use in Python 3, where all strings lead to the
                Unicode dtype, this dtype will also generate a StringAtom. Since
                this is only viable for strings that are castable as ascii, a
                warning is issued.
        
                    >>> Atom.from_dtype(numpy.dtype('U20')) # doctest: +SKIP
                    Atom.py:392: FlavorWarning: support for unicode type is very limited,
                        and only works for strings that can be cast as ascii
                    StringAtom(itemsize=20, shape=(), dflt=b'')
        """
        pass

    @classmethod
    def from_kind(cls, p_int, itemsize=2, shape=22): # real signature unknown; restored from __doc__
        """
        Create an Atom from a PyTables kind.
        
                Optional item size, shape and default value may be
                specified as the itemsize, shape and dflt
                arguments, respectively. Bear in mind that not all atoms support
                a default item size::
        
                    >>> Atom.from_kind('int', itemsize=2, shape=(2, 2))
                    Int16Atom(shape=(2, 2), dflt=0)
                    >>> Atom.from_kind('int', shape=(2, 2))
                    Int32Atom(shape=(2, 2), dflt=0)
                    >>> Atom.from_kind('int', shape=1)
                    Int32Atom(shape=(1,), dflt=0)
                    >>> Atom.from_kind('string', dflt=b'hello')
                    Traceback (most recent call last):
                    ...
                    ValueError: no default item size for kind ``string``
                    >>> Atom.from_kind('Float')
                    Traceback (most recent call last):
                    ...
                    ValueError: unknown kind: 'Float'
        
                Moreover, some kinds with atypical constructor signatures
                are not supported; you need to use the proper
                constructor::
        
                    >>> Atom.from_kind('enum') #doctest: +ELLIPSIS
                    Traceback (most recent call last):
                    ...
                    ValueError: the ``enum`` kind is not supported...
        """
        pass

    @classmethod
    def from_sctype(cls, numpy_int16, shape=22): # real signature unknown; restored from __doc__
        """
        Create an Atom from a NumPy scalar type sctype.
        
                Optional shape and default value may be specified as the
                shape and dflt
                arguments, respectively. Information in the
                sctype not represented in an Atom is ignored::
        
                    >>> import numpy
                    >>> Atom.from_sctype(numpy.int16, shape=(2, 2))
                    Int16Atom(shape=(2, 2), dflt=0)
                    >>> Atom.from_sctype('S5', dflt='hello')
                    Traceback (most recent call last):
                    ...
                    ValueError: unknown NumPy scalar type: 'S5'
                    >>> Atom.from_sctype('Float64')
                    Float64Atom(shape=(), dflt=0.0)
        """
        pass

    @classmethod
    def from_type(cls, bool): # real signature unknown; restored from __doc__
        """
        Create an Atom from a PyTables type.
        
                Optional shape and default value may be specified as the
                shape and dflt arguments, respectively::
        
                    >>> Atom.from_type('bool')
                    BoolAtom(shape=(), dflt=False)
                    >>> Atom.from_type('int16', shape=(2, 2))
                    Int16Atom(shape=(2, 2), dflt=0)
                    >>> Atom.from_type('string40', dflt='hello')
                    Traceback (most recent call last):
                    ...
                    ValueError: unknown type: 'string40'
                    >>> Atom.from_type('Float64')
                    Traceback (most recent call last):
                    ...
                    ValueError: unknown type: 'Float64'
        """
        pass

    @classmethod
    def prefix(cls, *args, **kwargs): # real signature unknown
        """ Return the atom class prefix. """
        pass

    def _get_init_args(self): # reliably restored by inspect
        """
        Get a dictionary of instance constructor arguments.
        
                This implementation works on classes which use the same names
                for both constructor arguments and instance attributes.
        """
        pass

    def _is_equal_to_atom(self, atom): # reliably restored by inspect
        """ Is this object equal to the given `atom`? """
        pass

    def __eq__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, nptype, shape, dflt): # reliably restored by inspect
        # no doc
        pass

    def __ne__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    ndim = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of dimensions of the atom.

        .. versionadded:: 2.4"""

    recarrtype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """String type to be used in numpy.rec.array()."""

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Total size in bytes of the atom."""

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'tables.atom\', \'__doc__\': "Defines the type of atomic cells stored in a dataset.\\n\\n    The meaning of *atomic* is that individual elements of a cell can\\n    not be extracted directly by indexing (i.e.  __getitem__()) the\\n    dataset; e.g. if a dataset has shape (2, 2) and its atoms have\\n    shape (3,), to get the third element of the cell at (1, 0) one\\n    should use dataset[1,0][2] instead of dataset[1,0,2].\\n\\n    The Atom class is meant to declare the different properties of the\\n    *base element* (also known as *atom*) of CArray, EArray and\\n    VLArray datasets, although they are also used to describe the base\\n    elements of Array datasets. Atoms have the property that their\\n    length is always the same.  However, you can grow datasets along\\n    the extensible dimension in the case of EArray or put a variable\\n    number of them on a VLArray row. Moreover, they are not restricted\\n    to scalar values, and they can be *fully multidimensional\\n    objects*.\\n\\n    Parameters\\n    ----------\\n    itemsize : int\\n        For types with a non-fixed size, this sets the size in\\n        bytes of individual items in the atom.\\n    shape : tuple\\n        Sets the shape of the atom. An integer shape of\\n        N is equivalent to the tuple (N,).\\n    dflt\\n        Sets the default value for the atom.\\n\\n    The following are the public methods and attributes of the Atom class.\\n\\n    Notes\\n    -----\\n    A series of descendant classes are offered in order to make the\\n    use of these element descriptions easier. You should use a\\n    particular Atom descendant class whenever you know the exact type\\n    you will need when writing your code. Otherwise, you may use one\\n    of the Atom.from_*() factory Methods.\\n\\n    .. rubric:: Atom attributes\\n\\n    .. attribute:: dflt\\n\\n        The default value of the atom.\\n\\n        If the user does not supply a value for an element while\\n        filling a dataset, this default value will be written to disk.\\n        If the user supplies a scalar value for a multidimensional\\n        atom, this value is automatically *broadcast* to all the items\\n        in the atom cell. If dflt is not supplied, an appropriate zero\\n        value (or *null* string) will be chosen by default.  Please\\n        note that default values are kept internally as NumPy objects.\\n\\n    .. attribute:: dtype\\n\\n        The NumPy dtype that most closely matches this atom.\\n\\n    .. attribute:: itemsize\\n\\n        Size in bytes of a single item in the atom.\\n        Specially useful for atoms of the string kind.\\n\\n    .. attribute:: kind\\n\\n        The PyTables kind of the atom (a string).\\n\\n    .. attribute:: shape\\n\\n        The shape of the atom (a tuple for scalar atoms).\\n\\n    .. attribute:: type\\n\\n        The PyTables type of the atom (a string).\\n\\n        Atoms can be compared with atoms and other objects for\\n        strict (in)equality without having to compare individual\\n        attributes::\\n\\n            >>> atom1 = StringAtom(itemsize=10)  # same as ``atom2``\\n            >>> atom2 = Atom.from_kind(\'string\', 10)  # same as ``atom1``\\n            >>> atom3 = IntAtom()\\n            >>> atom1 == \'foo\'\\n            False\\n            >>> atom1 == atom2\\n            True\\n            >>> atom2 != atom1\\n            False\\n            >>> atom1 == atom3\\n            False\\n            >>> atom3 != atom2\\n            True\\n\\n    ", \'prefix\': <classmethod object at 0x00000115CF8323C8>, \'from_sctype\': <classmethod object at 0x00000115CF82B4A8>, \'from_dtype\': <classmethod object at 0x00000115CF82B470>, \'from_type\': <classmethod object at 0x00000115CF82B438>, \'from_kind\': <classmethod object at 0x00000115CF83C6D8>, \'size\': <property object at 0x00000115CF869318>, \'recarrtype\': <property object at 0x00000115CF8693B8>, \'ndim\': <property object at 0x00000115CF869408>, \'__init__\': <function Atom.__init__ at 0x00000115CF86B2F0>, \'__repr__\': <function Atom.__repr__ at 0x00000115CF86B378>, \'__eq__\': <function _cmp_dispatcher.<locals>.dispatched_cmp at 0x00000115CF86B400>, \'__ne__\': <function Atom.__ne__ at 0x00000115CF86B488>, \'copy\': <function Atom.copy at 0x00000115CF86B510>, \'_get_init_args\': <function Atom._get_init_args at 0x00000115CF86B598>, \'_is_equal_to_atom\': <function Atom._is_equal_to_atom at 0x00000115CF86B620>, \'__dict__\': <attribute \'__dict__\' of \'Atom\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'Atom\' objects>, \'__hash__\': None})'
    __hash__ = None


class Col(__tables_atom.Atom):
    """
    Defines a non-nested column.
    
        Col instances are used as a means to declare the different properties of a
        non-nested column in a table or nested column.  Col classes are descendants
        of their equivalent Atom classes (see :ref:`AtomClassDescr`), but their
        instances have an additional _v_pos attribute that is used to decide the
        position of the column inside its parent table or nested column (see the
        IsDescription class in :ref:`IsDescriptionClassDescr` for more information
        on column positions).
    
        In the same fashion as Atom, you should use a particular Col descendant
        class whenever you know the exact type you will need when writing your
        code. Otherwise, you may use one of the Col.from_*() factory methods.
    
        Each factory method inherited from the Atom class is available with the
        same signature, plus an additional pos parameter (placed in last position)
        which defaults to None and that may take an integer value.  This parameter
        might be used to specify the position of the column in the table.
    
        Besides, there are the next additional factory methods, available only for
        Col objects.
    
        The following parameters are available for most Col-derived constructors.
    
        Parameters
        ----------
        itemsize : int
            For types with a non-fixed size, this sets the size in bytes of
            individual items in the column.
        shape : tuple
            Sets the shape of the column. An integer shape of N is equivalent to
            the tuple (N,).
        dflt
            Sets the default value for the column.
        pos : int
            Sets the position of column in table.  If unspecified, the position
            will be randomly selected.
    """
    @classmethod
    def from_atom(cls, *args, **kwargs): # real signature unknown
        """
        Create a Col definition from a PyTables atom.
        
                An optional position may be specified as the pos argument.
        """
        pass

    @classmethod
    def from_dtype(cls, *args, **kwargs): # real signature unknown
        """
        Create a `Col` definition from a NumPy `dtype`.
        
                Optional default value and position may be specified as the
                `dflt` and `pos` arguments, respectively.  The `dtype` must have
                a byte order which is irrelevant or compatible with that of the
                system.  Information in the `dtype` not represented in a `Col`
                is ignored.
        """
        pass

    @classmethod
    def from_kind(cls, *args, **kwargs): # real signature unknown
        """
        Create a `Col` definition from a PyTables `kind`.
        
                Optional item size, shape, default value and position may be
                specified as the `itemsize`, `shape`, `dflt` and `pos`
                arguments, respectively.  Bear in mind that not all columns
                support a default item size.
        """
        pass

    @classmethod
    def from_sctype(cls, *args, **kwargs): # real signature unknown
        """
        Create a `Col` definition from a NumPy scalar type `sctype`.
        
                Optional shape, default value and position may be specified as
                the `shape`, `dflt` and `pos` arguments, respectively.
                Information in the `sctype` not represented in a `Col` is
                ignored.
        """
        pass

    @classmethod
    def from_type(cls, *args, **kwargs): # real signature unknown
        """
        Create a `Col` definition from a PyTables `type`.
        
                Optional shape, default value and position may be specified as
                the `shape`, `dflt` and `pos` arguments, respectively.
        """
        pass

    @classmethod
    def prefix(cls, *args, **kwargs): # real signature unknown
        """ Return the column class prefix. """
        pass

    def _get_init_args(self): # reliably restored by inspect
        """ Get a dictionary of instance constructor arguments. """
        pass

    @classmethod
    def _subclass_from_prefix(cls, *args, **kwargs): # real signature unknown
        """ Get a column subclass for the given `prefix`. """
        pass

    def __init__(self, nptype, shape, dflt): # reliably restored by inspect
        # no doc
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    _class_from_prefix = {
        'Bool': tables.BoolCol,
        'Complex': tables.ComplexCol,
        'Complex128': tables.Complex128Col,
        'Complex32': tables.Complex32Col,
        'Complex64': tables.Complex64Col,
        'Enum': tables.EnumCol,
        'Float': tables.FloatCol,
        'Float16': tables.Float16Col,
        'Float32': tables.Float32Col,
        'Float64': tables.Float64Col,
        'Int': tables.IntCol,
        'Int16': tables.Int16Col,
        'Int32': tables.Int32Col,
        'Int64': tables.Int64Col,
        'Int8': tables.Int8Col,
        'String': tables.StringCol,
        'Time': tables.TimeCol,
        'Time32': tables.Time32Col,
        'Time64': tables.Time64Col,
        'UInt': tables.UIntCol,
        'UInt16': tables.UInt16Col,
        'UInt32': tables.UInt32Col,
        'UInt64': tables.UInt64Col,
        'UInt8': tables.UInt8Col,
    }


class Description(object):
    """
    This class represents descriptions of the structure of tables.
    
        An instance of this class is automatically bound to Table (see
        :ref:`TableClassDescr`) objects when they are created.  It provides a
        browseable representation of the structure of the table, made of non-nested
        (Col - see :ref:`ColClassDescr`) and nested (Description) columns.
    
        Column definitions under a description can be accessed as attributes of it
        (*natural naming*). For instance, if table.description is a Description
        instance with a column named col1 under it, the later can be accessed as
        table.description.col1. If col1 is nested and contains a col2 column, this
        can be accessed as table.description.col1.col2. Because of natural naming,
        the names of members start with special prefixes, like in the Group class
        (see :ref:`GroupClassDescr`).
    
    
        .. rubric:: Description attributes
    
        .. attribute:: _v_colobjects
    
            A dictionary mapping the names of the columns hanging
            directly from the associated table or nested column to their
            respective descriptions (Col - see :ref:`ColClassDescr` or
            Description - see :ref:`DescriptionClassDescr` instances).
    
            .. versionchanged:: 3.0
               The *_v_colObjects* attribute has been renamed into
               *_v_colobjects*.
    
        .. attribute:: _v_dflts
    
            A dictionary mapping the names of non-nested columns
            hanging directly from the associated table or nested column
            to their respective default values.
    
        .. attribute:: _v_dtype
    
            The NumPy type which reflects the structure of this
            table or nested column.  You can use this as the
            dtype argument of NumPy array factories.
    
        .. attribute:: _v_dtypes
    
            A dictionary mapping the names of non-nested columns
            hanging directly from the associated table or nested column
            to their respective NumPy types.
    
        .. attribute:: _v_is_nested
    
            Whether the associated table or nested column contains
            further nested columns or not.
    
        .. attribute:: _v_itemsize
    
            The size in bytes of an item in this table or nested column.
    
        .. attribute:: _v_name
    
            The name of this description group. The name of the
            root group is '/'.
    
        .. attribute:: _v_names
    
            A list of the names of the columns hanging directly
            from the associated table or nested column. The order of the
            names matches the order of their respective columns in the
            containing table.
    
        .. attribute:: _v_nested_descr
    
            A nested list of pairs of (name, format) tuples for all the columns
            under this table or nested column. You can use this as the dtype and
            descr arguments of NumPy array factories.
    
            .. versionchanged:: 3.0
               The *_v_nestedDescr* attribute has been renamed into
               *_v_nested_descr*.
    
        .. attribute:: _v_nested_formats
    
            A nested list of the NumPy string formats (and shapes) of all the
            columns under this table or nested column. You can use this as the
            formats argument of NumPy array factories.
    
            .. versionchanged:: 3.0
               The *_v_nestedFormats* attribute has been renamed into
               *_v_nested_formats*.
    
        .. attribute:: _v_nestedlvl
    
            The level of the associated table or nested column in the nested
            datatype.
    
        .. attribute:: _v_nested_names
    
            A nested list of the names of all the columns under this table or
            nested column. You can use this as the names argument of NumPy array
            factories.
    
            .. versionchanged:: 3.0
               The *_v_nestedNames* attribute has been renamed into
               *_v_nested_names*.
    
        .. attribute:: _v_pathname
    
            Pathname of the table or nested column.
    
        .. attribute:: _v_pathnames
    
            A list of the pathnames of all the columns under this table or nested
            column (in preorder).  If it does not contain nested columns, this is
            exactly the same as the :attr:`Description._v_names` attribute.
    
        .. attribute:: _v_types
    
            A dictionary mapping the names of non-nested columns hanging directly
            from the associated table or nested column to their respective PyTables
            types.
    
        .. attribute:: _v_offsets
    
            A list of offsets for all the columns.  If the list is empty, means that
            there are no padding in the data structure.  However, the support for
            offsets is currently limited to flat tables; for nested tables, the
            potential padding is always removed (exactly the same as in pre-3.5
            versions), and this variable is set to empty.
    
            .. versionadded:: 3.5
               Previous to this version all the compound types were converted
               internally to 'packed' types, i.e. with no padding between the
               component types.  Starting with 3.5, the holes in native HDF5
               types (non-nested) are honored and replicated during dataset
               and attribute copies.
    """
    def _f_walk(self, type=None): # reliably restored by inspect
        """
        Iterate over nested columns.
        
                If type is 'All' (the default), all column description objects (Col and
                Description instances) are yielded in top-to-bottom order (preorder).
        
                If type is 'Col' or 'Description', only column descriptions of that
                type are yielded.
        """
        pass

    def _g_set_nested_names_descr(self): # reliably restored by inspect
        """ Computes the nested names and descriptions for nested datatypes. """
        pass

    def _g_set_path_names(self): # reliably restored by inspect
        """
        Compute the pathnames for arbitrary nested descriptions.
        
                This method sets the ``_v_pathname`` and ``_v_pathnames``
                attributes of all the elements (both descriptions and columns)
                in this nested description.
        """
        pass

    def __init__(self, classdict, nestedlvl=-1, validate=True, ptparams=None): # reliably restored by inspect
        # no doc
        pass

    def __repr__(self): # reliably restored by inspect
        """ Gives a detailed Description column representation. """
        pass

    def __str__(self): # reliably restored by inspect
        """ Gives a brief Description representation. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'tables.description\', \'__doc__\': "This class represents descriptions of the structure of tables.\\n\\n    An instance of this class is automatically bound to Table (see\\n    :ref:`TableClassDescr`) objects when they are created.  It provides a\\n    browseable representation of the structure of the table, made of non-nested\\n    (Col - see :ref:`ColClassDescr`) and nested (Description) columns.\\n\\n    Column definitions under a description can be accessed as attributes of it\\n    (*natural naming*). For instance, if table.description is a Description\\n    instance with a column named col1 under it, the later can be accessed as\\n    table.description.col1. If col1 is nested and contains a col2 column, this\\n    can be accessed as table.description.col1.col2. Because of natural naming,\\n    the names of members start with special prefixes, like in the Group class\\n    (see :ref:`GroupClassDescr`).\\n\\n\\n    .. rubric:: Description attributes\\n\\n    .. attribute:: _v_colobjects\\n\\n        A dictionary mapping the names of the columns hanging\\n        directly from the associated table or nested column to their\\n        respective descriptions (Col - see :ref:`ColClassDescr` or\\n        Description - see :ref:`DescriptionClassDescr` instances).\\n\\n        .. versionchanged:: 3.0\\n           The *_v_colObjects* attribute has been renamed into\\n           *_v_colobjects*.\\n\\n    .. attribute:: _v_dflts\\n\\n        A dictionary mapping the names of non-nested columns\\n        hanging directly from the associated table or nested column\\n        to their respective default values.\\n\\n    .. attribute:: _v_dtype\\n\\n        The NumPy type which reflects the structure of this\\n        table or nested column.  You can use this as the\\n        dtype argument of NumPy array factories.\\n\\n    .. attribute:: _v_dtypes\\n\\n        A dictionary mapping the names of non-nested columns\\n        hanging directly from the associated table or nested column\\n        to their respective NumPy types.\\n\\n    .. attribute:: _v_is_nested\\n\\n        Whether the associated table or nested column contains\\n        further nested columns or not.\\n\\n    .. attribute:: _v_itemsize\\n\\n        The size in bytes of an item in this table or nested column.\\n\\n    .. attribute:: _v_name\\n\\n        The name of this description group. The name of the\\n        root group is \'/\'.\\n\\n    .. attribute:: _v_names\\n\\n        A list of the names of the columns hanging directly\\n        from the associated table or nested column. The order of the\\n        names matches the order of their respective columns in the\\n        containing table.\\n\\n    .. attribute:: _v_nested_descr\\n\\n        A nested list of pairs of (name, format) tuples for all the columns\\n        under this table or nested column. You can use this as the dtype and\\n        descr arguments of NumPy array factories.\\n\\n        .. versionchanged:: 3.0\\n           The *_v_nestedDescr* attribute has been renamed into\\n           *_v_nested_descr*.\\n\\n    .. attribute:: _v_nested_formats\\n\\n        A nested list of the NumPy string formats (and shapes) of all the\\n        columns under this table or nested column. You can use this as the\\n        formats argument of NumPy array factories.\\n\\n        .. versionchanged:: 3.0\\n           The *_v_nestedFormats* attribute has been renamed into\\n           *_v_nested_formats*.\\n\\n    .. attribute:: _v_nestedlvl\\n\\n        The level of the associated table or nested column in the nested\\n        datatype.\\n\\n    .. attribute:: _v_nested_names\\n\\n        A nested list of the names of all the columns under this table or\\n        nested column. You can use this as the names argument of NumPy array\\n        factories.\\n\\n        .. versionchanged:: 3.0\\n           The *_v_nestedNames* attribute has been renamed into\\n           *_v_nested_names*.\\n\\n    .. attribute:: _v_pathname\\n\\n        Pathname of the table or nested column.\\n\\n    .. attribute:: _v_pathnames\\n\\n        A list of the pathnames of all the columns under this table or nested\\n        column (in preorder).  If it does not contain nested columns, this is\\n        exactly the same as the :attr:`Description._v_names` attribute.\\n\\n    .. attribute:: _v_types\\n\\n        A dictionary mapping the names of non-nested columns hanging directly\\n        from the associated table or nested column to their respective PyTables\\n        types.\\n\\n    .. attribute:: _v_offsets\\n\\n        A list of offsets for all the columns.  If the list is empty, means that\\n        there are no padding in the data structure.  However, the support for\\n        offsets is currently limited to flat tables; for nested tables, the\\n        potential padding is always removed (exactly the same as in pre-3.5\\n        versions), and this variable is set to empty.\\n\\n        .. versionadded:: 3.5\\n           Previous to this version all the compound types were converted\\n           internally to \'packed\' types, i.e. with no padding between the\\n           component types.  Starting with 3.5, the holes in native HDF5\\n           types (non-nested) are honored and replicated during dataset\\n           and attribute copies.\\n    ", \'__init__\': <function Description.__init__ at 0x00000115CF97F268>, \'_g_set_nested_names_descr\': <function Description._g_set_nested_names_descr at 0x00000115CF97F2F0>, \'_g_set_path_names\': <function Description._g_set_path_names at 0x00000115CF97F378>, \'_f_walk\': <function Description._f_walk at 0x00000115CF97F400>, \'__repr__\': <function Description.__repr__ at 0x00000115CF97F488>, \'__str__\': <function Description.__str__ at 0x00000115CF97F510>, \'__dict__\': <attribute \'__dict__\' of \'Description\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'Description\' objects>})'


class Enum(object):
    """
    Enumerated type.
    
        Each instance of this class represents an enumerated type. The
        values of the type must be declared
        *exhaustively* and named with
        *strings*, and they might be given explicit
        concrete values, though this is not compulsory. Once the type is
        defined, it can not be modified.
    
        There are three ways of defining an enumerated type. Each one
        of them corresponds to the type of the only argument in the
        constructor of Enum:
    
        - *Sequence of names*: each enumerated
          value is named using a string, and its order is determined by
          its position in the sequence; the concrete value is assigned
          automatically::
    
              >>> boolEnum = Enum(['True', 'False'])
    
        - *Mapping of names*: each enumerated
          value is named by a string and given an explicit concrete value.
          All of the concrete values must be different, or a
          ValueError will be raised::
    
              >>> priority = Enum({'red': 20, 'orange': 10, 'green': 0})
              >>> colors = Enum({'red': 1, 'blue': 1})
              Traceback (most recent call last):
              ...
              ValueError: enumerated values contain duplicate concrete values: 1
    
        - *Enumerated type*: in that case, a copy
          of the original enumerated type is created. Both enumerated
          types are considered equal::
    
              >>> prio2 = Enum(priority)
              >>> priority == prio2
              True
    
        Please note that names starting with _ are
        not allowed, since they are reserved for internal usage::
    
            >>> prio2 = Enum(['_xx'])
            Traceback (most recent call last):
            ...
            ValueError: name of enumerated value can not start with ``_``: '_xx'
    
        The concrete value of an enumerated value is obtained by
        getting its name as an attribute of the Enum
        instance (see __getattr__()) or as an item (see
        __getitem__()). This allows comparisons between
        enumerated values and assigning them to ordinary Python
        variables::
    
            >>> redv = priority.red
            >>> redv == priority['red']
            True
            >>> redv > priority.green
            True
            >>> priority.red == priority.orange
            False
    
        The name of the enumerated value corresponding to a concrete
        value can also be obtained by using the
        __call__() method of the enumerated type. In this
        way you get the symbolic name to use it later with
        __getitem__()::
    
            >>> priority(redv)
            'red'
            >>> priority.red == priority[priority(priority.red)]
            True
    
        (If you ask, the __getitem__() method is
        not used for this purpose to avoid ambiguity in the case of using
        strings as concrete values.)
    """
    def _check_and_set_pair(self, name, value): # reliably restored by inspect
        """ Check validity of enumerated value and insert it into type. """
        pass

    def __call__(self, value, *default): # reliably restored by inspect
        """
        Get the name of the enumerated value with that concrete value.
        
                If there is no value with that concrete value in the enumeration and a
                second argument is given as a default, this is returned. Else, a
                ValueError is raised.
        
                This method can be used for checking that a concrete value belongs to
                the set of concrete values in an enumerated type.
        
                Examples
                --------
                Let ``enum`` be an enumerated type defined as:
        
                >>> enum = Enum({'T0': 0, 'T1': 2, 'T2': 5})
        
                then:
        
                >>> enum(5)
                'T2'
                >>> enum(42, None) is None
                True
                >>> enum(42)
                Traceback (most recent call last):
                  ...
                ValueError: no enumerated value with that concrete value: 42
        """
        pass

    def __contains__(self, name): # reliably restored by inspect
        """
        Is there an enumerated value with that name in the type?
        
                If the enumerated type has an enumerated value with that name, True is
                returned.  Otherwise, False is returned. The name must be a string.
        
                This method does *not* check for concrete values matching a value in an
                enumerated type. For that, please use the :meth:`Enum.__call__` method.
        
                Examples
                --------
                Let ``enum`` be an enumerated type defined as:
        
                >>> enum = Enum({'T0': 0, 'T1': 2, 'T2': 5})
        
                then:
        
                >>> 'T1' in enum
                True
                >>> 'foo' in enum
                False
                >>> 0 in enum
                Traceback (most recent call last):
                  ...
                TypeError: name of enumerated value is not a string: 0
                >>> enum.T1 in enum  # Be careful with this!
                Traceback (most recent call last):
                  ...
                TypeError: name of enumerated value is not a string: 2
        """
        pass

    def __delattr__(self, name): # reliably restored by inspect
        """ This operation is forbidden. """
        pass

    def __delitem__(self, name): # reliably restored by inspect
        """ This operation is forbidden. """
        pass

    def __eq__(self, other): # reliably restored by inspect
        """
        Is the other enumerated type equivalent to this one?
        
                Two enumerated types are equivalent if they have exactly the same
                enumerated values (i.e. with the same names and concrete values).
        
                Examples
                --------
        
                Let ``enum*`` be enumerated types defined as:
        
                >>> enum1 = Enum({'T0': 0, 'T1': 2})
                >>> enum2 = Enum(enum1)
                >>> enum3 = Enum({'T1': 2, 'T0': 0})
                >>> enum4 = Enum({'T0': 0, 'T1': 2, 'T2': 5})
                >>> enum5 = Enum({'T0': 0})
                >>> enum6 = Enum({'T0': 10, 'T1': 20})
        
                then:
        
                >>> enum1 == enum1
                True
                >>> enum1 == enum2 == enum3
                True
                >>> enum1 == enum4
                False
                >>> enum5 == enum1
                False
                >>> enum1 == enum6
                False
        
                Comparing enumerated types with other kinds of objects produces
                a false result:
        
                >>> enum1 == {'T0': 0, 'T1': 2}
                False
                >>> enum1 == ['T0', 'T1']
                False
                >>> enum1 == 2
                False
        """
        pass

    def __getattr__(self, name): # reliably restored by inspect
        """
        Get the concrete value of the enumerated value with that name.
        
                The name of the enumerated value must be a string. If there is no value
                with that name in the enumeration, an AttributeError is raised.
        
                Examples
                --------
                Let ``enum`` be an enumerated type defined as:
        
                >>> enum = Enum({'T0': 0, 'T1': 2, 'T2': 5})
        
                then:
        
                >>> enum.T1
                2
                >>> enum.foo
                Traceback (most recent call last):
                  ...
                AttributeError: no enumerated value with that name: 'foo'
        """
        pass

    def __getitem__(self, name): # reliably restored by inspect
        """
        Get the concrete value of the enumerated value with that name.
        
                The name of the enumerated value must be a string. If there is no value
                with that name in the enumeration, a KeyError is raised.
        
                Examples
                --------
        
                Let ``enum`` be an enumerated type defined as:
        
                >>> enum = Enum({'T0': 0, 'T1': 2, 'T2': 5})
        
                then:
        
                >>> enum['T1']
                2
                >>> enum['foo']
                Traceback (most recent call last):
                  ...
                KeyError: "no enumerated value with that name: 'foo'"
        """
        pass

    def __init__(self, enum): # reliably restored by inspect
        # no doc
        pass

    def __iter__(self): # reliably restored by inspect
        """
        Iterate over the enumerated values.
        
                Enumerated values are returned as (name, value) pairs *in no particular
                order*.
        
                Examples
                --------
                >>> enumvals = {'red': 4, 'green': 2, 'blue': 1}
                >>> enum = Enum(enumvals)
                >>> enumdict = dict([(name, value) for (name, value) in enum])
                >>> enumvals == enumdict
                True
        """
        pass

    def __len__(self): # reliably restored by inspect
        """
        Return the number of enumerated values in the enumerated type.
        
                Examples
                --------
                >>> len(Enum(['e%d' % i for i in range(10)]))
                10
        """
        pass

    def __ne__(self, other): # reliably restored by inspect
        """
        Is the `other` enumerated type different from this one?
        
                Two enumerated types are different if they don't have exactly
                the same enumerated values (i.e. with the same names and
                concrete values).
        
                Examples
                --------
        
                Let ``enum*`` be enumerated types defined as:
        
                >>> enum1 = Enum({'T0': 0, 'T1': 2})
                >>> enum2 = Enum(enum1)
                >>> enum3 = Enum({'T1': 2, 'T0': 0})
                >>> enum4 = Enum({'T0': 0, 'T1': 2, 'T2': 5})
                >>> enum5 = Enum({'T0': 0})
                >>> enum6 = Enum({'T0': 10, 'T1': 20})
        
                then:
        
                >>> enum1 != enum1
                False
                >>> enum1 != enum2 != enum3
                False
                >>> enum1 != enum4
                True
                >>> enum5 != enum1
                True
                >>> enum1 != enum6
                True
        """
        pass

    def __repr__(self): # reliably restored by inspect
        """
        Return the canonical string representation of the enumeration. The
                output of this method can be evaluated to give a new enumeration object
                that will compare equal to this one.
        
                Examples
                --------
                >>> repr(Enum({'name': 10}))
                "Enum({'name': 10})"
        """
        pass

    def __setattr__(self, name, value): # reliably restored by inspect
        """ This operation is forbidden. """
        pass

    def __setitem__(self, name, value): # reliably restored by inspect
        """ This operation is forbidden. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'tables.misc.enum\', \'__doc__\': "Enumerated type.\\n\\n    Each instance of this class represents an enumerated type. The\\n    values of the type must be declared\\n    *exhaustively* and named with\\n    *strings*, and they might be given explicit\\n    concrete values, though this is not compulsory. Once the type is\\n    defined, it can not be modified.\\n\\n    There are three ways of defining an enumerated type. Each one\\n    of them corresponds to the type of the only argument in the\\n    constructor of Enum:\\n\\n    - *Sequence of names*: each enumerated\\n      value is named using a string, and its order is determined by\\n      its position in the sequence; the concrete value is assigned\\n      automatically::\\n\\n          >>> boolEnum = Enum([\'True\', \'False\'])\\n\\n    - *Mapping of names*: each enumerated\\n      value is named by a string and given an explicit concrete value.\\n      All of the concrete values must be different, or a\\n      ValueError will be raised::\\n\\n          >>> priority = Enum({\'red\': 20, \'orange\': 10, \'green\': 0})\\n          >>> colors = Enum({\'red\': 1, \'blue\': 1})\\n          Traceback (most recent call last):\\n          ...\\n          ValueError: enumerated values contain duplicate concrete values: 1\\n\\n    - *Enumerated type*: in that case, a copy\\n      of the original enumerated type is created. Both enumerated\\n      types are considered equal::\\n\\n          >>> prio2 = Enum(priority)\\n          >>> priority == prio2\\n          True\\n\\n    Please note that names starting with _ are\\n    not allowed, since they are reserved for internal usage::\\n\\n        >>> prio2 = Enum([\'_xx\'])\\n        Traceback (most recent call last):\\n        ...\\n        ValueError: name of enumerated value can not start with ``_``: \'_xx\'\\n\\n    The concrete value of an enumerated value is obtained by\\n    getting its name as an attribute of the Enum\\n    instance (see __getattr__()) or as an item (see\\n    __getitem__()). This allows comparisons between\\n    enumerated values and assigning them to ordinary Python\\n    variables::\\n\\n        >>> redv = priority.red\\n        >>> redv == priority[\'red\']\\n        True\\n        >>> redv > priority.green\\n        True\\n        >>> priority.red == priority.orange\\n        False\\n\\n    The name of the enumerated value corresponding to a concrete\\n    value can also be obtained by using the\\n    __call__() method of the enumerated type. In this\\n    way you get the symbolic name to use it later with\\n    __getitem__()::\\n\\n        >>> priority(redv)\\n        \'red\'\\n        >>> priority.red == priority[priority(priority.red)]\\n        True\\n\\n    (If you ask, the __getitem__() method is\\n    not used for this purpose to avoid ambiguity in the case of using\\n    strings as concrete values.)\\n\\n    ", \'__init__\': <function Enum.__init__ at 0x00000115CF8680D0>, \'_check_and_set_pair\': <function Enum._check_and_set_pair at 0x00000115CF868268>, \'__getitem__\': <function Enum.__getitem__ at 0x00000115CF8682F0>, \'__setitem__\': <function Enum.__setitem__ at 0x00000115CF868378>, \'__delitem__\': <function Enum.__delitem__ at 0x00000115CF868400>, \'__getattr__\': <function Enum.__getattr__ at 0x00000115CF868488>, \'__setattr__\': <function Enum.__setattr__ at 0x00000115CF868510>, \'__delattr__\': <function Enum.__delattr__ at 0x00000115CF868598>, \'__contains__\': <function Enum.__contains__ at 0x00000115CF868620>, \'__call__\': <function Enum.__call__ at 0x00000115CF8686A8>, \'__len__\': <function Enum.__len__ at 0x00000115CF868730>, \'__iter__\': <function Enum.__iter__ at 0x00000115CF8687B8>, \'__eq__\': <function Enum.__eq__ at 0x00000115CF868840>, \'__ne__\': <function Enum.__ne__ at 0x00000115CF8688C8>, \'__repr__\': <function Enum.__repr__ at 0x00000115CF868950>, \'__dict__\': <attribute \'__dict__\' of \'Enum\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'Enum\' objects>, \'__hash__\': None})'
    __hash__ = None


class EnumAtom(__tables_atom.Atom):
    """
    Description of an atom of an enumerated type.
    
        Instances of this class describe the atom type used to store enumerated
        values. Those values belong to an enumerated type, defined by the first
        argument (enum) in the constructor of the atom, which accepts the same
        kinds of arguments as the Enum class (see :ref:`EnumClassDescr`).  The
        enumerated type is stored in the enum attribute of the atom.
    
        A default value must be specified as the second argument (dflt) in the
        constructor; it must be the *name* (a string) of one of the enumerated
        values in the enumerated type. When the atom is created, the corresponding
        concrete value is broadcast and stored in the dflt attribute (setting
        different default values for items in a multidimensional atom is not
        supported yet). If the name does not match any value in the enumerated
        type, a KeyError is raised.
    
        Another atom must be specified as the base argument in order to determine
        the base type used for storing the values of enumerated values in memory
        and disk. This *storage atom* is kept in the base attribute of the created
        atom. As a shorthand, you may specify a PyTables type instead of the
        storage atom, implying that this has a scalar shape.
    
        The storage atom should be able to represent each and every concrete value
        in the enumeration. If it is not, a TypeError is raised. The default value
        of the storage atom is ignored.
    
        The type attribute of enumerated atoms is always enum.
    
        Enumerated atoms also support comparisons with other objects::
    
            >>> enum = ['T0', 'T1', 'T2']
            >>> atom1 = EnumAtom(enum, 'T0', 'int8')  # same as ``atom2``
            >>> atom2 = EnumAtom(enum, 'T0', Int8Atom())  # same as ``atom1``
            >>> atom3 = EnumAtom(enum, 'T0', 'int16')
            >>> atom4 = Int8Atom()
            >>> atom1 == enum
            False
            >>> atom1 == atom2
            True
            >>> atom2 != atom1
            False
            >>> atom1 == atom3
            False
            >>> atom1 == atom4
            False
            >>> atom4 != atom1
            True
    
        Examples
        --------
    
        The next C enum construction::
    
            enum myEnum {
                T0,
                T1,
                T2
            };
    
        would correspond to the following PyTables
        declaration::
    
            >>> my_enum_atom = EnumAtom(['T0', 'T1', 'T2'], 'T0', 'int32')
    
        Please note the dflt argument with a value of 'T0'. Since the concrete
        value matching T0 is unknown right now (we have not used explicit concrete
        values), using the name is the only option left for defining a default
        value for the atom.
    
        The chosen representation of values for this enumerated atom uses unsigned
        32-bit integers, which surely wastes quite a lot of memory. Another size
        could be selected by using the base argument (this time with a full-blown
        storage atom)::
    
            >>> my_enum_atom = EnumAtom(['T0', 'T1', 'T2'], 'T0', UInt8Atom())
    
        You can also define multidimensional arrays for data elements::
    
            >>> my_enum_atom = EnumAtom(
            ...    ['T0', 'T1', 'T2'], 'T0', base='uint32', shape=(3,2))
    
        for 3x2 arrays of uint32.
    """
    def _checkbase(self, base): # reliably restored by inspect
        """ Check the `base` storage atom. """
        pass

    def _get_init_args(self): # reliably restored by inspect
        """ Get a dictionary of instance constructor arguments. """
        pass

    def _is_equal_to_atom(self, atom): # reliably restored by inspect
        """ Is this object equal to the given `atom`? """
        pass

    def _is_equal_to_enumatom(self, enumatom): # reliably restored by inspect
        """ Is this object equal to the given `enumatom`? """
        pass

    def __eq__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, enum, dflt, base, shape='()'): # reliably restored by inspect
        # no doc
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    itemsize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Size in bytes of a single item in the atom."""


    kind = 'enum'
    type = 'enum'
    __hash__ = None


class HDF5ExtError(RuntimeError):
    """
    A low level HDF5 operation failed.
    
        This exception is raised the low level PyTables components used for
        accessing HDF5 files.  It usually signals that something is not
        going well in the HDF5 library or even at the Input/Output level.
    
        Errors in the HDF5 C library may be accompanied by an extensive
        HDF5 back trace on standard error (see also
        :func:`tables.silence_hdf5_messages`).
    
        .. versionchanged:: 2.4
    
        Parameters
        ----------
        message
            error message
        h5bt
            This parameter (keyword only) controls the HDF5 back trace
            handling. Any keyword arguments other than h5bt is ignored.
    
            * if set to False the HDF5 back trace is ignored and the
              :attr:`HDF5ExtError.h5backtrace` attribute is set to None
            * if set to True the back trace is retrieved from the HDF5
              library and stored in the :attr:`HDF5ExtError.h5backtrace`
              attribute as a list of tuples
            * if set to "VERBOSE" (default) the HDF5 back trace is
              stored in the :attr:`HDF5ExtError.h5backtrace` attribute
              and also included in the string representation of the
              exception
            * if not set (or set to None) the default policy is used
              (see :attr:`HDF5ExtError.DEFAULT_H5_BACKTRACE_POLICY`)
    """
    def format_h5_backtrace(self, backtrace=None): # reliably restored by inspect
        """
        Convert the HDF5 trace back represented as a list of tuples.
                (see :attr:`HDF5ExtError.h5backtrace`) into a string.
        
                .. versionadded:: 2.4
        """
        pass

    @classmethod
    def set_policy_from_env(cls, *args, **kwargs): # real signature unknown
        pass

    def _dump_h5_backtrace(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def __str__(self): # reliably restored by inspect
        """
        Returns a sting representation of the exception.
        
                The actual result depends on policy set in the initializer
                :meth:`HDF5ExtError.__init__`.
        
                .. versionadded:: 2.4
        """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    DEFAULT_H5_BACKTRACE_POLICY = 'VERBOSE'


class ReferenceAtom(__tables_atom.Atom):
    """
    Defines an atom of type object to read references.
        This atom is read-only.
    """
    def __init__(self, shape='()'): # reliably restored by inspect
        # no doc
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    itemsize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Size in bytes of a single item in the atom."""


    kind = 'reference'
    type = 'object'
    _deftype = 'NoneType'
    _defvalue = None


# variables with complex values

blosc_version = (
    '1.16.3',
    '$Date:: 2019-03-08 #$',
)

bzip2_version = (
    '1.0.8',
    '13-Jul-2019',
)

HDF5ClassToString = {
    -1: 'H5T_NO_CLASS',
    0: 'H5T_INTEGER',
    1: 'H5T_FLOAT',
    2: 'H5T_TIME',
    3: 'H5T_STRING',
    4: 'H5T_BITFIELD',
    5: 'H5T_OPAQUE',
    6: 'H5T_COMPOUND',
    7: 'H5T_REFERENCE',
    8: 'H5T_ENUM',
    9: 'H5T_VLEN',
    10: 'H5T_ARRAY',
}

hdf5_class_to_string = {
    -1: 'H5T_NO_CLASS',
    0: 'H5T_INTEGER',
    1: 'H5T_FLOAT',
    2: 'H5T_TIME',
    3: 'H5T_STRING',
    4: 'H5T_BITFIELD',
    5: 'H5T_OPAQUE',
    6: 'H5T_COMPOUND',
    7: 'H5T_REFERENCE',
    8: 'H5T_ENUM',
    9: 'H5T_VLEN',
    10: 'H5T_ARRAY',
}

lzo_version = (
    '2.10',
    'Mar 01 2017',
)

NPExtPrefixesToPTKinds = {
    'S': 'string',
    'b': 'bool',
    'c': 'complex',
    'e': 'enum',
    'f': 'float',
    'i': 'int',
    't': 'time',
    'u': 'uint',
}

npext_prefixes_to_ptkinds = {
    'S': 'string',
    'b': 'bool',
    'c': 'complex',
    'e': 'enum',
    'f': 'float',
    'i': 'int',
    't': 'time',
    'u': 'uint',
}

PTSpecialKinds = [
    'complex',
    'string',
    'enum',
    'bool',
]

PTTypeToHDF5 = {
    'float128': 216172782113783852,
    'float32': 216172782113783862,
    'float64': 216172782113783864,
    'float96': 216172782113783852,
    'int16': 216172782113783870,
    'int32': 216172782113783872,
    'int64': 216172782113783874,
    'int8': 216172782113783868,
    'time32': 216172782113783892,
    'time64': 216172782113783894,
    'uint16': 216172782113783878,
    'uint32': 216172782113783880,
    'uint64': 216172782113783882,
    'uint8': 216172782113783876,
}

pttype_to_hdf5 = {
    'float128': 216172782113783852,
    'float32': 216172782113783862,
    'float64': 216172782113783864,
    'float96': 216172782113783852,
    'int16': 216172782113783870,
    'int32': 216172782113783872,
    'int64': 216172782113783874,
    'int8': 216172782113783868,
    'time32': 216172782113783892,
    'time64': 216172782113783894,
    'uint16': 216172782113783878,
    'uint32': 216172782113783880,
    'uint64': 216172782113783882,
    'uint8': 216172782113783876,
}

pt_special_kinds = [
    'complex',
    'string',
    'enum',
    'bool',
]

typeDict = numpy.sctypeDict

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000115BF67D438>'

__pyx_capi__ = {
    'cstr_to_pystr': None, # (!) real value is '<capsule object "PyObject *(char const *)" at 0x00000115BF649B10>'
    'get_native_type': None, # (!) real value is '<capsule object "hid_t (hid_t)" at 0x00000115BF649900>'
    'load_reference': None, # (!) real value is '<capsule object "int (hid_t, hobj_ref_t *, size_t, PyArrayObject *)" at 0x00000115BF649AE0>'
    'malloc_dims': None, # (!) real value is '<capsule object "hsize_t *(PyObject *)" at 0x00000115BF649B40>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='tables.utilsextension', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000115BF67D438>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\tables\\\\utilsextension.cp37-win_amd64.pyd')"

__test__ = {}

