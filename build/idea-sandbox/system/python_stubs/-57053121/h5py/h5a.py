# encoding: utf-8
# module h5py.h5a
# from C:\Users\Doly\Anaconda3\lib\site-packages\h5py\h5a.cp37-win_amd64.pyd
# by generator 1.147
""" Provides access to the low-level HDF5 "H5A" attribute interface. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import h5py._objects as _objects # C:\Users\Doly\Anaconda3\lib\site-packages\h5py\_objects.cp37-win_amd64.pyd
from h5py._objects import (create, delete, exists, get_info, get_num_attrs, 
    iterate, open, rename, with_phil)

import h5py._objects as __h5py__objects


# functions

def __pyx_unpickle_AttrID(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle__AttrVisitor(*args, **kwargs): # real signature unknown
    pass

# classes

class AttrID(__h5py__objects.ObjectID):
    """
    Logical representation of an HDF5 attribute identifier.
    
            Objects of this class can be used in any HDF5 function call
            which expects an attribute identifier.  Additionally, all ``H5A*``
            functions which always take an attribute instance as the first
            argument are presented as methods of this class.
    
            * Hashable: No
            * Equality: Identifier comparison
    """
    def get_name(self, *args, **kwargs): # real signature unknown
        """
        () => STRING name
        
                Determine the name of this attribute.
        """
        pass

    def get_space(self, *args, **kwargs): # real signature unknown
        """
        () => SpaceID
        
                Create and return a copy of the attribute's dataspace.
        """
        pass

    def get_storage_size(self, *args, **kwargs): # real signature unknown
        """
        () => INT
        
                Get the amount of storage required for this attribute.
        """
        pass

    def get_type(self, *args, **kwargs): # real signature unknown
        """
        () => TypeID
        
                Create and return a copy of the attribute's datatype.
        """
        pass

    def read(self, *args, **kwargs): # real signature unknown
        """
        (NDARRAY arr, TypeID mtype=None)
        
                Read the attribute data into the given Numpy array.  Note that the
                Numpy array must have the same shape as the HDF5 attribute, and a
                conversion-compatible datatype.
        
                The Numpy array must be writable and C-contiguous.  If this is not
                the case, the read will fail with an exception.
        
                If provided, the HDF5 TypeID mtype will override the array's dtype.
        """
        pass

    def write(self, *args, **kwargs): # real signature unknown
        """
        (NDARRAY arr)
        
                Write the contents of a Numpy array too the attribute.  Note that
                the Numpy array must have the same shape as the HDF5 attribute, and
                a conversion-compatible datatype.
        
                The Numpy array must be C-contiguous.  If this is not the case,
                the write will fail with an exception.
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
    """A Numpy-stype dtype object representing the attribute's datatype"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The attribute's name"""

    shape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A Numpy-style shape tuple representing the attribute's dataspace"""



class AttrInfo(object):
    # no doc
    def _hash(self, *args, **kwargs): # real signature unknown
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

    corder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Creation order"""

    corder_valid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if the creation order is valid"""

    cset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Character set of attribute name (integer typecode from h5t)"""

    data_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Size of raw data"""



class _AttrVisitor(object):
    # no doc
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

phil = _objects.phil

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000016D48BED438>'

__spec__ = None # (!) real value is "ModuleSpec(name='h5py.h5a', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000016D48BED438>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\h5py\\\\h5a.cp37-win_amd64.pyd')"

__test__ = {}

