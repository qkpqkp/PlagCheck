# encoding: utf-8
# module h5py.h5t
# from C:\Users\Doly\Anaconda3\lib\site-packages\h5py\h5t.cp37-win_amd64.pyd
# by generator 1.147
"""
HDF5 "H5T" data-type API

    This module contains the datatype identifier class TypeID, and its
    subclasses which represent things like integer/float/compound identifiers.
    The majority of the H5T API is presented as methods on these identifiers.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import sys as sys # <module 'sys' (built-in)>
import operator as operator # C:\Users\Doly\Anaconda3\lib\operator.py
import numpy as np # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py
import platform as platform # C:\Users\Doly\Anaconda3\lib\platform.py
from h5py._objects import (array_create, check_dtype, convert, create, decode, 
    enum_create, find, open, special_dtype, vlen_create, with_phil)

from _warnings import warn

import collections.abc as __collections_abc
import h5py.h5py_warnings as __h5py_h5py_warnings
import h5py._objects as __h5py__objects
import numpy as __numpy


# Variables with simple values

ARRAY = 10

BITFIELD = 4

BKG_NO = 0
BKG_TEMP = 1
BKG_YES = 2

COMPOUND = 6

CSET_ASCII = 0
CSET_UTF8 = 1

DIR_ASCEND = 1
DIR_DEFAULT = 0
DIR_DESCEND = 2

ENUM = 8

FLOAT = 1

INTEGER = 0

MACHINE = 'AMD64'

NORM_IMPLIED = 0
NORM_MSBSET = 1
NORM_NONE = 2

NO_CLASS = -1

OPAQUE = 5

ORDER_BE = 1
ORDER_LE = 0
ORDER_NATIVE = 0
ORDER_NONE = 4
ORDER_VAX = 2

PAD_BACKGROUND = 2
PAD_ONE = 1
PAD_ZERO = 0

PY3 = True

REFERENCE = 7

SGN_2 = 1
SGN_NONE = 0

STRING = 3

STR_NULLPAD = 1
STR_NULLTERM = 0
STR_SPACEPAD = 2

TIME = 2

VARIABLE = 18446744073709551615

VLEN = 9

# functions

def get_config(*args, **kwargs): # real signature unknown
    """
    () => H5PYConfig
    
        Get a reference to the global library configuration object.
    """
    pass

def py_create(*args, **kwargs): # real signature unknown
    """
    (OBJECT dtype_in, BOOL logical=False) => TypeID
    
        Given a Numpy dtype object, generate a byte-for-byte memory-compatible
        HDF5 datatype object.  The result is guaranteed to be transient and
        unlocked.
    
        Argument dtype_in may be a dtype object, or anything which can be
        converted to a dtype, including strings like '<i4'.
    
        logical
            If this flag is set, instead of returning a byte-for-byte identical
            representation of the type, the function returns the closest logically
            appropriate HDF5 type.  For example, in the case of a "hinted" dtype
            of kind "O" representing a string, it would return an HDF5 variable-
            length string type.
    """
    pass

def py_get_enum(*args, **kwargs): # real signature unknown
    """
    (DTYPE dt_in) => DICT
    
        Deprecated; use check_dtype() instead.
    """
    pass

def py_get_vlen(*args, **kwargs): # real signature unknown
    """
    (OBJECT dt_in) => TYPE
    
        Deprecated; use check_dtype() instead.
    """
    pass

def py_new_enum(*args, **kwargs): # real signature unknown
    """
    (DTYPE dt_in, DICT enum_vals) => DTYPE
    
        Deprecated; use special_dtype() instead.
    """
    pass

def py_new_vlen(*args, **kwargs): # real signature unknown
    """
    (OBJECT kind) => DTYPE
    
        Deprecated; use special_dtype() instead.
    """
    pass

def typewrap(*args, **kwargs): # real signature unknown
    pass

def _get_available_ftypes(*args, **kwargs): # real signature unknown
    pass

def _get_float_dtype_to_hdf5(*args, **kwargs): # real signature unknown
    pass

# classes

class defaultdict(dict):
    """
    defaultdict(default_factory[, ...]) --> dict with default factory
    
    The default factory is called without arguments to produce
    a new value when a key is not present, in __getitem__ only.
    A defaultdict compares equal to a dict with the same items.
    All remaining arguments are treated the same as if they were
    passed to the dict constructor, including keyword arguments.
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ D.copy() -> a shallow copy of D. """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        """ D.copy() -> a shallow copy of D. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, default_factory, *some): # real signature unknown; restored from __doc__
        pass

    def __missing__(self, key): # real signature unknown; restored from __doc__
        """
        __missing__(key) # Called by __getitem__ for missing key; pseudo-code:
          if self.default_factory is None: raise KeyError((key,))
          self[key] = value = self.default_factory()
          return value
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Return state information for pickling. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    default_factory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Factory for default value called by __missing__()."""



