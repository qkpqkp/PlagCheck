# encoding: utf-8
# module h5py.h5l
# from C:\Users\Doly\Anaconda3\lib\site-packages\h5py\h5l.cp37-win_amd64.pyd
# by generator 1.147
"""
API for the "H5L" family of link-related operations.  Defines the class
    LinkProxy, which comes attached to GroupID objects as <obj>.links.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
from h5py._objects import with_phil


# Variables with simple values

TYPE_EXTERNAL = 64
TYPE_HARD = 0
TYPE_SOFT = 1

# functions

def __pyx_unpickle_LinkProxy(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle__LinkVisitor(*args, **kwargs): # real signature unknown
    pass

# classes

class LinkInfo(object):
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

    corder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ Creation order """

    corder_valid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ Indicates if the creation order is valid """

    cset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ Integer type code for character set (h5t.CSET_*) """

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ Integer type code for link (h5l.TYPE_*) """

    u = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ Either the address of a hard link or the size of a soft/UD link """



class LinkProxy(object):
    """
    Proxy class which provides access to the HDF5 "H5L" API.
    
            These come attached to GroupID objects as "obj.links".  Since every
            H5L function operates on at least one group, the methods provided
            operate on their parent group identifier.  For example::
    
                >>> g = h5g.open(fid, '/')
                >>> g.links.exists("MyGroup")
                True
                >>> g.links.exists("FooBar")
                False
    
            * Hashable: No
            * Equality: Undefined
    
            You will note that this class does *not* inherit from ObjectID.
    """
    def create_external(self, *args, **kwargs): # real signature unknown
        """
        (STRING link_name, STRING file_name, STRING obj_name,
                PropLCID lcpl=None, PropLAID lapl=None)
        
                Create a new external link, pointing to an object in another file.
        """
        pass

    def create_hard(self, *args, **kwargs): # real signature unknown
        """
        (STRING new_name, GroupID cur_loc, STRING cur_name,
                PropID lcpl=None, PropID lapl=None)
        
                Create a new hard link in this group pointing to an existing link
                in another group.
        """
        pass

    def create_soft(self, *args, **kwargs): # real signature unknown
        """
        (STRING new_name, STRING target, PropID lcpl=None, PropID lapl=None)
        
                Create a new soft link in this group, with the given string value.
                The link target does not need to exist.
        """
        pass

    def exists(self, *args, **kwargs): # real signature unknown
        """
        (STRING name, PropID lapl=None) => BOOL
        
                    Check if a link of the specified name exists in this group.
        """
        pass

    def get_info(self, *args, **kwargs): # real signature unknown
        """
        (STRING name=, INT index=, **kwds) => LinkInfo instance
        
                Get information about a link, either by name or its index.
        
                Keywords:
        """
        pass

    def get_val(self, *args, **kwargs): # real signature unknown
        """
        (STRING name, PropLAID lapl=None) => STRING or TUPLE(file, obj)
        
                Get the string value of a soft link, or a 2-tuple representing
                the contents of an external link.
        """
        pass

    def iterate(self, *args, **kwargs): # real signature unknown
        """
        (CALLABLE func, **kwds) => <Return value from func>, <index to restart at>
        
                Iterate a function or callable object over all groups in this
                one.  Your callable should conform to the signature::
        
                    func(STRING name) => Result
        
                or if the keyword argument "info" is True::
        
                    func(STRING name, LinkInfo info) => Result
        
                Returning None or a logical False continues iteration; returning
                anything else aborts iteration and returns that value.
        
                BOOL info (False)
                    Provide a LinkInfo instance to callback
        
                STRING obj_name (".")
                    Visit this subgroup instead
        
                PropLAID lapl (None)
                    Link access property list for "obj_name"
        
                INT idx_type (h5.INDEX_NAME)
        
                INT order (h5.ITER_INC)
        
                hsize_t idx (0)
                    The index to start iterating at
        """
        pass

    def move(self, *args, **kwargs): # real signature unknown
        """
        (STRING src_name, GroupID dst_loc, STRING dst_name)
        
                Move a link to a new location in the file.
        """
        pass

    def visit(self, *args, **kwargs): # real signature unknown
        """
        (CALLABLE func, **kwds) => <Return value from func>
        
                Iterate a function or callable object over all groups below this
                one.  Your callable should conform to the signature::
        
                    func(STRING name) => Result
        
                or if the keyword argument "info" is True::
        
                    func(STRING name, LinkInfo info) => Result
        
                Returning None or a logical False continues iteration; returning
                anything else aborts iteration and returns that value.
        
                BOOL info (False)
                    Provide a LinkInfo instance to callback
        
                STRING obj_name (".")
                    Visit this subgroup instead
        
                PropLAID lapl (None)
                    Link access property list for "obj_name"
        
                INT idx_type (h5.INDEX_NAME)
        
                INT order (h5.ITER_INC)
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


class _LinkVisitor(object):
    """ Helper class for iteration callback """
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

phil = None # (!) real value is '<h5py._objects.FastRLock object at 0x000002F4D2604288>'

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000002F4E1008EB8>'

__spec__ = None # (!) real value is "ModuleSpec(name='h5py.h5l', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000002F4E1008EB8>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\h5py\\\\h5l.cp37-win_amd64.pyd')"

__test__ = {}

