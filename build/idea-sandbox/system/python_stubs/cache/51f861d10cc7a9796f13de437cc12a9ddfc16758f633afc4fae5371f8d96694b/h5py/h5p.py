# encoding: utf-8
# module h5py.h5p
# from C:\Users\Doly\Anaconda3\lib\site-packages\h5py\h5p.cp37-win_amd64.pyd
# by generator 1.147
""" HDF5 property list interface. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import h5py._objects as _objects # C:\Users\Doly\Anaconda3\lib\site-packages\h5py\_objects.cp37-win_amd64.pyd
from h5py._objects import create, with_phil

import h5py._objects as __h5py__objects


# Variables with simple values

CRT_ORDER_INDEXED = 2
CRT_ORDER_TRACKED = 1

DEFAULT = None

# functions

def __pyx_unpickle_PropClassID(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_PropCopyID(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_PropCreateID(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_PropDAID(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_PropDCID(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_PropDXID(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_PropFAID(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_PropFCID(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_PropGCID(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_PropID(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_PropInstanceID(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_PropLCID(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_PropOCID(*args, **kwargs): # real signature unknown
    pass

# classes

class PropID(__h5py__objects.ObjectID):
    """ Base class for all property lists and classes """
    def equal(self, *args, **kwargs): # real signature unknown
        """
        (PropID plist) => BOOL
        
                Compare this property list (or class) to another for equality.
        """
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


class PropClassID(PropID):
    """
    An HDF5 property list class.
    
            * Hashable: Yes, by identifier
            * Equality: Logical H5P comparison
    """
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
        """
        Since classes are library-created and immutable, they are uniquely
                    identified by their HDF5 identifiers.
        """
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


class PropInstanceID(PropID):
    """
    Base class for property list instance objects.  Provides methods which
            are common across all HDF5 property list classes.
    
            * Hashable: No
            * Equality: Logical H5P comparison
    """
    def copy(self, *args, **kwargs): # real signature unknown
        """
        () => PropList newid
        
                 Create a new copy of an existing property list object.
        """
        pass

    def get_class(self, *args, **kwargs): # real signature unknown
        """
        () => PropClassID
        
                Determine the class of a property list object.
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


class PropCopyID(PropInstanceID):
    """ Generic object copy property list """
    def get_copy_object(self, *args, **kwargs): # real signature unknown
        """
        () => UINT flags
        
                Get copy process flags. Legal flags are h5o.COPY*.
        """
        pass

    def set_copy_object(self, *args, **kwargs): # real signature unknown
        """
        (UINT flags)
        
                Set flags for object copying process.  Legal flags are
                from the h5o.COPY* family:
        
                h5o.COPY_SHALLOW_HIERARCHY_FLAG
                    Copy only immediate members of a group.
        
                h5o.COPY_EXPAND_SOFT_LINK_FLAG
                    Expand soft links into new objects.
        
                h5o.COPY_EXPAND_EXT_LINK_FLAG
                    Expand external link into new objects.
        
                h5o.COPY_EXPAND_REFERENCE_FLAG
                    Copy objects that are pointed to by references.
        
                h5o.COPY_WITHOUT_ATTR_FLAG
                    Copy object without copying attributes.
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


class PropCreateID(PropInstanceID):
    """ Generic object creation property list. """
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


class PropDAID(PropInstanceID):
    """ Dataset access property list """
    def get_chunk_cache(self, *args, **kwargs): # real signature unknown
        """
        () => TUPLE chunk cache info
        
                Get the metadata and raw data chunk cache settings.  See the HDF5
                docs for element definitions.  Return is a 3-tuple with entries:
        
                0. size_t rdcc_nslots: Number of chunk slots in the raw data chunk cache hash table.
                1. size_t rdcc_nbytes: Total size of the raw data chunk cache, in bytes.
                2. DOUBLE rdcc_w0:     Preemption policy.
        """
        pass

    def get_virtual_printf_gap(self, *args, **kwargs): # real signature unknown
        """
        () => LONG gap_size
        
                    Return the maximum number of missing source files and/or datasets
                    with the printf-style names when getting the extent for an
                    unlimited virtual dataset.
        """
        pass

    def get_virtual_view(self, *args, **kwargs): # real signature unknown
        """
        () => UINT view
        
                    Retrieve the view of the virtual dataset.
        
                    Valid values are:
        
                    - h5d.VDS_FIRST_MISSING
                    - h5d.VDS_LAST_AVAILABLE
        """
        pass

    def set_chunk_cache(self, *args, **kwargs): # real signature unknown
        """
        (size_t rdcc_nslots,size_t rdcc_nbytes, double rdcc_w0)
        
                Sets the raw data chunk cache parameters.
        """
        pass

    def set_virtual_printf_gap(self, *args, **kwargs): # real signature unknown
        """
        (LONG gap_size=0)
        
                    Set the maximum number of missing source files and/or datasets
                    with the printf-style names when getting the extent of an unlimited
                    virtual dataset.
        
                    Instruct the library to stop looking for the mapped data stored in
                    the files and/or datasets with the printf-style names after not
                    finding gap_size files and/or datasets. The found source files and
                    datasets will determine the extent of the unlimited virtual dataset
                    with the printf-style mappings. Default value: 0.
        """
        pass

    def set_virtual_view(self, *args, **kwargs): # real signature unknown
        """
        (UINT view)
        
                    Set the view of the virtual dataset (VDS) to include or exclude
                    missing mapped elements.
        
                    If view is set to h5d.VDS_FIRST_MISSING, the view includes all data
                    before the first missing mapped data. This setting provides a view
                    containing only the continuous data starting with the dataset’s
                    first data element. Any break in continuity terminates the view.
        
                    If view is set to h5d.VDS_LAST_AVAILABLE, the view includes all
                    available mapped data.
        
                    Missing mapped data is filled with the fill value set in the
                    virtual dataset's creation property list.
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