class ftype(bytes, __numpy.character):
    # no doc
    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
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


class H5pyDeprecationWarning(__h5py_h5py_warnings.H5pyWarning):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Mapping(__collections_abc.Collection):
    # no doc
    def get(self, key, default=None): # reliably restored by inspect
        """ D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None. """
        pass

    def items(self): # reliably restored by inspect
        """ D.items() -> a set-like object providing a view on D's items """
        pass

    def keys(self): # reliably restored by inspect
        """ D.keys() -> a set-like object providing a view on D's keys """
        pass

    def values(self): # reliably restored by inspect
        """ D.values() -> an object providing a view on D's values """
        pass

    def __contains__(self, key): # reliably restored by inspect
        # no doc
        pass

    def __eq__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __getitem__(self, key): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _abc_impl = None # (!) real value is '<_abc_data object at 0x000001A6325C4540>'
    __abstractmethods__ = frozenset({'__getitem__', '__iter__', '__len__'})
    __hash__ = None
    __reversed__ = None
    __slots__ = ()


class TypeID(__h5py__objects.ObjectID):
    """
    Base class for type identifiers (implements common operations)
    
            * Hashable: If committed; in HDF5 1.8.X, also if locked
            * Equality: Logical H5T comparison
    """
    def commit(self, *args, **kwargs): # real signature unknown
        """
        (ObjectID group, STRING name, PropID lcpl=None)
        
                Commit this (transient) datatype to a named datatype in a file.
                If present, lcpl may be a link creation property list.
        """
        pass

    def committed(self, *args, **kwargs): # real signature unknown
        """
        () => BOOL is_comitted
        
                Determine if a given type object is named (T) or transient (F).
        """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        """
        () => TypeID
        
                Create a copy of this type object.
        """
        pass

    def detect_class(self, *args, **kwargs): # real signature unknown
        """
        (INT classtype) => BOOL class_is_present
        
                Determine if a member of the given class exists in a compound
                datatype.  The search is recursive.
        """
        pass

    def encode(self, *args, **kwargs): # real signature unknown
        """
        () => STRING
        
                Serialize an HDF5 type.  Bear in mind you can also use the
                native Python pickle/unpickle machinery to do this.  The
                returned string may contain binary values, including NULLs.
        """
        pass

    def equal(self, *args, **kwargs): # real signature unknown
        """
        (TypeID typeid) => BOOL
        
                Logical comparison between datatypes.  Also called by
                Python's "==" operator.
        """
        pass

    def get_class(self, *args, **kwargs): # real signature unknown
        """
        () => INT classcode
        
                Determine the datatype's class code.
        """
        pass

    def get_size(self, *args, **kwargs): # real signature unknown
        """
        () => INT size
        
                    Determine the total size of a datatype, in bytes.
        """
        pass

    def get_super(self, *args, **kwargs): # real signature unknown
        """
        () => TypeID
        
                Determine the parent type of an array, enumeration or vlen datatype.
        """
        pass

    def lock(self, *args, **kwargs): # real signature unknown
        """
        ()
        
                Lock this datatype, which makes it immutable and indestructible.
                Once locked, it can't be unlocked.
        """
        pass

    def set_size(self, *args, **kwargs): # real signature unknown
        """
        (UINT size)
        
                Set the total size of the datatype, in bytes.
        """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
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

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
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

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    dtype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ A Numpy-style dtype object representing this object.
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001A63469D180>'


