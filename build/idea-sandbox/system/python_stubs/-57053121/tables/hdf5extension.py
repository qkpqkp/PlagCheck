# encoding: utf-8
# module tables.hdf5extension
# from C:\Users\Doly\Anaconda3\lib\site-packages\tables\hdf5extension.cp37-win_amd64.pyd
# by generator 1.147
"""
Cython interface between several PyTables classes and HDF5 library.

Classes (type extensions):

    File
    AttributeSet
    Node
    Leaf
    Group
    Array
    VLArray
    UnImplemented

Functions:

Misc variables:
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import os as os # C:\Users\Doly\Anaconda3\lib\os.py
import warnings as warnings # C:\Users\Doly\Anaconda3\lib\warnings.py
import pickle as pickle # C:\Users\Doly\Anaconda3\lib\pickle.py
import numpy as numpy # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py
from tables.utilsextension import (atom_from_hdf5_type, atom_to_hdf5_type, 
    create_nested_type, encode_filename, hdf5_to_np_ext_type, 
    set_blosc_max_threads)

import numpy as __numpy


# Variables with simple values

HAVE_DIRECT_DRIVER = False

HAVE_WINDOWS_DRIVER = True

platform_byteorder = 0

# functions

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

def correct_byteorder(ptype, byteorder): # reliably restored by inspect
    """ Fix the byteorder depending on the PyTables types. """
    pass

def descr_from_dtype(dtype_, ptparams=None): # reliably restored by inspect
    """ Get a description instance and byteorder from a (nested) NumPy dtype. """
    pass

def namedtuple(typename, field_names, *, rename=False, defaults=None, module=None): # reliably restored by inspect
    """
    Returns a new subclass of tuple with named fields.
    
        >>> Point = namedtuple('Point', ['x', 'y'])
        >>> Point.__doc__                   # docstring for the new class
        'Point(x, y)'
        >>> p = Point(11, y=22)             # instantiate with positional args or keywords
        >>> p[0] + p[1]                     # indexable like a plain tuple
        33
        >>> x, y = p                        # unpack like a regular tuple
        >>> x, y
        (11, 22)
        >>> p.x + p.y                       # fields also accessible by name
        33
        >>> d = p._asdict()                 # convert to a dictionary
        >>> d['x']
        11
        >>> Point(**d)                      # convert from a dictionary
        Point(x=11, y=22)
        >>> p._replace(x=100)               # _replace() is like str.replace() but targets named fields
        Point(x=100, y=22)
    """
    pass

def __pyx_unpickle_AttributeSet(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_File(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Group(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Node(*args, **kwargs): # real signature unknown
    pass

# classes

class Node(object):
    # no doc
    def _get_obj_info(self, *args, **kwargs): # real signature unknown
        pass

    def _get_obj_timestamps(self, *args, **kwargs): # real signature unknown
        pass

    def _g_delete(self, *args, **kwargs): # real signature unknown
        pass

    def _g_new(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass


class Leaf(Node):
    # no doc
    def _get_obj_track_times(self, *args, **kwargs): # real signature unknown
        """
        Get track_times boolean for dataset
        
            Uses H5Pget_obj_track_times to determine if the dataset was
            created with the track_times property.  If the leaf is not a
            dataset, this will fail with HDF5ExtError.
        
            The track times dataset creation property does not seem to survive
            closing and reopening as of HDF5 1.8.17.  Currently, it may be
            more accurate to test whether the ctime for the dataset is 0:
            track_times = (leaf._get_obj_timestamps().ctime == 0)
        """
        pass

    def _get_storage_size(self, *args, **kwargs): # real signature unknown
        pass

    def _g_close(self, *args, **kwargs): # real signature unknown
        pass

    def _g_flush(self, *args, **kwargs): # real signature unknown
        pass

    def _g_new(self, *args, **kwargs): # real signature unknown
        pass

    def _g_truncate(self, *args, **kwargs): # real signature unknown
        """ Truncate a Leaf to `size` nrows. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001D7BC22FF00>'