class PropOCID(PropCreateID):
    """
    Object creation property list
    
        This seems to be a super class for dataset creation property list
        and group creation property list.
    
        The documentation is somewhat hazy
    """
    def get_attr_creation_order(self, *args, **kwargs): # real signature unknown
        """
        () -> UINT flags
        
                Get tracking and indexing of creation order for object attributes
        """
        pass

    def get_obj_track_times(self, *args, **kwargs): # real signature unknown
        """ Determines whether times associated with an object are being recorded. """
        pass

    def set_attr_creation_order(self, *args, **kwargs): # real signature unknown
        """
        (UINT flags)
        
                Set tracking and indexing of creation order for object attributes
        
                flags -- h5p.CRT_ORDER_TRACKED, h5p.CRT_ORDER_INDEXED
        """
        pass

    def set_obj_track_times(self, *args, **kwargs): # real signature unknown
        """ Sets the recording of times associated with an object. """
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


class PropDCID(PropOCID):
    """ Dataset creation property list. """
    def all_filters_avail(self, *args, **kwargs): # real signature unknown
        """
        () => BOOL
        
                Determine if all the filters in the pipelist are available to
                the library.
        """
        pass

    def fill_value_defined(self, *args, **kwargs): # real signature unknown
        """
        () => INT fill_status
        
                Determine the status of the dataset fill value.  Return values are:
        
                - h5d.FILL_VALUE_UNDEFINED
                - h5d.FILL_VALUE_DEFAULT
                - h5d.FILL_VALUE_USER_DEFINED
        """
        pass

    def get_alloc_time(self, *args, **kwargs): # real signature unknown
        """
        () => INT alloc_time
        
                Get the storage space allocation time.  One of h5d.ALLOC_TIME*.
        """
        pass

    def get_chunk(self, *args, **kwargs): # real signature unknown
        """
        () => TUPLE chunk_dimensions
        
                Obtain the dataset chunk size, as a tuple.
        """
        pass

    def get_external(self, *args, **kwargs): # real signature unknown
        """
        (UINT idx=0) => TUPLE external_file_info
        
                Returns information about the indexed external file.
                Tuple elements are:
        
                0. STRING name of file (256 chars max)
                1. UINT offset
                2. UINT size
        """
        pass

    def get_external_count(self, *args, **kwargs): # real signature unknown
        """
        () => INT
        
                Returns the number of external files for the dataset.
        """
        pass

    def get_fill_time(self, *args, **kwargs): # real signature unknown
        """
        () => INT
        
                Determine when fill values are written to the dataset.  Legal
                values (defined in module h5d) are:
        
                - h5d.FILL_TIME_ALLOC
                - h5d.FILL_TIME_NEVER
                - h5d.FILL_TIME_IFSET
        """
        pass

    def get_fill_value(self, *args, **kwargs): # real signature unknown
        """
        (NDARRAY value)
        
                Read the dataset fill value into a NumPy array.  It will be
                converted to match the array dtype.  If the array has nonzero
                rank, only the first element will contain the value.
        """
        pass

    def get_filter(self, *args, **kwargs): # real signature unknown
        """
        (UINT filter_idx) => TUPLE filter_info
        
                Get information about a filter, identified by its index.  Tuple
                elements are:
        
                0. INT filter code (h5z.FILTER*)
                1. UINT flags (h5z.FLAG*)
                2. TUPLE of UINT values; filter aux data (16 values max)
                3. STRING name of filter (256 chars max)
        """
        pass

    def get_filter_by_id(self, *args, **kwargs): # real signature unknown
        """
        (INT filter_code) => TUPLE filter_info or None
        
                Get information about a filter, identified by its code (one
                of h5z.FILTER*).  If the filter doesn't exist, returns None.
                Tuple elements are:
        
                0. UINT flags (h5z.FLAG*)
                1. TUPLE of UINT values; filter aux data (16 values max)
                2. STRING name of filter (256 chars max)
        """
        pass

    def get_layout(self, *args, **kwargs): # real signature unknown
        """
        () => INT layout_code
        
                Determine the storage strategy of a dataset; legal values are:
        
                - h5d.COMPACT
                - h5d.CONTIGUOUS
                - h5d.CHUNKED
                - h5d.VIRTUAL (If using HDF5 library version 1.10 or later)
        """
        pass

    def get_nfilters(self, *args, **kwargs): # real signature unknown
        """
        () => INT
        
                Determine the number of filters in the pipeline.
        """
        pass

    def get_virtual_count(self, *args, **kwargs): # real signature unknown
        """
        () => UINT
        
                    Get the number of mappings for the virtual dataset.
        """
        pass

    def get_virtual_dsetname(self, *args, **kwargs): # real signature unknown
        """
        (UINT index=0) => STR
        
                    Get the name of a source dataset used in the mapping of the virtual
                    dataset at the position index.
        """
        pass

    def get_virtual_filename(self, *args, **kwargs): # real signature unknown
        """
        (UINT index=0) => STR
        
                    Get the file name of a source dataset used in the mapping of the
                    virtual dataset at the position index.
        """
        pass

    def get_virtual_srcspace(self, *args, **kwargs): # real signature unknown
        """
        (UINT index=0) => SpaceID
        
                    Get a dataspace for the selection within the source dataset used
                    in the mapping.
        """
        pass

    def get_virtual_vspace(self, *args, **kwargs): # real signature unknown
        """
        (UINT index=0) => SpaceID
        
                    Get a dataspace for the selection within the virtual dataset used
                    in the mapping.
        """
        pass

    def remove_filter(self, *args, **kwargs): # real signature unknown
        """
        (INT filter_class)
        
                Remove a filter from the pipeline.  The class code is one of
                h5z.FILTER*.
        """
        pass

    def set_alloc_time(self, *args, **kwargs): # real signature unknown
        """
        (INT alloc_time)
        
                Set the storage space allocation time.  One of h5d.ALLOC_TIME*.
        """
        pass

    def set_chunk(self, *args, **kwargs): # real signature unknown
        """
        (TUPLE chunksize)
        
                Set the dataset chunk size.  It's up to you to provide
                values which are compatible with your dataset.
        """
        pass

    def set_deflate(self, *args, **kwargs): # real signature unknown
        """
        (UINT level=5)
        
                Enable deflate (gzip) compression, at the given level.
                Valid levels are 0-9, default is 5.
        """
        pass

    def set_external(self, *args, **kwargs): # real signature unknown
        """
        (STR name, UINT offset, UINT size)
        
                Adds an external file to the list of external files for the dataset.
        
                The first call sets the external storage property in the property list,
                thus designating that the dataset will be stored in one or more non-HDF5
                file(s) external to the HDF5 file.
        """
        pass

    def set_fill_time(self, *args, **kwargs): # real signature unknown
        """
        (INT fill_time)
        
                Define when fill values are written to the dataset.  Legal
                values (defined in module h5d) are:
        
                - h5d.FILL_TIME_ALLOC
                - h5d.FILL_TIME_NEVER
                - h5d.FILL_TIME_IFSET
        """
        pass

    def set_fill_value(self, *args, **kwargs): # real signature unknown
        """
        (NDARRAY value)
        
                Set the dataset fill value.  The object provided should be an
                0-dimensional NumPy array; otherwise, the value will be read from
                the first element.
        """
        pass

    def set_filter(self, *args, **kwargs): # real signature unknown
        """
        (INT filter_code, UINT flags=0, TUPLE values=None)
        
                Set a filter in the pipeline.  Params are:
        
                filter_code
                    One of the following:
        
                    - h5z.FILTER_DEFLATE
                    - h5z.FILTER_SHUFFLE
                    - h5z.FILTER_FLETCHER32
                    - h5z.FILTER_SZIP
        
                flags
                    Bit flags (h5z.FLAG*) setting filter properties
        
                values
                    TUPLE of UINTs giving auxiliary data for the filter
        """
        pass

    def set_fletcher32(self, *args, **kwargs): # real signature unknown
        """
        ()
        
                Enable Fletcher32 error correction on this list.
        """
        pass

    def set_layout(self, *args, **kwargs): # real signature unknown
        """
        (INT layout_code)
        
                Set dataset storage strategy; legal values are:
        
                - h5d.COMPACT
                - h5d.CONTIGUOUS
                - h5d.CHUNKED
                - h5d.VIRTUAL (If using HDF5 library version 1.10 or later)
        """
        pass

    def set_scaleoffset(self, *args, **kwargs): # real signature unknown
        """
        (H5Z_SO_scale_type_t scale_type, INT scale_factor)
        
                Enable scale/offset (usually lossy) compression; lossless (e.g. gzip)
                compression and other filters may be applied on top of this.
        
                Note that error detection (i.e. fletcher32) cannot precede this in
                the filter chain, or else all reads on lossily-compressed data will
                fail.
        """
        pass

    def set_shuffle(self, *args, **kwargs): # real signature unknown
        """
        ()
        
                Enable to use of the shuffle filter.  Use this immediately before
                the deflate filter to increase the compression ratio.
        """
        pass

    def set_szip(self, *args, **kwargs): # real signature unknown
        """
        (UINT options, UINT pixels_per_block)
        
                Enable SZIP compression.  See the HDF5 docs for argument meanings,
                and general restrictions on use of the SZIP format.
        """
        pass

    def set_virtual(self, *args, **kwargs): # real signature unknown
        """
        (SpaceID vspace, STR src_file_name, STR src_dset_name, SpaceID src_space)
        
                    Set the mapping between virtual and source datasets.
        
                    The virtual dataset is described by its virtual dataspace (vspace)
                    to the elements. The source dataset is described by the name of the
                    file where it is located (src_file_name), the name of the dataset
                    (src_dset_name) and its dataspace (src_space).
        """
        pass

    def _has_filter(self, *args, **kwargs): # real signature unknown
        """
        (INT filter_code)
        
                Slow & stupid method to determine if a filter is used in this
                property list.  Used because the HDF5 function H5Pget_filter_by_id
                is broken.
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


class PropDXID(PropInstanceID):
    """ Data transfer property list """
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


class PropFAID(PropInstanceID):
    """ File access property list """
    def get_alignment(self, *args, **kwargs): # real signature unknown
        """ Retrieves the current settings for alignment properties from a file access property list. """
        pass

    def get_cache(self, *args, **kwargs): # real signature unknown
        """
        () => TUPLE cache info
        
                Get the metadata and raw data chunk cache settings.  See the HDF5
                docs for element definitions.  Return is a 4-tuple with entries:
        
                1. INT mdc:              Number of metadata objects
                2. INT rdcc:             Number of raw data chunks
                3. UINT rdcc_nbytes:     Size of raw data cache
                4. DOUBLE rdcc_w0:       Preemption policy for data cache.
        """
        pass

    def get_driver(self, *args, **kwargs): # real signature unknown
        """
        () => INT driver code
        
                Return an integer identifier for the driver used by this list.
                Although HDF5 implements these as full-fledged objects, they are
                treated as integers by Python.  Built-in drivers identifiers are
                listed in module h5fd; they are:
        
                - h5fd.CORE
                - h5fd.FAMILY
                - h5fd.LOG
                - h5fd.MPIO
                - h5fd.MULTI
                - h5fd.SEC2
                - h5fd.STDIO
        """
        pass

    def get_fapl_core(self, *args, **kwargs): # real signature unknown
        """
        () => TUPLE core_settings
        
                Determine settings for the h5fd.CORE (memory-resident) file driver.
                Tuple elements are:
        
                0. UINT "increment": Chunk size for new memory requests
                1. BOOL "backing_store": If True, write the memory contents to
                   disk when the file is closed.
        """
        pass

    def get_fapl_family(self, *args, **kwargs): # real signature unknown
        """
        () => TUPLE info
        
                Determine family driver settings. Tuple values are:
        
                0. UINT memb_size
                1. PropFAID memb_fapl or None
        """
        pass

    def get_fclose_degree(self, *args, **kwargs): # real signature unknown
        """
        () => INT close_degree
                - h5fd.
                Get the file-close degree, which determines library behavior when
                a file is closed when objects are still open.  Legal values:
        
                * h5f.CLOSE_WEAK
                * h5f.CLOSE_SEMI
                * h5f.CLOSE_STRONG
                * h5f.CLOSE_DEFAULT
        """
        pass

    def get_libver_bounds(self, *args, **kwargs): # real signature unknown
        """
        () => (INT low, INT high)
        
                Get the compatibility level for file format. Returned values are from:
        
                - h5f.LIBVER_EARLIEST
                - h5f.LIBVER_LATEST
        """
        pass

    def get_mdc_config(self, *args, **kwargs): # real signature unknown
        """
        () => CacheConfig
                Returns an object that stores all the information about the meta-data cache
                configuration
        """
        pass

    def get_sieve_buf_size(self, *args, **kwargs): # real signature unknown
        """
        () => UINT size
        
                Get the current maximum size of the data sieve buffer (in bytes).
        """
        pass

    def set_alignment(self, *args, **kwargs): # real signature unknown
        """ Sets alignment properties of a file access property list. """
        pass

    def set_cache(self, *args, **kwargs): # real signature unknown
        """
        (INT mdc, INT rdcc, UINT rdcc_nbytes, DOUBLE rdcc_w0)
        
                Set the metadata (mdc) and raw data chunk (rdcc) cache properties.
                See the HDF5 docs for a full explanation.
        """
        pass

    def set_driver(self, *args, **kwargs): # real signature unknown
        """
        (INT driver_id)
        
                Sets the file driver identifier for this file access or data
                transfer property list.
        """
        pass

    def set_fapl_core(self, *args, **kwargs): # real signature unknown
        """
        (UINT increment=64k, BOOL backing_store=True)
        
                Use the h5fd.CORE (memory-resident) file driver.
        
                increment
                    Chunk size for new memory requests (default 1 meg)
        
                backing_store
                    If True (default), memory contents are associated with an
                    on-disk file, which is updated when the file is closed.
                    Set to False for a purely in-memory file.
        """
        pass

    def set_fapl_family(self, *args, **kwargs): # real signature unknown
        """
        (UINT memb_size=2**31-1, PropFAID memb_fapl=None)
        
                Set up the family driver.
        
                memb_size
                    Member file size
        
                memb_fapl
                    File access property list for each member access
        """
        pass

    def set_fapl_log(self, *args, **kwargs): # real signature unknown
        """
        (STRING logfile, UINT flags, UINT buf_size)
        
                Enable the use of the logging driver.  See the HDF5 documentation
                for details.  Flag constants are stored in module h5fd.
        """
        pass

    def set_fapl_sec2(self, *args, **kwargs): # real signature unknown
        """
        ()
        
                Select the "section-2" driver (h5fd.SEC2).
        """
        pass

    def set_fapl_stdio(self, *args, **kwargs): # real signature unknown
        """
        ()
        
                Select the "stdio" driver (h5fd.STDIO)
        """
        pass

    def set_fclose_degree(self, *args, **kwargs): # real signature unknown
        """
        (INT close_degree)
        
                Set the file-close degree, which determines library behavior when
                a file is closed when objects are still open.  Legal values:
        
                * h5f.CLOSE_WEAK
                * h5f.CLOSE_SEMI
                * h5f.CLOSE_STRONG
                * h5f.CLOSE_DEFAULT
        """
        pass

    def set_fileobj_driver(self, *args, **kwargs): # real signature unknown
        """
        (INT driver_id, OBJECT fileobj)
        
                Select the "fileobj" file driver (h5py-specific).
        """
        pass

    def set_file_image(self, *args, **kwargs): # real signature unknown
        """
        Copy a file image into the property list. Passing None releases
                    any image currently loaded. The parameter image must either be
                    None or support the buffer protocol.
        """
        pass

    def set_libver_bounds(self, *args, **kwargs): # real signature unknown
        """
        (INT low, INT high)
        
                Set the compatibility level for file format.  Legal values are:
        
                - h5f.LIBVER_EARLIEST
                - h5f.LIBVER_LATEST
        """
        pass

    def set_mdc_config(self, *args, **kwargs): # real signature unknown
        """
        (CacheConfig) => None
                Returns an object that stores all the information about the meta-data cache
                configuration
        """
        pass

    def set_sieve_buf_size(self, *args, **kwargs): # real signature unknown
        """
        (UINT size)
        
                Set the maximum size of the data sieve buffer (in bytes).  This
                buffer can improve I/O performance for hyperslab I/O, by combining
                reads and writes into blocks of the given size.  The default is 64k.
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