class TypeArrayID(TypeID):
    """ Represents an array datatype """
    def get_array_dims(self, *args, **kwargs): # real signature unknown
        """
        () => TUPLE dimensions
        
                Get the dimensions of the given array datatype as
                a tuple of integers.
        """
        pass

    def get_array_ndims(self, *args, **kwargs): # real signature unknown
        """
        () => INT rank
        
                Get the rank of the given array datatype.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001A63469D1B0>'


class TypeAtomicID(TypeID):
    """ Base class for atomic datatypes (float or integer) """
    def get_offset(self, *args, **kwargs): # real signature unknown
        """
        () => INT offset
        
                Get the offset of the first significant bit.
        """
        pass

    def get_order(self, *args, **kwargs): # real signature unknown
        """
        () => INT order
        
                Obtain the byte order of the datatype; one of:
        
                - ORDER_LE
                - ORDER_BE
        """
        pass

    def get_pad(self, *args, **kwargs): # real signature unknown
        """
        () => (INT lsb_pad_code, INT msb_pad_code)
        
                Determine the padding type.  Possible values are:
        
                - PAD_ZERO
                - PAD_ONE
                - PAD_BACKGROUND
        """
        pass

    def get_precision(self, *args, **kwargs): # real signature unknown
        """
        () => UINT precision
        
                Get the number of significant bits (excludes padding).
        """
        pass

    def set_offset(self, *args, **kwargs): # real signature unknown
        """
        (UINT offset)
        
                Set the offset of the first significant bit.
        """
        pass

    def set_order(self, *args, **kwargs): # real signature unknown
        """
        (INT order)
        
                Set the byte order of the datatype; one of:
        
                - ORDER_LE
                - ORDER_BE
        """
        pass

    def set_pad(self, *args, **kwargs): # real signature unknown
        """
        (INT lsb_pad_code, INT msb_pad_code)
        
                Set the padding type.  Possible values are:
        
                - PAD_ZERO
                - PAD_ONE
                - PAD_BACKGROUND
        """
        pass

    def set_precision(self, *args, **kwargs): # real signature unknown
        """
        (UINT precision)
        
                Set the number of significant bits (excludes padding).
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001A63469D300>'


class TypeBitfieldID(TypeID):
    """ HDF5 bitfield type """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001A63469D2A0>'


class TypeCompositeID(TypeID):
    """ Base class for enumerated and compound types. """
    def get_member_index(self, *args, **kwargs): # real signature unknown
        """
        (STRING name) => INT index
        
                Determine the index of a member of a compound or enumerated datatype
                identified by a string name.
        """
        pass

    def get_member_name(self, *args, **kwargs): # real signature unknown
        """
        (INT member) => STRING name
        
                Determine the name of a member of a compound or enumerated type,
                identified by its index (0 <= member < nmembers).
        """
        pass

    def get_nmembers(self, *args, **kwargs): # real signature unknown
        """
        () => INT number_of_members
        
                Determine the number of members in a compound or enumerated type.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001A63469D390>'


class TypeCompoundID(TypeCompositeID):
    """ Represents a compound datatype """
    def get_member_class(self, *args, **kwargs): # real signature unknown
        """
        (INT member) => INT class
        
                Determine the datatype class of the member of a compound type,
                identified by its index (0 <= member < nmembers).
        """
        pass

    def get_member_offset(self, *args, **kwargs): # real signature unknown
        """
        (INT member) => INT offset
        
                Determine the offset, in bytes, of the beginning of the specified
                member of a compound datatype.
        """
        pass

    def get_member_type(self, *args, **kwargs): # real signature unknown
        """
        (INT member) => TypeID
        
                Create a copy of a member of a compound datatype, identified by its
                index.
        """
        pass

    def insert(self, *args, **kwargs): # real signature unknown
        """
        (STRING name, UINT offset, TypeID field)
        
                Add a named member datatype to a compound datatype.  The parameter
                offset indicates the offset from the start of the compound datatype,
                in bytes.
        """
        pass

    def pack(self, *args, **kwargs): # real signature unknown
        """
        ()
        
                Recursively removes padding (introduced on account of e.g. compiler
                alignment rules) from a compound datatype.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001A63469D3F0>'