class Array(Leaf):
    # no doc
    def perform_selection(self, *args, **kwargs): # real signature unknown
        """
        Performs a selection using start/count/step in the given axis.
        
            All other axes have their full range selected.  The selection is
            added to the current `space_id` selection using the given mode.
        
            Note: This is a backport from the h5py project.
        """
        pass

    def _append(self, *args, **kwargs): # real signature unknown
        pass

    def _create_array(self, *args, **kwargs): # real signature unknown
        pass

    def _create_carray(self, *args, **kwargs): # real signature unknown
        pass

    def _g_read_coords(self, *args, **kwargs): # real signature unknown
        """ Read coordinates in an already created NumPy array. """
        pass

    def _g_read_selection(self, *args, **kwargs): # real signature unknown
        """ Read a selection in an already created NumPy array. """
        pass

    def _g_read_slice(self, *args, **kwargs): # real signature unknown
        pass

    def _g_write_coords(self, *args, **kwargs): # real signature unknown
        """ Write a selection in an already created NumPy array. """
        pass

    def _g_write_selection(self, *args, **kwargs): # real signature unknown
        """ Write a selection in an already created NumPy array. """
        pass

    def _g_write_slice(self, *args, **kwargs): # real signature unknown
        """ Write a slice in an already created NumPy array. """
        pass

    def _open_array(self, *args, **kwargs): # real signature unknown
        pass

    def _read_array(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001D7BC2391B0>'


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


    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'tables.atom\', \'__doc__\': "Defines the type of atomic cells stored in a dataset.\\n\\n    The meaning of *atomic* is that individual elements of a cell can\\n    not be extracted directly by indexing (i.e.  __getitem__()) the\\n    dataset; e.g. if a dataset has shape (2, 2) and its atoms have\\n    shape (3,), to get the third element of the cell at (1, 0) one\\n    should use dataset[1,0][2] instead of dataset[1,0,2].\\n\\n    The Atom class is meant to declare the different properties of the\\n    *base element* (also known as *atom*) of CArray, EArray and\\n    VLArray datasets, although they are also used to describe the base\\n    elements of Array datasets. Atoms have the property that their\\n    length is always the same.  However, you can grow datasets along\\n    the extensible dimension in the case of EArray or put a variable\\n    number of them on a VLArray row. Moreover, they are not restricted\\n    to scalar values, and they can be *fully multidimensional\\n    objects*.\\n\\n    Parameters\\n    ----------\\n    itemsize : int\\n        For types with a non-fixed size, this sets the size in\\n        bytes of individual items in the atom.\\n    shape : tuple\\n        Sets the shape of the atom. An integer shape of\\n        N is equivalent to the tuple (N,).\\n    dflt\\n        Sets the default value for the atom.\\n\\n    The following are the public methods and attributes of the Atom class.\\n\\n    Notes\\n    -----\\n    A series of descendant classes are offered in order to make the\\n    use of these element descriptions easier. You should use a\\n    particular Atom descendant class whenever you know the exact type\\n    you will need when writing your code. Otherwise, you may use one\\n    of the Atom.from_*() factory Methods.\\n\\n    .. rubric:: Atom attributes\\n\\n    .. attribute:: dflt\\n\\n        The default value of the atom.\\n\\n        If the user does not supply a value for an element while\\n        filling a dataset, this default value will be written to disk.\\n        If the user supplies a scalar value for a multidimensional\\n        atom, this value is automatically *broadcast* to all the items\\n        in the atom cell. If dflt is not supplied, an appropriate zero\\n        value (or *null* string) will be chosen by default.  Please\\n        note that default values are kept internally as NumPy objects.\\n\\n    .. attribute:: dtype\\n\\n        The NumPy dtype that most closely matches this atom.\\n\\n    .. attribute:: itemsize\\n\\n        Size in bytes of a single item in the atom.\\n        Specially useful for atoms of the string kind.\\n\\n    .. attribute:: kind\\n\\n        The PyTables kind of the atom (a string).\\n\\n    .. attribute:: shape\\n\\n        The shape of the atom (a tuple for scalar atoms).\\n\\n    .. attribute:: type\\n\\n        The PyTables type of the atom (a string).\\n\\n        Atoms can be compared with atoms and other objects for\\n        strict (in)equality without having to compare individual\\n        attributes::\\n\\n            >>> atom1 = StringAtom(itemsize=10)  # same as ``atom2``\\n            >>> atom2 = Atom.from_kind(\'string\', 10)  # same as ``atom1``\\n            >>> atom3 = IntAtom()\\n            >>> atom1 == \'foo\'\\n            False\\n            >>> atom1 == atom2\\n            True\\n            >>> atom2 != atom1\\n            False\\n            >>> atom1 == atom3\\n            False\\n            >>> atom3 != atom2\\n            True\\n\\n    ", \'prefix\': <classmethod object at 0x000001D7BC1C2240>, \'from_sctype\': <classmethod object at 0x000001D7BC1BB320>, \'from_dtype\': <classmethod object at 0x000001D7BC1BB2E8>, \'from_type\': <classmethod object at 0x000001D7BC1BB2B0>, \'from_kind\': <classmethod object at 0x000001D7BC1CB550>, \'size\': <property object at 0x000001D7BC1E3408>, \'recarrtype\': <property object at 0x000001D7BC1E34A8>, \'ndim\': <property object at 0x000001D7BC1E34F8>, \'__init__\': <function Atom.__init__ at 0x000001D7BC1FA378>, \'__repr__\': <function Atom.__repr__ at 0x000001D7BC1FA400>, \'__eq__\': <function _cmp_dispatcher.<locals>.dispatched_cmp at 0x000001D7BC1FA488>, \'__ne__\': <function Atom.__ne__ at 0x000001D7BC1FA510>, \'copy\': <function Atom.copy at 0x000001D7BC1FA598>, \'_get_init_args\': <function Atom._get_init_args at 0x000001D7BC1FA620>, \'_is_equal_to_atom\': <function Atom._is_equal_to_atom at 0x000001D7BC1FA6A8>, \'__dict__\': <attribute \'__dict__\' of \'Atom\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'Atom\' objects>, \'__hash__\': None})'
    __hash__ = None


class AttributeSet(object):
    # no doc
    def _g_getattr(self, *args, **kwargs): # real signature unknown
        """
        Get HDF5 attributes and retrieve them as NumPy objects.
        
            H5T_SCALAR types will be retrieved as scalar NumPy.
            H5T_ARRAY types will be retrieved as ndarray NumPy objects.
        """
        pass

    def _g_list_attr(self, *args, **kwargs): # real signature unknown
        """ Return a tuple with the attribute list """
        pass

    def _g_new(self, *args, **kwargs): # real signature unknown
        pass

    def _g_remove(self, *args, **kwargs): # real signature unknown
        pass

    def _g_setattr(self, *args, **kwargs): # real signature unknown
        """
        Save Python or NumPy objects as HDF5 attributes.
        
            Scalar Python objects, scalar NumPy & 0-dim NumPy objects will all be
            saved as H5T_SCALAR type.  N-dim NumPy objects will be saved as H5T_ARRAY
            type.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass


class DataTypeWarning(Warning):
    """
    Unsupported data type.
    
        This warning is issued when an unsupported HDF5 data type is found
        (normally in a file created with other tool than PyTables).
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class File(object):
    # no doc
    def fileno(self, *args, **kwargs): # real signature unknown
        """
        Return the underlying OS integer file descriptor.
        
            This is needed for lower-level file interfaces, such as the ``fcntl``
            module.
        """
        pass

    def get_filesize(self, *args, **kwargs): # real signature unknown
        """
        Returns the size of an HDF5 file.
        
            The returned size is that of the entire file, as opposed to only
            the HDF5 portion of the file. I.e., size includes the user block,
            if any, the HDF5 portion of the file, and any data that may have
            been appended beyond the data written through the HDF5 Library.
        
            .. versionadded:: 3.0
        """
        pass

    def get_file_image(self, *args, **kwargs): # real signature unknown
        """
        Retrieves an in-memory image of an existing, open HDF5 file.
        
            .. note:: this method requires HDF5 >= 1.8.9.
        
            .. versionadded:: 3.0
        """
        pass

    def get_userblock_size(self, *args, **kwargs): # real signature unknown
        """
        Retrieves the size of a user block.
        
            .. versionadded:: 3.0
        """
        pass

    def _close_file(self, *args, **kwargs): # real signature unknown
        pass

    def _flush_file(self, *args, **kwargs): # real signature unknown
        pass

    def _get_file_id(self, *args, **kwargs): # real signature unknown
        pass

    def _g_new(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass


class Group(Node):
    # no doc
    def _g_close_group(self, *args, **kwargs): # real signature unknown
        pass

    def _g_create(self, *args, **kwargs): # real signature unknown
        pass

    def _g_flush_group(self, *args, **kwargs): # real signature unknown
        pass

    def _g_get_gchild_attr(self, *args, **kwargs): # real signature unknown
        """
        Return an attribute of a child `Group`.
        
            If the attribute does not exist, ``None`` is returned.
        """
        pass

    def _g_get_lchild_attr(self, *args, **kwargs): # real signature unknown
        """
        Return an attribute of a child `Leaf`.
        
            If the attribute does not exist, ``None`` is returned.
        """
        pass

    def _g_get_objinfo(self, *args, **kwargs): # real signature unknown
        """ Check whether 'name' is a children of 'self' and return its type. """
        pass

    def _g_list_group(self, *args, **kwargs): # real signature unknown
        """ Return a tuple with the groups and the leaves hanging from self. """
        pass

    def _g_move_node(self, *args, **kwargs): # real signature unknown
        pass

    def _g_open(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass


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


class ObjInfo(tuple):
    """ ObjInfo(addr, rc) """
    def _asdict(self): # reliably restored by inspect
        """ Return a new OrderedDict which maps field names to their values. """
        pass

    @classmethod
    def _make(cls, *args, **kwargs): # real signature unknown
        """ Make a new ObjInfo object from a sequence or iterable """
        pass

    def _replace(_self, **kwds): # reliably restored by inspect
        """ Return a new ObjInfo object replacing specified fields with new values """
        pass

    def __getnewargs__(self): # reliably restored by inspect
        """ Return self as a plain tuple.  Used by copy and pickle. """
        pass

    def __init__(self, addr, rc): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(_cls, addr, rc): # reliably restored by inspect
        """ Create new instance of ObjInfo(addr, rc) """
        pass

    def __repr__(self): # reliably restored by inspect
        """ Return a nicely formatted representation string """
        pass

    addr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 0"""

    rc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 1"""


    _fields = (
        'addr',
        'rc',
    )
    _fields_defaults = {}
    __slots__ = ()


class ObjTimestamps(tuple):
    """ ObjTimestamps(atime, mtime, ctime, btime) """
    def _asdict(self): # reliably restored by inspect
        """ Return a new OrderedDict which maps field names to their values. """
        pass

    @classmethod
    def _make(cls, *args, **kwargs): # real signature unknown
        """ Make a new ObjTimestamps object from a sequence or iterable """
        pass

    def _replace(_self, **kwds): # reliably restored by inspect
        """ Return a new ObjTimestamps object replacing specified fields with new values """
        pass

    def __getnewargs__(self): # reliably restored by inspect
        """ Return self as a plain tuple.  Used by copy and pickle. """
        pass

    def __init__(self, atime, mtime, ctime, btime): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(_cls, atime, mtime, ctime, btime): # reliably restored by inspect
        """ Create new instance of ObjTimestamps(atime, mtime, ctime, btime) """
        pass

    def __repr__(self): # reliably restored by inspect
        """ Return a nicely formatted representation string """
        pass

    atime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 0"""

    btime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 3"""

    ctime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 2"""

    mtime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 1"""


    _fields = (
        'atime',
        'mtime',
        'ctime',
        'btime',
    )
    _fields_defaults = {}
    __slots__ = ()


class SizeType(__numpy.signedinteger):
    """
    Signed integer type, compatible with C ``long long``.
        Character code: ``'q'``.
        Canonical name: ``np.longlong``.
        Alias *on this platform*: ``np.int64``: 64-bit signed integer (-9223372036854775808 to 9223372036854775807).
        Alias *on this platform*: ``np.intp``: Signed integer large enough to fit pointer, compatible with C ``intptr_t``.
    """
    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass


class UnImplemented(Leaf):
    # no doc
    def _g_close(self, *args, **kwargs): # real signature unknown
        pass

    def _open_unimplemented(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001D7BC239210>'


class VLArray(Leaf):
    # no doc
    def get_row_size(self, *args, **kwargs): # real signature unknown
        """ Return the total size in bytes of all the elements contained in a given row. """
        pass

    def _append(self, *args, **kwargs): # real signature unknown
        pass

    def _create_array(self, *args, **kwargs): # real signature unknown
        pass

    def _get_memory_size(self, *args, **kwargs): # real signature unknown
        pass

    def _modify(self, *args, **kwargs): # real signature unknown
        pass

    def _open_array(self, *args, **kwargs): # real signature unknown
        pass

    def _read_array(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001D7BC2391E0>'


# variables with complex values

byteorders = {
    '<': 'little',
    '=': 'little',
    '>': 'big',
    '|': 'irrelevant',
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

_supported_drivers = (
    'H5FD_SEC2',
    'H5FD_DIRECT',
    'H5FD_WINDOWS',
    'H5FD_STDIO',
    'H5FD_CORE',
    'H5FD_SPLIT',
)

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001D7BC23E748>'

__spec__ = None # (!) real value is "ModuleSpec(name='tables.hdf5extension', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001D7BC23E748>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\tables\\\\hdf5extension.cp37-win_amd64.pyd')"

__test__ = {}