class PropFCID(PropOCID):
    """ File creation property list. """
    def get_link_creation_order(self, *args, **kwargs): # real signature unknown
        """
        () -> UINT flags
        
                Get tracking and indexing of creation order for links added to this group
        """
        pass

    def get_sizes(self, *args, **kwargs): # real signature unknown
        """
        () => TUPLE sizes
        
                Determine addressing offsets and lengths for objects in an
                HDF5 file, in bytes.  Return value is a 2-tuple with values:
        
                0.  UINT Address offsets
                1.  UINT Lengths
        """
        pass

    def get_userblock(self, *args, **kwargs): # real signature unknown
        """
        () => LONG size
        
                Determine the user block size, in bytes.
        """
        pass

    def get_version(self, *args, **kwargs): # real signature unknown
        """
        () => TUPLE version_info
        
                Determine version information of various file attributes.
                Elements are:
        
                0.  UINT Super block version number
                1.  UINT Freelist version number
                2.  UINT Symbol table version number
                3.  UINT Shared object header version number
        """
        pass

    def set_link_creation_order(self, *args, **kwargs): # real signature unknown
        """
        (UINT flags)
        
                Set tracking and indexing of creation order for links added to this group
        
                flags -- h5p.CRT_ORDER_TRACKED, h5p.CRT_ORDER_INDEXED
        """
        pass

    def set_sizes(self, *args, **kwargs): # real signature unknown
        """
        (UINT addr, UINT size)
        
                Set the addressing offsets and lengths for objects
                in an HDF5 file, in bytes.
        """
        pass

    def set_userblock(self, *args, **kwargs): # real signature unknown
        """
        (INT/LONG size)
        
                Set the file user block size, in bytes.
                Must be a power of 2, and at least 512.
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


class PropGCID(PropOCID):
    """ Group creation property list """
    def get_link_creation_order(self, *args, **kwargs): # real signature unknown
        """
        () -> UINT flags
        
                Get tracking and indexing of creation order for links added to this group
        """
        pass

    def set_link_creation_order(self, *args, **kwargs): # real signature unknown
        """
        (UINT flags)
        
                Set tracking and indexing of creation order for links added to this group
        
                flags -- h5p.CRT_ORDER_TRACKED, h5p.CRT_ORDER_INDEXED
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