class TypeEnumID(TypeCompositeID):
    """ Represents an enumerated type """
    def enum_insert(self, *args, **kwargs): # real signature unknown
        """
        (STRING name, INT/LONG value)
        
                Define a new member of an enumerated type.  The value will be
                automatically converted to the base type defined for this enum.  If
                the conversion results in overflow, the value will be silently
                clipped.
        """
        pass

    def enum_nameof(self, *args, **kwargs): # real signature unknown
        """
        (LONG value) => STRING name
        
                Determine the name associated with the given value.  Due to a
                limitation of the HDF5 library, this can only retrieve names up to
                1023 characters in length.
        """
        pass

    def enum_valueof(self, *args, **kwargs): # real signature unknown
        """
        (STRING name) => LONG value
        
                Get the value associated with an enum name.
        """
        pass

    def get_member_value(self, *args, **kwargs): # real signature unknown
        """
        (UINT index) => LONG value
        
                Determine the value for the member at the given zero-based index.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001A63469D3C0>'


class TypeFloatID(TypeAtomicID):
    """ Floating-point atomic datatypes """
    def get_ebias(self, *args, **kwargs): # real signature unknown
        """
        () => UINT ebias
        
                Get the exponent bias.
        """
        pass

    def get_fields(self, *args, **kwargs): # real signature unknown
        """
        () => TUPLE field_info
        
                Get information about floating-point bit fields.  See the HDF5
                docs for a full description.  Tuple has the following members:
        
                0. UINT spos
                1. UINT epos
                2. UINT esize
                3. UINT mpos
                4. UINT msize
        """
        pass

    def get_inpad(self, *args, **kwargs): # real signature unknown
        """
        () => INT pad_code
        
                Determine the internal padding strategy.  Legal values are:
        
                - PAD_ZERO
                - PAD_ONE
                - PAD_BACKGROUND
        """
        pass

    def get_norm(self, *args, **kwargs): # real signature unknown
        """
        () => INT normalization_code
        
                Get the normalization strategy.  Legal values are:
        
                - NORM_IMPLIED
                - NORM_MSBSET
                - NORM_NONE
        """
        pass

    def set_ebias(self, *args, **kwargs): # real signature unknown
        """
        (UINT ebias)
        
                Set the exponent bias.
        """
        pass

    def set_fields(self, *args, **kwargs): # real signature unknown
        """
        (UINT spos, UINT epos, UINT esize, UINT mpos, UINT msize)
        
                Set floating-point bit fields.  Refer to the HDF5 docs for
                argument definitions.
        """
        pass

    def set_inpad(self, *args, **kwargs): # real signature unknown
        """
        (INT pad_code)
        
                Set the internal padding strategy.  Legal values are:
        
                - PAD_ZERO
                - PAD_ONE
                - PAD_BACKGROUND
        """
        pass

    def set_norm(self, *args, **kwargs): # real signature unknown
        """
        (INT normalization_code)
        
                Set the normalization strategy.  Legal values are:
        
                - NORM_IMPLIED
                - NORM_MSBSET
                - NORM_NONE
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001A63469D360>'


