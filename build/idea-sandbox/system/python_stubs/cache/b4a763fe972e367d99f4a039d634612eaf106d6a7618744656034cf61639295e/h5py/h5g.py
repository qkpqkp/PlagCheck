# encoding: utf-8
# module h5py.h5g
# from C:\Users\Doly\Anaconda3\lib\site-packages\h5py\h5g.cp37-win_amd64.pyd
# by generator 1.147
""" Low-level HDF5 "H5G" group interface. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import h5py._objects as _objects # C:\Users\Doly\Anaconda3\lib\site-packages\h5py\_objects.cp37-win_amd64.pyd
from h5py._objects import (_path_valid, create, get_objinfo, iterate, open, 
    with_phil)

import h5py._objects as __h5py__objects


# Variables with simple values

CRT_ORDER_TRACKED = 1

DATASET = 1

GROUP = 0

LINK = 3

LINK_ERROR = -1
LINK_HARD = 0
LINK_SOFT = 1

TYPE = 2

UNKNOWN = -1

# functions

def __pyx_unpickle_GroupID(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_GroupIter(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle__GroupVisitor(*args, **kwargs): # real signature unknown
    pass

# classes

class GroupID(__h5py__objects.ObjectID):
    """
    Represents an HDF5 group identifier
    
            Python extensions:
    
            __contains__
                Test for group member ("if name in grpid")
    
            __iter__
                Get an iterator over member names
    
            __len__
                Number of members in this group; len(grpid) = N
    
            If HDF5 1.8.X is used, the attribute "links" contains a proxy object
            providing access to the H5L family of routines.  See the docs
            for h5py.h5l.LinkProxy for more information.
    
            * Hashable: Yes, unless anonymous
            * Equality: True HDF5 identity unless anonymous
    """
    def get_comment(self, *args, **kwargs): # real signature unknown
        """
        (STRING name) => STRING comment
        
                Retrieve the comment for a group member.
        """
        pass

    def get_create_plist(self, *args, **kwargs): # real signature unknown
        """
        () => PropGCID
        
                Retrieve a copy of the group creation property list used to
                create this group.
        """
        pass

    def get_linkval(self, *args, **kwargs): # real signature unknown
        """
        (STRING name) => STRING link_value
        
                Retrieve the value (target name) of a symbolic link.
                Limited to 2048 characters on Windows.
        """
        pass

    def get_num_objs(self, *args, **kwargs): # real signature unknown
        """
        () => INT number_of_objects
        
                Get the number of objects directly attached to a given group.
        """
        pass

    def get_objname_by_idx(self, *args, **kwargs): # real signature unknown
        """
        (INT idx) => STRING
        
                Get the name of a group member given its zero-based index.
        """
        pass

    def get_objtype_by_idx(self, *args, **kwargs): # real signature unknown
        """
        (INT idx) => INT object_type_code
        
                Get the type of an object attached to a group, given its zero-based
                index.  Possible return values are:
        
                - LINK
                - GROUP
                - DATASET
                - TYPE
        """
        pass

    def link(self, *args, **kwargs): # real signature unknown
        """
        (STRING current_name, STRING new_name, INT link_type=LINK_HARD,
                GroupID remote=None)
        
                Create a new hard or soft link.  current_name identifies
                the link target (object the link will point to).  The new link is
                identified by new_name and (optionally) another group "remote".
        
                Link types are:
        
                LINK_HARD
                    Hard link to existing object (default)
        
                LINK_SOFT
                    Symbolic link; link target need not exist.
        """
        pass

    def move(self, *args, **kwargs): # real signature unknown
        """
        (STRING current_name, STRING new_name, GroupID remote=None)
        
                Relink an object.  current_name identifies the object.
                new_name and (optionally) another group "remote" determine
                where it should be moved.
        """
        pass

    def set_comment(self, *args, **kwargs): # real signature unknown
        """
        (STRING name, STRING comment)
        
                Set the comment on a group member.
        """
        pass

    def unlink(self, *args, **kwargs): # real signature unknown
        """
        (STRING name)
        
                Remove a link to an object from this group.
        """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """
        (STRING name)
        
                Determine if a group member of the given name is present
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Return an iterator over the names of group members. """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Number of group members """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    links = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class GroupIter(object):
    """
    Iterator over the names of group members.  After this iterator is
            exhausted, it releases its reference to the group ID.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass


class GroupStat(object):
    """
    Represents the H5G_stat_t structure containing group member info.
    
        Fields (read-only):
    
        * fileno:   2-tuple uniquely identifying the current file
        * objno:    2-tuple uniquely identifying this object
        * nlink:    Number of hard links to this object
        * mtime:    Modification time of this object
        * linklen:  Length of the symbolic link name, or 0 if not a link.
    
        "Uniquely identifying" means unique among currently open files,
        not universally unique.
    
        * Hashable: Yes
        * Equality: Yes
    """
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

    fileno = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    linklen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mtime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nlink = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    objno = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class _GroupVisitor(object):
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

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000002A87491DD30>'

__spec__ = None # (!) real value is "ModuleSpec(name='h5py.h5g', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000002A87491DD30>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\h5py\\\\h5g.cp37-win_amd64.pyd')"

__test__ = {}

