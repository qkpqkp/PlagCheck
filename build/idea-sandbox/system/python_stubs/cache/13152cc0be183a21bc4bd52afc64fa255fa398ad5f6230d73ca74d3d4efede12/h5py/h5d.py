# encoding: utf-8
# module h5py.h5d
# from C:\Users\Doly\Anaconda3\lib\site-packages\h5py\h5d.cp37-win_amd64.pyd
# by generator 1.147
""" Provides access to the low-level HDF5 "H5D" dataset interface. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import h5py._objects as _objects # C:\Users\Doly\Anaconda3\lib\site-packages\h5py\_objects.cp37-win_amd64.pyd
from h5py._objects import create, open, with_phil

import h5py._objects as __h5py__objects


# Variables with simple values

ALLOC_TIME_DEFAULT = 0
ALLOC_TIME_EARLY = 1
ALLOC_TIME_INCR = 3
ALLOC_TIME_LATE = 2

CHUNKED = 2

COMPACT = 0
CONTIGUOUS = 1

FILL_TIME_ALLOC = 0
FILL_TIME_IFSET = 2
FILL_TIME_NEVER = 1

FILL_VALUE_DEFAULT = 1
FILL_VALUE_UNDEFINED = 0

FILL_VALUE_USER_DEFINED = 2

SPACE_STATUS_ALLOCATED = 2

SPACE_STATUS_NOT_ALLOCATED = 0

SPACE_STATUS_PART_ALLOCATED = 1

VDS_FIRST_MISSING = 0

VDS_LAST_AVAILABLE = 1

VIRTUAL = 3

# functions

def __pyx_unpickle_DatasetID(*args, **kwargs): # real signature unknown
    pass

# classes

class DatasetID(__h5py__objects.ObjectID):
    """
    Represents an HDF5 dataset identifier.
    
            Objects of this class may be used in any HDF5 function which expects
            a dataset identifier.  Also, all H5D* functions which take a dataset
            instance as their first argument are presented as methods of this
            class.
    
            Properties:
            dtype:  Numpy dtype representing the dataset type
            shape:  Numpy-style shape tuple representing the dataspace
            rank:   Integer giving dataset rank
    
            * Hashable: Yes, unless anonymous
            * Equality: True HDF5 identity if unless anonymous
    """
    def extend(self, *args, **kwargs): # real signature unknown
        """
        (TUPLE shape)
        
                    Extend the given dataset so it's at least as big as "shape".  Note
                    that a dataset may only be extended up to the maximum dimensions of
                    its dataspace, which are fixed when the dataset is created.
        """
        pass

    def flush(self, *args, **kwargs): # real signature unknown
        """
        no return
        
                    Flushes all buffers associated with a dataset to disk.
        
                    This function causes all buffers associated with a dataset to be
                    immediately flushed to disk without removing the data from the cache.
        
                    Use this in SWMR write mode to allow readers to be updated with the
                    dataset changes.
        
                    Feature requires: 1.9.178 HDF5
        """
        pass

    def get_access_plist(self, *args, **kwargs): # real signature unknown
        """
        () => PropDAID
        
                    Create an return a new copy of the dataset access property list.
        """
        pass

    def get_create_plist(self, *args, **kwargs): # real signature unknown
        """
        () => PropDCID
        
                    Create an return a new copy of the dataset creation property list
                    used when this dataset was created.
        """
        pass

    def get_offset(self, *args, **kwargs): # real signature unknown
        """
        () => LONG offset or None
        
                    Get the offset of this dataset in the file, in bytes, or None if
                    it doesn't have one.  This is always the case for datasets which
                    use chunked storage, compact datasets, and datasets for which space
                    has not yet been allocated in the file.
        """
        pass

    def get_space(self, *args, **kwargs): # real signature unknown
        """
        () => SpaceID
        
                    Create and return a new copy of the dataspace for this dataset.
        """
        pass

    def get_space_status(self, *args, **kwargs): # real signature unknown
        """
        () => INT space_status_code
        
                    Determine if space has been allocated for a dataset.
                    Return value is one of:
        
                    * SPACE_STATUS_NOT_ALLOCATED
                    * SPACE_STATUS_PART_ALLOCATED
                    * SPACE_STATUS_ALLOCATED
        """
        pass

    def get_storage_size(self, *args, **kwargs): # real signature unknown
        """
        () => LONG storage_size
        
                    Determine the amount of file space required for a dataset.  Note
                    this only counts the space which has actually been allocated; it
                    may even be zero.
        """
        pass

    def get_type(self, *args, **kwargs): # real signature unknown
        """
        () => TypeID
        
                    Create and return a new copy of the datatype for this dataset.
        """
        pass

    def read(self, *args, **kwargs): # real signature unknown
        """
        (SpaceID mspace, SpaceID fspace, NDARRAY arr_obj,
                     TypeID mtype=None, PropDXID dxpl=None)
        
                    Read data from an HDF5 dataset into a Numpy array.
        
                    It is your responsibility to ensure that the memory dataspace
                    provided is compatible with the shape of the Numpy array.  Since a
                    wide variety of dataspace configurations are possible, this is not
                    checked.  You can easily crash Python by reading in data from too
                    large a dataspace.
        
                    If a memory datatype is not specified, one will be auto-created
                    based on the array's dtype.
        
                    The provided Numpy array must be writable and C-contiguous.  If
                    this is not the case, ValueError will be raised and the read will
                    fail.  Keyword dxpl may be a dataset transfer property list.
        """
        pass

    def refresh(self, *args, **kwargs): # real signature unknown
        """
        no return
        
                    Refreshes all buffers associated with a dataset.
        
                    This function causes all buffers associated with a dataset to be
                    cleared and immediately re-loaded with updated contents from disk.
        
                    This function essentially closes the dataset, evicts all metadata
                    associated with it from the cache, and then re-opens the dataset.
                    The reopened dataset is automatically re-registered with the same ID.
        
                    Use this in SWMR read mode to poll for dataset changes.
        
                    Feature requires: 1.9.178 HDF5
        """
        pass

    def set_extent(self, *args, **kwargs): # real signature unknown
        """
        (TUPLE shape)
        
                    Set the size of the dataspace to match the given shape.  If the new
                    size is larger in any dimension, it must be compatible with the
                    maximum dataspace size.
        """
        pass

    def write(self, *args, **kwargs): # real signature unknown
        """
        (SpaceID mspace, SpaceID fspace, NDARRAY arr_obj,
                     TypeID mtype=None, PropDXID dxpl=None)
        
                    Write data from a Numpy array to an HDF5 dataset. Keyword dxpl may
                    be a dataset transfer property list.
        
                    It is your responsibility to ensure that the memory dataspace
                    provided is compatible with the shape of the Numpy array.  Since a
                    wide variety of dataspace configurations are possible, this is not
                    checked.  You can easily crash Python by writing data from too
                    large a dataspace.
        
                    If a memory datatype is not specified, one will be auto-created
                    based on the array's dtype.
        
                    The provided Numpy array must be C-contiguous.  If this is not the
                    case, ValueError will be raised and the read will fail.
        """
        pass

    def write_direct_chunk(self, *args, **kwargs): # real signature unknown
        """
        (offsets, bytes data, H5Z_filter_t filter_mask=H5Z_FILTER_NONE, PropID dxpl=None)
        
                    Writes data from a bytes array (as provided e.g. by struct.pack) directly
                    to a chunk at position specified by the offsets argument.
        
                    Feature requires: 1.8.11 HDF5
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

    dtype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ Numpy dtype object representing the dataset type """

    rank = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ Integer giving the dataset rank (0 = scalar) """

    shape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ Numpy-style shape tuple representing the dataspace """



# variables with complex values

phil = _objects.phil

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000017FBABEC400>'

__spec__ = None # (!) real value is "ModuleSpec(name='h5py.h5d', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000017FBABEC400>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\h5py\\\\h5d.cp37-win_amd64.pyd')"

__test__ = {}