class TypeIntegerID(TypeAtomicID):
    """ Integer atomic datatypes """
    def get_sign(self, *args, **kwargs): # real signature unknown
        """
        () => INT sign
        
                Get the "signedness" of the datatype; one of:
        
                SGN_NONE
                    Unsigned
        
                SGN_2
                    Signed 2's complement
        """
        pass

    def set_sign(self, *args, **kwargs): # real signature unknown
        """
        (INT sign)
        
                Set the "signedness" of the datatype; one of:
        
                SGN_NONE
                    Unsigned
        
                SGN_2
                    Signed 2's complement
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001A63469D330>'


class TypeOpaqueID(TypeID):
    """ Represents an opaque type """
    def get_tag(self, *args, **kwargs): # real signature unknown
        """
        () => STRING tag
        
                Get the tag associated with an opaque datatype.
        """
        pass

    def set_tag(self, *args, **kwargs): # real signature unknown
        """
        (STRING tag)
        
                Set a string describing the contents of an opaque datatype.
                Limited to 256 characters.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001A63469D1E0>'


class TypeReferenceID(TypeID):
    """ HDF5 object or region reference """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001A63469D2D0>'


class TypeStringID(TypeID):
    """ String datatypes, both fixed and vlen. """
    def get_cset(self, *args, **kwargs): # real signature unknown
        """
        () => INT character_set
        
                Retrieve the character set used for a string.
        """
        pass

    def get_strpad(self, *args, **kwargs): # real signature unknown
        """
        () => INT padding_type
        
                Get the padding type.  Legal values are:
        
                STR_NULLTERM
                    NULL termination only (C style)
        
                STR_NULLPAD
                    Pad buffer with NULLs
        
                STR_SPACEPAD
                    Pad buffer with spaces (FORTRAN style)
        """
        pass

    def is_variable_str(self, *args, **kwargs): # real signature unknown
        """
        () => BOOL is_variable
        
                Determine if the given string datatype is a variable-length string.
        """
        pass

    def set_cset(self, *args, **kwargs): # real signature unknown
        """
        (INT character_set)
        
                Set the character set used for a string.
        """
        pass

    def set_strpad(self, *args, **kwargs): # real signature unknown
        """
        (INT pad)
        
                Set the padding type.  Legal values are:
        
                STR_NULLTERM
                    NULL termination only (C style)
        
                STR_NULLPAD
                    Pad buffer with NULLs
        
                STR_SPACEPAD
                    Pad buffer with spaces (FORTRAN style)
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001A63469D210>'


class TypeTimeID(TypeID):
    """ Unix-style time_t (deprecated) """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001A63469D270>'


class TypeVlenID(TypeID):
    """ Non-string vlen datatypes. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001A63469D240>'


class _DeprecatedMapping(__collections_abc.Mapping):
    """ Mapping class which warns when members are accessed """
    def __getitem__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _abc_impl = None # (!) real value is '<_abc_data object at 0x000001A642F2C360>'
    __abstractmethods__ = frozenset()
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'h5py.h5t', '__doc__': '\\n    Mapping class which warns when members are accessed\\n    ', '__init__': <cyfunction _DeprecatedMapping.__init__ at 0x000001A642EFC8E8>, '__len__': <cyfunction _DeprecatedMapping.__len__ at 0x000001A642EFC9A0>, '__iter__': <cyfunction _DeprecatedMapping.__iter__ at 0x000001A642EFCA58>, '__getitem__': <cyfunction _DeprecatedMapping.__getitem__ at 0x000001A642EFCB10>, '__dict__': <attribute '__dict__' of '_DeprecatedMapping' objects>, '__weakref__': <attribute '__weakref__' of '_DeprecatedMapping' objects>, '__abstractmethods__': frozenset(), '_abc_impl': <_abc_data object at 0x000001A642F2C360>})"


