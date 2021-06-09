# encoding: utf-8
# module h5py.h5f
# from C:\Users\Doly\Anaconda3\lib\site-packages\h5py\h5f.cp37-win_amd64.pyd
# by generator 1.147
""" Low-level operations on HDF5 file objects. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import h5py._objects as _objects # C:\Users\Doly\Anaconda3\lib\site-packages\h5py\_objects.cp37-win_amd64.pyd
import h5py.h5fd as h5fd # C:\Users\Doly\Anaconda3\lib\site-packages\h5py\h5fd.cp37-win_amd64.pyd
from h5py._objects import (create, flush, get_name, get_obj_count, 
    get_obj_ids, is_hdf5, mount, open, open_file_image, unmount, with_phil)

import h5py.h5g as __h5py_h5g


# Variables with simple values

ACC_EXCL = 4
ACC_RDONLY = 0
ACC_RDWR = 1

ACC_SWMR_READ = 64
ACC_SWMR_WRITE = 32

ACC_TRUNC = 2

CLOSE_DEFAULT = 0
CLOSE_SEMI = 2
CLOSE_STRONG = 3
CLOSE_WEAK = 1

FILE_IMAGE_OPEN_RW = 1

LIBVER_EARLIEST = 0
LIBVER_LATEST = 2

OBJ_ALL = 31
OBJ_ATTR = 16
OBJ_DATASET = 2
OBJ_DATATYPE = 8
OBJ_FILE = 1
OBJ_GROUP = 4
OBJ_LOCAL = 32

SCOPE_GLOBAL = 1
SCOPE_LOCAL = 0

UNLIMITED = 18446744073709551615

# functions

def __pyx_unpickle_FileID(*args, **kwargs): # real signature unknown
    pass

# classes

class FileID(__h5py_h5g.GroupID):
    """
    Represents an HDF5 file identifier.
    
            These objects wrap a small portion of the H5F interface; all the
            H5F functions which can take arbitrary objects in addition to
            file identifiers are provided as functions in the h5f module.
    
            Properties:
    
            * name:   File name on disk
    
            Behavior:
    
            * Hashable: Yes, unique to the file (but not the access mode)
            * Equality: Hash comparison
    """
    def close(self, *args, **kwargs): # real signature unknown
        """
        ()
        
                Terminate access through this identifier.  Note that depending on
                what property list settings were used to open the file, the
                physical file might not be closed until all remaining open
                identifiers are freed.
        """
        pass

    def get_access_plist(self, *args, **kwargs): # real signature unknown
        """
        () => PropFAID
        
                Retrieve a copy of the file access property list which manages access
                to this file.
        """
        pass

    def get_create_plist(self, *args, **kwargs): # real signature unknown
        """
        () => PropFCID
        
                Retrieve a copy of the file creation property list used to
                create this file.
        """
        pass

    def get_filesize(self, *args, **kwargs): # real signature unknown
        """
        () => LONG size
        
                Determine the total size (in bytes) of the HDF5 file,
                including any user block.
        """
        pass

    def get_file_image(self, *args, **kwargs): # real signature unknown
        """
        () => BYTES
        
                    Retrieves a copy of the image of an existing, open file.
        
                    Feature requires: 1.8.9
        """
        pass

    def get_freespace(self, *args, **kwargs): # real signature unknown
        """
        () => LONG freespace
        
                Determine the amount of free space in this file.  Note that this
                only tracks free space until the file is closed.
        """
        pass

    def get_intent(self, *args, **kwargs): # real signature unknown
        """
        () => INT
        
                Determine the file's write intent, either of:
                - H5F_ACC_RDONLY
                - H5F_ACC_RDWR
        """
        pass

    def get_mdc_config(self, *args, **kwargs): # real signature unknown
        """
        () => CacheConfig
                Returns an object that stores all the information about the meta-data cache
                configuration
        """
        pass

    def get_mdc_hit_rate(self, *args, **kwargs): # real signature unknown
        """
        () => DOUBLE
        
                Retrieve the cache hit rate
        """
        pass

    def get_mdc_size(self, *args, **kwargs): # real signature unknown
        """
        () => (max_size, min_clean_size, cur_size, cur_num_entries) [SIZE_T, SIZE_T, SIZE_T, INT]
        
                Obtain current metadata cache size data for specified file.
        """
        pass

    def get_vfd_handle(self, *args, **kwargs): # real signature unknown
        """
        () => INT
        
                Retrieve the file handle used by the virtual file driver.
        
                This method is only functional when the the SEC2 driver is used.
        """
        pass

    def reopen(self, *args, **kwargs): # real signature unknown
        """
        () => FileID
        
                Retrieve another identifier for a file (which must still be open).
                The new identifier is guaranteed to neither be mounted nor contain
                a mounted file.
        """
        pass

    def reset_mdc_hit_rate_stats(self, *args, **kwargs): # real signature unknown
        """
        no return
        
                rests the hit-rate statistics
        """
        pass

    def set_mdc_config(self, *args, **kwargs): # real signature unknown
        """
        (CacheConfig) => None
                Returns an object that stores all the information about the meta-data cache
                configuration
        """
        pass

    def start_swmr_write(self, *args, **kwargs): # real signature unknown
        """
        no return
        
                    Enables SWMR writing mode for a file.
        
                    This function will activate SWMR writing mode for a file associated
                    with file_id. This routine will prepare and ensure the file is safe
                    for SWMR writing as follows:
        
                        * Check that the file is opened with write access (H5F_ACC_RDWR).
                        * Check that the file is opened with the latest library format
                          to ensure data structures with check-summed metadata are used.
                        * Check that the file is not already marked in SWMR writing mode.
                        * Enable reading retries for check-summed metadata to remedy
                          possible checksum failures from reading inconsistent metadata
                          on a system that is not atomic.
                        * Turn off usage of the library’s accumulator to avoid possible
                          ordering problem on a system that is not atomic.
                        * Perform a flush of the file’s data buffers and metadata to set
                          a consistent state for starting SWMR write operations.
        
                    Library objects are groups, datasets, and committed datatypes. For
                    the current implementation, groups and datasets can remain open when
                    activating SWMR writing mode, but not committed datatypes. Attributes
                    attached to objects cannot remain open.
        
                    Feature requires: 1.9.178 HDF5
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

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ File name on disk (according to h5f.get_name()) """



# variables with complex values

phil = _objects.phil

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001ECED27D940>'

__spec__ = None # (!) real value is "ModuleSpec(name='h5py.h5f', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001ECED27D940>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\h5py\\\\h5f.cp37-win_amd64.pyd')"

__test__ = {}

