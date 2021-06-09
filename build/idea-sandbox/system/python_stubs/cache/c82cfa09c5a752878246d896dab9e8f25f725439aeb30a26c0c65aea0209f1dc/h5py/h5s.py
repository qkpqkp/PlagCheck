# encoding: utf-8
# module h5py.h5s
# from C:\Users\Doly\Anaconda3\lib\site-packages\h5py\h5s.cp37-win_amd64.pyd
# by generator 1.147
""" Low-level interface to the "H5S" family of data-space functions. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import h5py._objects as _objects # C:\Users\Doly\Anaconda3\lib\site-packages\h5py\_objects.cp37-win_amd64.pyd
from h5py._objects import create, create_simple, decode, with_phil

import h5py._objects as __h5py__objects


# Variables with simple values

NO_CLASS = -1

NULL = 2

SCALAR = 0

SELECT_AND = 2
SELECT_APPEND = 6
SELECT_INVALID = 8
SELECT_NOOP = -1
SELECT_NOTA = 5
SELECT_NOTB = 4
SELECT_OR = 1
SELECT_PREPEND = 7
SELECT_SET = 0
SELECT_XOR = 3

SEL_ALL = 3
SEL_ERROR = -1
SEL_HYPERSLABS = 2
SEL_NONE = 0
SEL_POINTS = 1

SIMPLE = 1

UNLIMITED = 18446744073709551615

# no functions
# classes

class SpaceID(__h5py__objects.ObjectID):
    """
    Represents a dataspace identifier.
    
            Properties:
    
            shape
                Numpy-style shape tuple with dimensions.
    
            * Hashable: No
            * Equality: Unimplemented
    
            Can be pickled if HDF5 1.8 is available.
    """
    def copy(self, *args, **kwargs): # real signature unknown
        """
        () => SpaceID
        
                Create a new copy of this dataspace.
        """
        pass

    def encode(self, *args, **kwargs): # real signature unknown
        """
        () => STRING
        
                Serialize a dataspace, including its selection.  Bear in mind you
                can also use the native Python pickling machinery to do this.
        """
        pass

    def extent_copy(self, *args, **kwargs): # real signature unknown
        """
        (SpaceID source)
        
                Replace this dataspace's extent with another's, changing its
                typecode if necessary.
        """
        pass

    def get_regular_hyperslab(self, *args, **kwargs): # real signature unknown
        """
        () => (TUPLE start, TUPLE stride, TUPLE count, TUPLE block)
        
                    Retrieve a regular hyperslab selection.
        """
        pass

    def get_select_bounds(self, *args, **kwargs): # real signature unknown
        """
        () => (TUPLE start, TUPLE end)
        
                Determine the bounding box which exactly contains
                the current selection.
        """
        pass

    def get_select_elem_npoints(self, *args, **kwargs): # real signature unknown
        """
        () => LONG npoints
        
                Determine the number of elements selected in point-selection mode.
        """
        pass

    def get_select_elem_pointlist(self, *args, **kwargs): # real signature unknown
        """
        () => NDARRAY
        
                Get a list of all selected elements.  Return is a Numpy array of
                unsigned ints, with shape ``(<npoints>, <space rank)``.
        """
        pass

    def get_select_hyper_blocklist(self, *args, **kwargs): # real signature unknown
        """
        () => NDARRAY
        
                Get the current hyperslab selection.  The returned array has shape::
        
                    (<npoints>, 2, <rank>)
        
                and can be interpreted as a nested sequence::
        
                    [ (corner_coordinate_1, opposite_coordinate_1), ... ]
        
                with length equal to the total number of blocks.
        """
        pass

    def get_select_hyper_nblocks(self, *args, **kwargs): # real signature unknown
        """
        () => LONG nblocks
        
                Get the number of hyperslab blocks currently selected.
        """
        pass

    def get_select_npoints(self, *args, **kwargs): # real signature unknown
        """
        () => LONG npoints
        
                Determine the total number of points currently selected.
                Works for all selection techniques.
        """
        pass

    def get_select_type(self, *args, **kwargs): # real signature unknown
        """
        () => INT select_code
        
                    Determine selection type.  Return values are:
        
                    - SEL_NONE
                    - SEL_ALL
                    - SEL_POINTS
                    - SEL_HYPERSLABS
        """
        pass

    def get_simple_extent_dims(self, *args, **kwargs): # real signature unknown
        """
        (BOOL maxdims=False) => TUPLE shape
        
                Determine the shape of a "simple" (slab) dataspace.  If "maxdims"
                is True, retrieve the maximum dataspace size instead.
        """
        pass

    def get_simple_extent_ndims(self, *args, **kwargs): # real signature unknown
        """
        () => INT rank
        
                Determine the rank of a "simple" (slab) dataspace.
        """
        pass

    def get_simple_extent_npoints(self, *args, **kwargs): # real signature unknown
        """
        () => LONG npoints
        
                Determine the total number of elements in a dataspace.
        """
        pass

    def get_simple_extent_type(self, *args, **kwargs): # real signature unknown
        """
        () => INT class_code
        
                Class code is either SCALAR or SIMPLE.
        """
        pass

    def is_regular_hyperslab(self, *args, **kwargs): # real signature unknown
        """
        () => BOOL
        
                    Determine whether a hyperslab selection is regular.
        """
        pass

    def is_simple(self, *args, **kwargs): # real signature unknown
        """
        () => BOOL is_simple
        
                Determine if an existing dataspace is "simple" (including scalar
                dataspaces). Currently all HDF5 dataspaces are simple.
        """
        pass

    def offset_simple(self, *args, **kwargs): # real signature unknown
        """
        (TUPLE offset=None)
        
                Set the offset of a dataspace.  The length of the given tuple must
                match the rank of the dataspace. If None is provided (default),
                the offsets on all axes will be set to 0.
        """
        pass

    def select_all(self, *args, **kwargs): # real signature unknown
        """
        ()
        
                Select all points in the dataspace.
        """
        pass

    def select_elements(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        (SEQUENCE coords, INT op=SELECT_SET)
        
                Select elements by specifying coordinates points.  The argument
                "coords" may be an ndarray or any nested sequence which can be
                converted to an array of uints with the shape::
        
                    (<npoints>, <space rank>)
        
                Examples::
        
                    >>> obj.shape
                    (10, 10)
                    >>> obj.select_elements([(1,2), (3,4), (5,9)])
        
                A zero-length selection (i.e. shape ``(0, <rank>)``) is not allowed
                by the HDF5 library.
        """
        pass

    def select_hyperslab(self, *args, **kwargs): # real signature unknown
        """
        (TUPLE start, TUPLE count, TUPLE stride=None, TUPLE block=None,
                     INT op=SELECT_SET)
        
                Select a block region from an existing dataspace.  See the HDF5
                documentation for the meaning of the "block" and "op" keywords.
        """
        pass

    def select_none(self, *args, **kwargs): # real signature unknown
        """
        ()
        
                Deselect entire dataspace.
        """
        pass

    def select_valid(self, *args, **kwargs): # real signature unknown
        """
        () => BOOL
        
                Determine if the current selection falls within
                the dataspace extent.
        """
        pass

    def set_extent_none(self, *args, **kwargs): # real signature unknown
        """
        ()
        
                Remove the dataspace extent; typecode changes to NO_CLASS.
        """
        pass

    def set_extent_simple(self, *args, **kwargs): # real signature unknown
        """
        (TUPLE dims_tpl, TUPLE max_dims_tpl=None)
        
                Reset the dataspace extent via a tuple of dimensions.
                Every element of dims_tpl must be a positive integer.
        
                You can optionally specify the maximum dataspace size. The
                special value UNLIMITED, as an element of max_dims, indicates
                an unlimited dimension.
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

    shape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ Numpy-style shape tuple representing dimensions.  () == scalar.
        """



# variables with complex values

ALL = None # (!) real value is '<h5py.h5s.SpaceID object at 0x000001DD52C5FEF8>'

phil = _objects.phil

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001DD52C5D780>'

__spec__ = None # (!) real value is "ModuleSpec(name='h5py.h5s', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001DD52C5D780>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\h5py\\\\h5s.cp37-win_amd64.pyd')"

__test__ = {
    'SpaceID.select_elements (line 460)': '(SEQUENCE coords, INT op=SELECT_SET)\n\n        Select elements by specifying coordinates points.  The argument\n        "coords" may be an ndarray or any nested sequence which can be\n        converted to an array of uints with the shape::\n\n            (<npoints>, <space rank>)\n\n        Examples::\n\n            >>> obj.shape\n            (10, 10)\n            >>> obj.select_elements([(1,2), (3,4), (5,9)])\n\n        A zero-length selection (i.e. shape ``(0, <rank>)``) is not allowed\n        by the HDF5 library.\n        ',
}