# variables with complex values

available_ftypes = None # (!) real value is '<h5py.h5t._DeprecatedMapping object at 0x000001A642F30D68>'

cfg = None # (!) real value is '<h5py.h5.H5PYConfig object at 0x000001A642F00A08>'

C_S1 = None # (!) real value is '<h5py.h5t.TypeStringID object at 0x000001A642F400A0>'

FORTRAN_S1 = None # (!) real value is '<h5py.h5t.TypeStringID object at 0x000001A642F400F8>'

IEEE_F128BE = None # (!) real value is '<h5py.h5t.TypeFloatID object at 0x000001A642F40200>'

IEEE_F128LE = None # (!) real value is '<h5py.h5t.TypeFloatID object at 0x000001A642F40258>'

IEEE_F16BE = None # (!) real value is '<h5py.h5t.TypeFloatID object at 0x000001A642F40150>'

IEEE_F16LE = None # (!) real value is '<h5py.h5t.TypeFloatID object at 0x000001A642F401A8>'

IEEE_F32BE = None # (!) real value is '<h5py.h5t.TypeFloatID object at 0x000001A642F32410>'

IEEE_F32LE = None # (!) real value is '<h5py.h5t.TypeFloatID object at 0x000001A642F323B8>'

IEEE_F64BE = None # (!) real value is '<h5py.h5t.TypeFloatID object at 0x000001A642F324C0>'

IEEE_F64LE = None # (!) real value is '<h5py.h5t.TypeFloatID object at 0x000001A642F32468>'

LDOUBLE_BE = None # (!) real value is '<h5py.h5t.TypeFloatID object at 0x000001A642F40308>'

LDOUBLE_LE = None # (!) real value is '<h5py.h5t.TypeFloatID object at 0x000001A642F402B0>'

NATIVE_DOUBLE = None # (!) real value is '<h5py.h5t.TypeFloatID object at 0x000001A642F32DB0>'

NATIVE_FLOAT = None # (!) real value is '<h5py.h5t.TypeFloatID object at 0x000001A642F32D58>'

NATIVE_INT16 = None # (!) real value is '<h5py.h5t.TypeIntegerID object at 0x000001A642F32B48>'

NATIVE_INT32 = None # (!) real value is '<h5py.h5t.TypeIntegerID object at 0x000001A642F32BF8>'

NATIVE_INT64 = None # (!) real value is '<h5py.h5t.TypeIntegerID object at 0x000001A642F32CA8>'

NATIVE_INT8 = None # (!) real value is '<h5py.h5t.TypeIntegerID object at 0x000001A642F32A98>'

NATIVE_LDOUBLE = None # (!) real value is '<h5py.h5t.TypeFloatID object at 0x000001A642F32E08>'

NATIVE_UINT16 = None # (!) real value is '<h5py.h5t.TypeIntegerID object at 0x000001A642F32BA0>'

NATIVE_UINT32 = None # (!) real value is '<h5py.h5t.TypeIntegerID object at 0x000001A642F32C50>'

NATIVE_UINT64 = None # (!) real value is '<h5py.h5t.TypeIntegerID object at 0x000001A642F32D00>'

NATIVE_UINT8 = None # (!) real value is '<h5py.h5t.TypeIntegerID object at 0x000001A642F32AF0>'

phil = None # (!) real value is '<h5py._objects.FastRLock object at 0x000001A6346712B0>'

PYTHON_OBJECT = None # (!) real value is '<h5py.h5t.TypeOpaqueID object at 0x000001A642F40360>'

STD_I16BE = None # (!) real value is '<h5py.h5t.TypeIntegerID object at 0x000001A642F326D0>'

STD_I16LE = None # (!) real value is '<h5py.h5t.TypeIntegerID object at 0x000001A642F32570>'

STD_I32BE = None # (!) real value is '<h5py.h5t.TypeIntegerID object at 0x000001A642F32728>'