class PropLAID(PropInstanceID):
    """ Link access property list """
    def get_elink_fapl(self, *args, **kwargs): # real signature unknown
        """
        () => PropFAID fapl
        
                Get the file access property list used when opening external files.
        """
        pass

    def get_elink_prefix(self, *args, **kwargs): # real signature unknown
        """
        () => STRING prefix
        
                Get the external link prefix
        """
        pass

    def get_nlinks(self, *args, **kwargs): # real signature unknown
        """
        () => UINT
        
                Get the maximum traversal depth for soft links
        """
        pass

    def set_elink_fapl(self, *args, **kwargs): # real signature unknown
        """
        (PropFAID fapl)
        
                Set the file access property list used when opening external files.
        """
        pass

    def set_elink_prefix(self, *args, **kwargs): # real signature unknown
        """
        (STRING prefix)
        
                Set the external link prefix.
        """
        pass

    def set_nlinks(self, *args, **kwargs): # real signature unknown
        """
        (UINT nlinks)
        
                Set the maximum traversal depth for soft links
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


class PropLCID(PropCreateID):
    """ Link creation property list """
    def get_char_encoding(self, *args, **kwargs): # real signature unknown
        """
        () => INT encoding
        
                Get the character encoding for link names.  Legal values are:
        
                - h5t.CSET_ASCII
                - h5t.CSET_UTF8
        """
        pass

    def get_create_intermediate_group(self, *args, **kwargs): # real signature unknown
        """
        () => BOOL
        
                Determine if missing intermediate groups are automatically created.
        """
        pass

    def set_char_encoding(self, *args, **kwargs): # real signature unknown
        """
        (INT encoding)
        
                Set the character encoding for link names.  Legal values are:
        
                - h5t.CSET_ASCII
                - h5t.CSET_UTF8
        """
        pass

    def set_create_intermediate_group(self, *args, **kwargs): # real signature unknown
        """
        (BOOL create)
        
                Set whether missing intermediate groups are automatically created.
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