STD_I32LE = None # (!) real value is '<h5py.h5t.TypeIntegerID object at 0x000001A642F325C8>'

STD_I64BE = None # (!) real value is '<h5py.h5t.TypeIntegerID object at 0x000001A642F32780>'

STD_I64LE = None # (!) real value is '<h5py.h5t.TypeIntegerID object at 0x000001A642F32620>'

STD_I8BE = None # (!) real value is '<h5py.h5t.TypeIntegerID object at 0x000001A642F32678>'

STD_I8LE = None # (!) real value is '<h5py.h5t.TypeIntegerID object at 0x000001A642F32518>'

STD_REF_DSETREG = None # (!) real value is '<h5py.h5t.TypeReferenceID object at 0x000001A642F40048>'

STD_REF_OBJ = None # (!) real value is '<h5py.h5t.TypeReferenceID object at 0x000001A642F32FC0>'

STD_U16BE = None # (!) real value is '<h5py.h5t.TypeIntegerID object at 0x000001A642F32990>'

STD_U16LE = None # (!) real value is '<h5py.h5t.TypeIntegerID object at 0x000001A642F32830>'

STD_U32BE = None # (!) real value is '<h5py.h5t.TypeIntegerID object at 0x000001A642F329E8>'

STD_U32LE = None # (!) real value is '<h5py.h5t.TypeIntegerID object at 0x000001A642F32888>'

STD_U64BE = None # (!) real value is '<h5py.h5t.TypeIntegerID object at 0x000001A642F32A40>'

STD_U64LE = None # (!) real value is '<h5py.h5t.TypeIntegerID object at 0x000001A642F328E0>'

STD_U8BE = None # (!) real value is '<h5py.h5t.TypeIntegerID object at 0x000001A642F32938>'

STD_U8LE = None # (!) real value is '<h5py.h5t.TypeIntegerID object at 0x000001A642F327D8>'

UNIX_D32BE = None # (!) real value is '<h5py.h5t.TypeTimeID object at 0x000001A642F32F10>'

UNIX_D32LE = None # (!) real value is '<h5py.h5t.TypeTimeID object at 0x000001A642F32E60>'

UNIX_D64BE = None # (!) real value is '<h5py.h5t.TypeTimeID object at 0x000001A642F32F68>'

UNIX_D64LE = None # (!) real value is '<h5py.h5t.TypeTimeID object at 0x000001A642F32EB8>'

_available_ftypes = (
    (
        np.half,
        finfo(resolution=0.001, min=-6.55040e+04, max=6.55040e+04, dtype=float16),
        2,
    ),
    (
        np.float32,
        finfo(resolution=1e-06, min=-3.4028235e+38, max=3.4028235e+38, dtype=float32),
        4,
    ),
    (
        np.double,
        finfo(resolution=1e-15, min=-1.7976931348623157e+308, max=1.7976931348623157e+308, dtype=float64),
        8,
    ),
    (
        np.longdouble,
        '<value is a self-reference, replaced by this string>',
        8,
    ),
)

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001A63468AD68>'

__pyx_capi__ = {
    'H5PY_OBJ': None, # (!) real value is '<capsule object "hid_t" at 0x000001A63469D0F0>'
    'py_create': None, # (!) real value is '<capsule object "struct __pyx_obj_4h5py_3h5t_TypeID *(PyObject *, int __pyx_skip_dispatch, struct __pyx_opt_args_4h5py_3h5t_py_create *__pyx_optional_args)" at 0x000001A63469D150>'
    'typewrap': None, # (!) real value is '<capsule object "struct __pyx_obj_4h5py_3h5t_TypeID *(hid_t, int __pyx_skip_dispatch)" at 0x000001A63469D120>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='h5py.h5t', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001A63468AD68>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\h5py\\\\h5t.cp37-win_amd64.pyd')"

__test__ = {}