# variables with complex values

DATASET_ACCESS = None # (!) real value is '<h5py.h5p.PropClassID object at 0x00000213240DF2C8>'

DATASET_CREATE = None # (!) real value is '<h5py.h5p.PropClassID object at 0x00000213240DF188>'

DATASET_XFER = None # (!) real value is '<h5py.h5p.PropClassID object at 0x00000213240DF228>'

FILE_ACCESS = None # (!) real value is '<h5py.h5p.PropClassID object at 0x00000213240DF098>'

FILE_CREATE = None # (!) real value is '<h5py.h5p.PropClassID object at 0x00000213240DF0E8>'

GROUP_CREATE = None # (!) real value is '<h5py.h5p.PropClassID object at 0x00000213240DF548>'

LINK_ACCESS = None # (!) real value is '<h5py.h5p.PropClassID object at 0x00000213240DF4A8>'

LINK_CREATE = None # (!) real value is '<h5py.h5p.PropClassID object at 0x00000213240DF408>'

NO_CLASS = None # (!) real value is '<h5py.h5p.PropClassID object at 0x00000213240D0E58>'

OBJECT_COPY = None # (!) real value is '<h5py.h5p.PropClassID object at 0x00000213240DF368>'

OBJECT_CREATE = None # (!) real value is '<h5py.h5p.PropClassID object at 0x00000213240DF5E8>'

phil = _objects.phil

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000213240BDA90>'

__pyx_capi__ = {
    'pdefault': None, # (!) real value is '<capsule object "hid_t (struct __pyx_obj_4h5py_3h5p_PropID *)" at 0x00000213240D14E0>'
    'propwrap': None, # (!) real value is '<capsule object "PyObject *(hid_t)" at 0x00000213240D1510>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='h5py.h5p', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000213240BDA90>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\h5py\\\\h5p.cp37-win_amd64.pyd')"

__test__ = {}

